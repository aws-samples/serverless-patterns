# Amazon CloudFront to AWS Lambda URLs

This pattern demonstrates how to setup Amazon CloudFront to proxy and cache traffic to AWS Lambda Function URLs. 

A function URL is a dedicated endpoint for your Lambda function. When you create a function URL, Lambda automatically generates a unique URL endpoint for you.

By configuring CloudFront infront of the Lambda Function URL endpoint you can use custom domain names, AWS Web Application Firewall (WAF) and AWS Shield Advanced to protect your endpoint from attacks.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd cloudfront-lambda-url-java
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

An Amazon CloudFront distribution is created that forwards requests to the domain name of the deployed AWS Lambda function URL. Amazon CloudFront also caches responses from the Lambda function. 

## Testing

Getting the CloudFront domain from the stack deployment we can test it using Curl. 

```bash
curl -D - https://dsd6hgzvwqfxn.cloudfront.net/
HTTP/2 200 
content-type: text/plain
content-length: 12
date: Thu, 21 Apr 2022 04:20:14 GMT
x-amzn-requestid: 0f803e2e-dc5e-4c3e-8f90-8ab3a1b0f337
x-amzn-trace-id: root=1-6260db7e-685b10df5828b0284f923adb;sampled=0
x-cache: Miss from cloudfront
via: 1.1 a63f63c0130cd2db055700cdbe2c6c88.cloudfront.net (CloudFront)
x-amz-cf-pop: SYD62-P1
x-amz-cf-id: Jw_dYSCio5elb-XgDYILECjKH9yPr9YNg91TrLFod70hpMn_frUD8Q==
age: 103

Hello, World
```

Note that if we make a second request we get a hit from the cache. 

```bash
curl -D - https://dsd6hgzvwqfxn.cloudfront.net/
HTTP/2 200 
content-type: text/plain
content-length: 12
date: Thu, 21 Apr 2022 04:20:14 GMT
x-amzn-requestid: 0f803e2e-dc5e-4c3e-8f90-8ab3a1b0f337
x-amzn-trace-id: root=1-6260db7e-685b10df5828b0284f923adb;sampled=0
x-cache: Hit from cloudfront
via: 1.1 3437ef72cec711eb0ebed9222a22cf66.cloudfront.net (CloudFront)
x-amz-cf-pop: SYD62-P1
x-amz-cf-id: cNb50PRL1QrfFk-OWOggN3QN738Y0SL8t7_xkNjTVk-Sr-IMOqjRsg==
age: 401

Hello, World
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
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
