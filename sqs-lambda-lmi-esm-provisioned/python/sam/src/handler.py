import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    batch_item_failures = []

    for record in event.get("Records", []):
        try:
            body = json.loads(record["body"])
            logger.info("Processing message", extra={"message_id": record["messageId"], "body": body})
        except Exception as e:
            logger.error("Failed to process record %s: %s", record["messageId"], e)
            batch_item_failures.append({"itemIdentifier": record["messageId"]})

    return {"batchItemFailures": batch_item_failures}
