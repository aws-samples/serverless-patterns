# AWS SNS to Step Functions via EventBridge Pipes and Bus

This pattern demonstrates how to trigger a Step Function from an Event that is publisehded into
SNS and is handled by EventBridge Pipes where it is filtered and transformed before sending to an
EventBus

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

-   [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
-   [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
-   [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
-   [Node and NPM](https://nodejs.org/en/download/) installed
-   [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd cdk-sns-sqs-eventbridge-pipes-stepfunctions
    ```
3. Install the project dependencies
    ```
     npm instaall
    ```
4. Deploy the stack to your default AWS account and region
    ```
    cdk deploy
    ```

## How it works

This pattern is designed to help connect producers that are submitting messages into SNS with EventBridge as a way to deliver those same events in a more configuration driven and scalable way. It also helps reduce load and needless code downstream by leveraging AWS EventBridge Pipes to both filter and transform the data from the producer before attaching to an EventBus for further consumption.

Once the pattern is deployed to AWS, you will have the following resources created with the described capabilities

-   SNS Topic that is used for receiving the input message
-   SQS Queue which is subscrited to the SNS Topic with `rawMessageDelivery` enabled
-   EventBridge Pipe is reading from the SQS
    -   A Filter step will be attached for limiting the events the pipe allows through
    -   A Transformation step will be attached to the Pipe for modifying the incoming Message Body to a more suitable output for consumption
-   An EventBridge Custom EventBus
-   EventBridge Rule attached to the Custom Bus which Triggers the State Machine
-   A very basic Step Function with a Succeed Task to simply demonstrate connectivity

## Testing

In the AWS Console, browse to the SNS Service and find the `sample-topic` that is created. Once the Topic is opened, choose to `Publish Message`. Enter the below in the Message Body

```javascript
{
    "eventType": "SampleEvent",
    "field1": "Sample Field 1",
    "field2": "Sample Field 2",
    "field3": "Sample Field 3"
}
```

After publishing, browse to the Step Functions Service and inspect that the State Machine was triggered and that the input supplied matches the input defined in the EventBridge Pipe.

## Cleanup

1. Delete the stack
    ```bash
    cdk destroy
    ```

## Documentation

-   [AWS EventBridge Pipes](https://aws.amazon.com/eventbridge/pipes/)
-   [AWS EventBridge Pipes SQS Source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-sqs.html)

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
