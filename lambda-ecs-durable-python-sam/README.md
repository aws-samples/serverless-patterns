# Lambda Durable Functions to Amazon ECS with Python

This pattern demonstrates how to invoke Amazon ECS tasks from AWS Lambda durable functions using Python. The workflow starts an ECS task, waits for a callback, and resumes based on the task result while maintaining state across the pause/resume cycle.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-ecs-python-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Docker](https://docs.docker.com/get-docker/) installed (for building Lambda container images)
* [Python 3.13](https://www.python.org/downloads/) or later

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-ecs-python-sam
    ```
1. From the command line, use AWS SAM to build the application:
    ```
    sam build
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the VpcCIDR parameter (default: 10.0.0.0/16)
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Create managed ECR repositories for all functions (required for container images)

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern implements an ECS task orchestration workflow using Lambda durable functions with callback pattern:

1. **Sync Lambda** starts an ECS task and polls for completion using durable waits (no compute charges during waits)
2. **Callback Lambda** starts an ECS task, pauses execution using `callback.result()`, and waits for a callback
3. The ECS task processes work and calls Lambda durable execution callback API when complete
4. The Lambda function resumes automatically when the callback is invoked and returns the result

The pattern uses the AWS Durable Execution SDK for Python with the `@durable_execution` decorator to maintain state across the pause/resume cycle. The callback pattern ensures no compute charges while waiting for ECS task completion.

### Architecture Components

- **Sync Lambda**: Orchestrates ECS tasks using Lambda durable functions SDK with polling pattern and durable waits
- **Callback Lambda**: Orchestrates ECS tasks using Lambda durable functions SDK with callback pattern
- **ECS Tasks**: Process work and send callbacks to Lambda using durable execution callback APIs
- **VPC and Networking**: Provides network connectivity for ECS tasks to pull Docker images and call AWS APIs
- **CloudWatch Logs**: Stores execution logs for Lambda functions and ECS tasks

## Testing

### Set Environment Variables

```bash
export AWS_DEFAULT_REGION=us-east-1
export STACK_NAME=<your-stack-name>

# Get function names from CloudFormation outputs
export SYNC_FUNCTION=$(aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --query 'Stacks[0].Outputs[?OutputKey==`SyncLambdaFunctionArn`].OutputValue' \
  --output text | awk -F: '{print $NF}')

export CALLBACK_FUNCTION=$(aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --query 'Stacks[0].Outputs[?OutputKey==`CallbackLambdaFunctionArn`].OutputValue' \
  --output text | awk -F: '{print $NF}')
```

### Test Synchronous Pattern

```bash
# Invoke the sync function (must use qualified ARN with :$LATEST)
aws lambda invoke \
  --function-name $SYNC_FUNCTION:\$LATEST \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{"message": "Hello from sync pattern", "processingTime": 10}' \
  response.json

# Monitor Lambda logs
aws logs tail /aws/lambda/$SYNC_FUNCTION --follow

# Monitor ECS task logs
aws logs tail /ecs/$STACK_NAME --follow
```

### Test Callback Pattern

```bash
# Invoke the callback function (must use qualified ARN with :$LATEST)
aws lambda invoke \
  --function-name $CALLBACK_FUNCTION:\$LATEST \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{"message": "Hello from callback pattern", "processingTime": 30}' \
  response.json

# Monitor Lambda logs
aws logs tail /aws/lambda/$CALLBACK_FUNCTION --follow

# Monitor ECS task logs
aws logs tail /ecs/$STACK_NAME --follow
```

Expected output: The Lambda function should complete and return the ECS task result. The logs should show the callback being received and the function resuming execution.

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'$STACK_NAME')].StackStatus"
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
