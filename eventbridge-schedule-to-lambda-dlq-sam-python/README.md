# Amazon EventBridge Scheduler to AWS Lambda with Dual Dead Letter Queues

This pattern demonstrates how to use Amazon EventBridge Scheduler to invoke AWS Lambda functions with comprehensive failure handling through dual Dead Letter Queues (DLQs). The pattern is deployed using the AWS Serverless Application Model (SAM).

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns](https://serverlessland.com/patterns)

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
    cd eventbridge-schedule-to-lambda-dlq-sam-python
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern showcases EventBridge Scheduler's robust failure handling capabilities through two distinct failure paths:

### Dual Dead Letter Queue Architecture

**Lambda Execution DLQ**: Captures failures that occur during Lambda function execution (code errors, timeouts, out-of-memory errors). After Lambda's built-in async retry mechanism exhausts its attempts (default: 2 retries), failed events are sent to this queue.

**EventBridge Scheduler DLQ**: Captures failures that occur at the invocation level before the Lambda function executes. This includes:
- IAM permission errors (scheduler role lacks lambda:InvokeFunction permission)
- Lambda service throttling (concurrent execution limits reached)
- Lambda function state issues (function being deleted, doesn't exist, invalid ARN)
- Resource not found errors (function deleted after schedule creation)
- Maximum event age exceeded (event couldn't be delivered within configured time window)
- Maximum retry attempts exhausted (all scheduler retries failed)

### Workflow

1. EventBridge Scheduler invokes the Lambda function asynchronously every 5 minutes
2. If invocation fails (permissions, throttling, etc.), EventBridge Scheduler retries up to 3 times
3. After scheduler retries are exhausted, the event is sent to the EventBridge Scheduler DLQ
4. If invocation succeeds but execution fails (code error), Lambda retries automatically
5. After Lambda retries are exhausted, the event is sent to the Lambda Execution DLQ

This dual DLQ architecture provides complete visibility into both configuration-level and code-level failures, enabling appropriate remediation strategies for each failure type.

## Testing

### Test Normal Execution

The function runs automatically every 5 minutes. View the logs:

```bash
# Get function name from stack outputs
FUNCTION_NAME=$(aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query 'Stacks[0].Outputs[?OutputKey==`ScheduledFunctionName`].OutputValue' \
  --output text)

# Tail logs
aws logs tail /aws/lambda/${FUNCTION_NAME} --follow
```

### Test Lambda Execution Failure

Enable failure simulation to test the Lambda Execution DLQ:

```bash
# Update function to simulate failures
aws lambda update-function-configuration \
  --function-name ${FUNCTION_NAME} \
  --environment 'Variables={LOG_LEVEL=INFO,SIMULATE_FAILURE=true}'
```

Wait up to 5 minutes for the next scheduled execution. After Lambda retries are exhausted, check the Lambda Execution DLQ:

```bash
LAMBDA_DLQ_URL=$(aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query 'Stacks[0].Outputs[?OutputKey==`LambdaExecutionDLQUrl`].OutputValue' \
  --output text)

aws sqs receive-message --queue-url ${LAMBDA_DLQ_URL}
```

Disable failure simulation:

```bash
aws lambda update-function-configuration \
  --function-name ${FUNCTION_NAME} \
  --environment 'Variables={LOG_LEVEL=INFO,SIMULATE_FAILURE=false}'
```

### Test EventBridge Scheduler Invocation Failure

Remove Lambda invoke permission to test the EventBridge Scheduler DLQ:

```bash
# Get schedule name
SCHEDULE_NAME=$(aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query 'Stacks[0].Outputs[?OutputKey==`ScheduleName`].OutputValue' \
  --output text)

# Get scheduler role name
SCHEDULER_ROLE=$(aws cloudformation describe-stack-resources \
  --stack-name <your-stack-name> \
  --logical-resource-id SchedulerRole \
  --query 'StackResources[0].PhysicalResourceId' \
  --output text)

# Remove Lambda invoke permission
aws iam delete-role-policy \
  --role-name ${SCHEDULER_ROLE} \
  --policy-name InvokeLambda
```

Wait up to 5 minutes for the next scheduled execution. After scheduler retries are exhausted, check the Scheduler DLQ:

```bash
SCHEDULER_DLQ_URL=$(aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query 'Stacks[0].Outputs[?OutputKey==`SchedulerDLQUrl`].OutputValue' \
  --output text)

aws sqs receive-message --queue-url ${SCHEDULER_DLQ_URL}
```

Restore permissions by redeploying:

```bash
sam deploy
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name <your-stack-name>
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'<your-stack-name>')].StackStatus"
    ```
----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
