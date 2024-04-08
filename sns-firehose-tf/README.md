# Amazon SNS to Amazon Kinesis Data Firehose

This pattern publishes SNS messages to a Kinesis Firehose Delivery Stream so that they can be forwarded to archival or analytics destinations.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sns-firehose-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change the working directory to this pattern's directory

   ```sh
   cd serverless-patterns/sns-firehose-tf
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
    * Enter a bucket name
    * Enter yes

1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This template creates an SNS Topic, Kinesis Firehose Delivery Stream, S3 bucket, and subscribed the Kinesis Firehose Delivery Stream to the SNS Topic. As messages are published to the topic, they are streamed to the Firehose Delivery Stream, and then delivered the the Firehose Delivery Stream's destinations, which in this case is an S3 bucket. 

## Testing

1. Publish a message to the SNS topic by running the CLI command: 
```
aws sns publish --topic-arn arn:aws:sns:us-east-1:{AWS ACCOUNT NUMBER}:SourceSNSTopic-TF --message "Hello world"
```

2. Check that test messages are being sent to the destination S3 bucket (it will take a few minutes for events to begin streaming):

```
aws s3 ls s3://{destination bucket name} --recursive --human-readable --summarize
```

## Cleanup

1. Change directory to the pattern directory:
    ```
    cd sns-firehose-tf
    ```
1. Delete the files if you have published the message from SNS because bucket will be not deleted if any files exist.
    ```
    aws s3 rm s3://{destination bucket name} --recursive
    ```
1. Delete all created resources by terraform
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter a bucket name
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
