# S3 to StepFunctions with EventBridge Rule

This pattern demonstrates how to create an EventBridge rule with S3 as the event source and Step Functions as target. Implemented with CDK.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-eventbridge-sfn-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd s3-eventbridge-sfn-cdk/src
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
7. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/s3-eventbridge-sfn-stack`
   ```
   cdk deploy
   ```
8. The CDK template successfully creates a new S3 bucket, a StepFunction state machine and an EventBridge rule targeting the state machine for the `Object Created` event.

9. Note the outputs from the CDK deployment process. This contains the S3 bucket name.

## How it works

- Upload a file to the newly created S3 bucket
- This will send an `Object Created` event to EventBridge
- Based on the EventBridge rule, the state machine is executed

## Testing

1. Navidate to AWS console and go to the S3 bucket that was created by this CDK template

2. Upload a file to the S3 bucket

3. Immediately after the upload is completed successfully, navigate to the Step Functions state machine, you will see an execution has been triggered

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

## Documentations and next step

To create a full Step Functions workflow with the pattern created, you can find out example workflows at Step Functions Workflow: https://serverlessland.com/workflows

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
