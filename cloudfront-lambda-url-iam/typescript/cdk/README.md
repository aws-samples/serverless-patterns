# CloudFront to Lambda URL

This pattern demonstrates how to setup Amazon CloudFront to proxy and cache traffic to AWS Lambda Function URLs, secured via IAM and Lambda@Edge. 

A function URL is a dedicated endpoint for your Lambda function. When you create a function URL, Lambda automatically generates a unique URL endpoint for you. Unlike API Gateway endpoints, using this URL does not incur any additional charges, beyond the usual data transfer costs.

By configuring CloudFront in front of the Lambda Function URL endpoint you can use custom domain names, Cognito authentication via Lambda@Edge, AWS Web Application Firewall (WAF) and AWS Shield Advanced to protect your endpoint from attacks.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudfront-lambda-url-iam-cdk-ts.

Note: the Lambda@Edge uses pure Javascript instead of Typescript due to the limitations of the [Lambda@Edge CDK construct](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.experimental.EdgeFunction.html), which does not offer a native Typescript packaging option.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured with your account's credentials
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Modify the `cdk/bin/cdk.ts` and `cdk/lib/lambda-edge/authEdge.js` with your prefered region (the default is `eu-central-1`)    
1. Change directory to the pattern directory:
    ```bash
    cd cloudfront-lambda-url-iam-cdk-ts/cdk
    ```    
1. From the command line, install the Node.js dependencies, bootstrap CDK in your AWS account, and finally deploy the pattern:
    ```bash
    npm i
    npx cdk bootstrap
    npx cdk deploy CdkStack
    ```
1. Note the outputs from the CDK deployment. The `CdkStack.CloudFrontDistributionURL` contains the URL of the cloudfront distribution that you can use to test the deployment.

## How it works

An Amazon CloudFront distribution is created that forwards requests to the domain name of the deployed AWS Lambda function URL. Amazon CloudFront also caches responses from the Lambda function. The Lambda URL is protected via IAM and can only be called via the CloudFront distribution which includes a Lambda@Edge adding the necessary IAM credentials.

## Testing

Copy the url of the CloudFront distribution that you can find in the `cdk deploy` command output, called `CdkStack.CloudFrontDistributionURL`. Paste this URL in a browser and you will get a JSON response.

```bash
{"message":"Hello, world!"}
```

## Cleanup

Delete all deployed resources

```bash
npx cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
