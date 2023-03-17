# Split messages from SQS to multiple SQS with EventBridge Pipes

This pattern will split messages in a source SQS queue into multiple target SQS Queues with the original payload using EventBridge Pipes, Event Bus and Rules.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-sqs-to-multiple-sqs

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
   cd serverless-patterns/eventbridge-pipes-sqs-to-multiple-sqs
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

This template will create 3 SQS queues (one source queue and two target queues), an EventBridge Pipe, a Lambda function, Event Bus and two EventBridge Rules.

When a message is added to the source SQS queue, it will be polled by Pipe and the original message is extracted using the enrichment Lambda function. Then the message is sent to the Event Bus. Then, based on the "type" value of the original payload, the message is sent to a target SQS queue using Event Bus Rule.

## Testing

Once this stack is deployed in your AWS account, copy the `SourceQueueUrl` value and add 2 messages into the source SQS queue as follows.

Send OrderCreated message:
```sh
 aws sqs send-message \
 --queue-url=SourceQueueUrl \
 --message-body '{"orderId":"125a2e1e-d420-482e-8008-5a606f4b2076", "customerId": "a48516db-66aa-4dbc-bb66-a7f058c5ec24", "type": "OrderCreated"}'
```

Send OrderUpdated message:
```sh
 aws sqs send-message \
 --queue-url=SourceQueueUrl \
 --message-body '{"orderId":"125a2e1e-d420-482e-8008-5a606f4b2076", "customerId": "a48516db-66aa-4dbc-bb66-a7f058c5ec24", "type": "OrderUpdated"}'
```

You can see the messages are successfully delivered to the respective target queues (TargetQueueOrderCreated and TargetQueueOrderUpdated) with the original payload.

## Delete stack

```bash
cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0