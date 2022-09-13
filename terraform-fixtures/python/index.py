import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info(json.dumps(event, indent=2))
    logging.info(json.dumps(context, indent=2))

    eventObject = {
        "hello": "Hello Python! Hello Terraform!",
        "functionName": context.function_name,
        "event": event
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(eventObject)
    }
