"""
BEFORE - the poller.

Runs every minute. Scans the table for PENDING (or stale RUNNING) rows,
claims one with a conditional update, runs the steps, and writes progress
back after every step so a crash can be resumed by the next poll.

Everything in this file is the "where was I?" bookkeeping that durable
functions do for you. Compare with after/job.py.
"""

import logging
import os
import time
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Attr
from steps import TransientError, fetch_source, publish_result, transform

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["JOBS_TABLE"])

# A RUNNING row older than this is assumed crashed and is picked up again.
STALE_AFTER_SECONDS = 120
MAX_ATTEMPTS = 3


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _now() -> int:
    return int(time.time())


def _update(
    job_id: str,
    fields: dict,
    condition: str | None = None,
    cond_values: dict | None = None,
) -> None:
    """SET the given fields. Every name is aliased: status, error and result
    are DynamoDB reserved words, and a bare name in an UpdateExpression fails."""
    names = {f"#f{i}": k for i, k in enumerate(fields)}
    values = {f":v{i}": v for i, v in enumerate(fields.values())}
    expr = "SET " + ", ".join(f"#f{i} = :v{i}" for i in range(len(fields)))
    kwargs = {
        "Key": {"job_id": job_id},
        "UpdateExpression": expr,
        "ExpressionAttributeNames": names,
        "ExpressionAttributeValues": {**values, **(cond_values or {})},
    }
    if condition:
        kwargs["ConditionExpression"] = condition
    table.update_item(**kwargs)


def _claim(job: dict) -> bool:
    """Take ownership of a row. Returns False if another poller got it first."""
    try:
        _update(
            job["job_id"],
            {"status": "RUNNING", "updated_at": _now()},
            condition="#f0 = :pending OR (#f0 = :running AND #f1 < :stale)",
            cond_values={
                ":pending": "PENDING",
                ":running": "RUNNING",
                ":stale": _now() - STALE_AFTER_SECONDS,
            },
        )
        return True
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        return False


def _checkpoint(job_id: str, step: str, outputs: dict) -> None:
    """Persist all step outputs so far so a restart can skip finished steps."""
    _update(job_id, {"step": step, "outputs": outputs, "updated_at": _now()})


def _finish(job_id: str, status: str, **fields) -> None:
    _update(job_id, {"status": status, "updated_at": _now(), **fields})


def _run_job(job: dict) -> None:
    job_id = job["job_id"]
    payload = job.get("payload", {})
    outputs = dict(job.get("outputs") or {})
    attempts = int(job.get("attempts", Decimal(0)))

    try:
        # Each step: skip if a previous attempt already finished it, else run and checkpoint.
        if "fetch_source" not in outputs:
            outputs["fetch_source"] = fetch_source(job_id, payload)
            _checkpoint(job_id, "fetch_source", outputs)

        if "transform" not in outputs:
            outputs["transform"] = transform(
                job_id, outputs["fetch_source"], attempt=attempts + 1
            )
            _checkpoint(job_id, "transform", outputs)

        if "publish_result" not in outputs:
            outputs["publish_result"] = publish_result(job_id, outputs["transform"])
            _checkpoint(job_id, "publish_result", outputs)

        _finish(job_id, "DONE", result=outputs["publish_result"])
        logger.info("job %s DONE", job_id)

    except TransientError as exc:
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            logger.error("job %s FAILED after %d attempts: %s", job_id, attempts, exc)
            _finish(job_id, "FAILED", error=str(exc), attempts=attempts)
        else:
            # Put it back for the next poll. No backoff, no jitter: you would add those by hand.
            logger.warning(
                "job %s attempt %d failed, requeued: %s", job_id, attempts, exc
            )
            _finish(job_id, "PENDING", error=str(exc), attempts=attempts)

    except Exception as exc:
        logger.exception("job %s FAILED", job_id)
        _finish(job_id, "FAILED", error=str(exc))


MAX_JOBS_PER_POLL = 25


def _due_jobs(stale: int) -> list[dict]:
    """Every PENDING or stale RUNNING row. Scan's Limit counts rows READ, not
    rows matched, so a single limited scan would skip pending jobs once the
    table holds more than a page of finished rows. Paginate instead."""
    kwargs = {
        "FilterExpression": Attr("status").eq("PENDING")
        | (Attr("status").eq("RUNNING") & Attr("updated_at").lt(stale)),
    }
    due: list[dict] = []
    while True:
        page = table.scan(**kwargs)
        due.extend(page.get("Items", []))
        if "LastEvaluatedKey" not in page or len(due) >= MAX_JOBS_PER_POLL:
            return due[:MAX_JOBS_PER_POLL]
        kwargs["ExclusiveStartKey"] = page["LastEvaluatedKey"]


def lambda_handler(event: dict, context) -> dict:
    processed = 0
    for job in _due_jobs(stale=_now() - STALE_AFTER_SECONDS):
        if _claim(job):
            _run_job(job)
            processed += 1
    return {"processed": processed}
