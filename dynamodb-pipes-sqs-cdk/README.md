# DynamoDB Streams to SQS using EventBridge Pipes
This pattern demonstrates a low code way to send DynamoDB stream records to an SQS queue using EventBridge Pipes.

Although you can process records from a DynamoDB stream directly using Lambda, it can be difficult to reprocess errors from that Lambda that end up in a dead letter queue.  The messages in the dead letter queue have DynamoDB stream information, not the actual stream record itself.

`See sample-messages/dynamo-dlq-message.json for an example.`

In order to reprocess a failed DynamoDB streams message, you would need to write separate code that uses the stream information to read the records from the stream, and then trigger the same Lambda code manually.  In addition, you must reprocess those failed messages quickly as DynamoDB stream messages expire after 24 hours.

This approach leverages SQS and its feature to re-drive failed messages from the dead letter queue to the input queue. That means the same code can be used to process both the original messages and the failed messages.  The dead letter queue is configured to keep the messages for up to 14 days, which allow the team time to fix the problem and reprocess the messages without having to rush.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-pipes-sqs-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd dynamodb-pipes-sqs-cdk
    ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
    ```
    cdk deploy
    ```

## How it works

When items are put in the DynamoDB table, the DynamoDB stream captures a time ordered sequence of the changes to the items. The EventBridge pipe uses the stream records as a source and writes those records to the target SQS queue.

## Testing

You can run the following command from the same directory as this file.  It will insert 10 records with random primary keys to the DynamoDB table, and those DynamoDB stream change records will be reflected as messages in the SQS queue.

```bash
./scripts/insert-data.sh
```

Alternatively, you can insert items into the DynamoDB table with the name "dynamo-pipes-to-sqs" manually through the AWS Console.

To view the messages in the queue, you can run the following script after replacing the region and account number.

```bash
./scripts/read-queue-messages.sh https://sqs.<your-region>.amazonaws.com/<your-account-number>/dynamo-pipes-to-sqs
```

You will need to have jq installed to run this script.  Alternatively, you can go to the AWS Console to

## Cleanup

1. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
