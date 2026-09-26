"""
Minimal async AgentCore Runtime entrypoint for the
EventBridge API Destination -> AgentCore Runtime pattern.

Why async: EventBridge API Destinations enforce a hard 5-second response
timeout on the target endpoint. Agent reasoning (an LLM call via Strands)
routinely takes longer than that, so this entrypoint acknowledges the
request immediately (HTTP 2xx, well under 5s) and continues the actual
agent work in a background asyncio task.

This is intentionally minimal so the pattern deploys and can be tested
end-to-end. Swap the Strands `Agent()` call for your own tools/model
config as needed.
"""
import asyncio
import logging

from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = BedrockAgentCoreApp()
agent = Agent(model="us.anthropic.claude-haiku-4-5-20251001-v1:0")


async def process_event(payload: dict) -> None:
    """Runs the actual agent reasoning after the HTTP response has
    already been returned to EventBridge. Errors here are logged only:
    there is no caller left to report back to."""
    prompt = payload.get("prompt", "Summarize this event.")
    order_id = payload.get("orderId", "unknown")
    try:
        result = agent(prompt)
        logger.info("orderId=%s agent result: %s", order_id, result)
    except Exception:
        logger.exception("orderId=%s agent invocation failed", order_id)


@app.entrypoint
async def invoke(payload: dict) -> dict:
    # Fire-and-forget the real work so we can return well within the
    # API Destination's 5-second timeout.
    asyncio.create_task(process_event(payload))
    return {"status": "accepted", "orderId": payload.get("orderId")}


if __name__ == "__main__":
    app.run()
