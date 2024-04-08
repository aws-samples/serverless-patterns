# API Gateway Websockets - Lambda - Step Functions - Transcribe - Translate - Polly - S3

This pattern demonstrates the use of API Gateway, Lambda, Step Functions, Transcribe, Translate, Polly and S3 to create an online language converter app.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Programming Language

This is a Maven project which uses Node.js and WebPack along with AWS SDK for Javascript.

## Services

The AWS services used in this pattern are

- Amazon API Gateway
- Amazon S3
- AWS Lamdba
- AWS Step Functions
- Amazon Transcribe
- Amazon Translate
- Amazon Polly

<img src="Architecture.png" alt="architecture" width="62%"/>

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
    cd apigw-lambda-sfn-transcribe-translate-polly-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

API Gateway handles incoming traffic and sends it to the lambda which in turn invokes the step function. The step function orchestrates the process to transcribe for converting speech to text, then to translate for language translation of the text file and finally to polly for converting text to speech and store the audio file in S3. The step function at last returns the S3 signed url to the lambda which is returned as response from API Gateway websockets.

## Testing

Follow the steps to test the pattern:

1. Copy the audio to the S3 audio input bucket
    ```bash
    aws s3 cp audio.mp3 s3://{bucket-name}
    ```
1. Run the curl command to invoke the API Gateway
    ```bash
    curl
    ```
1. Play the audio file.

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0