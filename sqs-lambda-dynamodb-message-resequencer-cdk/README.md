# SQS to Lambda and DynamoDB (Message Resequencer pattern)

This pattern create two SQS queue, one for receiving the unordered messages and one FIFO for the final broadcasting, a lambda function and a DynamoDB Table. The pattern is an implementation of the Integration pattern: "Message Resequencer" available here: [https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html)

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/sqs-lambda-dynamodb-message-resequencer-cdk](https://serverlessland.com/patterns/sqs-lambda-dynamodb-message-resequencer-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS SAMCDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    $: git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    $: cd sqs-lambda-dynamodb-message-resequencer-cdk/src
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```bash
    $: cdk deploy
    ```
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The pattern is composed by an SQS Queue which is capable to receive unordered messages. Messages can be aggregated together by providing, for each message, two distinct attributes. `CorrelationId` will inform the AWS Lambda function how to keep multiple messages in a sequence and `Total` will inform the AWS Lambda about the total amount of messages that should be expected for one single aggregation. Additionally, each message will need an `Order` attribute, which inform the Lambda how to re-order the messages.

Messages are tracked inside a DynamoDB table. When all messages with the same `CorrelationId` are received, the messages are re-ordered, forwarded to a destination SQS FIFO Queue and the record is deleted from DynamoDB, to avoid unecessary costs.

## Testing

Provide steps to trigger the integration and show what should be observed if successful.

## Cleanup
 
1. Delete the stack
    ```bash
    $: cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0