# AWS pattern for API Gateway to Lambda to DynamoDB

This project contains a sample AWS CDK template for a workflow that integrates API Gateway with Lambda and DynamoDB.

 This CDK pattern guides you through setting up an [Amazon API Gateway](https://aws.amazon.com/api-gateway/) endpoint, validating request before triggering a [AWS Lambda ](https://aws.amazon.com/lambda/) function, which processes requests and interacts with [ Amazon DynamoDB](https://aws.amazon.com/dynamodb/) as a database.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
 2. Change directory to the pattern directory:
     ```
     cd cdk-apigw-lambda-dynamodb
     ```
 3. Install dependencies:
     ```
     npm install
     ```

 4. Synthesize CloudFormation template:
     ```
     cdk synth
     ```
 5. Deploy the stack to your default AWS account and region. This command should deploy the serverless workflow to your AWS account.
     ```
     cdk deploy
     ```
 6. Browse to the AWS CloudFormation console to verify the successful deployment of the stack.


## How it works

1. The AWS CDK template deploys and API to API Gateway, a Lambda function to Lambda, and a table to DynamoDB. 
2. The API is configured with a POST method at the root resource in API Gateway, which triggers the Lambda function.
3. The Lambda function processes the request and saves the data to the DynamoDB table.


## Testing

To test the API Gateway endpoint, you can use the following `curl` command to invoke the POST method with a sample email address. Replace `your-api-id` and `your-region` with your actual API Gateway ID and region.

1. Invoke the Endpoint:
    ```
    curl -X POST \
      https://your-api-id.execute-api.your-region.amazonaws.com/prod/ \
      -H "Content-Type: application/json" \
      -d '{
        "email": "example@email.com"
      }'
    ```

2. Expected Response:
If successful, you should receive a response indicating that the email has been saved:

    ```
    {
      "message": "Your email has been saved!"
    }
    ```

## Cleanup

 1. Delete the stack
    ```
    cdk destroy
    ```
 2. Confirm the stack has been deleted
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'ENTER_STACK_NAME')].StackStatus"
    ```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
