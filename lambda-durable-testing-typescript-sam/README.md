# Testing AWS Lambda durable functions in TypeScript

This pattern demonstrates comprehensive testing strategies for AWS Lambda durable functions using the Durable Execution SDK testing library. It covers local testing, cloud integration testing, and best practices for testing long-running workflows.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-testing-typescript-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Node.js 24+](https://nodejs.org/en/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd lambda-durable-testing-typescript-sam
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Run the test suite locally (no AWS credentials required):
    ```
    npm test
    ```
5. From the command line, use AWS SAM to build and deploy the AWS resources:
    ```
    sam build
    sam deploy --guided
    ```
6. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

7. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern demonstrates five key testing scenarios for durable functions:

### 1. Basic Workflow Testing (Order Processor)
Tests simple step operations and wait operations with time-skipping enabled for instant execution.

### 2. Retry Logic Testing (Payment Processor)
Validates retry strategies, failure scenarios, and exhausting retry attempts with mocked external API calls.

### 3. Callback Testing (Approval Workflow)
Demonstrates testing external event integration patterns, including callback sending and timeout handling.

### 4. Parallel Operations Testing (Batch Processor)
Shows how to test concurrent execution patterns with independent operation tracking and result aggregation.

### 5. Nested Functions Testing (Main + Child Workflow)
Validates function composition and orchestration using function invocation and registration.

## Testing

### Local Testing (No AWS Required)

Run all local tests:
```bash
npm test
```

Run tests in watch mode:
```bash
npm run test:watch
```

Run tests with coverage:
```bash
npm run test:coverage
```

### Cloud Integration Testing

After deployment, update the function names in `tests/cloud/` files with your deployed function names, then run:

```bash
npm run test:cloud
```

Run all tests (local + cloud):
```bash
npm run test:all
```

## Example Test Output

```
PASS  tests/order-processor.test.ts
  Order Processor
    ✓ should process order successfully (45ms)
    ✓ should execute operations in correct order (32ms)

PASS  tests/payment-processor.test.ts
  Payment Processor
    ✓ should succeed on first attempt (28ms)
    ✓ should retry on failure (41ms)
    ✓ should exhaust retries (55ms)

PASS  tests/approval-workflow.test.ts
  Approval Workflow
    ✓ should timeout when no approval is received (38ms)

PASS  tests/batch-processor.test.ts
  Batch Processor
    ✓ should process items in parallel (52ms)

PASS  tests/main-workflow.test.ts
  Main Workflow
    ✓ should invoke child workflow (44ms)

Test Suites: 5 passed, 5 total
Tests:       8 passed, 8 total
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

## Key Testing Patterns

This pattern demonstrates these essential testing practices:

1. **Setup/Teardown**: Use `beforeAll` and `afterAll` for test environment configuration
2. **Skip Time**: Enable `skipTime: true` for instant test execution without waiting
3. **Operation Inspection**: Use `getOperation()` and `getOperationByIndex()` to verify execution flow
4. **Mock External Dependencies**: Mock fetch and other external calls with Jest
5. **Callback Simulation**: Use `getOperation().sendCallback()` for testing callbacks
6. **Function Registration**: Use `registerDurableFunction()` for nested workflows

## Best Practices

✅ **DO:**
- Use `LocalDurableTestRunner` for fast local tests
- Enable `skipTime: true` to skip waits instantly
- Mock external API calls with Jest
- Test both success and failure scenarios
- Inspect operations to verify execution flow

❌ **DON'T:**
- Run tests against real AWS services in unit tests
- Wait for actual timeouts in tests
- Skip testing error handling
- Forget to test retry logic

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
