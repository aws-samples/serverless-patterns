import boto3
import json,time


# Modify these two values accordingly to match your environment
region = 'us-east-1'
sqs_queue_url = 'https://sqs.us-east-1.amazonaws.com/451717132371/sam-app-source-queue'


client = boto3.client('sqs', region_name=region)

# test items
request = [
    {
	"order_id":"103",
	"address": "address-1",
	"amount": "50"
    },
    {
    "order_id":"104",
	"address": "address-2",
	"amount": "100"
    },
    {
    "order_id":"105",
	"address": "address-3",
	"amount": "101"
    }
]

entries = []

for i in range(len(request)):
    entry = {
        "Id" : str(i+1),
        "MessageBody" : json.dumps(request[i]),
    }
    entries.append(entry)

response = client.send_message_batch(
    QueueUrl= sqs_queue_url,
    Entries = entries
    )



