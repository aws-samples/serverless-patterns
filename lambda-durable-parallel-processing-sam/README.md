# Parallel Processing with AWS Lambda Durable Functions

This pattern demonstrates parallel processing using AWS Lambda Durable Functions to execute multiple independent validation operations concurrently. The workflow processes orders by running inventory checks, payment validation, shipping calculations, and tax calculations in parallel, significantly reducing total processing time.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-parallel-processing-sam

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Node.js 22.x](https://nodejs.org/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change directory to the pattern directory:
    ```bash
    cd lambda-durable-parallel-processing-sam
    ```

3. Install dependencies:
    ```bash
    cd src/orchestrator && npm install && cd ../..
    ```

4. From the command line, use AWS SAM to build the application:
    ```bash
    sam build
    ```

5. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```bash
    sam deploy --guided
    ```

6. During the prompts:
    * Enter a stack name
    * Enter your preferred AWS Region (Lambda Durable Functions is available in multiple regions)
    * Allow SAM CLI to create IAM roles with the required permissions (CAPABILITY_IAM and CAPABILITY_NAMED_IAM).
    * Keep default values for other parameters

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

7. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern uses AWS Lambda Durable Functions to orchestrate parallel execution of multiple worker functions:

### Architecture

The solution consists of five Lambda functions:

**Orchestrator (Durable Function)**
- Coordinates the entire workflow with automatic checkpointing
- Executes four worker functions in parallel using `context.parallel()`
- Aggregates results and validates all responses
- Calculates final totals and confirms the order

**Worker Functions (Non-Durable)**
1. **Inventory Check** - Validates product availability and reserves stock
2. **Payment Validation** - Validates payment method and authorizes transaction
3. **Shipping Calculation** - Calculates shipping costs and delivery estimates
4. **Tax Calculation** - Computes taxes based on customer location

### Workflow Steps

1. **Validate Input** (checkpointed) - Validates order data and customer information
2. **Calculate Subtotal** (checkpointed) - Sums up item prices
3. **Parallel Execution** (checkpointed) - Runs all four workers concurrently:
   - Inventory Check
   - Payment Validation
   - Shipping Calculation
   - Tax Calculation
4. **Validate Results** (checkpointed) - Checks all worker responses for success
5. **Calculate Totals** (checkpointed) - Computes final order total
6. **Durable Wait** - Waits 1 second (no compute charges)
7. **Finalize Order** (checkpointed) - Confirms order and returns result

### Performance Benefits

**Sequential Execution** (hypothetical):
- Inventory: 150ms
- Payment: 200ms
- Shipping: 125ms
- Tax: 100ms
- **Total: 575ms**

**Parallel Execution** (actual):
- All workers: ~200ms (longest worker)
- **Total: ~200ms**
- **Speedup: 2.9x faster**

### Key Features

- ✅ **Parallel Processing** - Execute multiple operations concurrently using `context.parallel()`
- ✅ **Automatic Checkpointing** - Each step is checkpointed automatically
- ✅ **Failure Recovery** - Resumes from last checkpoint on failure
- ✅ **Child Context Pattern** - Each parallel task uses its own child context for isolated checkpoint management
- ✅ **Result Aggregation** - Collects and validates all parallel results (returns object with `all` array)
- ✅ **Structured Logging** - JSON-formatted logs with correlation IDs
- ✅ **Error Handling** - Comprehensive validation and error reporting

### Important Implementation Details

**Parallel Execution Return Format:**

The `context.parallel()` method returns an object with an `all` property containing an array of results:

```javascript
const parallelResults = await context.parallel([...tasks]);
// Returns: { 
//   all: [{result: ..., index: 0, status: "SUCCEEDED"}, ...], 
//   completionReason: "ALL_COMPLETED" 
// }

// Extract results
const results = parallelResults.all.map(item => item.result);
const [inventoryResult, paymentResult, shippingResult, taxResult] = results;
```

**Child Context Usage:**

Each parallel task receives a child context parameter that must be used instead of the parent context:

```javascript
await context.parallel([
  async (childCtx) => {
    return await childCtx.step('task-name', async () => {
      // Task logic here
    });
  }
]);
```

## Testing

### Test 1: Successful Order Processing

Create a test payload file:

```bash
cat > test-order.json << 'EOF'
{
  "orderId": "ORD-12345",
  "items": [
    {"productId": "PROD-001", "quantity": 2, "price": 29.99},
    {"productId": "PROD-002", "quantity": 1, "price": 49.99}
  ],
  "customer": {
    "id": "CUST-789",
    "address": {"state": "CA", "zipCode": "94102"},
    "paymentMethod": "credit_card"
  }
}
EOF
```

Invoke the function:

```bash
aws lambda invoke \
  --function-name STACK_NAME-ParallelProcessor:prod \
  --payload file://test-order.json \
  --cli-binary-format raw-in-base64-out \
  response.json

cat response.json | jq .
```

Expected response:

```json
{
  "success": true,
  "orderId": "ORD-12345",
  "result": {
    "orderId": "ORD-12345",
    "status": "CONFIRMED",
    "inventory": {
      "available": true,
      "reservationId": "RES-1707423456789-abc123def"
    },
    "payment": {
      "valid": true,
      "authorizationCode": "AUTH-1707423456789-XYZ789ABC"
    },
    "shipping": {
      "cost": 12.74,
      "estimatedDays": 2,
      "carrier": "USPS"
    },
    "tax": {
      "amount": 7.97,
      "rate": 0.0725,
      "jurisdiction": "CA State Tax"
    },
    "totals": {
      "subtotal": 109.97,
      "shipping": 12.74,
      "tax": 7.97,
      "total": 130.68,
      "currency": "USD"
    }
  },
  "message": "Order processed successfully with parallel execution",
  "processingTimeMs": 1234
}
```

### Test 2: Different State (Different Tax Rate)

Test with New York (4% tax rate):

```bash
cat > test-ny.json << 'EOF'
{
  "orderId": "ORD-NY-001",
  "items": [{"productId": "PROD-001", "quantity": 1, "price": 100.00}],
  "customer": {
    "id": "CUST-NY-123",
    "address": {"state": "NY", "zipCode": "10001"},
    "paymentMethod": "credit_card"
  }
}
EOF

aws lambda invoke \
  --function-name STACK_NAME-ParallelProcessor:prod \
  --payload file://test-ny.json \
  --cli-binary-format raw-in-base64-out \
  response-ny.json

cat response-ny.json | jq .
```

### Test 3: Multiple Items

Test with bulk order:

```bash
cat > test-bulk.json << 'EOF'
{
  "orderId": "ORD-BULK-001",
  "items": [
    {"productId": "PROD-001", "quantity": 5, "price": 29.99},
    {"productId": "PROD-002", "quantity": 3, "price": 49.99},
    {"productId": "PROD-003", "quantity": 2, "price": 19.99}
  ],
  "customer": {
    "id": "CUST-456",
    "address": {"state": "TX", "zipCode": "75001"},
    "paymentMethod": "credit_card"
  }
}
EOF

aws lambda invoke \
  --function-name STACK_NAME-ParallelProcessor:prod \
  --payload file://test-bulk.json \
  --cli-binary-format raw-in-base64-out \
  response-bulk.json

cat response-bulk.json | jq .
```

### Test 4: Invalid Input (Missing Required Fields)

Test validation error handling:

```bash
cat > test-invalid.json << 'EOF'
{
  "orderId": "ORD-INVALID",
  "items": [],
  "customer": {"id": "CUST-999"}
}
EOF

aws lambda invoke \
  --function-name STACK_NAME-ParallelProcessor:prod \
  --payload file://test-invalid.json \
  --cli-binary-format raw-in-base64-out \
  response-invalid.json

cat response-invalid.json | jq .
```

Expected error response:

```json
{
  "success": false,
  "error": {
    "name": "ValidationError",
    "message": "items array is required and must not be empty",
    "field": "items"
  },
  "message": "Order processing failed"
}
```

### Monitor Logs

View real-time logs to see parallel execution:

```bash
# Get function name
FUNCTION_NAME=$(aws cloudformation describe-stack-resources \
  --stack-name STACK_NAME \
  --query 'StackResources[?LogicalResourceId==`ParallelProcessorFunction`].PhysicalResourceId' \
  --output text)

# Tail logs
aws logs tail /aws/lambda/${FUNCTION_NAME} \
  --follow \
  --format short
```

Look for parallel execution messages:
```
Starting parallel worker execution
Invoking InventoryCheck worker
Invoking PaymentValidation worker
Invoking ShippingCalculation worker
Invoking TaxCalculation worker
Parallel execution completed
```

## Cleanup

1. Delete the stack:
    ```bash
    sam delete
    ```

2. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks \
      --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

## Documentation

- [Lambda Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Durable Execution SDK for JavaScript](https://github.com/aws/aws-durable-execution-sdk-js)
- [Parallel Processing Patterns](https://docs.aws.amazon.com/lambda/latest/dg/durable-parallel.html)
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)

---

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
