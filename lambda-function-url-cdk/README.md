# AWS Lambda function URL using CDK

This pattern can be used to boostrap a Lambda Function with a Function URL.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed with min version 2.22

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd lambda-function-url-cdk/src
   ```
3. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the template.yml file:

   ```
   cdk deploy
   ```

4. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Lambda Function URL's add HTTPS endpoints to any Lambda function.

## Testing

Use the Cloudformation Output FunctionURLEndpoint from the `cdk deploy` command to test your Lambda function in a browser or API tesing tool.

## Cleanup

1. Delete the stack
   ```
   cdk destroy
   ```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
