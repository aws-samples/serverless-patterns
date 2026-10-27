"""
AFTER - the job as an SQS-triggered Lambda consumer.

Same three steps as before/api.py ran on a thread. The difference is what is
NOT here: no web server, no request handling. One SQS message in, the steps
run, the same table row moves PENDING -> RUNNING -> DONE/FAILED.

What SQS + Lambda gives you that the in-process thread did not:
  - redelivery: a crash mid-job leaves the message unacked; SQS redelivers it
    after the visibility timeout, so the job is retried instead of stranded.
  - a dead-letter queue: a message that fails maxReceiveCount times is parked
    in the DLQ for inspection instead of looping forever.
  - partial batch response: only the messages that failed are redelivered,
    not the whole batch.
  - independent scaling: the API and the worker scale on their own.
"""

import json
import logging
import os
import time

import boto3
from steps import TransientError, fetch_source, publish_result, transform

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["JOBS_TABLE"])

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _update(job_id: str, fields: dict, remove: list[str] | None = None) -> None:
    """SET the given fields (and REMOVE the named ones). Every name is aliased:
    status, step, error and result are DynamoDB reserved words."""
    names = {f"#f{i}": k for i, k in enumerate(fields)}
    values = {f":v{i}": v for i, v in enumerate(fields.values())}
    expr = "SET " + ", ".join(f"#f{i} = :v{i}" for i in range(len(fields)))
    if remove:
        names.update({f"#r{i}": k for i, k in enumerate(remove)})
        expr += " REMOVE " + ", ".join(f"#r{i}" for i in range(len(remove)))
    table.update_item(
        Key={"job_id": job_id},
        UpdateExpression=expr,
        ExpressionAttributeNames=names,
        ExpressionAttributeValues=values,
    )


def _run_one(job_id: str, payload: dict, attempt: int) -> None:
    """Run the steps once. attempt is the SQS receive count: the transform's
    transient failure clears on redelivery, so a flaky job succeeds on its
    second delivery with no in-process retry loop."""
    _update(job_id, {"status": "RUNNING", "step": "fetch_source",
                     "updated_at": int(time.time())})
    source = fetch_source(job_id, payload)
    _update(job_id, {"step": "transform", "updated_at": int(time.time())})
    result = transform(job_id, source, attempt=attempt)
    _update(job_id, {"step": "publish_result", "updated_at": int(time.time())})
    published = publish_result(job_id, result)
    # Clear any error from a prior failed delivery so DONE never reads as
    # DONE-with-error.
    _update(
        job_id,
        {"status": "DONE", "result": published, "updated_at": int(time.time())},
        remove=["error"],
    )
    logger.info("job %s DONE on attempt %d", job_id, attempt)


def lambda_handler(event: dict, context) -> dict:
    """SQS batch handler. Returns batchItemFailures so only failed messages are
    redelivered (ReportBatchItemFailures is set on the event source mapping)."""
    failures: list[dict] = []
    for record in event.get("Records", []):
        message_id = record["messageId"]
        attempt = int(record.get("attributes", {}).get("ApproximateReceiveCount", "1"))
        body = json.loads(record["body"])
        job_id = body["job_id"]
        payload = body.get("payload", {})
        try:
            _run_one(job_id, payload, attempt)
        except TransientError as exc:
            # Let SQS redeliver: do NOT mark FAILED yet. After maxReceiveCount
            # deliveries the message goes to the DLQ instead.
            logger.warning("job %s attempt %d transient failure, will redeliver: %s",
                           job_id, attempt, exc)
            _update(job_id, {"status": "RUNNING", "error": str(exc),
                             "updated_at": int(time.time())})
            failures.append({"itemIdentifier": message_id})
        except Exception as exc:  # a permanent error fails this job only
            logger.exception("job %s FAILED (permanent)", job_id)
            _update(job_id, {"status": "FAILED", "error": str(exc),
                             "updated_at": int(time.time())})
    return {"batchItemFailures": failures}
