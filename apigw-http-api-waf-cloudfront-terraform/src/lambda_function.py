import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Return Lambda mock response
def lambda_handler(event, context):
    logger.info(f"event: {event}")
    logger.info(f"context {context}")
    return {"statusCode": 200, "body": "Hello from Lambda!"}
