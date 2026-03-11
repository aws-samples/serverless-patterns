"""Chat agent entrypoint for AgentCore runtime.

Pure streaming agent with S3-backed session persistence.
Yields response chunks via SSE. Has no knowledge of delivery
mechanism (AppSync, WebSocket, etc.).
"""

import os
import logging

from strands import Agent
from strands.models import BedrockModel
from strands.session.s3_session_manager import S3SessionManager
from strands_tools import http_request, calculator, current_time
from bedrock_agentcore.runtime import BedrockAgentCoreApp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = BedrockAgentCoreApp()

MODEL_ID = os.environ.get("BEDROCK_MODEL_ID")
if not MODEL_ID:
    raise ValueError("BEDROCK_MODEL_ID environment variable is required")

REGION = os.environ.get("AWS_REGION", "eu-west-1")
SESSION_BUCKET = os.environ.get("SESSION_BUCKET")

SYSTEM_PROMPT = """\
You are a research assistant with access to the web, a calculator, and a clock.

You can:
- Fetch and summarise content from any public URL using http_request
- Perform mathematical calculations using calculator
- Check the current date and time in any timezone using current_time

When fetching web content, prefer converting HTML to markdown for readability
by setting convert_to_markdown=true. Always cite the URL you fetched.
Keep responses clear and concise.
"""


def _create_agent(session_id: str | None = None) -> Agent:
    """Create a Strands agent with Bedrock model and optional session."""
    model = BedrockModel(model_id=MODEL_ID, region_name=REGION)

    kwargs = {
        "system_prompt": SYSTEM_PROMPT,
        "model": model,
        "tools": [http_request, calculator, current_time],
    }

    if session_id and SESSION_BUCKET:
        kwargs["session_manager"] = S3SessionManager(
            session_id=session_id,
            bucket=SESSION_BUCKET,
            region_name=REGION,
        )

    return Agent(**kwargs)


@app.entrypoint
async def invoke(payload=None):
    """Stream agent response as SSE events."""
    if not payload:
        yield {"status": "error", "error": "payload is required"}
        return

    query = payload.get("content") or payload.get("prompt")
    if not query:
        yield {"status": "error", "error": "content or prompt is required"}
        return

    session_id = payload.get("sessionId")
    logger.info("Processing query: %s (session: %s)", query[:100], session_id)

    agent = _create_agent(session_id)

    async for event in agent.stream_async(query):
        if "data" in event:
            yield {"data": event["data"]}
        elif "result" in event:
            result = event["result"]
            yield {
                "result": {
                    "stop_reason": str(result.stop_reason),
                    "message": result.message,
                },
            }


if __name__ == "__main__":
    app.run()
