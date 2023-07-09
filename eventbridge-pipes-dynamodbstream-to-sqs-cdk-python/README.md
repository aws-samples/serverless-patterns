# DynamoDB Stream to SQS using EventBridge Pipes with CDK/Python

This pattern will send messages from a DynamoDB Stream into a target SQS queue using EventBridge Pipes.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-dynamodbstream-to-sqs-cdk-python

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/eventbridge-pipes-dynamodbstream-to-sqs-cdk-python
   ```
3. To manually create a virtualenv on MacOS and Linux:
    ```bash
    $ python3 -m venv .venv
    ```
4. After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.
    ```bash
    $ source .venv/bin/activate
    ```
5. If you are a Windows platform, you would activate the virtualenv like this:
    ```bash
    % .venv\Scripts\activate.bat
    ```
6. Once the virtualenv is activated, you can install the required dependencies.
    ```bash
    $ pip install -r requirements.txt
    ```
7. To deploy the application:
    ```bash
    $ cdk deploy
    ```

## How it works

This template will create a DynamoDB table, EventBridge Pipe and a SQS queue. DynamoDB Stream is enabled in the DynamoDB table.

Whenever a change happened to an item in the DynamoDB table, the information about the item and change will be available in DynamoDB Stream as a message. EventBridge Pipe polls DynamoDB table and when messages are found, it first filter the message based on the filter criteria provided. In this case, it matches the 'entity' value as 'user'. Then the matched messages will be sent to the target SQS queue.

## Testing

Once this stack is deployed in your AWS account, copy the DynamoDBTableName value from the output.

Then, insert two records to the DynamoDB table as follows:
Record with user entity:
```sh
    aws dynamodb put-item \
        --table-name DynamoDBTableName \
        --item '{"pk": {"S":"8679eec3-0dc4-4dc2-91bd-81400b31c5dd"}, "entity": {"S":"user"}}'
```

Record with payment entity:
```sh
    aws dynamodb put-item \
        --table-name DynamoDBTableName \
        --item '{"pk": {"S":"b87d00d5-7819-4224-83d4-78fc14d552f3"}, "entity": {"S":"payment"}}'
```

When you check the SQS queue, you can see only the message with entity user from DynamoDB stream is available in the SQS queue.

## Delete stack

```bash
cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0