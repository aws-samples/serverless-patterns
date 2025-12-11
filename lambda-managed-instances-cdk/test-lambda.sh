#!/bin/bash

# Test script for Hello World Lambda function on Managed Instances
# Usage: ./test-lambda.sh [profile]

set -e

# Configuration
FUNCTION_NAME="hello-world-managed-instances"
PROFILE=${1:-default}
EVENT_FILE="events/hello-world.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Testing Hello World Lambda Function on Managed Instances ===${NC}"
echo -e "${YELLOW}Function: ${FUNCTION_NAME}${NC}"
echo -e "${YELLOW}Profile: ${PROFILE}${NC}"
echo ""

# Check if event file exists
if [ ! -f "$EVENT_FILE" ]; then
    echo -e "${RED}Error: Event file $EVENT_FILE not found${NC}"
    exit 1
fi

# Test 1: Basic invocation with sample event
echo -e "${BLUE}Test 1: Basic invocation with sample event${NC}"
echo "Invoking function with event from $EVENT_FILE..."

aws lambda invoke \
    --function-name "$FUNCTION_NAME" \
    --payload file://"$EVENT_FILE" \
    --cli-binary-format raw-in-base64-out \
    --profile "$PROFILE" \
    response.json

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Function invoked successfully${NC}"
    echo -e "${YELLOW}Response:${NC}"
    cat response.json | jq '.'
    echo ""
else
    echo -e "${RED}✗ Function invocation failed${NC}"
    exit 1
fi

# Test 2: View recent CloudWatch logs
echo -e "${BLUE}Test 2: Recent CloudWatch logs${NC}"
echo "Fetching recent logs from CloudWatch..."

LOG_GROUP="/aws/lambda/$FUNCTION_NAME"
START_TIME=$(date -v-5M +%s)000

aws logs filter-log-events \
    --log-group-name "$LOG_GROUP" \
    --start-time "$START_TIME" \
    --profile "$PROFILE" \
    --query 'events[*].[timestamp,message]' \
    --output table

# Test 3: View Lambda Managed Instances (EC2 instances)
echo -e "${BLUE}Test 3: Lambda Managed Instances (EC2 instances)${NC}"
echo "Checking capacity provider and associated EC2 instances..."

echo -e "${YELLOW}Capacity Provider Details:${NC}"
aws lambda get-capacity-provider --capacity-provider-name lambda-capacity-provider --query 'CapacityProvider.[CapacityProviderArn,State,InstanceRequirements.Architectures[0],CapacityProviderScalingConfig.ScalingMode]' --output table --profile "$PROFILE"

echo -e "${YELLOW}EC2 Instances provisioned for Lambda Managed Instances:${NC}"
# Get subnet IDs from capacity provider
SUBNET_IDS=$(aws lambda get-capacity-provider --capacity-provider-name lambda-capacity-provider --query 'CapacityProvider.VpcConfig.SubnetIds' --output text --profile "$PROFILE" | tr '\t' ',')
SECURITY_GROUP_ID=$(aws lambda get-capacity-provider --capacity-provider-name lambda-capacity-provider --query 'CapacityProvider.VpcConfig.SecurityGroupIds[0]' --output text --profile "$PROFILE")

# List EC2 instances tagged with this capacity provider
CAPACITY_PROVIDER_ARN="arn:aws:lambda:us-west-2:220537809147:capacity-provider:lambda-capacity-provider"
aws ec2 describe-instances \
    --filters "Name=tag:aws:lambda:capacity-provider,Values=$CAPACITY_PROVIDER_ARN" \
    --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,LaunchTime,SubnetId,PrivateIpAddress]' \
    --output table \
    --profile "$PROFILE"

# Also show instance count
INSTANCE_COUNT=$(aws ec2 describe-instances \
    --filters "Name=tag:aws:lambda:capacity-provider,Values=$CAPACITY_PROVIDER_ARN" "Name=instance-state-name,Values=running" \
    --query 'length(Reservations[*].Instances[*])' \
    --output text \
    --profile "$PROFILE")

echo "Currently running instances: $INSTANCE_COUNT"

echo ""
echo -e "${GREEN}=== Testing completed successfully! ===${NC}"
echo ""
echo -e "${YELLOW}Useful commands for further testing:${NC}"
echo "1. View function details:"
echo "   aws lambda get-function --function-name $FUNCTION_NAME --profile $PROFILE"
echo ""
echo "2. View function configuration:"
echo "   aws lambda get-function-configuration --function-name $FUNCTION_NAME --profile $PROFILE"
echo ""
echo "3. View CloudWatch logs:"
echo "   aws logs filter-log-events --log-group-name $LOG_GROUP --start-time \$(date -d '10 minutes ago' +%s)000 --profile $PROFILE"
echo ""
echo "4. Custom invocation:"
echo "   echo '{\"name\":\"Your Name\"}' | aws lambda invoke --function-name $FUNCTION_NAME --payload file:///dev/stdin --cli-binary-format raw-in-base64-out --profile $PROFILE output.json"
echo ""
echo "5. View capacity provider details:"
echo "   aws lambda get-capacity-provider --capacity-provider-name lambda-capacity-provider --profile $PROFILE"
echo ""
echo "6. List EC2 instances for managed instances:"
echo "   aws ec2 describe-instances --filters \"Name=tag:aws:lambda:capacity-provider,Values=arn:aws:lambda:*:capacity-provider:lambda-capacity-provider\" --profile $PROFILE"

# Cleanup temporary files
rm -f response.json