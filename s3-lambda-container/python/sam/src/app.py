import boto3
import os

s3 = boto3.client('s3')


def lambda_handler(event, context):

    bucket = os.environ['S3_BUCKET']
    key = event['Records'][0]['s3']['object']['key']

    obj = s3.get_object(Bucket=bucket, Key=key)
    lines = obj['Body'].read().decode('utf-8').splitlines()
    
    print("Lines:")
    print(lines)
