"""
API handler for async job submission and status polling.
POST /jobs — submits a new job, returns job_id immediately.
GET /jobs/{job_id} — returns current job status and progress.
"""

import json
import os
import uuid
import logging
from datetime import datetime, timezone
from decimal import Decimal

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["JOBS_TABLE"])
lambda_client = boto3.client("lambda")

PROCESSOR_FUNCTION_NAME = os.environ["PROCESSOR_FUNCTION_NAME"]


class DecimalEncoder(json.JSONEncoder):
    """Handle DynamoDB Decimal types in JSON serialization."""

    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj == int(obj) else float(obj)
        return super().default(obj)


def lambda_handler(event, context):
    """Route requests to submit or poll handlers."""
    method = event.get("requestContext", {}).get("http", {}).get("method", "")
    path = event.get("rawPath", "")

    if method == "POST" and path == "/jobs":
        return submit_job(event)
    elif method == "GET" and path.startswith("/jobs/"):
        job_id = event.get("pathParameters", {}).get("job_id", "")
        return get_job_status(job_id)
    else:
        return response(404, {"error": "Not found"})


def submit_job(event):
    """Create a new job and invoke the durable processor asynchronously."""
    try:
        body = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return response(400, {"error": "Invalid JSON body"})

    job_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()

    # Write initial job record
    table.put_item(
        Item={
            "job_id": job_id,
            "status": "SUBMITTED",
            "progress": 0,
            "input": body,
            "created_at": now,
            "updated_at": now,
        }
    )

    # Invoke durable processor asynchronously using qualified ARN
    # Durable functions MUST be invoked with a published version or alias
    lambda_client.invoke(
        FunctionName=f"{PROCESSOR_FUNCTION_NAME}:$LATEST",
        InvocationType="Event",
        Payload=json.dumps({"job_id": job_id, "input": body}),
    )

    logger.info("Job %s submitted", job_id)
    return response(202, {"job_id": job_id, "status": "SUBMITTED"})


def get_job_status(job_id):
    """Retrieve current job status from DynamoDB."""
    if not job_id:
        return response(400, {"error": "job_id is required"})

    result = table.get_item(Key={"job_id": job_id})
    item = result.get("Item")

    if not item:
        return response(404, {"error": f"Job {job_id} not found"})

    return response(
        200,
        {
            "job_id": item["job_id"],
            "status": item["status"],
            "progress": item.get("progress", 0),
            "result": item.get("result"),
            "error": item.get("error"),
            "created_at": item.get("created_at"),
            "updated_at": item.get("updated_at"),
        },
    )


def response(status_code, body):
    """Build an HTTP API response."""
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, cls=DecimalEncoder),
    }
