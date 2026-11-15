import boto3
import os
import json
import logging
import botocore
from datetime import datetime
logger = logging.getLogger()
logger.setLevel(logging.INFO)


client_lambda = boto3.client('lambda')
client_s3 = boto3.client('s3')

ASYNC_LAMBDA_FUNCTIONNAME=os.environ.get('AsyncLambdaFunctionName')
PAYLOAD_PREFIX = os.environ.get('PayloadPrefix')
BUCKET_NAME = os.environ.get('PayloadBucketName')

def call_asynchronous_function(payload):
    response = None
    try:
        response = client_lambda.invoke(FunctionName=ASYNC_LAMBDA_FUNCTIONNAME, InvocationType="Event", Payload=json.dumps(payload))
    except botocore.exceptions.ClientError as e:
        # Save payload to s3 and s3 trigger async lambda when payload size exceeded 250kb
        if e.response['Error']['Code'] == 'RequestEntityTooLargeException':
            filename = f"{PAYLOAD_PREFIX}{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
            response = client_s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=json.dumps(payload))
        else:
            logger.error(e)
            raise

    return response

def lambda_handler(event, context):
    # Call asynchronous lambda function. Upload payload to S3 when payload size is too large.
    logger.info(len(event))
    response = call_asynchronous_function(event);

    logger.info(response)
    response.pop('Payload', None)

    return {
        "statusCode": 200,
        "body": json.dumps(
            response
        ),
    }

