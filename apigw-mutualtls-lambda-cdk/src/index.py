from http import HTTPStatus
import json
import os

def handler(event, context):
    try:
        body={
            "MutualTLS": "Success"
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
