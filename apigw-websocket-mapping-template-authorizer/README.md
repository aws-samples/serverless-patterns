# AWS API Gateway Websocket API to AWS Lambda with authorization and mapping template

This pattern will create an AWS API Gateway Websocket API protected by a Lambda authorizer. The websocket is integrated with a Lambda function through a mapping template that passes the main informations of the request.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-websocket-mapping-template-authorizer

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Install NPM](https://www.npmjs.com/get-npm).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-websocket-mapping-template-authorizer
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

The architecture uses proxy integration for the `$connect` and `$disconnect` routes, each linked to their respective AWS Lambda functions. The `sendmessage` route uses non-proxy integration with a backend Lambda function, incorporating a mapping template to pass essential data such as the message body and connection ID.


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
The backend Lambda function `SendMessageFunction` operates independently by retrieving the endpoint and DynamoDB table name from environment variables. The API stage name is defined in the Lambda environment variables. To modify the stage name, you can either update the environment variable or extract it from the mapping template in the event sent to Lambda.

This implementation includes security through a Lambda REQUEST Authorizer. The authorizer function validates the header `token`, granting access only when the token value is "hello". Requests with invalid tokens receive a 401 Unauthorized response.

All Lambda functions use Node.js 22 with ".mjs" files and implement ES module import syntax. To send responses to clients, the Lambda function constructs the endpoint URL using environment variables:
`"https://" + process.env.API_ID + ".execute-api." + process.env.AWS_REGION + ".amazonaws.com/" + process.env.STAGE + "/"` and the command `PostToConnectionCommand` from the client [`ApiGatewayManagementApiClient`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/apigatewaymanagementapi/).

## Testing

Once the template deployed, you would need to use a websocket client, I would recommend either Postman ior wscat.

1. Install wscat:
    ```
    $ npm install -g wscat
    ```

1. Connect to the WebSocket with the following command:
    ```
    $ wscat --header token:hello -c wss://<websocket_url>
    ```
If you don't put the header and its value, you will get `Unauthorized`

You can then send the Json Payload to the `sendmessage` route:
```
> {"action": "sendmessage","message" : "hey queen"}
< good job on deploying this template, keep slaying!!
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
