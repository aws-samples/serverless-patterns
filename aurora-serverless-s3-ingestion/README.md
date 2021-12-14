# AWS S3 Aurora Serverless data ingestion from S3

This pattern contains a sample AWS Cloud Development Kit (AWS CDK) template to deploying an Aurora Serverless Cluster Database, a AWS Secrets Manager entry, a S3 bucket and a lambda function. The lambda function is triggered by a S3 put object and the handler ingest the .CSV file to the AWS Aurora Serverless. At this pattern an Aurora Table called movies is created at the first lambda call and the .CSV is designed according to the movies table.

Learn more about this pattern at Serverless Land Patterns: https://github.com/aws-samples/serverless-patterns/aurora-serverless-s3-ingestion

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd aurora-serverless-s3-ingestion/cdk
    ```
1. Create a virtual environment for python:
    ```
    python3 -m venv .venv
    ```
1. Activate the virtual environment: 
   ```
   source .venv/bin/activate
    ```
2. Install python modules:
    ```
    python3 -m pip install -r requirements.txt
    ```
2. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```
    cdk synth
    ```
2. From the command line, use CDK to deploy the stack:
    ```
    cdk deploy
    ```


## How it works

-   The VPC and Subnets are created;
-   A RDS security group is created to allow conections at 3306 port from all VPC CIDR range;
-   The Amazon Aurora Serverless Cluster Database is created;
-   An IAM Policy to be used by the lambda function is created;
-   An IAM Role is created;
-   An S3 Bucket is created and is used as stage to raw data;
-   A lambda function is create using the same VPC as Amazon Aurora Serverless, with 10 minutes timeout and is triggered by S3 creat put on the raw S3 bucket.

## Testing

After deploy retrieve the S3 Bucket Name and transfer the movies.csv to the S3 Bucket.

```
aws s3 cp movies.csv s3://<New-Bucket>
```

Use the Aurora Serverless Query Console to query the new table:

```
select count(*) from movies
```

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
