# EventBridge Scheduler to Amazon SNS

This pattern will create an [EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/getting-started.html) to publish a message to an Amazon [SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) topic every 5 minutes. The pattern is deployed using the AWS Cloud Development Kit (AWS CDK) for Java. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-schedule-to-sns-cdk-java

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one
  and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS
  resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Java 11+](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-to-sns-publish-cdk-java
    ```
3. From the command line, bootstrap the CDK if you haven't already done so. 
    ```
    cdk bootstrap 
    ```
4. Deploy the CDK stack to your default AWS account and region. Replace email address after "email=" if you wish to test the notification with your email address.
    ```
    cdk deploy -c email=sample@example.com
    ```

## How it works

An EventBridge Schedule is created that publishes a message to an Amazon SNS topic every 5 minutes. Along with a schedule, the CDK stack creates a SNS topic and an IAM role and policy for EventBridge scheduler to assume and send messages.  During CDK deployment, the email address provided in the parameters will receive a subscription confirmation email. Confirm the subscription by clicking the link in the email if you would like to receive the testing notification.  Check the junk email if you do not receive subsciption confirmation email. 

## Testing

The provided email address should receive notification email every 5 minutes after confirming the subscription.

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
