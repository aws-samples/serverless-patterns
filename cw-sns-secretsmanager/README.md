# AWS Service 1 to AWS Service 2

This pattern explains how to deploy a SAM application that Detects and Notify on Amazon Secrets Manager Secret Key Creation, Updation and Deletion using Amazon CloudWatch event and Amazon SNS

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudwatch-secrets-manager

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* You can either create a Secret Key in AWS Manager now or you can create it later after deployment for testing the flow - https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd cw-sns-secretsmanager
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    * In SNSEndpoint, Provide your email address to receive notification from Amazon SNS

    Once you have run `sam deploy --guided --capabilities CAPABILITY_NAMED_IAM` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This template deploys an application to monitor AWS Secrets Manager secret keys. This helps in reporting when something is wrong, and take automatic actions when appropriate. Once the template is deployed, you will receive an email notification on the email address you defined in Requirements. Make sure to confirm email subscription in order to receive updates related to your Secret Keys present in AWS Secret manager.

## Testing

Once the SAM deployment is successful, first thing to do is to confirm the Email subscription. You will receive an email to confirm it.  Then, head to AWS Secrets Manager console and Create a Secret Key by following these steps - https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html . That's it. You will soon receive a notification about the key you created. Now any event (Like Update or Delete) happens related to that Secret Key, you will receive the notification.

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
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
