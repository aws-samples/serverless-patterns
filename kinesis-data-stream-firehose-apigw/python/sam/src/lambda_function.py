import json
import time

def lambda_handler(event, context):
    print(event)

    body =  {
        "requestId": event["headers"]["X-Amz-Firehose-Request-Id"],
        "timestamp": int(time.time() * 1000)
    }

    output = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    print(output)
    return output