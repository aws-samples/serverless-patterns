# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import json
import logging
import base64
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)
        
def lambda_handler(event, context):
    
    logging.info(json.dumps(event, indent=2))
    logging.info(f"Lambda function ARN: {context.invoked_function_arn}")
    logging.info(f"CloudWatch log stream name: {context.log_stream_name}")
    logging.info(f"CloudWatch log group name:  {context.log_group_name}")
    logging.info(f"Lambda Request ID: {context.aws_request_id}")
    logging.info(f"Lambda function memory limits in MB: {context.memory_limit_in_mb}")

    eventObject = {
    "functionName":context.function_name,
    "xForwardedFor":event["headers"]["X-Forwarded-For"],
    "method":event["requestContext"]["httpMethod"],
    "rawPath":event["requestContext"]["path"],
    "queryString":event["queryStringParameters"],
    "timestamp":event["requestContext"]["requestTime"]
    }
    
    if event["requestContext"]["httpMethod"] == "POST":

        eventObject["body"] = event["body"]
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message ": eventObject
            })
        }
    else:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message ": eventObject
            })
        }