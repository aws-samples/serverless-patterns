# Amazon SQS FIFO queue with delay using AWS Lambda and Amazon DynamoDB

This pattern shows how to introduce a delay between processing messages while maintaining order from an individual client. The message is sent sequentially to the downstream service for processing to minimize the consequences of unordered events.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sqs-fifo-delayed-queue-dynamodb

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sqs-fifo-delayed-queue-dynamodb
    ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `delay_fifo_queue_test/delay_fifo_queue_test_stack.py` file.
    ```
    python3 -m pip install -r requirements.txt
    cdk synth
    cdk deploy
    ```

## How it works

This pattern deploys an Amazon SQS FIFO queue called `primary_queue`, a AWS Lambda function `process_queue_function`, a DynamoDB table `customer_table` and a second SQS FIFO queue `downstream_queue`. 

When a messages from `primary_queue` is processed by the `process_queue_function`, it is checked against `customer_table` to see if another message from the same message sender has been processed with in a specified time frame.
If true, the message is not processed and with be retried after the visibility timeout on the `primary_queue`.
If false, the message is sent to the `downstream_queue` for processing. An entry is made to `customer_table` with a TTL.


## Testing

1. Edit lines 3 and 7 of `send_messages.sh` with the `DelayFifoQueue` URL from the output of the `cdk deploy`. Run this script to send test messages to the queue.
2. Head to AWS console and go to SQS service. Click on Queues, and select the queue containing the text `DelayFifoQueueDownstream`.
3. Click on `Send and receive messages` then `Poll for messages` to see current messages in the queue.
4. You shold observe messages with `test1`, `test2-first-message`, `test3` and `test4` in the `downstream_queue`.
5. After around 60 seconds poll again, there should be another messages in the `downstream_queue` with `test2-delayed-message-1` as MessageBody.
6. After another 60 seconds poll again, there should be another messages in the `downstream_queue` with `test2-delayed-message-2` as MessageBody.

## Cleanup
 
1. Delete the stack
    ```
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
