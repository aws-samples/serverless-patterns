"""
AFTER - the same FastAPI job API, with the work moved to SQS + Lambda.

POST /v1/jobs       -> write {job_id, status=PENDING}, send one SQS message,
                       return. The web process does NOT run the steps.
GET  /v1/jobs/{id}  -> read the row and return its status (unchanged)

The API is unchanged in shape: same framework, same routes, same public
job_id, same status words. What changed is behind it. The POST now returns
after a single SQS SendMessage; a separate Lambda consumer (worker.py) runs
the identical step code and writes progress back to the same table.

Why this is better: the work no longer rides the web process. A deploy or
scale-in cannot strand a job - unacked SQS messages are redelivered, and a
poison message lands in a dead-letter queue instead of looping forever. The
API and the worker scale independently.

Cutover: this reuses the SAME table and the SAME /v1 routes, so clients need
no change. A row written by the old in-process version carries no "source":
"sqs" marker; the worker ignores it and the old server drains it. Point all
traffic at this version and old in-flight jobs finish on the old box until the
table is empty.
"""

import json
import os
import time
import uuid

import boto3
from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.metrics import MetricUnit
from botocore.config import Config
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum

logger = Logger()
tracer = Tracer()  # patches boto3 so DynamoDB and SQS calls become X-Ray subsegments
metrics = Metrics()

# Keep SDK calls well inside the 10s function timeout: a hung dependency
# surfaces as a logged error, not a Task timed out.
_SDK = Config(connect_timeout=2, read_timeout=5, retries={"mode": "standard", "max_attempts": 2})
dynamodb = boto3.resource("dynamodb", config=_SDK)
table = dynamodb.Table(os.environ["JOBS_TABLE"])
sqs = boto3.client("sqs", config=_SDK)

QUEUE_URL = os.environ["JOBS_QUEUE_URL"]
TTL_SECONDS = 3 * 24 * 60 * 60

app = FastAPI(title="jobs (sqs + lambda)", docs_url=None, redoc_url=None)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info("request", method=request.method, path=request.url.path,
                status=response.status_code)
    return response


@app.exception_handler(Exception)
async def _unhandled(request: Request, exc: Exception) -> JSONResponse:
    # An SDK error (throttle, timeout) must come back as JSON, not the
    # framework's text 500.
    logger.exception("unhandled error", method=request.method, path=request.url.path)
    return JSONResponse({"error": "internal error"}, status_code=500)


def _row_to_body(job_id: str, item: dict) -> dict:
    body = {"job_id": job_id, "status": item["status"], "step": item.get("step")}
    for k in ("result", "error"):
        if k in item:
            body[k] = item[k]
    return body


@app.post("/v1/jobs")
async def create_job(request: Request) -> JSONResponse:
    try:
        payload = await request.json()
    except ValueError:
        return JSONResponse({"error": "body must be JSON"}, status_code=400)
    if not isinstance(payload, dict) or not payload:
        return JSONResponse({"error": "body must be a non-empty JSON object"}, status_code=400)
    job_id = payload.get("job_id") or str(uuid.uuid4())
    now = int(time.time())

    # Conditional put so a client retry with the same job_id does not reset a
    # job or enqueue it twice.
    try:
        table.put_item(
            Item={
                "job_id": job_id,
                "status": "PENDING",
                "step": None,
                "source": "sqs",
                "created_at": now,
                "updated_at": now,
                "expires_at": now + TTL_SECONDS,
            },
            ConditionExpression="attribute_not_exists(job_id)",
        )
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        existing = table.get_item(Key={"job_id": job_id})["Item"]
        return JSONResponse(_row_to_body(job_id, existing), status_code=200)

    # Hand the job off. The row is already PENDING, so a GET works immediately
    # even if the worker has not picked the message up yet. If the send fails,
    # roll the row back so a client retry with the same job_id enqueues again
    # instead of hitting the conditional put and reading a PENDING row forever.
    try:
        sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps({"job_id": job_id, "payload": payload}),
        )
    except Exception:
        logger.exception("enqueue failed; rolling back row", job_id=job_id)
        table.delete_item(
            Key={"job_id": job_id},
            ConditionExpression="#s = :p",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":p": "PENDING"},
        )
        return JSONResponse({"error": "could not enqueue job, retry", "job_id": job_id},
                            status_code=503)
    metrics.add_metric(name="JobsEnqueued", unit=MetricUnit.Count, value=1)
    return JSONResponse({"job_id": job_id, "status": "PENDING"}, status_code=202)


@app.get("/v1/jobs/{job_id}")
async def get_job(job_id: str) -> JSONResponse:
    item = table.get_item(Key={"job_id": job_id}).get("Item")
    if not item:
        return JSONResponse({"error": "job not found", "job_id": job_id}, status_code=404)
    return JSONResponse(_row_to_body(job_id, item), status_code=200)


# Lambda entry point. Lifespan is off because there is no startup work to run.
_asgi = Mangum(app, lifespan="off")


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context) -> dict:
    return _asgi(event, context)
