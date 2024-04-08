# Amazon SQS to Amazon API Gateway using Amazon Eventbridge Pipes with enrichment

This pattern demonstrates how to use an EventBridge pipe to push and modify events before sending it to DynamoDB. This pattern is leveraging EventBridge pipe to first integrate 3 services together, simplifying the process by reducing the need for integration code. Here, SQS is the EventBridge source, Lambda to enrich the data, before pushing to the target API Destination that invokes an API Gateway.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [AWS Python SDK Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-pipes-sqs-lambda-api-destination
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

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

EventBridge Pipes helps to integrate various services together, thereby simplifying the process and reducing the need for integration code. Here, we are able to push data from SQS to API Destination via Lambda (enrichment) without any integration code. To take it a step further, the target of the EventBridge Pipe, API Destination, is configured to invoke an API Gateway endpoint which in turn inserts the data into DynamoDB via a Lambda Proxy. The addition of DynamoDB and Lambda proxy is excluded from the EventBridge Pipe, and serves to give you a better visualisation of the outputs of this serverless pattern.

## Testing

Run the test file (testing.py) located in the testing folder (/testing). 
```
cd testing
python3 testing.py
```
We have declared three test items within the test file that will be pushed into the SQS queue to begin the workflow. To ensure that the deployment is running correctly, you should be able to see three test items created in the DynamodB table, with an additional attribute of 'Type: Food' that was inserted via the enrichment lambda.

Take note, ensure that the region and SQS queue url is modified in the testing file (testing.py) accordingly.

## Cleanup
 
Delete the stack
```
sam delete
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
