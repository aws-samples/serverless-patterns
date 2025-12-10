# Lambda durable functions on Lambda Managed Instances

This pattern demonstrates how to implement Lambda durable functions running on Lambda Managed Instances using AWS CDK. Lambda durable functions allow Lambda functions to maintain state and execution context across multiple invocations, while Lambda Managed Instances provide predictable performance and reduced cold starts.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-managed-instances-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

**Note**: Lambda Managed Instances provision EC2 instances that are **NOT eligible for the AWS Free Tier**. These instances will incur charges immediately upon deployment, regardless of your Free Tier status.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) installed and configured
* [Node.js](https://nodejs.org/) (version 24.x or later)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-durable-managed-instances-cdk
    ```
1. Install the project dependencies:
    ```
    npm install
    ```
1. Build the project:
    ```
    npm run build
    ```
1. Deploy the CDK stack:
    ```
    npx cdk deploy
    ```
    Note: This stack is currently configured to deploy to the `us-east-2` region. Please refer to the [AWS capabilities explorer](https://builder.aws.com/build/capabilities/explore) for feature availability in your desired region.

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern demonstrates the integration of two key Lambda features:

### Lambda durable functions
[Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) enable Lambda functions to maintain state and execution context across multiple invocations. This allows for:
- Long-running workflows that can span multiple function invocations
- State persistence between executions
- Improved reliability for complex processing tasks
- Better handling of timeouts and retries

### Lambda Managed Instances
[Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) provide:
- Predictable performance with pre-warmed execution environments
- Reduced cold start latency
- Consistent execution characteristics
- Better resource utilization for frequently invoked functions

The combination of these features allows for building robust, stateful serverless applications that can handle complex workflows while maintaining high performance and reliability.

## Testing

After deployment, you can test the Lambda durable function using the provided test script, AWS CLI, or AWS Console.

### Automated Testing Script

The pattern includes a comprehensive test script that demonstrates all aspects of durable function execution:

1. **Make the test script executable and run it**:
   ```bash
   chmod +x test-lambda.sh
   ./test-lambda.sh [profile] [region]
   ```
   
   Examples:
   ```bash
   # Using default AWS profile and region
   ./test-lambda.sh
   
   # Using specific profile and region
   ./test-lambda.sh my-profile us-west-2
   ```

2. **What the script does**:
   - Invokes the function asynchronously with a test payload
   - Extracts the durable execution ARN from the response
   - Shows real-time execution history with step details
   - Displays CloudWatch logs with execution flow
   - Retrieves the final execution result with input/output JSON
   - Provides helpful CLI commands for manual inspection

3. **Script output includes**:
   - Function invocation status and durable execution ARN
   - Step-by-step execution history showing the step-wait-step pattern
   - Detailed logs with business logic tracing
   - Final execution result with timestamps and processed data

### Manual AWS CLI Testing

#### Basic Function Invocation

1. **Synchronous invocation** (for immediate response):
   ```bash
   aws lambda invoke \
     --function-name step-wait-step-durable-function \
     --payload file://events/basic-order.json \
     --cli-binary-format raw-in-base64-out \
     --region us-east-2 \
     response.json
   ```

2. **Asynchronous invocation** (recommended for durable functions):
   ```bash
   aws lambda invoke \
     --function-name step-wait-step-durable-function:$LATEST.PUBLISHED \
     --invocation-type Event \
     --payload file://events/basic-order.json \
     --cli-binary-format raw-in-base64-out \
     --region us-east-2 \
     response.json
   ```

#### Monitoring Durable Execution

After invoking the function asynchronously, you'll receive a durable execution ARN. Use these commands to monitor the execution:

1. **Get execution details and result**:
   ```bash
   aws lambda get-durable-execution \
     --durable-execution-arn "YOUR_EXECUTION_ARN" \
     --region us-east-2
   ```

2. **View execution history** (step-by-step flow):
   ```bash
   aws lambda get-durable-execution-history \
     --durable-execution-arn "YOUR_EXECUTION_ARN" \
     --region us-east-2
   ```

3. **List all executions for the function**:
   ```bash
   aws lambda list-durable-executions-by-function \
     --function-name step-wait-step-durable-function \
     --region us-east-2
   ```

4. **View CloudWatch logs**:
   ```bash
   aws logs filter-log-events \
     --log-group-name /aws/lambda/step-wait-step-durable-function \
     --start-time $(date -d '5 minutes ago' +%s)000 \
     --region us-east-2 \
     --filter-pattern 'INFO'
   ```

### AWS Console Testing

1. Navigate to the Lambda service in the AWS Console
2. Find the function named `step-wait-step-durable-function`
3. Create a test event using the payload from `events/basic-order.json` or create a custom payload with:
   ```json
   {
     "orderId": "your-test-order-id"
   }
   ```
4. Execute the test and observe the results in the execution logs

### Expected Behavior

The function demonstrates the **step-wait-step pattern** with durable execution:

1. **Step 1 - Validate Order**: 
   - Processes the input order ID
   - Returns validation status with timestamp
   - Logs: "Validating order [orderId]"

2. **Wait Phase - 5 Second Delay**:
   - Durable wait without consuming execution time
   - Function execution pauses and resumes automatically
   - Logs: "Order validated, waiting 5 seconds before processing"

3. **Step 2 - Process Order**:
   - Final processing with completion timestamp
   - Returns processed order with both validation and processing timestamps
   - Logs: "Processing order [orderId]" and "Step-wait-step execution completed"

### Sample Output

**Execution History** shows the durable execution flow:
```
ExecutionStarted → StepStarted (validate-order) → StepSucceeded → 
WaitStarted (wait 5s) → WaitSucceeded → StepStarted (process-order) → 
StepSucceeded → ExecutionSucceeded
```

**Final Result** contains the processed order data:
```json
{
  "orderId": "order-123",
  "status": "processed", 
  "validatedAt": 1765404928643,
  "processedAt": 1765404934023
}
```

### Monitoring and Observability

Monitor the execution through multiple channels:
- **CloudWatch Logs**: Detailed execution flow and business logic tracing
- **Durable Execution History**: Step-by-step execution events with timestamps
- **Lambda Metrics**: Function performance and invocation statistics
- **Execution State**: Real-time status and result data via AWS CLI

## Regional Availability

This stack is configured to deploy to the `us-east-2` region. Before deploying to a different region, please verify that both Lambda durable functions and Lambda Managed Instances features are available in your target region by using the [AWS capabilities explorer](https://builder.aws.com/build/capabilities/explore) or consulting the official AWS documentation:

- [Lambda durable functions documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Lambda Managed Instances documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html)

## Cleanup
 
1. Delete the stack
    ```bash
    npx cdk destroy
    ```
1. Confirm the stack has been deleted by checking the AWS CloudFormation console or running:
    ```bash
    aws cloudformation describe-stacks --stack-name lambda-durable-functions-managed-instances --region us-east-2
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0