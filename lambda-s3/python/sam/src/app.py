import boto3
import os

bucket = os.environ.get('DestinationBucketName')

def lambda_handler(event, context):

    # Upload the file
    data = b'Hello World'
    client = boto3.client('s3')
    response = client.put_object(Body=data, Bucket=bucket, Key='filename.txt')
    return True