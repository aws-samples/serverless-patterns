#!/bin/bash

# Cleanup script for Lambda Managed Instances Terraform pattern
# Usage: ./cleanup.sh [aws-region]

set -e

# Configuration
AWS_REGION=${1:-us-west-2}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Cleaning up Lambda Managed Instances Pattern (Terraform) ===${NC}"
echo -e "${YELLOW}Region: ${AWS_REGION}${NC}"
echo ""

# Confirm destruction
echo -e "${YELLOW}This will destroy all resources created by this pattern.${NC}"
read -p "Are you sure you want to continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Cleanup cancelled.${NC}"
    exit 0
fi

# Destroy infrastructure
echo -e "${BLUE}Destroying Terraform infrastructure...${NC}"
terraform destroy -var="aws_region=${AWS_REGION}" -auto-approve

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Infrastructure successfully destroyed${NC}"
else
    echo -e "${RED}✗ Failed to destroy infrastructure${NC}"
    exit 1
fi

# Clean up local files
echo -e "${BLUE}Cleaning up local files...${NC}"
rm -f lambda-function.zip
rm -f response.json
rm -f custom-response.json
rm -f output.json

# Clean up Terraform temporary and state files
echo -e "${BLUE}Cleaning up Terraform temporary and state files...${NC}"
rm -f terraform.tfstate
rm -f terraform.tfstate.backup
rm -f .terraform.tfstate.lock.info
rm -rf .terraform/
rm -f .terraform.lock.hcl
rm -f terraform.tfplan
rm -f terraform.log
rm -f crash.log

echo ""
echo -e "${GREEN}=== Cleanup completed successfully! ===${NC}"