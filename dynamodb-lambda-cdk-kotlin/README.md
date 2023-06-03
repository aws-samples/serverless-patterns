# DynamoDB to Lambda

The CDK stack deploys a Lambda function, a DynamoDB table, and the minimum IAM resources required to run the application.

When items are written or updated in the DynamoDB table, the changes are sent to a stream. This pattern configures a Lambda function to poll this stream. The function is invoked with a payload containing the contents of the table item that changed.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd dynamodb-lambda-cdk-kotlin/
    ```
1. From the command line, build a shadow jar containing the lambda deployment package
     ```
    cd serverless
    gradle shadow
     ```

1. Change directory to the stack directory and use cdk to deploy the AWS resources for the pattern:
    ```
    cd ../stack
    cdk deploy
    ```

## Testing

After deployment, add an item to the DynamoDB table and confirm the resulting Lambda invocation in CloudWatch Logs.

## Cleanup

1. Delete the stack
    ```bash
      cdk destroy
    ```
   
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
