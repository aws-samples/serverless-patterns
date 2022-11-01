# Amazon S3 Claim Check pattern with Amazon EventBridge
This project contains an event-driven pattern that allows you listen for files uploaded and removed from S3 and fire domain events for them. S3 events go into EventBridge for processing, then the events are transformed into domain events, enriched and a presigned url is generated for the S3 contents for downstream consumers. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-to-eventbridge-claim-check-pattern.

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

- User uploads a file to s3 (/claims/{user-id}/{file-name}).
- Upload and deletion events from S3 are forwarded to EventBridge
- Custom domain events (ClaimCreated and ClaimProcessed) are generated with metadata and presigned urls.
- Downstream consumers process domain events.
- [Read more details here](./cdk/README.md)

## Testing

Upload a file to your new S3 bucket created using this pattern. Make sure the key is `(/claims/{user-id}/{file-name})`.
View the CloudWatch log groups for the consumers to see enriched data and presigned URL back to the s3 bucket.

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0