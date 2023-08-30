# Kinesis DataStreams with Lambda Integration

![architecture diagram](architecture.png)

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Java 11+](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html) installed
* [Docker](https://docs.docker.com/get-docker/) Installed
## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:

    ```
    cd serverless-patterns/cdk-kinesis-lambda-java
    ```
3. From the command line, use AWS CDK to deploy the AWS resources for the serverless application

    ```bash
    cd infrastructure
    ```
4. From the command line, Synthesize the cdk stack to emits the synthesized CloudFormation template. Set up will make sure to build and package
   the lambda functions residing in [software](/software) directory.

    ```bash
    cdk synth
    ```
5. From the command line, use AWS CDK to deploy the AWS resources.

    ```bash
    cdk deploy
    ```
6. Note the outputs of CDK and copy the Kinesis Resource Name. Use the copied stream name in the producer.sh file which will be used in the next step to put records in to the stream created.

## How it works

Explain how the service interaction works.

## Testing

Provide steps to trigger the integration and show what should be observed if successful.

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