# Amazon SQS to AWS Lambda

The CDK template deploys a Lambda function, an SQS queue and the IAM permissions required to run the application. SQS invokes the Lambda function when new messages are available.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/sql-lambda-cdk](https://serverlessland.com/patterns/sqs-lambda-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (AWS CDK) installed and account bootstrapped

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/sqs-lambda-cdk/cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. From the command line, configure AWS CDK:
    ```
    cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
    cdk bootstrap 1111111111/us-east-1
    cdk bootstrap --profile test 1111111111/us-east-1
    ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the lib/cdk-stack.ts file:
    ```
    cdk deploy
    ```
6. Note the outputs from the CDK deployment process. This contains the Lambda function Name and the SQS Queue URL which is used for testing.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SQS queue and observe the event delivered to the Lambda function:

1. Send the SQS message:
```bash
aws sqs send-message --queue-url ENTER_YOUR_SQS_QUEUE_URL --message-body "Test message"
```
2. Retrieve the logs from the Lambda function:
```bash
aws logs describe-log-streams --log-group-name '/aws/lambda/<LAMBDA_FUNCTION_NAME>' | jq '.logStreams[0].logStreamName'
aws logs get-log-events --log-group-name '/aws/lambda/<LAMBDA_FUNCTION_NAME>' --log-stream-name 'LOGSTREAM_NAME_FROM_ABOVE_OUTPUT'
```


## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
