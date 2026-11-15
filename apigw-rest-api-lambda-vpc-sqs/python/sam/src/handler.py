import json
import boto3
import os

def lambda_handler(event, context):
 
    body=json.loads(event['body'])
    sqs = boto3.client('sqs')
    url=os.getenv('SQSqueueName')
    msg=sqs.send_message(QueueUrl=os.getenv('SQSqueueName'),MessageBody=body['message'])
    return {
        'statusCode': 200,
        'body': json.dumps('Message has been sent to SQS Queue')
    }