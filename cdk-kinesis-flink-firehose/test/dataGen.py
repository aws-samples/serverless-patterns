# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

import datetime
import json
import random
import boto3
import time

STREAM_NAME = "CdkStack-KinesisSourceF9B97A74-RdTeyeKl6gIV"
REGION = "us-west-2"

def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'price': round(random.random() * 100, 2)}

def generate(stream_name, kinesis_client):
    t_end = time.time() + 10
    while time.time() < t_end:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")

generate(STREAM_NAME, boto3.client('kinesis', region_name=REGION))