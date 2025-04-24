# Amazon SQS to Amazon S3 integration using AWS Lambda

This pattern creates an SQS queue, a Lambda function, an S3 bucket along with event source mapping for the Lambda function and appropriate permissions to enable the interfacing between these resources.

An example of where this pattern could be useful is **handling large number of deployment requests asynchronously**. Given that deployment requests can vary in terms of application target and payload, this pattern can be employed as an _entry point_ component for deployment systems, that receive and process a large number of requests for deployments across multiple applications. Requests can be processed in batches and outcomes can be saved on the S3 bucket, which can further trigger notifications workflows.

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

1. Pick a unique name for the target S3 bucket eg. `my-bucket-20250329`. Replace the bucket name and AWS region in `variables.tf`:

    ```
    variable aws_region_name {
        type = string
        default = "ap-south-1"
        description = "AWS Region"
    }

    variable "s3_bucket_name" {
        type = string
        default = "my-bucket-20250329"
        description = "S3 Bucket name"
    }
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

1. Before the test script can be executed, a few pre-steps should be completed:

    1. IAM user creation - [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
    2. Grant permissions to IAM user - [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)
    3. Generate access key pair for IAM user - [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
    4. Configure AWS CLI - [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)

1. Update the AWS region in the test script `send_sqs_event.py` with the region, in which the SQS queue will be created:
    
    ```
    config = Config(region_name='ap-south-1')
    ```

1. Run the test script:
    
    ```
    python send_sqs_event.py
    ```

1. Check the S3 bucket to see if a new JSON object has been created:

    ```
    aws s3 ls [bucket-name]
    ```

    Alternately, the S3 bucket can be looked up on the AWS Console.

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
