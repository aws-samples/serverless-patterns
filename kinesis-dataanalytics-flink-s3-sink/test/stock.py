
import datetime
import json
import random
import boto3

# Change the stream name per your testing requirements
STREAM_NAME = "demo_stream" 

def get_data():
    return {
    'event_time': datetime.datetime.now().isoformat(),
    'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
    'price': round(random.random() * 100, 2)}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
                StreamName=stream_name,
                Data=json.dumps(data),
                PartitionKey="partitionkey")


#change the AWS Region per your testing needs
if __name__ == '__main__':
        generate(STREAM_NAME, boto3.client('kinesis', region_name='us-east-1'))