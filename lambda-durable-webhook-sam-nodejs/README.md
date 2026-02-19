# Webhook Receiver with AWS Lambda durable functions - NodeJS

This serverless pattern demonstrates a serverless webhook receiver using AWS Lambda durable functions with NodeJS. The pattern receives webhook events via API Gateway, processes them durably with automatic checkpointing, and provides status query capabilities.

## How It Works

This pattern demonstrates a serverless webhook receiver using AWS Lambda durable functions. The pattern receives webhook events via API Gateway, processes them durably with automatic checkpointing, and provides status query capabilities.

### Webhook Processing Workflow (3 Steps)

The durable function processes webhooks in 3 checkpointed steps:

1. **Validate** - Verify webhook payload and structure
2. **Process** - Execute business logic on webhook data  
3. **Finalize** - Complete processing and update final status

✅ Each step is automatically checkpointed, allowing the workflow to resume from the last successful step if interrupted.

## Key Features

- ✅ **Automatic Checkpointing** - Each processing step is checkpointed automatically
- ✅ **Failure Recovery** - Resumes from last checkpoint on failure
- ✅ **Asynchronous Processing** - Immediate 202 response, processing in background
- ✅ **State Persistence** - Execution state stored in DynamoDB with TTL
- ✅ **Status Query API** - Real-time status tracking via REST API

## Important

⚠️ **Important:** Please check the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) for regions currently supported by AWS Lambda durable functions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-webhook-sam-python

## Prerequisites

- [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed
- [Node.js 24.x](https://nodejs.org/en/download/) runtime installed
- [Docker](https://docs.docker.com/get-docker/) (for containerized builds)

## Required IAM Permissions

Your AWS CLI user/role needs the following permissions for deployment:

- **CloudFormation**: `cloudformation:DescribeStacks`, `cloudformation:DeleteStack`
- **Lambda**: `lambda:CreateFunction`, `lambda:InvokeFunction`, `lambda:GetFunction`
- **DynamoDB**: `dynamodb:Scan`, `dynamodb:GetItem`, `dynamodb:PutItem`
- **CloudWatch Logs**: `logs:DescribeLogGroups`, `logs:FilterLogEvents`, `logs:GetLogEvents`, `logs:TailLogEvents`

## Deployment

1. **Build the application**:
   ```bash
   sam build
   ```

2. **Deploy to AWS**:
   ```bash
   sam deploy --guided
   ```
   
   Note the outputs after deployment:
   - `WebhookApiUrl`: Use this for sending webhook POST requests
   - `StatusQueryApiUrl`: Use this for querying execution status

3. **Test the webhook**:
   ```bash
   # Send a test webhook
   curl -X POST <WebhookApiUrl> \
     -H "Content-Type: application/json" \
     -d '{
       "type": "order", 
       "orderId": "123456",
       "data": {"amount": 100}
     }'
   ```

4. **Query webhook status**:
   ```bash
   # Get execution status (use executionToken from webhook response)
   curl <StatusQueryApiUrl>
   ```
   
   **Success indicators:**
   - Webhook returns 202 with `executionToken`
   - Status query shows progression: `STARTED` → `VALIDATING` → `PROCESSING` → `COMPLETED`
   - Execution state persists in DynamoDB with TTL
   - Failed webhooks show `FAILED` status with error details

## Architecture

![Architecture Diagram](architecture.png)

## Components

### 1. Webhook Processor Function (`src/webhook_processor/`)
- **Lambda durable function**: Main orchestrator with automatic checkpointing
- **3-Step Processing**: Validate → Process → Finalize
- **API Gateway Integration**: Receives POST requests at `/webhook`
- **State Persistence**: Stores execution state in DynamoDB
- **Dependencies**: `@aws-sdk/client-dynamodb`, `@aws-sdk/lib-dynamodb`, `aws-durable-execution-sdk`

### 2. Webhook Validator Function (`src/webhook_validator/`)
- **Validation Logic**: Validates webhook payload structure and required fields
- **Extensible**: Easy to add custom validation rules
- **Dependencies**: None (pure Node.js)

### 3. Status Query Function (`src/status_query/`)
- **Real-time Status**: Query execution status via GET `/status/{executionToken}`
- **CORS Enabled**: Supports browser-based queries
- **Dependencies**: `@aws-sdk/client-dynamodb`, `@aws-sdk/lib-dynamodb`

## API Endpoints

### POST /webhook
Receives webhook events for processing.

**Request:**
```json
{
  "type": "order",
  "orderId": "123456", 
  "data": {"amount": 100}
}
```

**Response (202):**
```json
{
  "message": "Webhook processing completed successfully",
  "executionToken": "dev-esm-abc123",
  "status": "COMPLETED",
  "result": { ... }
}
```

### GET /status/{executionToken}
Query processing status of a webhook.

**Response (200):**
```json
{
  "executionToken": "dev-esm-abc123",
  "status": "COMPLETED",
  "timestamp": "2023-...",
  "currentStep": "finalize",
  "result": { ... }
}
```

## Monitoring

- **CloudWatch Logs**: Execution tracking for all functions
- **DynamoDB**: Persistent execution state with TTL (7 days)
- **API Gateway**: Request/response logging and metrics

## Configuration

Key environment variables:
- `ENVIRONMENT`: Deployment environment (dev/prod)
- `EVENTS_TABLE_NAME`: DynamoDB table for execution state
- `WEBHOOK_VALIDATOR_FUNCTION_ARN`: ARN of validation function
- `WEBHOOK_SECRET`: Optional secret for HMAC signature validation

## Error Handling

- **Automatic Retries**: Built-in retry logic with exponential backoff
- **State Recovery**: Resume from last checkpoint on failure
- **Error Tracking**: Failed executions stored with error details
- **Timeout Handling**: Configurable execution timeout (default: 1 hour)

## Cost Optimization

- **Pay-per-execution**: Only charged for active processing time
- **Automatic scaling**: Scales based on incoming webhook volume
- **TTL Storage**: Automatic cleanup of old execution records

## NodeJS Implementation Notes

- **Node.js 24.x runtime** (latest LTS) 
- **AWS SDK v3** with modular imports for optimal performance
- **Modern async/await** syntax throughout
- **Command pattern** for DynamoDB operations
- **Individual package.json** files for each function

## Security Considerations

- **CORS Configuration**: Configurable for your domain requirements
- **Webhook Secrets**: Optional HMAC signature validation support
- **IAM Permissions**: Principle of least privilege for all functions

## Cleanup

```bash
sam delete
```

## Learn More

- [AWS Lambda durable functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Lambda durable functions Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions-best-practices.html)
- [AWS SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Node.js AWS SDK v3 Documentation](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/)
