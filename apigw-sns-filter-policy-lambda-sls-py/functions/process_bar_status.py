import json

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
        logger.info(f"Notification received for Bar message: {message_json}")
