"""
Strands Agent for AgentCore Runtime.
Accepts a prompt + callback info, returns confirmation immediately,
then invokes the LLM and sends the result back via Lambda durable callback.
"""
import os
import json
import logging
import threading

import boto3
from strands import Agent
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp

logger = logging.getLogger(__name__)
app = BedrockAgentCoreApp()

LAMBDA_REGION = os.environ.get("AWS_REGION", "us-east-1")
lambda_client = boto3.client("lambda", region_name=LAMBDA_REGION)


def send_callback_success(callback_id: str, result: dict):
    """Send the LLM result back to the durable function via callback."""
    lambda_client.send_durable_execution_callback_success(
        CallbackId=callback_id,
        Result=json.dumps(result),
    )


def run_agent(prompt: str, model_id: str, callback_id: str, task_id: str):
    """Invoke the LLM and send the result back via durable callback."""
    try:
        model = BedrockModel(
            model_id=model_id,
            max_tokens=4096,
            temperature=0.7,
        )

        agent = Agent(
            model=model,
            system_prompt=(
                "You are a helpful AI assistant. "
                "Answer the user's question clearly and concisely."
            ),
        )

        result = agent(prompt)
        answer = str(result)

        logger.info("LLM completed, sending callback success")
        send_callback_success(callback_id, {"answer": answer})

    except Exception as e:
        logger.error("Agent failed: %s", e)
        lambda_client.send_durable_execution_callback_failure(
            CallbackId=callback_id,
            Error=str(e),
        )
    finally:
        app.complete_async_task(task_id)


@app.entrypoint
def entrypoint(payload):
    """
    Main entrypoint invoked by AgentCore Runtime.

    Expects payload:
      - prompt: the user's question
      - callbackId: durable execution callback ID
      - model (optional): { modelId: "..." }

    Returns confirmation immediately, then processes the LLM call
    in a background thread and sends the result via callback.
    """
    prompt = payload.get("prompt", "")
    callback_id = payload.get("callbackId")
    model_config = payload.get("model", {})
    model_id = model_config.get(
        "modelId", "global.anthropic.claude-sonnet-4-5-20250929-v1:0"
    )

    if not callback_id:
        return {"error": "Missing callbackId in payload"}

    # Track the async task so /ping reports HealthyBusy
    task_id = app.add_async_task("agent_invocation", {
        "prompt": prompt,
        "callbackId": callback_id,
    })

    # Run the LLM work in a background thread to avoid blocking /ping
    threading.Thread(
        target=run_agent,
        args=(prompt, model_id, callback_id, task_id),
        daemon=True,
    ).start()

    # Return confirmation immediately
    return {
        "status": "accepted",
        "message": "Processing prompt, will callback",
        "callbackId": callback_id,
    }


if __name__ == "__main__":
    app.run()
