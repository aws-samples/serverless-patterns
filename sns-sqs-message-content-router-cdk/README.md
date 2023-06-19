# Amazon SNS to Amazon SQS by filtering content

This pattern creates an SNS topic and various SQS destination queues. Messages received by the SNS topic are routed to various SQS queues according to routing logic.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here [https://serverlessland.com/patterns/sns-sqs-message-content-router-cdk](https://serverlessland.com/patterns/sns-sqs-message-content-router-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS SAMCDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sns-sqs-message-content-router-cdk/src
    ```
1. From the command line, use AWS CDK to deploy the Stack:
    ```
    cdk deploy
    ```
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The CDK Stack pick-up a configuration from `stackconfiguration.js` stored inside the `src` folder. This files contains a JSON structure that describe the routing logic. The stack will also create a DeadQueue letter for each Queue and a Default Queue for messages that do not match any

```json
{
    "Sns": {
        "Name": "The name of the SNS Topic"
    },
    "Sqs": [
        {
            "Name": "The name of the SQS queue",
            "ContentFilter": "True - the filter will act on the message content; False - the filter will act on the message attribute",
            "Filter: {
                "Name": "The property name of the filter",
                "Values": ["value1", "value2"]
            }
        }
    ]
}
```

## Testing

In order to test the solution, you need to login into your AWS Console and generate a couple of Amazon SNS messages that mimics the filters provided in `stackconfiguration.js`.

**Scenario-1 Attribute based**

Create an SNS message with the following information:

```
Message Body:
{
   "Message":"Test Message to be received by Queue3 only"
}
Message Attribute:
Type - String; Name - Filter1Name; Value - Filter1Value1   
```

**Scenario-2 Content based**

Create an SNS message with the following information:

```
Message body based filter. Copy Json to the message body and add attibutes given below. This message should be received by Queue1 and Queue3
Message Body:
{
   "Message":"Test Message to be received by Queue2 only",
   "Filter1Name":"Filter1Value1"
}   
```

Then head to the Amazon SQS queues, pull the messages and verify that the messages have been routed to the correct queue.

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0