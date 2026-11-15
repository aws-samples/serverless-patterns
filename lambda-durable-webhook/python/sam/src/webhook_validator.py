"""
Webhook Validator - Synchronous validation before async processing
Validates HMAC signature and invokes durable processor
"""
import json
import os
import hmac
import hashlib
import boto3

lambda_client = boto3.client('lambda')


def validate_signature(payload: str, signature: str, secret: str) -> bool:
    """Validate HMAC-SHA256 signature"""
    if not secret or not signature:
        return True
    
    if signature.startswith('sha256='):
        signature = signature[7:]
    
    expected = hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected, signature)


def lambda_handler(event, context):
    """Validate webhook and invoke durable processor"""
    
    # Parse request
    body = event.get('body', '{}')
    headers = event.get('headers', {})
    signature = headers.get('x-hub-signature-256', headers.get('X-Hub-Signature-256', ''))
    webhook_secret = os.environ.get('WEBHOOK_SECRET', '')
    
    # Validate signature
    if webhook_secret and not validate_signature(body, signature, webhook_secret):
        return {
            'statusCode': 401,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Invalid signature'})
        }
    
    # Parse payload
    try:
        payload = json.loads(body) if isinstance(body, str) else body
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Invalid JSON'})
        }
    
    # Invoke durable processor asynchronously
    processor_arn = os.environ['PROCESSOR_FUNCTION_NAME']
    lambda_client.invoke(
        FunctionName=processor_arn,
        InvocationType='Event',
        Payload=json.dumps(payload)
    )
    
    return {
        'statusCode': 202,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({
            'message': 'Webhook accepted for processing',
            'requestId': context.aws_request_id
        })
    }
