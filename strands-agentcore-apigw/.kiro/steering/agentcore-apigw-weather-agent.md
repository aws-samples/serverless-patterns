---
inclusion: auto
---

# AgentCore API Gateway Weather Agent — Implementation Guide

This project builds a serverless AI weather agent using AWS Bedrock AgentCore Gateway with an API Gateway target type. Follow these patterns strictly during implementation.

## Architecture

```
User → Agent Lambda (Strands SDK / Bedrock Claude Sonnet 4.6)
     → Cognito JWT auth
     → AgentCore Gateway (CUSTOM_JWT, API Gateway target)
     → API Gateway REST API (API key validated via usage plan)
     → WeatherAPI.com (HTTP_PROXY integration)
```

## Target Type: API Gateway (NOT OpenAPI)

- GatewayTarget TargetConfiguration must be nested: `Mcp.ApiGateway` (not top-level `ApiGateway`)
- Use `RestApiId` (not `ApiId`) inside the ApiGateway block
- `ApiGatewayToolConfiguration` is REQUIRED with `ToolFilters` array
- Each API method MUST have either an `operationId` in the OpenAPI export OR a `ToolOverrides` entry — otherwise AgentCore fails with "no operationId and no override provided"
- API Gateway methods MUST have `MethodResponses` defined — AgentCore parses the exported OpenAPI spec and fails with "responses is missing" if omitted
- AgentCore auto-discovers operations via `GetExportAPI` — do NOT provide an OpenAPI spec manually
- Credential type must be `API_KEY` (not `GATEWAY_IAM_ROLE` or `OAUTH`)

## Two Separate API Keys

1. **AgentCore → API Gateway**: Managed by credential provider, injected as `x-api-key` header
2. **API Gateway → WeatherAPI.com**: Injected via stage variable in integration request parameters

These are independent. Do not conflate them.

## AgentCore Gateway Resource (AWS::BedrockAgentCore::Gateway)

Required properties (case-sensitive):
- `ProtocolType: MCP` — REQUIRED, not optional
- `RoleArn` — NOT `ExecutionRoleArn` (extraneous key error)
- `AuthorizerType: CUSTOM_JWT`
- `AuthorizerConfiguration.CustomJWTAuthorizer` — NOT `JwtConfiguration` (extraneous key error)
  - Note: `CustomJWTAuthorizer` (all caps JWT), NOT `CustomJwtAuthorizer`
  - `DiscoveryUrl` must end with `/.well-known/openid-configuration`
  - `AllowedAudience` replaces the old `Audience` array

## Credential Provider Configuration (GatewayTarget)

The `CredentialProviderConfigurations` structure is nested:
```yaml
CredentialProviderConfigurations:
  - CredentialProviderType: API_KEY
    CredentialProvider:
      ApiKeyCredentialProvider:
        ProviderArn: <credential-provider-arn>
        CredentialLocation: HEADER
        CredentialParameterName: x-api-key
```
Do NOT put `ProviderArn` directly under the configuration item — it must be inside `CredentialProvider.ApiKeyCredentialProvider`.

## Credential Provider — CLI Detection and Create/Update

The credential provider is NOT a CloudFormation resource. Manage via CLI (requires AWS CLI 2.28+).

To detect CLI support, use `list-api-key-credential-providers` — do NOT use `help` (it's buggy and returns "list index out of range" even when the CLI supports the commands):
```bash
# Detect support (correct)
aws bedrock-agentcore-control list-api-key-credential-providers --region us-east-1

# Detect support (WRONG — help is buggy)
# aws bedrock-agentcore-control create-api-key-credential-provider help
```

Create or update:
```bash
# Create new
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name <name> --api-key <value> --region us-east-1

# Update existing (e.g. after stack recreate with new API key)
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name <name> --api-key <new-value> --region us-east-1
```
Or create manually in the AWS Console under Bedrock → AgentCore → Identity → Outbound Auth.

## Stage Variable Secret Reference

Use `!Sub` with dynamic reference to resolve the WeatherAPI key from Secrets Manager:
```yaml
Variables:
  weatherApiKey: !Sub '{{resolve:secretsmanager:${WeatherApiKeySecretArn}}}'
```
Do NOT hardcode `PLACEHOLDER` — CloudFormation resolves dynamic references at deploy time.

## CloudFormation Dependency Chain (CRITICAL)

```
RestApi → Resource(/weather) → Resource(/weather/current) → Method(GET)
Method → Deployment (DependsOn: ALL methods) → Stage
Stage → UsagePlan + ApiKey (both DependsOn: Stage) → UsagePlanKey
```

- `ApiDeployment` MUST have `DependsOn` for every Method resource
- `ApiKey` MUST depend on `ApiStage`
- `UsagePlan` references stage by name string, not `!Ref`
- Every method MUST have `ApiKeyRequired: true`

## Gateway Execution Role — All 4 ARN Patterns Required

Missing any causes "Internal Error" on `tools/call` while `tools/list` works fine:

```yaml
Resource:
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:token-vault/default'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:token-vault/default/apikeycredentialprovider/*'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:workload-identity-directory/default'
  - !Sub 'arn:aws:bedrock-agentcore:${AWS::Region}:${AWS::AccountId}:workload-identity-directory/default/workload-identity/${GatewayName}-*'
```

Also needs: `apigateway:GET` on REST API exports resource for GetExportAPI.

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
`requests` and `PyJWT` are used by `jwt_utils.py` for JWKS fetching and token validation. `[crypto]` pulls in `cryptography` for RS256 signature verification.

## Lambda Packaging — Two-Step pip Install (CRITICAL)

`--only-binary=:all:` with `--platform` silently skips pure Python packages like `requests`, `PyJWT`, `urllib3`, etc. You MUST use a two-step install:

```bash
# Step 1: Binary packages (strands, mcp, and their native deps)
pip3 install --target $DIR --platform manylinux2014_x86_64 --python-version 3.12 --only-binary=:all: -r requirements.txt

# Step 2: Pure Python packages (skipped by step 1)
pip3 install --target $DIR --platform manylinux2014_x86_64 --python-version 3.12 --only-binary=:all: --no-deps \
  requests urllib3 charset-normalizer idna certifi PyJWT cryptography cffi
```
The `--no-deps` flag in step 2 prevents re-resolving dependencies already installed in step 1.

## JWT Validation — ID Tokens, Not Access Tokens

Cognito `USER_PASSWORD_AUTH` flow returns an ID token. The JWT validation code MUST:
- Accept both `token_use: access` and `token_use: id` (AgentCore Gateway expects ID tokens)
- Disable audience verification (`verify_aud: False`) — the ID token contains `aud` (client ID) which PyJWT tries to verify against nothing, causing "Invalid audience" errors. The Gateway handles audience validation via `AllowedAudience` in its config.
- Handle ID token claim names: `cognito:username` (not `username`), `aud` (not `client_id`)

## Deployment Order

1. Create Secrets Manager secrets (WeatherAPI key + placeholder APIGW key)
2. Deploy CloudFormation stack
3. Retrieve actual API Gateway key value from stack
4. Update Secrets Manager secret with real key
5. Create/update credential provider via CLI (auto-detected)
6. Update stack with credential provider ARN
7. Package and deploy Lambda code (two-step pip install)
8. Create test user
9. Generate test script (`scripts/test.sh`)

## Test Script

The deploy script generates `scripts/test.sh` with baked-in values (client ID, function name, region, credentials). This avoids shell escaping issues with nested JSON payloads. Usage:
```bash
./scripts/test.sh                                          # default: London, UK
./scripts/test.sh 'What is the weather in Liverpool, UK?'  # custom prompt
```
Do NOT try to echo copy-paste test commands with nested JSON — the escaping is fragile and breaks `${ID_TOKEN}` substitution.

## Region

All resources MUST be deployed in `us-east-1` (BedrockAgentCore availability).

## Existing Code (Reuse As-Is)

```
src/agent/handler.py          — Lambda entry point
src/agent/agent_processor.py  — MCP client + Strands Agent lifecycle
src/agent/strands_client.py   — Factory functions
src/shared/models.py          — UserContext, AgentRequest, AgentResponse
src/shared/logging_utils.py   — Structured logging
src/shared/error_utils.py     — Error handling
src/shared/jwt_utils.py       — JWT validation
```

## Custom Resource Lambdas

If writing any custom resource handlers:
- Use `urllib.request` (NOT `urllib3` — not available in Python 3.12 Lambda runtime)
- MUST send responses for ALL request types (Create, Update, Delete)
- Failure to respond causes 1-hour timeout and stack failure

## WeatherAPI Key Injection Pattern

Inject the WeatherAPI.com key via stage variable in the integration request:

```yaml
Integration:
  Type: HTTP_PROXY
  RequestParameters:
    integration.request.querystring.key: stageVariables.weatherApiKey
```

The stage variable value is resolved from Secrets Manager at deploy time via `!Sub '{{resolve:secretsmanager:${WeatherApiKeySecretArn}}}'`.
