# Kinesis Data Streams with Lambda Integration

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
   the lambda functions residing in software directory.

    ```bash
    cdk synth
    ```
5. From the command line, use AWS CDK to deploy the AWS resources.

    ```bash
    cdk deploy
    ```
   Alternatively infrastructure/deploy.sh can be used to build and deploy the stack

6. Note the outputs of CDK and copy the Kinesis Resource Name. Use the copied stream name in the producer.sh file which will be used in the next step to put records in to the stream created.

## How it works

This Kinesis-Lambda integration pattern makes use of the aws-kinesisstreams-lambda [Solution construct](https://docs.aws.amazon.com/solutions/latest/constructs/aws-kinesisstreams-lambda.html) to create the infrastructure.

Lambda get triggered based on the events from the Kinesis Data Stream. For any error in invocation of the lambda function events are persisted in the configured dead-letter SQS queue.

In the example the Kinesis Event Source is configured with `maxretryattempt` as 1, bisectBatchOnError set to true, and `reportBatchItemFailures` set to true with batch size of 3.

Lambda code has been updated to handle exception on any error due to event processing as per the best practice to return the sequence number. Using this configuration and approach duplicate message reprocessing can be avoided. 

For more details on handling Success and Failure conditions in Kinesis data streams consumption, refer the [documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-errors).
## Testing
Update the producer.sh file with Kinesis stream name which got created. Update the number of messages to get published in to the stream by updating the number in loop as shown in the below statement

while [ $a -lt 24 ]

From the command line

   ```bash
   cd ../software
   cd KinesisCliProducers
   sh producers.sh
   ```
This will publish the messages in the Kinesis stream and the lambda function gets triggered based on that.

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0