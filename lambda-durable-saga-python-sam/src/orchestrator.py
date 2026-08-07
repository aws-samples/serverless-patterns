"""
Saga orchestrator using Lambda durable functions (Python).

Processes an order through 3 steps:
  1. Reserve inventory
  2. Process payment
  3. Confirm order

If any step fails, compensating transactions execute in REVERSE order
to undo all previously completed steps, ensuring data consistency.
"""

import os
import uuid
import logging
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation

import json
import boto3
from aws_durable_execution_sdk_python.context import DurableContext, StepContext, durable_step
from aws_durable_execution_sdk_python.config import StepConfig
from aws_durable_execution_sdk_python.execution import durable_execution
from aws_durable_execution_sdk_python.retries import RetryPresets, RetryStrategyConfig, create_retry_strategy

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
dynamodb_client = boto3.client("dynamodb")
sqs_client = boto3.client("sqs")
orders_table = dynamodb.Table(os.environ["ORDERS_TABLE"])
payments_table = dynamodb.Table(os.environ["PAYMENTS_TABLE"])
inventory_table = dynamodb.Table(os.environ["INVENTORY_TABLE"])


# ─── Custom Exceptions ───────────────────────────────────────────────────────


class InsufficientInventoryError(Exception):
    """Raised when requested quantity exceeds available stock."""
    pass


class PaymentDeclinedError(Exception):
    """Raised when payment processing is declined."""
    pass


# Step config that disables retries for deterministic business-logic failures
_NO_RETRY_STEP_CONFIG = StepConfig(retry_strategy=RetryPresets.none())


# ─── INPUT VALIDATION ────────────────────────────────────────────────────────


def _validate_event(event: dict) -> None:
    """Validate event at the trust boundary before any processing."""
    required = ("customer_id", "items", "total_amount")
    for key in required:
        if key not in event:
            raise ValueError(f"Missing required field: {key}")

    items = event["items"]
    if not isinstance(items, list) or len(items) == 0:
        raise ValueError("items must be a non-empty list")
    if len(items) > 100:
        raise ValueError("items list exceeds maximum of 100 entries")

    for i, item in enumerate(items):
        if "item_id" not in item or "quantity" not in item:
            raise ValueError(f"items[{i}] must have item_id and quantity")
        qty = item["quantity"]
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError(f"items[{i}].quantity must be a positive integer, got {qty!r}")

    try:
        amount = Decimal(str(event["total_amount"]))
    except InvalidOperation:
        raise ValueError(f"total_amount is not a valid decimal: {event['total_amount']!r}")
    if amount.is_nan() or amount.is_infinite():
        raise ValueError("total_amount must be a finite number")
    if amount <= 0:
        raise ValueError("total_amount must be positive")


# ─── FORWARD STEPS ───────────────────────────────────────────────────────────


@durable_step
def generate_order_id(step_context: StepContext) -> str:
    """Generate a stable order ID — inside a step so it's checkpointed across replays."""
    return str(uuid.uuid4())


@durable_step
def reserve_inventory(step_context: StepContext, order_id: str, items: list) -> dict:
    """Step 1: Reserve inventory for each item in the order."""
    step_context.logger.info("Reserving inventory for order %s", order_id)

    reservation_id = str(uuid.uuid4())
    reserved_items = []

    for item in items:
        item_id = item["item_id"]
        quantity = item["quantity"]

        # Check availability and reserve
        response = inventory_table.get_item(Key={"item_id": item_id})
        stock = response.get("Item")

        if not stock or int(stock.get("available", 0)) < quantity:
            raise InsufficientInventoryError(
                f"Insufficient stock for item {item_id}: "
                f"requested {quantity}, available {stock.get('available', 0) if stock else 0}"
            )

        # Decrement available stock
        inventory_table.update_item(
            Key={"item_id": item_id},
            UpdateExpression="SET available = available - :qty, reserved = reserved + :qty",
            ExpressionAttributeValues={":qty": quantity},
            ConditionExpression="available >= :qty",
        )
        reserved_items.append({"item_id": item_id, "quantity": quantity})

    return {"reservation_id": reservation_id, "reserved_items": reserved_items}


@durable_step
def process_payment(step_context: StepContext, order_id: str, amount: str, customer_id: str) -> dict:
    """Step 2: Process payment (reserve funds)."""
    step_context.logger.info("Processing payment of %s for order %s", amount, order_id)

    payment_id = str(uuid.uuid4())

    # Simulate payment processing — in production, call a payment gateway
    # For demo: fail if amount > 10000 to trigger saga compensation
    if Decimal(amount) > Decimal("10000"):
        raise PaymentDeclinedError(f"Payment of {amount} declined: exceeds limit")

    payments_table.put_item(
        Item={
            "payment_id": payment_id,
            "order_id": order_id,
            "customer_id": customer_id,
            "amount": Decimal(amount),
            "status": "RESERVED",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
    )

    return {"payment_id": payment_id, "status": "RESERVED"}


@durable_step
def confirm_order(step_context: StepContext, order_id: str, reservation: dict, payment: dict) -> dict:
    """Step 3: Confirm the order after inventory and payment succeed."""
    step_context.logger.info("Confirming order %s", order_id)

    now = datetime.now(timezone.utc).isoformat()

    # Atomic: both writes succeed or neither does — prevents CONFIRMED order with un-CAPTURED payment
    dynamodb_client.transact_write_items(
        TransactItems=[
            {
                "Put": {
                    "TableName": os.environ["ORDERS_TABLE"],
                    "Item": {
                        "order_id": {"S": order_id},
                        "status": {"S": "CONFIRMED"},
                        "reservation_id": {"S": reservation["reservation_id"]},
                        "payment_id": {"S": payment["payment_id"]},
                        "confirmed_at": {"S": now},
                    },
                }
            },
            {
                "Update": {
                    "TableName": os.environ["PAYMENTS_TABLE"],
                    "Key": {"payment_id": {"S": payment["payment_id"]}},
                    "UpdateExpression": "SET #s = :status, confirmed_at = :now",
                    "ConditionExpression": "#s = :reserved",
                    "ExpressionAttributeNames": {"#s": "status"},
                    "ExpressionAttributeValues": {
                        ":status": {"S": "CAPTURED"},
                        ":reserved": {"S": "RESERVED"},
                        ":now": {"S": now},
                    },
                }
            },
        ]
    )

    return {"order_id": order_id, "status": "CONFIRMED"}


# ─── COMPENSATING STEPS (reverse order) ─────────────────────────────────────


@durable_step
def compensate_payment(step_context: StepContext, payment: dict) -> dict:
    """Compensation: Refund/cancel the payment reservation."""
    step_context.logger.info("Compensating payment %s", payment["payment_id"])

    payments_table.update_item(
        Key={"payment_id": payment["payment_id"]},
        UpdateExpression="SET #s = :status, cancelled_at = :now",
        ConditionExpression="#s = :reserved",
        ExpressionAttributeValues={
            ":status": "REFUNDED",
            ":reserved": "RESERVED",
            ":now": datetime.now(timezone.utc).isoformat(),
        },
        ExpressionAttributeNames={"#s": "status"},
    )

    return {"payment_id": payment["payment_id"], "status": "REFUNDED"}


@durable_step
def compensate_inventory(step_context: StepContext, reservation: dict) -> dict:
    """Compensation: Release reserved inventory back to available stock."""
    step_context.logger.info("Compensating inventory reservation %s", reservation["reservation_id"])

    for item in reservation["reserved_items"]:
        inventory_table.update_item(
            Key={"item_id": item["item_id"]},
            UpdateExpression="SET available = available + :qty, reserved = reserved - :qty",
            ExpressionAttributeValues={":qty": item["quantity"]},
        )

    return {"reservation_id": reservation["reservation_id"], "status": "RELEASED"}


@durable_step
def record_failed_order(step_context: StepContext, order_id: str, error: str) -> dict:
    """Record a failed order — in a step so it's checkpointed and not replayed."""
    orders_table.put_item(
        Item={
            "order_id": order_id,
            "status": "FAILED",
            "error": error,
            "failed_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    return {"order_id": order_id, "status": "FAILED"}


# ─── ORCHESTRATOR ────────────────────────────────────────────────────────────


@durable_execution
def lambda_handler(event, context: DurableContext) -> dict:
    """
    Saga orchestrator: executes steps in order, compensates in reverse on failure.

    Input event:
    {
        "order_id": "ORD-123",
        "customer_id": "CUST-456",
        "items": [{"item_id": "ITEM-A", "quantity": 2}],
        "total_amount": "99.99"
    }
    """
    _validate_event(event)

    # Generate order_id inside a step if not provided so it's stable across replays
    order_id = event.get("order_id") or context.step(generate_order_id())
    customer_id = event["customer_id"]
    items = event["items"]
    total_amount = event["total_amount"]

    completed_steps = []

    try:
        # Step 1: Reserve inventory — no retry, InsufficientInventoryError is deterministic
        reservation = context.step(reserve_inventory(order_id, items), config=_NO_RETRY_STEP_CONFIG)
        completed_steps.append(("inventory", reservation))
        context.logger.info("Inventory reserved: %s", reservation["reservation_id"])

        # Step 2: Process payment — no retry, PaymentDeclinedError is deterministic
        payment = context.step(process_payment(order_id, total_amount, customer_id), config=_NO_RETRY_STEP_CONFIG)
        completed_steps.append(("payment", payment))
        context.logger.info("Payment processed: %s", payment["payment_id"])

        # Step 3: Confirm order
        confirmation = context.step(confirm_order(order_id, reservation, payment))
        context.logger.info("Order confirmed: %s", order_id)

        return {
            "status": "SUCCESS",
            "order_id": order_id,
            "confirmation": confirmation,
        }

    except Exception as err:
        context.logger.error("Saga failed at step: %s. Starting compensation.", str(err))

        # Compensate in REVERSE order — track what actually succeeded
        successful_compensations = []
        failed_compensations = []
        for step_name, step_data in reversed(completed_steps):
            try:
                if step_name == "payment":
                    context.step(compensate_payment(step_data))
                elif step_name == "inventory":
                    context.step(compensate_inventory(step_data))
                successful_compensations.append(step_name)
            except Exception as comp_err:
                context.logger.error(
                    "Compensation failed for %s: %s", step_name, str(comp_err)
                )
                failed_compensations.append(step_name)

        context.step(record_failed_order(order_id, str(err)))

        if failed_compensations:
            # Publish to DLQ so the inconsistency surfaces for human remediation
            dlq_url = os.environ.get("COMPENSATION_DLQ_URL")
            if dlq_url:
                sqs_client.send_message(
                    QueueUrl=dlq_url,
                    MessageBody=json.dumps({
                        "order_id": order_id,
                        "failed_compensations": failed_compensations,
                        "original_error": str(err),
                    }),
                )

        return {
            "status": "FAILED",
            "order_id": order_id,
            "error": str(err),
            "compensations_executed": successful_compensations,
        }
