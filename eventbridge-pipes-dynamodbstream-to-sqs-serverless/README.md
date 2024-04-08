# DynamoDB Stream to SQS queue using EventBridge Pipes

This serverless pattern demonstrates how to send events from DynamoDB Stream to SQS using EventBridge Pipes.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ``` sh
    cd serverless-patterns/eventbridge-pipes-dynamodbstream-to-sqs-serverless
    ```
1. From the command line, use npm/yarn to install the development dependencies:
    ``` sh
    npm install
    ```
    -or-
    ``` sh
    yarn install
    ```
1. From the command line, use Serverless Framework to deploy the AWS resources for the pattern as specified in the serverless.yml file:
    ``` sh
    serverless deploy --verbose
    ```
    The above command will deploy resources to `ap-south-1` region by default. You can override the target region with `--region <region>` CLI option, e.g.
    ``` sh
    serverless deploy --verbose --region us-west-2
    ```

## How it works

This template will create a DynamoDB table, EventBridge Pipe and a SQS queue. DynamoDB Stream is enabled in the DynamoDB table.

Whenever an item is inserted in DynamoDB table, the stream picks up the event & send it to EventBridge Pipes. The EventBridge Pipes Filter function in the Pipes filters the event and passes to the next states accordingly. For this example pattern, it checks for `INSERT` events & passes it to Enrichment Lambda function if found one. The Lambda function makes some logs regarding to event & event name & finally passes it to the Target SQS queue. In Target SQS queue, when new messages are polled, the event information information can be retrieved. 

## Testing

Once this stack is deployed in your AWS account, copy the `DynamoDBSourceTableName` value from the output.

Then, insert one record to the DynamoDB table as follows:
```sh
    aws dynamodb put-item \ 
    --table-name DynamoDBSourceTable \
    --item \
        '{"Album": {"S": "Item-One"}}'
```
When you check the Target SQS queue, you can see the message from DynamoDB stream is available in the SQS queue.
Optional - Under the Enrichment Lambda Function of EventBrudge Pipes, you can see the CloudWatch logs for the event information and eventName.


## Cleanup
1. Delete the stack
    ```sh
    serverless remove --verbose
    ```
1. Confirm the stack has been deleted
    ```sh
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'dynamodbstream-ebpipes-sqs-serverless-prod')].StackStatus"
    ```
    Expected output
    ```json
    [
        "DELETE_COMPLETE"
    ]
    ```
    NOTE: You might need to add `--region <region>` option to AWS CLI command if you AWS CLI default region does not match the one, that you used for the Serverless Framework deployment.
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0