import json
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Data vbalidation succeded",
            "data": json.loads(event["body"])
        }),
    }