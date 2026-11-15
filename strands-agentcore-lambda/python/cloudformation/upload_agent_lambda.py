#!/usr/bin/env python3
"""
Upload Agent Lambda deployment package to AWS.
"""

import boto3
import json
import sys
from pathlib import Path
from botocore.exceptions import ClientError


def upload_agent_lambda():
    """Upload Agent Lambda deployment package."""
    print("=" * 60)
    print("UPLOADING AGENT LAMBDA")
    print("=" * 60)
    
    # Load stack outputs
    outputs_file = Path("infrastructure/stack_outputs.json")
    if not outputs_file.exists():
        print(f"✗ Stack outputs not found: {outputs_file}")
        print("  Run: python3 infrastructure/deploy_stack.py")
        return False
    
    with open(outputs_file) as f:
        outputs = json.load(f)
    
    function_arn = outputs.get("AgentLambdaArn")
    if not function_arn:
        print("✗ AgentLambdaArn not found in stack outputs")
        return False
    
    function_name = function_arn.split(":")[-1]
    print(f"Function: {function_name}")
    print(f"ARN: {function_arn}")
    
    # Check deployment package exists
    zip_file = Path("agent-lambda-deployment.zip")
    if not zip_file.exists():
        print(f"\n✗ Deployment package not found: {zip_file}")
        print("  Run: python3 package_agent_lambda.py")
        return False
    
    zip_size = zip_file.stat().st_size / (1024 * 1024)
    print(f"Package: {zip_file} ({zip_size:.2f} MB)")
    
    # Upload to Lambda
    print("\nUploading to Lambda...")
    
    try:
        lambda_client = boto3.client('lambda', region_name='us-east-1')
        
        with open(zip_file, 'rb') as f:
            zip_content = f.read()
        
        response = lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zip_content,
            Publish=True
        )
        
        print("  ✓ Upload successful")
        print(f"\n  Function ARN: {response['FunctionArn']}")
        print(f"  Version: {response['Version']}")
        print(f"  Runtime: {response['Runtime']}")
        print(f"  Handler: {response['Handler']}")
        print(f"  Code Size: {response['CodeSize'] / (1024 * 1024):.2f} MB")
        print(f"  Last Modified: {response['LastModified']}")
        
        # Wait for function to be active
        print("\nWaiting for function to be active...")
        waiter = lambda_client.get_waiter('function_updated')
        waiter.wait(FunctionName=function_name)
        print("  ✓ Function is active")
        
    except ClientError as e:
        print(f"✗ Upload failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✓ AGENT LAMBDA DEPLOYED")
    print("=" * 60)
    
    return True


if __name__ == "__main__":
    success = upload_agent_lambda()
    sys.exit(0 if success else 1)
