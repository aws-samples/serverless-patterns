# Amazon Cognito to Amazon API Gateway HTTP APIs (JWT)

The SAM template deploys a nested stack with authentication configured using Cognito. It also deploys an HTTP API configured with a JWT authorizer based on the Cognito configuration and a Lambda function on a secure route.

Note: when deploying this pattern, both *CAPABILITY_AUTO_EXPAND* and *CAPABILITY_IAM* are required.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/cognito-httpapi](https://serverlessland.com/patterns/cognito-httpapi)

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
2. Change directory to the pattern directory:
    ```
    cd cognito-httpapi
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy -g --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Select the desired AWS Region
    * Enter a client domain
    * Enter an AppName
    * For **TestWithPostman**, set this to true for local development and testing only. Do not enable for production as it allows implicit grant OAuth flow that is less secure.
    * Allow SAM to create roles with the required permissions.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

The stack will output the **authorization domain** and **client id** required for using authorization via postman. Configure postman authorization as follows:

![Postman authentication](https://serverlessland.s3.amazonaws.com/assets/patterns/patterns-cognito-httpapi1.png)

1. The first time you get a new token, click **Sign Up** on the bottom of the hosted URL

    ![Postman authentication](https://serverlessland.s3.amazonaws.com/assets/patterns/patterns-cognito-httpapi2.png)
2. Retrieve code from your email
3. After verifying the code you can login and then be returned to postman with the proper access token.

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