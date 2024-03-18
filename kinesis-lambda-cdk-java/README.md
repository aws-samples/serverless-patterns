# Kinesis Data Streams integration with Lambda using the AWS CDK in Java

This pattern creates an Amazon [Kinesis Data Stream](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) and an AWS [Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), using the AWS Cloud Development Kit (AWS CDK) in Java.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/kinesis-lambda-cdk-java](https://serverlessland.com/patterns/kinesis-lambda-cdk-java).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
    cd serverless-patterns/kinesis-lambda-cdk-java
    ```
3. From the command line, use AWS CDK to deploy the AWS resources for the serverless application as specified in the MyServerlessApplicationStack.java file:
    ```
    cdk deploy
    ```

## How it works

When data is sent to the Kinesis data stream, the Lambda function will be triggered and process data from the stream.

## Testing

From the command line, run the following command to send a single data record to the Kinesis data stream. Note that you must edit the {MyServerlessApplicationStack.KinesisLambda-KinesisStream} with the Kinesis data stream ARN that is deployed. This is provided in the MyServerlessApplicationStack deployment outputs.

```
aws kinesis put-record --stream-arn {MyServerlessApplicationStack.KinesisLambda-KinesisStream} --partition-key 123 --data testdata
```

## Cleanup

1. From the command line the AWS CDK to delete the Serverless application stack
   ```
   cdk destroy
   ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
