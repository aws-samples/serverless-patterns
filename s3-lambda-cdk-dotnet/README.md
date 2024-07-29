# AWS Lambda function that reads file information when file is uploaded to Amazon S3 bucket using AWS CDK.

This AWS CDK application shows triggering a AWS Lambda function, when a file is uploaded in a S3 bucket.

This pattern provides a solution for accessing the file information from AWS Lambda function, when a new file is uploaded to a S3 bucket. An ideal use case for this is reading various file types e.g. image, csv, text, pdf files and extracting its metadata information and other file contents for further processing or just passing this information to downstream systems.

## Architecture 
![architecture diagram](images/architecture.png)

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-lambda-cdk-dotnet

**Important**: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory.
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change the working directory.
    ```
    cd s3-lambda-cdk-dotnet/src
    ```
3. Build the .NET CDK project
    ```
    dotnet build src
    ```
4. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## Testing

1. After deployment, upload a sample file to the S3 bucket that was created by the stack.
2. Check the Lambda function logs in the CloudWatch log groups. You should see the file name of file you uploaded, in the function logs.


## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
