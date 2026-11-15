"""Agent invoker — thin dispatcher for AppSync Events direct Lambda integration.

Receives chat events, invokes the stream relay Lambda asynchronously,
and returns immediately so AppSync gets a fast response.

Requires sessionId in the message payload — used for both session
persistence and channel isolation.
"""

import json
import os

import boto3
from aws_lambda_powertools import Logger, Tracer

logger = Logger()
tracer = Tracer()

lambda_client = boto3.client("lambda")

STREAM_RELAY_ARN = os.environ["STREAM_RELAY_ARN"]


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def handler(event: dict, context) -> dict:
    """Handle incoming chat messages from AppSync Events."""
    logger.info("Received event", extra={"event": event})

    incoming_events = event.get("events", [])
    channel = event.get("info", {}).get("channel", {}).get("path", "/chat/default")
    results = []

    for e in incoming_events:
        payload = e.get("payload", {})
        event_id = e.get("id")

        message = payload.get("message")
        if not message or not str(message).strip():
            results.append(
                {
                    "id": event_id,
                    "payload": {
                        "error": "message is required and cannot be empty",
                    },
                }
            )
            continue

        session_id = payload.get("sessionId")
        if not session_id or not str(session_id).strip():
            results.append(
                {
                    "id": event_id,
                    "payload": {
                        "error": "sessionId is required and cannot be empty",
                    },
                }
            )
            continue

        relay_payload = {
            "content": payload.get("message", ""),
            "channel": f"/responses{channel}",
            "eventId": event_id,
            "sessionId": session_id,
        }

        logger.info(
            "Invoking stream relay",
            extra={
                "event_id": event_id,
                "channel": channel,
                "session_id": session_id,
            },
        )

        lambda_client.invoke(
            FunctionName=STREAM_RELAY_ARN,
            InvocationType="Event",
            Payload=json.dumps(relay_payload).encode(),
        )

        results.append(
            {
                "id": event_id,
                "payload": {**payload, "sessionId": session_id},
            }
        )

    return {"events": results}
