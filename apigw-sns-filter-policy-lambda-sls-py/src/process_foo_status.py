import json
from enum import Enum

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.data_classes import event_source, SNSEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


@event_source(data_class=SNSEvent)
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: SNSEvent, context: LambdaContext):
    for record in event.records:
        message = record.sns.message
        message_json = json.loads(message)
        notify(message_json)


def notify(data: dict):
    if data.get('status', None) == 'foo' and data.get('id', None) is not None:
        # do stuff...
        logger.info(f"Processed request with ID: {data.get('id')}")
