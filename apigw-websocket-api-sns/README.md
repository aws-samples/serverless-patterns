# API WebSocket to SNS with request validation

This pattern creates a WebSocket API to send notification via SNS topic with request validation.

Learn more about this pattern at Serverless Land Patterns: 

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
    cd apigw-websocket-api-sns/
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

This sample project demonstrates how to use WebSocket API to integrate with Amazon Simple Notification service (SNS) to send notifications. This pattern also implements data validation in WebSocket API using model in API Gateway. This template does not implement Authentication in WebSocket API to keep it simple. However, it is recommended to implement Authentication on WebSocket API.
This pattern is utilizing native AWS Integration between WebSocket API Gateway and SNS. Request template is used in WebSocket integration to map the input to SNS payload.
This pattern is also a workaround to invoke AWS services in WebSocket API which requires Content-Type header to be application/x-www-form-urlencoded. By default, WebSocket APIs do not support overriding headers from AWS console and supports application/json in Content-Type header.

## Testing

1. The stack will output the **api endpoint**. Use wscat to test the API (see [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html) for more details on how to set it up):

```bash
wscat -c < API ENdpoint from the stack >
```
2. Send a payload to the API in the correct format of the Model, otherwise you will receive a 'Forbidden' exception. The model in the template expects the request in below format:
```
{"action":"sendOrder","Name":"Jon","SirName":"Doe","Number":"123"}
```
3. A successful invocation to Amazon SNS would return the message ID like below:
```
{"PublishResponse":{"PublishResult":{"MessageId":"10e10111-a2bf-3a33-b44b-5b55dbde5555","SequenceNumber":null},"ResponseMetadata":{"RequestId":"bd11111e-2222-3c33-4444-055c5550c55e"}}}
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
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0