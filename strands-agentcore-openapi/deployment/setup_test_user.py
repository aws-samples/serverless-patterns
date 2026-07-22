#!/usr/bin/env python3
"""
Create a test user in Cognito User Pool and obtain JWT token.

This script creates a test user with a permanent password, authenticates,
and saves the credentials and JWT token for testing.
"""

import boto3
import json
import sys
from pathlib import Path
from typing import Dict, Optional
from botocore.exceptions import ClientError


def load_stack_outputs() -> Optional[Dict[str, str]]:
    """Load CloudFormation stack outputs."""
    outputs_file = Path("deployment/stack_outputs.json")
    
    if not outputs_file.exists():
        print(f"✗ Stack outputs not found: {outputs_file}")
        print("  Run: python deployment/deploy_stack.py")
        return None
    
    try:
        with open(outputs_file, 'r') as f:
            outputs = json.load(f)
        return outputs
    except Exception as e:
        print(f"✗ Failed to load stack outputs: {e}")
        return None


def get_user_pool_client_id(cognito_client, user_pool_id: str) -> Optional[str]:
    """Get the first user pool client ID."""
    try:
        response = cognito_client.list_user_pool_clients(
            UserPoolId=user_pool_id,
            MaxResults=10
        )
        
        if not response.get('UserPoolClients'):
            print("  ✗ No user pool clients found")
            return None
        
        client_id = response['UserPoolClients'][0]['ClientId']
        client_name = response['UserPoolClients'][0]['ClientName']
        
        print(f"  User Pool Client: {client_name}")
        print(f"  Client ID: {client_id}")
        
        return client_id
        
    except ClientError as e:
        print(f"  ✗ Failed to get client ID: {e}")
        return None


def create_or_update_user(
    cognito_client,
    user_pool_id: str,
    username: str,
    email: str,
    password: str
) -> bool:
    """Create or update a Cognito user."""
    try:
        # Try to create user
        print(f"\nCreating user: {username}")
        try:
            cognito_client.admin_create_user(
                UserPoolId=user_pool_id,
                Username=username,
                UserAttributes=[
                    {'Name': 'email', 'Value': email},
                    {'Name': 'email_verified', 'Value': 'true'}
                ],
                TemporaryPassword=password,
                MessageAction='SUPPRESS'
            )
            print("  ✓ User created")
        except ClientError as e:
            if e.response['Error']['Code'] == 'UsernameExistsException':
                print("  ℹ User already exists - deleting and recreating...")
                
                # Delete existing user
                cognito_client.admin_delete_user(
                    UserPoolId=user_pool_id,
                    Username=username
                )
                
                # Recreate user
                cognito_client.admin_create_user(
                    UserPoolId=user_pool_id,
                    Username=username,
                    UserAttributes=[
                        {'Name': 'email', 'Value': email},
                        {'Name': 'email_verified', 'Value': 'true'}
                    ],
                    TemporaryPassword=password,
                    MessageAction='SUPPRESS'
                )
                print("  ✓ User recreated")
            else:
                raise
        
        # Set permanent password
        print("  Setting permanent password...")
        cognito_client.admin_set_user_password(
            UserPoolId=user_pool_id,
            Username=username,
            Password=password,
            Permanent=True
        )
        print("  ✓ Password set")
        
        return True
        
    except ClientError as e:
        print(f"  ✗ Failed to create user: {e}")
        return False


def authenticate_user(
    cognito_client,
    client_id: str,
    username: str,
    password: str
) -> Optional[Dict[str, str]]:
    """Authenticate user and get JWT tokens."""
    try:
        print("\nAuthenticating user...")
        
        response = cognito_client.initiate_auth(
            ClientId=client_id,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        
        auth_result = response['AuthenticationResult']
        
        tokens = {
            'access_token': auth_result['AccessToken'],
            'id_token': auth_result['IdToken'],
            'refresh_token': auth_result.get('RefreshToken', ''),
            'expires_in': auth_result.get('ExpiresIn', 3600)
        }
        
        print("  ✓ Authentication successful")
        print(f"  Access Token: {tokens['access_token'][:50]}...")
        print(f"  ID Token: {tokens['id_token'][:50]}...")
        print(f"  Expires in: {tokens['expires_in']} seconds")
        
        return tokens
        
    except ClientError as e:
        print(f"  ✗ Authentication failed: {e}")
        return None


def decode_jwt_token(token: str) -> Optional[Dict]:
    """Decode JWT token to show claims (without verification)."""
    try:
        import base64
        
        # Split token into parts
        parts = token.split('.')
        if len(parts) != 3:
            return None
        
        # Decode payload (add padding if needed)
        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:
            payload += '=' * padding
        
        decoded = base64.urlsafe_b64decode(payload)
        claims = json.loads(decoded)
        
        return claims
        
    except Exception:
        return None


def setup_test_user(
    username: str = "testuser@example.com",
    password: str = "TestPassword123!"
) -> bool:
    """Set up test user and save credentials."""
    print("=" * 60)
    print("COGNITO TEST USER SETUP")
    print("=" * 60)
    
    # Load stack outputs
    print("\nLoading stack outputs...")
    outputs = load_stack_outputs()
    if not outputs:
        return False
    
    user_pool_id = outputs.get('CognitoUserPoolId')
    if not user_pool_id:
        print("✗ CognitoUserPoolId not found in stack outputs")
        return False
    
    print(f"  User Pool ID: {user_pool_id}")
    
    # Initialize Cognito client
    cognito_client = boto3.client('cognito-idp', region_name='us-east-1')
    
    # Get client ID
    print("\nGetting User Pool Client ID...")
    client_id = get_user_pool_client_id(cognito_client, user_pool_id)
    if not client_id:
        return False
    
    # Create or update user
    email = username  # Username is email for this user pool
    if not create_or_update_user(cognito_client, user_pool_id, username, email, password):
        return False
    
    # Authenticate and get tokens
    tokens = authenticate_user(cognito_client, client_id, username, password)
    if not tokens:
        return False
    
    # Decode ID token to show claims
    print("\nID Token Claims:")
    claims = decode_jwt_token(tokens['id_token'])
    if claims:
        print(f"  sub (user_id): {claims.get('sub', 'N/A')}")
        print(f"  email: {claims.get('email', 'N/A')}")
        print(f"  cognito:username: {claims.get('cognito:username', 'N/A')}")
        print(f"  iss (issuer): {claims.get('iss', 'N/A')}")
        print(f"  aud (audience): {claims.get('aud', 'N/A')}")
        print(f"  exp (expires): {claims.get('exp', 'N/A')}")
    
    # Save credentials
    credentials = {
        'user_pool_id': user_pool_id,
        'client_id': client_id,
        'username': username,
        'email': email,
        'password': password,
        'access_token': tokens['access_token'],
        'id_token': tokens['id_token'],
        'refresh_token': tokens['refresh_token'],
        'expires_in': tokens['expires_in']
    }
    
    creds_file = Path("deployment/test_credentials.json")
    with open(creds_file, 'w') as f:
        json.dump(credentials, f, indent=2)
    
    print(f"\n  ✓ Credentials saved to: {creds_file}")
    
    # Also save to root for backward compatibility
    root_creds_file = Path("test_credentials.json")
    with open(root_creds_file, 'w') as f:
        json.dump(credentials, f, indent=2)
    
    print(f"  ✓ Credentials also saved to: {root_creds_file}")
    
    print("\n" + "=" * 60)
    print("✓ TEST USER READY")
    print("=" * 60)
    print(f"\nUsername: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")
    print(f"\nCredentials saved to:")
    print(f"  - {creds_file}")
    print(f"  - {root_creds_file}")
    print("\nYou can now use these credentials to test the Agent Lambda:")
    print("  - Use the 'id_token' as the Bearer token in Authorization header")
    print("  - The token is valid for ~1 hour")
    print("\nNext steps:")
    print("  1. Run integration tests: pytest tests/integration/")
    print("  2. Test manually with the saved credentials")
    
    return True


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Create Cognito test user and obtain JWT token'
    )
    parser.add_argument(
        '--username',
        default='testuser@example.com',
        help='Username (email) for test user'
    )
    parser.add_argument(
        '--password',
        default='TestPassword123!',
        help='Password for test user'
    )
    
    args = parser.parse_args()
    
    success = setup_test_user(args.username, args.password)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
