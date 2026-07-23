# Amazon Verified Permissions with AWS Lambda

This pattern deploys a Lambda function that authorizes requests using Amazon Verified Permissions with Cedar policies for fine-grained access control.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-verified-permissions-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 22+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed

## Architecture

![Architecture Diagram](architecture.png)

1. Client sends a SigV4-signed request to the Lambda Function URL.
2. Lambda receives the authorization request with user identity, action, and resource.
3. Lambda calls the Verified Permissions `IsAuthorized` API with the request context.
4. Cedar policies evaluate the request and return ALLOW or DENY.

## Cedar Policies

The pattern includes four policies demonstrating different authorization patterns:

- **Admin policy** – Admins can read, write, and delete documents (scoped to explicit actions).
- **Reader policy** – Readers can only read documents.
- **Owner policy** – Document owners can write to their own documents.
- **Confidential deny policy** – Readers cannot access confidential documents.

## Deployment

```bash
cd src && npm install && cd ..
npm install
cdk deploy
```

## Testing

The Lambda Function URL uses `AWS_IAM` authentication, so requests must be signed with [SigV4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html). The simplest way is using `curl` with `--aws-sigv4`:

```bash
# Get the Function URL from stack outputs
FUNCTION_URL=$(aws cloudformation describe-stacks \
  --stack-name LambdaVerifiedPermissionsStack \
  --query 'Stacks[0].Outputs[?OutputKey==`FunctionUrl`].OutputValue' \
  --output text)

# Admin can delete (ALLOW)
curl -s "$FUNCTION_URL" \
  --aws-sigv4 "aws:amz:us-east-1:lambda" \
  --user "$(aws configure get aws_access_key_id):$(aws configure get aws_secret_access_key)" \
  -H "Content-Type: application/json" \
  -d '{"userId":"alice","role":"admin","action":"Delete","resourceId":"doc-1","classification":"confidential"}'

# Reader cannot delete (DENY)
curl -s "$FUNCTION_URL" \
  --aws-sigv4 "aws:amz:us-east-1:lambda" \
  --user "$(aws configure get aws_access_key_id):$(aws configure get aws_secret_access_key)" \
  -H "Content-Type: application/json" \
  -d '{"userId":"bob","role":"reader","action":"Delete","resourceId":"doc-2","classification":"public"}'

# Reader cannot access confidential documents (DENY)
curl -s "$FUNCTION_URL" \
  --aws-sigv4 "aws:amz:us-east-1:lambda" \
  --user "$(aws configure get aws_access_key_id):$(aws configure get aws_secret_access_key)" \
  -H "Content-Type: application/json" \
  -d '{"userId":"bob","role":"reader","action":"Read","resourceId":"doc-3","classification":"confidential"}'
```

> **Note:** Replace `us-east-1` with your deployment region. If using temporary credentials (e.g., SSO), include the session token via `--header "x-amz-security-token: $AWS_SESSION_TOKEN"`.

## Cleanup

```bash
cdk destroy
```
