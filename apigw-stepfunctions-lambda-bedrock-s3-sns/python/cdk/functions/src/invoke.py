import json
import random
import time
import boto3
import os

bedrock_runtime = boto3.client("bedrock-runtime")
def handler(event, context):

    Model_Id = "amazon.nova-reel-v1:0"
    S3_Destination_Bucket = os.environ['BUCKET_NAME']
    print(event)
    video_prompt = event['prompt']

    model_input = {
        "taskType": "TEXT_VIDEO",
        "textToVideoParams": {"text": video_prompt},
        "videoGenerationConfig": {
            "durationSeconds": 6,
            "fps": 24,
            "dimension": "1280x720",
            "seed": random.randint(0, 2147483648)
        }
    }
    # start video generation using asynchronous API call
    invocation = bedrock_runtime.start_async_invoke(
        modelId=Model_Id,
        modelInput=model_input,
        outputDataConfig={"s3OutputDataConfig": {"s3Uri": f"s3://{S3_Destination_Bucket}"}}
    )
    
    invocation_arn = invocation["invocationArn"]
    s3_prefix = invocation_arn.split('/')[-1]
    s3_location = f"s3://{S3_Destination_Bucket}/{s3_prefix}"
    print(f"\nS3 URI: {s3_location}")
    # return Invocation ARN and S3 Location to State Machine
    return {
        "InvocationARN": invocation_arn,
        "S3Location": s3_location
    }