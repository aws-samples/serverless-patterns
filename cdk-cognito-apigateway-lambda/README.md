# Authenticate API using Cognito User Pool client credentials flow

This project contains a sample AWS CDK template for invoking an API hosted on [Amazon API Gateway](https://aws.amazon.com/api-gateway/) from a client server. The API is authenticated via an Authorizer that uses [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) client credentials flow.

This pattern guides you to authenticate service calls using Cognito User Pool. Often, we come across scenarios where microservices need to communicate with each other in a secure manner using an established standard like OAuth2. The Cognito client_credentials grant type helps you create application client with a set of client credentials that can be used to generate access token. This token can be used to access APIs hosted on API Gateway secured by an authorizer that uses the Cognito User Pool.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deploy

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd cdk-cognito-apigateway-lambda
   ```

3. Install the project dependencies

   ```sh
   npm install
   ```

4. Synthesize an AWS CloudFormation template for the app

    ```sh
   cdk synth
   ```

5. Deploy the stack to your default AWS account and region. The output of this command shows API endpoint.

   ```sh
   cdk deploy
   ```

## Test

You can test the API using a tool like Postman or using a CURL command

1. Generate access token: You can get the domain name by navigating to Cognito console >> Manage User Pools >> Select your user pool >> "Domain name". The client_id and client_secret can be accessed from "App clients" section. The domain needs to be available at the the time of your deployment, so please update the the "domainPrefix" attribute in "cdk-cognito-apigateway-lambda-stack.ts" if the deployment fails due to domain name being unavailable. If a domain is deleted, it will not be available immediately for use. It would be better to use a new domain name instead.

   ```sh
   curl -X POST https://apg-user-pool-client.auth.us-east-2.amazoncognito.com/oauth2/token \
    -H 'content-type: application/x-www-form-urlencoded' \
    -d 'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope=users/read'
   ```

2. Invoke the API using access token returned from above POST response

    ```sh
    curl -X POST https://ojrod6the1.execute-api.us-east-2.amazonaws.com/prod/ -H 'Authorization:{access_token}'
    ```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```sh
cdk destroy
```

## References

1. [Generate access token](https://docs.aws.amazon.com/cognito/latest/developerguide/token-endpoint.html)
2. [Understand AWS Cognito grants](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html)

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0