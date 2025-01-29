# AWS Wesocket API to Lambda 

This pattern will create a websocket API protected by a Lambda authorizer. The websocket is integrated with a Lambda function through a mapping template that passes the main informations of the request.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd _patterns-model
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

Websocket APIs are commonly used for 2-ways communications between a client and a server (like a chatbot for instance).
I once came across a scenario where a mapping template was needed, so I thought it could help other people if I published it here. 

The routes $connect and $disconnect have a proxy integration with their Lambdas. 
The integration for the "sendmessage" route is non-proxy with a Lambda function in the back-end. 
The Mapping Template used is this one : 
```
          {
            "requestContext": {
              "routeKey": "$context.routeKey",
              "messageId": "$context.messageId",
              "auth": "$context.authorizer.principalId",
              "token": "$context.authorizer.token",
              "eventType": "$context.eventType",
              "extendedRequestId": "$context.extendedRequestId",
              "requestTime": "$context.requestTime",
              "messageDirection": "$context.messageDirection",
              "stage": "$context.stage",
              "connectedAt": "$context.connectedAt",
              "requestTimeEpoch": "$context.requestTimeEpoch",
              "sourceIp": "$context.identity.sourceIp",
              "requestId": "$context.requestId",
              "domainName": "$context.domainName",
              "connectionId": "$context.connectionId",
              "apiId": "$context.apiId"
            },
              "body": "$util.escapeJavaScript($input.body)",
              "isBase64Encoded": "$context.isBase64Encoded"
          }
```
So it will pass a bunch of important information like the Body and the connectionId. You can add and remove as many variables as you want. 
To make it as independant as I could, the back-end Lambda "SendMessageFunction" does not need any of these information to run successfully, because it is getting the @connection URL from its environment variables and the connectionId from the DynamoDB which name is also in the environment variables.

Only the stage name "stage" is hardcodeded in the environment variable of the Lambda, so if you want to change it you would need to change the environment variable or get it from the Mapping Template in the event sent to Lambda. 

The Websocket API is also protected by a Lambda REQUEST Authorizer. This Lambda function will look for the header "token" and will only allow the request if its value is "hello" - else it will throw a 401 Unauthorized response to the client. 

All Lambda functions are written in Node.js 22 with ".mjs" files and implement the ES module import syntax. 

## Testing

Once the template deployed, you would need to use a websocket client, I would recommend either Postman ior wscat.

1. [Install NPM](https://www.npmjs.com/get-npm).

1. Install wscat:
    ```
    $ npm install -g wscat
    ```

1. Connect to the WebSocket with the following command:
    ```
    $ wscat --header token:hello -c wss://<websocket_url>
    ```
If you don't put the header and its value, you will get `Unauthorized`

You can then send the Json Payload to the `sendmessage` route

    ```
    > {"action": "sendmessage","message" : "hey queen"}
    < good job on deploying this template, keep slaying!!

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
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
