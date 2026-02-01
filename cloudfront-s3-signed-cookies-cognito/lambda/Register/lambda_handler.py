import json
import os
from typing import Any, Dict

import boto3
from botocore.exceptions import ClientError
from aws_lambda_powertools import Logger

logger = Logger()

# Initialize Cognito client
cognito_client = boto3.client('cognito-idp')

# Environment variables
USER_POOL_ID = os.environ['USER_POOL_ID']
USER_POOL_CLIENT_ID = os.environ['USER_POOL_CLIENT_ID']
ALLOWED_ORIGIN = os.environ.get('ALLOWED_ORIGIN', '*')


def get_cors_headers() -> Dict[str, str]:
    """Return CORS headers based on configuration."""
    return {
        'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
        'Access-Control-Allow-Credentials': 'true',
        'Content-Type': 'application/json'
    }


@logger.inject_lambda_context(log_event=True)
def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for user registration."""
    # Extract request information for logging
    request_id = context.aws_request_id
    logger.append_keys(request_id=request_id)
    
    # Handle preflight OPTIONS requests for CORS
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
                'Access-Control-Allow-Headers': 'Content-Type,Authorization',
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
                'Access-Control-Allow-Credentials': 'true'
            },
            'body': ''
        }
    
    event_body = json.loads(event.get('body')) if 'body' in event else event

    email = event_body.get('email')
    password = event_body.get('password')
    name = event_body.get('name', '')

    logger.info("Processing registration", extra={
        "email": email,
        "has_name": bool(name)
    })
    
    # Validate input
    if not email or not password:
        logger.warning("Registration validation failed", extra={
            "reason": "missing_required_fields",
            "has_email": bool(email),
            "has_password": bool(event_body.get('password'))
        })
    
        return {
            'statusCode': 400,
            'headers': get_cors_headers(),
            'body': json.dumps({'message': 'Email and password are required'})
        }
    
    return register_user(email, password, name)


def register_user(email: str, password: str, name: str) -> Dict[str, Any]:
    """Register a new user in Cognito."""
    headers = get_cors_headers()
    
    try:
        # Register user in Cognito
        response = cognito_client.sign_up(
            ClientId=USER_POOL_CLIENT_ID,
            Username=email,
            Password=password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                },
                {
                    'Name': 'name',
                    'Value': name
                }
            ]
        )
        
        # Auto confirm the user (for development purposes)
        # In production, you might want to use email verification
        cognito_client.admin_confirm_sign_up(
            UserPoolId=USER_POOL_ID,
            Username=email
        )

        logger.info("User sign-up successful", extra={
            "user_sub": response['UserSub']
        })
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'User registered successfully',
                'userSub': response['UserSub']
            })
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        
        logger.error("Cognito client error", extra={
            "error_code": error_code,
            "error_message": error_message,
            "operation": "sign_up/admin_confirm_sign_up"
        })
        
        if error_code == 'UsernameExistsException':
            return {
                'statusCode': 409,
                'headers': headers,
                'body': json.dumps({'message': 'User already exists'})
            }
        
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'message': f'Registration error: {error_message}'})
        }
        
    except Exception as e:
        logger.exception("Unexpected error during registration", extra={
            "error": str(e)
        })
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'message': 'An unexpected error occurred'})
        }