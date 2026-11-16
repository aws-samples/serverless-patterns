import logging
import os

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands.agent.conversation_manager import SlidingWindowConversationManager
from strands.models import BedrockModel
from strands.types.exceptions import MaxTokensReachedException

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("agent")
app = BedrockAgentCoreApp()

# Caps the output tokens of every answer. The web app caps the prompt length.
MAX_OUTPUT_TOKENS = 200
# Number of messages (prompts and answers) sent to the model on each turn: the last 5 turns.
HISTORY_MESSAGES = 10

model_id = os.environ["MODEL_ID"]
log.info("model_id=%s", model_id)
# Thinking tokens count against max_tokens. With a small cap, a model that thinks first can spend
# the whole budget on thinking and return no answer, so thinking is turned off. Remove
# additional_request_fields if you set model_id to a model that does not accept this field.
model = BedrockModel(
    model_id=model_id,
    max_tokens=MAX_OUTPUT_TOKENS,
    additional_request_fields={"thinking": {"type": "disabled"}},
)

# AgentCore Runtime runs every session in its own microVM, and the web app creates a new session
# for every login. So one Agent per process is one conversation: the agent remembers the earlier
# turns of that conversation and nobody else's. The sliding window keeps only the most recent
# messages, so the input tokens of a turn stay bounded however long the conversation gets.
agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant in a chat web app. Answer briefly and clearly, and use Markdown when it helps.",
    conversation_manager=SlidingWindowConversationManager(window_size=HISTORY_MESSAGES),
)


def message_text(message):
    """Concatenate the text blocks of a model message."""
    return "".join(block["text"] for block in (message or {}).get("content", []) if "text" in block)


@app.entrypoint
async def app_entrypoint(request_payload, context):
    prompt = request_payload.get("prompt")
    if not prompt:
        log.error("Request payload is missing required field: 'prompt'")
        yield {"type": "error", "error": "Missing required field: 'prompt'"}
        return

    log.info("> app_entrypoint session=%s", context.session_id)

    # Stream the agent's response as the model generates it. When the answer reaches
    # MAX_OUTPUT_TOKENS, Strands keeps the partial answer in the conversation history and raises
    # MaxTokensReachedException right after the assembled message event. Send any text that was not
    # streamed yet, then tell the user that the answer was cut off.
    streamed = ""
    assembled = ""
    try:
        async for event in agent.stream_async(prompt):
            if "data" in event:
                streamed += event["data"]
                yield {"type": "chunk", "data": event["data"]}
            elif "message" in event:
                assembled = message_text(event["message"])
    except MaxTokensReachedException:
        log.warning("answer truncated at max_tokens=%d", MAX_OUTPUT_TOKENS)
        remainder = assembled[len(streamed):] if assembled.startswith(streamed) else ""
        if remainder:
            yield {"type": "chunk", "data": remainder}
        yield {"type": "chunk", "data": "\n\n*(Answer cut off at the response token limit.)*"}

    log.info("< app_entrypoint (stream complete)")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
