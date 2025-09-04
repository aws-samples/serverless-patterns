# Amazon DynamoDB to S3 with zero-ETL using AWS Glue with Terraform

This pattern demonstrates how to create a zero-ETL integration between Aamazon DynamoDB and Amazon S3 using AWS Glue transformation job. The AWS Glue job copies data in the specified format, which can be queried usind Amazon Athena.

Learn more about this pattern at Serverless Land Patterns: Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/terraform-dynamodb-glue-s3-integration

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://www.terraform.io/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd terraform-dynamodb-glue-s3-integration
    ```
3. Run below terraform commands to deploy to your AWS account in the desired region (default is us-east-1):
    ```
    terraform init
    terraform validate
    terraform plan -var region=<YOUR_REGION>
    terraform apply -var region=<YOUR_REGION>
    ```

## How it works

This Terraform pattern creates a zero-ETL integration that automatically exports DynamoDB data to S3 using AWS Glue. The AWS Glue job reads from the Amazon DynamoDB table and writes the data in the specified format (currently specified as Parquet in the script) to an encrypted Amazon S3 bucket for potential use in analytics and/or for long-term storage. The entire infrastructure is provisioned with the required IAM permissions, and includes automated testing script to validate the data pipeline functionality.

## Testing

After deployment, run ./test.sh. This script adds rows to Amazon DynamoDB database and triggers then the AWS Glue job. Once the job is complete, check Amazon S3 for the target files.

## Cleanup
 
1. Delete the stack
    ```
    terraform destroy -var region=<YOUR_REGION>
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
