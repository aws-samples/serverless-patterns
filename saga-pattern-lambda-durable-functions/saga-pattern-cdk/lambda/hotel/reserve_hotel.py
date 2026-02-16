import json
import os
import uuid
from datetime import datetime
from decimal import Decimal
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-hotel-reservations')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Reserve a hotel by creating a reservation record in DynamoDB
    Handles both direct invocation and API Gateway events
    Supports failBookHotel flag for testing saga compensation
    """
    try:
        # Handle different event formats
        if isinstance(event, str):
            event = json.loads(event)
        
        # If event has a 'body' field (API Gateway format), parse it
        if 'body' in event:
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            body = event
        
        # Check for failure flag to test saga compensation
        if body.get('failBookHotel', False):
            print("SIMULATED FAILURE: failBookHotel flag is set to True")
            raise Exception("Simulated hotel reservation failure for testing saga compensation")
        
        # Extract reservation details from event
        reservation_id = body.get('reservationId', str(uuid.uuid4()))
        guest_name = body.get('guestName', 'John Doe')
        hotel_name = body.get('hotelName', 'Grand Hotel')
        room_type = body.get('roomType', 'Deluxe Suite')
        check_in = body.get('checkIn', datetime.utcnow().date().isoformat())
        check_out = body.get('checkOut', datetime.utcnow().date().isoformat())
        price = Decimal(str(body.get('price', 199.99)))  # Convert to Decimal for DynamoDB
        
        # Validate required fields
        if not guest_name or not hotel_name:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'Missing required fields: guestName, hotelName'
                })
            }
        
        # Create reservation record
        item = {
            'reservationId': reservation_id,
            'guestName': guest_name,
            'hotelName': hotel_name,
            'roomType': room_type,
            'checkIn': check_in,
            'checkOut': check_out,
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
                'message': 'Hotel reserved successfully',
                'reservationId': reservation_id,
                'hotelName': hotel_name,
                'roomType': room_type,
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
                'message': 'Failed to reserve hotel',
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
                'message': 'Failed to reserve hotel',
                'error': str(e),
                'errorType': type(e).__name__
            })
        }
