# Amazon S3 to Amazon SNS

This pattern sends notifications from S3 to SNS when an object is created

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-sns-terraform](https://serverlessland.com/patterns/s3-sns-terraform)

Important: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd s3-sns-terraform
    ```
1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This template creates an S3 bucket, allows you to upload objects to that bucket, and will send you notifications from S3 to SNS when an object is created in that bucket.

## Testing
1. Subscribe your email address to the SNS topic:
    ```bash
    aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email-json --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS
    ```
1. Click the confirmation link delivered to your email to verify the endpoint.
1. Upload an object to the S3 bucket created by the deployment. You can also use the below command to upload a file:
    ```bash
    aws s3 cp README.md s3://ENTER_YOUR_S3_BUCKET_NAME
    ```
1. The s3 notification is delivered to your email address.

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd s3-sns-terraform
    ```
1. Delete all files from the S3 bucket
1. Delete all created resources by terraform
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0