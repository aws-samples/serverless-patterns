import json
import random
import time
import boto3
import os

bedrock_runtime = boto3.client("bedrock-runtime")
def get_url(s3_location):
    s3_client = boto3.client('s3')
    s3_bucket = s3_location.split('/')[2]
    s3_key = '/'.join(s3_location.split('/')[3:])
    print("Generating PreSigned URL for S3 Bucket Key:", s3_bucket, "  ", s3_key)
    # generate the Pre-Signed URL that is valid for ExpiresIn time
    s3_presigned_url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': s3_bucket, 'Key': s3_key},
        ExpiresIn=3600
    )
    return s3_presigned_url

def handler(event, context):
    # read Invocation ARN and S3 Location from Step Functions event
    invocation_arn = event["InvocationARN"]
    s3_location = event["S3Location"]
    #fetch status of video generation
    response = bedrock_runtime.get_async_invoke(
        invocationArn=invocation_arn
    )
    status = response["status"]
    print(f"Status: {status}")
 
    if status == "Completed":
        print(f"\nVideo is ready at {s3_location}/output.mp4")
        return {
            'Status': "Completed",
            'PreSignedURL': json.dumps(get_url(s3_location+'/output.mp4'))
        }
    elif status == "InProgress":
        print(f"\nVideo generation status: {status}")
        return {
            'Status': "InProgress",
            'PreSignedURL': "Still Generating",
            'InvocationARN': invocation_arn,
            'S3Location': s3_location
        }
    else:
        print(f"\nVideo generation status: {status}")
        return {
            'Status': {status},
            'PreSignedURL': "Something went wrong"
        }