#!/bin/bash

# Deployment script for MSK Lambda Schema Avro Python SAM
# This script helps replace placeholders in the template with actual values

set -e

echo "MSK Lambda Schema Avro Python SAM Deployment Script"
echo "=================================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Setting up..."
    ./setup_venv.sh
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Verify Python environment
echo "Using Python: $(which python)"
echo "Python version: $(python --version)"

# Check if AWS CLI is configured
if ! aws sts get-caller-identity > /dev/null 2>&1; then
    echo "Error: AWS CLI is not configured or credentials are not available"
    exit 1
fi

# Get current AWS region
AWS_REGION=$(aws configure get region)
if [ -z "$AWS_REGION" ]; then
    echo "Error: AWS region is not set. Please configure your AWS CLI with a default region."
    exit 1
fi

echo "Using AWS Region: $AWS_REGION"

# Function to get CloudFormation stack outputs
get_stack_output() {
    local stack_name=$1
    local output_key=$2
    aws cloudformation describe-stacks \
        --stack-name "$stack_name" \
        --query "Stacks[0].Outputs[?OutputKey=='$output_key'].OutputValue" \
        --output text \
        --region "$AWS_REGION" 2>/dev/null || echo ""
}

# Check if MSKAndKafkaClientEC2 CloudFormation stack exists
echo "Checking for existing MSKAndKafkaClientEC2 CloudFormation stack..."
MSK_STACK_NAME=""
for stack in $(aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --query 'StackSummaries[].StackName' --output text --region "$AWS_REGION"); do
    # Check for MSKArn or ServerlessMSKArn outputs (from MSKAndKafkaClientEC2.yaml template)
    if aws cloudformation describe-stacks --stack-name "$stack" --region "$AWS_REGION" --query 'Stacks[0].Outputs[?OutputKey==`MSKArn` || OutputKey==`ServerlessMSKArn`]' --output text 2>/dev/null | grep -q .; then
        MSK_STACK_NAME=$stack
        break
    fi
done

if [ -n "$MSK_STACK_NAME" ]; then
    echo "Found MSKAndKafkaClientEC2 stack: $MSK_STACK_NAME"
    
    # Get values from CloudFormation outputs (based on MSKAndKafkaClientEC2.yaml template)
    MSK_ARN=$(get_stack_output "$MSK_STACK_NAME" "MSKArn")
    SERVERLESS_MSK_ARN=$(get_stack_output "$MSK_STACK_NAME" "ServerlessMSKArn")
    KAFKA_TOPIC=$(get_stack_output "$MSK_STACK_NAME" "KafkaTopicForLambda")
    VPC_ID=$(get_stack_output "$MSK_STACK_NAME" "VPCId")
    SUBNET_IDS=$(get_stack_output "$MSK_STACK_NAME" "PrivateSubnetMSKOne"),$(get_stack_output "$MSK_STACK_NAME" "PrivateSubnetMSKTwo"),$(get_stack_output "$MSK_STACK_NAME" "PrivateSubnetMSKThree")
    SECURITY_GROUP_ID=$(get_stack_output "$MSK_STACK_NAME" "SecurityGroupId")
    CONTACT_SCHEMA_ARN=$(get_stack_output "$MSK_STACK_NAME" "ContactSchemaArn")
    
    # Get Glue Schema Registry name from stack parameters (since it's not in outputs)
    GLUE_SCHEMA_REGISTRY_NAME=$(aws cloudformation describe-stacks \
        --stack-name "$MSK_STACK_NAME" \
        --query "Stacks[0].Parameters[?ParameterKey=='GlueSchemaRegistryForMSKName'].ParameterValue" \
        --output text \
        --region "$AWS_REGION" 2>/dev/null || echo "GlueSchemaRegistryForMSK")
    
    # Determine which MSK ARN to use (Provisioned or Serverless)
    if [ -n "$MSK_ARN" ]; then
        CLUSTER_ARN="$MSK_ARN"
        CLUSTER_TYPE="Provisioned"
    elif [ -n "$SERVERLESS_MSK_ARN" ]; then
        CLUSTER_ARN="$SERVERLESS_MSK_ARN"
        CLUSTER_TYPE="Serverless"
    else
        echo "Error: No MSK cluster ARN found in stack outputs"
        exit 1
    fi
    
    # Extract cluster name and ID from ARN
    CLUSTER_NAME=$(echo "$CLUSTER_ARN" | awk -F'/' '{print $2}')
    CLUSTER_ID=$(echo "$CLUSTER_ARN" | awk -F'/' '{print $3}')
    
    echo "Retrieved parameters from CloudFormation stack:"
    echo "  Cluster Type: $CLUSTER_TYPE"
    echo "  Cluster ARN: $CLUSTER_ARN"
    echo "  Cluster Name: $CLUSTER_NAME"
    echo "  Cluster ID: $CLUSTER_ID"
    echo "  Kafka Topic: $KAFKA_TOPIC"
    echo "  VPC ID: $VPC_ID"
    echo "  Subnet IDs: $SUBNET_IDS"
    echo "  Security Group ID: $SECURITY_GROUP_ID"
    echo "  Contact Schema ARN: $CONTACT_SCHEMA_ARN"
    echo "  Glue Schema Registry Name: $GLUE_SCHEMA_REGISTRY_NAME"
    
    # Create template.yaml from template_original.yaml with replacements
    echo "Creating template.yaml with actual values..."
    cp template_original.yaml template.yaml
    
    # Replace placeholders with actual values from CloudFormation outputs
    sed -i.bak "s/CLUSTER_NAME/$CLUSTER_NAME/g" template.yaml
    sed -i.bak "s/CLUSTER_ID/$CLUSTER_ID/g" template.yaml
    sed -i.bak "s/KAFKA_TOPIC/$KAFKA_TOPIC/g" template.yaml
    sed -i.bak "s/VPC_ID/$VPC_ID/g" template.yaml
    sed -i.bak "s/SUBNET_IDS/$SUBNET_IDS/g" template.yaml
    sed -i.bak "s/LAMBDA_SECURITY_GROUP_ID/$SECURITY_GROUP_ID/g" template.yaml
    sed -i.bak "s/GLUE_SCHEMA_REGISTRY_NAME/$GLUE_SCHEMA_REGISTRY_NAME/g" template.yaml
    sed -i.bak "s/AVRO_SCHEMA/ContactSchema/g" template.yaml
    
    # Clean up backup file
    rm template.yaml.bak
    
else
    echo "No MSKAndKafkaClientEC2 CloudFormation stack found."
    echo "Please deploy the MSKAndKafkaClientEC2.yaml template first, or provide parameters manually."
    echo "You can manually edit template.yaml or provide parameters during deployment."
    exit 1
fi

# Verify dependencies are installed
echo "Verifying Python dependencies..."
python -c "import boto3, kafka, avro; print('All dependencies verified successfully')" || {
    echo "Error: Missing dependencies. Installing..."
    pip install -r requirements.txt
}

# Build the application
echo "Building SAM application..."
sam build

# Deploy the application
echo "Deploying SAM application..."
# Deploy with parameters from MSKAndKafkaClientEC2 CloudFormation stack
sam deploy \
    --resolve-s3 \
    --capabilities CAPABILITY_IAM \
    --no-confirm-changeset \
    --no-disable-rollback \
    --region "$AWS_REGION" \
    --stack-name msk-lambda-schema-avro-python-sam \
    --parameter-overrides \
        MSKClusterName="$CLUSTER_NAME" \
        MSKClusterId="$CLUSTER_ID" \
        MSKTopic="$KAFKA_TOPIC" \
        ContactSchemaName="ContactSchema" \
        VpcId="$VPC_ID" \
        SubnetIds="$SUBNET_IDS" \
        SecurityGroupIds="$SECURITY_GROUP_ID"

echo "Deployment completed successfully!"
echo ""
echo "To test the application:"
echo "1. Make sure virtual environment is activated: source venv/bin/activate"
echo "2. Invoke the producer function:"
echo "   sam remote invoke LambdaMSKProducerPythonFunction --region $AWS_REGION --stack-name msk-lambda-schema-avro-python-sam"
echo ""
echo "3. Check consumer function logs:"
echo "   sam logs --name LambdaMSKConsumerPythonFunction --stack-name msk-lambda-schema-avro-python-sam --region $AWS_REGION"
