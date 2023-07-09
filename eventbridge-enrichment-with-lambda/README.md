# Amazon Eventbridge enrichment with AWS Lambda
This project contains a pattern that allows you to enrich events using Lambda functions. When raising events with `enrich` metadata, rules will forward the event to Lambda to enrich and then forward the event onto the bus once enriched.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-enrichment-with-lambda.

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
   cd serverless-patterns/eventbridge-enrichment-with-lambd/cdk
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

- The project contains a producer, consumer and enricher functions.
- The producer is an example of raising an event that will get picked up by the enricher
- The enricher then enriches the data and forward the event back onto the bus
- Downstream consumer picks up event as usual
- Rules are setup on the EventBridge bus to forward enriched events to the correct locations.
- [Read more details here](./cdk/README.md)

## Testing

Deploy the stack and trigger the `producer` Lambda function. Then view the CloudWatch logs of the `consumer` function. You will see the event has been enriched with user data (as an example).

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0