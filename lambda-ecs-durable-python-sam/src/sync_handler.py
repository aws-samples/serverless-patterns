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

@durable_step
def start_ecs_task(step_context, cluster, task_definition, subnet1, subnet2, security_group, message, processing_time):
    """
    Durable step that starts an ECS task.
    This step is checkpointed, so if interrupted, it won't re-execute.
    """
    step_context.logger.info(f"[SYNC] Starting ECS task with message: {message}")
    
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
                    'name': 'python-sync-container',
                    'environment': [
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
    step_context.logger.info(f"[SYNC] Task started: {task_arn}")
    
    return task_arn

@durable_step
def check_task_status(step_context, cluster, task_arn):
    """
    Durable step that checks ECS task status.
    This step is checkpointed and can be retried if it fails.
    """
    step_context.logger.info(f"[SYNC] Checking task status: {task_arn}")
    
    describe_response = ecs_client.describe_tasks(
        cluster=cluster,
        tasks=[task_arn]
    )
    
    if not describe_response['tasks']:
        raise Exception(f"Task not found: {task_arn}")
    
    task = describe_response['tasks'][0]
    last_status = task['lastStatus']
    
    step_context.logger.info(f"[SYNC] Task status: {last_status}")
    
    return {
        'status': last_status,
        'task': task
    }

@durable_execution
def lambda_handler(event, context: DurableContext):
    """
    Lambda Durable Function that invokes an ECS task and waits for completion.
    Uses the Durable Execution SDK for automatic checkpointing and replay.
    
    This function can run for up to 1 year, with automatic state management
    and recovery from failures.
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
        # Step 1: Start ECS task (checkpointed)
        task_arn = context.step(start_ecs_task(
            cluster, task_definition, subnet1, subnet2, 
            security_group, message, processing_time
        ))
        
        # Poll for task completion using durable waits
        max_attempts = 60  # 5 minutes max (60 * 5 seconds)
        poll_interval = 5  # Check every 5 seconds
        
        for attempt in range(max_attempts):
            # Wait before checking status (no compute charges during wait)
            context.wait(Duration.from_seconds(poll_interval))
            
            # Step 2: Check task status (checkpointed)
            status_result = context.step(check_task_status(cluster, task_arn))
            
            if status_result['status'] == 'STOPPED':
                # Task completed
                task = status_result['task']
                stop_code = task.get('stopCode', 'Unknown')
                
                if stop_code == 'EssentialContainerExited':
                    exit_code = task['containers'][0].get('exitCode', 1)
                    
                    if exit_code == 0:
                        context.logger.info(f"[SYNC] Task completed successfully")
                        return {
                            'statusCode': 200,
                            'body': json.dumps({
                                'status': 'success',
                                'message': f'Processed: {message}',
                                'processingTime': processing_time,
                                'taskArn': task_arn
                            })
                        }
                    else:
                        raise Exception(f"Task failed with exit code: {exit_code}")
                else:
                    raise Exception(f"Task stopped unexpectedly: {stop_code}")
        
        # Timeout
        raise Exception(f"Task did not complete within {max_attempts * poll_interval} seconds")
        
    except Exception as e:
        context.logger.error(f"[SYNC] Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'status': 'error',
                'error': str(e)
            })
        }
