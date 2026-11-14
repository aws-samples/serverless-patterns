#!/usr/bin/env python3
"""
Create a test user in Cognito User Pool.
"""

import boto3
import json
import sys
from pathlib import Path
from botocore.exceptions import ClientError


def create_test_user():
    """Create a test user in Cognito."""
    print("=" * 60)
    print("CREATING COGNITO TEST USER")
    print("=" * 60)
    
    # Load stack outputs
    outputs_file = Path("infrastructure/stack_outputs.json")
    if not outputs_file.exists():
        print(f"✗ Stack outputs not found: {outputs_file}")
        return False
    
    with open(outputs_file) as f:
        outputs = json.load(f)
    
    user_pool_id = outputs.get("CognitoUserPoolId")
    if not user_pool_id:
        print("✗ CognitoUserPoolId not found in stack outputs")
        return False
    
    print(f"User Pool ID: {user_pool_id}")
    
    # User details (username must be email for this user pool)
    email = "testuser@example.com"
    username = email  # Username is the email
    password = "TestPassword123!"
    
    print(f"\nCreating user:")
    print(f"  Username/Email: {username}")
    print(f"  Password: {password}")
    
    try:
        cognito_client = boto3.client('cognito-idp', region_name='us-east-1')
        
        # Create user
        print("\nCreating user in Cognito...")
        try:
            response = cognito_client.admin_create_user(
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
                print("  ℹ User already exists, deleting and recreating...")
                cognito_client.admin_delete_user(
                    UserPoolId=user_pool_id,
                    Username=username
                )
                response = cognito_client.admin_create_user(
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
        print("Setting permanent password...")
        cognito_client.admin_set_user_password(
            UserPoolId=user_pool_id,
            Username=username,
            Password=password,
            Permanent=True
        )
        print("  ✓ Password set")
        
        # Get user pool client ID
        print("\nGetting User Pool Client ID...")
        response = cognito_client.list_user_pool_clients(
            UserPoolId=user_pool_id,
            MaxResults=10
        )
        
        if not response.get('UserPoolClients'):
            print("  ✗ No user pool clients found")
            return False
        
        client_id = response['UserPoolClients'][0]['ClientId']
        client_name = response['UserPoolClients'][0]['ClientName']
        print(f"  Client ID: {client_id}")
        print(f"  Client Name: {client_name}")
        
        # Test authentication
        print("\nTesting authentication...")
        auth_response = cognito_client.initiate_auth(
            ClientId=client_id,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        
        access_token = auth_response['AuthenticationResult']['AccessToken']
        id_token = auth_response['AuthenticationResult']['IdToken']
        
        print("  ✓ Authentication successful")
        print(f"  Access Token: {access_token[:50]}...")
        print(f"  ID Token: {id_token[:50]}...")
        
        # Save credentials
        credentials = {
            'user_pool_id': user_pool_id,
            'client_id': client_id,
            'username': username,
            'password': password,
            'email': email,
            'access_token': access_token,
            'id_token': id_token
        }
        
        creds_file = Path("test_credentials.json")
        with open(creds_file, 'w') as f:
            json.dump(credentials, f, indent=2)
        
        print(f"\n  ✓ Credentials saved to: {creds_file}")
        
    except ClientError as e:
        print(f"✗ Failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✓ TEST USER READY")
    print("=" * 60)
    print(f"\nUsername: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")
    print(f"\nCredentials saved to: test_credentials.json")
    print("\nNext step: python3 test_e2e_flow.py")
    
    return True


if __name__ == "__main__":
    success = create_test_user()
    sys.exit(0 if success else 1)
