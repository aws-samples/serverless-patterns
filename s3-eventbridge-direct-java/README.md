# Amazon S3 to Amazon EventBridge - Publish events directly from S3

The SAM template deploys an S3 bucket that publishes events to Amazon EventBridge, and sets up a Lambda function to show how to consume these events via an EventBridge rule. It deploys the IAM resources required to run the application.

This version is a Java port of the [original pattern](https://serverlessland.com/patterns/s3-eventbridge).

EventBridge consumes events directly from S3 buckets when the NoticationConfiguration is enabled, as shown in the template. Learn more about this setting in the documentation at https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications-eventbridge.html.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd s3-eventbridge-direct-java
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:
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

* Upload an object to the deployed S3 bucket.
* The Lambda function is invoked with the event from S3, routed via EventBridge.

## Example payload

The event delivered to the EventBridge rule target (a Lambda function in this example) has the following structure:

```
    {
        "version": "0",
        "id": "5d1069c2-1234-1234-1234-123456789012",
        "detail-type": "Object Created",
        "source": "aws.s3",
        "account": "123456789012",
        "time": "2021-12-10T12:55:54Z",
        "region": "us-east-1",
        "resources": [
            "arn:aws:s3:::eb-s3-test-sourcebucket-123456789012"
        ],
        "detail": {
            "version": "0",
            "bucket": {
                "name": "eb-s3-test-sourcebucket-123456789012"
            },
            "object": {
                "key": "small-test-file.txt",
                "size": 2726,
                "etag": "123456789012123456789012123456789012",
                "sequencer": "123456789012"
            },
            "request-id": "123456789012",
            "requester": "123456789012",
            "source-ip-address": "123.123.123.123",
            "reason": "PutObject"
        }
    }
```

## Testing

1. Run the following S3 CLI command to upload an object to the S3 bucket. Note, you must edit the *SourceBucketName* placeholder with the name of the S3 Bucket. This is provided in the stack outputs.

```bash
aws s3 cp './events/example.jpg'  s3://*SourceBucketName*
```

2. Run the following command to check to get the logs from the deployed Lambda function (use the function name from the stack output):

```bash
sam logs -n *FunctionName* --region *YourRegion*
```

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
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
