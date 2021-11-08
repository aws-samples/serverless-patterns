# Amazon API Gateway HTTP API to AWS Lambda

This pattern creates an Amazon API Gateway HTTP API and an AWS Lambda function.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-lambda).

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
    cd apigw-http-api-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys an Amazon API Gateway HTTP API with a default route and basic CORS configuration. The default route is integrated with an AWS Lambda function written in Node.js. The function logs the incoming API event (v2) and context object to an Amazon CloudWatch Logs log group and returns basic information about the event to the caller.

## Testing

Once the application is deployed, retrieve the HttpApiEndpoint value from CloudFormation Outputs. Either browse to the endpoint in a web browser or call the endpoint from Postman.

Example GET Request: https://{HttpApiId}.execute-api.us-east-2.amazonaws.com/

Response:
```
{
  "functionName": "http-api-lambda-proxy-function",
  "xForwardedFor": "{YourIpAddress}",
  "method": "GET",
  "rawPath": "/"
}
```

Example POST Request: https://{HttpApiId}.execute-api.us-east-2.amazonaws.com/path1/path2?foo=bar
- Request Header: "Content-Type: application/json"
- Request Body: {"key1":"value1", "key2":"value2"}

Response: 
```
{
  "functionName": "http-api-lambda-proxy-function",
  "xForwardedFor": "{YourIpAddress}",
  "contentType": "application/json",
  "method": "POST",
  "rawPath": "/path1/path2",
  "queryString": {
    "foo": "bar"
  },
  "body": "{\"key1\":\"value1\", \"key2\":\"value2\"}"
}
```

## Documentation
- [Working with HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)
- [Working with AWS Lambda proxy integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
- [AWS Lambda - the Basics](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/aws-lambdathe-basics.html)
- [Lambda Function Handler](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-handler.html)
- [Function Event Object - Overview](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-event-object.html)
- [Function Event Object - HTTP API v2 Event](https://github.com/awsdocs/aws-lambda-developer-guide/blob/master/sample-apps/nodejs-apig/event-v2.json)
- [Function Context Object - Overview](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-context-object.html)
- [Function Context Object in Node.js - Properties](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-context.html)
- [Function Environment Variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

This pattern was contributed by Greg Davis.

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0