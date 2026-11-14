from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
import json
import boto3
import base64

logger = Logger()
tracer = Tracer()
table = boto3.resource("dynamodb").Table("EventTable")


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    logger.info(f"Received event: {event}")

    # process records from kinesis event
    for record in event["Records"]:
        payload = record["kinesis"]["data"]
        # base64 decode payload
        data = json.loads(base64.b64decode(payload))

        logger.info(f"Received data: {data}")
        table.put_item(Item=data)

    return {"statusCode": 200}
