import json
import os
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'saga-car-rentals')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Cancel a car rental by updating the status
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
        
        # Extract rental ID from event
        rental_id = body.get('rentalId')
        
        if not rental_id:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'rentalId is required'
                })
            }
        
        # Check if rental exists
        response = table.get_item(Key={'rentalId': rental_id})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({
                    'message': f'Rental {rental_id} not found'
                })
            }
        
        # Update rental status to CANCELLED
        table.update_item(
            Key={'rentalId': rental_id},
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
                'message': 'Car rental cancelled successfully',
                'rentalId': rental_id,
                'status': 'CANCELLED'
            })
        }
        
    except ClientError as e:
        error_msg = f"DynamoDB error: {e.response['Error']['Message']}"
        print(error_msg)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to cancel car rental',
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
                'message': 'Failed to cancel car rental',
                'error': str(e),
                'errorType': type(e).__name__
            })
        }
