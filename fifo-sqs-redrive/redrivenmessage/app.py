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

    # # message = json.loads(record['body'])

    # receive_count = int(record["attributes"]["ApproximateReceiveCount"])
    # message = record["body"]
        
    # if receive_count == 1:
    #     # Raise exception if receive count is 1
    #     raise Exception('Failed to process message')
        
    # # Otherwise process message successfully    
    # message_data = json.loads(message)
    # print(f"Processed message: {message_data}")
    
    # # Process message but fail on purpose
    # # if message['id'] % 3 == 0:
    # # raise Exception('Failed to process message')
    
    # # # Delete message if processed successfully 
    # sqs.delete_message(
    #   QueueUrl=os.environ['QUEUE_URL'],
    #   ReceiptHandle=record['receiptHandle']
    # )