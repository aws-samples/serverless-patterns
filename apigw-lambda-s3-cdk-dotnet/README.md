# Amazon API Gateway API to AWS Lambda for S3 Presigned URL

This pattern helps you to deploy a CDK stack with API Gateway, Lambda, and S3 bucket. For an HTTP GET request with the query string of an object key to the APIGateway Endpoint backed by AWS Lambda Function will generate the PresignedURL for the object available in the S3 Bucket.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet)
    - 3.1 for the CDK Stack - https://dotnet.microsoft.com/en-us/download/dotnet/6.0
    - 6.0 for the Lambda Function - https://dotnet.microsoft.com/en-us/download/dotnet/6.0
* [Docker](https://docs.docker.com/get-docker/) installed and running
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-lambda-s3-cdk-dotnet/cdk
    ```
3. Install dependencies
    ```
    dotnet restore/src
    ```

4. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```
5. The output contains the APIGateway Endpoint url.

## How it works

An HTTP GET request with the querystring of an object key to the APIGateway Endpoint backed by AWS Lambda Function will yeild the PresignedURL for the object available in the S3 Bucket.


## Testing

Open the enbdpoint in the browser and click or copy paste the generated url in a new tab to view the object.

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
