# AWS Durable Function with Amazon Bedrock Agent - Fraud Detection Demo

This project demonstrates AWS Lambda Durable Functions integrated with AWS Bedrock AgentCore for intelligent fraud detection. It showcases a multi-step, stateful workflow that can run for extended periods (up to one year) with automatic state persistence, human-in-the-loop verification, and AI-powered risk scoring.

## Overview

The fraud detection workflow:
1. **Risk Assessment**: Invokes a Bedrock AgentCore agent to analyze transaction amounts and assign risk scores (1-5)
2. **Automated Decisions**: 
   - Low risk (score < 3): Auto-authorize
   - High risk (score ≥ 5): Escalate to fraud department
3. **Human Verification**: Medium risk (score 3-4) triggers parallel email/SMS verification callbacks
4. **Durable State**: All progress is checkpointed, allowing the function to suspend and resume without losing state

## Architecture

```
Transaction → Durable Lambda → Bedrock AgentCore Agent → Risk Score
                    ↓
              Score < 3: Authorize
              Score 3-4: Human Verification (Email/SMS Callbacks)
              Score ≥ 5: Send to Fraud Department
```

## Deployment Methods

This project supports deployment through a SAM Template (Recommended) - Infrastructure as Code with CloudFormation


## Shell Compatibility

⚠️ **Important**: All scripts in this project are written for **Bash** and may not work with other shells (zsh, fish, etc.).

If you're on macOS Catalina or later (which defaults to zsh), you can:
- Run scripts with `bash ./script.sh` explicitly
- Or temporarily switch to bash: `bash` then run scripts normally

## Prerequisites

### Core Requirements

1. **AWS CLI v2** with configured credentials
2. **Docker Desktop** - Required for building containers and layers
3. **jq** - JSON processor for parsing outputs

### For SAM Deployment (Recommended)

4. **SAM CLI 1.51 or later** - [Installation Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)


### Installation Commands

```bash
# AWS CLI v2
# macOS: brew install awscli
# Linux: curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install
aws configure  # Configure with your credentials

# Docker Desktop
# macOS: brew install --cask docker
# Linux: curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
docker run hello-world  # Verify installation

# jq
# macOS: brew install jq
# Ubuntu/Debian: sudo apt install jq

# SAM CLI (for SAM deployment)
# macOS: brew install aws-sam-cli
# Linux: Follow AWS SAM CLI installation guide

# Python 3.11+ and UV (for shell script deployment)
# macOS: brew install python@3.11
# Ubuntu/Debian: sudo apt update && sudo apt install python3.11
curl -LsSf https://astral.sh/uv/install.sh | sh

# Node.js 24.x (for shell script deployment)
# macOS: brew install node@24
# Linux: curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash && nvm install 24
```

## Deployment

Deploy using Infrastructure as Code with AWS SAM:

```bash
# Quick deployment
chmod +x deploy-sam.sh
./deploy-sam.sh
```

Or manually:
```bash
# 1. Get AWS Account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
LAMBDA_REGION="us-east-2"
AGENT_REGION="us-east-2"
ECR_REPO_NAME="fraud-risk-scorer"
FUNCTION_NAME="fn-Fraud-Detection"
LAYER_NAME="lr-FraudDetection"

# 2. Build and push Docker image for Bedrock AgentCore agent
cd FraudDetection-Agent

# Create ECR repository if it doesn't exist
aws ecr create-repository --repository-name $ECR_REPO_NAME --region $AGENT_REGION || true

# Login to ECR
aws ecr get-login-password --region $AGENT_REGION | \
  docker login --username AWS --password-stdin \
  $ACCOUNT_ID.dkr.ecr.$AGENT_REGION.amazonaws.com

# Build and push ARM64 image
docker buildx create --use --name sam-builder 2>/dev/null || docker buildx use sam-builder
docker buildx build --platform linux/arm64 \
  -t $ACCOUNT_ID.dkr.ecr.$AGENT_REGION.amazonaws.com/$ECR_REPO_NAME:latest \
  --push .

cd ..

# 3. Build Lambda function and layer packages
cd FraudDetection-Lambda

# Clean and install dependencies
rm -rf node_modules dist function.zip layer.zip || true
npm install

# Compile TypeScript
tsc

# Create function package
cd dist && zip -qr ../function.zip . && cd ..
zip -r function.zip package.json

# Create layer package
mkdir -p layer/nodejs
cp -r node_modules layer/nodejs/
cd layer && zip -qr ../layer.zip . && cd ..

# 4. Create S3 bucket for deployment artifacts
BUCKET_NAME="durable-functions-$ACCOUNT_ID"

# Create bucket with proper configuration
if [ "$LAMBDA_REGION" = "us-east-1" ]; then
    aws s3api create-bucket --bucket $BUCKET_NAME --region $LAMBDA_REGION
else
    aws s3api create-bucket --bucket $BUCKET_NAME --region $LAMBDA_REGION \
        --create-bucket-configuration LocationConstraint=$LAMBDA_REGION
fi

# Enable versioning and encryption
aws s3api put-bucket-versioning --bucket $BUCKET_NAME \
    --versioning-configuration Status=Enabled --region $LAMBDA_REGION

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

# 5. Upload packages to S3
aws s3 cp function.zip s3://$BUCKET_NAME/functions/$FUNCTION_NAME.zip --region $LAMBDA_REGION
aws s3 cp layer.zip s3://$BUCKET_NAME/layers/$LAYER_NAME.zip --region $LAMBDA_REGION

# Clean up build artifacts
rm -rf node_modules dist layer function.zip layer.zip

cd ..

# 6. Deploy SAM application
sam deploy \
    --stack-name fraud-detection-durable-function \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $LAMBDA_REGION \
    --parameter-overrides \
        FunctionName=$FUNCTION_NAME \
        LayerName=$LAYER_NAME \
        RoleName=durable-function-execution-role \
        AgentRuntimeName=fraud_risk_scorer \
        AgentRoleName=bedrock-agentcore-runtime-fraud-role \
        ECRRepoName=$ECR_REPO_NAME \
        LambdaRegion=$LAMBDA_REGION \
        AgentRegion=$AGENT_REGION \
    --no-fail-on-empty-changeset

# 7. Wait for deployment completion
aws cloudformation wait stack-create-complete \
    --stack-name fraud-detection-durable-function \
    --region $LAMBDA_REGION
```

### Deployment Process

The following will install:
1. **Build Agent Container**: Create and push Python FastAPI agent to ECR
2. **Deploy Agent Runtime**: Create Bedrock AgentCore runtime with container
3. **Create Infrastructure**: S3 bucket, IAM roles, Lambda layer
4. **Deploy Lambda Function**: Durable function with proper configuration
5. **Configure Permissions**: Set up cross-service permissions
6. **Publish Version**: Create versioned deployment

**Note**: First deployment takes ~5-10 minutes due to Docker image building and ECR push.

### Verify Deployment

Check that both components are deployed:

```bash
# Check agent runtime status
aws bedrock-agentcore-control list-agent-runtimes --region us-east-2

# Check Lambda function
aws lambda get-function \
  --function-name fn-Fraud-Detection \
  --region us-east-2

# For SAM deployments, check stack status
aws cloudformation describe-stacks \
  --stack-name fraud-detection-durable-function \
  --region us-east-2
```

## Usage

### Invoking the Fraud Detection Function

Use the interactive invoke script to test transactions:

```bash
# Make script executable
chmod +x invoke-function.sh

# Run the script
./invoke-function.sh
```

The script will prompt you for:
- **Transaction ID** (default: current timestamp)
- **Amount** (default: $5000.00) - This determines the risk score
- **Location** (default: "New York")
- **Vendor** (default: "Amazon")
- **Initial Score** (default: 0) - Set to 0 to use the Bedrock Agent, or 1-5 to override

**Risk Score Behavior**:
- Amounts < $1,000: Agent returns scores 1-2 (auto-approved)
- Amounts $1,000-$4,999: Agent returns scores 1-4 (weighted toward lower scores)
- Amounts $5,000-$9,999: Agent returns scores 3-5 (higher risk, weighted toward lower scores)
- Amount = $6500: Agent returns 3 (forces human-in-the-loop)
- Amounts >= $10,000: Agent returns scores 5 (Send to Fraud)

### Example Invocations

**Low Risk Transaction (Auto-Approve)**:
```bash
./invoke-function.sh
# Enter amount: 500
# Result: Automatically authorized (score < 3)
```

**High Risk Transaction (Auto-Reject)**:
```bash
./invoke-function.sh
# Enter amount: 10000
# Result: Sent to fraud department (score 5)
```

**Medium Risk Transaction (Human Verification)**:
```bash
./invoke-function.sh
# Enter amount: 6500
# Result: Triggers email/SMS verification callbacks (score 3)
```

### Handling Human-in-the-Loop Callbacks

When a transaction requires human verification (risk score 3-4), the function will:
1. Suspend the transaction
2. Generate two callback IDs (one for email, one for SMS)
3. Wait for user response via callback

**Retrieve Callback IDs**:

Option 1 - From CloudWatch Logs:
```bash
aws logs tail /aws/lambda/fn-Fraud-Detection \
  --region eu-south-1 \
  --follow
```

Option 2 - From Execution History:
```bash
aws lambda get-durable-execution-history \
  --durable-execution-arn <ARN_FROM_INVOKE_OUTPUT> \
  --region us-east-2 \
  --include-execution-data
```

**Send Callback Response**:

```bash
# Make script executable
chmod +x send-callback.sh

# Run the callback script
./send-callback.sh
```

The script will prompt you for:
1. **Callback ID** (from logs or execution history)
2. **Response Type**:
   - `1` = Success (approve transaction)
   - `2` = Failure (reject transaction)

**Callback Behavior**:
- If **either** email or SMS is approved → Transaction is authorized
- If **any** callback fails/rejects → Transaction is sent to fraud department
- The parallel execution uses `toleratedFailureCount: 0`, so any failure immediately escalates

## Project Structure

```
DFNs/
├── template.yaml                      # SAM template (Infrastructure as Code)
├── samconfig.toml                     # SAM configuration
├── deploy-sam.sh                      # SAM deployment script
├── invoke-function.sh                 # Interactive function invocation
├── send-callback.sh                   # Send callback responses
├── README.md                          # This file
│
├── FraudDetection-Agent/              # Bedrock AgentCore Agent
│   ├── agent.py                       # FastAPI fraud detection agent
│   ├── Dockerfile                     # Container definition (ARM64)
│   ├── pyproject.toml                 # Python dependencies
│   └── uv.lock                        # Package lock file
│
└── FraudDetection-Lambda/             # Durable Lambda Function
    ├── src/
    │   └── index.ts                   # Main Lambda handler 
    ├── dist/                          # Compiled JavaScript (created after build)
    │   └── index.js                   
    ├── package.json                   # Node.js dependencies
    ├── function.zip                   # Lambda deployment package (created after build)
    ├── layer.zip                      # Lambda layer package (created after build)
    └── tsconfig.json                  # TypeScript configuration
```

### Key Files

- **`template.yaml`**: SAM/CloudFormation template defining all AWS resources
- **`samconfig.toml`**: Configuration for SAM CLI (regions, parameters, etc.)
- **`deploy-sam.sh`**: Automated SAM deployment with Docker image building
- **`invoke-function.sh`**: Interactive script for testing transactions
- **`send-callback.sh`**: Script for responding to human verification callbacks

## Key Features Demonstrated

### 1. Durable Execution
- **State Persistence**: Function state is automatically checkpointed at each step
- **Automatic Recovery**: If the function fails, it resumes from the last checkpoint
- **Long-Running**: Can execute for up to one year (async invocations)

### 2. Bedrock AgentCore Integration
- **AI-Powered Scoring**: Uses containerized agent for fraud risk assessment
- **Streaming Responses**: Properly handles AgentCore's streaming HTTP responses
- **Dynamic Invocation**: Agent is called only when needed (score = 0)

**Note**: No LLM is actually used by the Agent.  It is using random numbers weighted based on the transaction amount.  However, the agent is built with strands SDK and can easily be extended to prompt LLMs.

### 3. Human-in-the-Loop
- **Parallel Callbacks**: Email and SMS verification run concurrently (MOCKED: no actual email/SMS messages are sent)
- **Flexible Completion**: Succeeds when either channel approves
- **Failure Handling**: Immediately escalates if any verification fails

### 4. Workflow Orchestration
- **Conditional Branching**: Different paths based on risk score
- **Step Isolation**: Each step is independently retryable
- **Result Tracking**: Comprehensive transaction result objects

## Monitoring and Debugging

### View CloudWatch Logs
```bash
# Tail logs in real-time
aws logs tail /aws/lambda/fn-Fraud-Detection \
  --region eu-south-1 \
  --follow

# View recent logs
aws logs tail /aws/lambda/fn-Fraud-Detection \
  --region eu-south-1 \
  --since 1h
```

### Check Execution Status
```bash
# List all executions
aws lambda list-durable-executions-by-function \
  --function-name fn-Fraud-Detection \
  --region us-east-2

# Get specific execution details
aws lambda get-durable-execution \
  --durable-execution-arn <ARN> \
  --region us-east-2

# View execution history with data
aws lambda get-durable-execution-history \
  --durable-execution-arn <ARN> \
  --region us-east-2 \
  --include-execution-data
```

### Agent Logs
```bash
# View agent runtime logs
aws logs tail /aws/bedrock-agentcore/runtimes/fraud_risk_scorer-<ID>-DEFAULT \
  --region us-east-2 \
  --follow
```

## IAM Permissions

The Lambda execution role requires:

1. **Basic Lambda Execution**:
   - `AWSLambdaBasicExecutionRole` (managed policy)

2. **Durable Execution**:
   - `lambda:CheckpointDurableExecution`
   - `lambda:GetDurableExecutionState`

3. **Bedrock AgentCore**:
   - `bedrock-agentcore:InvokeAgentRuntime`

Reference: [Bedrock AgentCore Runtime Permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html)

## Configuration

### Default Settings

The deployment creates resources with these default configurations:

#### Lambda Function
- **Name**: `fn-Fraud-Detection`
- **Region**: `us-east-2` (configurable)
- **Runtime**: Node.js 24.x
- **Timeout**: 120 seconds (per invocation)
- **Execution Timeout**: 600 seconds (total durable execution)
- **Memory**: 128 MB
- **Retention**: 7 days
- **Layer**: `lr-FraudDetection`

#### Bedrock AgentCore Agent
- **Name**: `fraud_risk_scorer`
- **Region**: `us-east-2` (required for Bedrock AgentCore)
- **Runtime**: Python 3.11 (FastAPI + Uvicorn)
- **Platform**: ARM64 (Graviton)
- **Port**: 8080
- **Endpoints**: `/invocations`, `/ping`
- **ECR Repository**: `fraud-risk-scorer`

#### IAM Roles
- **Lambda Role**: `durable-function-execution-role`
- **Agent Role**: `bedrock-agentcore-runtime-fraud-role`

### Customizing Configuration

#### SAM Template Parameters

Edit `samconfig.toml` or override during deployment:

```bash
sam deploy --parameter-overrides \
    FunctionName=my-fraud-function \
    LambdaRegion=us-west-2 \
    AgentRuntimeName=my_agent \
    AgentRegion=us-east-1
```

Available parameters:
- `FunctionName`: Lambda function name
- `LayerName`: Lambda layer name
- `RoleName`: Lambda execution role name
- `AgentRuntimeName`: Bedrock AgentCore runtime name
- `AgentRoleName`: Agent IAM role name
- `ECRRepoName`: ECR repository name
- `LambdaRegion`: Region for Lambda deployment
- `AgentRegion`: Region for Bedrock AgentCore 

#### Shell Script Variables

Edit the variables at the top of `deploy.sh`:

```bash
FUNCTION_NAME="fn-Fraud-Detection"
LAYER_NAME="lr-FraudDetection"
REGION="us-east-2"
ROLE_NAME="durable-function-execution-role"
# ... other variables
```

## Troubleshooting

### Issue: "Invalid base64" error when invoking
**Solution**: The payload is automatically base64 encoded by `invoke-function.sh`. Don't manually encode it.

### Issue: Agent returns 500 error
**Solution**: Check agent logs for errors. Ensure the payload format is `{"input": {"amount": X}}`.

### Issue: Callback not found
**Solution**: Callbacks expire after the timeout period (default: 1 day). Retrieve the callback ID from recent logs.

### Issue: Docker build fails on macOS
**Solution**: Ensure Docker Desktop is running and configured for ARM64 builds.

### Issue: "Cannot find module" errors
**Solution**: Run `npm install` in `FraudDetection-Lambda/` directory.

## Cleanup

### SAM Deployment Cleanup

```bash
# Delete entire stack (recommended)
sam delete --stack-name fraud-detection-durable-function --region us-east-2

# Or use CloudFormation directly
aws cloudformation delete-stack \
  --stack-name fraud-detection-durable-function \
  --region us-east-2
```

### Shell Script Deployment Cleanup

```bash
# Delete Lambda function
aws lambda delete-function \
  --function-name fn-Fraud-Detection \
  --region us-east-2

# Delete agent runtime (get runtime ID from list-agent-runtimes)
aws bedrock-agentcore-control delete-agent-runtime \
  --agent-runtime-id <RUNTIME_ID> \
  --region us-east-2

# Delete S3 bucket (if desired)
aws s3 rb s3://durable-functions-<ACCOUNT_ID> --force

# Delete IAM roles
aws iam delete-role --role-name durable-function-execution-role
aws iam delete-role --role-name bedrock-agentcore-runtime-fraud-role

# Delete ECR repository
aws ecr delete-repository \
  --repository-name fraud-risk-scorer \
  --region us-east-2 \
  --force
```

## Additional Resources

- [AWS Lambda Durable Functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [AWS Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/)
- [Durable Functions SDK Specification](./docs/4-sdk-functional-spec.md)
- [Durable Functions API Specification](./docs/5-api-functional-spec.md)

## License

This is a demonstration project for educational purposes.