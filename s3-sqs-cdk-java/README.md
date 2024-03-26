# Amazon S3 to AWS SQS

Sends notifications from S3 to SQS when an object is created

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-sqs-cdk-java](https://serverlessland.com/patterns/s3-sqs-cdk-java)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change the working directory to this pattern's directory
    ```
    cd serverless-patterns/s3-sqs-cdk-java
    ```

3. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 1111111111/us-east-1
   cdk bootstrap --profile test 1111111111/us-east-1
   ```
4. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```
5. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This CDK stack creates an S3 bucket, allows you to upload objects to that bucket, and will send notifications from S3 to SQS when an object is created in that bucket.

## Testing

1. Upload an object to the S3 bucket created by the deployment.
    ```bash
    aws s3 cp 'test-file-to-upload.txt'  s3://<BUCKET_NAME>
    ```

1. You can then use the SQS CLI to fetch new messages from the queue:
    ```bash
    aws sqs receive-message --queue-url <QUEUE_URL> --max-number-of-messages 10
    ```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
