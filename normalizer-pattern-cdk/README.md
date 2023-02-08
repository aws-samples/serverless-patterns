# SQS to EventBridge using EventBridge Pipes with normalizer pattern

This pattern demonstrates the [normalizer pattern](https://www.enterpriseintegrationpatterns.com/Normalizer.html) between SQS and EventBridge, implemented using an EventBridge Pipe. The pipe uses a Step Functions workflow to unify the events.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/normalizer-pattern-cdk

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
    cd serverless-patterns/normalizer-pattern-cdk/src
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

This template demonstrates how EventBridge Pipes can filter events between two Kinesis streams. The pipe uses a filter to discard unwanted messages and an input transformer to select which attributes to keep for the remaining messages. Use the AWS Lambda function as described below to generate sample events.

## Testing

Step-by-step instructions to understand the implementation for the pattern:

1. Deploy the ContentFilterStack
1. Trigger the ContentFilterTestLambda-function to generate two sample events on the sourceStream.
1. Look at the SourceStream: you will find two records per ContentFilterTestLambda-execution, including PII-data.
1. Look at the TargetStream, you will find that only the ORDER event has been forwarded, and it does not contain personal data anymore.

## Cleanup
 
Delete the stack
    ```cdk destroy```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
