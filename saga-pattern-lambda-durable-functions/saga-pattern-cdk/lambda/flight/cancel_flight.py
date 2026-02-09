import json
import os
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-flight-bookings')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Cancel a flight booking by updating the status
    Handles both direct invocation and API Gateway events
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
        
        # Extract booking ID from event
        booking_id = body.get('bookingId')
        
        if not booking_id:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'bookingId is required'
                })
            }
        
        # Check if booking exists
        response = table.get_item(Key={'bookingId': booking_id})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({
                    'message': f'Booking {booking_id} not found'
                })
            }
        
        # Update booking status to CANCELLED
        table.update_item(
            Key={'bookingId': booking_id},
            UpdateExpression='SET #status = :status, updatedAt = :updatedAt',
            ExpressionAttributeNames={'#status': 'status'},
            ExpressionAttributeValues={
                ':status': 'CANCELLED',
                ':updatedAt': datetime.utcnow().isoformat()
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Flight booking cancelled successfully',
                'bookingId': booking_id,
                'status': 'CANCELLED'
            })
        }
        
    except ClientError as e:
        error_msg = f"DynamoDB error: {e.response['Error']['Message']}"
        print(error_msg)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to cancel flight booking',
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
                'message': 'Failed to cancel flight booking',
                'error': str(e),
                'errorType': type(e).__name__
            })
        }
