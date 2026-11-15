import boto3
import json
import os
import logging
from datetime import datetime, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
ses = boto3.client("ses")

TABLE_NAME = os.environ["DYNAMODB_TABLE"]
SENDER_EMAIL = os.environ["SENDER_EMAIL"]

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    """
    Notification Processor — invoked hourly by EventBridge Scheduler.

    1. Queries the DynamoDB GSI for records where CartAbandoned = "true"
    2. Filters for NotificationSent = "false"
    3. Sends a personalised abandoned-cart email via SES
    4. Marks NotificationSent = "true" so the customer is not emailed again
    """
    logger.info("Received event: %s", json.dumps(event))
    invoked_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # ── 1. Query the GSI for all abandoned carts ──
    abandoned = _get_abandoned_carts()
    logger.info("Found %d abandoned cart(s) needing notification", len(abandoned))

    if not abandoned:
        return _response(invoked_at, sent=0, skipped=0, errors=0)

    sent = 0
    skipped = 0
    errors = 0

    for record in abandoned:
        customer_id = record.get("CustomerId", "unknown")
        email = record.get("Email", "")
        name = record.get("CustomerName", "Customer")
        notification_sent = record.get("NotificationSent", "false")

        # ── 2. Skip if already notified ──
        if notification_sent == "true":
            logger.info("Skipping %s — already notified", customer_id)
            skipped += 1
            continue

        # ── 3. Skip if no email address ──
        if not email:
            logger.warning("Skipping %s — no email address", customer_id)
            skipped += 1
            continue

        # ── 4. Build and send the email ──
        try:
            cart_items = _format_cart_items(record.get("CartItems", []))
            cart_total = record.get("CartTotal", "0.00")
            abandoned_at = record.get("CartAbandonedAt", "recently")

            _send_email(email, name, cart_items, cart_total, abandoned_at)
            logger.info("Sent notification to %s (%s)", customer_id, email)

            # ── 5. Mark as notified ──
            _mark_notified(customer_id, invoked_at)
            sent += 1

        except Exception as e:
            logger.error(
                "Failed to notify %s (%s): %s", customer_id, email, str(e)
            )
            errors += 1

    return _response(invoked_at, sent=sent, skipped=skipped, errors=errors)


# ──────────────────────────────────────────
# DynamoDB helpers
# ──────────────────────────────────────────


def _get_abandoned_carts() -> list:
    """
    Query the GSI for all records with CartAbandoned = 'true'.
    The GSI returns all abandoned carts; we filter NotificationSent
    in application code for flexibility.
    """
    items = []
    last_key = None

    while True:
        query_params = {
            "IndexName": "CartAbandonedIndex",
            "KeyConditionExpression": "CartAbandoned = :abandoned",
            "ExpressionAttributeValues": {":abandoned": "true"},
        }

        if last_key:
            query_params["ExclusiveStartKey"] = last_key

        response = table.query(**query_params)
        items.extend(response.get("Items", []))

        last_key = response.get("LastEvaluatedKey")
        if not last_key:
            break

    return items


def _mark_notified(customer_id: str, notified_at: str) -> None:
    """Set NotificationSent = 'true' and record the timestamp."""
    table.update_item(
        Key={"CustomerId": customer_id},
        UpdateExpression=(
            "SET NotificationSent = :sent, NotifiedAt = :ts"
        ),
        ExpressionAttributeValues={
            ":sent": "true",
            ":ts": notified_at,
        },
    )


# ──────────────────────────────────────────
# SES helpers
# ──────────────────────────────────────────


def _send_email(
    to_email: str,
    customer_name: str,
    cart_items_html: str,
    cart_total: str,
    abandoned_at: str,
) -> None:
    """Send a personalised abandoned-cart email via SES."""

    subject = f"{customer_name}, you left something in your cart!"

    html_body = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background-color: #ff9900; color: white; padding: 20px;
                       text-align: center; border-radius: 8px 8px 0 0; }}
            .content {{ padding: 20px; border: 1px solid #ddd;
                        border-top: none; border-radius: 0 0 8px 8px; }}
            .cart-table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
            .cart-table th, .cart-table td {{ padding: 10px; text-align: left;
                                             border-bottom: 1px solid #eee; }}
            .cart-table th {{ background-color: #f5f5f5; }}
            .total {{ font-size: 18px; font-weight: bold; color: #ff9900; }}
            .cta-button {{ display: inline-block; background-color: #ff9900;
                           color: white; padding: 12px 30px; text-decoration: none;
                           border-radius: 5px; font-weight: bold; margin-top: 15px; }}
            .footer {{ text-align: center; color: #999; font-size: 12px;
                       margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Don't forget your items!</h1>
            </div>
            <div class="content">
                <p>Hi {customer_name},</p>
                <p>We noticed you left some great items in your cart on
                   <strong>{abandoned_at}</strong>. They're still waiting
                   for you!</p>

                {cart_items_html}

                <p class="total">Cart Total: ${cart_total}</p>

                <p>Complete your purchase before these items sell out.</p>

                <a href="https://example.com/cart" class="cta-button">
                    Return to Your Cart
                </a>

                <p style="margin-top:20px; color:#666; font-size:13px;">
                    If you've already completed your purchase, please
                    disregard this email.</p>
            </div>
            <div class="footer">
                <p>This is an automated notification. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """

    text_body = (
        f"Hi {customer_name},\n\n"
        f"You left items in your cart on {abandoned_at}.\n"
        f"Cart Total: ${cart_total}\n\n"
        f"Return to your cart: https://example.com/cart\n\n"
        f"If you've already completed your purchase, please disregard."
    )

    ses.send_email(
        Source=SENDER_EMAIL,
        Destination={"ToAddresses": [to_email]},
        Message={
            "Subject": {"Data": subject, "Charset": "UTF-8"},
            "Body": {
                "Html": {"Data": html_body, "Charset": "UTF-8"},
                "Text": {"Data": text_body, "Charset": "UTF-8"},
            },
        },
    )


def _format_cart_items(cart_items: list) -> str:
    """Convert DynamoDB cart items list into an HTML table."""
    if not cart_items:
        return "<p><em>Your cart items are waiting for you.</em></p>"

    rows = ""
    for item in cart_items:
        name = item.get("ItemName", "Item")
        price = item.get("Price", "0.00")
        # Handle both Decimal (from DynamoDB resource) and string
        rows += f"<tr><td>{name}</td><td>${price}</td></tr>\n"

    return f"""
    <table class="cart-table">
        <thead>
            <tr><th>Item</th><th>Price</th></tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    """


# ──────────────────────────────────────────
# Response helper
# ──────────────────────────────────────────


def _response(invoked_at: str, sent: int, skipped: int, errors: int) -> dict:
    """Build a structured Lambda response."""
    summary = {
        "invokedAt": invoked_at,
        "notificationsSent": sent,
        "skipped": skipped,
        "errors": errors,
    }
    logger.info("Execution summary: %s", json.dumps(summary))
    return {"statusCode": 200, "body": json.dumps(summary)}