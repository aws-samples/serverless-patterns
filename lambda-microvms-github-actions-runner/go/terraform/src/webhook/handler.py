"""GitHub webhook handler: verifies the HMAC signature, mints a JIT runner config
for each queued workflow_job that requests all runner labels, and launches one
MicroVM for it.
"""

import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.request

import boto3

RUNNER_SCOPE = os.environ.get("RUNNER_SCOPE", "repo")
GITHUB_OWNER = os.environ["GITHUB_OWNER"]
GITHUB_REPO = os.environ.get("GITHUB_REPO", "")
GITHUB_ORG = os.environ.get("GITHUB_ORG", "")
RUNNER_LABELS = os.environ.get("RUNNER_LABELS", "self-hosted,lambda").split(",")
RUNNER_GROUP_ID = int(os.environ.get("RUNNER_GROUP_ID", "1"))
PAT_SECRET_ARN = os.environ["PAT_SECRET_ARN"]
WEBHOOK_SECRET_ARN = os.environ["WEBHOOK_SECRET_ARN"]
# Lets a rotated PAT or webhook secret take effect without recycling the function.
SECRET_CACHE_TTL = int(os.environ.get("SECRET_CACHE_TTL_SECONDS", "300"))

# No imageVersion is passed to RunMicrovm, so it uses the latest active version.
MICROVM_IMAGE_ARN = os.environ["MICROVM_IMAGE_ARN"]
MICROVM_EXECUTION_ROLE_ARN = os.environ["MICROVM_EXECUTION_ROLE_ARN"]
MICROVM_MAX_DURATION_SECONDS = int(os.environ.get("MICROVM_MAX_DURATION_SECONDS", "900"))
JIT_BUCKET = os.environ["JIT_BUCKET"]
JIT_KEY_PREFIX = os.environ.get("JIT_KEY_PREFIX", "jit")
JIT_URL_TTL = int(os.environ.get("JIT_URL_TTL", "60"))  # presigned URL lifetime (s)
LOG_GROUP = os.environ.get("MICROVM_LOG_GROUP", "")
REGION = os.environ.get("AWS_REGION", "us-east-1")

# The runner only dials out, so it needs no ingress.
_NO_INGRESS = f"arn:aws:lambda:{REGION}:aws:network-connector:aws-network-connector:NO_INGRESS"
_INTERNET_EGRESS = f"arn:aws:lambda:{REGION}:aws:network-connector:aws-network-connector:INTERNET_EGRESS"

_secrets = boto3.client("secretsmanager")
_s3 = boto3.client("s3")
_microvms = boto3.client("lambda-microvms")

# arn -> (value, monotonic time fetched)
_cache: dict[str, tuple[str, float]] = {}


class SafeError(Exception):
    """A failure whose message is safe to log: never secrets, headers or bodies."""


def _err(e: Exception) -> str:
    """Exception type + AWS error code only (str(e) can echo request data)."""
    code = getattr(e, "response", {}).get("Error", {}).get("Code", "")
    return f"{type(e).__name__} {code}".strip()


def _secret(arn: str) -> str:
    """Secret value, whitespace-stripped (a stored trailing newline breaks the
    Authorization header). Raises SafeError if it can't be read or is empty."""
    now = time.monotonic()
    cached = _cache.get(arn)
    if cached is not None and now - cached[1] < SECRET_CACHE_TTL:
        return cached[0]
    try:
        value = _secrets.get_secret_value(SecretId=arn)["SecretString"].strip()
    except Exception as e:  # noqa: BLE001 — log type/code only, never the value
        if cached is not None:
            print(f"[webhook] WARN: reading secret {arn} failed ({_err(e)}); using cached value")
            return cached[0]
        raise SafeError(f"reading secret {arn} failed ({_err(e)})") from None
    if not value:
        raise SafeError(f"secret {arn} is empty; store a value (see README.md)")
    _cache[arn] = (value, now)
    return value


def _verify_signature(body: bytes, signature_header: str) -> bool:
    if not signature_header:
        return False
    secret = _secret(WEBHOOK_SECRET_ARN).encode()
    expected = "sha256=" + hmac.new(secret, body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature_header)


def _generate_jitconfig(runner_name: str) -> str:
    """Return the base64 JIT config from GitHub generate-jitconfig.

    Raises SafeError without chaining: urllib errors can embed the PAT header.
    """
    if RUNNER_SCOPE == "org":
        path = f"/orgs/{GITHUB_ORG}/actions/runners/generate-jitconfig"
    else:
        path = f"/repos/{GITHUB_OWNER}/{GITHUB_REPO}/actions/runners/generate-jitconfig"
    url = f"https://api.github.com{path}"

    payload = json.dumps(
        {
            "name": runner_name,
            "runner_group_id": RUNNER_GROUP_ID,
            "labels": RUNNER_LABELS,
            "work_folder": "/tmp/_work",
        }
    ).encode()

    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Authorization", f"Bearer {_secret(PAT_SECRET_ARN)}")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        return data["encoded_jit_config"]
    except urllib.error.HTTPError as e:
        # The response body is never read or logged.
        if e.code in (401, 403):
            # Bad or rotated PAT: refetch it on the next invocation.
            _cache.pop(PAT_SECRET_ARN, None)
        raise SafeError(f"POST {path} failed: HTTP {e.code} {e.reason}") from None
    except Exception as e:  # noqa: BLE001 — type only; str(e) may hold the header
        raise SafeError(f"POST {path} failed ({type(e).__name__})") from None


def _labels_match(requested: list[str]) -> bool:
    """True only if the job requested all of our runner labels."""
    return all(label in requested for label in RUNNER_LABELS)


def handler(event, _context):
    body = event.get("body", "")
    if event.get("isBase64Encoded"):
        import base64

        raw = base64.b64decode(body)
    else:
        raw = body.encode() if isinstance(body, str) else body

    headers = {k.lower(): v for k, v in (event.get("headers") or {}).items()}

    try:
        signature_ok = _verify_signature(raw, headers.get("x-hub-signature-256", ""))
    except SafeError as e:
        print(f"[webhook] ERROR: {e}")
        return {"statusCode": 500, "body": "internal error"}
    if not signature_ok:
        return {"statusCode": 401, "body": "invalid signature"}

    gh_event = headers.get("x-github-event", "")
    if gh_event == "ping":
        return {"statusCode": 200, "body": "pong"}
    if gh_event != "workflow_job":
        return {"statusCode": 204, "body": "ignored event"}

    parsed = json.loads(raw)
    if parsed.get("action") != "queued":
        return {"statusCode": 204, "body": "ignored action"}

    requested = parsed.get("workflow_job", {}).get("labels", [])
    if not _labels_match(requested):
        return {"statusCode": 204, "body": "labels do not match"}

    job_id = parsed.get("workflow_job", {}).get("id", "unknown")
    runner_name = f"lambda-jit-{job_id}"

    try:
        jitconfig = _generate_jitconfig(runner_name)
    except SafeError as e:
        print(f"[webhook] ERROR: job {job_id}: {e}")
        return {"statusCode": 500, "body": "internal error"}

    # The JIT config exceeds the 4096-char run-hook-payload limit, so pass a
    # short-lived presigned URL instead. The URL is a bearer credential for it.
    jit_key = f"{JIT_KEY_PREFIX}/{job_id}-{int(time.time())}"
    try:
        _s3.put_object(Bucket=JIT_BUCKET, Key=jit_key, Body=jitconfig.encode())
        presigned_url = _s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": JIT_BUCKET, "Key": jit_key},
            ExpiresIn=JIT_URL_TTL,
        )
    except Exception as e:  # noqa: BLE001 — type/code only, never the JIT config
        print(f"[webhook] ERROR: job {job_id}: storing JIT config failed ({_err(e)})")
        return {"statusCode": 500, "body": "internal error"}

    run_kwargs = {
        "imageIdentifier": MICROVM_IMAGE_ARN,
        "executionRoleArn": MICROVM_EXECUTION_ROLE_ARN,
        "ingressNetworkConnectors": [_NO_INGRESS],
        "egressNetworkConnectors": [_INTERNET_EGRESS],
        "maximumDurationInSeconds": MICROVM_MAX_DURATION_SECONDS,
        "runHookPayload": presigned_url,
    }
    if LOG_GROUP:
        run_kwargs["logging"] = {
            "cloudWatch": {"logGroup": LOG_GROUP, "logStream": f"job-{job_id}-{int(time.time())}"}
        }
    try:
        resp = _microvms.run_microvm(**run_kwargs)
    except Exception as e:  # noqa: BLE001 — type/code only; str(e) may echo the pre-signed URL
        print(f"[webhook] ERROR: job {job_id}: RunMicrovm failed ({_err(e)})")
        return {"statusCode": 500, "body": "internal error"}
    microvm_id = resp.get("microvmId", "unknown")

    # Never log the presigned URL; log the key only.
    print(f"[webhook] launched {microvm_id} for job {job_id} (runner {runner_name}, jit s3 key {jit_key})")
    return {"statusCode": 202, "body": f"launched {microvm_id}"}
