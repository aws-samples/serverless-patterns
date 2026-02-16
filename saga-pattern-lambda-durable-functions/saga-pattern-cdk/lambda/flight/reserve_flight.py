import json
import os
import uuid
from datetime import datetime
from decimal import Decimal
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-flight-bookings')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Reserve a flight by creating a booking record in DynamoDB
    Handles both direct invocation and API Gateway events
    Supports failBookFlight flag for testing saga compensation
    """
    try:
        # Handle different event formats (direct invocation vs API Gateway)
        if isinstance(event, str):
            event = json.loads(event)
        
        # If event has a 'body' field (API Gateway format), parse it
        if 'body' in event:
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            body = event
        
        # Check for failure flag to test saga compensation
        if body.get('failBookFlight', False):
            print("SIMULATED FAILURE: failBookFlight flag is set to True")
            raise Exception("Simulated flight booking failure for testing saga compensation")
        
        # Extract booking details from event
        booking_id = body.get('bookingId', str(uuid.uuid4()))
        passenger_name = body.get('passengerName', 'John Doe')
        flight_number = body.get('flightNumber', f'FL{uuid.uuid4().hex[:6].upper()}')
        departure = body.get('departure', 'JFK')
        destination = body.get('destination', 'LAX')
        price = Decimal(str(body.get('price', 299.99)))  # Convert to Decimal for DynamoDB
        
        # Validate required fields
        if not passenger_name or not departure or not destination:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'Missing required fields: passengerName, departure, destination'
                })
            }
        
        # Create booking record
        item = {
            'bookingId': booking_id,
            'passengerName': passenger_name,
            'flightNumber': flight_number,
            'departure': departure,
            'destination': destination,
            'price': price,
            'status': 'RESERVED',
            'createdAt': datetime.utcnow().isoformat(),
            'updatedAt': datetime.utcnow().isoformat()
        }
        
        # Put item in DynamoDB
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Flight reserved successfully',
                'bookingId': booking_id,
                'flightNumber': flight_number,
                'status': 'RESERVED',
                'price': float(price)  # Convert back to float for JSON response
            })
        }
        
    except ClientError as e:
        error_msg = f"DynamoDB error: {e.response['Error']['Message']}"
        print(error_msg)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to reserve flight',
                'error': e.response['Error']['Message'],
                'errorType': 'DynamoDBError'
            })
        }
    except json.JSONDecodeError as e:
        error_msg = f"JSON parsing error: {str(e)}"
        print(error_msg)
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Invalid JSON in request',
                'error': str(e),
                'errorType': 'JSONDecodeError'
            })
        }
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(error_msg)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to reserve flight',
                'error': str(e),
                'errorType': type(e).__name__
            })
        }
