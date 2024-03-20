import json
import boto3
import os

sqs = boto3.client('sqs')

def lambda_handler(event, context):

  for record in event['Records']:
    message = json.loads(record['body'])

    print("Message redriven from DLQ")
    print(f"Processed message: {message}")
    # Delete message if processed successfully
    sqs.delete_message(
      QueueUrl=os.environ['QUEUE_URL'],
      ReceiptHandle=record['receiptHandle']
    )
