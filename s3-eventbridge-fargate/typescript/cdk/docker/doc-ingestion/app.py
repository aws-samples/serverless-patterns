import os
import boto3

s3_bucket = os.environ['S3_BUCKET']
s3_object = os.environ['S3_OBJECT_KEY']

s3_client = boto3.client('s3')
try:
    s3_response = s3_client.get_object(Bucket=s3_bucket, Key=s3_object)
    data = s3_response['Body'].read().decode('utf-8').splitlines(True)
    print(data)

    # implement business logic to process file

except Exception as e:
    print(f"Error: {e}")
    raise e

