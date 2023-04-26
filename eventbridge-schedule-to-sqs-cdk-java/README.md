# Amazon EventBridge Schedule to Amazon SQS

This pattern will create an EventBridge schedule to send a message to an Amazon SQS queue every 5 minutes. The pattern is deployed using the AWS Cloud Development Kit (AWS CDK) for Java.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements
* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Maven](https://maven.apache.org/download.cgi) installed and configured
* [Java 11+](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-schedule-to-sqs-cdk-java
    ```
1. From the command line, use Maven to build and package the project
    ```
    mvn clean package
    ```
1. From the command line, bootstrap the CDK if you haven't already done so. 
    ```
    cdk bootstrap 
    ```
1. Deploy the CDK stack to your default AWS account and region. 
    ```
    cdk deploy
    ```

## How it works
The CDK stack creates an EventBridge Scheduler that sends a message to an Amazon SQS queue every 5 minutes. Along with a schedule and SQS queue, the CDK stack creates an IAM role and policy for EventBridge Scheduler to assume and send messages. 

## Testing
1. You can confirm messages are being published to the SQS queue by navigating to the Amazon SQS web console, selecting the SQS queue from the list (check the CloudFormation Outputs for the queue name), and clicking the "Send and receive message" button in the top right to poll for messages.

You can also check the queues "ApproximateNumberOfMessagesVisible" metric in CloudWatch and verifying positive data points. 

## Cleanup

1. Delete the stack
```bash
   cdk destroy
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0