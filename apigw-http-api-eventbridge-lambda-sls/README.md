# Amazon API Gateway HTTP API to Amazon EventBridge

This pattern creates an HTTP API endpoint that directly integrates with Amazon EventBridge

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigateway-http-eventbridge-lambda-sls](https://serverlessland.com/patterns/apigateway-http-eventbridge-lambda-sls).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ``` sh
    cd serverless-patterns/apigw-http-api-eventbridge-lambda-sls
    ```

1. From the command line, use npm to install the development dependencies:

    ``` sh
    npm install
    ```

1. From the command line, use Serverless Framework to deploy the AWS resources for the pattern as specified in the serverless.yml file:

    ``` sh
    serverless deploy --verbose
    ```

    The above command will deploy resources to `us-east-1` region by default. You can override the target region with `--region <region>` CLI option, e.g.

    ``` sh
    serverless deploy --verbose --region us-west-2
    ```

1. Note the `ApiEndpoint` output from the Serverless Framework deployment process. You will use this value for testing.

## How it works

This pattern creates an Amazon API gateway HTTP API endpoint. The endpoint uses service integrations to directly connect to Amazon EventBridge.

Once a new event is published to EventBridge `WebApp` custom event bus it is delivered to a Lambda function, which will simply log that event to EventLog.
Lambda function is written in TypeScript and deployed to ARM64 architecture for demo purposes.

## Testing

### Sending a new test message to API Gateway endpoint

To test the endpoint first send data using the following command. Be sure to update the endpoint with endpoint of your stack.

``` sh
curl --location --request POST 'ApiEndpoint output value' --header 'Content-Type: application/json' \
--data-raw '{
    "Detail":{
        "message": "This is my test"
    }
}'
```

### Expected result

```json
{"Entries":[{"EventId":"Event_UUID"}],"FailedEntryCount":0}
```

### CloudWatch logs

Open AWS CloudWatch Console and navigate to [/aws/lambda/apigw-http-api-eventbridge-lambda-sls-prod-logEvent](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fapigw-http-api-eventbridge-lambda-sls-prod-logEvent) log group.
You should be able to see a new Event Stream with the Received Event information, and Event Message, logged into the stream.

## Cleanup

1. Delete the stack

    ```sh
    serverless remove --verbose
    ```

1. Confirm the stack has been deleted

    ```sh
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'apigw-http-api-eventbridge-lambda-sls-prod')].StackStatus"
    ```

    Expected output

    ```json
    [
        "DELETE_COMPLETE"
    ]
    ```

    NOTE: You might need to add `--region <region>` option to AWS CLI command if you AWS CLI default region does not match the one, that you used for the Serverless Framework deployment.

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
