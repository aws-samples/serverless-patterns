import json
import os
import uuid
from datetime import datetime, timezone
from decimal import Decimal
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-flight-bookings')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Reserve a flight by creating a booking record in Amazon DynamoDB.
    Invoked directly via context.invoke() from the saga orchestrator.
    Returns the booking result on success; raises exceptions on failure
    so the durable SDK can handle retries and error propagation.
    """
    if isinstance(event, str):
        event = json.loads(event)

    # Check for failure flag to test saga compensation
    if event.get('failBookFlight', False):
        raise RuntimeError("Simulated flight booking failure for testing saga compensation")

    # Validate required fields
    passenger_name = event.get('passengerName', 'John Doe')
    departure = event.get('departure', 'JFK')
    destination = event.get('destination', 'LAX')

    if not passenger_name or not departure or not destination:
        raise ValueError("Missing required fields: passengerName, departure, destination")

    # Extract booking details
    booking_id = event.get('bookingId', str(uuid.uuid4()))
    flight_number = event.get('flightNumber', f'FL{uuid.uuid4().hex[:6].upper()}')
    price = Decimal(str(event.get('price', 299.99)))

    # Create booking record in Amazon DynamoDB
    item = {
        'bookingId': booking_id,
        'passengerName': passenger_name,
        'flightNumber': flight_number,
        'departure': departure,
        'destination': destination,
        'price': price,
        'status': 'RESERVED',
        'createdAt': datetime.now(timezone.utc).isoformat(),
        'updatedAt': datetime.now(timezone.utc).isoformat()
    }

    table.put_item(Item=item)

    return {
        'bookingId': booking_id,
        'flightNumber': flight_number,
        'status': 'RESERVED',
        'price': float(price)
    }
