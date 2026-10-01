import json
import os
from datetime import datetime, timezone
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-flight-bookings')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Cancel a flight booking by updating its status in Amazon DynamoDB.
    Invoked directly via context.invoke() from the saga orchestrator.
    Raises exceptions on failure so the durable SDK can handle retries.
    """
    if isinstance(event, str):
        event = json.loads(event)

    booking_id = event.get('bookingId')

    if not booking_id:
        raise ValueError("bookingId is required")

    # Verify booking exists
    response = table.get_item(Key={'bookingId': booking_id})

    if 'Item' not in response:
        raise LookupError(f"Booking {booking_id} not found")

    # Update booking status to CANCELLED
    table.update_item(
        Key={'bookingId': booking_id},
        UpdateExpression='SET #status = :status, updatedAt = :updatedAt',
        ExpressionAttributeNames={'#status': 'status'},
        ExpressionAttributeValues={
            ':status': 'CANCELLED',
            ':updatedAt': datetime.now(timezone.utc).isoformat()
        }
    )

    return {
        'bookingId': booking_id,
        'status': 'CANCELLED'
    }
