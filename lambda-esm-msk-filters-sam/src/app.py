import json
import base64

def lambda_handler(event, context):
    records = event["records"]
    for partition in records:
        base64EventValue = records[partition][0]["value"]
        print("Event from topic: " +  base64ToString(base64EventValue))
    return {
        'statusCode': 200,
        'body': json.dumps('MSK ESM filter patterns demo')
    }

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')
