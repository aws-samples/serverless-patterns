import logging
import json
import boto3
import ast
import os

from botocore.exceptions import ClientError


def handle(event, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))

    queue_name = os.environ.get('QUEUE_NAME')

    sqs_client = boto3.client("sqs")

    queue_url = sqs_client.get_queue_url(
        QueueName=queue_name
    )["QueueUrl"]

    try:
        sent_message = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(event)
        )

        if sent_message is not None:
            logger.info(f"Success - Message ID: {sent_message['MessageId']}")
        return {
            "statusCode": 200,
            "body": json.dumps(event)
        }

    except ClientError as e:
        logger.error(e)
        return None
