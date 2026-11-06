"""
AFTER - the same FastAPI job API, backed by durable executions.

POST /v2/jobs       -> start a durable execution named by job_id, store its ARN
GET  /v2/jobs/{id}  -> job_id -> execution ARN -> GetDurableExecution

The web app is unchanged in shape: same framework, same routes, same public
job_id. What changed is behind it. The table shrinks to one job: map a public
job_id to an execution ARN. Status, step progress, retries and results now
live in the durable runtime.

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
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum

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

app = FastAPI(title="jobs (durable)", docs_url=None, redoc_url=None)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info("%s %s -> %s", request.method, request.url.path, response.status_code)
    return response


@app.post("/v2/jobs")
async def create_job(request: Request) -> JSONResponse:
    try:
        payload = await request.json()
    except ValueError:
        return JSONResponse({"error": "body must be JSON"}, status_code=400)
    if not isinstance(payload, dict):
        return JSONResponse({"error": "body must be a JSON object"}, status_code=400)
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
        return JSONResponse(
            {"error": "target is not a durable function", "job_id": job_id},
            status_code=500,
        )

    # Conditional put: never overwrite the row. A duplicate POST after a redeploy
    # gets back an ARN stamped with the alias's CURRENT version, but the execution
    # keeps the version it was created under, so overwriting would break later GETs.
    now = int(time.time())
    try:
        table.put_item(
            Item={
                "job_id": job_id,
                "execution_arn": execution_arn,
                "created_at": now,
                "expires_at": now + TTL_SECONDS,
            },
            ConditionExpression="attribute_not_exists(job_id)",
        )
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        # Already started: report where it really is, same as the legacy API does.
        return await get_job(job_id)

    return JSONResponse({"job_id": job_id, "status": "RUNNING"}, status_code=202)


@app.get("/v2/jobs/{job_id}")
async def get_job(job_id: str) -> JSONResponse:
    item = table.get_item(Key={"job_id": job_id}).get("Item")
    if not item:
        return JSONResponse(
            {"error": "job not found", "job_id": job_id}, status_code=404
        )

    execution_arn = item.get("execution_arn")
    if not execution_arn:
        # Legacy row from the status-table version: still in flight on the old poller.
        body = {
            "job_id": job_id,
            "status": item.get("status", "UNKNOWN"),
            "step": item.get("step"),
            "legacy": True,
        }
        for k in ("result", "error"):
            if k in item:
                body[k] = item[k]
        return JSONResponse(body, status_code=200)

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
    return JSONResponse(body, status_code=200)


# Lambda entry point. Lifespan is off because there is no startup work to run.
lambda_handler = Mangum(app, lifespan="off")
