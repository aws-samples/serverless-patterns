# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 
# SPDX-License-Identifier: MIT-0

import os
import json
import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.Session()
region = session.region_name
iotdata_client = boto3.client('iot-data')


def handler(event, context):
    logger.info(event)
    body = event['body']
    data = json.loads(body)
    logger.info(data)

    if (not 'topic' in data) or (not 'payload' in data):
        return {
            "statusCode": 500,
        }
    
    message = data['payload']

    response = iotdata_client.publish(
        topic=data['topic'],
        qos=0,
        payload=json.dumps(message)
    )

    logger.info(response)

    return {
        "statusCode": 200,
        "body": json.dumps(
                response
        ),
    }