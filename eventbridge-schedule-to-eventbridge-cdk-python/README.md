# EventBridge Scheduler to Amazon EventBridge

This pattern will trigger an EventBridge event every 5 minutes using an EventBridge schedule and CDK with Python.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-schedule-to-eventbridge-cdk-python

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
   cd serverless-patterns/eventbridge-schedule-to-eventbridge-cdk-python
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

This template will create an EventBridge Schedule, Event Bus, EventBridge Rule and a Lambda function.

EventBridge Schedule will put an event to Event Bus every 5 minutes. Lambda function is configured as the target of the EventBridge Rule, so it will be triggered every time Event Bus received the messsage.

## Testing

Once this stack is deployed in your AWS account, wait about 5 minutes and visit the Lambda function's CloudWatch Log Group. You can see the logs are being generated every 5 minutes with same format as below:

```json
{
    "version": "0",
    "id": "2866b92b-d8ed-7a66-d15e-4a4b936387bf",
    "detail-type": "ScheduleTriggered",
    "source": "scheduled.events",
    "account": "xxxxxxxxxxxx",
    "time": "2023-01-13T09:23:21Z",
    "region": "eu-central-1",
    "resources": [],
    "detail": {
        "metadata": {
            "eventId": "MY_SCHEDULED_EVENT"
        },
        "data": {
            "firstName": "Pubudu",
            "lastName": "Jayawardana"
        }
    }
}
```

## Delete stack

```bash
cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0