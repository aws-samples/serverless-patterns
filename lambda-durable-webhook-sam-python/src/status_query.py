"""
Status Query Function
Retrieves webhook processing status from DynamoDB
"""
import json
import os
from typing import Dict, Any
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['EVENTS_TABLE_NAME'])


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Query webhook processing status
    
    Args:
        event: API Gateway event with executionToken in path parameters
        context: Lambda context
    
    Returns:
        HTTP response with status information
    """
    print(f"Status query event: {json.dumps(event)}")
    
    # Extract execution token from path parameters
    execution_token = event.get('pathParameters', {}).get('executionToken')
    
    if not execution_token:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Missing executionToken in path'
            })
        }
    
    print(f"Querying status for execution token: {execution_token}")
    
    try:
        # Query DynamoDB for the execution token
        response = table.get_item(
            Key={'executionToken': execution_token}
        )
        
        if 'Item' not in response:
            print(f"Execution token not found: {execution_token}")
            return {
                'statusCode': 404,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': 'Execution token not found',
                    'executionToken': execution_token
                })
            }
        
        item = response['Item']
        
        # Build response
        status_response = {
            'executionToken': item['executionToken'],
            'status': item['status'],
            'currentStep': item.get('currentStep'),
            'createdAt': item['createdAt'],
            'lastUpdated': item['lastUpdated']
        }
        
        # Include error if present
        if 'error' in item:
            status_response['error'] = item['error']
        
        # Include webhook payload summary (not full payload for security)
        if 'webhookPayload' in item:
            payload = item['webhookPayload']
            status_response['webhookSummary'] = {
                'type': payload.get('type', payload.get('event', 'unknown')),
                'source': payload.get('source', payload.get('sender', 'unknown')),
                'keys': list(payload.keys())[:10]  # Limit to first 10 keys
            }
        
        print(f"Status retrieved successfully: {execution_token}, status: {item['status']}")
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(status_response)
        }
    
    except Exception as e:
        print(f"Error querying status: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e)
            })
        }
