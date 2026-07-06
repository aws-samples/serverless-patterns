# AgentCore API Gateway Weather Agent

A serverless AI weather agent built on Amazon Bedrock AgentCore. Uses the Strands SDK to orchestrate an LLM (Claude Sonnet 4.6) that calls weather tools exposed through an Amazon Bedrock AgentCore Gateway backed by Amazon API Gateway and [Open-Meteo](https://open-meteo.com/) (a free, key-less weather API). Authentication is handled by Amazon Cognito, and the agent runs on AWS Lambda.

The agent auto-discovers two tools: `geocodeLocation` (resolve a city name to coordinates) and `getCurrentWeather` (fetch current conditions for those coordinates). Asked "what's the weather in London?", it chains them — geocode first, then forecast.

> **This pattern is a reusable integration template, not just a weather demo.** Weather is the concrete example, but the architecture applies to *any* Amazon API Gateway REST stage you want to expose as an MCP tool for an AI agent — internal microservices, third-party APIs, or data APIs. Swap the backend URL in the API Gateway integration and the agent automatically discovers the new tools via AgentCore's OpenAPI export. See [Extending to Other APIs](#extending-to-other-apis).

## Architecture

![Architecture Diagram](architecture/apigateway-target.png)

```
User → Agent Lambda → AgentCore Gateway (MCP) → API Gateway → Open-Meteo
         │                    │                      │          (forecast +
    Strands Agent        CUSTOM_JWT Auth         API Key Auth    geocoding,
    + BedrockModel       + MCP Routing           (credential     no key)
    + MCPClient          + Tool Discovery         provider)
         │
    Cognito JWT
    Validated
```

The LLM decides which tool to call. Amazon Bedrock AgentCore auto-discovers available tools from the Amazon API Gateway OpenAPI export and presents them to the agent via MCP `tools/list`. When the agent calls a tool, AgentCore routes the request to API Gateway, authenticating with an API key managed by a credential provider. API Gateway proxies to Open-Meteo, which needs no key.

### Who does what

| Component | Responsibility |
|-----------|----------------|
| **LLM (Claude on Amazon Bedrock)** | Decides *which* tool to call and *what* arguments to pass (e.g. the coordinates returned by geocoding) |
| **Strands SDK (in the Lambda)** | Owns the agentic loop — a single `agent(prompt)` call runs prompt → model reasoning → tool selection → tool execution → repeat → final response. Connects to the Gateway via an `MCPClient` and executes whatever tool the model picks. |
| **AgentCore Gateway** | Auto-discovers tools from the API Gateway OpenAPI export, exposes them over MCP (`tools/list`), validates the inbound Cognito JWT, and routes tool calls to API Gateway using the outbound API-key credential provider |
| **API Gateway → Open-Meteo** | The tool backend — two REST paths (`/geocoding`, `/weather/current`) proxied to Open-Meteo |

### Example: multi-tool chaining

Asked *"what's the weather in Liverpool?"*, the model chains both tools in one `agent()` call — the Strands SDK executes each call the model requests and feeds the result back:

```
Tool #1: geocodeLocation   → resolves "Liverpool" to lat 53.41, lon -2.98
Tool #2: getCurrentWeather → fetches the forecast for those coordinates
→ model composes the final natural-language answer
```

The LLM chooses the tools and arguments; the Strands SDK runs the loop and executes the calls; AgentCore discovers, routes, and authenticates. No tool wiring lives in the Lambda code — the agent adapts to whatever the Gateway discovers.

## Prerequisites

- AWS SAM CLI ([install guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html))
- AWS CLI 2.28+ (required for `bedrock-agentcore-control` commands)
- Python 3 with `pip` (any recent 3.x — used only to drive the build; the Lambda's Linux dependencies are downloaded as prebuilt wheels, so a local `python3.12` is not required)
- GNU Make (preinstalled on macOS and most Linux distros)
- AWS account with Amazon Bedrock and Amazon Bedrock AgentCore enabled in `us-east-1`

No third-party API key or signup is needed — the backend uses [Open-Meteo](https://open-meteo.com/), which is free and key-less (non-commercial use; data under CC-BY 4.0).

> **No Docker required.** `sam build` uses a Makefile custom build (`src/Makefile`) that downloads `manylinux` wheels for the Lambda runtime, so the build works on any host OS without Docker or a matching local Python version.

## Quick Start

### Step 1: Open a Terminal

Open a terminal on your machine and navigate to where you want to clone the project.

### Step 2: Clone the Repository

```bash
git clone https://github.com/aws-samples/serverless-patterns
cd serverless-patterns/strands-agentcore-apigw
```

### Step 3: Deploy

```bash
./scripts/deploy.sh \
  --environment-name dev \
  --region us-east-1
```

The default LLM is `us.anthropic.claude-sonnet-4-6`. To use a different model, add `--bedrock-model-id`:

```bash
./scripts/deploy.sh \
  --environment-name dev \
  --bedrock-model-id us.anthropic.claude-haiku-4-5-20251001-v1:0
```

See [Changing the Model](#changing-the-model) for available model IDs.

The script handles everything in order:
1. Validates the SAM template (`sam validate`)
2. Creates an AWS Secrets Manager secret for the API Gateway key (used by the AgentCore credential provider)
3. Builds the application with `sam build` (a Makefile custom build downloads `manylinux` wheels matching the Lambda runtime — no Docker needed)
4. Deploys the stack with `sam deploy` (API Gateway, AgentCore Gateway, Cognito, Lambda, IAM)
5. Retrieves the API Gateway key and updates Secrets Manager
6. Creates/updates the AgentCore credential provider via CLI
7. Re-deploys with the credential provider ARN
8. Creates a test user in Cognito
9. Generates `scripts/test.sh` with baked-in values

### Step 4: Test

```bash
./scripts/test.sh
./scripts/test.sh 'What is the weather in Liverpool, England?'
```

The test script authenticates via Amazon Cognito, gets an ID token, and invokes the AWS Lambda function with your prompt.

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--environment-name` | Yes | Environment name (e.g. `dev`, `staging`, `prod`). Used for resource namespacing. |
| `--region` | No | AWS region (default: `us-east-1`) |
| `--s3-bucket` | No | S3 bucket for SAM deployment artifacts. If omitted, SAM uses its own managed bucket (`--resolve-s3`). |
| `--bedrock-model-id` | No | Bedrock model ID (default: `us.anthropic.claude-sonnet-4-6`) |


## Project Structure

```
├── architecture/
│   └── apigateway-target.png          # Architecture diagram
├── infrastructure/
│   └── template.yaml                  # SAM template: API GW, AgentCore, Cognito, Lambda, IAM
├── scripts/
│   ├── deploy.sh                      # One-command SAM deployment script
│   └── test.sh                        # Generated after deploy — end-to-end test (git-ignored)
├── src/
│   ├── requirements.txt               # Lambda dependencies (used by the build)
│   ├── Makefile                       # SAM custom build — downloads manylinux wheels (no Docker)
│   ├── agent/
│   │   ├── handler.py                 # Lambda entry point
│   │   ├── agent_processor.py         # MCP client + Strands Agent lifecycle
│   │   └── strands_client.py          # Factory functions
│   └── shared/
│       ├── models.py                  # UserContext, AgentRequest, AgentResponse
│       ├── jwt_utils.py               # JWT validation (Cognito ID tokens)
│       ├── error_utils.py             # Error handling
│       └── logging_utils.py           # Structured logging
├── tests/
│   ├── unit/
│   │   ├── test_sam_template.py
│   │   ├── test_properties.py         # Property-based tests
│   │   └── conftest.py
│   └── integration/
│       └── test_e2e.py
├── example-pattern.json               # Serverless Land pattern metadata
├── requirements.txt                   # Dev/test dependencies
└── README.md
```

## Changing the Model

The model is controlled by the `--bedrock-model-id` parameter. Claude Sonnet 4.6 and newer models on Amazon Bedrock **require a cross-region inference profile ID** — using the bare `anthropic.*` model ID will result in a `ValidationException`.

Profile IDs follow the pattern `<routing>.<model-id>`:
- `us.*` — routes within the US (lower latency for US-based workloads)
- `global.*` — routes globally (higher availability)

### Available Claude 4.x inference profiles

| Profile ID | Model |
|------------|-------|
| `us.anthropic.claude-sonnet-4-6` | Claude Sonnet 4.6 (US) — **default** |
| `global.anthropic.claude-sonnet-4-6` | Claude Sonnet 4.6 (Global) |
| `us.anthropic.claude-sonnet-4-5-20250929-v1:0` | Claude Sonnet 4.5 (US) |
| `us.anthropic.claude-sonnet-4-20250514-v1:0` | Claude Sonnet 4 (US) |
| `us.anthropic.claude-opus-4-7` | Claude Opus 4.7 (US) |
| `us.anthropic.claude-haiku-4-5-20251001-v1:0` | Claude Haiku 4.5 (US) — fastest/cheapest |

### Example

```bash
./scripts/deploy.sh \
  --environment-name dev \
  --bedrock-model-id us.anthropic.claude-haiku-4-5-20251001-v1:0
```

### Changing the model on an existing deployment

Re-run `deploy.sh` with the new model ID — no teardown needed. SAM rebuilds and redeploys the stack:

```bash
./scripts/deploy.sh \
  --environment-name dev \
  --bedrock-model-id us.anthropic.claude-opus-4-7
```

Alternatively, update just the Lambda environment variable directly (faster, skips infrastructure steps):

```bash
# 1. Get current environment variables
CURRENT_ENV=$(aws lambda get-function-configuration \
  --function-name dev-weather-agent \
  --region us-east-1 \
  --query 'Environment.Variables' --output json)

# 2. Update BEDROCK_MODEL_ID in place
NEW_ENV=$(echo $CURRENT_ENV | python3 -c "
import json, sys
env = json.load(sys.stdin)
env['BEDROCK_MODEL_ID'] = 'us.anthropic.claude-opus-4-7'
print(json.dumps({'Variables': env}))
")

# 3. Apply
aws lambda update-function-configuration \
  --function-name dev-weather-agent \
  --environment "$NEW_ENV" \
  --region us-east-1
```

To list all available inference profiles in your account:

```bash
aws bedrock list-inference-profiles --region us-east-1 \
  --query "inferenceProfileSummaries[].{id:inferenceProfileId,name:inferenceProfileName}" \
  --output table
```

## Extending to Other APIs

Weather is just the demo payload. The reusable part of this pattern is wiring an existing Amazon API Gateway REST stage into an AI agent as auto-discovered MCP tools. To point it at a different backend, change these pieces in `infrastructure/template.yaml`:

1. **API Gateway integration** — Update the `GetCurrentWeatherMethod` integration `Uri` (and add more `AWS::ApiGateway::Method` / `AWS::ApiGateway::Resource` resources for additional endpoints) to target your backend. AgentCore auto-discovers whatever operations the stage exposes via its OpenAPI export — you don't register tools manually.

2. **Tool filters / overrides** — Adjust `OpenMeteoTarget`'s `ApiGatewayToolConfiguration` (`ToolFilters` and `ToolOverrides`) to control which paths/methods are surfaced as tools and how they're named/described for the model.

3. **Backend authentication** — Open-Meteo needs no key, so this example injects nothing downstream. If your backend requires a key, inject it via an API Gateway stage variable sourced from Secrets Manager (add the parameter + stage variable back, then map it as an integration request parameter, e.g. `integration.request.querystring.key: stageVariables.apiKey`).

4. **Outbound credential provider (optional)** — AgentCore → API Gateway auth is handled by an API-key credential provider (`scripts/deploy.sh`, Step 7). If your API Gateway stage uses a different scheme (e.g. IAM auth or an OAuth authorizer), swap the credential provider type accordingly — AgentCore supports API key and OAuth outbound auth.

Nothing in the Lambda, Cognito, or agent code changes — the agent adapts automatically to whatever tools the Gateway discovers. In most cases, extending to a new API is purely an infrastructure change.

## Teardown

```bash
# Delete credential provider (managed via CLI, not the stack)
aws bedrock-agentcore-control delete-api-key-credential-provider \
  --name dev-weather-apigw-key --region us-east-1

# Delete the stack
sam delete --stack-name dev-weather-agent --region us-east-1 --no-prompts

# Delete secret
aws secretsmanager delete-secret --secret-id "dev/apigw-api-key" \
  --force-delete-without-recovery --region us-east-1
```

Replace `dev` with your environment name if different.

## Running Tests

```bash
# Unit tests
python3 -m pytest tests/unit/ -v

# Property-based tests
python3 -m pytest tests/unit/test_properties.py -v
```

## Key Implementation Notes

- **Single API key**: The only key is for AgentCore → API Gateway (managed by the credential provider). The Open-Meteo backend is key-less, so there's no downstream API secret. If you point the pattern at a keyed backend, see [Extending to Other APIs](#extending-to-other-apis) for injecting a downstream key via a stage variable.
- **SAM build without Docker (Makefile custom build)**: The Agent Lambda uses `BuildMethod: makefile` (see `src/Makefile`). Instead of Docker or a host pip install, the Makefile runs a two-step `pip install --platform manylinux2014_x86_64 --python-version 3.12 --only-binary=:all:` that downloads prebuilt Linux wheels for binary dependencies (`cryptography`, `cffi`). This makes `sam build` work on any host OS with no Docker and no local `python3.12`. (The two-step install is needed because `--only-binary=:all:` with `--platform` silently skips pure-Python packages, so a second `--no-deps` pass installs those explicitly.)
- **JWT validation**: Accepts both access and ID tokens. Audience verification is disabled (AgentCore Gateway handles it via `AllowedAudience`)
- **Credential provider**: Provisioned via CLI (`bedrock-agentcore-control`), not the SAM stack. The deploy script auto-detects CLI support and creates/updates it between deploys, with a fallback to manual instructions. AgentCore reached GA with CloudFormation support in September 2025 and `AWS::BedrockAgentCore::ApiKeyCredentialProvider` is now an available resource type, so folding it into the template is a possible future simplification.
- **Region**: Must be `us-east-1` (AgentCore availability)
- **Bedrock model ID — inference profile required**: Claude Sonnet 4.6 does not support direct on-demand invocation on Bedrock. You must use a cross-region inference profile ID. The default is `us.anthropic.claude-sonnet-4-6` (US profile). Using the bare `anthropic.claude-sonnet-4-6` ID will result in a `ValidationException`. If you need global routing, use `global.anthropic.claude-sonnet-4-6` instead.
- **SAM template**: The Lambda is an `AWS::Serverless::Function` — SAM generates its execution role (from the inline `Policies`) and log group, and `sam build`/`sam deploy` handle packaging and upload. The remaining resources (AgentCore Gateway and target, API Gateway, Cognito, the Gateway execution role) are plain CloudFormation resources included in the SAM template unchanged, since SAM offers no shorthand for them.

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
