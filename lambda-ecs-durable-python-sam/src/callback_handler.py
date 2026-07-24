import json
import boto3
import os
import hashlib
from aws_durable_execution_sdk_python import (
    DurableContext,
    durable_execution,
)

ecs_client = boto3.client('ecs')

def start_ecs_task_with_callback(cluster, task_definition, subnet1, subnet2, security_group, 
                                  callback_token, message, processing_time):
    """
    Starts an ECS task and passes the callback token via environment variable.
    The ECS task will call Lambda durable execution callback APIs when complete.
    Uses callback_token as idempotency token to prevent duplicate tasks on retry.
    """
    print(f"[CALLBACK] Starting ECS task with callback token")
    
    # Use callback token hash as clientToken for idempotency (max 64 chars)
    client_token = hashlib.sha256(callback_token.encode()).hexdigest()[:64]
    
    response = ecs_client.run_task(
        cluster=cluster,
        taskDefinition=task_definition,
        launchType='FARGATE',
        clientToken=client_token,
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [subnet1, subnet2],
                'securityGroups': [security_group],
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': 'python-callback-container',
                    'environment': [
                        {'name': 'CALLBACK_TOKEN', 'value': callback_token},
                        {'name': 'MESSAGE', 'value': message},
                        {'name': 'PROCESSING_TIME', 'value': str(processing_time)}
                    ]
                }
            ]
        }
    )
    
    if not response['tasks']:
        raise Exception("Failed to start ECS task")
    
    task_arn = response['tasks'][0]['taskArn']
    print(f"[CALLBACK] Task started: {task_arn}")
    
    return task_arn

@durable_execution
def lambda_handler(event, context: DurableContext):
    """
    Lambda durable function that invokes an ECS task and waits for callback.
    
    The ECS task receives a callback token and calls Lambda durable execution
    callback APIs (SendDurableExecutionCallbackSuccess/Failure) when complete.
    
    This function pauses execution while waiting for the callback, with no
    compute charges during the wait period.
    """
    
    # Get configuration from environment variables
    cluster = os.environ['ECS_CLUSTER']
    task_definition = os.environ['TASK_DEFINITION']
    subnet1 = os.environ['SUBNET_1']
    subnet2 = os.environ['SUBNET_2']
    security_group = os.environ['SECURITY_GROUP']
    
    # Get input parameters
    message = event.get('message', 'No message provided')
    processing_time = event.get('processingTime', 5)
    
    try:
        # Create callback to get callback token
        callback = context.create_callback()
        
        print(f"[CALLBACK] Created callback with token: {callback.callback_id[:20]}...")
        
        # Start ECS task with callback token (call directly, no context.step!)
        task_arn = start_ecs_task_with_callback(
            cluster, task_definition, subnet1, subnet2, security_group,
            callback.callback_id, message, processing_time
        )
        
        print(f"[CALLBACK] Waiting for callback from ECS task...")
        
        # Wait for callback (pauses execution here, no compute charges)
        result = callback.result()
        
        print(f"[CALLBACK] Received callback with result")
        
        # Return the result from the callback
        return {
            'statusCode': 200,
            'body': json.dumps({
                'status': 'success',
                'message': 'ECS task completed and sent callback',
                'taskArn': task_arn,
                'result': result
            })
        }
        
    except Exception as e:
        context.logger.error(f"[CALLBACK] Error: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'status': 'error',
                'error': str(e)
            })
        }
