"""
Strands Agent on AgentCore Runtime that connects to an AgentCore Gateway
to discover and use the emit_event MCP tool.

The agent connects to the Gateway using the Streamable HTTP MCP transport.
Authentication: authorizerType=NONE on the Gateway trusts callers within
the same account via the AgentCore platform's workload identity.
"""
import os
import logging

from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = BedrockAgentCoreApp()

GATEWAY_URL = os.environ.get("GATEWAY_MCP_URL", "")


def create_mcp_client():
    """Create a fresh MCP client instance per invocation."""
    if not GATEWAY_URL:
        return None
    return MCPClient(lambda: streamablehttp_client(GATEWAY_URL))


@app.entrypoint
def invoke(payload: dict) -> dict:
    """Process a request and let the agent decide whether to emit events."""
    prompt = payload.get("prompt", "No prompt provided.")
    logger.info("Received prompt: %s", prompt[:200])

    try:
        mcp_client = create_mcp_client()
        if mcp_client:
            with mcp_client:
                agent = Agent(
                    model="us.anthropic.claude-haiku-4-5-20251001-v1:0",
                    tools=mcp_client.list_tools_sync(),
                )
                result = agent(prompt)
        else:
            agent = Agent(model="us.anthropic.claude-haiku-4-5-20251001-v1:0")
            result = agent(prompt)

        logger.info("Agent completed: %s", str(result)[:500])
        return {"status": "completed", "result": str(result)[:2000]}
    except Exception as e:
        logger.exception("Agent invocation failed")
        return {"status": "error", "error": str(e)[:500]}


if __name__ == "__main__":
    app.run()
