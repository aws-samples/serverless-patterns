"""
BEFORE - a FastAPI job API whose work runs IN THE WEB PROCESS.

POST /v1/jobs       -> write {job_id, status=PENDING} and start a background
                       thread that runs the steps inside this same process
GET  /v1/jobs/{id}  -> read the row and return its status

This is the shape a team already has: one FastAPI service that both takes the
request AND does the work, on a thread it spawns itself. The jobs table is the
only record of progress. It runs locally as `uvicorn api:app`; on Lambda,
Mangum adapts the ASGI app to the API Gateway proxy event unchanged.

Why this hurts: the work is tied to the web process. A deploy, a scale-in, or
a crash kills every in-flight thread, and the row is stuck at RUNNING forever.
The box is sized for the work, not the traffic. Compare with after/api.py,
where the POST returns after an SQS send and the work runs in its own Lambda.
"""

import logging
import os
import threading
import time
import uuid

import boto3
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum
from steps import TransientError, fetch_source, publish_result, transform

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["JOBS_TABLE"])

TTL_SECONDS = 3 * 24 * 60 * 60
MAX_ATTEMPTS = 3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI(title="jobs (in-process worker)", docs_url=None, redoc_url=None)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info("%s %s -> %s", request.method, request.url.path, response.status_code)
    return response


def _update(job_id: str, fields: dict, remove: list[str] | None = None) -> None:
    """SET the given fields (and REMOVE the named ones). Every name is aliased:
    status, step, error and result are DynamoDB reserved words, and a bare name
    in an UpdateExpression fails. attribute_exists stops a late update from
    phantom-creating a row (with no expires_at) after the TTL removed it."""
    names = {f"#f{i}": k for i, k in enumerate(fields)}
    values = {f":v{i}": v for i, v in enumerate(fields.values())}
    expr = "SET " + ", ".join(f"#f{i} = :v{i}" for i in range(len(fields)))
    if remove:
        names.update({f"#r{i}": k for i, k in enumerate(remove)})
        expr += " REMOVE " + ", ".join(f"#r{i}" for i in range(len(remove)))
    table.update_item(
        Key={"job_id": job_id},
        UpdateExpression=expr,
        ConditionExpression="attribute_exists(job_id)",
        ExpressionAttributeNames=names,
        ExpressionAttributeValues=values,
    )


def _run_job(job_id: str, payload: dict) -> None:
    """Run the three steps on a background thread. A crash or deploy mid-run
    leaves the row at RUNNING with no one to resume it: the cost this pattern
    removes."""
    attempt = 0
    while True:
        attempt += 1
        try:
            _update(job_id, {"status": "RUNNING", "step": "fetch_source",
                             "updated_at": int(time.time())})
            source = fetch_source(job_id, payload)
            _update(job_id, {"step": "transform", "updated_at": int(time.time())})
            result = transform(job_id, source, attempt=attempt)
            _update(job_id, {"step": "publish_result", "updated_at": int(time.time())})
            published = publish_result(job_id, result)
            # Clear any error from a prior failed attempt so DONE never reads
            # as DONE-with-error.
            _update(
                job_id,
                {"status": "DONE", "result": published, "updated_at": int(time.time())},
                remove=["error"],
            )
            logger.info("job %s DONE", job_id)
            return
        except TransientError as exc:
            # Retry only the transient class, by hand, in this process.
            if attempt >= MAX_ATTEMPTS:
                _update(job_id, {"status": "FAILED", "error": str(exc),
                                 "updated_at": int(time.time())})
                logger.error("job %s FAILED after %d attempts", job_id, attempt)
                return
            logger.warning("job %s attempt %d failed, retrying: %s", job_id, attempt, exc)
            time.sleep(0.5 * attempt)
        except table.meta.client.exceptions.ConditionalCheckFailedException:
            # The row is gone (TTL expired mid-run); nothing left to update.
            logger.error("job %s has no row (expired or never created); dropping", job_id)
            return
        except Exception as exc:  # a bad job must not kill the thread
            _update(job_id, {"status": "FAILED", "error": str(exc),
                             "updated_at": int(time.time())})
            logger.exception("job %s FAILED", job_id)
            return


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

    # Conditional put so a client retry with the same job_id does not reset a job.
    try:
        table.put_item(
            Item={
                "job_id": job_id,
                "status": "PENDING",
                "step": None,
                "created_at": now,
                "updated_at": now,
                "expires_at": now + TTL_SECONDS,
            },
            ConditionExpression="attribute_not_exists(job_id)",
        )
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        existing = table.get_item(Key={"job_id": job_id})["Item"]
        return JSONResponse(_row_to_body(job_id, existing), status_code=200)

    # Do the work right here, in the web process.
    threading.Thread(target=_run_job, args=(job_id, payload), daemon=True).start()
    return JSONResponse({"job_id": job_id, "status": "PENDING"}, status_code=202)


def _row_to_body(job_id: str, item: dict) -> dict:
    body = {"job_id": job_id, "status": item["status"], "step": item.get("step")}
    for k in ("result", "error"):
        if k in item:
            body[k] = item[k]
    return body


@app.get("/v1/jobs/{job_id}")
async def get_job(job_id: str) -> JSONResponse:
    item = table.get_item(Key={"job_id": job_id}).get("Item")
    if not item:
        return JSONResponse({"error": "job not found", "job_id": job_id}, status_code=404)
    return JSONResponse(_row_to_body(job_id, item), status_code=200)


# Lambda entry point. Lifespan is off because there is no startup work to run.
# NOTE: on Lambda the background thread is best-effort only - the invocation can
# be frozen the moment the handler returns. This "before" runs its work properly
# only on a long-lived server (uvicorn), which is exactly the constraint the
# "after" removes.
lambda_handler = Mangum(app, lifespan="off")
