
import datetime
import json
import random
import boto3

# Change the stream name per your testing requirements
STREAM_NAME = "kinesis_stream_lambda_esm" 

def get_data():
    return {
    'event_time': datetime.datetime.now().isoformat(),
    'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
    'price': round(random.random() * 100, 2)}

def generate(stream_name, kinesis_client):
    counter = 1
    max     = 5

    while counter < max+1:
        data = get_data()
        print(data)
        kinesis_client.put_record(
                StreamName=stream_name,
                Data=json.dumps(data),
                PartitionKey="partitionkey")
        counter += 1

#change the AWS Region per your testing needs
if __name__ == '__main__':
        generate(STREAM_NAME, boto3.client('kinesis', region_name='us-east-1'))