# Amazon EventBridge to Amazon SQS

This project contains sample AWS CDK code to create an EventBridge Rule, as well as, an SQS Queue. The EventBridge Rule publishes matched events to the SQS Queue. In this example, the rule filters for specific attributes in the event before sending the event to the Queue.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-sqs-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [Python, pip, virtuenv](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deploy

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd eventbridge-sqs-cdk/cdk
   ```

3. Create and activate the project's virtual environment. This allows the project's dependencies to be installed locally in the project folder, instead of globally. Note that if you have multiple versions of Python installed, where the `python` command references Python 2.x, then you can reference Python 3.x by using the `python3` command. You can check which version of Python is being referenced by running the command `python --version` or `python3 --version`

   ```sh
    python -m venv .venv
    source .venv/bin/activate
   ```

4. Install the project dependencies

   ```sh
   python -m pip install -r requirements.txt
   ```

5. Deploy the stack to your default AWS account and region. 

   ```sh
   cdk deploy
   ```

## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The EventBridge Rule specified in `app.py` which filters the events based upon the criteria in the `rule.add_event_pattern` method. When matching events are sent to the custom EventBridge Bus that trigger the Rule, they are published to the SQS Queue.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the event delivered to the Lambda function by reviewing the Amazon CloudWatch Logs associated with the function:

1. Send an event to the custom EventBridge Bus. Note that Custom Bus Name is in the `event.json` file) :

```sh
aws events put-events --entries file://event.json
```

2. Retrieve the Message from SQS, referencing the SQS Queue URL from the Outputs section of the deployed Stack, to see a Message matching this example:

```sh
aws sqs receive-message --queue-url <SQS Queue URL>
```
```json
{
    "Messages": [
        {
            "MessageId": "db759882-e6fe-4d50-8c19-c09f1ae8c87e",
            "ReceiptHandle": "AQEBwhNNAlv...Sgd0VL",
            "MD5OfBody": "ad70b8...123f",
            "Body": "{\"version\":\"0\",\"id\":\"def5aa42-ab94-bc96-0794-3f2bcd143e76\",\"detail-type\":\"message-for-queue\",\"source\":\"my-cdk-application\",\"account\":\"123456789012\",\"time\":\"2021-10-08T18:43:15Z\",\"region\":\"us-west-2\",\"resources\":[],\"detail\":{\"message\":\"Hello CDK world!\"}}"
        }
    ]
}
```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```sh
cdk destroy
```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0