"""Factory functions for Strands SDK client configuration.

Target-type agnostic factories for creating MCP clients and Bedrock model
instances. These functions connect to AgentCore Gateway via MCP protocol
and are unaware of the target type behind the gateway.
"""

import logging
import os

from mcp.client.streamable_http import streamablehttp_client
from strands.models.bedrock import BedrockModel
from strands.tools.mcp import MCPClient

logger = logging.getLogger(__name__)

# Bedrock model ID — override via BEDROCK_MODEL_ID environment variable.
# Defaults to Claude Sonnet 4.5 cross-region inference profile.
DEFAULT_MODEL_ID = os.environ.get(
    "BEDROCK_MODEL_ID",
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
)

# Default AWS region for Bedrock
DEFAULT_REGION = "us-east-1"


def create_mcp_client(gateway_url: str, token: str) -> MCPClient:
    """Create an MCP client configured to connect to AgentCore Gateway.

    Uses streamable HTTP transport with a Bearer token for authentication.
    The returned client is NOT used as a context manager — the Agent manages
    the MCP session lifecycle, and cleanup should occur in a finally block.

    Args:
        gateway_url: The AgentCore Gateway endpoint URL.
        token: JWT token for gateway authentication.

    Returns:
        An MCPClient instance configured for the gateway.
    """
    logger.info("Creating MCP client for gateway: %s", gateway_url)

    mcp_client = MCPClient(
        lambda: streamablehttp_client(
            gateway_url,
            headers={"Authorization": f"Bearer {token}"},
        )
    )

    return mcp_client


def create_bedrock_model(
    model_id: str = DEFAULT_MODEL_ID,
    region_name: str = DEFAULT_REGION,
) -> BedrockModel:
    """Create a Bedrock model instance for the Strands Agent.

    Configures Claude Sonnet 4.5 as the LLM provider via AWS Bedrock.
    The model can be overridden at deploy time via the BEDROCK_MODEL_ID
    environment variable without any code changes.

    Args:
        model_id: Bedrock model identifier. Defaults to the value of the
            BEDROCK_MODEL_ID env var, falling back to Claude Sonnet 4.5.
        region_name: AWS region for Bedrock API calls. Defaults to us-east-1.

    Returns:
        A BedrockModel instance ready for use with a Strands Agent.
    """
    logger.info("Creating Bedrock model: %s in %s", model_id, region_name)

    model = BedrockModel(
        model_id=model_id,
        region_name=region_name,
    )

    return model
