import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info(json.dumps(event, indent=2))

    # [ERROR] TypeError: Object of type LambdaContext is not JSON serializable
    # logging.info(json.dumps(context, indent=2))

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
