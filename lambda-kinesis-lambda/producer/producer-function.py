#! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: MIT-0
from concurrent.futures import process
import boto3
import json
from datetime import datetime
import calendar
import random
import time
import os
  
stream_name = os.environ['KINESIS_STREAM']
kinesis_client = boto3.client('kinesis', region_name=os.environ['AWS_REGION'])

def put_to_stream(property_id, property_value, property_timestamp):
    payload = {
                'prop': str(property_value),
                'timestamp': str(property_timestamp),
                'property_id': property_id
              }
    print(payload)
    put_response = kinesis_client.put_record(
                        StreamName=stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=property_id)

def lambda_handler(event, context):
    property_value = random.randint(40, 120)
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    property_id = 'Property11'
    put_to_stream(property_id, property_value, property_timestamp)
    return {"statusCode":200, "body":"Successfully posted"}