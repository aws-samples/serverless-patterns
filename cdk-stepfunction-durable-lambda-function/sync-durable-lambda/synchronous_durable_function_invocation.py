from aws_durable_execution_sdk_python.config import Duration
from aws_durable_execution_sdk_python.context import DurableContext, StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution
import random
import datetime

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

@durable_execution
def lambda_handler(event: dict, context: DurableContext) -> dict:

    context.logger.info(f"Lambda Event: {event}")
    # Step 1: Create the order
    order_details = context.step(create_order())
    context.logger.info(f"Order created: {order_details['order_id']}")

    # Step 2: Wait 10 seconds - simulate a short running process
    context.logger.info("Waiting 10 seconds before sending notification...")
    context.wait(Duration.from_seconds(10))

    # Step 3: Send notification
    context.logger.info("Waited for 10 seconds without consuming CPU.")
    notification_details = context.step(send_notification(order_details['order_id']))
    context.logger.info("Notification sent successfully...")

    return {
        "success": True,
        "notification": notification_details
    }
