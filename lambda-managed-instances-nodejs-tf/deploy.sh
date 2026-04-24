#!/bin/bash

# Deployment script for Lambda Managed Instances Terraform pattern
# Usage: ./deploy.sh [aws-region]

set -e

# Configuration
AWS_REGION=${1:-us-west-2}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Deploying Lambda Managed Instances Pattern (Terraform) ===${NC}"
echo -e "${YELLOW}Region: ${AWS_REGION}${NC}"
echo ""

# Step 1: Install Lambda dependencies
echo -e "${BLUE}Step 1: Installing Lambda function dependencies${NC}"
cd lambda
if [ ! -f "package-lock.json" ]; then
    npm install
else
    echo "Dependencies already installed"
fi
cd ..

# Step 2: Initialize Terraform
echo -e "${BLUE}Step 2: Initializing Terraform${NC}"
terraform init

# Step 3: Plan deployment
echo -e "${BLUE}Step 3: Planning Terraform deployment${NC}"
terraform plan -var="aws_region=${AWS_REGION}"

# Step 4: Apply infrastructure
echo -e "${BLUE}Step 4: Applying Terraform configuration${NC}"
terraform apply -var="aws_region=${AWS_REGION}" -auto-approve

echo -e "${GREEN}✓ Lambda function automatically associated with capacity provider via Terraform${NC}"

echo ""
echo -e "${GREEN}=== Deployment completed successfully! ===${NC}"
echo ""
echo -e "${YELLOW}Outputs:${NC}"
terraform output

echo ""
echo -e "${YELLOW}Next steps:${NC}"
CAPACITY_PROVIDER_NAME=$(terraform output -raw capacity_provider_name)
FUNCTION_NAME=$(terraform output -raw function_name)
echo "1. Test the function: ./test-lambda.sh"
echo "2. View capacity provider: aws lambda get-capacity-provider --capacity-provider-name $CAPACITY_PROVIDER_NAME --region $AWS_REGION"
echo "3. View function details: aws lambda get-function --function-name $FUNCTION_NAME --region $AWS_REGION"