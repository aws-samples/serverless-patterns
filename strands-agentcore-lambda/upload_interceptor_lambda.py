#!/usr/bin/env python3
"""Upload Interceptor Lambda deployment package to AWS."""

import boto3
import json
import sys
from pathlib import Path


def upload_interceptor_lambda():
    """Upload Interceptor Lambda code to AWS."""
    print("="*60)
    print("Uploading Interceptor Lambda")
    print("="*60)
    
    # Load stack outputs
    outputs_file = Path("infrastructure/stack_outputs.json")
    if not outputs_file.exists():
        print(f"✗ Stack outputs not found: {outputs_file}")
        print("  Run: python3 infrastructure/deploy_stack.py")
        return False
    
    with open(outputs_file, 'r') as f:
        outputs = json.load(f)
    
    interceptor_lambda_arn = outputs.get('InterceptorLambdaArn')
    if not interceptor_lambda_arn:
        print("✗ InterceptorLambdaArn not found in stack outputs")
        print("  The Interceptor Lambda may not be deployed yet")
        return False
    
    # Extract function name from ARN
    function_name = interceptor_lambda_arn.split(':')[-1]
    
    # Check deployment package exists
    zip_path = Path("interceptor-lambda-deployment.zip")
    if not zip_path.exists():
        print(f"✗ Deployment package not found: {zip_path}")
        print("  Run: python3 package_interceptor_lambda.py")
        return False
    
    # Get package size
    size_mb = zip_path.stat().st_size / (1024 * 1024)
    
    print(f"\n1. Configuration:")
    print(f"   Function: {function_name}")
    print(f"   Package: {zip_path} ({size_mb:.2f} MB)")
    
    # Initialize Lambda client
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    
    # Upload code
    print(f"\n2. Uploading code to Lambda...")
    try:
        with open(zip_path, 'rb') as f:
            zip_content = f.read()
        
        response = lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zip_content,
            Publish=True
        )
        
        version = response['Version']
        code_size = response['CodeSize'] / (1024 * 1024)
        
        print(f"   ✓ Code uploaded successfully")
        print(f"   Version: {version}")
        print(f"   Code size: {code_size:.2f} MB")
        
    except Exception as e:
        print(f"   ✗ Upload failed: {e}")
        return False
    
    print("\n" + "="*60)
    print("✓ Interceptor Lambda uploaded successfully!")
    print("="*60)
    
    return True


if __name__ == '__main__':
    success = upload_interceptor_lambda()
    sys.exit(0 if success else 1)
