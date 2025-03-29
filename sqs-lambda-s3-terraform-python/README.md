# Amazon SQS to Amazon S3 integration using AWS Lambda

This pattern creates an SQS queue, a Lambda function, an S3 bucket along with event source mapping for the Lambda function and appropriate permissions to enable the interfacing between these resources.

Learn more about this pattern at Serverless Land Patterns: [SQS to Lambda to S3](https://serverlessland.com/patterns/sqs-lambda-s3)

**Important:** this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* **AWS Resources**<br>
    Creation of AWS resources requires the following:
    * [AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) - An AWS account is required for creating the various resources. If you do not already have one, then create an account and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
    * [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - This is required for cloning this repo.
    * [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) - Terraform is an IaC (Infrastructure as Code) software tool used for creating and managing AWS resources using a declarative configuration language.

* **Test Setup**<br>
    In order to test this integration, the following are required:
    * [Python](https://wiki.python.org/moin/BeginnersGuide/Download) is required to run the test script.
    * [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) is a prerequisite for using boto3 module in the test script.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sqs-lambda-s3-terraform-python
    ```
1. Pick a unique name for the target S3 bucket eg. `my-bucket-20250329`. Replace the bucket name in following files:

    * Lambda handler - `handler.py`
        
        ```
        resp = s3_client.put_object(
            Body=str(request_body).encode(encoding="utf-8"),
            Bucket='my-bucket-20250329',
            Key=file_name
        )
        ```
    * Terraform configuration - `main.tf`
        
        ```
        # S3 bucket
        resource "aws_s3_bucket" "event-storage" {
            bucket        = "my-bucket-20250329"
            force_destroy = true
            tags = {
                Name = "event-storage"
            }
        }
        ```
1. Update the AWS region in the following files with the region, in which the resources will be created:

    * Lambda handler - `handler.py`
        
        ```
        config = Config(region_name='ap-south-1')
        ```
    * Terraform configuration - `main.tf`
        
        ```
        provider "aws" {
            region = "ap-south-1"
        }
        ```

1. Compress the lambda handler to generate a zip file:
    
    ```
    cp handler.py handler_1.py
    gzip -S .zip handler.py
    mv handler.py.zip sqs-lambda-s3.zip
    mv handler_1.py handler.py
    ```

1. Deploy the AWS resources through Terraform:
    
    ```
    terraform init -upgrade
    terraform fmt
    terraform validate
    terraform apply -auto-approve
    ```

## How it works

The AWS resources created as a part of this integration are as follows:

* Amazon SQS queue
* AWS Lambda function
* Amazon S3 bucket
* IAM policies and roles

The SQS queue is configured as a trigger for the Lambda function. Whenever a message is posted to the SQS queue, the Lambda function is invoked synchronously. This is useful in scenarios, where the message requires some pre-processing before storage.

## Testing

1. Create an IAM user which will be used for writing messages on the SQS queue

2. Add persmissions for the IAM user through the following inline policy:
    
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "sqs:DeleteMessage",
                    "sqs:TagQueue",
                    "sqs:UntagQueue",
                    "sqs:ReceiveMessage",
                    "sqs:SendMessage"
                ],
                "Resource": "arn:aws:sqs:[AWS_REGION]:[AWS_ACCOUNT]:event-collector-queue"
            }
        ]
    }
    ```
    Replace `[AWS_REGION]` and `[AWS_ACCOUNT]` in the above policy before attaching with the IAM user.

1. Generate an access key pair (access key and secret access key) for IAM user in the AWS CLI. The key pair will be used while running the test script.

1. Update the AWS region in the test script `send_sqs_event.py` with the region, in which the SQS queue will be created:
    
    ```
    config = Config(region_name='ap-south-1')
    ```

1. Run the test script:
    
    ```
    python send_sqs_event.py
    ```

1. Enter the Access Key and Secret Access Key when prompted:

    ```
    Enter Access Key: ********************
    Enter Secret Access Key: ****************************************
    ```

1. Check the S3 bucket to see if a new JSON object has been created:

    ```
    aws s3 ls --region ap-south-1 my-bucket-20250329
    ```

## Cleanup
 
1. Delete the AWS resources through Terraform:

    ```
    terraform apply -destroy -auto-approve
    ```

## Resources

* [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
* [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
* [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
