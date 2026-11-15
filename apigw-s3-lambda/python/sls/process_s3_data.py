import json
from urllib.parse import unquote_plus

import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.data_classes import event_source, S3Event
from aws_lambda_powertools.utilities.typing import LambdaContext

s3 = boto3.client('s3')
logger = Logger()


@event_source(data_class=S3Event)
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: S3Event, context: LambdaContext):
    bucket_name = event.bucket_name
    for record in event.records:
        object_key = unquote_plus(record.s3.get_object.key)
        result = s3.get_object(Bucket=bucket_name, Key=object_key)
        json_data = json.loads(result["Body"].read().decode())
        logger.info(f"Process the incoming data: {json_data}")

