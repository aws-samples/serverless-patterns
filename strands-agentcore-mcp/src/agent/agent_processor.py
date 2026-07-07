"""Agent request processor with MCP session lifecycle management.

Target-type agnostic processor that creates a Strands Agent with an MCP
client connected to AgentCore Gateway. Manages the MCP session in a
try/finally block to ensure cleanup on both success and failure paths.
"""

import os

from strands import Agent

from src.agent.strands_client import create_bedrock_model, create_mcp_client
from src.shared.error_utils import format_internal_error_response
from src.shared.logging_utils import get_logger
from src.shared.models import AgentRequest, AgentResponse

logger = get_logger(__name__)

# Environment variable for the gateway URL
GATEWAY_URL_ENV = "GATEWAY_URL"

SYSTEM_PROMPT = """You have access to product management tools via MCP.
- Use list_products to see available products (optionally filter by category)
- Use get_product with category and productId to retrieve a specific product
- Use put_product to create or update a product

Respond conversationally based on tool results."""


def process_request(request: AgentRequest, gateway_url: str | None = None) -> AgentResponse:
    """Process an agent request by invoking the Strands Agent with MCP tools.

    Creates an MCP client connected to the AgentCore Gateway, builds a Strands
    Agent with a Bedrock model, and invokes the agent with the user's prompt.
    The MCP session lifecycle is managed in a try/finally block — NOT a with
    context manager — to ensure cleanup occurs even on exceptions.

    Args:
        request: The agent request containing the prompt and user context.
        gateway_url: Optional gateway URL override. If not provided, reads
            from the GATEWAY_URL environment variable.

    Returns:
        An AgentResponse with the agent's response on success, or an error
        response on failure.
    """
    url = gateway_url or os.environ.get(GATEWAY_URL_ENV)
    if not url:
        logger.error("Gateway URL not configured")
        return format_internal_error_response("Gateway URL not configured")

    token = request.user_context.token
    prompt = request.prompt

    logger.info("Processing request for user: %s", request.user_context.username)

    mcp_client = create_mcp_client(url, token)
    try:
        bedrock_model = create_bedrock_model()
        agent = Agent(model=bedrock_model, tools=[mcp_client], system_prompt=SYSTEM_PROMPT)
        result = agent(prompt)
        logger.info("Agent completed successfully for user: %s", request.user_context.username)
        return AgentResponse(success=True, response=str(result))
    except Exception as e:
        logger.error("Agent processing failed: %s", e)
        return format_internal_error_response("Agent processing error", exception=e)
    finally:
        logger.info("Cleaning up MCP client")
        try:
            mcp_client.cleanup()
        except AttributeError:
            try:
                mcp_client.close()
            except AttributeError:
                pass
