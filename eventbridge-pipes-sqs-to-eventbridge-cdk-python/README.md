# SQS to EventBridge Bus using EventBridge Pipes

This pattern demonstrates sending SQS messages directly to EventBridge bus using EventBridge Pipes.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-sqs-to-eventbridge-cdk-python

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/eventbridge-pipes-sqs-to-eventbridge-cdk-python
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

The template will create an SQS queue, event bus and pipe. Sending messages to the SQS queue will trigger the pipe to forward the messages onto the event bus.

Send SQS message that will trigger event on event bus

```sh
 # Send SQS message to be sent to EventBridge using the filter.
 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"orderId":"125a2e1e-d420-482e-8008-5a606f4b2076, "customerId": "a48516db-66aa-4dbc-bb66-a7f058c5ec24", "type": "NEW"}'
```

## Delete stack

```bash
cdk destroy
```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0