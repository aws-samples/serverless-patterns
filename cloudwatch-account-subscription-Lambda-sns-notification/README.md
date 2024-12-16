# Amazon CloudWatch Logs Subscription to AWS Lambda along with SNS notification using SAM

This pattern demonstrates an alerting system using CloudWatch Logs Account level Subscription filter to a Lambda function to trigger a SNS notification when specified pattern " Exception" is matched in logevent across any of the loggroups in account. Currently we dont have out of box offering to alert the customer on specific event pattern accross the account.

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
    cd cloudwatch-account-subscription-Lambda-sns-notification
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build

    sam deploy --guided --parameter-overrides 'EmailAddress="your-Exmaple-email@mail.com"'
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys :
1. One SNS topic with email subsciption
2. CloudWatch loggroup Account level subscription filter
3. Notification Lambda.

This pattern depploys account level subscritption filter which is monitors all the existing and new loggroup with matching log pattern of Exception. Thus, can catch any event with pattern Excpetion across all application. Optionally, you can produce any Exception in any applciation logs
*This parrten cretes a new SNS topic with email subscription. Please confirm email verification by clicking on "Confirm subscription" link sent via Amazon SNS.*

## Testing
This pattern monitors existing and new loggroups, you can raise the "Exception" across any of the loggroup.
Thus, triggering the CloudWatch log subscription filter with pattern matching. The notification Lambda publish a sns email notification with loggroup, logstream and logevent details

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
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
