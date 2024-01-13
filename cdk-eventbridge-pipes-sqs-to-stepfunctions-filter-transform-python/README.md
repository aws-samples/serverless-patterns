# EventBridge Pipe from SQS to Step Functions with filter and transformation

This pattern will use Amazon EventBridge Pipe to accept source messages from Amazon Simple Queue Service and will apply filter and transformation before sending the target message to AWS Step Functions.
This example project implemented with CDK/Python.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-sqs-to-stepfunctions-cdk-python

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
   cd serverless-patterns/eventbridge-pipes-sqs-to-stepfunctions-cdk-python/
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

The template will create an Amazon Simple Queue Service, AWS Step Functions and Amazon EventBridge Pipe. 
Sending messages to the Amazon Simple Queue Service will trigger the pipe to initiate AWS Step Function execution.
SQS Messages will be filtered and transformed before sending to AWS Step Functions.


Replace the "SQS_URL" with your SQS URL in the below command and send SQS message that will trigger step function execution as below:

```sh
 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"id":"id1","team": "Team1", "status": "COMPLETE"}'

 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"id":"id2","team": "Team2", "status": "COMPLETE"}'
 
 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"id":"id3","team": "Team3", "status": "NOTSTARTED"}'

Validate the below from the step functions execution window. 
Amazon SQS messsages are filtered with status COMPLETE only filered and delivered to AWS Step Functions. 
AWS Stepfunctions receive the transformed message attributes as below. 
    "id" tranformed to "playerid" 
    "team" transformed to "teamname"
    "status" transformed to "teamstatus"
    
```

## Delete stack

```bash
cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0