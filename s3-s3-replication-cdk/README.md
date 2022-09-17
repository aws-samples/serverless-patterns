# Start Step Function execution within Step Function with CDK

This pattern demonstrates how to replicate S3 bucket objects to multiple S3 buckets. Filters is in use to determine which files needs to replicate to which destination buckets. Implemented with CDK (TypeScript).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-s3-replication-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd s3-s3-replication-cdk
    ```
2. Run below command to install required dependancies:
    ```
    npm install
    ```
4. From the command line, run:
    ```
    cdk deploy --all
    ```

## Testing

1. In the stack output, you can see 3 buckets: `sourceBucket`, `firstDestinationBucket` and `secondDestinationBucket`.

2. In the AWS CLI, upload 2 files to `sourceBucket` with `/images` and `/data` prefixes.
    ```
    aws s3 cp image.jpg s3://[sourceBucket]/images/image.jpg
    aws s3 cp file.json s3://[sourceBucket]/data/file.json
    ```
3. If you go to the AWS S3 console, you can see both files in `sourceBucket`.

4. In the `firstDestinationBucket`, you can see only the `images/` is replicated and in the `secondDestinationBucket` you can see only the `data/` is replicated.

## Cleanup
 
1. Since the versioning is enabled in the buckets, first it is required to delete the versions and delete markers from them.

2. In the folder, update the `remove_objects.sh` shell script adding 3 bucket names with space separated and run it.

3. Then remove the CDK stack as:
    ```bash
    cdk destroy --all
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0