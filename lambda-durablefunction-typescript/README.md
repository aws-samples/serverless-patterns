# AWS Durable Functions - Fraud Detection Demo

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

## Shell Compatibility

⚠️ **Important**: All scripts in this project are written for **Bash** and may not work with other shells (zsh, fish, etc.).

If you're on macOS Catalina or later (which defaults to zsh), you can:
- Run scripts with `bash ./script.sh` explicitly
- Or temporarily switch to bash: `bash` then run scripts normally

## Requirements

Ensure you have the following installed and configured:

### 1. Python 3.11+
```bash
# Check if installed
python3 --version

# Install on macOS
brew install python@3.11

# Install on Ubuntu/Debian
sudo apt update && sudo apt install python3.11
```

### 2. AWS CLI (configured with credentials)
```bash
# Check if installed
aws --version

# Install on macOS
brew install awscli

# Install on Linux
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configure with your credentials
aws configure
```

### 3. UV Package Manager (Python package manager)
```bash
# Check if installed
uv --version

# Install
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"
```

### 4. Docker Desktop (required for building ARM64 container images)
```bash
# Check if installed
docker --version

# Install on macOS
brew install --cask docker

# Install on Linux
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Start Docker and verify
docker run hello-world
```

### 5. Node.js 24.x (for Lambda function)
```bash
# Check if installed
node --version

# Install on macOS
brew install node@24

# Install on Linux (using nvm)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 24
```

### 6. jq (JSON processor for CLI output)
```bash
# Check if installed
jq --version

# Install on macOS
brew install jq

# Install on Ubuntu/Debian
sudo apt install jq
```

## Deployment

### Step 1: Deploy the Complete Stack

The main deployment script handles both the Bedrock AgentCore agent and the Lambda durable function:

```bash
# Make script executable
chmod +x deploy.sh

# Deploy everything (agent + Lambda function)
./deploy.sh
```

This script will:
1. Deploy the Bedrock AgentCore fraud detection agent (containerized FastAPI app)
2. Wait for the agent runtime to be ready
3. Build and package the Lambda function with dependencies
4. Create/update IAM roles with necessary permissions
5. Deploy the durable Lambda function
6. Publish a new version

**Note**: First deployment takes ~5-10 minutes due to Docker image building and ECR push.

### Step 2: Verify Deployment

Check that both components are deployed:

```bash
# Check agent runtime status, update with the region you deployed to
aws bedrock-agentcore list-runtimes --region us-east-1

# Check Lambda function, update with the region you deployed to
aws lambda get-function \
  --function-name fn-Fraud-Detection \
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
├── deploy.sh                          # Main deployment script
├── invoke-function.sh                 # Interactive function invocation
├── send-callback.sh                   # Send callback responses
├── service.json                       # AWS CLI durable-lambda service model
├── README.md                          # This file
│
├── FraudDetection-Agent/              # Bedrock AgentCore Agent
│   ├── agent.py                       # FastAPI fraud detection agent
│   ├── Dockerfile                     # Container definition (ARM64)
│   ├── deploy.sh                      # Agent deployment script
│   ├── pyproject.toml                 # Python dependencies
│   └── uv.lock                        # Package lock file
│
└── FraudDetection-Lambda/             # Durable Lambda Function
    ├── src/
    │   └── index.ts                   # Main Lambda handler 
    ├── dist/
    │   └── index.js                   # Node Coverted Lambda handler (created after deployment)
    ├── package.json                   # Node.js dependencies
    ├── function.zip                   # Zip file for Lambda (created after deployment)
    ├── layer.zip                      # Zip file for Lambda Layer (created after deployment)
    └── tsconfig.json                  # TypeScript configuration
```

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
  --region us-east-1 \
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

### Lambda Function Settings
- **Region**: `us-east-2`
- **Runtime**: Node.js 24.x
- **Timeout**: 120 seconds (per invocation)
- **Execution Timeout**: 600 seconds (total durable execution)
- **Memory**: 128 MB
- **Retention**: 7 days

### Agent Settings
- **Region**: `us-east-1`
- **Runtime**: Python 3.11 (FastAPI + Uvicorn)
- **Platform**: ARM64 (Graviton)
- **Port**: 8080
- **Endpoints**: `/invocations`, `/ping`

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

To remove all deployed resources:

```bash
# Delete Lambda function
aws lambda delete-function \
  --function-name fn-Fraud-Detection \
  --region us-east-2

# Delete agent runtime
aws bedrock-agentcore delete-runtime \
  --runtime-identifier <RUNTIME_ID> \
  --region us-east-1

# Delete S3 bucket (if desired)
aws s3 rb s3://durable-functions-<ACCOUNT_ID> --force

# Delete IAM role
aws iam delete-role --role-name durable-function-execution-role
```

## Additional Resources

- [AWS Lambda Durable Functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [AWS Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/)
- [Durable Functions SDK Specification](./docs/4-sdk-functional-spec.md)
- [Durable Functions API Specification](./docs/5-api-functional-spec.md)

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0