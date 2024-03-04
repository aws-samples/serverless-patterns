import datetime
import json
import random
import boto3
import os
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location/'../cdk.json'

with open(file_location, "r") as f:
    cdk_config = json.load(f)

STREAM_NAME = cdk_config["context"]["InputStream"]

def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'product': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'price': round(random.random() * 100, 2)
    }

def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")


if __name__ == '__main__':
    session = boto3.session.Session()
    region = session.region_name
    generate(STREAM_NAME, boto3.client('kinesis', region_name=region))
