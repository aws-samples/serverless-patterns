# AWS Lambda durable functions with Node.js

This pattern demonstrates AWS Lambda durable functions using Node.js to build resilient, long-running workflows that can execute for up to one year.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-durable-functions-nodejs-sam](https://serverlessland.com/patterns/lambda-durable-functions-nodejs-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-durable-functions-nodejs-sam
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region (must support Lambda durable functions)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern demonstrates AWS Lambda durable functions using Node.js. It implements a simple order processing workflow with automatic checkpointing, durable waits, and fault tolerance.

The orchestrator function uses the `@aws/durable-execution-sdk-js` to implement:
- Checkpointed steps with `context.step()`
- Durable waits with `context.wait()`
- Automatic recovery from failures
- Structured JSON logging

The workflow:
1. Validates input (checkpointed)
2. Executes enrichment step (checkpointed) by invoking the OrderEnricher Lambda
3. Waits 5 seconds (durable wait - no compute charges)
4. Executes finalization step (checkpointed)
5. Returns result

## Architecture

This demo includes two Lambda functions:

1. **DurableOrderProcessor** (Orchestrator) — Uses `@aws/durable-execution-sdk-js` for durable execution. Orchestrates the workflow with checkpointed steps and durable waits.

2. **OrderEnricher** (Worker) — Simple Lambda function (non-durable) that enriches order data with customer information. Called by the orchestrator.

## Testing

After deployment, use the test command from the stack outputs to invoke the durable function:

```bash
# Get the test command from stack outputs
aws cloudformation describe-stacks \
  --stack-name STACK_NAME \
  --query 'Stacks[0].Outputs[?OutputKey==`TestCommand`].OutputValue' \
  --output text
```

Run the output command to invoke the function. Alternatively, you can copy the `TestCommand` value directly from the `sam deploy` output.

### View Logs

```bash
# View orchestrator logs
aws logs tail /aws/lambda/STACK_NAME-DurableOrderProcessor --follow

# View enricher logs
aws logs tail /aws/lambda/STACK_NAME-OrderEnricher --follow
```

## Expected Output

Successful execution returns:

```json
{
  "success": true,
  "orderId": "ORDER-123",
  "enrichmentResult": {
    "statusCode": 200,
    "orderId": "ORDER-123",
    "enrichedData": {
      "customerId": "CUST-XXXX",
      "timestamp": "2026-02-08T20:58:24.548Z"
    }
  },
  "finalResult": {
    "orderId": "ORDER-123",
    "status": "COMPLETED",
    "enrichedData": { ... },
    "finalizedAt": "2026-02-08T20:58:26.859Z",
    "message": "Order finalized successfully"
  },
  "message": "Order processed successfully with durable execution",
  "processedAt": "2026-02-08T20:58:26.954Z"
}
```

## Observing Durable Execution

Check CloudWatch Logs to see the durable execution in action:

1. **First Invocation**: Executes enrichment step, hits wait, suspends
2. **Second Invocation** (~2 seconds later): Resumes from checkpoint, skips enrichment (uses stored result), completes finalization

You'll notice:
- Multiple Lambda invocations for a single workflow
- Enrichment step result is reused (not re-executed)
- Total execution time includes the 2-second wait, but you only pay for active compute time

## Cleanup

To remove all resources:

```bash
sam delete --stack-name STACK_NAME
```

## Additional Information

### Supported Runtimes

AWS Lambda durable functions are available only in selected runtimes. Check the [Supported runtimes for durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-supported-runtimes.html) page for the latest availability.

### Troubleshooting

**"InvalidParameterValueException: You cannot invoke a durable function using an unqualified ARN"**
- Solution: Always use a qualified ARN (with version or alias). This template automatically creates a `prod` alias.

**"Cannot find module '@aws/durable-execution-sdk-js'"**
- Solution: Ensure dependencies are installed. SAM CLI automatically runs `npm install` during build.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
