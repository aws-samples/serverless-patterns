# AWS AppSync and Amazon Cognito to Amazon Bedrock via AWS Lambda

This pattern demonstrates how to invoke Amazon Bedrock models from AWS AppSync using an AWS Lambda resolver, with user authentication handled by Amazon Cognito.

> **Note**: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Prerequisites

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node and NPM](https://nodejs.org/en/download/) installed (Node.js 20.x recommended as used by the Lambda function)
- [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) installed
- This pattern is region-driven. Deploy it in an AWS Region that supports the selected Bedrock model or inference profile.
- The default Bedrock target is the global Amazon Nova 2 Lite inference profile `global.amazon.nova-2-lite-v1:0`, which is available from `ap-south-1` and other [documented source Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html#model-card-amazon-nova-2-lite-regions).
- Access to Amazon Bedrock foundation models is enabled by default when the caller has the required AWS Marketplace and IAM permissions. Anthropic models additionally require a one-time use-case submission before first use.

## Architecture

This pattern sets up an AWS AppSync GraphQL API configured with Amazon Cognito User Pools for authentication. Authenticated users can send a prompt through a GraphQL mutation (`invoke`).

![Architecture Diagram](diagram.png)

### Flow

1. **Authentication**: Users are authenticated against an Amazon Cognito User Pool
2. **AppSync Mutation**: The client sends a GraphQL mutation including the prompt and a valid Cognito ID token
3. **Lambda resolver**: AppSync uses an AWS Lambda resolver to process the `invoke` mutation
4. **Bedrock Invocation**: The AWS Lambda function receives the prompt from AppSync, builds the correct Bedrock payload for the configured model family, and invokes Bedrock. The default deployment uses the Nova inference profile and includes IAM permission both for the inference profile ARN and the routed foundation-model ARNs.
5. **Response**: The Bedrock model processes the prompt and returns a response. The Lambda function forwards this response back to AppSync, which then relays it to the client

### Resources

The AWS CDK project under `cognito-appsync-bedrock/cdk` provisions the following resources:

- An Amazon Cognito User Pool and User Pool Client
- An AWS AppSync GraphQL API (`schema.gql`) with Cognito User Pool as the default authorization mode
- An AWS Lambda function with permissions to invoke the specified Bedrock model
- An AppSync Lambda Data Source and a Resolver connecting the `invoke` mutation to the Lambda function
- CloudFormation outputs for easy access to API endpoints and Cognito identifiers

The Bedrock model ID and inference parameters can be configured in `cognito-appsync-bedrock/cdk/lib/cdk-stack.ts` and consumed in `cognito-appsync-bedrock/cdk/src/lambda/invokeBedrock/index.ts`.

## Step-By-Step Deployment

1. Clone the repository and move into the CDK project:

   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   cd serverless-patterns/cognito-appsync-bedrock/cdk
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Verify that your AWS CLI is pointed at the account and region you want to use:

   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```

4. Bootstrap the target account and region if this environment has not been bootstrapped yet:

   ```bash
   # Example account ID and AWS Region code; replace both values for your environment.
   ./node_modules/.bin/cdk bootstrap aws://123456789012/us-east-1
   ```

5. Build the TypeScript project:

   ```bash
   npm run build
   ```

6. Deploy the stack:

   ```bash
   npm run deploy
   ```

7. Confirm that `cdk-outputs.json` was created:

   ```bash
   cat cdk-outputs.json
   ```

8. Verify that the output file contains these values under `AppsyncBedrockCognitoStack`:

   - `GraphQLApiUrl`
   - `AWSRegion`
   - `CognitoUserPoolId`
   - `CognitoUserPoolClientId`
   - `BedrockModelIdUsed`

9. For the most detailed instructions, troubleshooting notes, and exact test flow, continue with [`cognito-appsync-bedrock/cdk/README.md`](cdk/README.md).

## Using A Different Bedrock Model

You can use a different Amazon Bedrock model with this pattern, but you need to verify three things before deploying:

1. The model or inference profile is available in your target AWS region
2. Your deployment role and Lambda execution role have the required IAM and AWS Marketplace permissions
3. The Lambda request and response handling matches that model family

### Step 1: Find the model or inference profile you want to use

- Open the Amazon Bedrock console for your target region
- Check model and inference-profile availability in the deployment Region
- If the model is invoked through an inference profile, use the inference profile ID instead of the raw foundation model ID

Examples:

- Default model used by this pattern: `global.amazon.nova-2-lite-v1:0`
- Example Anthropic model: `anthropic.claude-3-sonnet-20240229-v1:0`
- Example US Anthropic inference profile: `us.anthropic.claude-3-5-sonnet-20240620-v1:0`

### Step 2: Verify permissions and regional availability

- Access to Amazon Bedrock foundation models is enabled by default when the caller has the required AWS Marketplace and IAM permissions.
- Anthropic models require a one-time use-case submission before their first invocation.
- Use the CLI to confirm that a model or inference-profile ID exists in the deployment Region:

```bash
aws bedrock list-foundation-models --region us-east-1
aws bedrock list-inference-profiles --region us-east-1
aws bedrock get-inference-profile \
  --inference-profile-identifier global.amazon.nova-2-lite-v1:0 \
  --region us-east-1
```

### Step 3: Update the model configured by this pattern

Change the `modelIdForLambda` value in `cognito-appsync-bedrock/cdk/lib/cdk-stack.ts`.

Examples:

- Amazon Nova 2 Lite global inference profile:

  ```ts
  const modelIdForLambda = "global.amazon.nova-2-lite-v1:0";
  ```

- Anthropic foundation model:

  ```ts
  const modelIdForLambda = "anthropic.claude-3-sonnet-20240229-v1:0";
  ```

### Step 4: Confirm the Lambda payload format matches the model family

The Lambda handler in `cognito-appsync-bedrock/cdk/src/lambda/invokeBedrock/index.ts` currently supports:

- Amazon Nova-style payloads and responses
- Anthropic-style Messages API payloads and responses

If you change to another provider or another model family with a different request schema, update:

- The request body sent in `InvokeModelCommand`
- The response parsing logic
- Any model-specific inference parameters

### Step 5: Confirm the IAM permissions match the model type

- Foundation models require permission on the foundation-model ARN
- Inference profiles require permission on the inference-profile ARN
- Some inference profiles can route requests across regions, so the Lambda role may also need permission on the underlying foundation-model ARNs

This pattern handles `global.`, `us.`, `eu.`, `apac.`, `jp.`, and `au.` system-defined inference-profile IDs and grants access to the routed foundation-model ARNs.

### Step 6: Redeploy and verify

After changing the model:

```bash
npm run build
npm run deploy
cat cdk-outputs.json
npm run test
```

Verify that `BedrockModelIdUsed` in `cdk-outputs.json` matches the model you selected.

## Testing

The CDK project includes:

- `test/appsyncRequest.test.ts` for the AppSync transport helper
- `test/cdk-stack.test.ts` for the synthesized Lambda model and IAM configuration
- `test/invokeBedrock.test.ts` for the Lambda region-selection helper
- `test/cdk.test.ts` for the live Cognito + AppSync + Lambda + Bedrock flow

The integration test will:

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

Important notes:

- The integration test requires `cdk-outputs.json`
- If `cdk-outputs.json` is missing, only the transport unit test runs and the deployment-backed test is skipped
- The integration test uses a longer timeout because Bedrock invocation is a live network call
- The test creates a temporary Cognito user and deletes it during cleanup

## Troubleshooting

- If deployment fails with `No bucket named cdk-hnb659fds-assets-ACCOUNT-REGION`, rerun CDK bootstrap for the target account and region
- If Bedrock reports an invalid model identifier, confirm the exact model or inference-profile ID in the deployment Region with `aws bedrock get-inference-profile` or `aws bedrock list-inference-profiles`
- If Bedrock returns an authorization error, verify the Lambda role's IAM permissions, required AWS Marketplace permissions, and any applicable organization SCPs
- For an Anthropic model's first invocation, complete the one-time use-case submission if requested
- If AppSync returns a GraphQL error during testing, inspect the Lambda logs and the test output together
- If Cognito sign-up or login fails, verify your AWS CLI credentials, region, and generated `cdk-outputs.json`

## Cleanup

To delete the stack and remove the resources created by this pattern:

```bash
cd cognito-appsync-bedrock/cdk
./node_modules/.bin/cdk destroy AppsyncBedrockCognitoStack
```

Recommended cleanup flow:

1. Move into the CDK project directory
2. Make sure your AWS CLI is still pointing to the same account and region used for deployment
3. Run the destroy command
4. Confirm the destroy operation when CDK prompts you
5. After the stack is deleted, verify in the CloudFormation console that `AppsyncBedrockCognitoStack` no longer exists

What this cleanup removes:

- The AppSync API
- The Cognito User Pool and User Pool Client
- The Lambda function and related IAM roles created by this stack
- The AppSync resolver and Lambda data source

What to keep in mind:

- `cdk-outputs.json` is a local file and is not deleted automatically
- Shared CDK bootstrap resources are not removed by destroying this application stack
- If you created additional users or changed resources manually outside this stack, those manual changes may need separate cleanup

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
