import logging
import os
from collections.abc import AsyncGenerator
from pathlib import Path
from typing import Any

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands.models import BedrockModel
from strands.vended_tools import python_repl

from log_events import log_event
from sandbox import CodeInterpreterSandbox

app = BedrockAgentCoreApp()

# A child of the AgentCore SDK's app logger, so records use its JSON format with request and session IDs:
# https://github.com/aws/bedrock-agentcore-sdk-python/blob/v1.25.4/src/bedrock_agentcore/runtime/app.py#L124
# The runtime writes them to its CloudWatch Logs log group, as described under "View logs" in
# https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/view-observability-data-cloudwatch.html
logger = logging.getLogger("bedrock_agentcore.app.agent")

model = BedrockModel(model_id=os.environ["MODEL_ID"])

# {MOUNT_PATH} in the prompt is replaced with the mount path that the stack passes to the runtime.
SYSTEM_PROMPT = (
    (Path(__file__).parent / "system_prompt.md")
    .read_text(encoding="utf-8")
    .replace("{MOUNT_PATH}", os.environ["MOUNT_PATH"])
)


@app.entrypoint
async def invoke(payload: Any) -> AsyncGenerator[Any, None]:
    """Stream the agent's text response for the prompt in the request payload.

    Errors raised here are logged and sent to the caller as an error event by the AgentCore SDK:
    https://github.com/aws/bedrock-agentcore-sdk-python/blob/v1.25.4/src/bedrock_agentcore/runtime/app.py#L884
    """
    prompt = payload.get("prompt") if isinstance(payload, dict) else None
    if not isinstance(prompt, str) or not prompt.strip():
        logger.warning("Rejected a request without a prompt")
        yield {"error": "Request payload must be a JSON object with a non-empty 'prompt' string."}
        return

    log_event(logger, "prompt", prompt=prompt)
    # A new Code Interpreter session and agent per request keep invocations independent of each other.
    async with CodeInterpreterSandbox() as sandbox:
        # callback_handler=None stops Strands from also printing the response to the logs. See
        # https://strandsagents.com/docs/user-guide/sdk/streaming/callback-handlers/
        agent = Agent(
            model=model, system_prompt=SYSTEM_PROMPT, tools=[python_repl], sandbox=sandbox, callback_handler=None,
        )
        async for event in agent.stream_async(prompt):
            if "data" in event:
                yield event["data"]
    logger.info("Finished request")


if __name__ == "__main__":
    app.run()
