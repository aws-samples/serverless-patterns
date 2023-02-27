# EventBridge Pipes Splitter Pattern using DynamoDB and EventBridge as an example.

![Splitter Architecture using Pipes](./architecture.png)

This pattern demonstrates the [splitter pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Sequencer.html), takes an event from DynamoDB and splits the event into many events directly into EventBridge.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-splitter-pattern

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
   cd serverless-patterns/eventbridge-pipes-splitter-pattern/cdk
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 1111111111/us-east-1
   cdk bootstrap --profile test 1111111111/us-east-1
   ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   npm run build && cdk deploy
   ```

## How it works

This pattern with create a DDB table and EventBridge pipe to split the event into three events for EventBridge (target). To get started, deploy the pattern and run the command below to insert a new record into DDB.

The new INSERT will trigger EventBridge Pipes and split out the event into three.

```sh
 # Insert info into orders table
aws dynamodb put-item \
--table-name=Orders-Table \
--item '{"id":{"S":"905fa520-4d4a-4850-97c5-1d429f8c23ba"},"userId":{"S":"b507de3e-d9d4-4e88-9e61-28416394777f"},"tickets":{"L":[{"M":{"id":{"S":"5c27a12d-f33f-4b64-8afe-844a8a297660"}}},{"M":{"id":{"S":"2208130e-4f78-48d4-b3e3-bf94912ae71d"}}},{"M":{"id":{"S":"0325bf78-a162-4486-adb1-218aadf41fdc"}}}]}}'

```

## Delete stack

```bash
cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
