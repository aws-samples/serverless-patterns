# Amazon S3 to AWS SQS 

Sends notifications from S3 to SQS when an object is created

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-sqs-dotnet-cdk](https://serverlessland.com/patterns/s3-sqs-dotnet-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [.NET](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) (.NET Core 3.1) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change the working directory to this pattern's directory
    ```
    cd s3-sqs-dotnet-cdk
    ```

1. Build the .NET CDK project
    ```
    dotnet build src
    ```

1. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL.
    ```
    cdk deploy
    ```

1. Note the outputs from the CDK deployment process. This contains the S3 <BUCKET_NAME> and SQS <QUEUE_URL> attributes used to test this deployment.

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
