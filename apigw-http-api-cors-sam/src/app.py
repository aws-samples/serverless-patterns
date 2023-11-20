import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello there! You just created an HTTP API with CORS"
        })
    }
