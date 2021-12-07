# AWS  VPC, Subnets, Aurora Serverless, Secrets Manager

This project contains a sample AWS Cloud Development Kit (AWS CDK) template for deploying  an Aurora Serverless db Cluster, a Secret Manager, and required VPC with subnets.

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
   cd serverless-patterns/s3-cdk/cdk
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
5. Ensure that the bucket name is unique in [cdk-stack.ts](./cdk/lib/cdk-stack.ts)
6. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/s3cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```

## How it works

- The  VPC, Subnets, Aurora Serverless Cluster is created when `cdk deploy` is executed
- The complete stack is removed when `cdk destroy` is executed


## Testing

Run `tsc && npm test` to ensure the stack contains an S3 bucket as expected


Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
