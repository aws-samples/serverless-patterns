# Amazon CloudWatch Mertics Streaming to Amazon Kinesis Firehose with Terraform

This pattern demonstrates how to create the Amazon CloudWatch Metric Streams to Amazon Kinesis Firehose. Metrics are saved to S3 from Amazon Kinesis Firehose. Metric selection is also demonstrated to stream only certain metrics related to certain AWS services to be sent from Cloudwatch to Firehose.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudwatch-metric-streams-firehose-terraform

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
    cd cloudwatch-metric-streams-firehose-terraform
    ```
3. Run below terraform commands to deploy to your AWS account in desired region:
    ```
    terraform init
    terraform validate
    terraform plan
    terraform apply
    ```

## How it works
When AWS services are provisioned, the listed metrics(in the IaC) will be captured and streamed to Kinesis Firehose. The destination in this case is a S3 bucket, where the metrics are saved. The code is configured to eu-west-2, but can be changed to any desired region.

![pattern](Images/pattern.png)

## Testing

After deployment, launch an EC2 instance in eu-west-2 region, and after a few minutes the metrics data will appear in the S3 bucket.


## Cleanup

1. Delete the stack:
    ```
    terraform destroy
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
