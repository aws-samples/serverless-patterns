import boto3
import json
import os
import uuid
import logging
from datetime import datetime, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bedrock_agent_runtime = boto3.client("bedrock-agent-runtime")

AGENT_ID = os.environ["BEDROCK_AGENT_ID"]
AGENT_ALIAS_ID = os.environ["BEDROCK_AGENT_ALIAS_ID"]


def lambda_handler(event, context):
    """
    Orchestrator Lambda — invoked by EventBridge Scheduler.
    Parses the schedule payload, enriches it with a real timestamp,
    and sends it to the Bedrock Agent for processing.
    """
    logger.info("Received event: %s", json.dumps(event))

    # ── Enrich the payload with the actual invocation time ──
    task_type = event.get("taskType", "scheduled-report")
    schedule_name = event.get("scheduleName", "unknown-schedule")
    scheduled_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    prompt = (
        f"Process this scheduled task execution:\n\n"
        f'{{"taskType": "{task_type}", '
        f'"scheduleName": "{schedule_name}", '
        f'"scheduledTime": "{scheduled_time}"}}\n\n'
        f"Parse the payload, generate a summary, and record the execution."
    )

    # ── Invoke the Bedrock Agent ──
    session_id = str(uuid.uuid4())
    logger.info(
        "Invoking agent %s (alias %s) | session %s",
        AGENT_ID,
        AGENT_ALIAS_ID,
        session_id,
    )

    response = bedrock_agent_runtime.invoke_agent(
        agentId=AGENT_ID,
        agentAliasId=AGENT_ALIAS_ID,
        sessionId=session_id,
        inputText=prompt,
    )

    # ── Collect the streaming response ──
    agent_response = ""
    for stream_event in response.get("completion", []):
        if "chunk" in stream_event:
            agent_response += stream_event["chunk"]["bytes"].decode("utf-8")

    logger.info("Agent response: %s", agent_response)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "sessionId": session_id,
                "taskType": task_type,
                "scheduledTime": scheduled_time,
                "agentResponse": agent_response,
            }
        ),
    }