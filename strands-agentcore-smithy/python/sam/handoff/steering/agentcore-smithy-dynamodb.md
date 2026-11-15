---
inclusion: auto
---

# AgentCore Smithy DynamoDB Agent — Implementation Guide

This project builds a serverless AI agent using AWS Bedrock AgentCore Gateway with a Smithy model target type connecting to DynamoDB. Follow these patterns strictly during implementation.

## Architecture

```
User → Agent Lambda (Strands SDK / Bedrock Claude 3 Sonnet)
     → Cognito JWT auth
     → AgentCore Gateway (CUSTOM_JWT, Smithy model target)
     → DynamoDB (via GATEWAY_IAM_ROLE auth)
```

## Target Type: Smithy Model (NOT API Gateway, NOT OpenAPI)

- GatewayTarget TargetConfiguration must be nested: `Mcp.SmithyModel` (not top-level)
- Use `InlinePayload` for the Smithy model JSON (or S3 for models >10MB)
- Smithy model MUST use `aws.protocols#restJson1` trait on the service
- Operations need `smithy.api#http` trait with method and URI
- Credential type is `GATEWAY_IAM_ROLE` (NOT `API_KEY`) — DynamoDB uses IAM auth
- No credential provider CLI dance needed — IAM role handles auth
- No API Gateway, no API keys, no secrets for target auth

## Smithy Model Rules

1. Must use `aws.protocols#restJson1` trait on the service shape
2. Every operation needs `smithy.api#http` trait with method and URI
3. Input members use `smithy.api#httpQuery` for query params, `smithy.api#httpLabel` for path params
4. Use `smithy.api#required` trait for mandatory fields
5. Only RestJson protocol is supported
6. Max model size: 10MB
7. No streaming operations
8. Avoid dynamic endpoint patterns (security risk)

## DynamoDB Operations to Expose

Expose these DynamoDB operations via the Smithy model:
- `GetItem` — retrieve a single item by key
- `PutItem` — create or update an item
- `Query` — query items by partition key with optional sort key conditions

The LLM decides which operation to call based on the user's natural language prompt.

## AgentCore Gateway Resource (AWS::BedrockAgentCore::Gateway)

Required properties (case-sensitive):
- `ProtocolType: MCP` — REQUIRED, not optional
- `RoleArn` — NOT `ExecutionRoleArn` (extraneous key error)
- `AuthorizerType: CUSTOM_JWT`
- `AuthorizerConfiguration.CustomJWTAuthorizer` — NOT `JwtConfiguration` (extraneous key error)
  - Note: `CustomJWTAuthorizer` (all caps JWT), NOT `CustomJwtAuthorizer`
  - `DiscoveryUrl` must end with `/.well-known/openid-configuration`
  - `AllowedAudience` replaces the old `Audience` array

## Gateway Execution Role — All 4 ARN Patterns + DynamoDB

Missing any of the 4 core ARN patterns causes "Internal Error" on `tools/call` while `tools/list` works fine:

```yaml
Resource:
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:token-vault/default'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:token-vault/default/apikeycredentialprovider/*'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:workload-identity-directory/default'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:workload-identity-directory/default/workload-identity/${GatewayName}-*'
```

Additionally, add DynamoDB permissions for the target service:
```yaml
- PolicyName: DynamoDBAccess
  PolicyDocument:
    Version: '2012-10-17'
    Statement:
      - Effect: Allow
        Action:
          - dynamodb:GetItem
          - dynamodb:PutItem
          - dynamodb:Query
        Resource: !GetAtt ProductTable.Arn
```

Do NOT include `apigateway:GET` — no API Gateway in this project.

## Credential Provider Configuration (Smithy/DynamoDB)

Use `GATEWAY_IAM_ROLE` — no API key credential provider needed:
```yaml
CredentialProviderConfigurations:
  - CredentialProviderType: GATEWAY_IAM_ROLE
```

This means:
- No credential provider CLI commands
- No Secrets Manager secrets for target auth
- No stack re-update with credential provider ARN
- The Gateway execution role's DynamoDB permissions handle everything

## Agent Lambda — Strands SDK Rules

- Runtime: `python3.12`, Architecture: `x86_64`
- Timeout: minimum 120 seconds, Memory: minimum 1024 MB
- IAM must include ALL four Bedrock actions: `InvokeModel`, `InvokeModelWithResponseStream`, `Converse`, `ConverseStream`
- Do NOT use `with mcp_client:` context manager — let Agent manage the session, clean up in `finally` block
- Do NOT remove `.dist-info` directories during packaging (opentelemetry needs them)
- If zip > 50MB, upload to S3 first then update Lambda from S3

## Lambda Dependencies (requirements.txt)

All four are required:
```
strands-agents>=1.0.0
mcp>=1.0.0
requests>=2.31.0
PyJWT[crypto]>=2.8.0
```

## Lambda Packaging — Two-Step pip Install (CRITICAL)

`--only-binary=:all:` with `--platform` silently skips pure Python packages. You MUST use a two-step install:

```bash
# Step 1: Binary packages
pip3 install --target $DIR --platform manylinux2014_x86_64 --python-version 3.12 --only-binary=:all: -r requirements.txt

# Step 2: Pure Python packages (skipped by step 1)
pip3 install --target $DIR --platform manylinux2014_x86_64 --python-version 3.12 --only-binary=:all: --no-deps \
  requests urllib3 charset-normalizer idna certifi PyJWT cryptography cffi
```

## JWT Validation — ID Tokens, Not Access Tokens

Cognito `USER_PASSWORD_AUTH` flow returns an ID token. The JWT validation code MUST:
- Accept both `token_use: access` and `token_use: id`
- Disable audience verification (`verify_aud: False`) — Gateway handles it via `AllowedAudience`
- Handle ID token claim names: `cognito:username` (not `username`), `aud` (not `client_id`)

## Deployment Order (Simplified — No Credential Provider Dance)

1. Validate CloudFormation template
2. Deploy CloudFormation stack (DynamoDB table, AgentCore Gateway, Cognito, Lambda, IAM)
3. Package Lambda code (two-step pip install)
4. Deploy Lambda code (50MB S3 fallback)
5. Seed DynamoDB table with sample data
6. Create test user in Cognito
7. Generate test script (`scripts/test.sh`)

No secrets, no credential provider CLI, no stack re-update. Much simpler than the API Gateway project.

## Deploy Script Pattern

- Stack create vs update: check `DOES_NOT_EXIST` pattern
- Use `pip3` not `pip`
- Generate `scripts/test.sh` with baked-in values — do NOT echo nested JSON commands
- Use `stat -f%z` (macOS) with `stat -c%s` fallback (Linux) for file size check

## Test Script

Generated by deploy.sh with baked-in values. Usage:
```bash
./scripts/test.sh                                              # default prompt
./scripts/test.sh 'Show me all products under $50'             # query
./scripts/test.sh 'Get the details for product ABC123'         # get item
./scripts/test.sh 'Add a new product called Widget for $29.99' # put item
```

Do NOT echo copy-paste test commands with nested JSON — shell escaping breaks `${ID_TOKEN}` substitution.

## Existing Code (Reuse As-Is from apigw project)

```
src/agent/handler.py          — Lambda entry point
src/agent/agent_processor.py  — MCP client + Strands Agent lifecycle
src/agent/strands_client.py   — Factory functions
src/shared/models.py          — UserContext, AgentRequest, AgentResponse
src/shared/logging_utils.py   — Structured logging
src/shared/error_utils.py     — Error handling
src/shared/jwt_utils.py       — JWT validation
```

These are target-type agnostic — they connect to AgentCore Gateway via MCP and don't care what's behind it.

## Region

All resources MUST be deployed in `us-east-1` (BedrockAgentCore availability).

## Resources NOT Needed (from apigw project)

Do NOT create any of these:
- `RestApi`, API Gateway resources, methods, deployments, stages
- `ApiKey`, `UsagePlan`, `UsagePlanKey`
- Secrets Manager secrets for API keys
- Credential provider CLI commands
- `apigateway:GET` IAM policy
