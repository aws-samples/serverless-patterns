import boto3
import json
import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

events_client = boto3.client("events")


def handler(event, context):
    logger.setLevel(logging.INFO)

    replay_name = event["taskresult"]["Payload"]["replay_name"]

    response = events_client.describe_replay(ReplayName=replay_name)

    describe_replay_output = {"action": "failed", "replay_name": replay_name}

    if response["State"] in ["STARTING", "RUNNING", "CANCELLING"]:
        describe_replay_output = {"action": "recheck", "replay_name": replay_name}
    elif response["State"] in ["CANCELLED", "FAILED"]:
        describe_replay_output = {"action": "failed", "replay_name": replay_name}
    elif response["State"] in ["COMPLETED"]:
        describe_replay_output = {"action": "success", "replay_name": replay_name}

    logger.info(f"Describe event response: {response}")

    return describe_replay_output
