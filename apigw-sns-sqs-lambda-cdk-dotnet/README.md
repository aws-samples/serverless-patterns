# Amazon API Gateway REST API that integrates with Amazon SNS and Amazon SQS to implement Topic-Queue-Chaining using .NET CDK

This CDK application demonstrates how to set up a topic-queue-chaining pattern using Amazon SNS and Amazon SQS behind an Amazon API Gateway. This architecture helps in setting up a highly scalable API that can consume messages/events, fan them out and process them asynchronously.

Important: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change the working directory to this pattern's directory
    ```
    cd apigw-sns-sqs-lambda-cdk-dotnet
    ```

1. Build the .NET CDK project
    ```
    dotnet build src
    ```

1. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL.
    ```
    cdk deploy
    ```

## How it works

This pattern creates an Amazon API gateway HTTP API endpoint. The endpoint uses service integrations to directly connect to Amazon SNS, SNS fans out the message to Amazon SQS and an Lambda subscribes to the queue.

## Testing

1. Get Rest API Endpoint from stack output
```
    RESTAPI_ENDPOINT=$(aws cloudformation describe-stacks \
        --stack-name CdkApigwSnsSqsLambdaStack \
        --query "Stacks[0].Outputs[0].OutputValue" \
        --output text)
```

2. Send a sample request to the API endpoint
```
    curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"name": "Test message", "category": "Testing", "id": 1}' \
        $RESTAPI_ENDPOINT
```

3. Check the lambda logs from cloudwatch log groups connected to the 2 SQS queues. If the setup is successful you should see the message logged by worker type one lambda and worker type lambda. 
## Cleanup
 
Run the following command to delete all the resources from your AWS account.
```
cdk destroy
```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.