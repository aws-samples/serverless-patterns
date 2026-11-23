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

import os
import time

import boto3
from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities.batch import (
    BatchProcessor,
    EventType,
    process_partial_response,
)
from aws_lambda_powertools.utilities.data_classes.sqs_event import SQSRecord
from botocore.config import Config
from steps import TransientError, fetch_source, publish_result, transform

logger = Logger()
tracer = Tracer()  # patches boto3 so each UpdateItem becomes an X-Ray subsegment
metrics = Metrics()

# Keep SDK calls well inside the 60s function timeout.
_SDK = Config(connect_timeout=2, read_timeout=5, retries={"mode": "standard", "max_attempts": 3})
dynamodb = boto3.resource("dynamodb", config=_SDK)
table = dynamodb.Table(os.environ["JOBS_TABLE"])

# One SQS record at a time; a failing record is reported back as a
# batchItemFailure so only it is redelivered. raise_on_entire_batch_failure is
# off so a batch of nothing but bad messages still returns the item list
# instead of failing the invocation.
processor = BatchProcessor(event_type=EventType.SQS, raise_on_entire_batch_failure=False)


def _update(job_id: str, fields: dict, remove: list[str] | None = None) -> None:
    """SET the given fields (and REMOVE the named ones) on an EXISTING row.
    Every name is aliased: status, step, error and result are DynamoDB reserved
    words. attribute_exists stops a redelivered message from phantom-creating a
    row (with no expires_at) after the TTL removed the original."""
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


@tracer.capture_method
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
    metrics.add_metric(name="JobsDone", unit=MetricUnit.Count, value=1)
    logger.info("job DONE", job_id=job_id, attempt=attempt)


@tracer.capture_method
def record_handler(record: SQSRecord) -> None:
    """One SQS message. Raising reports the message as a batch item failure, so
    SQS redelivers it and, after maxReceiveCount, moves it to the DLQ."""
    attempt = int(record.attributes.approximate_receive_count or "1")
    # A body that is not JSON raises here (-> redeliver -> DLQ); so does a JSON
    # value that is not a job object. Neither can identify a row to mark FAILED.
    body = record.json_body
    if not isinstance(body, dict) or not body.get("job_id"):
        raise ValueError("message is not a job object with a job_id")
    job_id = body["job_id"]
    try:
        _run_one(job_id, body.get("payload") or {}, attempt)
    except TransientError as exc:
        # Let SQS redeliver: do NOT mark FAILED yet. The row stays RUNNING; the
        # error is recorded only when the job ends FAILED, so a GET during the
        # redelivery window never shows RUNNING-with-error.
        logger.warning("transient failure, will redeliver", job_id=job_id,
                       attempt=attempt, error=str(exc))
        raise
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        # No row: it expired (TTL) or was never created. Nothing to update and
        # nothing to retry; consume the message.
        logger.error("no row for job (expired or never created); dropping message",
                     job_id=job_id)
    except Exception as exc:  # a permanent error fails this job only
        logger.exception("job FAILED (permanent)", job_id=job_id, attempt=attempt)
        metrics.add_metric(name="JobsFailed", unit=MetricUnit.Count, value=1)
        try:
            _update(job_id, {"status": "FAILED", "error": str(exc),
                             "updated_at": int(time.time())})
        except Exception:
            # Could not record the failure (table throttled, row gone). Report
            # the item so SQS redelivers it instead of losing the FAILED mark.
            logger.exception("could not mark job FAILED, will redeliver", job_id=job_id)
            raise


@logger.inject_lambda_context
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context) -> dict:
    """SQS batch handler. Returns batchItemFailures so only failed messages are
    redelivered (ReportBatchItemFailures is set on the event source mapping)."""
    return process_partial_response(event=event, record_handler=record_handler,
                                    processor=processor, context=context)
