import logging
import json
import boto3
import os

from botocore.exceptions import ClientError


def lambda_handler(event, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))

    try:
        topic_arn = os.environ.get('TOPIC_ARN')
        if not topic_arn:
            logger.error("Missing TOPIC_ARN environment variable")
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Server configuration error"})
            }

        sns_client = boto3.client("sns")
        sent_message = sns_client.publish(
            TargetArn=topic_arn,
            Message=json.dumps({'default': json.dumps(event)})
        )

        logger.info(f"Success - Message ID: {sent_message['MessageId']}")
        return {
            "statusCode": 200,
            "body": json.dumps({"status": "Success", "messageId": sent_message['MessageId']})
        }

    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        logger.error(f"ClientError: {error_code} - {error_message}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to publish message to SNS"})
        }
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }