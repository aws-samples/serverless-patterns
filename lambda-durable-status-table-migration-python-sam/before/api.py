"""
BEFORE - job API backed by a status table.

POST /v1/jobs       -> write {job_id, status=PENDING, payload} to the table
GET  /v1/jobs/{id}  -> read the row and return its status

The table is the only source of truth about where a job is.
A separate poller (worker.py) moves rows through PENDING -> RUNNING -> DONE.
"""

import json
import logging
import os
import time
import uuid

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["JOBS_TABLE"])

TTL_SECONDS = 3 * 24 * 60 * 60


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
    now = int(time.time())

    # Conditional put so a client retry with the same job_id does not reset a job.
    try:
        table.put_item(
            Item={
                "job_id": job_id,
                "status": "PENDING",
                "step": None,
                "payload": payload,
                "created_at": now,
                "updated_at": now,
                "expires_at": now + TTL_SECONDS,
            },
            ConditionExpression="attribute_not_exists(job_id)",
        )
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        # Already exists: report where it really is, not a fresh PENDING.
        existing = table.get_item(Key={"job_id": job_id})["Item"]
        body = {
            "job_id": job_id,
            "status": existing["status"],
            "step": existing.get("step"),
        }
        for k in ("result", "error"):
            if k in existing:
                body[k] = existing[k]
        return _response(200, body)

    return _response(202, {"job_id": job_id, "status": "PENDING"})


def get_job(event: dict) -> dict:
    job_id = (event.get("pathParameters") or {}).get("job_id")
    item = table.get_item(Key={"job_id": job_id}).get("Item")
    if not item:
        return _response(404, {"error": "job not found", "job_id": job_id})

    body = {
        "job_id": job_id,
        "status": item["status"],
        "step": item.get("step"),
    }
    if "result" in item:
        body["result"] = item["result"]
    if "error" in item:
        body["error"] = item["error"]
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
