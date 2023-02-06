import logging
import json
import boto3
import os
import zlib

from base64 import b64decode
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))
    
    compressed_payload = b64decode(event["awslogs"]["data"])
    json_payload = zlib.decompress(compressed_payload, 16+zlib.MAX_WBITS)
    #return json.loads(json_payload)

    topic_arn = os.environ.get('TOPIC_ARN')

    sns_client = boto3.client("sns")

    try:
        sent_message = sns_client.publish(
            TargetArn=topic_arn,
            Message=json.dumps({'default': json.loads(json_payload)})
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