# Amazon EventBridge Scheduler to Amazon SNS

This pattern will create an EventBridge schedule to send a message to an Amazon SNS topic every 5 minutes. The pattern is deployed using the AWS Cloud Development Kit (AWS CDK) for Python. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one
  and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS
  resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Go](https://go.dev/dl/) (`1.18` or above) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-to-sns-cdk-go
    ```
3. From the command line, bootstrap the CDK if you haven't already done so. 
    ```
    cdk bootstrap 
    ```
4. Install the Go required dependencies:
    ```
    go build
    ```
5. Deploy the CDK stack to your default AWS account and region. 
    ```
    cdk deploy
    ```

## How it works

An EventBridge Schedule is created that sends a message to an Amazon SNS topic every 5 minutes. Along with a schedule and topic, the CDK stack creates an IAM role and policy for EventBridge scheduler to assume and send messages. 

## Testing
After the stack has been deployed, you can verify EventBridge is successfully publishing to the topic by viewing the topics "NumberOfMessagesPublished" metric in CloudWatch and verifying positive data points. 

You can also add a subscription to the SNS topic such as an email address or phone number to verify messages are being published to Amazon SNS from EventBridge.

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
