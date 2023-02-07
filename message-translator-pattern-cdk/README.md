# SQS to Step Functions using EventBridge Pipes with message translator pattern

This pattern implementes the [message translator](https://www.enterpriseintegrationpatterns.com/MessageTranslator.html) pattern using an EventBridge Pipe. This example uses SQS as source and Step Functions as target, but the pattern can be applied to other sources and targets as well. 

In an event-driven architecture, event senders and receivers are independent from each other, and for that reason, the events they exchange may have different formats. To allow communication between different components, a translation of these events is needed, known as the Message Translator pattern. For example, an event contains an address, but the consumer expects coordinates.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/message-translator-pattern-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/message-translator-pattern-cdk/src
    ```
1. Install dependencies:
    ```
    npm install
    ```
1. From the command line, configure AWS CDK:
   ```
    cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
    cdk bootstrap 1111111111/us-east-1
    cdk bootstrap --profile test 1111111111/us-east-1
   ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern.
    ```
    npm run build && cdk deploy 
    ```
1. During the prompts:
    * Enter the desired AWS Region
    

## How it works

For demonstration purposes this pattern is implemented using a lambda function which mocks the result. This way, you can test it without the need for an geolocation API.

## Testing

Step-by-step instructions to understand the implementation for the pattern:

1. Trigger the MessageTranslatorSampleDataCreatorLambda-function to generate an example event with an address.
2. Take a look at the MessageTranslatorTargetStepFunctionsWorkflow to see the result.

## Cleanup
 
Delete the stack
    ```cdk destroy```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
