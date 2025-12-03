# Order Processing Workflow with Lambda Durable Functions

This pattern demonstrates a multi-step order processing workflow using AWS Lambda Durable Functions. The workflow handles order validation, payment processing, inventory checking, and shipping arrangement with automatic checkpointing and state persistence across long-running operations.

**Important:** Lambda Durable Functions are currently available in the **us-east-2 (Ohio)** region only.

## Architecture

![Architecture Diagram](architecture.png)

The Order Processor uses Lambda Durable Functions to execute a multi-step workflow with automatic checkpointing. Each step (validate, payment, inventory, shipping) is checkpointed, allowing the workflow to resume from the last successful step if interrupted.

### Workflow Steps

1. **Validate Order** - Validates order data and customer information
2. **Process Payment** - Simulates payment processing with 5-second wait
3. **Check Inventory** - Verifies item availability with 5-second wait
4. **Arrange Shipping** - Creates shipment with 5-second wait
5. **Complete Order** - Saves final order state to DynamoDB

Each step is automatically checkpointed, allowing the workflow to resume from the last successful step if interrupted.

## Key Features

- ✅ **Automatic Checkpointing** - Each step is checkpointed automatically
- ✅ **Failure Recovery** - Resumes from last checkpoint on failure
- ✅ **Compensation Logic** - Rolls back on errors
- ✅ **Wait States** - Efficient waiting without compute charges
- ✅ **State Persistence** - Order status stored in DynamoDB
- ✅ **API Integration** - REST API for order submission and status checking

## Prerequisites

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed
* [Node.js 18+](https://nodejs.org/) installed

## Deployment

1. Navigate to the pattern directory:
   ```bash
   cd lambda-durable-order-processing-sam
   ```

2. Install dependencies:
   ```bash
   cd src && npm install && cd ..
   ```

3. Build the SAM application:
   ```bash
   sam build
   ```

4. Deploy the application (must use us-east-2 region):
   ```bash
   sam deploy --guided --region us-east-2
   ```
   
   During the guided deployment:
   - Stack Name: `lambda-durable-order-processing`
   - AWS Region: `us-east-2`
   - Confirm changes: `N`
   - Allow SAM CLI IAM role creation: `Y`
   - Disable rollback: `N`
   - Save arguments to config file: `Y`

5. Note the `OrderApiEndpoint` from the outputs.

## Testing

### Get Your API Endpoint

First, retrieve your API endpoint from the CloudFormation stack:

```bash
API_ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name lambda-durable-order-processing \
  --region us-east-2 \
  --query 'Stacks[0].Outputs[?OutputKey==`OrderApiEndpoint`].OutputValue' \
  --output text)

echo "API Endpoint: $API_ENDPOINT"
```

### Create Test Orders

**Test 1: Simple order**
```bash
curl -X POST ${API_ENDPOINT}/orders \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "CUST-001",
    "customerEmail": "customer1@example.com",
    "items": [
      {"productId": "LAPTOP-001", "quantity": 1}
    ]
  }'
```

**Test 2: Multiple items**
```bash
curl -X POST ${API_ENDPOINT}/orders \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "CUST-002",
    "customerEmail": "customer2@example.com",
    "items": [
      {"productId": "PHONE-001", "quantity": 2},
      {"productId": "CASE-001", "quantity": 2},
      {"productId": "CHARGER-001", "quantity": 1}
    ]
  }'
```

**Test 3: Validation error (missing customerId)**
```bash
curl -X POST ${API_ENDPOINT}/orders \
  -H "Content-Type: application/json" \
  -d '{
    "items": [
      {"productId": "LAPTOP-001", "quantity": 1}
    ]
  }'
```

Response format:
```json
{
  "message": "Order processing initiated",
  "orderId": "order-1234567890-abc123",
  "statusUrl": "/orders/order-1234567890-abc123"
}
```

### Check Order Status

Replace `<orderId>` with the order ID from the response:

```bash
curl ${API_ENDPOINT}/orders/<orderId>
```

### Monitor Durable Executions

**View Lambda logs in real-time:**
```bash
FUNCTION_NAME=$(aws cloudformation describe-stack-resources \
  --stack-name lambda-durable-order-processing \
  --region us-east-2 \
  --query 'StackResources[?ResourceType==`AWS::Lambda::Function`].PhysicalResourceId' \
  --output text | grep -i "order-processor")

aws logs tail /aws/lambda/${FUNCTION_NAME} \
  --follow \
  --format short \
  --region us-east-2
```

**View recent logs:**
```bash
aws logs tail /aws/lambda/${FUNCTION_NAME} \
  --since 5m \
  --format short \
  --region us-east-2
```

### Verify DynamoDB Storage

Check orders saved to DynamoDB:

```bash
TABLE_NAME=$(aws cloudformation describe-stacks \
  --stack-name lambda-durable-order-processing \
  --region us-east-2 \
  --query 'Stacks[0].Outputs[?OutputKey==`OrdersTableName`].OutputValue' \
  --output text)

aws dynamodb scan \
  --table-name ${TABLE_NAME} \
  --region us-east-2 \
  --max-items 10
```

### List Durable Executions

View all durable executions for the function:

```bash
aws lambda list-durable-executions \
  --function-name ${FUNCTION_NAME}:prod \
  --region us-east-2
```

Get details for a specific execution:

```bash
aws lambda get-durable-execution \
  --function-name ${FUNCTION_NAME}:prod \
  --execution-id <execution-id> \
  --region us-east-2
```

For detailed testing instructions, see [TESTING.md](TESTING.md).

## How It Works

### Durable Execution

The order processing function uses the `@aws/durable-execution-sdk-js` to create checkpoints at each step:

```javascript
import { withDurableExecution } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(async (event, context) => {
  // Each step is automatically checkpointed
  await context.step('validate-order', async () => {
    console.log('Validating order');
    // Validation logic
  });

  // Wait 5 seconds (simulating external API call)
  await context.wait({ seconds: 5 });

  await context.step('process-payment', async () => {
    console.log('Processing payment');
    // Payment logic
  });

  // More steps...
});
```

### Checkpoint Behavior

When a durable function executes:
1. Each `context.step()` creates a checkpoint before execution
2. If the function is interrupted, Lambda saves the checkpoint state
3. On retry, the function replays from the beginning
4. Completed steps are skipped using stored checkpoint results
5. Execution continues from the last incomplete step

You'll see the same order ID appear multiple times in logs - this is the durable execution resuming from checkpoints!

### State Persistence

Final order state is saved to DynamoDB after all steps complete:

```javascript
await context.step('save-order', async () => {
  await dynamodb.putItem({
    TableName: process.env.ORDERS_TABLE,
    Item: { orderId, status: 'completed', ... }
  });
});
```

## Configuration

### Durable Execution Settings

The durable function must be created with durable configuration (cannot be added to existing functions):

```bash
aws lambda create-function \
  --function-name my-durable-function \
  --runtime nodejs22.x \
  --durable-config '{"ExecutionTimeout":86400,"RetentionPeriodInDays":7}' \
  ...
```

- **ExecutionTimeout**: 86400 seconds (24 hours)
- **RetentionPeriodInDays**: 7 days

### IAM Permissions

The function requires these permissions:

```yaml
Policies:
  - Statement:
    - Effect: Allow
      Action:
        - lambda:CheckpointDurableExecution
        - lambda:GetDurableExecutionState
      Resource: !Sub 'arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:function:${FunctionName}:*/durable-execution/*'
  - DynamoDBCrudPolicy:
      TableName: !Ref OrdersTable
```

## Customization

### Adjust Wait Time

Modify the wait duration in `src/index.js`:

```javascript
await context.wait({ seconds: 3600 }); // Wait 1 hour
```

### Add More Steps

Add additional processing steps:

```javascript
await context.step('send-notification', async () => {
  console.log('Sending notification');
  // Send email/SMS notification
});
```

### Integrate Real Services

Replace simulation code with actual service calls:

```javascript
await context.step('process-payment', async () => {
  const stripe = require('stripe')(process.env.STRIPE_KEY);
  return await stripe.charges.create({
    amount: order.total * 100,
    currency: 'usd',
    customer: order.customerId
  });
});
```

### Modify Execution Timeout

Update the durable configuration when creating the function:

```yaml
DurableConfig:
  ExecutionTimeout: 172800  # 48 hours
  RetentionPeriodInDays: 14
```

## Monitoring

### CloudWatch Metrics

Monitor durable execution metrics:
- `DurableExecutionStarted`
- `DurableExecutionCompleted`
- `DurableExecutionFailed`
- `DurableExecutionCheckpointCreated`

### CloudWatch Logs

Look for log entries with `[DURABLE_EXECUTION]` prefix to track:
- Checkpoint creation
- Replay events
- Step execution

### X-Ray Tracing

Enable X-Ray tracing in the SAM template:

```yaml
Tracing: Active
```

## Cleanup

Delete the stack:

```bash
sam delete --region us-east-2
```

Or via AWS CLI:

```bash
aws cloudformation delete-stack --stack-name lambda-durable-order-processing --region us-east-2
```

## Cost Considerations

- **Lambda**: Pay per invocation and execution time
- **DynamoDB**: Pay-per-request pricing
- **API Gateway**: Pay per API call
- **Durable Execution**: Checkpoint storage costs (minimal)
- **Wait States**: No compute charges during waits

## Learn More

- [Lambda Durable Functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Durable Execution SDK (JavaScript)](https://github.com/aws/aws-durable-execution-sdk-js)
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)

---

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
