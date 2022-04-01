# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import boto3
import os
from aws_lambda_powertools import Logger

logger = Logger()
client = boto3.client('stepfunctions')
sfnArn = os.environ['SFN_ARN']

def lambda_handler(event, context):
    # TODO implement
    
    logger.info(f"Received Choice: {event['Choice']}")
    response = client.start_execution(
        stateMachineArn=sfnArn,
        input=json.dumps(event)
    )
    
    logger.info(f"Received Response: {response}")
    
    return {
        'statusCode': 200,
        'body': json.dumps(response,default=str)
    }
