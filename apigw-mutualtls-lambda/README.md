# Amazon API Gateway HTTP API to AWS Lambda authenticated by certificate based mutual TLS

This pattern creates an Amazon API Gateway HTTP API authenticated by mutual TLS and an AWS Lambda function.

Learn more about this pattern at: https://serverlessland.com/patterns/apigw-lambda-tls.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [AWS Certificate Manager](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains-prerequisites.html) Before setting up a custom domain name for an API, you must have an SSL/TLS certificate ready in AWS Certificate Manager.
* [Configure truststore](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-mutual-tls.html) Create a truststore of X.509 certificates that you trust to access your API and upload the truststore to an Amazon S3 bucket in a single file.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-mutualtls-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the HTTP AppName(API)
    * Enter the Custom Domain name
    * Enter the ACM Certificate ARN
    * Enter the S3 truststore uri
    * Enter the public hosted zone id
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs that were created.

## How it works

This pattern deploys an Amazon API Gateway HTTP API with a default route and basic CORS configuration. The default route is integrated with an AWS Lambda function written in Node.js and API is authenticated by certificate based mutual TLS. The function logs the incoming API event and context object to an Amazon CloudWatch Logs log group and returns basic information about the event to the caller.

## Testing

Once the application is deployed, use the custom domain name value for testing. As a best practice the default endpoint for HTTP Api will be disabled when mutual TLS is enabled. Either use a curl or call the endpoint from Postman using your client side public and private keys.

Example GET Request: curl --key my_client.key --cert my_client.pem https://{your-custom-domain-name}

Response:
```
{
  "functionName": "apigw-mutualtls-lambda-function",
  "xForwardedFor": "{YourIpAddress}",
  "method": "GET",
  "rawPath": "/"
}
```

Example POST Request: curl --key my_client.key --cert my_client.pem https://{your-custom-domain-name}
- Request Header: "Content-Type: application/json"
- Request Body: {"key1":"value1", "key2":"value2"}

Response:
```
{
  "functionName": "apigw-mutualtls-lambda-function",
  "xForwardedFor": "{YourIpAddress}",
  "contentType": "application/json",
  "method": "POST",
  "rawPath": "/",
  "body": "{\"key1\":\"value1\", \"key2\":\"value2\"}"
}
```

## Documentation
- [Working with HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)
- [Working with AWS Lambda proxy integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
- [Working with AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)
- [Setting up custom domain names for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-custom-domain-names.html)
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
Note: Cloudformation stack deletion doesn't delete the ACM certificate and truststore file from S3 bucket.

This pattern was contributed by Sudheer Yalamanchili.

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
