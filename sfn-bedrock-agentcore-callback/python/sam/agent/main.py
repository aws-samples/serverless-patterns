import asyncio
import json
import os

import boto3
from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

# Replace with a model or inference profile that you can use in your Region.
MODEL_ID = os.environ.get("MODEL_ID", "global.anthropic.claude-haiku-4-5-20251001-v1:0")

app = BedrockAgentCoreApp()

# Region comes from the AWS_REGION env var the runtime sets; the client uses
# the runtime's execution-role credentials automatically.
sfn = boto3.client("stepfunctions")

# Keep strong references to in-flight background tasks so they are not
# garbage-collected before they finish.
_background_tasks: set = set()


def run_agent(prompt):
    # A new Agent for each invocation, so that invocations that share a
    # runtime session do not share conversation history.
    return Agent(model=MODEL_ID)(prompt)


@app.async_task
async def run_and_callback(prompt, task_token):
    """Long-running work for the callback pattern, run in the background.

    @app.async_task holds the runtime HEALTHY_BUSY so the platform keeps the
    session alive (up to the session lifetime) instead of reaping it. Blocking
    calls are pushed to threads so the event loop stays free to answer /ping
    health checks.
    """
    try:
        # The agent call is blocking, so run it in a worker thread.
        result = await asyncio.to_thread(run_agent, prompt)

        # The result goes to Step Functions through SendTaskSuccess.
        # "output" must be a JSON string of 256 KB or less.
        output = json.dumps({"result": result.message})
        await asyncio.to_thread(
            lambda: sfn.send_task_success(taskToken=task_token, output=output)
        )
    except Exception as exc:
        # Fail the Step Functions task promptly instead of letting it wait out its timeout.
        cause_text = str(exc)[:32768]
        await asyncio.to_thread(
            lambda: sfn.send_task_failure(
                taskToken=task_token,
                error="AgentRuntimeError",
                cause=cause_text,
            )
        )
        raise


@app.entrypoint
async def invoke(payload):
    prompt = payload.get("prompt", "Hello! How can I help you today?")
    task_token = payload.get("task_token")

    # Request Response: run the agent and return its answer in the response.
    if not task_token:
        result = await asyncio.to_thread(run_agent, prompt)
        return {"result": result.message}

    # Callback: start the work in the background and return immediately.
    # The result reaches Step Functions later through SendTaskSuccess.
    task = asyncio.create_task(run_and_callback(prompt, task_token))
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)
    return {"status": "ACCEPTED"}


if __name__ == "__main__":
    app.run()
