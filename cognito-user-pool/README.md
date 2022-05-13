# Amazon Cognito User Pool

The SAM template deploys an Amazon Cognito User Pool with its associated User, App Client, Domain and Resource Server.

You can use the tokens provided upon successful authentication with your User Pool to, for example, access a REST API protected with a Cognito User Pool authorizer. 

Note: when deploying this pattern, *CAPABILITY_IAM* is required.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/cognito-user-pool](https://serverlessland.com/patterns/cognito-user-pool)

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
    cd cognito-user-pool
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy -g
    ```
1. During the prompts:
    * Enter a stack name
    * Select the desired AWS Region
    * Enter the email that will be used as username. You will receive your temporary password in this email address.
    * Enter the URL that you would like Cognito to use as callback URL once you have authenticated with your username and password.
    * Allow SAM to create roles with the required permissions if needed.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

The stack will output the **Cognito Hosted UI URL**. You will also receive an email with your temporary password at the email address specified in the parameters. You can copy-paste the **Cognito Hosted UI URL** into a browser and authenticate with your username and password. Upon successful authentication, the callback URL will be called, which will include a *id_token* parameter and a *access_token* parameter in the request. You can now use these tokens to authenticate to, for example, a REST API protected with a Cognito User Pool authorizer. 
   
## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0