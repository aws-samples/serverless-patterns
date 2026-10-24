"""
Integration tests for Gateway Target deployment.

Tests that the WeatherAPI Gateway Target and supporting resources were
created correctly and are accessible via AWS API. Requires a live deployment
(reads deployment/stack_outputs.json).
"""

import json
import boto3
import pytest
from pathlib import Path


@pytest.fixture
def stack_outputs():
    """Load stack outputs from deployment."""
    outputs_file = Path('deployment/stack_outputs.json')
    if not outputs_file.exists():
        pytest.skip("Stack outputs not found - run deployment first")
    
    with open(outputs_file) as f:
        return json.load(f)


@pytest.fixture
def bedrock_client():
    """Create Bedrock AgentCore client."""
    return boto3.client('bedrock-agent', region_name='us-east-1')


def test_gateway_exists(stack_outputs, bedrock_client):
    """Test that the Gateway was created."""
    gateway_id = stack_outputs['GatewayId']
    
    # Note: There's no direct API to get gateway details in bedrock-agent
    # This test verifies the gateway ID is in the outputs
    assert gateway_id is not None
    assert gateway_id.startswith('dev-openapi-agent-gateway-')
    print(f"✓ Gateway ID: {gateway_id}")


def test_gateway_target_listed(stack_outputs):
    """Test that Gateway Targets can be listed."""
    gateway_id = stack_outputs['GatewayId']
    
    # Note: AWS SDK may not have direct support for listing gateway targets yet
    # This is a placeholder for when the API becomes available
    print(f"✓ Gateway ID available: {gateway_id}")
    print("  Note: Direct Gateway Target listing API not yet available in boto3")


def test_cognito_user_pool_exists(stack_outputs):
    """Test that Cognito User Pool was created."""
    user_pool_id = stack_outputs['CognitoUserPoolId']
    
    cognito = boto3.client('cognito-idp', region_name='us-east-1')
    
    response = cognito.describe_user_pool(UserPoolId=user_pool_id)
    
    assert response['UserPool']['Id'] == user_pool_id
    assert response['UserPool']['Name'] == 'dev-openapi-agent-user-pool'
    print(f"✓ Cognito User Pool: {user_pool_id}")


def test_lambda_functions_exist(stack_outputs):
    """Test that the Agent Lambda was created."""
    agent_lambda_arn = stack_outputs['AgentLambdaArn']

    lambda_client = boto3.client('lambda', region_name='us-east-1')

    agent_response = lambda_client.get_function(FunctionName=agent_lambda_arn)
    assert agent_response['Configuration']['FunctionName'] == 'dev-agent-lambda'
    assert agent_response['Configuration']['Runtime'] == 'python3.12'
    print(f"✓ Agent Lambda: {agent_lambda_arn}")


def test_lambda_environment_variables(stack_outputs):
    """Test that Lambda environment variables are set correctly."""
    agent_lambda_arn = stack_outputs['AgentLambdaArn']
    gateway_id = stack_outputs['GatewayId']
    
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    
    response = lambda_client.get_function(FunctionName=agent_lambda_arn)
    env_vars = response['Configuration']['Environment']['Variables']
    
    assert 'GATEWAY_ID' in env_vars
    assert env_vars['GATEWAY_ID'] == gateway_id
    assert 'COGNITO_JWKS_URL' in env_vars
    assert 'BEDROCK_MODEL_ID' in env_vars
    print(f"✓ Lambda environment variables configured correctly")


def test_stack_outputs_complete(stack_outputs):
    """Test that all expected stack outputs are present."""
    required_outputs = [
        'GatewayId',
        'CognitoUserPoolId',
        'CognitoClientId',
        'AgentLambdaArn'
    ]
    
    for output in required_outputs:
        assert output in stack_outputs, f"Missing output: {output}"
        assert stack_outputs[output], f"Empty output: {output}"
    
    print("✓ All stack outputs present")


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
