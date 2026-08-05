"""
DynamoDB Streams → Lambda Durable Function.

Processes stream records through a multi-step pipeline:
  1. Validate — check record integrity
  2. Enrich — add computed fields and metadata
  3. Notify — write an audit notification record

Each step is checkpointed. If the function is interrupted during processing,
it resumes from the last checkpoint without re-executing completed steps.

Uses ReportBatchItemFailures for partial batch error handling.
"""

import os
import uuid
import logging
from datetime import datetime, timezone
from decimal import Decimal

import boto3
from aws_durable_execution_sdk_python.context import DurableContext, StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
processed_table = dynamodb.Table(os.environ["PROCESSED_TABLE"])
notifications_table = dynamodb.Table(os.environ["NOTIFICATIONS_TABLE"])


@durable_step
def validate_record(step_context: StepContext, record: dict) -> dict:
    """Step 1: Validate the stream record has required fields."""
    step_context.logger.info("Validating record: %s", record.get("pk"))

    event_name = record.get("event_name")
    new_image = record.get("new_image", {})

    if event_name == "REMOVE":
        # Deletions are valid but we skip enrichment
        return {"valid": True, "skip_processing": True, "event_name": event_name}

    # Validate required fields for INSERT/MODIFY
    required_fields = ["pk", "name"]
    missing = [f for f in required_fields if f not in new_image]

    if missing:
        raise UnrecoverableInvocationError(
            f"Record missing required fields: {missing}"
        )

    return {
        "valid": True,
        "skip_processing": False,
        "event_name": event_name,
        "data": new_image,
    }


@durable_step
def enrich_record(step_context: StepContext, validation: dict) -> dict:
    """Step 2: Enrich the record with computed fields."""
    step_context.logger.info("Enriching record: %s", validation["data"].get("pk"))

    data = validation["data"]
    now = datetime.now(timezone.utc).isoformat()

    # Add enrichment fields
    enriched = {
        "pk": data["pk"],
        "name": data["name"],
        "category": data.get("category", "UNCATEGORIZED"),
        "event_type": validation["event_name"],
        "processed_at": now,
        "name_length": len(data.get("name", "")),
        "has_description": "description" in data,
    }

    # Write enriched record to processed table
    processed_table.put_item(Item=enriched)

    return enriched


@durable_step
def send_notification(step_context: StepContext, enriched: dict) -> dict:
    """Step 3: Create an audit notification for the processed record."""
    step_context.logger.info("Sending notification for: %s", enriched["pk"])

    notification_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()

    notification = {
        "notification_id": notification_id,
        "record_pk": enriched["pk"],
        "event_type": enriched["event_type"],
        "message": f"Record '{enriched['name']}' was processed (event: {enriched['event_type']})",
        "created_at": now,
    }

    notifications_table.put_item(Item=notification)

    return {"notification_id": notification_id, "status": "SENT"}


@durable_execution
def lambda_handler(event, context: DurableContext) -> dict:
    """
    Process DynamoDB stream records through a checkpointed pipeline.
    Returns batch item failures for records that could not be processed.
    """
    batch_item_failures = []

    for record in event.get("Records", []):
        event_id = record.get("eventID", "unknown")

        try:
            # Extract stream record data
            stream_record = {
                "pk": record.get("dynamodb", {}).get("Keys", {}).get("pk", {}).get("S", ""),
                "event_name": record.get("eventName", ""),
                "new_image": _deserialize_image(
                    record.get("dynamodb", {}).get("NewImage", {})
                ),
                "old_image": _deserialize_image(
                    record.get("dynamodb", {}).get("OldImage", {})
                ),
            }

            # Step 1: Validate
            validation = context.step(validate_record(stream_record))

            if validation.get("skip_processing"):
                context.logger.info("Skipping REMOVE event for %s", stream_record["pk"])
                continue

            # Step 2: Enrich
            enriched = context.step(enrich_record(validation))

            # Step 3: Notify
            notification = context.step(send_notification(enriched))

            context.logger.info(
                "Processed %s → notification %s",
                stream_record["pk"],
                notification["notification_id"],
            )

        except Exception as err:
            context.logger.error("Failed to process record %s: %s", event_id, str(err))
            batch_item_failures.append({"itemIdentifier": event_id})

    return {"batchItemFailures": batch_item_failures}


def _deserialize_image(image: dict) -> dict:
    """Simple DynamoDB image deserializer for common types."""
    result = {}
    for key, value in image.items():
        if "S" in value:
            result[key] = value["S"]
        elif "N" in value:
            result[key] = value["N"]
        elif "BOOL" in value:
            result[key] = value["BOOL"]
        elif "NULL" in value:
            result[key] = None
        else:
            result[key] = str(value)
    return result
