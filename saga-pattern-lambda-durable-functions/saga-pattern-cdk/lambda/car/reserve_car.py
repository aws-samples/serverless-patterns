import json
import os
import uuid
from datetime import datetime, timezone
from decimal import Decimal
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-car-rentals')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Reserve a car rental by creating a rental record in Amazon DynamoDB.
    Invoked directly via context.invoke() from the saga orchestrator.
    Returns the rental result on success; raises exceptions on failure
    so the durable SDK can handle retries and error propagation.
    """
    if isinstance(event, str):
        event = json.loads(event)

    # Check for failure flag to test saga compensation
    if event.get('failBookCar', False):
        raise RuntimeError("Simulated car rental failure for testing saga compensation")

    # Validate required fields
    driver_name = event.get('driverName', 'John Doe')
    car_type = event.get('carType', 'Sedan')

    if not driver_name or not car_type:
        raise ValueError("Missing required fields: driverName, carType")

    # Extract rental details
    rental_id = event.get('rentalId', str(uuid.uuid4()))
    pickup_location = event.get('pickupLocation', 'Airport')
    dropoff_location = event.get('dropoffLocation', 'Airport')
    pickup_date = event.get('pickupDate', datetime.now(timezone.utc).date().isoformat())
    dropoff_date = event.get('dropoffDate', datetime.now(timezone.utc).date().isoformat())
    price = Decimal(str(event.get('price', 89.99)))

    # Create rental record in Amazon DynamoDB
    item = {
        'rentalId': rental_id,
        'driverName': driver_name,
        'carType': car_type,
        'pickupLocation': pickup_location,
        'dropoffLocation': dropoff_location,
        'pickupDate': pickup_date,
        'dropoffDate': dropoff_date,
        'price': price,
        'status': 'RESERVED',
        'createdAt': datetime.now(timezone.utc).isoformat(),
        'updatedAt': datetime.now(timezone.utc).isoformat()
    }

    table.put_item(Item=item)

    return {
        'rentalId': rental_id,
        'carType': car_type,
        'status': 'RESERVED',
        'price': float(price)
    }
