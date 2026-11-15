import json
import boto3
import os

sqs = boto3.client('sqs')

def lambda_handler(event, context):

  for record in event['Records']:
    message = json.loads(record['body'])
    print(message)
    raise Exception('Failed to process message')

 