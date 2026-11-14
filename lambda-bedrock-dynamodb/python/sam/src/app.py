import json
import boto3
import os

bedrock = boto3.client('bedrock-runtime')
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['table_name']

model_id = os.environ['model_ID']

def lambda_handler(event, context):

    messages = {
    "role": "user",
    "content": [{"text": event['query']}]}

    response = bedrock.converse(
        modelId=model_id,
        messages=[messages]
    )

    # Store the response in DynamoDB
    table = dynamodb.Table(table_name)
    item = {
        'id': str(context.aws_request_id),
        'query': event['query'],
        'response': response
    }
    table.put_item(Item=item)

    return {
        'statusCode': 200
    }
