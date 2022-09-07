# AWS Step Function to Amazon Polly to S3 with CDK (Typescript)

This pattern demonstrates how to build a AWS Step Function State machine to generate mp3 files given a list of words using Amazon Polly. Generated mp3 files will be saved in a S3 bucket.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/stepfunction-polly-s3-cdk

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
    cd stepfunction-polly-s3-cdk
    ```
2. Run below command to install required dependancies:
    ```
    npm install
    ```

3. From the command line, run:
    ```
    cdk deploy --all
    ```

## Testing

1. In your State Machine, start a new execution with a similar payload below with some common english words.
```
[
  {
    "word": "Serverless"
  },
  {
    "word": "Learning"
  },
  {
    "word": "Knowledge"
  }
]
```
2. In the S3 bucket, there will be mp3 files generated for each word provided.

## Cleanup
 
1. To delete the stack, run:
    ```bash
    cdk destroy --all
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
