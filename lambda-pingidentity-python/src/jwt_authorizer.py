import json
import jwt
import os
from typing import Dict, Any
from jwt import PyJWKClient
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    PingOne JWT Authorizer Lambda function
    Validates JWT tokens from PingOne and returns authorization policy
    """
    print(f"PingOne Authorizer event: {json.dumps(event)}")
    
    try:
        # Extract token from Authorization header
        token = extract_token(event)
        if not token:
            print("No token found")
            return generate_policy('user', 'Deny', event['methodArn'])
        
        # Validate JWT token with PingOne
        payload = validate_pingone_jwt(token)
        if not payload:
            print("Invalid PingOne token")
            return generate_policy('user', 'Deny', event['methodArn'])
        
        user_id = payload.get('sub', 'unknown')
        print(f"PingOne token validated for user: {user_id}")
        
        # Generate allow policy with user context
        policy = generate_policy(user_id, 'Allow', event['methodArn'])
        policy['context'] = {
            'userId': user_id,
            'email': payload.get('email', ''),
            'scope': payload.get('scope', ''),
            'clientId': payload.get('client_id', ''),
            'issuer': payload.get('iss', ''),
            'tokenPayload': json.dumps(payload, default=str)
        }
        
        return policy
        
    except Exception as e:
        print(f"PingOne Authorizer error: {str(e)}")
        return generate_policy('user', 'Deny', event['methodArn'])

def extract_token(event: Dict[str, Any]) -> str:
    """Extract JWT token from Authorization header"""
    auth_header = event.get('authorizationToken', '')
    
    if auth_header.startswith('Bearer '):
        return auth_header[7:]  # Remove 'Bearer ' prefix
    
    return auth_header

def validate_pingone_jwt(token: str) -> Dict[str, Any]:
    """Validate JWT token with PingOne JWKS"""
    try:
        ping_issuer = os.environ.get('PING_ISSUER_URL')
        ping_jwks_url = os.environ.get('PING_JWKS_URL')
        
        if not ping_issuer or not ping_jwks_url:
            print("PingOne configuration missing")
            return None
        
        # Get signing key from PingOne JWKS
        jwks_client = PyJWKClient(ping_jwks_url)
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        
        # Validate token
        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            issuer=ping_issuer,
            options={"verify_aud": False}  # Skip audience validation for simplicity
        )
        
        print(f"PingOne JWT payload: {json.dumps(payload, default=str)}")
        return payload
        
    except ExpiredSignatureError:
        print("PingOne token has expired")
        return None
    except InvalidTokenError as e:
        print(f"Invalid PingOne token: {str(e)}")
        return None
    except Exception as e:
        print(f"PingOne JWT validation error: {str(e)}")
        return None

def generate_policy(principal_id: str, effect: str, resource: str) -> Dict[str, Any]:
    """Generate IAM policy for API Gateway"""
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource
                }
            ]
        }
    }
