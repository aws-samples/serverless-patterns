import boto3
import json
import os
import logging
from datetime import datetime, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])


def lambda_handler(event, context):
    """
    Bedrock Agent Action Group Lambda.
    Called by the agent to persist task execution records in DynamoDB.
    """
    logger.info("Action group event: %s", json.dumps(event))

    api_path = event.get("apiPath", "")
    action_group = event.get("actionGroup", "")
    http_method = event.get("httpMethod", "")
    params = _extract_parameters(event)

    logger.info("API path: %s | params: %s", api_path, json.dumps(params))

    if api_path == "/record-task-execution":
        result = _record_task_execution(params)
    elif api_path == "/get-last-execution":
        result = _get_last_execution(params)
    else:
        result = {
            "statusCode": 400,
            "body": json.dumps({"error": f"Unknown API path: {api_path}"}),
        }

    return {
        "messageVersion": "1.0",
        "response": {
            "actionGroup": action_group,
            "apiPath": api_path,
            "httpMethod": http_method,
            "httpStatusCode": result["statusCode"],
            "responseBody": {
                "application/json": {"body": result["body"]}
            },
        },
    }


# ──────────────────────────────────────────
# Action handlers
# ──────────────────────────────────────────

def _record_task_execution(params: dict) -> dict:
    """Write an execution record to DynamoDB."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    item = {
        "TaskId": params.get("taskId", f"task-{now}"),
        "TaskType": params.get("taskType", "unknown"),
        "ScheduledTime": params.get("scheduledTime", now),
        "ExecutionSummary": params.get("executionSummary", ""),
        "Status": "COMPLETED",
        "RecordedAt": now,
    }

    table.put_item(Item=item)
    logger.info("Recorded task execution: %s", item["TaskId"])

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": f"Task execution {item['TaskId']} recorded successfully",
                "taskId": item["TaskId"],
                "recordedAt": now,
            }
        ),
    }


def _get_last_execution(params: dict) -> dict:
    """Scan for the most recent execution (simple approach for demo)."""
    task_type = params.get("taskType", "scheduled-report")

    response = table.scan(
        FilterExpression="TaskType = :tt",
        ExpressionAttributeValues={":tt": task_type},
        Limit=10,
    )

    items = sorted(
        response.get("Items", []),
        key=lambda x: x.get("RecordedAt", ""),
        reverse=True,
    )

    if items:
        last = items[0]
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "taskId": last["TaskId"],
                    "taskType": last["TaskType"],
                    "scheduledTime": last["ScheduledTime"],
                    "executionSummary": last.get("ExecutionSummary", ""),
                    "recordedAt": last["RecordedAt"],
                }
            ),
        }

    return {
        "statusCode": 404,
        "body": json.dumps(
            {"message": f"No executions found for task type: {task_type}"}
        ),
    }


# ──────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────

def _extract_parameters(event: dict) -> dict:
    """Pull parameters from the Bedrock Agent request body and/or parameters list."""
    params = {}

    # From requestBody (POST actions)
    properties = (
        event.get("requestBody", {})
        .get("content", {})
        .get("application/json", {})
        .get("properties", [])
    )
    for prop in properties:
        params[prop["name"]] = prop.get("value", "")

    # From top-level parameters (GET actions)
    for param in event.get("parameters", []):
        params[param["name"]] = param.get("value", "")

    return params