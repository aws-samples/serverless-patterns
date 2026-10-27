"""
BEFORE - FastAPI job API backed by a status table.

POST /v1/jobs       -> write {job_id, status=PENDING, payload} to the table
GET  /v1/jobs/{id}  -> read the row and return its status

This is the web app a team already has: a FastAPI service whose only record
of a job is a row in a "jobs" table. A separate poller (worker.py) moves rows
through PENDING -> RUNNING -> DONE. Mangum adapts the ASGI app to the API
Gateway proxy event, so the same app runs on Lambda unchanged.
"""

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

TTL_SECONDS = 3 * 24 * 60 * 60

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI(title="jobs (status table)", docs_url=None, redoc_url=None)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info("%s %s -> %s", request.method, request.url.path, response.status_code)
    return response


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
    if not isinstance(payload, dict):
        return JSONResponse({"error": "body must be a JSON object"}, status_code=400)
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
        return JSONResponse(_row_to_body(job_id, existing), status_code=200)

    return JSONResponse({"job_id": job_id, "status": "PENDING"}, status_code=202)


@app.get("/v1/jobs/{job_id}")
async def get_job(job_id: str) -> JSONResponse:
    item = table.get_item(Key={"job_id": job_id}).get("Item")
    if not item:
        return JSONResponse(
            {"error": "job not found", "job_id": job_id}, status_code=404
        )
    return JSONResponse(_row_to_body(job_id, item), status_code=200)


# Lambda entry point. Lifespan is off because there is no startup work to run.
lambda_handler = Mangum(app, lifespan="off")
