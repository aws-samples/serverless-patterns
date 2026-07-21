---
inclusion: auto
---

# AgentCore Smithy Bedrock Runtime Agent — Implementation Guide

This project builds a serverless AI agent using AWS Bedrock AgentCore Gateway with a Smithy model target type connecting to Bedrock Runtime. The agent uses Claude Sonnet as the main LLM and calls Claude Haiku as a tool via the gateway's Converse API. Follow these patterns strictly during implementation.

## Architecture

```
User → Agent Lambda (Strands SDK / Bedrock Claude 3 Sonnet)
     → Cognito JWT auth
     → AgentCore Gateway (CUSTOM_JWT, Smithy model target)
     → Bedrock Runtime (via GATEWAY_IAM_ROLE auth)
```

## Target Type: Smithy Model (NOT API Gateway, NOT OpenAPI)

- GatewayTarget TargetConfiguration must be nested: `Mcp.SmithyModel` (not top-level)
- Use official AWS Smithy model from `github.com/aws/api-models-aws` — upload to S3 and reference via `SmithyModel.S3.Uri`
- Custom Smithy models do NOT work for AWS services (missing endpoint resolution metadata)
- Credential type is `GATEWAY_IAM_ROLE` (NOT `API_KEY`) — Bedrock uses IAM auth
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
9. Must include `aws.auth#sigv4` trait on the service with the target service name (e.g. `"name": "bedrock"`)

## KNOWN LIMITATION: Smithy Model Target + DynamoDB Protocol Mismatch

The AgentCore Gateway's Smithy model target only supports `aws.protocols#restJson1` (path-based REST routing). DynamoDB uses `aws.protocols#awsJson1_0` (single POST endpoint with `X-Amz-Target` header). This protocol mismatch means the gateway cannot translate Smithy model tool calls into valid DynamoDB API requests — the last hop (gateway → DynamoDB) returns "internal error" even though the entire agent pipeline up to that point works correctly.

This affects any AWS service that uses `awsJson1_0` or `awsJson1_1` protocols (DynamoDB, SQS, SNS, etc.). The Smithy model target type works for services with REST-style APIs (`restJson1`, `restXml`).

Workaround options:
- Use the API Gateway target type with a REST API proxy in front of DynamoDB
- Use a Lambda target that calls DynamoDB directly
- Wait for AgentCore to add `awsJson1_0` protocol support for Smithy model targets

## SOLUTION: Targeting Bedrock Runtime Instead of DynamoDB

Since DynamoDB uses `awsJson1_0`, we pivoted to targeting Bedrock Runtime (which uses `restJson1`). The agent now calls another model (Claude Haiku) as a tool via the gateway. Here's what we learned:

### 1. Custom Smithy Models Cannot Resolve AWS Service Endpoints

A hand-written Smithy model with just `aws.auth#sigv4` and `aws.protocols#restJson1` is NOT enough for AWS services. The gateway derives the endpoint entirely from the model's built-in metadata:
- `aws.api#service` trait (with `sdkId`, `arnNamespace`, `endpointPrefix`)
- Full `smithy.rules#endpointRuleSet` with partition data, FIPS/DualStack logic

A custom `endpointRuleSet` pointing to `https://bedrock-runtime.us-east-1.amazonaws.com` does NOT work — the gateway needs the complete partition data.

**Fix:** Use the official AWS Smithy model from `github.com/aws/api-models-aws`. Upload to S3 and reference via `SmithyModel.S3.Uri` (not `S3Configuration`):
```yaml
SmithyModel:
  S3:
    Uri: !Sub 's3://${AWS::StackName}-smithy-models/bedrock-runtime-2023-09-30.json'
```

### 2. InvokeModel's Blob Body Doesn't Map to MCP Tool Inputs

The official Bedrock Runtime model's `InvokeModel` operation uses `Blob` with `httpPayload` trait for the request body. When the gateway converts this to an MCP tool, the blob field disappears — there's no input parameter for the LLM to pass the actual prompt body. The LLM tries to pass it as `content` but that's not a recognized field.

**Fix:** Use `Converse` instead of `InvokeModel`. Converse has structured `messages` and `modelId` fields that map cleanly to MCP tool input parameters.

### 3. Gateway Execution Role Needs Broad Bedrock Permissions

`bedrock:InvokeModel` on `arn:aws:bedrock:{region}::foundation-model/*` is not enough. Cross-region inference profiles (like `us.anthropic.claude-3-haiku-20240307-v1:0`) use different ARN patterns.

**Fix:** Broad permissions on `*`:
```yaml
- PolicyName: BedrockRuntimeAccess
  PolicyDocument:
    Version: '2012-10-17'
    Statement:
      - Effect: Allow
        Action:
          - bedrock:InvokeModel
          - bedrock:InvokeModelWithResponseStream
          - bedrock:Converse
          - bedrock:ConverseStream
        Resource: '*'
```

### 4. System Prompt Required for Correct Tool Usage

The official Smithy model exposes 10+ tools (InvokeModel, Converse, ConverseStream, CountTokens, etc.) with complex schemas. Without guidance, the LLM guesses wrong model IDs and message formats.

**Fix:** Add a system prompt to the Strands Agent telling it exactly which tool, model ID, and message format to use:
```python
SYSTEM_PROMPT = """Use the Converse tool (not InvokeModel).
- Set modelId to: us.anthropic.claude-3-haiku-20240307-v1:0
- Set messages to: [{"role": "user", "content": [{"text": "YOUR PROMPT"}]}]
- Only try ONCE"""
agent = Agent(model=bedrock_model, tools=[mcp_client], system_prompt=SYSTEM_PROMPT)
```

## Bedrock Runtime Operations Exposed

The official Smithy model exposes all Bedrock Runtime operations as MCP tools. The key ones:
- `Converse` — structured conversation API (USE THIS — maps cleanly to MCP tool inputs)
- `InvokeModel` — raw model invocation (DO NOT USE — Blob httpPayload doesn't map to MCP tool inputs)
- `ConverseStream`, `InvokeModelWithResponseStream` — streaming variants (not supported by Smithy targets)
- `CountTokens`, `ListAsyncInvokes`, etc. — utility operations

The agent's system prompt directs it to use `Converse` with the correct model ID and message format.

## AgentCore Gateway Resource (AWS::BedrockAgentCore::Gateway)

Required properties (case-sensitive):
- `ProtocolType: MCP` — REQUIRED, not optional
- `RoleArn` — NOT `ExecutionRoleArn` (extraneous key error)
- `AuthorizerType: CUSTOM_JWT`
- `AuthorizerConfiguration.CustomJWTAuthorizer` — NOT `JwtConfiguration` (extraneous key error)
  - Note: `CustomJWTAuthorizer` (all caps JWT), NOT `CustomJwtAuthorizer`
  - `DiscoveryUrl` must end with `/.well-known/openid-configuration`
  - `AllowedAudience` replaces the old `Audience` array

## Gateway Execution Role — All 4 ARN Patterns + Bedrock Runtime

Missing any of the 4 core ARN patterns causes "Internal Error" on `tools/call` while `tools/list` works fine:

```yaml
Resource:
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:token-vault/default'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:token-vault/default/apikeycredentialprovider/*'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:workload-identity-directory/default'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:workload-identity-directory/default/workload-identity/${GatewayName}-*'
```

Additionally, add Bedrock Runtime permissions (broad — cross-region inference profiles need `*`):
```yaml
- PolicyName: BedrockRuntimeAccess
  PolicyDocument:
    Version: '2012-10-17'
    Statement:
      - Effect: Allow
        Action:
          - bedrock:InvokeModel
          - bedrock:InvokeModelWithResponseStream
          - bedrock:Converse
          - bedrock:ConverseStream
        Resource: '*'
```

Do NOT include `apigateway:GET` — no API Gateway in this project.

## Credential Provider Configuration (Smithy/Bedrock Runtime)

Use `GATEWAY_IAM_ROLE` — no API key credential provider needed:
```yaml
CredentialProviderConfigurations:
  - CredentialProviderType: GATEWAY_IAM_ROLE
```

This means:
- No credential provider CLI commands
- No Secrets Manager secrets for target auth
- No stack re-update with credential provider ARN
- The Gateway execution role's Bedrock permissions handle everything

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

## Deployment Order

1. Validate CloudFormation template
2. Upload official Smithy model to S3
3. Deploy CloudFormation stack (AgentCore Gateway, Cognito, Lambda, IAM)
4. Package Lambda code (two-step pip install)
5. Deploy Lambda code (50MB S3 fallback)
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
./scripts/test.sh                                                                          # default prompt
./scripts/test.sh 'Use the invoke model tool to ask Haiku to write a haiku about clouds'   # invoke Haiku
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
