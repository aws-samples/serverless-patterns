import json
import boto3
import os
import base64

from botocore.exceptions import ClientError

ssm = boto3.client("ssm")
    
param_name = os.environ.get('PARAMETER_NAME')

def get(event, context):
    try:
        parameter = ssm.get_parameter(Name=param_name)['Parameter']['Value']
        return {
            "statusCode": 200,
            "body": json.dumps(parameter)
        }
    except ClientError as e:
        print(e)
        return None
def put(event, context):
    val = event['body']
    b64 = event['isBase64Encoded']
    try:
        if (b64 == True):
            decoded_val = base64.b64decode(val).decode('utf-8')
            ssm.put_parameter(Name=param_name, Value=decoded_val, Type='String', Overwrite=True)
        else:
            ssm.put_parameter(Name=param_name, Value=val, Type='String', Overwrite=True)
        return {
            "statusCode": 200,
            "body": "success"
        }
    except ClientError as e:
        print(e)
        return None    

