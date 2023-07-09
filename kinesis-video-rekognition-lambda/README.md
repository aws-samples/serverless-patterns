# Kinesis Video to Rekognition to Lambda

This pattern demonstrates how to use a Rekognition Stream Processors to analyse Kinesis Video Streams with a variety of operations and then pass the generated metadata to AWS Lambda for further processing/analytics.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd kinesis-video-rekognition-lambda/src
    ```
1. Install dependencies required by the project
    ```
    npm install
    ```
1. From the command line, configure AWS CDK with
   ```bash
   cdk bootstrap
   ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in `lib/kvs-rekognition-stack.ts` the folder:

   ```
   cdk deploy
   ```

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Leveraging the Rekognition Stream Processor Feature of Amazon Rekognition, we can have the rekognition APIs act on Kinesis Video Streams to detect and recognize faces or to detect connected home labels in a streaming video.

Rekognition Stream then outputs individual video events to Kinesis Data Streams for consumption where we set a lambda trigger for each event/batch of events to process them as necessary.

## Testing

Start the Rekognition Stream Processor with by using the Output `Rekognition Stream Processor` provided by the deploy process and put it in the following command:
    ```bash
    aws rekognition start-stream-processor --name "Rekognition Stream Processor"
    ```

Send video to the Kinesis Video Stream using the guide documented [here](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-gstreamer-plugin.html)

## Cleanup

Delete the stack from inside `kinesis-video-rekognition-lambda/src` with
   ```bash
   cdk destroy
   ```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
