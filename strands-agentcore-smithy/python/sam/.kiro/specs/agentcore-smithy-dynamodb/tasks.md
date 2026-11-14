# Implementation Plan: AgentCore Smithy DynamoDB

## Overview

Build a serverless AI agent that exposes DynamoDB operations through AWS Bedrock AgentCore Gateway using a Smithy model target. Implementation proceeds bottom-up: shared modules first, then infrastructure, then agent code, then deployment/test scripts. Python 3.12 throughout.

## Tasks

- [x] 1. Create shared modules (`src/shared/`)
  - [x] 1.1 Create `src/shared/__init__.py` and `src/shared/models.py`
    - Define `UserContext`, `AgentRequest`, `AgentResponse` dataclasses
    - `AgentResponse` includes optional `error` field
    - _Requirements: 11.2, 11.3_

  - [x] 1.2 Create `src/shared/jwt_utils.py`
    - Implement JWT validation that accepts both `token_use: access` and `token_use: id`
    - Disable audience verification (`verify_aud: False`)
    - Extract username from `cognito:username` claim (not `username` or `sub`)
    - _Requirements: 4.4, 4.5, 4.6, 11.3_

  - [x] 1.3 Create `src/shared/error_utils.py` and `src/shared/logging_utils.py`
    - Standardized error response formatting
    - Structured logging with correlation IDs
    - _Requirements: 11.3_

  - [x] 1.4 Write property tests for JWT validation (Properties 4, 5)
    - **Property 4: JWT validation accepts both token_use values**
    - **Validates: Requirements 4.4**
    - **Property 5: Username extraction from cognito:username claim**
    - **Validates: Requirements 4.6**

  - [x] 1.5 Write unit tests for shared modules
    - Test `UserContext`, `AgentRequest`, `AgentResponse` serialization
    - Test JWT validation edge cases (missing claims, expired tokens)
    - Test error_utils and logging_utils
    - _Requirements: 4.4, 4.5, 4.6, 11.3_

- [x] 2. Create agent Lambda modules (`src/agent/`)
  - [x] 2.1 Create `src/agent/__init__.py` and `src/agent/strands_client.py`
    - Factory function for MCP client creation (gateway URL + token)
    - Factory function for Bedrock model configuration (Claude 3 Sonnet)
    - _Requirements: 5.3, 5.4, 11.1_

  - [x] 2.2 Create `src/agent/agent_processor.py`
    - Create MCP client, Strands Agent with Bedrock model
    - Manage MCP session lifecycle in `try/finally` block (NOT `with` context manager)
    - Return `AgentResponse` with success/error
    - _Requirements: 5.4, 5.5, 11.1_

  - [x] 2.3 Create `src/agent/handler.py`
    - Lambda entry point: extract JWT from event, create `UserContext`, delegate to `agent_processor`
    - Validate JWT, extract username, build `AgentRequest`
    - Handle missing/invalid JWT with 401 response
    - _Requirements: 5.1, 5.5, 5.6, 11.1_

  - [x] 2.4 Write property test for agent code target-agnosticism (Property 8)
    - **Property 8: Agent code is target-type agnostic**
    - Scan all files in `src/agent/` and `src/shared/` for DynamoDB-specific or Smithy-specific identifiers
    - **Validates: Requirements 11.1**

  - [x] 2.5 Write unit tests for agent modules
    - Test handler JWT extraction and error responses
    - Test agent_processor try/finally lifecycle
    - Test strands_client factory functions
    - _Requirements: 5.3, 5.4, 5.5_

- [x] 3. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. Create CloudFormation template (`infrastructure/cloudformation-template.yaml`)
  - [x] 4.1 Define DynamoDB ProductTable resource
    - Partition key: `category` (S), Sort key: `productId` (S)
    - Billing mode: `PAY_PER_REQUEST`
    - _Requirements: 6.1, 6.2_

  - [x] 4.2 Define Cognito UserPool and UserPoolClient resources
    - UserPool with `USER_PASSWORD_AUTH` explicit auth flow
    - UserPoolClient associated with the UserPool
    - _Requirements: 4.1, 4.2_

  - [x] 4.3 Define GatewayExecutionRole with all required permissions
    - Trust policy for `bedrock-agentcore.amazonaws.com`
    - All 4 AgentCore ARN patterns (`token-vault/default`, `apikeycredentialprovider/*`, `workload-identity-directory/default`, `workload-identity-directory/default/workload-identity/{gateway-name}-*`)
    - DynamoDB permissions: `dynamodb:GetItem`, `dynamodb:PutItem`, `dynamodb:Query` on ProductTable ARN
    - No `apigateway:GET` permissions
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6_

  - [x] 4.4 Define AgentCore Gateway and GatewayTarget with inline Smithy model
    - Gateway: `ProtocolType: MCP`, `AuthorizerType: CUSTOM_JWT`
    - `CustomJWTAuthorizer` (all caps JWT) with `DiscoveryUrl` ending `/.well-known/openid-configuration`
    - `AllowedAudience` (not `Audience`) set to Cognito Client ID
    - `RoleArn` (not `ExecutionRoleArn`) referencing GatewayExecutionRole
    - GatewayTarget: `CredentialProviderType: GATEWAY_IAM_ROLE`
    - Target config nested as `Mcp.SmithyModel.InlinePayload`
    - Smithy 2.0 JSON model with `aws.protocols#restJson1`, GetItem/PutItem/Query operations
    - Each operation: POST method, URI path, `smithy.api#documentation` traits on all shapes
    - Required members marked with `smithy.api#required` trait
    - No streaming operations or custom protocols
    - _Requirements: 1.1–1.9, 2.1–2.7_

  - [x] 4.5 Define AgentLambdaRole and AgentLambdaFunction
    - Lambda: Python 3.12, x86_64, timeout 120s, memory 1024MB
    - IAM: `bedrock:InvokeModel`, `bedrock:InvokeModelWithResponseStream`, `bedrock:Converse`, `bedrock:ConverseStream`
    - IAM: `bedrock-agentcore:InvokeGateway` on gateway resource
    - IAM: CloudWatch Logs permissions
    - _Requirements: 5.1, 5.2, 5.6, 5.7_

  - [x] 4.6 Define stack outputs
    - Export Gateway ID, Cognito User Pool ID, Cognito Client ID, Lambda function name
    - _Requirements: 7.6_

  - [x] 4.7 Write property tests for CloudFormation template (Properties 1, 2, 3, 6)
    - **Property 1: Smithy operation structure completeness**
    - **Validates: Requirements 1.5, 1.6**
    - **Property 2: Smithy documentation coverage**
    - **Validates: Requirements 1.7**
    - **Property 3: No streaming or custom protocols in Smithy model**
    - **Validates: Requirements 1.9**
    - **Property 6: No API Gateway resources in CloudFormation template**
    - **Validates: Requirements 7.4**

  - [x] 4.8 Write unit tests for CloudFormation template
    - Verify gateway ProtocolType, AuthorizerType, CustomJWTAuthorizer casing, DiscoveryUrl suffix
    - Verify AllowedAudience (not Audience), RoleArn (not ExecutionRoleArn)
    - Verify GatewayExecutionRole has all 4 ARN patterns and DynamoDB permissions, no apigateway:GET
    - Verify Lambda config: Python 3.12, x86_64, timeout ≥120s, memory ≥1024MB
    - Verify Cognito USER_PASSWORD_AUTH flow
    - Verify no API Gateway resources, no Secrets Manager secrets
    - _Requirements: 1.1–1.9, 2.1–2.7, 3.1–3.6, 7.1–7.6_

- [x] 5. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Create deployment script (`scripts/deploy.sh`)
  - [x] 6.1 Implement CloudFormation deployment logic
    - Validate template before deployment
    - Detect stack existence via `DOES_NOT_EXIST` pattern, create or update accordingly
    - Handle "No updates are to be performed" gracefully
    - _Requirements: 9.1, 9.2_

  - [x] 6.2 Implement Lambda packaging with two-step pip install
    - First step: `pip3 install --only-binary=:all: --platform manylinux2014_x86_64 --python-version 3.12`
    - Second step: `pip3 install --no-deps` for pure Python packages (requests, urllib3, charset-normalizer, idna, certifi, PyJWT, cryptography, cffi)
    - Do NOT remove `.dist-info` directories
    - S3 fallback if zip exceeds 50MB
    - Include strands-agents, mcp, requests, PyJWT[crypto] dependencies
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 9.3_

  - [x] 6.3 Implement DynamoDB seeding and Cognito user creation
    - Seed ProductTable with sample product records across multiple categories
    - Create test user in Cognito with predefined username/password
    - _Requirements: 6.3, 6.4, 9.4, 9.5_

  - [x] 6.4 Implement test script generation
    - Generate `scripts/test.sh` with baked-in gateway endpoint, Cognito pool ID, client ID, username, password
    - Set executable permissions on generated script
    - Accept optional CLI prompt argument with default prompt
    - Authenticate with Cognito before invoking Lambda
    - No nested JSON echo commands that break `${ID_TOKEN}` substitution
    - _Requirements: 9.6, 10.1, 10.2, 10.3, 10.4, 10.5_

  - [x] 6.5 Ensure deploy script uses `pip3` exclusively and excludes forbidden patterns
    - All pip commands use `pip3` (not `pip`)
    - No credential provider CLI commands, API key retrieval, or stack re-update steps
    - _Requirements: 9.7, 9.8_

  - [x] 6.6 Write property test for deploy script (Property 7)
    - **Property 7: Deploy script uses pip3 exclusively**
    - **Validates: Requirements 9.7**

  - [x] 6.7 Write unit tests for deploy and test scripts
    - Verify two-step pip3 install pattern, no .dist-info removal
    - Verify DOES_NOT_EXIST check, S3 fallback logic
    - Verify no credential provider commands
    - Verify test script: no nested JSON echo, default prompt, auth before invoke
    - _Requirements: 8.1–8.5, 9.1–9.8, 10.1–10.5_

- [x] 7. Create requirements.txt and test configuration
  - [x] 7.1 Create `requirements.txt` with runtime dependencies
    - strands-agents, mcp, requests, PyJWT[crypto]
    - _Requirements: 8.5_

  - [x] 7.2 Create `tests/conftest.py` with shared fixtures
    - Fixtures for loading CloudFormation template, Smithy model, deploy script content
    - Fixtures for sample JWT tokens and user contexts
    - _Requirements: All_

- [x] 8. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
- Agent code in `src/agent/` and `src/shared/` must remain target-type agnostic (no DynamoDB/Smithy references)
- The Smithy model is embedded inline in the CloudFormation template, not in a separate file
