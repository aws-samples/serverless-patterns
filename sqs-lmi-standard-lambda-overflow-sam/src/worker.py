"""Shared SQS worker. Runs unchanged on Lambda Managed Instances and on Standard Lambda.

Both tiers consume the same queue, so both tiers must run the same code. The only
difference between them is the COMPUTE_TIER environment variable, which is used purely
for labelling metrics.
"""

import json
import logging
import os
import time

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Use a boto3 client, not a boto3 resource. Under Lambda Managed Instances one
# execution environment runs up to PerExecutionEnvironmentMaxConcurrency invocations
# concurrently on separate threads, and they all share this module-level object.
# boto3 clients are thread-safe; boto3 resources are not.
dynamodb = boto3.client("dynamodb")

IDEMPOTENCY_TABLE = os.environ["IDEMPOTENCY_TABLE"]
COMPUTE_TIER = os.environ["COMPUTE_TIER"]
METRIC_NAMESPACE = os.environ["METRIC_NAMESPACE"]
WORK_DURATION_MS = int(os.environ.get("WORK_DURATION_MS", "1000"))
WORK_MODE = os.environ.get("WORK_MODE", "cpu")
RECORD_TTL_SECONDS = 86400

STATUS_IN_PROGRESS = "IN_PROGRESS"
STATUS_DONE = "DONE"


def claim(work_item_id):
    """Reserve a work item for processing. Returns False if it is already complete.

    The claim and the completion are two separate writes. A single write before
    processing would turn any retryable processing failure into silent data loss: the
    redelivery would see the existing record, treat the message as a duplicate, and
    delete it without ever doing the work.
    """
    now = int(time.time())
    try:
        dynamodb.put_item(
            TableName=IDEMPOTENCY_TABLE,
            Item={
                "work_item_id": {"S": work_item_id},
                "status": {"S": STATUS_IN_PROGRESS},
                "tier": {"S": COMPUTE_TIER},
                "claimed_at": {"N": str(now)},
                "expires_at": {"N": str(now + RECORD_TTL_SECONDS)},
            },
            # Claim if we have never seen this item, or if a previous attempt claimed it
            # but did not finish. Only a completed item is a true duplicate.
            ConditionExpression="attribute_not_exists(work_item_id) OR #status <> :done",
            ExpressionAttributeNames={"#status": "status"},
            ExpressionAttributeValues={":done": {"S": STATUS_DONE}},
        )
        return True
    except ClientError as error:
        if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return False
        raise


def complete(work_item_id):
    now = int(time.time())
    dynamodb.update_item(
        TableName=IDEMPOTENCY_TABLE,
        Key={"work_item_id": {"S": work_item_id}},
        UpdateExpression="SET #status = :done, completed_at = :now, expires_at = :expires_at",
        ExpressionAttributeNames={"#status": "status"},
        ExpressionAttributeValues={
            ":done": {"S": STATUS_DONE},
            ":now": {"N": str(now)},
            ":expires_at": {"N": str(now + RECORD_TTL_SECONDS)},
        },
    )


def do_work(payload):
    """Stand-in for the real business operation.

    WORK_MODE controls which resource the workload consumes, and therefore which LMI
    throttle-reason metric fires:

    * cpu   - real arithmetic for WORK_DURATION_MS. Saturates vCPU as well as
              concurrency, so both CPUThrottles and ConcurrencyThrottles appear. This
              is the mode that reproduces a CPU-bound production workload.
    * sleep - occupies a concurrency slot without consuming CPU. Only
              ConcurrencyThrottles appears. Cheaper, and still a valid scale signal,
              because LMI scales on CPU utilisation *and* multi-concurrency saturation.

    Replace this function with an idempotent business operation.
    """
    deadline = time.monotonic() + (WORK_DURATION_MS / 1000.0)
    if WORK_MODE == "sleep":
        time.sleep(max(0.0, deadline - time.monotonic()))
        return

    accumulator = 0.0
    while time.monotonic() < deadline:
        # A tight inner loop keeps the monotonic() call count low enough that the clock
        # check is not itself the dominant cost.
        for value in range(2000):
            accumulator += value * value
    return accumulator


def emit_metrics(processed, failed, wait_millis):
    """Emit CloudWatch embedded metric format so the dashboard can chart each tier.

    One log line per batch. Dimensioned on Tier so LMI throughput and Standard Lambda
    throughput can be stacked on the same graph.
    """
    document = {
        "_aws": {
            "Timestamp": int(time.time() * 1000),
            "CloudWatchMetrics": [
                {
                    "Namespace": METRIC_NAMESPACE,
                    "Dimensions": [["Tier"]],
                    "Metrics": [
                        {"Name": "MessagesProcessed", "Unit": "Count"},
                        {"Name": "MessagesFailed", "Unit": "Count"},
                        {"Name": "QueueWaitMillis", "Unit": "Milliseconds"},
                    ],
                }
            ],
        },
        "Tier": COMPUTE_TIER,
        "MessagesProcessed": processed,
        "MessagesFailed": failed,
        "QueueWaitMillis": wait_millis,
    }
    print(json.dumps(document))


def queue_wait_millis(record):
    """Time from SQS enqueue to the start of this invocation.

    This is the number that matters to the customer: it shows the burst tier capping
    latency while LMI is still scaling up.
    """
    try:
        sent_at = int(record["attributes"]["SentTimestamp"])
    except (KeyError, TypeError, ValueError):
        return None
    return max(0, int(time.time() * 1000) - sent_at)


def lambda_handler(event, context):
    records = event.get("Records", [])
    failures = []
    processed = 0
    waits = []

    for record in records:
        message_id = record["messageId"]
        wait = queue_wait_millis(record)
        if wait is not None:
            waits.append(wait)

        try:
            payload = json.loads(record["body"])
            # Fall back to the SQS message ID when the producer does not supply a
            # business key. A business key is better: it survives a producer retry.
            work_item_id = str(payload.get("workItemId", message_id))

            if not claim(work_item_id):
                logger.info("Work item %s already completed; skipping", work_item_id)
                continue

            do_work(payload)
            complete(work_item_id)
            processed += 1
        except Exception:
            logger.exception("Failed to process SQS record %s", message_id)
            # The item stays IN_PROGRESS, so the redelivery reprocesses it rather than
            # mistaking it for a duplicate.
            failures.append({"itemIdentifier": message_id})

    if records:
        # Skip the metric on an empty invocation: a QueueWaitMillis of 0 would pull the
        # percentile statistics down and hide the latency the burst tier is preventing.
        emit_metrics(processed, len(failures), max(waits) if waits else 0)
    return {"batchItemFailures": failures}
