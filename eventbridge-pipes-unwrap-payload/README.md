# Using EventBridge Pipes to unwrap stringified payload

This pattern showcases two ways  to parse JSON-strings within an EventBridge Pipe. While an EventBridge Pipe target transformer can parse JSON-strings automatically, if the payload contains nested strings, an additional enricher is needed. This example shows 1) how the unwrapping can be achieved through code, using a Lambda function. 2) how the unwrapping can be achieved withough code, using AWS Step functions intrinsic functions.
Based on your use-case, you may prefer either way to unwrap events.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/unwrap-payload-with-pipes

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
    cd serverless-patterns/unwrap-payload-with-pipes/src
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
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
    ```
    npm run build && cdk deploy 
    ```
1. During the prompts:
    * Enter the desired AWS Region
    

## How it works

To demo the processing, a Lambda function puts three sample events on SNS. Two SQS queues are subscribed to the SNS topic, both receiving the three events. Each queue is conntected to an EventBridge bus, which logs all received events in CloudWatch. One pipe leverages Lambda enrichment to unwrap the stringified payload, the other pipe uses AWS Step Functions to unwrap the stringified payload.

## Testing

Step-by-step instructions to understand the implementation for the pattern:

1. Deploy the Stack
1. (optional) Look at the structure of events created by the "UnwrapSampleDataCreatorLambda-function" (inside unwrapSampleDataCreator.js). Some nested attributes are JSON-strings, rather than JSON-objects.
1. Trigger the UnwrapSampleDataCreatorLambda-function to generate three sample events on each source queue. You can do so in the console or using the CLI: aws lambda invoke --function-name (enter function name here) output.txt 
1. The events are automatically proccessed by two EventBridge Pipes. One uses a Lambda Enrichment, one a Step Function enrichment.
1. Look at the unwrapped events logged in "/aws/events/unwrapTargetLog": both Pipes achieve the same result, an unwrapped JSON-object.

## Cleanup
 
Delete the stack
    ```cdk destroy```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
