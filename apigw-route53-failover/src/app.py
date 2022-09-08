import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Function hit",
            "Function name": context.invoked_function_arn
        }),
    }