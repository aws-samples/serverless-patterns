# SQS to Step Functions Workflow using EventBridge Pipes

This pattern demonstrates sending SQS messages directly to a Step Functions workflow using EventBridge Pipes.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/eventbridge-pipes-sqs-to-step-functions-cdk-dotnet/cdk
   ```

3. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 1111111111/us-east-1
   cdk bootstrap --profile test 1111111111/us-east-1
   ```
4. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```

## How it works

The template will create an SQS queue, StepFunction workflow and pipe. Sending messages to the SQS queue will trigger the pipe to start a new execution of the Step Functions workflow.

Send SQS message that will start a Step Function execution

```sh
 # Send SQS message to be sent to EventBridge using the filter.
 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"orderId":"125a2e1e-d420-482e-8008-5a606f4b2076, "customerId": "a48516db-66aa-4dbc-bb66-a7f058c5ec24", "type": "NEW"}'
```

## Delete stack

```bash
cdk destroy
```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
