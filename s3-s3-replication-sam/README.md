# Amazon S3 Bucket Replication

This pattern demonstrates how to replicate S3 bucket objects to multiple S3 buckets. Implemented with SAM.

**Key Benefits**:

- **Data Redundancy and Durability**:
    S3 replication ensures that your data is replicated across multiple S3 buckets, offering redundancy and safeguarding against data loss.
- **Disaster Recovery**:
    By replicating your data to a different region or account, you establish a robust disaster recovery strategy. In the event of an outage or data corruption, you can quickly restore operations using the replicated data.
- **Global Content Distribution**:
    Replicate frequently accessed data to different geographical locations, reducing latency and enhancing the user experience for global audiences.
- **Compliance and Data Retention**:
    Address compliance requirements by replicating data to a separate account or region. This ensures data integrity and facilitates adherence to regulatory standards.
- **Operational Efficiency**:
    S3 replication operates asynchronously, allowing you to focus on other tasks while data is efficiently copied in the background.


Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-s3-replication-sam](https://serverlessland.com/patterns/s3-s3-replication-sam)

**Important**: This application utilizes various AWS services, and there are associated costs after Free Tier usage. Please refer to the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any incurred AWS costs. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. Ensure that the IAM user used has sufficient permissions to make necessary AWS service calls and manage resources.
* [Install and configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
* [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Install AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal, and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change the directory to the pattern directory:
    ```bash
    cd s3-s3-replication-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```bash
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name.
    * Enter the desired AWS Region.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in the future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs used for testing.

## How it Works

S3 replication in the same region involves copying objects from one S3 bucket to another within the same AWS region. When replication is configured, S3 automatically copies objects from the source bucket to the destination bucket, ensuring redundancy and data durability. This process helps in scenarios such as data backup, compliance requirements, and minimizing latency for accessing data.


## Testing

Upload some images to the source bucket, and then check the replication bucket. You should be able to see the same data replicated there.

## Cleanup
 
1. Empty buckets
    ```bash
    aws s3 rm s3://BUCKET_NAME_SOURCE --recursive
    aws s3 rm s3://BUCKET_NAME_REPLICA --recursive

    ```
2. Confirm the stack has been deleted:
    ```bash
    sam delete --stack-name STACK_NAME

    ```

----

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0