import base64
import json

def lambda_handler(event, context):
    for record in event['Records']:
        # Kinesis data is base64 encoded so need to decode
        data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("Kinesis Data: " + data)
