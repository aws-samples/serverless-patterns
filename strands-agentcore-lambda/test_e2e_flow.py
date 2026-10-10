#!/usr/bin/env python3
"""
End-to-End Test for Serverless AI Agent Gateway

This script tests the complete flow:
1. Authenticate with Cognito
2. Invoke Agent Lambda with JWT
3. Agent calls Gateway to list S3 buckets
4. Verify response includes bucket list
"""

import boto3
import json
import sys

def load_jwt_token():
    """Load JWT access token from file."""
    try:
        # Try new credentials file first
        try:
            with open('test_credentials.json', 'r') as f:
                creds = json.load(f)
            return creds['access_token']
        except FileNotFoundError:
            # Fall back to old format
            with open('jwt_tokens.json', 'r') as f:
                tokens = json.load(f)
            return tokens['access_token']
    except Exception as e:
        print(f"✗ Failed to load JWT token: {e}")
        print("  Run: python3 create_cognito_user.py")
        sys.exit(1)

def load_stack_outputs():
    """Load CloudFormation stack outputs."""
    try:
        with open('infrastructure/stack_outputs.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"✗ Failed to load stack outputs: {e}")
        sys.exit(1)

def invoke_agent(lambda_client, function_name, jwt_token, prompt):
    """Invoke the Agent Lambda function."""
    payload = {
        'headers': {
            'Authorization': f'Bearer {jwt_token}'
        },
        'body': json.dumps({
            'prompt': prompt
        })
    }
    
    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        
        response_payload = json.loads(response['Payload'].read())
        return response_payload
    except Exception as e:
        print(f"✗ Failed to invoke Agent Lambda: {e}")
        return None

def main():
    print("="*60)
    print("END-TO-END TEST: Serverless AI Agent Gateway")
    print("="*60)
    
    # Load configuration
    print("\n1. Loading configuration...")
    jwt_token = load_jwt_token()
    outputs = load_stack_outputs()
    
    agent_lambda_arn = outputs['AgentLambdaArn']
    gateway_id = outputs['GatewayId']
    
    print(f"   Gateway ID: {gateway_id}")
    print(f"   Agent Lambda: {agent_lambda_arn}")
    print(f"   JWT Token: {jwt_token[:50]}...")
    
    # Initialize Lambda client
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    
    # Test 1: Simple prompt
    print("\n2. Testing Agent with prompt: 'List my S3 buckets'")
    response = invoke_agent(
        lambda_client,
        agent_lambda_arn.split(':')[-1],  # Extract function name
        jwt_token,
        'List my S3 buckets'
    )
    
    if not response:
        print("✗ Test failed: No response from Agent")
        sys.exit(1)
    
    print(f"\n3. Response received:")
    print(json.dumps(response, indent=2, default=str))
    
    # Verify response structure
    print("\n4. Verifying response...")
    
    if 'statusCode' in response:
        status_code = response['statusCode']
        print(f"   Status Code: {status_code}")
        
        if status_code == 200:
            print("   ✓ Status code is 200")
            
            # Check body
            if 'body' in response:
                try:
                    body = json.loads(response['body']) if isinstance(response['body'], str) else response['body']
                    print(f"   ✓ Response body parsed successfully")
                    
                    # Check for buckets in response
                    if 'buckets' in body or 'response' in body:
                        print("   ✓ Response contains expected data")
                        print("\n" + "="*60)
                        print("✓ END-TO-END TEST PASSED!")
                        print("="*60)
                        return 0
                    else:
                        print("   ⚠️  Response doesn't contain expected bucket data")
                        print("   Response body:", body)
                except Exception as e:
                    print(f"   ✗ Failed to parse response body: {e}")
            else:
                print("   ✗ No body in response")
        else:
            print(f"   ✗ Unexpected status code: {status_code}")
            if 'body' in response:
                print(f"   Error: {response['body']}")
    else:
        print("   ✗ No statusCode in response")
    
    print("\n" + "="*60)
    print("✗ END-TO-END TEST FAILED")
    print("="*60)
    return 1

if __name__ == '__main__':
    sys.exit(main())
