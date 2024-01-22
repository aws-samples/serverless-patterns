import json
from http import HTTPStatus


def handler(event, context):
    response = {
        "statusCode": int(HTTPStatus.OK),
        "body": json.dumps({"message": "Hi from AWS_IAM auth enabled API"})
    }
    return response
