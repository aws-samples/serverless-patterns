# API Gateway WebSocket API to AWS Lambda

This pattern creates an Amazon API Gateway WebSocket API and an AWS Lambda function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-websocket-api-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [NPM](https://www.npmjs.com/get-npm) for testing

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:
    ``` bash
    cd apigw-websocket-api-lambda
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ``` bash
    sam deploy --guided
    ```

1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys an Amazon API Gateway WebSocket API with a $connect route, a $disconnect route and a custom route. The $connect route invokes an AWS Lambda function to record the WebSocket's connection ID to a DynamoDB table. The custom route is integrated with an AWS Lambda function written in Node.js which returns back the contents of the "data" node of a JSON object within the request's body. The $disconnect route invokes an AWS function to remove the connection ID from the DynamoDB table when the WebSocket connection is closed.

## Testing

Once the application is deployed, retrieve the WebSocketURL value from CloudFormation Outputs. To test the WebSocket API, you can use [wscat](https://github.com/websockets/wscat) which is an open-source command line tool.

1. [Install NPM](https://www.npmjs.com/get-npm).

1. Install wscat:
    ```
    $ npm install -g wscat
    ```

1. Connect to your WebSocketURL by executing the following command:
    ```
    $ wscat -c <YOUR WEBSOCKET URL>
    ```

1. To test the custom route and its associated function, send a JSON-formatted request like the following example. The Lambda function sends back the value of the "data" key using the callback URL:
```
$ wscat -c <YOUR WEBSOCKET URL>
connected (press CTRL+C to quit)
> {"action":"post", "data":"hello world"}
< hello world
```

## Documentation
- [Working with WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)
- [AWS Lambda - the Basics](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/aws-lambdathe-basics.html)
- [Lambda Function Handler](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-handler.html)
- [Function Event Object - Overview](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-event-object.html)
- [Function Environment Variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)

## Cleanup

1. Delete the stack
    ```
    aws cloudformation delete-stack --stack-name <YOUR STACK NAME>
    ```

1. Confirm the stack has been deleted
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'<YOUR STACK NAME>')].StackStatus"
    ```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0