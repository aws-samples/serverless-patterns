"""Stream relay — consumes SSE stream from AgentCore and publishes chunks to AppSync Events.

Invoked asynchronously by the agent_invoker Lambda. Has up to 15 minutes
to consume the full agent response stream.

Flow:
1. Receives agent runtime ARN, channel, and event context
2. Calls invoke_agent_runtime and consumes the SSE stream
3. Publishes each chunk to the AppSync Events channel
4. Publishes a completion event when the stream ends
"""

import json
import os
import urllib.request

import boto3
from aws_lambda_powertools import Logger, Tracer

logger = Logger()
tracer = Tracer()

agentcore_client = boto3.client("bedrock-agentcore")

APPSYNC_HTTP_ENDPOINT = os.environ["APPSYNC_HTTP_ENDPOINT"]
APPSYNC_API_KEY = os.environ["APPSYNC_API_KEY"]
AGENT_RUNTIME_ARN = os.environ["AGENT_RUNTIME_ARN"]


def _publish_to_channel(channel: str, event: dict):
    """Publish an event to an AppSync Events channel via HTTP."""
    url = f"https://{APPSYNC_HTTP_ENDPOINT}/event"
    body = json.dumps({
        "channel": channel,
        "events": [json.dumps(event)],
    }).encode()

    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "x-api-key": APPSYNC_API_KEY,
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            logger.debug("Published to %s: %s", channel, resp.status)
    except Exception:
        logger.exception("Failed to publish to %s", channel)


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def handler(event: dict, context) -> dict:
    """Consume agent SSE stream and relay chunks to AppSync Events."""
    channel = event["channel"]
    event_id = event["eventId"]
    content = event["content"]
    session_id = event["sessionId"]

    logger.info(
        "Starting stream relay",
        extra={
            "channel": channel,
            "event_id": event_id,
            "session_id": session_id,
        },
    )

    # Invoke AgentCore Runtime
    payload = json.dumps({
        "content": content,
        "sessionId": session_id,
    }).encode()
    response = agentcore_client.invoke_agent_runtime(
        agentRuntimeArn=AGENT_RUNTIME_ARN,
        payload=payload,
    )

    content_type = response.get("contentType", "")
    sequence = 0
    full_response = ""
    current_chunk = ""

    if "text/event-stream" in content_type:
        # Streaming SSE response — consume line by line
        for line in response["response"].iter_lines(chunk_size=1024):
            if not line:
                continue
            decoded = line.decode("utf-8")
            if not decoded.startswith("data: "):
                continue

            data_str = decoded[6:]  # strip "data: " prefix
            try:
                data = json.loads(data_str)
            except json.JSONDecodeError:
                # Raw text chunk
                current_chunk += data_str
                full_response += data_str
                continue

            # Skip non-dict events (shouldn't happen but be safe)
            if not isinstance(data, dict):
                logger.debug("Non-dict SSE event", extra={"data": data})
                continue

            # Skip Strands control events (init_event_loop, start, etc.)
            if any(k in data for k in (
                "init_event_loop", "start", "start_event_loop",
                "force_stop", "complete",
            )):
                logger.debug("Control event", extra={"data": data})
                continue

            # Extract text from the event — Strands uses "data" key
            text = data.get("data", "")
            if isinstance(text, str) and text:
                current_chunk += text
                full_response += text

                if (
                    len(current_chunk) >= 50
                    or text.endswith((".", "!", "?", "\n"))
                ):
                    _publish_to_channel(channel, {
                        "type": "chunk",
                        "sequence": sequence,
                        "content": current_chunk,
                        "eventId": event_id,
                    })
                    sequence += 1
                    current_chunk = ""
    else:
        # Non-streaming JSON response
        raw = response["response"].read().decode("utf-8")
        try:
            body = json.loads(raw)
            full_response = body.get("message", raw)
        except json.JSONDecodeError:
            full_response = raw

    # Publish completion event (includes any remaining chunk content)
    _publish_to_channel(channel, {
        "type": "complete",
        "sequence": sequence,
        "content": current_chunk,
        "response": full_response,
        "eventId": event_id,
    })

    logger.info(
        "Stream relay complete",
        extra={
            "event_id": event_id,
            "chunks_sent": sequence + 1,
            "response_length": len(full_response),
        },
    )

    return {"status": "success", "chunks_sent": sequence + 1}
