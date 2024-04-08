# EventBridge Scheduler to Amazon SQS

This pattern will create an EventBridge schedule to send a message to an Amazon SQS queue every 5 minutes. The pattern is deployed using the AWS Cloud Development Kit (AWS CDK) for Go. 

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
    cd eventbridge-schedule-to-sqs-cdk-go
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

An EventBridge Schedule is created to send a message to an Amazon SQS queue every 5 minutes. Along with a schedule and queue, the CDK stack creates an IAM role and policy for EventBridge scheduler to assume and send messages to the SQS queue.

The resources are deployed using the AWS CDK for Go. 

## Testing
You can confirm messages are being published to the SQS queue by navigating to the Amazon SQS web console, selecting the SQS queue from the list (check the CloudFormation Outputs for the queue name), and clicking the "Send and receive message" button at the top to poll for messages.

You can also check the queues "ApproximateNumberOfMessagesVisible" metric in CloudWatch and verifying positive data points. 
## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0