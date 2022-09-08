import json
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Data validation succeded",
            "data": json.loads(event["body"])
        }),
    }
