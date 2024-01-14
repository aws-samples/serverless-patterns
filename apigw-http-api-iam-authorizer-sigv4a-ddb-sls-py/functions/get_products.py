import json
import logging
import os

import boto3

logger = logging.getLogger(__name__)

products_table = os.getenv('products_table', None)
default_results = os.getenv('default_results', None)

client = boto3.resource('dynamodb')
table = client.Table(products_table)


def _get_products():
    scan_result = table.scan(Limit=int(default_results))
    return scan_result['Items']


def handler(event, context):
    logger.info(f"Fetching {default_results} records from table {products_table}")
    response = {
        "statusCode": 200,
        "body": json.dumps(_get_products()),
        "headers": {
            "Content-Type": 'application/json'
        }
    }
    return response
