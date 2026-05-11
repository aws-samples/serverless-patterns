"""
AgentCore Agent for Travel Itinerary Generation.
Accepts prompt + callback info, processes with Bedrock, and sends result via callback.
"""
import os
import json
import logging
import threading
import time

import boto3
from strands import Agent
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp

# Configure CloudWatch Logs
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# CloudWatch logging is handled by the AgentCore runtime itself
# No need for watchtower - just use standard logging
LAMBDA_REGION = os.environ.get("AWS_REGION", "us-east-2")
logger.info("Agent module loaded")

app = BedrockAgentCoreApp()


def send_callback_success(callback_id: str, result: dict):
    """Send the result back to the durable function via callback."""
    logger.info(f"Sending callback success for {callback_id[:20]}...")
    lambda_client = boto3.client("lambda", region_name=LAMBDA_REGION)
    lambda_client.send_durable_execution_callback_success(
        CallbackId=callback_id,
        Result=json.dumps(result),
    )
    logger.info("Callback sent successfully")


def send_callback_failure(callback_id: str, error: str):
    """Send error back to the durable function."""
    logger.error(f"Sending callback failure: {error}")
    lambda_client = boto3.client("lambda", region_name=LAMBDA_REGION)
    lambda_client.send_durable_execution_callback_failure(
        CallbackId=callback_id,
        Error={"errorMessage": error, "errorType": "AgentError"},
    )


def run_agent(prompt: str, model_id: str, callback_id: str, task_id: str, system_prompt: str = None):
    """Invoke Bedrock via Strands Agent and send result back via durable callback."""
    try:
        logger.info(f"Starting agent with model {model_id}")

        model = BedrockModel(
            model_id=model_id,
            max_tokens=8192,  # Increased for detailed itineraries
            temperature=0.8,
        )

        default_system = """You are a knowledgeable travel advisor who creates detailed,
personalized travel itineraries. Provide practical, specific recommendations with
clear day-by-day plans. Be helpful, enthusiastic, and concise."""

        agent = Agent(
            model=model,
            system_prompt=system_prompt or default_system,
        )

        logger.info("Invoking Bedrock model...")
        result = agent(prompt)
        answer = str(result)

        logger.info(f"LLM completed, generated {len(answer)} characters")
        send_callback_success(callback_id, {"itinerary": answer})

    except Exception as e:
        logger.error(f"Agent failed: {e}", exc_info=True)
        send_callback_failure(callback_id, str(e))
    finally:
        app.complete_async_task(task_id)


@app.entrypoint
def entrypoint(payload):
    """
    Main entrypoint invoked by AgentCore Runtime.

    Expects payload:
      - prompt: travel planning prompt
      - callbackId: durable execution callback ID
      - model (optional): { modelId: "..." }
      - systemPrompt (optional): custom system prompt

    Returns confirmation immediately, then processes in background.
    """
    prompt = payload.get("prompt", "")
    callback_id = payload.get("callbackId")
    model_config = payload.get("model", {})
    system_prompt = payload.get("systemPrompt")

    model_id = model_config.get(
        "modelId",
        "us.anthropic.claude-sonnet-4-6"
    )

    if not callback_id:
        logger.error("Missing callbackId in payload")
        return {"error": "Missing callbackId in payload"}

    if not prompt:
        logger.error("Missing prompt in payload")
        return {"error": "Missing prompt in payload"}

    logger.info(f"Received request with callback {callback_id[:20]}...")

    # Track the async task so /ping reports HealthyBusy
    task_id = app.add_async_task("itinerary_generation", {
        "prompt": prompt[:100] + "..." if len(prompt) > 100 else prompt,
        "callbackId": callback_id[:20] + "...",
    })

    # Run the LLM work in background thread
    threading.Thread(
        target=run_agent,
        args=(prompt, model_id, callback_id, task_id, system_prompt),
        daemon=True,
    ).start()

    logger.info("Request accepted, processing in background")

    # Return confirmation immediately
    return {
        "status": "accepted",
        "message": "Generating itinerary, will callback when complete",
        "callbackId": callback_id,
    }


if __name__ == "__main__":
    app.run()
