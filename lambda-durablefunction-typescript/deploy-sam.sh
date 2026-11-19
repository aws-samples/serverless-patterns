#!/bin/bash

# SAM-based deployment script for Fraud Detection Durable Function
set -e

# Configuration variables (matching original deploy.sh)
STACK_NAME="fraud-detection-durable-function"
FUNCTION_NAME="fn-Fraud-Detection"
LAYER_NAME="lr-FraudDetection"
ROLE_NAME="durable-function-execution-role"
AGENT_RUNTIME_NAME="fraud_risk_scorer"
AGENT_ROLE_NAME="bedrock-agentcore-runtime-fraud-role"
ECR_REPO_NAME="fraud-risk-scorer"
LAMBDA_REGION="us-east-2"
AGENT_REGION="us-east-2"

echo "🚀 Deploying Fraud Detection Durable Function using SAM"
echo "======================================================"
echo ""

# Get AWS Account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo "📋 Account ID: $ACCOUNT_ID"
echo "📋 Lambda Region: $LAMBDA_REGION"
echo "📋 Agent Region: $AGENT_REGION"
echo ""

# Check prerequisites
echo "🔍 Checking prerequisites..."

# Check if SAM CLI is installed
if ! command -v sam &> /dev/null; then
    echo "❌ SAM CLI is not installed. Please install it first:"
    echo "   https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker is not running. Please start Docker Desktop."
    exit 1
fi


echo "✅ Prerequisites checked"
echo ""

# Build and push Docker image for agent
echo "🐳 Building and pushing agent Docker image..."
cd FraudDetection-Agent

# Get ECR URI
ECR_URI="$ACCOUNT_ID.dkr.ecr.$AGENT_REGION.amazonaws.com/$ECR_REPO_NAME"

# Create ECR repository if it doesn't exist (SAM will also create it, but we need it for docker push)
echo "📦 Ensuring ECR repository exists..."
if ! aws ecr describe-repositories --repository-names $ECR_REPO_NAME --region $AGENT_REGION >/dev/null 2>&1; then
    echo "📝 Creating ECR repository: $ECR_REPO_NAME"
    aws ecr create-repository --repository-name $ECR_REPO_NAME --region $AGENT_REGION >/dev/null
fi

# Login to ECR
echo "🔐 Logging in to ECR..."
aws ecr get-login-password --region $AGENT_REGION | docker login --username AWS --password-stdin $ECR_URI

# Build and push image
echo "🏗️ Building and pushing Docker image..."
docker buildx create --use --name sam-builder 2>/dev/null || docker buildx use sam-builder
docker buildx build --platform linux/arm64 -t $ECR_URI:latest --push .

echo "✅ Docker image pushed to ECR"
cd ..

# Build Lambda function and layer
echo "📦 Building Lambda function and layer..."
cd FraudDetection-Lambda

# Clean previous builds
echo "🧹 Cleaning directory..."
rm -rf node_modules dist function.zip layer.zip || true

# Install dependencies
echo "📥 Installing dependencies..."
npm install --silent

# Build TypeScript
echo "🔨 Compiling TypeScript..."
tsc

# Create function package (without node_modules)
echo "📦 Creating function package..."
cd dist
zip -qr ../function.zip .
cd ..
zip -r function.zip package.json

# Create layer package
echo "📦 Creating layer package..."
mkdir -p layer/nodejs
cp -r node_modules layer/nodejs/
cd layer
zip -qr ../layer.zip .
cd ..

# Ensure S3 bucket exists before upload
BUCKET_NAME="durable-functions-$ACCOUNT_ID"
echo "📦 Ensuring S3 bucket exists: $BUCKET_NAME"

# Check if bucket exists, create if not
if ! aws s3api head-bucket --bucket $BUCKET_NAME --region $LAMBDA_REGION 2>/dev/null; then
    echo "📝 Creating S3 bucket: $BUCKET_NAME"
    if [ "$LAMBDA_REGION" = "us-east-1" ]; then
        aws s3api create-bucket --bucket $BUCKET_NAME --region $LAMBDA_REGION
    else
        aws s3api create-bucket --bucket $BUCKET_NAME --region $LAMBDA_REGION \
            --create-bucket-configuration LocationConstraint=$LAMBDA_REGION
    fi
    
    # Enable versioning
    aws s3api put-bucket-versioning --bucket $BUCKET_NAME \
        --versioning-configuration Status=Enabled --region $LAMBDA_REGION
    
    # Enable encryption
    aws s3api put-bucket-encryption --bucket $BUCKET_NAME --region $LAMBDA_REGION \
        --server-side-encryption-configuration '{
            "Rules": [{
                "ApplyServerSideEncryptionByDefault": {
                    "SSEAlgorithm": "AES256"
                }
            }]
        }'
    
    # Block public access
    aws s3api put-public-access-block --bucket $BUCKET_NAME --region $LAMBDA_REGION \
        --public-access-block-configuration \
        BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
fi

# Upload to S3
echo "⬆️  Uploading packages to S3..."
aws s3 cp function.zip s3://$BUCKET_NAME/functions/$FUNCTION_NAME.zip --region $LAMBDA_REGION
aws s3 cp layer.zip s3://$BUCKET_NAME/layers/$LAYER_NAME.zip --region $LAMBDA_REGION

# Clean up
echo "🧹 Cleaning up build artifacts..."
rm -rf node_modules dist layer function.zip layer.zip

cd ..

# Deploy SAM application
echo "🚀 Deploying SAM stack..."
sam deploy \
    --stack-name $STACK_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $LAMBDA_REGION \
    --parameter-overrides \
        FunctionName=$FUNCTION_NAME \
        LayerName=$LAYER_NAME \
        RoleName=$ROLE_NAME \
        AgentRuntimeName=$AGENT_RUNTIME_NAME \
        AgentRoleName=$AGENT_ROLE_NAME \
        ECRRepoName=$ECR_REPO_NAME \
        LambdaRegion=$LAMBDA_REGION \
        AgentRegion=$AGENT_REGION \
    --no-fail-on-empty-changeset

echo ""
echo "⏳ Waiting for stack deployment to complete..."

# Wait for stack to be complete
aws cloudformation wait stack-update-complete --stack-name $STACK_NAME --region $LAMBDA_REGION 2>/dev/null || \
aws cloudformation wait stack-create-complete --stack-name $STACK_NAME --region $LAMBDA_REGION

# Get outputs
echo "📋 Retrieving stack outputs..."
OUTPUTS=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --region $LAMBDA_REGION --query 'Stacks[0].Outputs')

FUNCTION_ARN=$(echo $OUTPUTS | jq -r '.[] | select(.OutputKey=="LambdaFunctionArn") | .OutputValue')
AGENT_RUNTIME_ARN=$(echo $OUTPUTS | jq -r '.[] | select(.OutputKey=="AgentRuntimeArn") | .OutputValue')
LAYER_ARN=$(echo $OUTPUTS | jq -r '.[] | select(.OutputKey=="LayerArn") | .OutputValue')
BUCKET_NAME=$(echo $OUTPUTS | jq -r '.[] | select(.OutputKey=="DeploymentBucket") | .OutputValue')

# Both durable function and agent runtime configuration handled natively by CloudFormation
echo "✅ All configuration handled natively by CloudFormation template"

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📋 Deployment Summary:"
echo "   Stack Name: $STACK_NAME"
echo "   Function Name: $FUNCTION_NAME"
echo "   Function ARN: $FUNCTION_ARN"
echo "   Agent Runtime ARN: $AGENT_RUNTIME_ARN"
echo "   Layer ARN: $LAYER_ARN"
echo "   S3 Bucket: $BUCKET_NAME"
echo "   Lambda Region: $LAMBDA_REGION"
echo "   Agent Region: $AGENT_REGION"
echo ""

echo "🧪 Test the Fraud Detection Function:"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 INTERACTIVE TESTING (Recommended)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Use the interactive invoke script:"
echo "   ./invoke-function.sh"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "💰 MANUAL TESTING - Transaction Scenarios"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if command -v aws durable-lambda help &> /dev/null; then
    echo "1️⃣  Low Risk Transaction (Auto-Approve, score < 3):"
    echo "   aws durable-lambda invoke \\"
    echo "     --function-name '$FUNCTION_ARN' \\"
    echo "     --invocation-type Event \\"
    echo "     --payload '{\"id\":1,\"amount\":500,\"location\":\"New York\",\"vendor\":\"Amazon\"}' \\"
    echo "     --region $LAMBDA_REGION \\"
    echo "     output-low-risk.json"
    echo ""
    echo "2️⃣  High Risk Transaction (Send to Fraud, score = 5):"
    echo "   aws durable-lambda invoke \\"
    echo "     --function-name '$FUNCTION_ARN' \\"
    echo "     --invocation-type Event \\"
    echo "     --payload '{\"id\":2,\"amount\":10000,\"location\":\"Unknown\",\"vendor\":\"Suspicious Store\"}' \\"
    echo "     --region $LAMBDA_REGION \\"
    echo "     output-high-risk.json"
    echo ""
    echo "3️⃣  Medium Risk Transaction (Human Verification, score 3-4):"
    echo "   aws durable-lambda invoke \\"
    echo "     --function-name '$FUNCTION_ARN' \\"
    echo "     --invocation-type Event \\"
    echo "     --payload '{\"id\":3,\"amount\":6500,\"location\":\"Los Angeles\",\"vendor\":\"Electronics Store\"}' \\"
    echo "     --region $LAMBDA_REGION \\"
    echo "     output-medium-risk.json"
else
    echo "⚠️  Using regular Lambda invoke (durable-lambda CLI not available):"
    echo ""
    echo "1️⃣  Low Risk Transaction:"
    echo "   aws lambda invoke \\"
    echo "     --function-name '$FUNCTION_NAME' \\"
    echo "     --invocation-type Event \\"
    echo "     --payload '{\"id\":1,\"amount\":500,\"location\":\"New York\",\"vendor\":\"Amazon\"}' \\"
    echo "     --region $LAMBDA_REGION \\"
    echo "     output-low-risk.json"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 MONITORING & DEBUGGING"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if command -v aws durable-lambda help &> /dev/null; then
    echo "📋 List all durable executions:"
    echo "   aws durable-lambda list-durable-executions-by-function \\"
    echo "     --function-name $FUNCTION_NAME \\"
    echo "     --region $LAMBDA_REGION"
    echo ""
    echo "🔍 Get execution details (replace <ARN> with execution ARN from invoke output):"
    echo "   aws durable-lambda get-durable-execution \\"
    echo "     --durable-execution-arn <ARN> \\"
    echo "     --region $LAMBDA_REGION"
    echo ""
fi

echo "📝 View CloudWatch Logs:"
echo "   aws logs tail /aws/lambda/$FUNCTION_NAME \\"
echo "     --region $LAMBDA_REGION \\"
echo "     --follow"
echo ""

echo "🗑️  To delete the stack:"
echo "   sam delete --stack-name $STACK_NAME --region $LAMBDA_REGION"
echo ""

echo "✅ SAM deployment complete!"