import json

def lambda_handler(event, context):
    # TODO implement
    print("Connection has been disconnected")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

