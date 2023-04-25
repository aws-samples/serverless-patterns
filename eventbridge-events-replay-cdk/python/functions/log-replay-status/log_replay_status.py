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
    action = event["taskresult"]["Payload"]["action"]

    if action == "failed":
        logger.info(f"Replay {event['taskresult']['Payload']['replay_name']} failed")
    elif action == "success":
        logger.info(
            f"Replay {event['taskresult']['Payload']['replay_name']} successful"
        )
