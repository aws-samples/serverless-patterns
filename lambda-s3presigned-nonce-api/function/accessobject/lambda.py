import json
import logging
import os
import requests
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table_name = os.environ["NONCE_TABLE"]
nonce_table = dynamodb.Table(table_name)


def getUrl(nonce):
    try:
        response = nonce_table.get_item(Key={"nonce_id": nonce})

    except ClientError as e:
        logger.error(e)
        return False

    if "Item" in response:

        url = response["Item"]["url"]
        count = response["Item"]["count"]
        if count == "0":
            nonce_table.delete_item(Key={"nonce_id": nonce})
        return url
    else:
        # Nonce not found
        return False


def lambda_handler(event, context):

    logger.info("Received event access object : " + json.dumps(event))
    nonce = event["queryStringParameters"]["nonce"]
    url = getUrl(nonce)
    return {"statusCode": "302", "headers": {"Location": url}}
    # Return the content in the Lambda response
