# Cognito Machine-to-Machine (M2M) OAuth 2.0 Authentication Using Custom Scopes with Amazon API Gateway

This pattern demonstrates how to implement machine-to-machine (M2M) authentication using AWS Cognito, OAuth 2.0, API Gateway, and AWS Lambda. It showcases the integration of Cognito as the authentication provider, allowing requests to be authorized based on custom scopes defined in OAuth 2.0

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cognito-m2m-oauth-apigw-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change the working directory to this pattern's directory
    ```
    cd cognito-m2m-oauth-apigw-cdk/src
    ```

1. Install dependencies
    ```
    npm install
    ```

1. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL of API Gateway.
    ```
    cdk deploy
    ```

## How it works

This pattern get OAuth 2.0 access tokens from Cognito User Pool and use them to access API Gateway resources.

## Testing

1. Generate a token by making a request to the oauth2/token endpoint, providing the client ID, client secret, and grant_type='client_credentials'.

```
curl --location 'https://<your cognito custom domain>/oauth2/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic {YOUR_TOKEN}' \
--header 'Cookie: XSRF-TOKEN=80b94546-34ea-4378-9cbb-fe5779e9b132; cognito-fl="W10="' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=integration-OauthResourceServer/read'
```

2. Use the generated token to authorize requests made to an API Gateway endpoint.

3. API Gateway uses the Cognito Authorizer to authenticate and authorize the request.

```
curl --location 'https:/<apigw endpoint>/prod/user' \
--header 'Authorization: <token you get from step 1>'
```
4. If the authorization is successful, the request is forwarded to an AWS Lambda function for further processing.

Then check the logs in Cloudwatch logs

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
