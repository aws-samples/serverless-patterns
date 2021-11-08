# Integration of Amplify Frontend, Cognito, API Gateway, Lambda

This pattern explains how to deploy a SAM application that includes an AWS Amplify Frontend, Cognito, API Gateway and Lambda Function and set environmental variables to be used by Amplify and the Lambda function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/amplify-apigw-lambda.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd _patterns-model
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the Frontend Repository URL that will be hosted by AWS Amplify Frontend
    * Enter the OauthToken for you git provider
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This template deploys a full-stack application where Amplify frontend application and Lambda Function will have as environmental variables Cognito Region, Cognito User Pool ID and Cognito User Pool Client ID allowing developer to quickly develop an application with Authentication on front and backend. Template set cognito as authorizer for API Gateway, requiring the frontend app to pass json web token (JWT) to call API

## Testing

On AWS amplify Service, click on the app name (same of SAM stack name), click environment varaibles. You should be able to see 4 environmental variables created by the template.

On AWS Lambda Service, click Applications, click the application name (same of SAM stack name), click on Resource called myFunction, click configuration, click Environment variables. You should be able to see 4 environmental variables created by the template.
Execute the lambda function and check the logs. You will see a result like:
Cognito Region:  us-east-1
Cognito User Pool Id:  us-east-1_aYtONfZZZ
Cognito User Pool Client ID:  1h2rrpldfqg8lhbgej2o5s2ZZZ

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
