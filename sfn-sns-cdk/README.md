# AWS Step Functions to Amazon SNS

The Step Functions state machine can be started using the AWS CLI or from another service (e.g. API Gateway) to run the workflow and return the result.

This CDK code deploys a Step Functions workflow that converts milliseconds to second, wait for the time passed to it and then finally sends a message to Amazon SNS. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-sns-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns && cd serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd sfn-sns-cdk/src
   ```
3. Install dependencies:
   ```
   npm install
   ```
4. This project uses typescript as client language for AWS CDK. Run the given command to compile typescript to javascript
   ```
   npm run build
   ```
5. From the command line, configure AWS CDK (if you had not done it):
   ```
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 1111111111/us-east-1
   cdk bootstrap --profile test 1111111111/us-east-1
   ```
6. Synthesize CloudFormation template from the AWS CDK app
   ```
   cdk synth
   ```
7. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/sfn-sns-cdk-stack`
   ```
   cdk deploy
   ```
8. The CDK template successfully creates a lambda function (to convert from millisecond to second) a SNS Topic and a Step Functions state machine .

9. Note the outputs from the CDK deployment process. It contains the ARN of Step Functions state machine ARN and SNS Topic ARN.

## How it works

* Step Functions receive an execution using the `start-execution` api command with the the message {"waitMilliseconds" : <time-in-milliseconds>} in the input payload.
* The state machine will first call Lambda function to convert milliseconds to seconds.
* The state machine will enter "Wait" state and wait for the time passed to it during execution 
* After waiting, Step Functions will send a message by the time it waited to the SNS topic.

## Testing

1. Subscribe your email address to the SNS topic:
    ```bash
    aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS
    ```
1. Click the confirmation link delivered to your email to verify the endpoint.

1. Start Step Functions execution with the command:
    ```bash
    aws stepfunctions start-execution --name "test" --state-machine-arn ENTER_YOUR_STATE_MACHINE_ARN --input  {\"waitMilliseconds\":5000}
    ```
1. The notification message is delivered to your email address.

## Cleanup


1. Delete the stack
   ```bash
   cdk destroy
   ```
---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0