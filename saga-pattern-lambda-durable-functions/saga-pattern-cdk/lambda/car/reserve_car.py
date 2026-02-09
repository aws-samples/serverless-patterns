import json
import os
import uuid
from datetime import datetime
from decimal import Decimal
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-car-rentals')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Reserve a car rental by creating a rental record in DynamoDB
    Handles both direct invocation and API Gateway events
    Supports failBookCar flag for testing saga compensation
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
        if body.get('failBookCar', False):
            print("SIMULATED FAILURE: failBookCar flag is set to True")
            raise Exception("Simulated car rental failure for testing saga compensation")
        
        # Extract rental details from event
        rental_id = body.get('rentalId', str(uuid.uuid4()))
        driver_name = body.get('driverName', 'John Doe')
        car_type = body.get('carType', 'Sedan')
        pickup_location = body.get('pickupLocation', 'Airport')
        dropoff_location = body.get('dropoffLocation', 'Airport')
        pickup_date = body.get('pickupDate', datetime.utcnow().date().isoformat())
        dropoff_date = body.get('dropoffDate', datetime.utcnow().date().isoformat())
        price = Decimal(str(body.get('price', 89.99)))  # Convert to Decimal for DynamoDB
        
        # Validate required fields
        if not driver_name or not car_type:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'Missing required fields: driverName, carType'
                })
            }
        
        # Create rental record
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
            'createdAt': datetime.utcnow().isoformat(),
            'updatedAt': datetime.utcnow().isoformat()
        }
        
        # Put item in DynamoDB
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Car reserved successfully',
                'rentalId': rental_id,
                'carType': car_type,
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
                'message': 'Failed to reserve car',
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
                'message': 'Failed to reserve car',
                'error': str(e),
                'errorType': type(e).__name__
            })
        }
