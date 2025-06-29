#!/bin/bash

# Cleanup script for MSK Lambda Schema Avro Python SAM
# This script helps clean up the deployed resources

set -e

echo "MSK Lambda Schema Avro Python SAM Cleanup Script"
echo "=============================================="

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Get current AWS region
AWS_REGION=$(aws configure get region)
if [ -z "$AWS_REGION" ]; then
    echo "Error: AWS region is not set. Please configure your AWS CLI with a default region."
    exit 1
fi

echo "Using AWS Region: $AWS_REGION"

# Delete the Lambda stack
echo "Deleting Lambda functions stack..."
sam delete --stack-name msk-lambda-schema-avro-python-sam --region "$AWS_REGION" --no-prompts

echo "Lambda functions stack deleted successfully!"
echo ""
echo "Note: If you also want to delete the MSK cluster and EC2 instance,"
echo "you need to delete the MSK CloudFormation stack manually from the AWS Console."
echo ""
echo "To find the MSK stack:"
echo "1. Go to CloudFormation console"
echo "2. Look for a stack that has MSK-related outputs"
echo "3. Delete that stack (this may take several minutes)"
echo ""
echo "To clean up the local virtual environment:"
echo "1. Deactivate: deactivate"
echo "2. Remove: rm -rf venv/"
