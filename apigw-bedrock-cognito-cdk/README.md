# Access Bedrock via API Gateway with Cognito User Management

This pattern creates an AWS CDK Python application to access Bedrock via API Gateway with Cognito user management, domain restriction, API request throttling, and quota limits.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [Install and Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
* [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Install Node and NPM](https://nodejs.org/en/download/)
* [Install AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/cli.html)
* [Install Python 3](https://www.python.org/downloads/)
* [Install Docker](https://www.docker.com/products/docker-desktop/)
* [Grant Bedrock Model Access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-bedrock-cognito-cdk
    ```
3. Create a virtual environment for Python:
    ```
    python3 -m venv .venv
    ```
4. Activate the virtual environment:
    ```
    source .venv/bin/activate
    ```
    For a Windows platform, activate the virtualenv like this:
    ```
    .venv\Scripts\activate.bat
    ```
5. Install the required Python dependencies:
    ```
    pip install -r requirements.txt
    ```
6. Bootstrap the AWS environment, if you haven't already done so:
    ```
    cdk bootstrap
    ```
7. Review the CloudFormation template AWS CDK generates for the stack:
    ```
    cdk synth
    ```
8. Deploy the AWS resources:
    ```
    cdk deploy
    ```
    Optionally you can add the optional variables using the `--context`, see [API Gateway Configuration](#API-Gateway-Configuration) and [Cognito Integration and Configuration](#Cognito-Integration-and-Configuration).
    ```
    cdk deploy --context API_THROTTLE_RATE_LIMIT=1 --context API_THROTTLE_BURST_LIMIT=2 --context API_QUOTA_LIMIT=25 --context API_QUOTA_PERIOD=DAY --context ORGANIZATION_DOMAIN=@example.com
    ```    
9. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

### Overview

This pattern deploys an Amazon API Gateway REST API with the following routes: `POST /register`, `POST /login`, `GET` and `POST /bedrock`. It includes a Amazon Cognito User Pool and Lambdas to handle requests from the API Gateway. The API Gateway allows CORS for all origins and methods, incorporates an Usage Plan, and has throttle and quota limits for the `/bedrock` endpoint. The `/bedrock` endpoint allows access to Amazon Bedrock Foundation models.

### Components and Configuration

#### API Gateway Routes
- `/register` endpoint: Accepts `email`, `password`, and `fullname` in the body, interacts with a proxy lambda integration to register users to the Cognito User Pool. Returns an API Key which will be associated with the API Gateway's usage plan and stored within the Cognito user's custom `api_key` field . If an organization domain is specified in the `ORGANIZATION_DOMAIN` context variable, a pre signup lambda is provisioned to reject users not belonging to the specified domain.

- `/login` endpoint: Accepts `email` and `password` in the body, interacts with a proxy lambda integration to authenticate the user. Returns an bearer token, containing `IdToken`, `AccessToken`, `RefreshToken` and other metadata. If the user loses their API key, they can decrypt the `IdToken` using [jwt.io](https://jwt.io/) or other libraries to retrieve the API key from the `custom:api_key` field.

- `/bedrock` endpoint: Protected with a Cognito authorizer to ensure only requests with valid `Authorization` and `x-api-key` tokens in headers can access the endpoint, interacts with a proxy lambda integration. A `GET` request lists all foundation models, and a `POST` request takes `modelId` and `inferenceParameters` in the body, to invoke and return response from the foundation model.

#### API Gateway Configuration
- CORS: Enabled for all origins and methods.
- Usage Plan: Configured to manage API access.
- Throttle Limits: Rate limit of 1 request per second with a burst limit of 2 requests.
- Quota Limits: Set to 25 requests per day for the `/bedrock` endpoint.
- These limits can be modified during deployment using context variables (`API_THROTTLE_RATE_LIMIT`, `API_THROTTLE_BURST_LIMIT`, `API_QUOTA_LIMIT`, `API_QUOTA_PERIOD`)
- Logging: Enabled for all Error and Info request logs.

#### Cognito Integration and Configuration
- User Pool: Manages user registration and login.
- Organization Domain Restriction: The organization domain restriction can be adjusted during deployment using the context variable `ORGANIZATION_DOMAIN`. A Pre SignUp Lambda trigger will be added to enforce specific domain restrictions.

#### Lambda Integration
- `bedrock.py`:
    - Uses the `boto3` library to make API calls to Amazon Bedrock APIs.
    - Utilizes the `jsonpath_ng` library to dynamically map and retrieve responses from foundation models provided by Anthropic, AI21 Labs, Amazon, and Meta.
- `auth.py`:
    - Uses the `boto3` library to make API calls to Amazon Cognito and Amazon API Gateway.
    - Manages user creation, login, and the creation and association of API keys.
- `pre_signup.py` (if valid):
    - Validates user email domain during registration.
- All Lambda Configuration:
    - Timeout: Set to 29 second due to maximum integration timeout limit - [Amazon API Gateway Limits](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html).
    - Logging: All events are logged to Amazon CloudWatch, with a custom redaction function to remove passwords from the `auth.py` Lambda prior to logging.

### Request and Response Examples

- **Register User**
  - **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "securePassword123",
      "fullname": "John Doe"
    }
    ```
  - **Response Body:**
    ```json
    {
      "status": 200,
      "message": "User user@example.com created successfully.",
      "data": {"API Key": "generatedApiKey"},
      "success": true,
    }
    ```

- **Login User**
  - **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "securePassword123"
    }
    ```
  - **Response Body:**
    ```json
    {
    "status": 200,
      "IdToken": "generatedIdToken",
      "AccessToken": "generatedAccessToken",
      "RefreshToken": "generatedRefreshToken",
      "ExpiresIn": 3600,
      "TokenType": "Bearer",
      "sucess": true
    }
    ```

- **Make Bedrock Request**
  - **Request Headers:**
    - Authorization: Bearer [IdToken]
    - x-api-key: [APIKey]
  - **GET /bedrock Response Body:**
    ```json
    {
      "status": 200,
      "foundationModels": [...],
      "message": "Successfully retrieved foundation models list."
    }
    ```
  - **POST /bedrock Request Body:**
    ```json
    {
      "modelId": "exampleModelId",
      "inferenceParameters": {...}
    }
    ```
  - **POST /bedrock Response Body:**
    ```json
    {
      "status": 200,
      "message": "Successfully retrieved response from foundation model.",
      "data": "..."
    }
    ```

## Testing

Prior to running the tests, ensure that your account has the necessary access to the following Bedrock models: `ai21.j2-mid-v1`, `anthropic.claude-instant-v1`, `amazon.titan-text-express-v1`, and `meta.llama2-13b-chat-v1`. Follow the guide provided in the [Requirements](#Requirements) - [Bedrock model access granted](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) to grant access to these models. Without access, the tests will fail due to insufficient permissions to interact with the foundation models.

1. Activate the virtual environment, if you haven't already done so from the deployment instructions:
    ```
    source .venv/bin/activate
    ```
    For a Windows platform, activate the virtualenv like this:
    ```
    .venv\Scripts\activate.bat
    ```
2. Install the Python required dependencies:
    ```
    pip install -r requirements-dev.txt
    ```
3. From the CDK output during the deployment process, obtain the values for Cognito User Pool ID and Rest API Endpoint:
    ``` 
    ApigwBedrockCognitoCdkStack.CognitoUserPoolID = us-east-1_XXXXXXXXX
    ApigwBedrockCognitoCdkStack.RestAPIEndpoint = https://XXXXXXXXX.execute-api.us-east-1.amazonaws.com/prod/
    ```
4. Update the `API_ENDPOINT` and `USER_POOL_ID` variables in `tests/e2e/test_apigw_bedrock_cognito_cdk_stack.py` with the obtained values:
    ```
    API_ENDPOINT = "https://XXXXXXXXX.execute-api.us-east-1.amazonaws.com/prod/"
    USER_POOL_ID = "us-east-1_XXXXXXXXX"
    ```
    If organization domain restriction is enabled, modify the `TEST_EMAIL` to be an email with your domain, and `NON_ORG_TEST_EMAIL` to an email without your domain:
    ```
    TEST_EMAIL = "johndoe@org.com"
    NON_ORG_TEST_EMAIL = "johndoe@example.com"
    ```
5. Execute Pytest:
    ```
    pytest -v
    ```

## Cleanup
 
1. Delete the stack:
    ```
    cdk destroy
    ```
2. Delete all API Keys:
    Before executing the following command, be aware that it will delete all API keys in the account. Ensure you have the necessary backups or are certain of the consequences.
    ```
    sh utils/delete_all_api_keys.sh
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0