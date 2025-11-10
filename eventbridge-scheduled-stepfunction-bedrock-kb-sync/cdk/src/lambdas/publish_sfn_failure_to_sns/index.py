"""
This is the handler for the Lambda function that will be triggered by the Step Function for
publishing the operational issues to SNS TOPIC.
"""

import json
import os
from typing import Union

import boto3
from aws_lambda_powertools import Logger

logger = Logger()


def find_keyvalue_in_dict(key: str, dictionary: dict) -> Union[str, dict]:
    """Find a key in a dictionary of arbitrary complexity at any position.

    Returns as soon as first key is found that matches.
    """
    for k, v in dictionary.items():
        if k == key:
            return v
        if isinstance(v, dict):
            result = find_keyvalue_in_dict(key, v)
            if result:
                return result
    return None


def publish_to_sns(message, original_message):
    """Publish message to SNS TOPIC
    Args:
        message (str): Message to be published
        original_message (dict): Original message received from the Step Function
    Returns:
        None
    """

    operation_sns_topic_arn = os.environ["SNS_TOPIC"]

    client_sns = boto3.client("sns", region_name="us-west-2")
    logger.info("Publishing message to SNS TOPIC: %s", operation_sns_topic_arn)
    subject_raw = (
        f'[{original_message["severity"]}]'
        f'ai-chat-support-operational-issue:{original_message["errorStatus"]}:{original_message["affectedResourceName"]}'
    )
    subject = (subject_raw[:97] + "..") if len(subject_raw) > 99 else subject_raw
    logger.info("Subject: %s", subject)
    client_sns.publish(TopicArn=operation_sns_topic_arn, Message=message, Subject=subject)


def handler(event: dict, context):
    # pylint: disable=unused-argument
    """
    Normalization the failure message and publish to SNS TOPIC:
    """
    # Extract all information from event!
    logger.info("-- Handler received event: %s", event)
    output_message = {}

    detail = event.get("detail", None)

    if "source" in event and event["source"] == "aws.states":
        # This is a Step Function event
        output_message["affectedResourceName"] = find_keyvalue_in_dict("stateMachineArn", detail).split(":")[-1]
        output_message["severity"] = "CRITICAL"
        output_message["errorStatus"] = find_keyvalue_in_dict("status", detail)
        output_message["affectedResourceArn"] = find_keyvalue_in_dict("stateMachineArn", detail)
        output_message["originalError"] = event
        message = json.dumps(output_message, indent=4, sort_keys=False)
        publish_to_sns(message, output_message)
    else:
        # This is an unknown error event type
        output_message["affectedResourceName"] = "UNKNOWN"
        output_message["severity"] = "UNKNOWN"
        output_message["errorStatus"] = "ERROR"
        output_message["affectedResourceArn"] = "Undefined"
        output_message["originalError"] = event
        message = json.dumps(output_message, indent=4, sort_keys=False)
        publish_to_sns(message, output_message)

    return output_message
