import os
import boto3

queue_url = os.environ.get("QUEUE_URL")

client_sqs = boto3.client("sqs")

received_messages = client_sqs.receive_message(QueueUrl=queue_url, AttributeNames=["SentTimestamp"],
                                               MaxNumberOfMessages=1,
                                               MessageAttributeNames=["All"], VisibilityTimeout=0, WaitTimeSeconds=0)

for message in received_messages["Messages"]:
    receipt_handle = message["ReceiptHandle"]

    body = message["Body"]
    print(f"body: {body}")

    client_sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
