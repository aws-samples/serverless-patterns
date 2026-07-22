"""
Saga orchestrator using Lambda Durable Functions (Python).

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
from decimal import Decimal

import boto3
from aws_durable_execution_sdk_python.context import DurableContext, StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
orders_table = dynamodb.Table(os.environ["ORDERS_TABLE"])
payments_table = dynamodb.Table(os.environ["PAYMENTS_TABLE"])
inventory_table = dynamodb.Table(os.environ["INVENTORY_TABLE"])


# ─── FORWARD STEPS ───────────────────────────────────────────────────────────


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

    orders_table.put_item(
        Item={
            "order_id": order_id,
            "status": "CONFIRMED",
            "reservation_id": reservation["reservation_id"],
            "payment_id": payment["payment_id"],
            "confirmed_at": now,
        }
    )

    # Finalize payment
    payments_table.update_item(
        Key={"payment_id": payment["payment_id"]},
        UpdateExpression="SET #s = :status, confirmed_at = :now",
        ExpressionAttributeValues={":status": "CAPTURED", ":now": now},
        ExpressionAttributeNames={"#s": "status"},
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
        ExpressionAttributeValues={
            ":status": "REFUNDED",
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
    order_id = event.get("order_id", str(uuid.uuid4()))
    customer_id = event["customer_id"]
    items = event["items"]
    total_amount = event["total_amount"]

    completed_steps = []

    try:
        # Step 1: Reserve inventory
        reservation = context.step(reserve_inventory(order_id, items))
        completed_steps.append(("inventory", reservation))
        context.logger.info("Inventory reserved: %s", reservation["reservation_id"])

        # Step 2: Process payment
        payment = context.step(process_payment(order_id, total_amount, customer_id))
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

        # Compensate in REVERSE order
        for step_name, step_data in reversed(completed_steps):
            try:
                if step_name == "payment":
                    context.step(compensate_payment(step_data))
                elif step_name == "inventory":
                    context.step(compensate_inventory(step_data))
            except Exception as comp_err:
                context.logger.error(
                    "Compensation failed for %s: %s", step_name, str(comp_err)
                )

        # Record failed order
        orders_table.put_item(
            Item={
                "order_id": order_id,
                "status": "FAILED",
                "error": str(err),
                "failed_at": datetime.now(timezone.utc).isoformat(),
            }
        )

        return {
            "status": "FAILED",
            "order_id": order_id,
            "error": str(err),
            "compensations_executed": [s[0] for s in reversed(completed_steps)],
        }


# ─── Custom Exceptions ───────────────────────────────────────────────────────


class InsufficientInventoryError(Exception):
    """Raised when requested quantity exceeds available stock."""
    pass


class PaymentDeclinedError(Exception):
    """Raised when payment processing is declined."""
    pass
