"""
Thin wrapper around the Lambda MicroVMs control plane.

All calls to the `lambda-microvms` service live here. Operation names and
payloads were verified against the service model shipped with the AWS CLI
(`lambda-microvms` 2025-09-09): run_microvm, create_microvm_auth_token,
terminate_microvm.

IMPORTANT — model loading:
`lambda-microvms` is a newer service that is NOT in the boto3/botocore version
bundled with the Lambda runtime, so `boto3.client("lambda-microvms")` raises
"Unknown service". We fix this by vendoring the botocore service model into
this package (middleware/botocore_models/) and pointing botocore at it via
AWS_DATA_PATH *before* the first client is created. This is the standard,
supported mechanism for teaching boto3 about an out-of-band service model.
"""

from __future__ import annotations

import json
import logging
import os

# --- Register the vendored lambda-microvms service model BEFORE importing or
# --- using boto3 clients. AWS_DATA_PATH is read by botocore at client build.
_MODELS_DIR = os.path.join(os.path.dirname(__file__), "botocore_models")
if os.path.isdir(_MODELS_DIR):
    _existing = os.environ.get("AWS_DATA_PATH", "")
    if _MODELS_DIR not in _existing.split(os.pathsep):
        os.environ["AWS_DATA_PATH"] = (
            f"{_MODELS_DIR}{os.pathsep}{_existing}" if _existing else _MODELS_DIR
        )

import boto3  # noqa: E402  (import after AWS_DATA_PATH is set)

logger = logging.getLogger(__name__)

REGION = os.environ.get("AWS_REGION", "us-east-1")

# Network connectors + logging are static for this demo; pulled from env so
# the Lambda can be reconfigured without code changes.
INGRESS_CONNECTOR = os.environ.get(
    "INGRESS_CONNECTOR",
    f"arn:aws:lambda:{REGION}:aws:network-connector:aws-network-connector:HTTP_INGRESS",
)
EGRESS_CONNECTOR = os.environ.get(
    "EGRESS_CONNECTOR",
    f"arn:aws:lambda:{REGION}:aws:network-connector:aws-network-connector:INTERNET_EGRESS",
)
LOG_GROUP = os.environ.get("MICROVM_LOG_GROUP", "/aws/lambda-microvms/state-persistence-demo")
APP_PORT = int(os.environ.get("APP_PORT", "8080"))


def _client():
    return boto3.client("lambda-microvms", region_name=REGION)


def run_microvm(
    image_arn: str,
    image_version: str,
    execution_role_arn: str,
    client_id: str,
    state_bucket: str,
) -> dict:
    """
    Launch a new MicroVM for a client. The run-hook payload carries the
    clientId + stateBucket, which the /run hook uses to restore the last
    session's notes and files from S3.

    Returns {"microvmId": str, "endpoint": str}.
    """
    run_hook_payload = json.dumps({"clientId": client_id, "stateBucket": state_bucket})

    resp = _client().run_microvm(
        imageIdentifier=image_arn,
        imageVersion=image_version,
        executionRoleArn=execution_role_arn,
        idlePolicy={
            "maxIdleDurationSeconds": 180,
            "suspendedDurationSeconds": 180,
            "autoResumeEnabled": True,
        },
        ingressNetworkConnectors=[INGRESS_CONNECTOR],
        egressNetworkConnectors=[EGRESS_CONNECTOR],
        logging={"cloudWatch": {"logGroup": LOG_GROUP}},
        runHookPayload=run_hook_payload,
    )
    logger.info("Launched MicroVM %s at %s", resp["microvmId"], resp["endpoint"])
    return {"microvmId": resp["microvmId"], "endpoint": resp["endpoint"]}


def get_microvm(microvm_id: str) -> dict | None:
    """
    Fetch a MicroVM's current control-plane state.

    Returns {"state": str, "endpoint": str} where state is one of
    PENDING | RUNNING | SUSPENDING | SUSPENDED | TERMINATING | TERMINATED,
    or None if the MicroVM no longer exists (deleted / not found).
    """
    try:
        resp = _client().get_microvm(microvmIdentifier=microvm_id)
        return {"state": resp.get("state", ""), "endpoint": resp.get("endpoint", "")}
    except Exception as e:  # not found / terminated-and-reaped / transient
        logger.info("get_microvm(%s) returned no usable state: %s", microvm_id, e)
        return None


def create_auth_token(microvm_id: str, expiration_minutes: int = 30) -> dict:
    """
    Mint an ingress auth token scoped to the app port.

    Returns {"token": str, "expiresInMinutes": int}.
    """
    resp = _client().create_microvm_auth_token(
        microvmIdentifier=microvm_id,
        expirationInMinutes=expiration_minutes,
        allowedPorts=[{"port": APP_PORT}],
    )
    token = resp["authToken"]["X-aws-proxy-auth"]
    return {"token": token, "expiresInMinutes": expiration_minutes}


def terminate_microvm(microvm_id: str) -> None:
    """Terminate a MicroVM. The /terminate hook flushes state to S3 first."""
    try:
        _client().terminate_microvm(microvmIdentifier=microvm_id)
        logger.info("Terminated MicroVM %s", microvm_id)
    except Exception as e:  # pragma: no cover - best-effort cleanup
        logger.warning("terminate_microvm(%s) failed (ignoring): %s", microvm_id, e)
