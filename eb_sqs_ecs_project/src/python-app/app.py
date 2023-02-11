import boto3
import os


sqs = boto3.client('sqs');

queue_url = os.environ['queueUrl'];

def read_sqs():
    print(f"Reading queue- {queue_url}")
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    key_to_lookup = 'Messages'
    if key_to_lookup in response:
        return response['Messages']
    else:
        print(f"The queue is empty")
        return None


def delete_sqs_message(receipt_handle):
    print(f"Deleting message {receipt_handle}")
    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

# Read SQS
messages = read_sqs()
print(f"Found messages {messages}")
#size = len(inp_lst)
if messages is None: 
    print("No messages in the queue")   
else:
    for message in messages:
    # Take custom actions based on the message contents
        print(f"Activating {message}")
        print(f"Hello")

        # Delete Message 
        delete_sqs_message(message['ReceiptHandle'])
        print(f"Finished for {message}")
       
