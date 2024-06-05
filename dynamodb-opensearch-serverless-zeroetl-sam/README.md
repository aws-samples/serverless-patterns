# DynamoDB to OpenSearch Serverless with Zero-ETL

This sample project demonstrates how to deploy a zero-ETL integration from a DynamoDB table to an OpenSearch Serverless collection.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-opensearch-serverless-zeroetl-sam

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
    cd dynamodb-opensearch-serverless-zeroetl-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the DeploymentName parameter
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the URLs which are used for testing.

## How it works

DynamoDB table item-level modifications (inserts, updates, and deletes) are captured with a DynamoDB Stream. Using the DynamoDB Stream as its source, an OpenSearch Ingestion pipeline sinks the data to an OpenSearch Serverless collection.

## Testing

1. Edit the data access policy (`DataAccessPolicyEditURL` from the stack outputs). In the **Select principals** section, add an [IAM role with permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html) to access the OpenSearch dashboard. Make sure you save the **Edit access policy** section, too! Wait 1 minute for the policy update to take effect.

1. Insert an item into the DynamoDB table (`InsertItemURL` from the stack outputs). Choose a random value for the uuid. You can insert additional attributes with random values if desired.

1. From the OpenSearch dashboard Dev Tools console (`DevToolsURL` from the stack outputs), search the index. You should see the item you created in DynamoDB.
    ```
    GET dynamo-index/_search
    ```

## Cleanup
 
1. From the [S3 console](https://console.aws.amazon.com/s3/home), empty the bucket created by this project (`BucketName` from the stack outputs).

1. Delete the stack
    ```
    sam delete
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
