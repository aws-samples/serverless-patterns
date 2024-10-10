# AWS Service 1 to AWS Service 2

This pattern demonstrates how to expose data from Redshift through API using API Gateway, Lambda and Redshift Data API.

Learn more about this pattern at Serverless Land Patterns: [<< Add the live URL here >>](https://serverlessland.com/patterns/apigw-lambda-redshiftdataapi)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK installed](https://docs.aws.amazon.com/cdk/latest/guide/cli.html)
- [Python 3 installed](https://www.python.org/downloads/)
- [Create Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html#serverless-console-resource-creation)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd apigw-lambda-redshiftdataapi
   ```
1. Install dependencies:
   ```
   pipenv install
   pipenv requirements > requirements.txt
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

   ```
   cdk deploy
   ```

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This setup orchestrates exposing data from Redshift through API Gateway with Cognito authorizer and Lambda using Redshift Data API.

## Testing

1. Use an api client with oauth capability such as Postman or Rapid API to test the api with the url found from CDK stack deployment output.

## Cleanup

cdk destroy --all

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
