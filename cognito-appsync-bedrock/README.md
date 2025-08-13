# AWS AppSync and Amazon Cognito to Amazon Bedrock via AWS Lambda 

This pattern demonstrates how to invoke Amazon Bedrock models from AWS AppSync using a AWS Lambda resolver, with user authentication handled by Amazon Cognito.

> **Note**: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Prerequisites

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node and NPM](https://nodejs.org/en/download/) installed (Node.js 20.x recommended as used by the Lambda function)
- [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) installed
- Make sure to enable the **Anthropic Claude 3 Sonnet** model (e.g., `anthropic.claude-3-sonnet-20240229-v1:0`) in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/modelaccess) for the AWS region you intend to deploy this stack

## Architecture

This pattern sets up an AWS AppSync GraphQL API configured with Amazon Cognito User Pools for authentication. Authenticated users can send a prompt through a GraphQL mutation (`invoke`).

### Flow

1. **Authentication**: Users are authenticated against an Amazon Cognito User Pool
2. **AppSync Mutation**: The client sends a GraphQL mutation including the prompt and a valid Cognito ID token
3. **Lambda Resolver**: AppSync uses a Lambda resolver to process the `invoke` mutation
4. **Bedrock Invocation**: The AWS Lambda function (`src/lambda/invokeBedrock/index.ts`) receives the prompt from AppSync. It then constructs a request and invokes the specified Amazon Bedrock model (defaulting to Anthropic Claude 3 Sonnet). The Lambda function has the necessary IAM permissions to call the Bedrock `InvokeModel` API
5. **Response**: The Bedrock model processes the prompt and returns a response. The Lambda function forwards this response back to AppSync, which then relays it to the client

### Resources

The AWS CDK script (`lib/cdk-stack.ts`) provisions the following resources:

- An Amazon Cognito User Pool and User Pool Client
- An AWS AppSync GraphQL API (`schema.gql`) with Cognito User Pool as the default authorization mode
- An AWS Lambda function with permissions to invoke the specified Bedrock model
- An AppSync Lambda Data Source and a Resolver connecting the `invoke` mutation to the Lambda function
- CloudFormation outputs for easy access to API endpoints and Cognito identifiers

The Bedrock model ID, Anthropic API version, and other inference parameters (like `max_tokens`, `temperature`) can be configured via environment variables in the Lambda function, as defined in `lib/cdk-stack.ts` and used in `src/lambda/invokeBedrock/index.ts`.

## Deployment

1. Clone the repository:

   ```bash
     git clone https://github.com/aws-samples/serverless-patterns
   ```

2. Navigate to the project directory:

   ```bash
   cd cognito-appsync-bedrock
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Deploy the stack:
   ```bash
   npm run deploy
   ```
   This will generate a `cdk-outputs.json` file containing the stack outputs.

## Testing

The project includes integration tests in `test/cdk.test.ts`. These tests will:

1. Read deployed stack outputs from `cdk-outputs.json`
2. Programmatically sign up a new user in the Cognito User Pool
3. Admin-confirm the new user
4. Log in with the new user to obtain an ID token
5. Use the ID token to make an authenticated `invoke` mutation to the AppSync API with a sample prompt
6. Verify that the response from Bedrock (via AppSync) is received and contains expected content

To run the tests:

```bash
npm run test
```

> **Note**: The tests require the CDK stack to be deployed first, as they rely on the cdk-outputs.json file. Ensure the AWS region and credentials configured for your AWS CLI (and thus for the tests) match where the stack was deployed.

## Cleanup

To delete the stack and all associated resources:

```bash
cdk destroy --all
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
