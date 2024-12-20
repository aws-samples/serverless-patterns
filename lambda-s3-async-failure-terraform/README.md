# Asynchronous Lambda with S3 Destination for Failed Invocations

This pattern demonstrates how to set up an AWS Lambda function with asynchronous invocation and S3 destination for failed executions using Terraform. The pattern includes configuration for zero concurrency to test failure handling, and uses a random UUID for unique S3 bucket naming.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-s3-async-failure-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-s3-async-failure-terraform
    ```
3. From the command line, initialize Terraform to download and install the providers defined in the configuration:
    ```
    terraform init
    ```
4. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
5. During the prompts:
    * Enter yes to apply the configuration

## How it works

This pattern creates:
- A Lambda function configured for asynchronous invocation
- An S3 bucket with a random UUID suffix as the destination for failed executions
- IAM roles and policies for Lambda and S3 interaction
- Zero concurrency configuration to demonstrate failure handling

The Lambda function includes a parameter `forceError` that when set to true will trigger an exception, allowing you to test the failure handling mechanism.

## Testing

1. Test successful execution (will still fail due to zero concurrency):
```bash
aws lambda invoke \
  --function-name async_function \
  --invocation-type Event \
  --payload '{"forceError": true}' \
  response.json
```
2. Check the S3 bucket for failure redords:
```bash
aws s3 ls s3://[YOUR-BUCKET-NAME]
```


## Cleanup

1. Empty the bucket.
   
2. Delete all created resources:
```bash
terraform destroy
```

***

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0