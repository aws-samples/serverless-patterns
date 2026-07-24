import json
import os
from datetime import datetime, timezone
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-hotel-reservations')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Cancel a hotel reservation by updating its status in Amazon DynamoDB.
    Invoked directly via context.invoke() from the saga orchestrator.
    Raises exceptions on failure so the durable SDK can handle retries.
    """
    if isinstance(event, str):
        event = json.loads(event)

    reservation_id = event.get('reservationId')

    if not reservation_id:
        raise ValueError("reservationId is required")

    # Verify reservation exists
    response = table.get_item(Key={'reservationId': reservation_id})

    if 'Item' not in response:
        raise LookupError(f"Reservation {reservation_id} not found")

    # Update reservation status to CANCELLED
    table.update_item(
        Key={'reservationId': reservation_id},
        UpdateExpression='SET #status = :status, updatedAt = :updatedAt',
        ExpressionAttributeNames={'#status': 'status'},
        ExpressionAttributeValues={
            ':status': 'CANCELLED',
            ':updatedAt': datetime.now(timezone.utc).isoformat()
        }
    )

    return {
        'reservationId': reservation_id,
        'status': 'CANCELLED'
    }
