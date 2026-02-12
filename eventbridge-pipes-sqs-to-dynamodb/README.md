# SQS to DynamoDB using EventBridge Pipes with API Gateway and CDK/Python

This pattern will send messages from an SQS queue to a DynamoDB table via API Gateway using EventBridge Pipes.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-sqs-to-dynamodb

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
   cd serverless-patterns/eventbridge-pipes-sqs-to-dynamodb
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

This template will create an SQS queue, EventBridge Pipe, API Gateway and a DynamoDB table.

Messages sent to the SQS queue are polled by EventBridge Pipe. EventBridge Pipe processes the messages and sends them to API Gateway endpoint. API Gateway transforms the message and writes the data to DynamoDB table using direct integration.

## Testing

Once this stack is deployed in your AWS account, copy the SQS queue name value from the output.

Then, send a message to the SQS queue as follows:
```sh
    aws sqs send-message \
        --queue-url "https://sqs.<region-id>.amazonaws.com/<account-id>/<queue-name>" \
        --message-body '{"Message": "{\"content\":\"Test message\",\"params\":{\"name\":\"Mario\",\"surname\":\"Rossi\"}}"}'
```

When you check the DynamoDB table, you can see the entry with all the attributes parsed by API Gateway.

## Cleanup
 
1. Delete the stack

```bash
    cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
