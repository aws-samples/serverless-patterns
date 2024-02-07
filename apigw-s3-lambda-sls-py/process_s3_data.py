import json
import boto3
from urllib.parse import unquote_plus

from aws_lambda_powertools.utilities.typing import LambdaContext
from retry import retry
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.data_classes import event_source, S3Event

s3 = boto3.client('s3')
logger = Logger()


@event_source(data_class=S3Event)
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: S3Event, context: LambdaContext):
    # Extracting information from the S3 event
    bucket_name = event.bucket_name
    for record in event.records:
        object_key = unquote_plus(record.s3.get_object.key)
        result = s3.get_object(Bucket=bucket_name, Key=object_key)
        json_data = json.loads(result["Body"].read().decode())
        logger.info(process(json_data))


@retry(tries=3, delay=2)
def process(incoming_data):
    # Processing the JSON order data from S3
    try:
        # do stuff ...
        processing_succeeded = True
    except Exception as e:
        logger.exception(repr(e))
        processing_succeeded = False

    incoming_data['processed'] = processing_succeeded
    return incoming_data
