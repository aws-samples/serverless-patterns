# Amazon Redshift Data API with Amazon API Gateway

This pattern demonstrates how to expose data from Redshift through API using API Gateway, Lambda and Redshift Data API.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-lambda-redshiftdataapi)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK installed](https://docs.aws.amazon.com/cdk/latest/guide/cli.html)
- [Python 3 installed](https://www.python.org/downloads/)
- [pipenv installed](https://pipenv.pypa.io/en/latest/installation.html)
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
1. Create python virtual environment and install dependencies:
   ```
   python3 -m venv venv
   source ./venv/bin/activate
   pipenv install
   pipenv install  -r requirements.txt
   ```
1. Create .env file to include Redshift cluster environment variables:
   ```
   Create a .env file in the cloned directory
   Add the following variables with respective to values
      REDSHIFT_CLUSTER_ARN=arn:aws:redshift-serverless:<region>:<accountid>:workgroup/<workgroupid>
      REDSHIFT_WORKGROUP=<workgroup-name>
      REDSHIFT_DATABASE=<database-name>
   ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the template.yml file:

   ```
   cdk deploy --app "python3 apigw_lambda_redshiftdataapi_stack.py"
   ```

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This setup orchestrates exposing data from Redshift through API Gateway with Cognito authorizer and Lambda using Redshift Data API.

## Testing

1. Use an api client with oauth capability such as Postman or Rapid API to test the api. API url can be found from CDK stack deployment output ApigwRedshiftDataApi.ApiUrl. You will need to login to AWS Console, navigate to Cognito app client and retrieve the client id and secret to pass it in the api call.

## Cleanup

cdk destroy --app "python3 apigw_lambda_redshiftdataapi_stack.py"

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
