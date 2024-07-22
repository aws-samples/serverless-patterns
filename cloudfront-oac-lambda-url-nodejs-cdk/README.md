# Amazon CloudFront Origin Access Control for AWS Lambda Function URL

This pattern shows how to protect AWS Lambda URL origins by using CloudFront Origin Access Control (OAC) to only allow access from designated CloudFront distributions.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change the working directory to this pattern's directory
    ```bash
    cd cloudfront-oac-lambda-url-nodejs-cdk
    ```

3. Install dependencies
    ```bash
    npm install
    ```

4. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL.
    ```bash
    cdk deploy
    ```

## How it works
Amazon CloudFront will use Origin Access Control (OAC) to authenticate access to Lambda Function URLS from their designated CloudFront distributions.

## Testing

The solution can be validated by accessing the URLs provided in the CloudFormation output:  

1. Positive testing - Check the output for a hello world message
    ```bash
    curl <cloudfrontUrl>
   
   "Hello from Lambda Function URL!"
    ```

2. Negative testing - Check the output for Forbidden access error
    ```bash
    curl <lambdaUrl>
   
   {"Message":"Forbidden"}
    ```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```bash
cdk destroy
```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0