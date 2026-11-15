import logging
import json
import boto3

from botocore.exceptions import ClientError

def main(event, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))

    sns_client = boto3.client("sns")
    topic_arn = event['topic_arn']


    try:
        sent_message = sns_client.publish(
            TopicArn=topic_arn,
            Message=json.dumps(event['message'])
        )

        if sent_message is not None:
            logger.info(f"Success - Message ID: {sent_message['MessageId']}")
        return {
            "statusCode": 200,
            "body": json.dumps(event['message'])
        }

    except ClientError as e:
        logger.error(e)
        return None
