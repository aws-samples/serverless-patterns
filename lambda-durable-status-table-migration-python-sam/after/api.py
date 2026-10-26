"""
AFTER - job API backed by durable executions.

POST /v2/jobs       -> start a durable execution named by job_id, store its ARN
GET  /v2/jobs/{id}  -> job_id -> execution ARN -> GetDurableExecution

The table shrinks to one job: map a public job_id to an execution ARN.
Status, step progress, retries and results now live in the durable runtime.

Cutover: a GET for a job created by the OLD API (a row with no execution
ARN) still answers from the row. Point clients at /v2 and the old poller
keeps draining old rows until they are gone.
"""

import json
import logging
import os
import time
import uuid

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["JOBS_TABLE"])
lambda_client = boto3.client("lambda")

JOB_FUNCTION = os.environ["JOB_FUNCTION"]  # qualified alias ARN
TTL_SECONDS = 3 * 24 * 60 * 60

# Durable execution status -> the status words the old API returned,
# so clients polling GET /jobs/{id} need no change.
STATUS_MAP = {
    "RUNNING": "RUNNING",
    "SUCCEEDED": "DONE",
    "FAILED": "FAILED",
    "TIMED_OUT": "FAILED",
    "STOPPED": "FAILED",
}


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _response(status_code: int, body: dict) -> dict:
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def create_job(event: dict) -> dict:
    try:
        payload = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return _response(400, {"error": "body must be JSON"})
    job_id = payload.get("job_id") or str(uuid.uuid4())

    # DurableExecutionName makes the start idempotent: a retry with the same
    # job_id returns the existing execution instead of creating a second one.
    invoke = lambda_client.invoke(
        FunctionName=JOB_FUNCTION,
        InvocationType="Event",
        DurableExecutionName=job_id,
        Payload=json.dumps({"job_id": job_id, "payload": payload}),
    )
    execution_arn = invoke.get("DurableExecutionArn")
    if not execution_arn:
        # Only a durable function returns this. A missing ARN means JOB_FUNCTION
        # points at a function without DurableConfig.
        return _response(
            500, {"error": "target is not a durable function", "job_id": job_id}
        )

    now = int(time.time())
    table.put_item(
        Item={
            "job_id": job_id,
            "execution_arn": execution_arn,
            "created_at": now,
            "expires_at": now + TTL_SECONDS,
        }
    )
    return _response(202, {"job_id": job_id, "status": "RUNNING"})


def get_job(event: dict) -> dict:
    job_id = (event.get("pathParameters") or {}).get("job_id")
    item = table.get_item(Key={"job_id": job_id}).get("Item")
    if not item:
        return _response(404, {"error": "job not found", "job_id": job_id})

    execution_arn = item.get("execution_arn")
    if not execution_arn:
        # Legacy row from the status-table version: still in flight on the old poller.
        body = {
            "job_id": job_id,
            "status": item.get("status", "UNKNOWN"),
            "step": item.get("step"),
            "legacy": True,
        }
        if "result" in item:
            body["result"] = item["result"]
        if "error" in item:
            body["error"] = item["error"]
        return _response(200, body)

    execution = lambda_client.get_durable_execution(DurableExecutionArn=execution_arn)
    body = {
        "job_id": job_id,
        "status": STATUS_MAP.get(execution["Status"], execution["Status"]),
    }
    if execution.get("Result"):
        body["result"] = json.loads(execution["Result"])
    if execution.get("Error"):
        body["error"] = execution["Error"].get("ErrorMessage") or str(
            execution["Error"]
        )
    return _response(200, body)


def lambda_handler(event: dict, context) -> dict:
    method = event.get("httpMethod")
    if method == "POST":
        response = create_job(event)
    elif method == "GET":
        response = get_job(event)
    else:
        response = _response(405, {"error": "method not allowed"})
    logger.info(
        "%s %s -> %s",
        method,
        event.get("path"),
        response["statusCode"],
    )
    return response
