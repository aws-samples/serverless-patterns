"""
Minimal async AgentCore Runtime entrypoint for the
EventBridge API Destination -> AgentCore Runtime pattern.

Why async: EventBridge API Destinations enforce a hard 5-second response
timeout on the target endpoint. Agent reasoning (an LLM call via Strands)
routinely takes longer than that, so this entrypoint acknowledges the
request immediately (HTTP 2xx, well under 5s) and continues the actual
agent work in a background task.

The background work is registered with the runtime through the
@app.async_task decorator. While it runs, the runtime's /ping endpoint
reports "HealthyBusy", so AgentCore Runtime keeps the session alive until
the work finishes instead of treating it as idle.

Delivery semantics, which matter for production use:

- Background failures are NOT retried. EventBridge considers the event
  delivered as soon as the 2xx acknowledgment is returned, so the
  dead-letter queue only captures delivery failures (401/403, 5xx,
  timeouts). An exception inside process_event is logged and nothing
  else. For production, report the outcome somewhere durable: emit a
  follow-up EventBridge event, write the result or failure to a store
  such as Amazon DynamoDB, or use a callback (for example a Step
  Functions task token with send_task_success / send_task_failure).
- No idempotency. EventBridge delivery is at-least-once, so the same
  event can be delivered more than once. The rule forwards the
  EventBridge event ID as "eventId"; for production, check it against an
  idempotency store before performing side effects.

This is intentionally minimal so the pattern deploys and can be tested
end-to-end. Swap the Strands Agent configuration for your own tools and
model as needed.
"""
import asyncio
import logging

from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Claude Haiku 5.5 through the US geographic cross-Region inference profile.
# The "us." prefix only works when the stack is deployed in a US Region. In
# other geographies use the matching prefix ("eu.", "jp.", "au.") or the
# global profile ("global.anthropic.claude-haiku-5-5"), and confirm the model
# is available in your Region.
MODEL_ID = "us.anthropic.claude-haiku-5-5"

app = BedrockAgentCoreApp()

# The event loop keeps only weak references to tasks, so an un-referenced
# task can be garbage collected before it finishes. Hold a strong reference
# until each task completes.
_background_tasks: set[asyncio.Task] = set()


@app.async_task
async def process_event(payload: dict) -> None:
    """Runs the agent reasoning after the HTTP response has already been
    returned to EventBridge. See the module docstring for why errors here
    are logged only and not retried."""
    prompt = payload.get("prompt", "Summarize this event.")
    order_id = payload.get("orderId", "unknown")
    # Production: deduplicate on event_id before performing side effects.
    event_id = payload.get("eventId", "unknown")
    try:
        # One Agent per event: a Strands Agent instance does not support
        # concurrent invocations. invoke_async keeps the event loop (and
        # therefore the /ping health check) responsive during the LLM call.
        agent = Agent(model=MODEL_ID)
        result = await agent.invoke_async(prompt)
        logger.info("eventId=%s orderId=%s agent result: %s", event_id, order_id, result)
    except Exception:
        # Production: emit a failure event or persist the failure here so
        # it can be inspected and redriven. The EventBridge DLQ never sees it.
        logger.exception("eventId=%s orderId=%s agent invocation failed", event_id, order_id)


@app.entrypoint
async def invoke(payload: dict) -> dict:
    # Start the real work and acknowledge right away, well within the
    # API Destination's 5-second timeout. @app.async_task keeps the runtime
    # busy until process_event finishes.
    task = asyncio.create_task(process_event(payload))
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)
    return {"status": "accepted", "orderId": payload.get("orderId")}


if __name__ == "__main__":
    app.run()
