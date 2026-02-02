import boto3
import logging
import os
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TABLE_NAME = os.environ["WEBSOCKETS_DDB_TABLE"]

# global variables - avoid creating a new client for every request
table = None

def lambda_handler(event, context):
    global table

    connection_id = event.get("requestContext", {}).get("connectionId")
    if TABLE_NAME is None or connection_id is None:
        return {"statusCode": 400}

    if table is None:
        table = boto3.resource("dynamodb").Table(TABLE_NAME)
    logger.info("Use table %s.", table.name)

    status_code = 200
    try:
        table.delete_item(Key={"connectionId": connection_id})
        logger.info("Disconnected connection %s.", connection_id)
    except ClientError:
        logger.exception("Couldn't disconnect connection %s.", connection_id)
        status_code = 503

    return { 'statusCode': status_code, 'body': 'Disconnected.' }