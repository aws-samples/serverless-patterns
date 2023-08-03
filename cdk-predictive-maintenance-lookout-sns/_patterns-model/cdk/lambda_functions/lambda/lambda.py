import boto3
import os

def lambda_handler(event, context):
    s3_client = boto3.client('s3')

    bucket = os.environ['OUTPUT_BUCKET']
    bucket_name = event[bucket]
    prefix = event['output_data/']
    object_name = event['text']
    file_content = ''  

    # Combine the prefix and the object name to create a "path" for the object
    key = os.path.join(prefix, object_name)

    # Put the object in the bucket
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=file_content)
