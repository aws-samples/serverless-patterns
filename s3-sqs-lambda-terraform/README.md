# Amazon S3 to Amazon SQS queue to AWS Lambda

The Terraform code deploys an AWS Lambda function, an Amazon SQS queue, one AWS S3 buckets and the AWS IAM resources required to run the application. The created Lambda function is triggered on every new `.jpg` image file uploaded to the S3 bucket using an SQS queue as a notification target. The Lambda function code contains only contains minimal code for demo purposes.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/s3-sqs-lambda-terraform](https://serverlessland.com/patterns/s3-sqs-lambda-terraform)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


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
    cd s3-sqs-lambda-terraform
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

* Use the AWS CLI or AWS console to upload an image to the source S3 Bucket
* If the object is a .jpg file, the Lambda function is triggered using SQS as a notification target.

## Testing

Run the following AWS CLI command to upload an image to the S3 bucket. Note, you must edit the {SourceBucketName} placeholder with the name of the source S3 bucket. This is provided in the stack outputs.

```bash
aws s3 cp './events/exampleImage.png'  s3://{SourceBucketName}
```

## Documentations and next step

To expand the Step Functions workflow that the pattern created, you can find out example workflows at Step Functions Workflow: [serverlessland.com/workflows](https://serverlessland.com/workflows)


## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd s3-sqs-lambda-terraform
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
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
