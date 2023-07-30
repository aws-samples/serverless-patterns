# Amazon API Gateway HTTP API to Amazon EventBridge

This repo contains serverless patterns showing how to integrate Simple Notification Service, Simple Queue Service and Lambda with Serverless framework.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigateway-http-eventbridge-lambda-sls](https://serverlessland.com/patterns/apigateway-http-eventbridge-lambda-sls).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ``` sh
    cd serverless-patterns/sns-sqs-lambda-sls-ts
    ```

1. From the command line, use npm to install the development dependencies:

    ``` sh
    npm install
    ```

1. From the command line, use Serverless Framework to deploy the AWS resources for the pattern as specified in the serverless.yml file:

    ``` sh
    sls deploy --stage dev
    ```
   
## How it works

This pattern creates a SNS topic with an SQS subscription. The SQS queue is consumed by a lambda that is triggered for each SQS event.


## Cleanup

1. Delete the stack

    ```sh
    sls remove --stage dev
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0