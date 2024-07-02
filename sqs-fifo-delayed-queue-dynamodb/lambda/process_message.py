# create python lambda function
# import json
import boto3
import os
import time

dynamodb = boto3.resource('dynamodb')
sqs = boto3.client('sqs')
table = dynamodb.Table(os.environ['TABLE_NAME'])

# Message delay and TTL for dynamodb item is 60 seconds
message_delay_seconds = 60 

def handler(event, context):
    batch_item_failures = []
    sqs_batch_response = {}

    # iterate sqs messages based on message group id
    for record in event['Records']:
        # get message group id
        message_group_id = record['attributes']['MessageGroupId']

        # get message body
        message_body = record['body']

        # query records with customer_id as message_group_id
        response = table.get_item(
            Key={
                'customer_id': message_group_id
            })
        
        # if response does not return a record
        if ('Item' in response):
            # get the item
            response_item = response['Item']
            
            # get the exprying time of the item from response_item
            item_ttl_epoch_seconds = response_item['ttl']

            # if TTL has expired, send the message body to downstream sqs queue and update the dynamodb table with a new TTL, else place the item back on the delay queue
            if (item_ttl_epoch_seconds - int(time.time()) < 0):
                process_message(message_body, message_group_id)
            else:
                message_id = record['messageId']
                # print(f'Message with id "{message_id}" has not expired yet, adding to batch item failures')
                batch_item_failures.append({"itemIdentifier": record['messageId']})
        else:
            # if no records found, send message to downstream sqs queue and update the dynamodb table with a ttl
            process_message(message_body, message_group_id)

    sqs_batch_response["batchItemFailures"] = batch_item_failures

    return sqs_batch_response
            
def process_message(message_body, message_group_id):
    # send message to downstream sqs queue
    expiry_epoch_time = int(time.time()) + message_delay_seconds
    sqs.send_message(
        QueueUrl=os.environ['QUEUE_URL'],
        MessageBody=message_body,
        MessageGroupId=message_group_id
    )        

    # Update Dynamodb table called CustomerTable with customer_id as partition key and created_timestamp as sort key with the ISO 8601 timestamp
    table.put_item(
        Item={
            'customer_id': message_group_id,
            'ttl': expiry_epoch_time
        }
    )