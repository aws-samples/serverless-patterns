# Amazon API Gateway to Lambda to Amazon EFS

This pattern attaches an EFS file system to your Lambda function to give it expandable, persistent storage. Having this level of storage in a Lambda function opens the door to many new possibilities (multiple functions can even use the same file system)

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-http-api-lambda-efs-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd lambda-efs-cdk
    ```
1. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
1. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
1. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```bash
    cdk synth
    ```
1. From the command line, use CDK to deploy the stack:
    ```bash
    cdk deploy
    ```
1. Cleanup
    
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.


## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

This pattern creates API Gateway HTTP API where any url you hit gets directed to a Lambda Function that is integrated with EFS.

## Example 
Our deployed Lambda Function is acting as a shared message broker. It allows you to send messages to it which it stores in EFS, then you can retrieve all messages to read them or delete all messages after you have finished reading.

The Lambda Function will behave differently based on the RESTful verb you use:

    GET - Retrieve messages
    POST - Send a message (whatever you send in the body is the message)
    DELETE - Deletes all stored messages

The URL for the HTTP API to use these commands will be printed in the CloudFormation stack output after you deploy.
Postman can be used to read/write text using API URL printed in output of the cdk deploy command.

Note - After deployment you may need to wait 60-90 seconds before the implementation works as expected. There are a lot of network configurations happening so you need to wait on propagation


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


## Useful References
[Using Amazon EFS with Lambda] (https://docs.aws.amazon.com/lambda/latest/dg/services-efs.html)
[[Configuring file system access for Lambda functions] https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html
Using Amazon EFS for AWS Lambda in your serverless applications] (https://aws.amazon.com/blogs/compute/[using-amazon-efs-for-aws-lambda-in-your-serverless-applications/
Danilo Poccia - A Shared File System for Your Lambda Functions] https://aws.amazon.com/blogs/aws/new-a-shared-file-system-for-your-lambda-functions/)

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
