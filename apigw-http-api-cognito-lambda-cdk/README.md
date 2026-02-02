# Amazon API Gateway HTTP API with Cognito JWT and AWS Lambda integration

This pattern creates an Amazon Gateway API (v2) and two Lambda functions protected by JwtAuthorizer and Cognito for user management.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-http-api-cognito-lambda-cdk](https://serverlessland.com/patterns/apigw-http-api-cognito-lambda-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:
    ```bash
    cd apigw-http-api-cognito-lambda-cdk
    ```

1. Install dependencies
    ```bash
    npm install
    ```

1. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL.
    ```bash
    cdk deploy
    ```

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates an Amazon API Gateway API HTTP API and two endpoints. The first endpoint is unprotected (no authentication/authorization) and integrate with a unprotected accessible Lambda function. The second endpoint is protected by a JWTAuthorizer that use Coginto as IDP and it integrates with a protected accessible Lambda function.

## Testing

**Pre-requisites**
1. Update the variables with the outputs of your stack.
   ```bash
     API_URL="<your api URL>"    
     POOL_ID="<your pool ID>" 
     CLIENT_ID="<your client ID>" 
   ```
2. Set the variables for the fake user to be created
   ```bash
     EMAIL="fake@example.com"                                
     PASSWORD="S3cuRe#FaKE*"
   ```

**Unprotected endpoint**
To test the unprotected endpoint, send a HTTP GET request command to the HTTP API unprotected endpoint. Be sure to update the endpoint with outputs of your stack. The response payload should shows `Hello Unprotected Space`.
```bash
curl ${API_URL}/unprotected
```

**Protected endpoint**
To test the protected endpoint:
1. First sign-up the fake user against Cognito. 
   ```bash
    aws cognito-idp sign-up \
    --client-id ${CLIENT_ID} \
    --username ${EMAIL} \
    --password ${PASSWORD}
   ```
2. Confirm the fake user to Cognito
   ```bash
    aws cognito-idp admin-confirm-sign-up \
    --user-pool-id ${POOL_ID} \
    --username ${EMAIL}
   ```
4. Then you send the authentication data and Cognito will return the token. 
   ```bash
   TOKEN=$(aws cognito-idp initiate-auth \
    --client-id ${CLIENT_ID} \
    --auth-flow USER_PASSWORD_AUTH \
    --auth-parameters USERNAME=${EMAIL},PASSWORD=${PASSWORD} \
    --query 'AuthenticationResult.AccessToken' \
    --output text)
   ```
5. Send an HTTP GET request to the API Gateway with the JWT token, which will verify the token call the protected Lambda function.
    ```bash
    curl -H "Authorization: ${TOKEN}" ${API_URL}/protected
    ```
6. The result payload should display `Hello Protected Space!`
 

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```bash
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
