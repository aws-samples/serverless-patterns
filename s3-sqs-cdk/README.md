# Amazon S3 to AWS SQS 

Sends notifications from S3 to SQS when an object is created

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-sqs-cdk](https://serverlessland.com/patterns/s3-sqs-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd s3-sqs-cdk/src
    ```
3. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
4. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
5. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
6. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```bash
    cdk synth
    ```
7. From the command line, use CDK to deploy the stack:
    ```bash
    cdk deploy
    ```
8. Note the outputs from the CDK deployment process. This contains the S3 <BUCKET_NAME> and SQS <QUEUE_URL> attributes used to test this deployment.

## How it works

This CDK stack creates an S3 bucket, allows you to upload objects to that bucket, and will send notifications from S3 to SQS when an object is created in that bucket.

## Testing

1. Upload an object to the S3 bucket created by the deployment.

```bash
aws s3 cp 'test_upload.txt'  s3://<BUCKET_NAME>
```

2. You can then use the SQS CLI to fetch new messages from the queue:
    ```bash
    aws sqs receive-message --queue-url <QUEUE_URL> --max-number-of-messages 10
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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
