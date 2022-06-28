import json
import boto3
import os
import base64

from botocore.exceptions import ClientError

bridge = boto3.client("events")
    
source_name = os.environ.get('SOURCE_NAME')
detail_type = os.environ.get('DETAIL_TYPE')
def post(event, context):
    val = event['body']
    b64 = event['isBase64Encoded']
    try:
        response = ''
        if (b64 == True):
            decoded_val = base64.b64decode(val).decode('utf-8')
            response = bridge.put_events(Entries=[
                { 'Source': source_name,
                  'DetailType': detail_type,
                  'Detail': decoded_val
                  },])
        else:
            response = bridge.put_events(Entries=[
                { 'Source': source_name,
                  'DetailType': detail_type,
                  'Detail': val
                  },])
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    except ClientError as e:
        print(e)
        return None    

