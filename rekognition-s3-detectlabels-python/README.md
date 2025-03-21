# Amazon S3 to Amazon Rekognition through AWS EventBridge

This pattern demonstrates how to create an Amazon S3 bucket that triggers an AWS Lambda function via Amazon EventBridge upon object upload. The Lambda function detects labels in an image using Amazon Rekognition. The Lambda function is built using Python.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/rekognition-s3-detectlabels-python

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
    cd rekognition-s3-detectlabels-python
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The CloudFormation template creates two Amazon S3 buckets (source and destination) along with an AWS Lambda function (written in Python) and an Amazon EventBridge event. The Lambda function is triggered by EventBridge, which listens for object uploads in the S3 source bucket. The Lambda function makes a `DetectLabels` API call to Amazon Rekognition to detect labels in an image and stores the output in the destination S3 bucket.

## Testing

Upload the file (document/image) to the input S3 `<STACK_NAME>-input-bucket-<AWS_ACCOUNTID>` bucket via the console or use the `PutObject` API call below:

```
aws s3api put-object --bucket <INPUT_BUCKET_NAME> --key <IMAGE_FILE> --body /path/to/your/<IMAGE_FILE>
```
The output of the operation can be downloaded from the output S3 bucket <STACK_NAME>-output-bucket-<AWS_ACCOUNTID>.

Replace the parameters in the above command appropriately.

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
