"""
Lambda handler that processes SQS messages and writes items to DynamoDB.
Uses ReportBatchItemFailures for partial batch error handling.
"""

import json
import os
import logging
from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def handler(event, context):
    """
    Process SQS batch and write items to DynamoDB.
    Returns batch item failures for messages that could not be processed.
    """
    batch_item_failures = []

    for record in event["Records"]:
        message_id = record["messageId"]

        try:
            item = parse_message(record["body"])
            write_to_dynamodb(item)
            logger.info("Successfully processed message %s", message_id)

        except (json.JSONDecodeError, KeyError, TypeError) as err:
            # Malformed message — will never succeed on retry
            # Still report as failure so it routes to DLQ after max retries
            logger.error(
                "Invalid message format for %s: %s", message_id, str(err)
            )
            batch_item_failures.append({"itemIdentifier": message_id})

        except ClientError as err:
            # DynamoDB error — may succeed on retry
            logger.error(
                "DynamoDB error for %s: %s",
                message_id,
                err.response["Error"]["Message"],
            )
            batch_item_failures.append({"itemIdentifier": message_id})

        except Exception as err:
            # Unexpected error — report failure for retry
            logger.error(
                "Unexpected error for %s: %s", message_id, str(err)
            )
            batch_item_failures.append({"itemIdentifier": message_id})

    logger.info(
        "Batch complete. Total: %d, Succeeded: %d, Failed: %d",
        len(event["Records"]),
        len(event["Records"]) - len(batch_item_failures),
        len(batch_item_failures),
    )

    return {"batchItemFailures": batch_item_failures}


def parse_message(body):
    """Parse and validate the SQS message body."""
    item = json.loads(body)

    # Validate required fields
    if "id" not in item:
        raise KeyError("Missing required field: id")

    return {
        "id": item["id"],
        "name": item.get("name", ""),
        "timestamp": item.get("timestamp", datetime.now(timezone.utc).isoformat()),
        "processed_at": datetime.now(timezone.utc).isoformat(),
    }


def write_to_dynamodb(item):
    """Write an item to the DynamoDB table."""
    table.put_item(Item=item)
