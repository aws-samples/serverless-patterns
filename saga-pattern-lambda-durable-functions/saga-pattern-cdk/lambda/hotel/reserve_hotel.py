import json
import os
import uuid
from datetime import datetime, timezone
from decimal import Decimal
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-hotel-reservations')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Reserve a hotel by creating a reservation record in Amazon DynamoDB.
    Invoked directly via context.invoke() from the saga orchestrator.
    Returns the reservation result on success; raises exceptions on failure
    so the durable SDK can handle retries and error propagation.
    """
    if isinstance(event, str):
        event = json.loads(event)

    # Check for failure flag to test saga compensation
    if event.get('failBookHotel', False):
        raise RuntimeError("Simulated hotel reservation failure for testing saga compensation")

    # Validate required fields
    guest_name = event.get('guestName', 'John Doe')
    hotel_name = event.get('hotelName', 'Grand Hotel')

    if not guest_name or not hotel_name:
        raise ValueError("Missing required fields: guestName, hotelName")

    # Extract reservation details
    reservation_id = event.get('reservationId', str(uuid.uuid4()))
    room_type = event.get('roomType', 'Deluxe Suite')
    check_in = event.get('checkIn', datetime.now(timezone.utc).date().isoformat())
    check_out = event.get('checkOut', datetime.now(timezone.utc).date().isoformat())
    price = Decimal(str(event.get('price', 199.99)))

    # Create reservation record in Amazon DynamoDB
    item = {
        'reservationId': reservation_id,
        'guestName': guest_name,
        'hotelName': hotel_name,
        'roomType': room_type,
        'checkIn': check_in,
        'checkOut': check_out,
        'price': price,
        'status': 'RESERVED',
        'createdAt': datetime.now(timezone.utc).isoformat(),
        'updatedAt': datetime.now(timezone.utc).isoformat()
    }

    table.put_item(Item=item)

    return {
        'reservationId': reservation_id,
        'hotelName': hotel_name,
        'roomType': room_type,
        'status': 'RESERVED',
        'price': float(price)
    }
