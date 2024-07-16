# AWS Lambda sending a notification when a new Amazon S3 bucket is created

This pattern creates an automated monitoring system for Amazon S3 bucket create events. It defines an Amazon EventBridge rule that listens for S3 bucket creation events and invokes an AWS Lambda function. The Lambda function processes the event details and sends a notification to an Amazon SNS topic, informing subscribers of the new bucket creation.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-s3-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.cxom/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-s3-lambda
    ```
1. From the command line, initialize terraform to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts
    #var.region
    - Enter a value: {enter the region for deployment}

## Testing

1. After deploying the stack, create a Subscriber for your Amazon SNS topic (For ex, your email) and confirm the subscription.
    https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html

1. Create a new S3 bucket using the following CLI command
    ```
    aws s3api create-bucket --bucket BUCKET_NAME --region REGION_NAME
    ```
    Note: Make sure that the region is same as the region in which you deployed the Terraform code.

1. The event invokes the Lambda function and you will receive an email from the SNS Topic.

## Cleanup

1. Delete the SNS Subscription:
    Go to SNS > Subsciptions > Select your Subscription and click on Delete

    https://docs.aws.amazon.com/sns/latest/dg/sns-delete-subscription-topic.html

1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-s3-lambda
    ```
1. Delete all created resources
    ```
    terraform destroy
    ```
    
1. During the prompts:
    ```
    Enter all details as entered during creation.
    ```
1. Confirm all created resources has been deleted
    ```
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
