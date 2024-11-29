import json
# import requests
import time

def lambda_handler(event, context):
    print("sleeping now - to produce timeout")
    time.sleep(4)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
