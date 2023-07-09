import json

def lambda_handler(event, context):
    print(event)

    return {
        'statusCode': 200,
        'event': json.dumps(event)
    }