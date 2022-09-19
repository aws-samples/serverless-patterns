# Serverless Data Enrichment Pipeline with Persistence

This pattern helps you deploy a CDK stack with SNS, SQS, Lambda and DynamoDB. The pattern uses these AWS services to create a serverless data enrichment pipeline with short-term persistence of data in SQS. The Lambda functions are used to consume data from SQS queues, perform enrichment, update DynamoDB table. The enriched data is further sent to another SQS queue.

The pattern also features usage of CrossStack to export resources from one CloudFormation stack to another.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.Net 6.0](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)
* [Docker](https://docs.docker.com/get-docker/) installed and running
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd cdk-sns-sqs-lambda-dynamodb-dotnet
    ```
3. Install dependencies
    ```
    dotnet restore/src
    ```

4. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy --all
    ```

## How it works

Data Pipeline Stack #1, relay the raw message from SNS to DynamoDB.

Data Pipeline Stack #2, enrich the raw message from SNS and route it to DynamoDB & SQS. 

One common design pattern is called “fanout.” In this pattern, a message published to an SNS topic is distributed to a number of SQS queues in parallel. By using this pattern, you can build applications that take advantage parallel, asynchronous processing.

## Testing

Have SQS Listner running, Send the following message to the SNS Topic 

``` bash
aws sns publish --topic-arn "<arn>" --message '{\"login\": \"mojombo\",\"type\": \"User\"}'

//enrich - output queue
aws sqs receive-message --queue-url <url> --attribute-names All --message-attribute-names All --max-number-of-messages 10

aws dynamodb get-item --table-name gitusers --key '{\"login\": {\"S\": \"mojombo\"},\"datatype\": {\"S\": \"enriched\"}}'
aws dynamodb get-item --table-name gitusers --key '{\"login\": {\"S\": \"mojombo\"},\"datatype\": {\"S\": \"rawdata\"}}'

```

If using console to send message

```
{"login": "mojombo","type": "User"}
```


## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
