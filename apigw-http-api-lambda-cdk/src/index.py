from http import HTTPStatus
import json
import os

def handler(event, context):
    try:
        body={
            # https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
            "aws_request_id": context.aws_request_id,
            "memory_limit_in_mb": context.memory_limit_in_mb,
            "remaining_time_in_millis": context.get_remaining_time_in_millis(),

            # https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html
            "cookies": event.get("cookies", []),
            "headers": event.get("headers", {}),
            "queryStringParameters": event.get("queryStringParameters", {}),
            "pathParameters": event.get("pathParameters", {}),

            # https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
            "environ": dict(os.environ), 
        }

        response = {
            "isBase64Encoded": False,
            "statusCode": HTTPStatus.OK.value,
            "body": json.dumps(body, indent=2),
            "headers": {
                "content-type": "application/json",
            },
        }

    except Exception as e:
        response = {
            "isBase64Encoded": False,
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR.value,
            "body": f"Exception={e}",
            "headers": {
                "content-type": "text/plain",
            },
        }

    return response