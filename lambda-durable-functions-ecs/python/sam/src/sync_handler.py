import json
import boto3
import os
import hashlib
from aws_durable_execution_sdk_python import (
    DurableContext,
    durable_execution,
    durable_step,
)
from aws_durable_execution_sdk_python.config import Duration
from aws_durable_execution_sdk_python.waits import WaitForConditionConfig, WaitForConditionDecision

ecs_client = boto3.client('ecs')


@durable_step
def start_ecs_task(step_context, cluster, task_definition, subnet1, subnet2, security_group, message, processing_time):
    """
    Durable step that starts an ECS task.
    Uses a deterministic clientToken for idempotency in case of retry
    before checkpoint is saved.
    """
    step_context.logger.info(f"[SYNC] Starting ECS task with message: {message}")
    
    # Generate deterministic idempotency token from inputs
    token_input = f"{cluster}:{task_definition}:{message}:{processing_time}"
    client_token = hashlib.sha256(token_input.encode()).hexdigest()[:64]
    
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


def check_ecs_status(cluster, task_arn):
    """Check ECS task status (called by wait_for_condition)."""
    describe_response = ecs_client.describe_tasks(
        cluster=cluster,
        tasks=[task_arn]
    )
    
    if not describe_response['tasks']:
        return {'status': 'UNKNOWN', 'cluster': cluster, 'task_arn': task_arn}
    
    task = describe_response['tasks'][0]
    return {
        'status': task['lastStatus'],
        'task': task,
        'cluster': cluster,
        'task_arn': task_arn
    }


@durable_execution
def lambda_handler(event, context: DurableContext):
    """
    Lambda durable function that invokes an ECS task and waits for completion.
    Uses wait_for_condition for polling and durable steps for checkpointing.
    """
    
    cluster = os.environ['ECS_CLUSTER']
    task_definition = os.environ['TASK_DEFINITION']
    subnet1 = os.environ['SUBNET_1']
    subnet2 = os.environ['SUBNET_2']
    security_group = os.environ['SECURITY_GROUP']
    
    message = event.get('message', 'No message provided')
    processing_time = event.get('processingTime', 5)
    
    try:
        # Step 1: Start ECS task (checkpointed, with idempotency token)
        task_arn = context.step(start_ecs_task(
            cluster, task_definition, subnet1, subnet2, 
            security_group, message, processing_time
        ))
        
        # Step 2: Poll for task completion using wait_for_condition
        result = context.wait_for_condition(
            lambda state, ctx: check_ecs_status(state['cluster'], state['task_arn']),
            config=WaitForConditionConfig(
                initial_state={'cluster': cluster, 'task_arn': task_arn, 'status': 'PENDING'},
                wait_strategy=lambda state, attempt:
                    WaitForConditionDecision(should_continue=False, delay=Duration.from_seconds(0)) if state.get('status') == 'STOPPED'
                    else WaitForConditionDecision(should_continue=True, delay=Duration.from_seconds(5))
            )
        )
        
        task = result.get('task', {})
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
        
    except Exception as e:
        context.logger.error(f"[SYNC] Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'status': 'error',
                'error': str(e)
            })
        }
