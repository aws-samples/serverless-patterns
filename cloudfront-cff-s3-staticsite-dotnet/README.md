# AWS S3 Hosting Static Site with CloudFront

This pattern helps you deploy a static site using Amazon CloudFront with Function and AWS S3 with a CDK stack. It use MKDOCS to generate the Static site from the Markdown files.

MkDocs is a fast, simple static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. For more [info](https://www.mkdocs.org/).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet)
    - 3.1 for the CDK Stack - https://dotnet.microsoft.com/en-us/download/dotnet/6.0
* [Docker](https://docs.docker.com/get-docker/) installed and running
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [MKDOCS](https://www.mkdocs.org/user-guide/installation/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns
    cd cloudfront-cff-s3-staticsite-dotnet
    ```
3. Install dependencies
    ```
    dotnet restore .\src\
    ```
4. Generate the Mkdocs Build Static Content
    ```
    cd mycontent && mkdocs build && cd ..
    ```
5. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## How it works

The generated static site will stored in S3 and served through CLoudFront. For each request to CloudFront, the Function and append index.html at the end of it, if not requested.

## Testing

On successful deployment, you will be able access the markdown site.

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
