import json

# import requests


def lambda_handler(event, context):


    print("Sample App 1 Log - To show how the log is captured by the extension and send to s3")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Sample App 1 Return",
        }),
    }
