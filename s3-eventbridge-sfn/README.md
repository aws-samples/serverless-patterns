# Amazon S3 to AWS Step Functions via Amazon EventBridge

The SAM template deploys an Amazon S3 bucket that publishes events to Amazon EventBridge, and sets up an AWS Step Functions workflow to show how to consume these events via an EventBridge rule. It deploys the the IAM resources required to run the application. EventBridge consumes events directly from S3 buckets when the NoticationConfiguration is enabled, as shown in the template. The template contains a sample Step Functions workflow that detects cats in images uploaded to the Amazon S3 bucket using Amazon Rekognition's DetectLabels API. Replace this workflow with your own state machine.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-eventbridge-sfn

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd s3-eventbridge-sfn
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   sam deploy --guided
   ```
1. During the prompts:

   - Enter a stack name
   - Enter the desired AWS Region
   - Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern sets up the following resources:

- An Amazon S3 bucket that is configured to send any events regarding its content, such as an `Object created` event that is emitted when an object is uploaded to the bucket, to Amazon EventBridge.
- An Amazon EventBridge rule that triggers a Step Functions workflow if a new `Object created` event is emitted by the S3 bucket. The workflow receives an [EventBridge event message](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-events.html) as its input which contains information such as the name of the S3 bucket and the key of the uploaded image.
- A sample AWS Step Functions workflow that calls the Amazon Rekognition [`DetectLabels API`](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html) to identify objects in an uploaded to the S3 bucket. The workflow posesses an IAM role that authorizes it to read from the S3 bucket and to call Rekognition.

## Testing

1. In the Outputs tab of the AWS CloudFormation console, note the `IngestionBucket` and `CatDetectorStateMachine` outputs.
1. In the Amazon S3 console, upload two images to the `IngestionBucket`: one containing a cat and one not containing a cat.
1. In the AWS Step Functions console, find two new workflow executions for the `CatDetectorStateMachine` workflow. The workflow results will show if a cat was detected in the respective image or not.

## Cleanup

Delete the stack:

```bash
sam delete
```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
