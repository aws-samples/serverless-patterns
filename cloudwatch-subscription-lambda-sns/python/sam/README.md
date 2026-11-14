# Account level alerting using Amazon CloudWatch, AWS Lambda and Amazon SNS

This pattern demonstrates an alerting system that leverages an AWS CloudWatch Logs Account-level Subscription filter to trigger a Lambda function, which in turn sends an SNS notification when a specified pattern (in this case, "Exception") is matched in log events across any log group within the account. Currently, there is no out-of-the-box offering from AWS that allows customers to be alerted on specific event patterns across their entire account.

By implementing this pattern, customers can proactively monitor and receive notifications for critical events or errors, such as exceptions or any specific pattern, that may occur in any of their applications or services. This centralized approach to log monitoring and alerting eliminates the need to configure individual alerting mechanisms for each log group or application, thereby streamlining the process and ensuring consistent alerting across the entire AWS account.

Important: 
* This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

* Additionally, There is a risk of causing an infinite recursive loop with subscription filters that can lead to a large increase in ingestion billing if not addressed. To mitigate this risk, we recommend that you use selection criteria in your account-level subscription filters to exclude log groups that ingest log data from resources that are part of the subscription delivery workflow. Please see [Account-level subscription filters risk](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters-AccountLevel.html)

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
    cd cloudwatch-account-subscription-Lambda-sns-notification
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build

    sam deploy --guided --parameter-overrides EmailAddress='example.your@mail.com' LambdaFunctionName='NotificationLambda'
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The key components of this pattern are:

1. AWS CloudWatch Logs Account-level Subscription Filter: This filter is configured to match the desired pattern ("Exception" in this case) and send the matching log events to a designated AWS Lambda function.

2. AWS Lambda Function: This function processes the log events received from the subscription filter and sends a notification to an SNS topic when the specified pattern is matched.

3. AWS Simple Notification Service (SNS) Topic: This SNS topic receives the notifications from the Lambda function and delivers them to subscribed endpoints, such as email addresses or mobile devices, enabling real-time alerting for critical events.


This pattern deploys an account-level subscription filter that monitors all existing and new log groups for a matching log pattern of "Exception". This allows you to catch any event containing the "Exception" pattern across all applications within your AWS account. Optionally, you can produce an exception in any application's logs to test this pattern.
*This pattern creates a new SNS topic with an email subscription. Please confirm the email verification by clicking on the "Confirm subscription" link sent via Amazon SNS.*

## Testing
To test this pattern, which monitors all log groups for the "Exception" pattern and sends SNS notifications, follow these steps:

    - Choose an application generating logs in your AWS account.
    - Intentionally introduce an exception or error condition that logs an "Exception" message.
    - Verify the log event containing "Exception" is written to CloudWatch Logs.
    - Monitor for an SNS email notification containing details like the log group name, log stream name, and the log event with the "Exception" pattern.

This pattern automatically monitors new log groups created, ensuring comprehensive coverage across your AWS account.

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
