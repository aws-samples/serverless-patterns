# Amazon QLDB to Amazon Kinesis Data Streams to AWS Lambda to Amazon DynamoDB

This pattern shows how to deploy a SAM template that uses QLDB Streams to stream data from an Amazon QLDB ledger to Amazon Kinesis Data Streams. These records are consumed by an AWS Lambda function which writes the data to an Amazon DynamoDB Table. This shows how to stream data out of QLDB to a downstream database engine using a Change Data Capture design pattern. The DynamoDB table could store data in a different format or just a subset of data, to cater for different use cases.

Note: This pattern builds upon the [API Gateway to Lambda to QLDB serverless pattern](https://serverlessland.com/patterns/apigw-lambda-qldb). That pattern creates the QLDB ledger and provides commands to populate data. It also outputs the ledger name which is then imported by this pattern.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

NOTE: The `sam template` as part of the [API Gateway to Lambda to QLDB serverless pattern](https://serverlessland.com/patterns/apigw-lambda-qldb) must be deployed first, as it creates the ledger required by this pattern.

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd qldb-kinesis-lambda-dynamodb
    ```
1. From the command line, use AWS SAM to build the serverless application with its dependencies
    ```
    sam build
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

## How it works

The `sam template` creates the following:

* A Kinesis Data Stream
* An IAM role the QLDB service can assume to write to Kinesis
* A QLDB Stream that connects the ledger previously created to the Kinesis Data Stream
* A DynamoDB table
* A Lambda function that consumes records from Kinesis and writes to the DynamoDB table

It is built upon the `sam template` deployed for the [API Gateway to Lambda to QLDB serverless pattern](https://serverlessland.com/patterns/apigw-lambda-qldb).

As changes are made to the journal in QLDB, they are continuously written out in near real time to the destination Kinesis Data Stream. An AWS Lambda function is configured to consume records from this stream. The Lambda function is developed to only process messages of the type `REVISION_DETAILS` which are changes made to a record in a table in QLDB which could be an insert, update or even deletion.

QLDB streams guarantees at-least-once delivery, which means it can publish duplicate and out-of-order records to Kinesis Data Streams. Each record includes an incrementing version number with the creation of the record being version `0`.

The create or update statement to DynamoDB use a `ConditionExpression` to check that the record either doesn't already exist, or the version number currently held as an attribute on the item in DynamoDB is less that the version number being passed in. This ensures that an out of sequence record will not overwrite a more recent update for a record. When a delete statement is identified, an `isDeleted` attribute is added to the item as a tombstone marker, to ensure that an out of sequence record does not create a new record.

## Testing

All test data is created following the test instructions set out in the GitHub repo for the [API Gateway to Lambda to QLDB serverless pattern](https://serverlessland.com/patterns/apigw-lambda-qldb).

Open up the `AWS Console` and navigate to `DynamoDB` and `Explore Items`.

![DynamoDB Console](/img/DynamoDB-Console.png)

Within a few seconds of creating, updating or deleting a record in QLDB, you will see the changes having been streamed out through Kinesis and updated in the DynamoDB table

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