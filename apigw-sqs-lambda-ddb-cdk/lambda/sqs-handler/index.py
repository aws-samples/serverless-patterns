from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
import json
import boto3
import os

logger = Logger()
tracer = Tracer()

tableName = os.environ['dynamo_db_name']
table = boto3.resource("dynamodb").Table(tableName)


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    # Getting environment variable
    

    # process records from sqs event
    for record in event["Records"]:
        payload = json.loads(record["body"])
        table.put_item(Item=payload)

    return {"statusCode": 200}
