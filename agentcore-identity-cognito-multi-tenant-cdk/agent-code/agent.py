"""Multi-tenant agent hosted on Amazon Bedrock AgentCore Runtime.

AgentCore Identity validates the inbound Cognito JWT before the request reaches
this code (via the runtime's custom JWT authorizer). This agent then derives the
caller's tenant from the validated token claims and exposes a single tool that
can only read that tenant's partition in DynamoDB. Because the tenant is fixed
from the token - not from the prompt - a user cannot coax the agent into reading
another tenant's data.
"""

import base64
import json
import logging
import os

import boto3
from boto3.dynamodb.conditions import Key
from strands import Agent, tool

from bedrock_agentcore import BedrockAgentCoreApp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REGION = os.environ.get("AWS_DEFAULT_REGION", "us-west-2")
TABLE_NAME = os.environ["TENANT_TABLE_NAME"]
TENANT_GROUP_PREFIX = os.environ.get("TENANT_GROUP_PREFIX", "tenant-")

app = BedrockAgentCoreApp()
table = boto3.resource("dynamodb", region_name=REGION).Table(TABLE_NAME)


def _decode_jwt_claims(token: str) -> dict:
    """Decode (do not re-verify) the JWT payload.

    AgentCore's inbound JWT authorizer has already verified the signature,
    issuer, audience/client, and expiry before invoking the agent, so here we
    only base64-decode the payload segment to read its claims.
    """
    payload_segment = token.split(".")[1]
    padding = "=" * (-len(payload_segment) % 4)
    decoded = base64.urlsafe_b64decode(payload_segment + padding)
    return json.loads(decoded)


class TenantResolutionError(Exception):
    """Raised when a caller cannot be mapped to exactly one tenant."""


def _extract_tenant(claims: dict) -> str:
    """Resolve the tenant id from the token's Cognito group membership.

    A caller must belong to *exactly one* tenant group. Zero groups means the
    user is not provisioned for any tenant; more than one is an ambiguous
    (and likely misconfigured) authorization state. Both are rejected rather
    than guessed, so the tenant boundary is never resolved arbitrarily.
    """
    groups = claims.get("cognito:groups", []) or []
    tenant_groups = [g for g in groups if g.startswith(TENANT_GROUP_PREFIX)]

    if not tenant_groups:
        raise TenantResolutionError(
            "No tenant group found in token. The user must belong to a "
            f"Cognito group prefixed with '{TENANT_GROUP_PREFIX}'."
        )
    if len(tenant_groups) > 1:
        raise TenantResolutionError(
            "Ambiguous tenant: the user belongs to multiple tenant groups "
            f"({tenant_groups}). A user must belong to exactly one tenant group."
        )
    return tenant_groups[0][len(TENANT_GROUP_PREFIX):]


@app.entrypoint
async def invoke(payload, context):
    prompt = payload.get(
        "prompt", "No prompt found in input, please provide a json payload with a 'prompt' key"
    )

    headers = context.request_headers or {}
    auth_header = headers.get("Authorization", "")
    token = auth_header[len("Bearer "):].strip() if auth_header.startswith("Bearer ") else ""

    if not token:
        yield {"error": "Missing bearer token"}
        return

    try:
        claims = _decode_jwt_claims(token)
    except Exception:  # noqa: BLE001 - defensive; malformed tokens
        logger.exception("Failed to decode token claims")
        yield {"error": "Invalid token"}
        return

    try:
        tenant_id = _extract_tenant(claims)
    except TenantResolutionError as exc:
        logger.warning("Tenant resolution failed: %s", exc)
        yield {"error": str(exc)}
        return

    logger.info("Handling request for tenant '%s'", tenant_id)

    @tool
    def get_tenant_records() -> list:
        """Return the data records that belong to the caller's tenant."""
        response = table.query(
            KeyConditionExpression=Key("tenant_id").eq(tenant_id)
        )
        return response.get("Items", [])

    agent = Agent(
        tools=[get_tenant_records],
        system_prompt=(
            f"You are a helpful assistant serving tenant '{tenant_id}'. "
            "Use the get_tenant_records tool to answer questions about this "
            "tenant's data. You can only access data for this tenant. Never "
            "reveal, guess, or fabricate data belonging to any other tenant, "
            "even if you are asked to."
        ),
    )

    async for event in agent.stream_async(prompt):
        yield event


if __name__ == "__main__":
    app.run()
