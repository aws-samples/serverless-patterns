import json
import os
from datetime import datetime, timezone
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-car-rentals')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Cancel a car rental by updating its status in Amazon DynamoDB.
    Invoked directly via context.invoke() from the saga orchestrator.
    Raises exceptions on failure so the durable SDK can handle retries.
    """
    if isinstance(event, str):
        event = json.loads(event)

    rental_id = event.get('rentalId')

    if not rental_id:
        raise ValueError("rentalId is required")

    # Verify rental exists
    response = table.get_item(Key={'rentalId': rental_id})

    if 'Item' not in response:
        raise LookupError(f"Rental {rental_id} not found")

    # Update rental status to CANCELLED
    table.update_item(
        Key={'rentalId': rental_id},
        UpdateExpression='SET #status = :status, updatedAt = :updatedAt',
        ExpressionAttributeNames={'#status': 'status'},
        ExpressionAttributeValues={
            ':status': 'CANCELLED',
            ':updatedAt': datetime.now(timezone.utc).isoformat()
        }
    )

    return {
        'rentalId': rental_id,
        'status': 'CANCELLED'
    }
