from aws_durable_execution_sdk_python.config import Duration
from aws_durable_execution_sdk_python.context import DurableContext, StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution
import random
import datetime
import boto3
import json

@durable_step
def create_order(context: StepContext):
    order_id = f"order-{random.randint(1, 100)}"
    context.logger.info(f"Creating order... : {order_id}")
    return {
        "order_id": order_id,
        "total": 50.00,
        "status": "Created"
    }

@durable_step
def send_notification(context: StepContext, order_id: str):
    context.logger.info(f"Sending notification...")
    return {
        "sent": True,
        "order_id": order_id,
        "recipient": "customer@example.com",
        "timestamp": datetime.datetime.now().isoformat()
    }

@durable_step
def send_sfn_task_success(context: StepContext, task_token: str, response: dict):
    sfn_client = boto3.client("stepfunctions")
    sfn_client.send_task_success(
        taskToken=task_token,
        output=json.dumps(response, default=str),
    )

@durable_execution
def lambda_handler(event: dict, context: DurableContext) -> dict:
    context.logger.info(f"Async Durable Lambda Event: {event}")

    # Extract Step Function Task Token outside durable step
    # Only deterministic operations like event.pop("TaskToken") are safe outside steps.
    task_token = event.pop("TaskToken", None)
    minutes_to_wait = event.pop("minutes_to_wait", 1)

    # Step 1: Create the order
    order_details = context.step(create_order())
    context.logger.info(f"Order created: {order_details['order_id']}")

    # Step 2: Wait X minutes - simulate a long running task
    context.logger.info(f"Waiting {minutes_to_wait} minutes before sending notification...")
    context.wait(Duration.from_minutes(minutes_to_wait))

    # Step 3: Send notification
    context.logger.info(f"Waited for {minutes_to_wait} minutes without consuming CPU.")
    notification_details = context.step(send_notification(order_details['order_id']))
    context.logger.info("Notification sent successfully...")

    response =  {
        "success": True,
        "notification": notification_details
    }

    # IMPORTANT: When using Step Function WAIT_FOR_TASK_TOKEN pattern, 
    # wrap SendTaskSuccess in context.step() to make it durable. 
    # If placed outside context.step(), it will execute on every
    # replay causing duplicate callbacks, or may never execute if 
    # Lambda is interrupted, leaving Step Functions waiting indefinitely. 
    # Send callback as the FINAL durable step
    if task_token:
        context.logger.info("Resuming Step Function by calling send_task_success with task_token")
        context.step(send_sfn_task_success(task_token, response))

    return response
