"""Strands SDK factory functions for AI agent orchestration."""

from typing import Optional

from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.models.bedrock import BedrockModel
from strands.tools.mcp import MCPClient


SYSTEM_PROMPT = (
    "You are a helpful AI assistant with access to tools. "
    "Use the available tools to help users accomplish their tasks. "
    "Always provide clear, accurate responses and explain what actions you are taking."
)


def create_mcp_client(gateway_url: str, jwt_token: str) -> MCPClient:
    """Create an MCPClient with streamablehttp_client transport.

    Args:
        gateway_url: AgentCore Gateway MCP endpoint URL
        jwt_token: Cognito access token for Authorization header

    Returns:
        Configured MCPClient (not yet started — Agent.load_tools() handles that)
    """
    return MCPClient(
        lambda: streamablehttp_client(
            url=gateway_url,
            headers={"Authorization": f"Bearer {jwt_token}"},
        )
    )


def create_agent(
    model_id: str,
    region: str,
    mcp_client: MCPClient,
    system_prompt: Optional[str] = None,
) -> Agent:
    """Create a Strands Agent with BedrockModel and MCPClient tool source.

    Args:
        model_id: Bedrock model ID (e.g., us.anthropic.claude-sonnet-4-6)
        region: AWS region for Bedrock
        mcp_client: MCPClient instance for tool discovery/execution
        system_prompt: Optional override for SYSTEM_PROMPT

    Returns:
        Configured Agent ready to be called with a prompt
    """
    bedrock_model = BedrockModel(
        model_id=model_id,
        region_name=region,
        max_tokens=4096,
    )

    return Agent(
        model=bedrock_model,
        tools=[mcp_client],
        system_prompt=system_prompt or SYSTEM_PROMPT,
    )
