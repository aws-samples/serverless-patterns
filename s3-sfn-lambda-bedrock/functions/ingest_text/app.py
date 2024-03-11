import base64
import boto3
import chardet
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract the S3 bucket and key from the Step Functions event
    bucket = event['detail']['bucket']['name']
    source_key = event['detail']['object']['key']

    # Download the file from S3
    response = s3.get_object(Bucket=bucket, Key=source_key)
    content = response['Body'].read()

    # Detect the file encoding
    detected_encoding = chardet.detect(content)['encoding']

    # Decode the content using the detected encoding
    decoded_content = content.decode(detected_encoding or 'utf-8')

    # Encode the content as UTF-8
    encoded_content = decoded_content.encode('utf-8')

    # Remove the 'raw/' prefix from the object key
    object_name = os.path.basename(source_key)

    next_key = os.path.join(os.environ['NextPrefix'], object_name + "_text.txt")
    s3.put_object(Bucket=bucket, Key=next_key, Body=encoded_content)

    return {
        'statusCode': 200,
        'body': f'File {source_key} processed and written to {next_key}',
        'next_key': next_key,
        'bucket': bucket
    }