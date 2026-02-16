import json
import boto3
import os
from aws_durable_execution_sdk_python import (
    DurableContext,
    durable_execution,
    durable_step,
)
from aws_durable_execution_sdk_python.config import Duration

ecs_client = boto3.client('ecs')
dynamodb = boto3.resource('dynamodb')

@durable_step
def create_execution_record(step_context, callback_table, execution_id, message, processing_time):
    """
    Durable step that creates initial execution record in DynamoDB.
    """
    step_context.logger.info(f"[CALLBACK] Creating execution record: {execution_id}")
    
    table = dynamodb.Table(callback_table)
    table.put_item(
        Item={
            'executionId': execution_id,
            'status': 'RUNNING',
            'message': message,
            'processingTime': processing_time
        }
    )
    
    return execution_id

@durable_step
def start_ecs_task_async(step_context, cluster, task_definition, subnet1, subnet2, security_group, 
                         message, processing_time, execution_id, callback_table):
    """
    Durable step that starts an ECS task for async processing.
    """
    step_context.logger.info(f"[CALLBACK] Starting ECS task with execution ID: {execution_id}")
    
    response = ecs_client.run_task(
        cluster=cluster,
        taskDefinition=task_definition,
        launchType='FARGATE',
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
                        {'name': 'MESSAGE', 'value': message},
                        {'name': 'PROCESSING_TIME', 'value': str(processing_time)},
                        {'name': 'EXECUTION_ID', 'value': execution_id},
                        {'name': 'CALLBACK_TABLE', 'value': callback_table}
                    ]
                }
            ]
        }
    )
    
    if not response['tasks']:
        raise Exception("Failed to start ECS task")
    
    task_arn = response['tasks'][0]['taskArn']
    step_context.logger.info(f"[CALLBACK] Task started: {task_arn}")
    
    return task_arn

@durable_step
def update_task_arn(step_context, callback_table, execution_id, task_arn):
    """
    Durable step that updates DynamoDB with task ARN.
    """
    step_context.logger.info(f"[CALLBACK] Updating task ARN in DynamoDB")
    
    table = dynamodb.Table(callback_table)
    table.update_item(
        Key={'executionId': execution_id},
        UpdateExpression='SET taskArn = :arn',
        ExpressionAttributeValues={':arn': task_arn}
    )
    
    return True

@durable_execution
def lambda_handler(event, context: DurableContext):
    """
    Lambda Durable Function that invokes an ECS task asynchronously.
    The ECS task will update DynamoDB when complete.
    
    This function uses durable execution to ensure reliable task initiation
    with automatic checkpointing and recovery.
    """
    
    # Get configuration from environment variables
    cluster = os.environ['ECS_CLUSTER']
    task_definition = os.environ['TASK_DEFINITION']
    subnet1 = os.environ['SUBNET_1']
    subnet2 = os.environ['SUBNET_2']
    security_group = os.environ['SECURITY_GROUP']
    callback_table = os.environ['CALLBACK_TABLE']
    
    # Get input parameters
    message = event.get('message', 'No message provided')
    processing_time = event.get('processingTime', 5)
    
    # Generate unique execution ID from durable execution ARN
    import uuid
    execution_id = event.get('executionId', str(uuid.uuid4()))
    
    try:
        # Step 1: Create execution record (checkpointed)
        context.step(create_execution_record(
            callback_table, execution_id, message, processing_time
        ))
        
        # Step 2: Start ECS task (checkpointed)
        task_arn = context.step(start_ecs_task_async(
            cluster, task_definition, subnet1, subnet2, security_group,
            message, processing_time, execution_id, callback_table
        ))
        
        # Step 3: Update DynamoDB with task ARN (checkpointed)
        context.step(update_task_arn(callback_table, execution_id, task_arn))
        
        # Return immediately (async pattern)
        return {
            'statusCode': 202,  # Accepted
            'body': json.dumps({
                'status': 'accepted',
                'message': 'ECS task started, will callback when complete',
                'executionId': execution_id,
                'taskArn': task_arn
            })
        }
        
    except Exception as e:
        context.logger.error(f"[CALLBACK] Error: {str(e)}")
        
        # Update DynamoDB with error
        try:
            table = dynamodb.Table(callback_table)
            table.update_item(
                Key={'executionId': execution_id},
                UpdateExpression='SET #status = :status, #error = :error',
                ExpressionAttributeNames={
                    '#status': 'status',
                    '#error': 'error'
                },
                ExpressionAttributeValues={
                    ':status': 'FAILED',
                    ':error': str(e)
                }
            )
        except:
            pass
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'status': 'error',
                'error': str(e),
                'executionId': execution_id
            })
        }
