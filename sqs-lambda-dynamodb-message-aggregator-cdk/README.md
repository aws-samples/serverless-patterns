# SQS to Lambda and DynamoDB (Message Aggregator pattern)

This pattern create two SQS queue, one for receiving the splitted messages and one for the final aggregation and a lambda function and a DynamoDB Table. The pattern is an implementation of the Integration pattern: "Message Aggregator" available here: [https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html)

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/sqs-lambda-dynamodb-message-aggregator-cdk](https://serverlessland.com/patterns/sqs-lambda-dynamodb-message-aggregator-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS SAMCDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    $: git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    $: cd sqs-lambda-dynamodb-message-aggregator-cdk/src
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```bash
    $: cdk deploy
    ```
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The pattern is composed by an SQS Queue which is capable to receive portion of messages. Messages can be aggregated together by providing, for each message, two distinct attributes. `CorrelationId` will inform the AWS Lambda function how to aggregate multiple messages and `Total` will inform the AWS Lambda about the total amount of messages that should be expected for one single aggregation.

Messages are tracked inside a DynamoDB table. When all messages with the same `CorrelationId` are received, the message is aggregated, forwarded to a destination SQS Queue and the record is deleted from DynamoDB, to avoid unecessary costs.

## Testing

Inside the Folder `msg` there are 3 distinct messages and the relative attribute file. The script `test.sh` will send all three messages to the source SqS queue.

```bash
$: ./msg/test.sh
Provide the name of the SQS queue to send messages to
https://sqs.us-east-1.amazonaws.com/[your account]/[your account]-src-queue
{
    "MD5OfMessageBody": "8be1b3b225c0f5113fa4c37f421667d2",
    "MD5OfMessageAttributes": "a512f8c4c91e1bd27eaedaa9916243fe",
    "MessageId": "35527c0c-3dcc-4ec7-8afa-b997019d0549"
}
{
    "MD5OfMessageBody": "4018bae8eed190d3c907720c3f3cdf1c",
    "MD5OfMessageAttributes": "a512f8c4c91e1bd27eaedaa9916243fe",
    "MessageId": "dda99dbf-2f97-4e88-ab28-68011b707a9a"
}
{
    "MD5OfMessageBody": "a9d29a076761cb5a4a1f955814338fcb",
    "MD5OfMessageAttributes": "a512f8c4c91e1bd27eaedaa9916243fe",
    "MessageId": "33e07f8d-5c37-4ffa-aaef-b8f90b9b7646"
}
```

The script will wait 5 seconds then try to pull the destination queue:

```bash
Provide the name of the SQS queue to receive the aggregated message
https://sqs.us-east-1.amazonaws.com/[your account]/[your account]-dest-queue
{
    "Messages": [
        {
            "MessageId": "52505cb6-7013-4f0f-a6f7-4d4f2f5e223d",
            "ReceiptHandle": "AQEB8E0k8R6Qn4BdU8fxWM93NTavPuy6+0lbtg7avweEoMWgETQar1puOAROTB5XZuiqSyaEi7pRH6qaBAgfEuzBLX9aC4gGxRPBXrYyu3byntEk2k6T68q2sLjrhlHpa5dbUuuJGk5ahluQkbMaLqtq3jMRHfVp8QLrzAGdBqZzIGLTJAI9kfD1H38anwnlWF1fSMsY/jC21spEeq8zM72w4Lc83qMynrsPJMCysrzoyG7/PVXYnf8OWHj+am9FPzGPSq0YE+1nW1ATJKEcug2DXJgVdbWpXe+uJ5osOHfEk+e/pTf0uHd2ZL1trr1ICwU4F4Af81tZH8GYP4S7aJ8EMLZycyZDxXBuoHIj2wh86E0gy4Ke0vygbskyYkLAZXSqmiwP87oCIYUcxuITgiA3Hg==",
            "MD5OfBody": "0871a008c15d4c8ccede318f8b942ee5",
            "Body": "{\"VAT\":\"7.7\",\"Street\":\"Louisiana Road 11\",\"Bank\":\"New York State Bank\",\"TotalAmount\":\"123.00 USD\",\"OrderId\":\"123ABC\",\"State\":\"NY\",\"Transaction\":\"123ABC\",\"Date\":\"2023-01-01\",\"Time\":\"08:00:00\"}"
        }
    ]
}
```

## Cleanup
 
1. Delete the stack
    ```bash
    $: cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0