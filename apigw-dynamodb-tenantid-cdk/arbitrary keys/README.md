# API Gateway with Cognito, Arbitrary Usage Identifier Keys (AUIK), and Lambda Authorizer

This pattern demonstrates API Gateway with a Cognito-authenticated Lambda authorizer that returns arbitrary usage identifier keys per the AUIK specification.

## How it works

![Architecture Diagram](./apigw-arbitrary-keys.drawio)

1. Client authenticates with Amazon Cognito and receives a JWT (ID token) containing the custom `tenantId` claim
2. Client sends a request with the JWT in the `Authorization` header
3. API Gateway forwards the token to the Lambda authorizer
4. The authorizer:
   - Decodes the JWT and extracts the `custom:tenantId` claim
   - Extracts the **stage** from the method ARN
   - Generates a random 128-character arbitrary API key
   - Calls `GetUsagePlans` to find a usage plan associated with the API + stage
   - Returns `usageIdentifierKey` (always) and `usagePlanId` (if a plan exists for the stage)
5. API Gateway uses the returned key for throttling/quota enforcement against the usage plan

Per the AUIK docs: if no `usagePlanId` is returned, API Gateway treats `usageIdentifierKey` as a configured API Key.

## Authorizer Response Format

```json
{
  "principalId": "tenant-id",
  "policyDocument": { ... },
  "usageIdentifierKey": "<128-char-random-key>",
  "usagePlanId": "<usage-plan-id>"
}
```

## Prerequisites

- AWS account allowlisted
- Node.js, npm, AWS CDK installed

## Deploy

```bash
cd "arbitrary keys"
npm install
cdk deploy
```

Note the outputs: Prod/Dev API URLs, Usage Plan IDs, Cognito User Pool ID, and User Pool Client ID.

## Test

1. Create a Cognito user with a tenantId:
    ```bash
    aws cognito-idp admin-create-user \
      --user-pool-id USER_POOL_ID \
      --username user@example.com \
      --user-attributes Name=email,Value=user@example.com Name=custom:tenantId,Value=my-tenant \
      --temporary-password "TempPass1!"
    ```

1. Set a permanent password:
    ```bash
    aws cognito-idp admin-set-user-password \
      --user-pool-id USER_POOL_ID \
      --username user@example.com \
      --password "MySecurePass1!" \
      --permanent
    ```

1. Get a token and call the API using the helper script:
    ```bash
    node get-token.js --user-pool-id USER_POOL_ID --client-id CLIENT_ID \
      --username user@example.com --password "MySecurePass1!" \
      --api-url https://<api-id>.execute-api.<region>.amazonaws.com/prod/protected
    ```

1. Without a token (should fail):
    ```bash
    curl https://<api-id>.execute-api.<region>.amazonaws.com/prod/protected
    ```

## Cleanup

```bash
cdk destroy
```
