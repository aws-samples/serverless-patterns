# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

endpoint = os.environ.get('ApiGatewayEndpoint')
logging.info(f"Loaded endpoint uri from environemt variable: {endpoint}")
api_client = boto3.client('apigatewaymanagementapi',endpoint_url=endpoint)

def lambda_handler(event, context):
    
    if event['Records']:

        json_dump = json.dumps(event['Records'])
        logging.info(f"json: {json_dump}")
        message = "Received record data!"
        
        for record in event['Records']:
            connection_id = record["messageAttributes"]["connectionId"]["stringValue"]
            response = {
                "connectionId":connection_id,
                "requestId":record["messageAttributes"]["requestId"]["stringValue"],
                "message":record["body"]
            }
            logging.info(f"response: {response}")
            data = json.dumps(response)
            api_client.post_to_connection(ConnectionId=connection_id, Data=data.encode('utf-8'))
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"message": message})
        }
    else:
        message = "Something went wrong"
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"message": message})
        }