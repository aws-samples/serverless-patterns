# Serving private content from CloudFront with signed URLs and signed cookies

This pattern demonstrates how to use CloudFront to securely serve private content.

In this pattern, the CDK stack creates an S3 bucket and a CloudFront distribution that is configured to accept requests with only valid signed URLs or signed Cookies.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudfront-s3-cdk-dotnet

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 7](https://dotnet.microsoft.com/en-us/download/dotnet/7.0) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change the working directory to this pattern's directory
    ```
    cd cloudfront-s3-cdk-dotnet/src/cdk/src
    ```
3. Build the application
    ```
    dotnet build
    ```
4. Return one level back to the path `cloudfront-s3-cdk-dotnet/src/cdk`
    ```
    cd..
    ```
5. Deploy the stack to your default AWS account and region. The output of this command should give you the signed URL of a `sample.pdf` document.
    ```
    cdk deploy
    ```

## Testing

1. After deployment, the output displays two URLs, one signed and one normal.
   - `CloudFrontToS3CdkStack.PDFFileSignedURL = https://d1vdgbnd2t5hch.cloudfront.net/sample.pdf?Policy=eyJTdGF......`
   - `CloudFrontToS3CdkStack.PDFFileURL = https://d1vdgbnd2t5hch.cloudfront.net/sample.pdf`
2. Try to access the resource `sample.pdf` using both URLs.
3. It should only be accessible via the signed URL.


## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
