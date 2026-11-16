import logging
import json
import boto3
import ast

dynamo_client = boto3.client('dynamodb')

def handler(event, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))

    for record in event['Records']:
        payload = record["body"]
        logger.info("received message " + payload)

        try:
            dynamo_client.batch_write_item(RequestItems=ast.literal_eval(payload))
        except Exception as e:
            logger.error(e)

 