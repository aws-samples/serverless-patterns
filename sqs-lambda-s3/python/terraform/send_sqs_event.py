import boto3
from botocore.config import Config
import json
import uuid


config = Config(region_name='ap-south-1')
sqs_client = boto3.client('sqs',
                          config=config)
uniq_id = str(uuid.uuid4())
response = sqs_client.send_message(
    QueueUrl='event-collector-queue',
    MessageBody=json.dumps({"status": 200, "uniqueID": uniq_id})
    )
print(response)
