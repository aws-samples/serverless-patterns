import json
import os
import time
import random
from decimal import Decimal

import boto3

# Custom JSON encoder to handle Decimal types from DynamoDB
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # Convert Decimal objects to strings for JSON serialization
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

bedrock_runtime = boto3.client("bedrock-runtime")
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    """
    Lambda handler for processing text-to-video generation requests using Amazon Bedrock.
    
    Args:
        event (dict): Contains job_id and prompt for video generation
        context: Lambda context object
    """
    try:
        # Extract required parameters from the event
        job_id = event['job_id']
        prompt = event['prompt']

        print(f"Processing job {job_id} with prompt: {prompt}")

        # Update DynamoDB to indicate processing has started
        table.update_item(
            Key={'job_id': job_id},
            UpdateExpression='SET #status = :status',
            ExpressionAttributeNames={'#status': 'status'},
            ExpressionAttributeValues={':status': 'PROCESSING'}
        )

        model_id = os.environ['MODEL_ID']
        bucket_name = os.environ['BUCKET']
        
        # Configure the video generation parameters
        model_input = {
            "taskType": "TEXT_VIDEO",
            "textToVideoParams": {"text": prompt},
            "videoGenerationConfig": {
                "durationSeconds": 6,
                "fps": 24,
                "dimension": "1280x720",
                "seed": random.randint(0, 2147483648)
            }
        }

        # Initiate asynchronous Bedrock inference
        invocation = bedrock_runtime.start_async_invoke(
            modelId=model_id,
            modelInput=model_input, 
            outputDataConfig={"s3OutputDataConfig": {"s3Uri": f"s3://{bucket_name}"}}
        )

        # Get the invocation ARN for tracking the request
        invocation_arn = invocation["invocationArn"]
        print(f"Started async invocation with ARN: {invocation_arn}")

        # Poll for completion status with 30-second intervals
        status = "InProgress"
        while status == "InProgress":
            response = bedrock_runtime.get_async_invoke(invocationArn=invocation_arn)
            status = response["status"]
            print(f"Current status: {status}")
            if status == "InProgress":
                time.sleep(30)

        if status == "Completed":
            # Extract S3 prefix from invocation ARN for video location
            s3_prefix = invocation_arn.split('/')[-1]
            video_location = f"s3://{bucket_name}/{s3_prefix}/output.mp4"
            print(f"Video generated successfully at: {video_location}")
            
            # Update DynamoDB with success status and video location
            table.update_item(
                Key={'job_id': job_id},
                UpdateExpression='SET #status = :status, video_url = :url',
                ExpressionAttributeNames={'#status': 'status'},
                ExpressionAttributeValues={
                    ':status': 'COMPLETED',
                    ':url': video_location
                }
            )
        else:
            error_message = f'Bedrock processing failed with status: {status}'
            print(f"Error: {error_message}")
            
            # Update DynamoDB with failure status and error message
            table.update_item(
                Key={'job_id': job_id},
                UpdateExpression='SET #status = :status, error = :error',
                ExpressionAttributeNames={'#status': 'status'},
                ExpressionAttributeValues={
                    ':status': 'FAILED',
                    ':error': error_message
                }
            )

    except Exception as e:
        error_message = str(e)
        print(f"Exception occurred: {error_message}")
        
        # Update DynamoDB with error status and message
        table.update_item(
            Key={'job_id': job_id},
            UpdateExpression='SET #status = :status, error = :error',
            ExpressionAttributeNames={'#status': 'status'},
            ExpressionAttributeValues={
                ':status': 'FAILED',
                ':error': error_message
            }
        )
