# Amazon SNS to Amazon SQS by filtering content (Message-content router pattern)

This pattern creates an SNS topic and various SQS destination queues. Messages received by the SNS topic are routed to various SQS queues according to routing logic. The pattern is an implementation of the Integration pattern: "Content-Based Message route" available here: [https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html)

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/sns-sqs-message-content-router-cdk](https://serverlessland.com/patterns/sns-sqs-message-content-router-cdk)

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

The CDK Stack pick-up a configuration from `stackconfiguration.json` stored inside the `src` folder. This files contains a JSON structure that describe the routing logic. The stack will also create a DeadQueue letter for each Queue.

The parameter `IsAttribute` specifies to CDK if the filter is of type attribute or content.

```json
{
    "Sns": {
        "TopicName": "content-router"
    },
    "Sqs": [
        {
            "QueueName": "country-usa",
            "IsAttribute": true,
            "Filter": {
                "FilterName": "country",
                "FilterValues": [
                    "united states of america",
                    "usa"
                ]
            }
        },
        {
            "QueueName": "country-germany",
            "IsAttribute": true,
            "Filter": {
                "FilterName": "country",
                "FilterValues": [
                    "germany",
                    "de"
                ]
            }
        },
        {
            "QueueName": "language-english",
            "IsAttribute": false,
            "Filter": {
                "FilterName": "language",
                "FilterValues": [
                    "english",
                    "en"
                ]
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
Type - String; Name - country; Value - usa   
```

**Scenario-2 Content based**

Create an SNS message with the following information:

```
Message body based filter. Copy Json to the message body and add attibutes given below. This message should be received by Queue1 and Queue3
Message Body:
{
   "Message":"Test Message to be received by Queue2 only",
   "Filter":{
        "Language": ["en"]
   }
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