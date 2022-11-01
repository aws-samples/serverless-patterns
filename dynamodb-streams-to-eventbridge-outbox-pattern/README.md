# Outbox pattern with DynamoDB and EventBridge
This project contains an event-driven pattern that is influenced by the [Transactional outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html). 

This pattern will write data into a DDB table and then create a stream from it. Lambda is then used to process the change events in the database and forwarded onto EventBridge.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-streams-to-eventbridge-outbox-pattern

For more details you can read the [pattern README](./cdk/README.md);

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/s3-to-eventbridge-claim-check-pattern/cdk
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

1. Lambda is triggered to insert data into DynamoDB (new user in this example). _This Lambda would be triggered from other event in reality, e.g API Gateway for example_
1. Table to store new information (user in this example)
1. Change data capture stream setup for table to listen for `New Image` (new items into the table)
1. Lambda connects to stream to process the change events, and processed them into `Domain` events (in this example `UserCreated`)
1. Events are sent to business event bus, and rules setup for downstream consumers. In this example we have a basic Lambda function listening for the new `UserCreated` event.

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0