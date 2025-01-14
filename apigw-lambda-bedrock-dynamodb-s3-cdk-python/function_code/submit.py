import json
import os
import uuid
import time
from decimal import Decimal

import boto3

class DecimalEncoder(json.JSONEncoder):
    """
    Custom JSON encoder to handle Decimal types from DynamoDB.
    Converts Decimal objects to strings for proper JSON serialization.
    """
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

def convert_dynamodb_item(item):
    """
    Helper function to convert DynamoDB items to Python native types.
    
    Args:
        item (dict): DynamoDB item with potential Decimal values
        
    Returns:
        dict: Converted item with Decimal values transformed to int or float
        None: If input item is None
    """
    if not item:
        return None
    
    converted = {}
    for key, value in item.items():
        if isinstance(value, Decimal):
            converted[key] = int(value) if value % 1 == 0 else float(value)
        else:
            converted[key] = value
    return converted

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])
lambda_client = boto3.client('lambda')

def handler(event, context):
    """
    Lambda handler for processing job submissions and status checks.
    Handles both GET requests (status checks) and POST requests (job submissions).
    
    Args:
        event (dict): API Gateway event containing request details
        context: Lambda context object
    
    Returns:
        dict: API Gateway response object with appropriate status code and body
    """
    try:
        # Handle GET request for job status check
        if event['httpMethod'] == 'GET':
            # Extract job ID from path parameters
            job_id = event['pathParameters']['jobId']
            response = table.get_item(Key={'job_id': job_id})
            
            # Return 404 if job not found
            if 'Item' not in response:
                return {
                    'statusCode': 404,
                    'headers': {
                        'Access-Control-Allow-Origin': '*',
                        'Content-Type': 'application/json'
                    },
                    'body': json.dumps({'error': 'Job not found'})
                }
            
            # Convert and return job details
            converted_item = convert_dynamodb_item(response['Item'])
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps(converted_item)
            }

        # Handle POST request for new job submission
        body = json.loads(event.get('body', '{}'))
        prompt = body.get('prompt')
        
        # Validate prompt existence
        if not prompt:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': 'Prompt is required'})
            }

        # Generate unique job ID and timestamp
        job_id = str(uuid.uuid4())
        timestamp = int(time.time())
        
        # Prepare item for DynamoDB
        item = {
            'job_id': job_id,
            'status': 'SUBMITTED',
            'prompt': prompt,
            'created_at': timestamp,
            'ttl': timestamp + (7 * 24 * 60 * 60)  # Set TTL to 7 days from creation
        }
        
        # Save job details to DynamoDB
        table.put_item(Item=item)

        # Trigger asynchronous processing Lambda
        lambda_client.invoke(
            FunctionName=os.environ['PROCESS_FUNCTION_NAME'],
            InvocationType='Event',
            Payload=json.dumps({
                'job_id': job_id,
                'prompt': prompt
            })
        )

        # Return success response
        return {
            'statusCode': 202,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'job_id': job_id,
                'status': 'SUBMITTED',
                'message': 'Job submitted successfully'
            })
        }

    except Exception as e:
        # Log and return any unexpected errors
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }
