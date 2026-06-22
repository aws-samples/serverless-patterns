#!/usr/bin/env python3
"""
CloudFormation Stack Deployment Script

This script deploys the Serverless AI Agent Gateway CloudFormation stack
and captures all outputs for validation.
"""

import boto3
import json
import time
import sys
from typing import Dict, Optional
from botocore.exceptions import ClientError


class StackDeployer:
    """Handles CloudFormation stack deployment and validation."""
    
    def __init__(self, stack_name: str, template_path: str, region: str = 'us-east-1'):
        """
        Initialize the stack deployer.
        
        Args:
            stack_name: Name of the CloudFormation stack
            template_path: Path to the CloudFormation template file
            region: AWS region for deployment
        """
        self.stack_name = stack_name
        self.template_path = template_path
        self.region = region
        self.cfn_client = boto3.client('cloudformation', region_name=region)
        
    def read_template(self) -> str:
        """Read the CloudFormation template file."""
        try:
            with open(self.template_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: Template file not found: {self.template_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading template: {e}")
            sys.exit(1)
    
    def validate_template(self, template_body: str) -> bool:
        """
        Validate the CloudFormation template.
        
        Args:
            template_body: CloudFormation template content
            
        Returns:
            True if valid, False otherwise
        """
        try:
            print("Validating CloudFormation template...")
            response = self.cfn_client.validate_template(TemplateBody=template_body)
            print("✓ Template validation successful")
            print(f"  Description: {response.get('Description', 'N/A')}")
            print(f"  Parameters: {len(response.get('Parameters', []))}")
            return True
        except ClientError as e:
            print(f"✗ Template validation failed: {e}")
            return False
    
    def stack_exists(self) -> bool:
        """Check if the stack already exists."""
        try:
            self.cfn_client.describe_stacks(StackName=self.stack_name)
            return True
        except ClientError as e:
            if 'does not exist' in str(e):
                return False
            raise
    
    def deploy_stack(self, template_body: str, parameters: Dict[str, str]) -> bool:
        """
        Deploy or update the CloudFormation stack.
        
        Args:
            template_body: CloudFormation template content
            parameters: Stack parameters
            
        Returns:
            True if deployment successful, False otherwise
        """
        try:
            # Convert parameters to CloudFormation format
            cfn_parameters = [
                {'ParameterKey': k, 'ParameterValue': v}
                for k, v in parameters.items()
            ]
            
            # Check if stack exists
            exists = self.stack_exists()
            
            if exists:
                print(f"Updating existing stack: {self.stack_name}")
                operation = 'update'
                try:
                    self.cfn_client.update_stack(
                        StackName=self.stack_name,
                        TemplateBody=template_body,
                        Parameters=cfn_parameters,
                        Capabilities=['CAPABILITY_NAMED_IAM']
                    )
                except ClientError as e:
                    if 'No updates are to be performed' in str(e):
                        print("✓ Stack is already up to date")
                        return True
                    raise
            else:
                print(f"Creating new stack: {self.stack_name}")
                operation = 'create'
                self.cfn_client.create_stack(
                    StackName=self.stack_name,
                    TemplateBody=template_body,
                    Parameters=cfn_parameters,
                    Capabilities=['CAPABILITY_NAMED_IAM'],
                    Tags=[
                        {'Key': 'Project', 'Value': 'ServerlessAIAgentGateway'},
                        {'Key': 'ManagedBy', 'Value': 'CloudFormation'}
                    ]
                )
            
            # Wait for stack operation to complete
            return self.wait_for_stack(operation)
            
        except ClientError as e:
            print(f"✗ Stack deployment failed: {e}")
            return False
    
    def wait_for_stack(self, operation: str) -> bool:
        """
        Wait for stack operation to complete.
        
        Args:
            operation: 'create' or 'update'
            
        Returns:
            True if successful, False otherwise
        """
        if operation == 'create':
            waiter = self.cfn_client.get_waiter('stack_create_complete')
            success_status = 'CREATE_COMPLETE'
            failure_statuses = ['CREATE_FAILED', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED']
        else:
            waiter = self.cfn_client.get_waiter('stack_update_complete')
            success_status = 'UPDATE_COMPLETE'
            failure_statuses = ['UPDATE_FAILED', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_FAILED']
        
        print(f"Waiting for stack {operation} to complete...")
        print("This may take several minutes...")
        
        try:
            waiter.wait(
                StackName=self.stack_name,
                WaiterConfig={'Delay': 10, 'MaxAttempts': 120}
            )
            print(f"✓ Stack {operation} completed successfully")
            return True
        except Exception as e:
            print(f"✗ Stack {operation} failed or timed out")
            self.print_stack_events()
            return False
    
    def print_stack_events(self, limit: int = 10):
        """Print recent stack events for debugging."""
        try:
            response = self.cfn_client.describe_stack_events(StackName=self.stack_name)
            events = response.get('StackEvents', [])[:limit]
            
            print("\nRecent stack events:")
            for event in events:
                status = event.get('ResourceStatus', 'UNKNOWN')
                resource = event.get('LogicalResourceId', 'UNKNOWN')
                reason = event.get('ResourceStatusReason', '')
                timestamp = event.get('Timestamp', '')
                
                print(f"  [{timestamp}] {resource}: {status}")
                if reason:
                    print(f"    Reason: {reason}")
        except Exception as e:
            print(f"Could not retrieve stack events: {e}")
    
    def get_stack_outputs(self) -> Optional[Dict[str, str]]:
        """
        Get stack outputs after deployment.
        
        Returns:
            Dictionary of output key-value pairs, or None if failed
        """
        try:
            response = self.cfn_client.describe_stacks(StackName=self.stack_name)
            stacks = response.get('Stacks', [])
            
            if not stacks:
                print("✗ Stack not found")
                return None
            
            stack = stacks[0]
            outputs = stack.get('Outputs', [])
            
            if not outputs:
                print("✗ No outputs found in stack")
                return None
            
            output_dict = {
                output['OutputKey']: output['OutputValue']
                for output in outputs
            }
            
            return output_dict
            
        except ClientError as e:
            print(f"✗ Failed to get stack outputs: {e}")
            return None
    
    def print_outputs(self, outputs: Dict[str, str]):
        """Print stack outputs in a formatted way."""
        print("\n" + "="*60)
        print("STACK OUTPUTS")
        print("="*60)
        
        for key, value in outputs.items():
            print(f"{key:30s}: {value}")
        
        print("="*60 + "\n")
    
    def save_outputs(self, outputs: Dict[str, str], output_file: str = 'stack_outputs.json'):
        """Save stack outputs to a JSON file."""
        try:
            with open(output_file, 'w') as f:
                json.dump(outputs, f, indent=2)
            print(f"✓ Outputs saved to: {output_file}")
        except Exception as e:
            print(f"✗ Failed to save outputs: {e}")


def main():
    """Main deployment function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Deploy Serverless AI Agent Gateway CloudFormation stack')
    parser.add_argument('--stack-name', default='serverless-ai-agent-gateway-test',
                       help='CloudFormation stack name')
    parser.add_argument('--template', default='infrastructure/cloudformation-template.yaml',
                       help='Path to CloudFormation template')
    parser.add_argument('--environment', default='test',
                       choices=['dev', 'test', 'prod'],
                       help='Environment name')
    parser.add_argument('--region', default='us-east-1',
                       help='AWS region')
    parser.add_argument('--bedrock-model-id', default='us.anthropic.claude-sonnet-4-6',
                       help='Bedrock cross-region inference profile model ID')
    parser.add_argument('--bedrock-base-model-id', default='anthropic.claude-sonnet-4-6',
                       help='Bedrock base foundation model ID (without cross-region prefix)')
    parser.add_argument('--output-file', default='infrastructure/stack_outputs.json',
                       help='File to save stack outputs')
    
    args = parser.parse_args()
    
    print("="*60)
    print("SERVERLESS AI AGENT GATEWAY - STACK DEPLOYMENT")
    print("="*60)
    print(f"Stack Name:   {args.stack_name}")
    print(f"Template:     {args.template}")
    print(f"Environment:  {args.environment}")
    print(f"Region:       {args.region}")
    print("="*60 + "\n")
    
    # Initialize deployer
    deployer = StackDeployer(args.stack_name, args.template, args.region)
    
    # Read and validate template
    template_body = deployer.read_template()
    if not deployer.validate_template(template_body):
        print("\n✗ Deployment aborted due to template validation failure")
        sys.exit(1)
    
    # Prepare parameters
    parameters = {
        'EnvironmentName': args.environment,
        'BedrockModelId': args.bedrock_model_id,
        'BedrockBaseModelId': args.bedrock_base_model_id,
    }
    
    # Deploy stack
    print()
    if not deployer.deploy_stack(template_body, parameters):
        print("\n✗ Deployment failed")
        sys.exit(1)
    
    # Get and display outputs
    print()
    outputs = deployer.get_stack_outputs()
    if outputs:
        deployer.print_outputs(outputs)
        deployer.save_outputs(outputs, args.output_file)
        
        print("\n✓ Deployment completed successfully!")
        print(f"\nNext steps:")
        print(f"  1. Review outputs in: {args.output_file}")
        print(f"  2. Package and upload Lambda code: python3 deploy_all.py")
        print(f"  3. Create test user: python3 create_cognito_user.py")
        print(f"  4. Run end-to-end test: python3 test_e2e_flow.py")
        print(f"  5. (Optional) Validate deployment: python3 infrastructure/validate_deployment.py")
    else:
        print("\n✗ Failed to retrieve stack outputs")
        sys.exit(1)


if __name__ == '__main__':
    main()
