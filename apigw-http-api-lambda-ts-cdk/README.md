# Amazon API Gateway HTTP API with AWS Lambda integration

This pattern in CDK offers a boilerlate to generate an Amazon API Gateway HTTP API endpoint with "ANY" method from the specified path. The Lambda function provided in TypeScript only returns a dummy "HelloWorld".

Amazon API Gateway has two ReSTful API products: REST APIs and HTTP APIs. REST APIs (v1) support more [features](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html) than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower price. For instance, [calculator.aws](https://calculator.aws/#/createCalculator/APIGateway) shows that 10 millions of requests cost 10 USD/month (Region: US East) whereas REST APIs costs 35 USD/month.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-http-api-lambda-ts-cdk](https://serverlessland.com/patterns/apigw-http-api-lambda-ts-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [Docker](https://www.docker.com/get-started/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
      git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory its source code folder:
    ```bash
      cd apigw-http-api-lambda-ts-cdk
    ```
3. From the command line, use npm to install the development dependencies:
    ```bash
      npm install
    ```
4. To deploy from the command line use the following:
    ```bash
      npm run deploy
    ```
5. _Optional_ If you do not use the default profile in your configuration for aws credentials, you must edit your scripts section in the `package.json`, replacing `<YOUR_PROFILE_NAME>` with your named profile:
    ```json
      {
        "scripts": {
          "deploy": "cdk deploy --profile <YOUR_PROFILE_NAME>",
          "destroy": "cdk destroy --profile <YOUR_PROFILE_NAME>"
        }
      }
    ```

## How it works

The solution works as follow:
1. CDK will provision an Amazon API Gateway HTTP API and a sample Lambda function.
2. It will integrate the Lambda function to the  HTTP API using the route "/"
3. Finally, it will return the HTTP API URL in the console. (So you can test the deployment)

## Testing

1. After deployment, the output shows the API Gateway URL with the Lambda integration, for example: ```HttpApiLambdaStack.HttpApiURL = https://<random id>.execute-api.<region>.amazonaws.com/```.
2. Accessing the URL in a browser, you see: ```Hello World```.

## Cleanup
 
1. From the command line, use the following in the source folder
    ```bash
    npm run destroy
    ```
2. Confirm the removal and wait for the resource deletion to complete.

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0