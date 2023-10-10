# Amazon Eventbridge to Amazon SQS

This project contains sample AWS CDK code to create an EventBridge Rule, as well as, a SQS Queue. The EventBridge Rule publishes matched events to the SQS Queue. In this example, the rule filters for specific attributes in the event before sending the event to the Queue.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-sqs-dotnet-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change the working directory to this pattern's directory
    ```
    cd eventbridge-sqs-dotnet-cdk
    ```

3. Install dependencies
    ```
    dotnet restore src/
    ```

4. Deploy the stack to your default AWS account and region
    ```
    cdk deploy
    ```

## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The EventBridge rule filters the events based upon the defined criteria. When matching events are sent to EventBridge that trigger the rule, they are published to the SQS Queue.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Send an event to EventBridge:
    ```
    aws events put-events --entries file://event.json
    ```

2. Retrieve the Message from SQS, referencing the SQS Queue URL from the Outputs section of the deployed Stack, to see a Message matching this example:
    ```
    aws sqs receive-message --queue-url SQS_QUEUE_URL
    ```
    ```json
    {
        "Messages": [
            {
                "MessageId": "db759882-e6fe-4d50-8c19-c09f1ae8c87e",
                "ReceiptHandle": "AQEBwhNNAlv...Sgd0VL",
                "MD5OfBody": "ad70b8...123f",
                "Body": "{\"version\":\"0\",\"id\":\"c9257dc0-7c6c-6bb8-5fdc-2f6d87cd6cb4\",\"detail-type\":\"message\",\"source\":\"cdk.myapp\",\"account\":\"123456789012\",\"time\":\"2022-05-05T22:09:10Z\",\"region\":\"eu-west-2\",\"resources\":[],\"detail\":{\"message\":\"Hello from EventBridge to SQS Queue!\"}}"
            }
        ]
    }
    ```

## Cleanup
 
1. Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
    ```
    cdk destroy
    ```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
