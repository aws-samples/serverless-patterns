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
    event_bus_name = os.environ["EVENT_BUS_NAME"]
    event_bus_arn = os.environ["EVENT_BUS_ARN"]
    event_source_arn = os.environ["EVENT_SOURCE_ARN"]
    allow_replay_events_only_rule_arn = os.environ["ALLOW_REPLAY_EVENTS_ONLY_RULE_ARN"]
    sample_start_epoch = float(os.environ["SAMPLE_START_EPOCH"])
    sample_end_epoch = float(os.environ["SAMPLE_END_EPOCH"])

    now = datetime.now()
    date_time_now = now.strftime("%Y_%m_%d_%H_%M_%S")

    replay_name = f"{date_time_now}_{event_bus_name}"
    response = events_client.start_replay(
        ReplayName=replay_name,
        Description=f"Replay for Event bus {event_bus_name}",
        EventSourceArn=event_source_arn,
        EventStartTime=datetime.fromtimestamp(sample_start_epoch),
        EventEndTime=datetime.fromtimestamp(sample_end_epoch),
        Destination={
            "Arn": event_bus_arn,
            "FilterArns": [
                allow_replay_events_only_rule_arn,
            ],
        },
    )

    logger.info(f"Replay event response: {response}")
    start_replay_output = {"replay_name": replay_name}

    return start_replay_output
