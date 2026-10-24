"""Strands Agents SDK client for AI agent orchestration.

Uses the official strands-agents SDK (pip install strands-agents) with
MCPClient to connect to the AgentCore Gateway MCP endpoint. The SDK
handles the full agentic loop automatically: reasoning, tool selection,
tool execution, and response generation.

References:
- https://strandsagents.com/docs/user-guide/concepts/agents/agent-loop/
- https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/
- https://strandsagents.com/docs/user-guide/deploy/deploy_to_aws_lambda/
"""

from typing import Optional

from strands import Agent
from strands.models.bedrock import BedrockModel
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

from shared.logging_utils import StructuredLogger


SYSTEM_PROMPT = """You are a helpful AI assistant that can interact with APIs to help users.
When retrieving information, use the available tools to fetch real data.
Format responses in a clear, human-readable way.
If a tool call fails, explain the error and suggest alternatives."""


def create_mcp_client(gateway_url: str, jwt_token: str) -> MCPClient:
    """Create an MCPClient connected to the AgentCore Gateway MCP endpoint.

    Args:
        gateway_url: Full Gateway MCP endpoint URL
        jwt_token: JWT token for authorization

    Returns:
        MCPClient configured for the Gateway
    """
    return MCPClient(
        lambda: streamablehttp_client(
            url=gateway_url,
            headers={"Authorization": f"Bearer {jwt_token}"}
        )
    )


def create_agent(
    model_id: str,
    region: str,
    mcp_client: MCPClient,
    system_prompt: Optional[str] = None,
    max_tokens: int = 4096,
) -> Agent:
    """Create a Strands Agent with Bedrock model and MCP tools.

    Args:
        model_id: Bedrock model ID
        region: AWS region
        mcp_client: MCPClient connected to Gateway
        system_prompt: Optional system prompt override
        max_tokens: Maximum tokens in response

    Returns:
        Configured Strands Agent
    """
    model = BedrockModel(
        model_id=model_id,
        region_name=region,
        max_tokens=max_tokens,
    )

    return Agent(
        model=model,
        tools=[mcp_client],
        system_prompt=system_prompt or SYSTEM_PROMPT,
    )
