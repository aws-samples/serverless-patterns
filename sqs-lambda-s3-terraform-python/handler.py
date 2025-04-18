import boto3
from botocore.config import Config
import os
import json

import boto3.s3

def lambda_handler(event, context):
    print(event['Records'][0]['body'])
    print(context)
    file_name = 'request_' + json.loads(event['Records'][0]['body'])["uniqueID"] + '.json'
    request_body = event['Records'][0]['body']
    aws_region = os.getenv('AWS_REGION')
    s3_bucket_ident = os.getenv('S3_BUCKET_NAME')
    config = Config(region_name=aws_region)
    s3_client = boto3.client('s3',config=config)
    resp = s3_client.put_object(
        Body=str(request_body).encode(encoding="utf-8"),
        Bucket=s3_bucket_ident,
        Key=file_name
    )
    
    print(resp)
