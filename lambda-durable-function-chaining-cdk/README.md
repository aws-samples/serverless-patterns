# Order Processing with AWS Lambda Durable Functions (CDK)

This pattern demonstrates an e-commerce order processing workflow using AWS Lambda Durable Functions with function chaining. The workflow orchestrates order validation, payment authorization, inventory allocation, and order fulfillment with automatic checkpointing and state persistence.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-function-chaining-cdk

## Architecture

![Architecture Diagram](architecture.png)

The solution implements a function chaining pattern where a durable orchestrator function coordinates multiple worker functions to process orders through a multi-step workflow.

### Components

- **ValidateOrder Function (Durable)**: Orchestrates the entire workflow with automatic checkpointing
- **AuthorizePayment Function**: Validates and authorizes payment methods
- **AllocateInventory Function**: Checks product availability and reserves inventory
- **FulfillOrder Function**: Creates shipments and generates tracking information
- **ProductCatalog Table**: DynamoDB table storing product information and stock levels

### Workflow Steps

The order processing workflow consists of 4 checkpointed steps:

1. **validate-order** - Validates order data, items, addresses, payment method, and order total
2. **authorize-payment** - Authorizes payment with the payment gateway
3. **allocate-inventory** - Checks inventory availability and reserves items
4. **fulfill-order** - Creates shipments and generates tracking numbers

Each step is automatically checkpointed, allowing the workflow to resume from the last successful step if interrupted.

## Key Features

- ✅ **Automatic Checkpointing** - Each step is checkpointed automatically
- ✅ **Failure Recovery** - Resumes from last checkpoint on failure
- ✅ **Function Chaining** - Orchestrator invokes worker functions sequentially
- ✅ **State Persistence** - Workflow state maintained across executions
- ✅ **Error Handling** - Graceful handling of validation, payment, and inventory failures
- ✅ **DynamoDB Integration** - Product catalog with stock level tracking

## Prerequisites

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed
* [Node.js 18+](https://nodejs.org/) installed
* [TypeScript](https://www.typescriptlang.org/) installed

## Deployment

1. Navigate to the pattern directory:
   ```bash
   cd lambda-durable-function-chaining-cdk
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Bootstrap CDK (if not already done):
   ```bash
   cdk bootstrap
   ```

4. Deploy the stack:
   ```bash
   cdk deploy
   ```

5. Note the `ProductCatalogTableName` from the outputs.

## Testing

### Step 1: Populate Product Catalog

Add test products to the DynamoDB table:

```bash
TABLE_NAME=$(aws cloudformation describe-stacks \
  --stack-name LambdaDurableFunctionChainingCdkStack \
  --query 'Stacks[0].Outputs[?OutputKey==`ProductCatalogTableName`].OutputValue' \
  --output text)

# Add sample products with pricing
aws dynamodb put-item \
  --table-name ${TABLE_NAME} \
  --item '{
    "productId": {"S": "LAPTOP-001"},
    "name": {"S": "Gaming Laptop"},
    "price": {"N": "1299.99"},
    "stockLevel": {"N": "50"},
    "warehouseLocation": {"S": "WAREHOUSE-A"}
  }'

aws dynamodb put-item \
  --table-name ${TABLE_NAME} \
  --item '{
    "productId": {"S": "MOUSE-001"},
    "name": {"S": "Wireless Mouse"},
    "price": {"N": "29.99"},
    "stockLevel": {"N": "200"},
    "warehouseLocation": {"S": "WAREHOUSE-A"}
  }'

aws dynamodb put-item \
  --table-name ${TABLE_NAME} \
  --item '{
    "productId": {"S": "KEYBOARD-001"},
    "name": {"S": "Mechanical Keyboard"},
    "price": {"N": "149.99"},
    "stockLevel": {"N": "20"},
    "warehouseLocation": {"S": "WAREHOUSE-B"}
  }'
```

### Step 2: Get Function Name

```bash
FUNCTION_NAME=$(aws cloudformation describe-stacks \
  --stack-name LambdaDurableFunctionChainingCdkStack \
  --query 'Stacks[0].Outputs[?OutputKey==`ValidateOrderFunctionName`].OutputValue' \
  --output text)

echo "Function Name: $FUNCTION_NAME"
```

### Step 3: Monitor Lambda Logs (Optional)

In a separate terminal, monitor the logs to see real-time execution:

```bash
FUNCTION_NAME=$(aws cloudformation describe-stacks \
  --stack-name LambdaDurableFunctionChainingCdkStack \
  --query 'Stacks[0].Outputs[?OutputKey==`ValidateOrderFunctionName`].OutputValue' \
  --output text)

aws logs tail /aws/lambda/${FUNCTION_NAME} --follow
```

Look for checkpoint and step execution messages showing the workflow progression through each step.

### Step 4: Test Order Processing

**Note**: Product pricing is retrieved from the database. Orders only need to specify productId and quantity.

**Test 1: Successful order**
```bash
aws lambda invoke \
  --function-name ${FUNCTION_NAME}:\$LATEST \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{
    "orderId": "ORDER-001",
    "customerId": "CUST-001",
    "items": [
      {
        "productId": "LAPTOP-001",
        "quantity": 1
      },
      {
        "productId": "MOUSE-001",
        "quantity": 2
      }
    ],
    "shippingAddress": "123 Main St, Seattle, WA 98101",
    "billingAddress": "123 Main St, Seattle, WA 98101",
    "paymentMethod": {
      "type": "credit",
      "cardNumber": 4532123456789012,
      "cardBrand": "Visa"
    }
  }' \
  response.json

echo "Order submitted asynchronously. Check logs for execution status."
```

**Test 2: Payment declined (10 laptops = $12,999.90, exceeds $10,000 limit)**
```bash
aws lambda invoke \
  --function-name ${FUNCTION_NAME}:\$LATEST \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{
    "orderId": "ORDER-002",
    "customerId": "CUST-002",
    "items": [
      {
        "productId": "LAPTOP-001",
        "quantity": 10
      }
    ],
    "shippingAddress": "456 Oak Ave, Portland, OR 97201",
    "billingAddress": "456 Oak Ave, Portland, OR 97201",
    "paymentMethod": {
      "type": "credit",
      "cardNumber": 5412345678901234,
      "cardBrand": "Mastercard"
    }
  }' \
  response.json

echo "Order submitted asynchronously. Check logs for execution status."
```

**Test 3: Insufficient inventory (60 keyboards, only 20 in stock)**
```bash
aws lambda invoke \
  --function-name ${FUNCTION_NAME}:\$LATEST \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{
    "orderId": "ORDER-003",
    "customerId": "CUST-003",
    "items": [
      {
        "productId": "KEYBOARD-001",
        "quantity": 60
      }
    ],
    "shippingAddress": "789 Pine Rd, Austin, TX 78701",
    "billingAddress": "789 Pine Rd, Austin, TX 78701",
    "paymentMethod": {
      "type": "debit",
      "cardNumber": 4111111111111111,
      "cardBrand": "Visa"
    }
  }' \
  response.json

echo "Order submitted asynchronously. Check logs for execution status."
```

**Test 4: Validation failure (empty items)**
```bash
aws lambda invoke \
  --function-name ${FUNCTION_NAME}:\$LATEST \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{
    "orderId": "ORDER-004",
    "customerId": "CUST-004",
    "items": [],
    "shippingAddress": "321 Elm St, Boston, MA 02101",
    "billingAddress": "321 Elm St, Boston, MA 02101",
    "paymentMethod": {
      "type": "credit",
      "cardNumber": 378282246310005,
      "cardBrand": "Amex"
    }
  }' \
  response.json

echo "Order submitted asynchronously. Check logs for execution status."
```

### Expected Test Results

- ✅ **Successful orders**: Complete all 4 steps and return full order details
- ✅ **Payment declined**: Fail at payment authorization step
- ✅ **Insufficient inventory**: Fail at inventory allocation step
- ✅ **Validation failures**: Reject immediately with error details
- ✅ **Checkpointing**: Function resumes from last checkpoint on retry

## How It Works

### Durable Execution with Function Chaining

The ValidateOrder function uses the Durable Execution SDK to orchestrate worker functions:

```typescript
import { DurableContext, withDurableExecution } from "@aws/durable-execution-sdk-js";

export const handler = withDurableExecution(async (event: Order, context: DurableContext) => {
  // Step 1: Validate order (inline)
  const validation = await context.step("validate-order", async () => {
    // Validation logic
  });

  // Step 2: Authorize payment (invoke worker function)
  const authorization = await context.step("authorize-payment", async () => {
    const response = await lambdaClient.send(
      new InvokeCommand({
        FunctionName: process.env.AUTHORIZE_PAYMENT_FUNCTION,
        Payload: JSON.stringify({ orderId, paymentMethod, amount })
      })
    );
    return JSON.parse(new TextDecoder().decode(response.Payload));
  });

  // Step 3: Allocate inventory (invoke worker function)
  const allocation = await context.step("allocate-inventory", async () => {
    // Invoke AllocateInventory function
  });

  // Step 4: Fulfill order (invoke worker function)
  const fulfillment = await context.step("fulfill-order", async () => {
    // Invoke FulfillOrder function
  });

  return { orderId, status: "completed", ... };
});
```

### Checkpoint Behavior

When the durable function executes:
1. Each context.step creates a checkpoint before execution
2. If interrupted, Lambda saves the checkpoint state
3. On retry, the function replays from the beginning
4. Completed steps are skipped using stored checkpoint results
5. Execution continues from the last incomplete step

### Worker Functions

**AuthorizePayment**: Simulates payment gateway authorization with amount limits

**AllocateInventory**: Queries DynamoDB for product availability and reserves inventory

**FulfillOrder**: Generates shipment details and tracking numbers

## Configuration

### Durable Execution Settings

The durable function is configured in the CDK stack:

```typescript
const validateOrderFunction = new nodejs.NodejsFunction(this, "ValidateOrderFunction", {
  runtime: lambda.Runtime.NODEJS_24_X,
  entry: path.join(__dirname, "functions", "validateOrder", "index.ts"),
  durableConfig: {
    executionTimeout: cdk.Duration.hours(1),
    retentionPeriod: cdk.Duration.days(7),
  },
});
```

- **executionTimeout**: 1 hour maximum workflow duration
- **retentionPeriod**: 7 days checkpoint retention

### IAM Permissions

The orchestrator function requires permissions to:
- Invoke worker Lambda functions
- Create and retrieve durable execution checkpoints

Worker functions require:
- DynamoDB read access (AllocateInventory)

## Customization

### Add More Workflow Steps

Add additional steps to the orchestrator:

```typescript
const notification = await context.step("send-notification", async () => {
  // Send order confirmation email
  return await sesClient.send(new SendEmailCommand({...}));
});
```

### Modify Validation Rules

Update validation logic in the validate-order step:

```typescript
const validation = await context.step("validate-order", async () => {
  const errors = [];
  
  // Add custom validation
  if (orderTotal < 10) {
    errors.push("Minimum order amount is $10");
  }
  
  return { isValid: errors.length === 0, errors };
});
```

### Integrate Real Payment Gateway

Replace mock payment logic with actual payment service:

```typescript
const authorization = await context.step("authorize-payment", async () => {
  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
  return await stripe.paymentIntents.create({
    amount: orderTotal * 100,
    currency: "usd",
    customer: customerId
  });
});
```

### Adjust Execution Timeout

Modify the durable configuration in the CDK stack:

```typescript
durableConfig: {
  executionTimeout: cdk.Duration.hours(24),  // 24 hours
  retentionPeriod: cdk.Duration.days(14),    // 14 days
}
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
- Function invocations

## Cleanup

Delete the stack:

```bash
cdk destroy
```

Or via AWS CLI:

```bash
aws cloudformation delete-stack --stack-name LambdaDurableFunctionChainingCdkStack
```

## Cost Considerations

- **Lambda**: Pay per invocation and execution time
- **DynamoDB**: On-demand pricing for product catalog reads
- **Durable Execution**: Checkpoint storage costs (minimal)
- **No charges during wait states**: Function suspended between steps

## Learn More

- [Lambda Durable Functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Durable Execution SDK (JavaScript)](https://github.com/aws/aws-durable-execution-sdk-js)
- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [Function Chaining Pattern](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions-patterns.html)

---

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
