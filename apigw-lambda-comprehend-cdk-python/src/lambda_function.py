import boto3
import os
import logging
import json
from botocore.exceptions import ClientError

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)

region_name = os.getenv("region", "us-east-1")
comprehend_obj = boto3.client("comprehend", region_name=region_name)


def lambda_handler(event, context):
    """
    :param event: Input from the user, through API Gateway
    :param context: Any methods and properties that provide information about the invocation, function, and execution environment
    :return: THe response from Comprehend service about the Sentiment of the user input.
    """
    try:
        LOG.info(f"Event is {event}")
        LOG.info(event['body'])
        user_input = json.loads(event['body'])['input']
        response = comprehend_obj.detect_sentiment(Text=user_input, LanguageCode="en")
        LOG.info(response)
        LOG.info(f"Sentiment detect is {response['Sentiment']}!!")
    except ClientError:
        LOG.error("Sentiment detection failed!!")
        raise
    else:
        return response
