"""
AgentCore Gateway tool backend: emit_event

Receives tool invocations from the AgentCore Gateway (MCP Lambda target),
validates the event payload, and publishes to an EventBridge custom bus.

The Gateway provides governance: schema validation on the tool input,
JWT authentication, rate limiting, and observability. This Lambda focuses
on the EventBridge integration and source-prefix enforcement.
"""
import boto3
import json
import os

events_client = boto3.client("events")
ALLOWED_SOURCES = os.environ.get("ALLOWED_SOURCES", "agent.").split(",")
EVENT_BUS_NAME = os.environ["EVENT_BUS_NAME"]


def handler(event, context):
    """Handle tool invocation from AgentCore Gateway."""
    # Gateway sends the tool input as the Lambda event body
    body = event if isinstance(event, dict) and "source" in event else json.loads(event.get("body", "{}"))

    source = body.get("source", "")
    detail_type = body.get("detail_type", "")
    detail = body.get("detail", {})
    notify = body.get("notify", False)

    # Validate required fields
    if not source or not detail_type or not detail:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "source, detail_type, and detail are required"}),
        }

    # Validate source prefix (governance: agents can only emit from allowed namespaces)
    if not any(source.startswith(prefix) for prefix in ALLOWED_SOURCES):
        return {
            "statusCode": 403,
            "body": json.dumps(
                {"error": f"Source must start with one of: {ALLOWED_SOURCES}"}
            ),
        }

    # Add notify flag to detail for downstream rule filtering
    if notify:
        detail["notify"] = True

    # Emit to EventBridge
    response = events_client.put_events(
        Entries=[
            {
                "Source": source,
                "DetailType": detail_type,
                "Detail": json.dumps(detail),
                "EventBusName": EVENT_BUS_NAME,
            }
        ]
    )

    failed_count = response["FailedEntryCount"]

    return {
        "statusCode": 200 if failed_count == 0 else 207,
        "body": json.dumps(
            {
                "success": failed_count == 0,
                "failed_count": failed_count,
                "event_id": response["Entries"][0].get("EventId", ""),
            }
        ),
    }
