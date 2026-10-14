import logging
import os

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands.models import BedrockModel

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("agent")
app = BedrockAgentCoreApp()

model_id = os.environ["MODEL_ID"]
log.info("model_id=%s", model_id)
model = BedrockModel(model_id=model_id)

# AgentCore Runtime runs every session in its own microVM, and the web app sends one session ID
# per browser tab. So one Agent per process is one conversation per tab: the agent remembers the
# earlier turns of that conversation and nobody else's.
agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant in a chat web app. Answer clearly and use Markdown when it helps.",
)


@app.entrypoint
async def app_entrypoint(request_payload, context):
    prompt = request_payload.get("prompt")
    if not prompt:
        log.error("Request payload is missing required field: 'prompt'")
        yield {"type": "error", "error": "Missing required field: 'prompt'"}
        return

    log.info("> app_entrypoint session=%s", context.session_id)

    # Stream the agent's response as the model generates it.
    async for event in agent.stream_async(prompt):
        if "data" in event:
            yield {"type": "chunk", "data": event["data"]}

    log.info("< app_entrypoint (stream complete)")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
