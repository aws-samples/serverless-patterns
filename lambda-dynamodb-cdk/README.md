# AWS Lambda to Amazon DynamoDB

This project contains a sample AWS Cloud Development Kit (AWS CDK) template for deploying a Lambda function that makes puts to a DynamoDB table.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-dynamodb-cdk.

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
   cd serverless-patterns/lambda-dynamodb-cdk/cdk
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
   cdk deploy
   ```
6. Note the outputs from the CDK deployment process. This contains the Lambda function ARN which is used for testing.

## How it works

This is similar to the `lambda-dynamodb` example but is implemented in CDK.

- A Lambda function is invoked by an event integration or CLI command
- The Lambda function "stringifies" the event payload
- The Function uses the AWS SDK to perform a `put` command on a DynamoDB table
- The name of the DynamoDB table is passed to the Lambda function via an environment variable named `DatabaseTable`
- The Lambda function is granted `PutItem` permissions, defined in CDK via `dynamoTable.grantWriteData(lambdaPutDynamoDB);`

## Testing

Run the following Lambda CLI invoke command to invoke the function. Note, you must edit the {LambdFunctionArn} placeholder with the ARN of the deployed Lambda function. This is provided in the stack outputs. Note that this requires AWS CLI v2.

```bash
aws lambda invoke --function-name "LAMBDA_FUNCTION_ARN" \
--invocation-type Event \
--payload '{ "Metadata": "Hello" }' \
--cli-binary-format raw-in-base64-out \
response.json
# Example
aws lambda invoke --function-name "arn:aws:lambda:ap-southeast-2:123456789123:function:CdkStack-lambdaPutDynamoDBHandler1A123456-fooBarBazFoo" \
--invocation-type Event \
--payload '{ "Metadata": "Hello" }' \
--cli-binary-format raw-in-base64-out \
response.json
```

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
