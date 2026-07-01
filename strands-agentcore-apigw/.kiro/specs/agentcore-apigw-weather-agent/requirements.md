# Requirements Document

## Introduction

This feature builds a serverless AI agent that uses AWS Bedrock AgentCore Gateway with an API Gateway target type to proxy weather API requests. The Agent Lambda uses the Strands Agents SDK with Bedrock Claude Sonnet 4.6 for natural language processing. AgentCore Gateway auto-discovers operations from the API Gateway REST API via GetExportAPI, and uses an API Key credential provider for outbound authentication. Cognito provides JWT-based user authentication. The API Gateway REST API proxies requests to WeatherAPI.com, injecting the downstream API key separately from the AgentCore-to-API-Gateway key.

Existing reusable code in `handoff/src/shared/` (models, error handling, logging, JWT utils) and `handoff/src/agent/` (handler, agent_processor, strands_client) is carried forward. The new work covers CloudFormation infrastructure, deployment scripts, and tests.

## Glossary

- **Agent_Lambda**: AWS Lambda function running the Strands Agents SDK with Bedrock Claude Sonnet 4.6 to process natural language weather queries
- **AgentCore_Gateway**: AWS Bedrock AgentCore Gateway configured with CUSTOM_JWT authorization and an API Gateway target
- **API_Gateway_REST_API**: AWS API Gateway REST API exposing weather endpoints that proxy to WeatherAPI.com
- **Credential_Provider**: AgentCore Identity credential provider (API_KEY type) that injects the x-api-key header into outbound requests from the Gateway to the API Gateway REST API
- **Cognito_User_Pool**: AWS Cognito User Pool providing JWT-based authentication for the AgentCore Gateway
- **AgentCore_API_Key**: API key managed by the Credential_Provider for authenticating AgentCore_Gateway requests to the API_Gateway_REST_API
- **WeatherAPI_Key**: API key for authenticating API_Gateway_REST_API requests to WeatherAPI.com
- **CloudFormation_Stack**: AWS CloudFormation stack defining all infrastructure resources for this feature
- **Deployment_Script**: Shell script automating the multi-step deployment process
- **Strands_SDK**: The strands-agents Python SDK used by the Agent_Lambda for agentic orchestration

## Requirements

### Requirement 1: API Gateway REST API with Weather Endpoints

**User Story:** As a developer, I want an API Gateway REST API that exposes weather endpoints proxying to WeatherAPI.com, so that AgentCore Gateway can auto-discover and invoke weather operations.

#### Acceptance Criteria

1. THE CloudFormation_Stack SHALL define an AWS::ApiGateway::RestApi resource with ApiKeySourceType set to HEADER
2. THE CloudFormation_Stack SHALL define API Gateway resources for the path `/weather/current`
3. THE CloudFormation_Stack SHALL define a GET method on the `/weather/current` resource with ApiKeyRequired set to true and AuthorizationType set to NONE
4. THE CloudFormation_Stack SHALL define an HTTP_PROXY integration on the GET method that proxies requests to `https://api.weatherapi.com/v1/current.json`
5. WHEN a request includes the query parameter `q`, THE API_Gateway_REST_API SHALL forward the `q` parameter to WeatherAPI.com
6. THE CloudFormation_Stack SHALL define the WeatherAPI_Key injection into downstream requests to WeatherAPI.com via a stage variable or mapping template
7. THE CloudFormation_Stack SHALL define an AWS::ApiGateway::Deployment resource with explicit DependsOn for every Method resource
8. THE CloudFormation_Stack SHALL define an AWS::ApiGateway::Stage resource referencing the Deployment

### Requirement 2: API Gateway API Key and Usage Plan

**User Story:** As a developer, I want API Gateway to validate API keys via a usage plan, so that only authorized callers (AgentCore Gateway) can invoke the weather endpoints.

#### Acceptance Criteria

1. THE CloudFormation_Stack SHALL define an AWS::ApiGateway::ApiKey resource that depends on the Stage resource
2. THE CloudFormation_Stack SHALL define an AWS::ApiGateway::UsagePlan resource referencing the Stage
3. THE CloudFormation_Stack SHALL define an AWS::ApiGateway::UsagePlanKey resource linking the ApiKey to the UsagePlan
4. WHEN a request to the API_Gateway_REST_API lacks a valid x-api-key header, THE API_Gateway_REST_API SHALL return a 403 Forbidden response

### Requirement 3: AgentCore Gateway with API Gateway Target

**User Story:** As a developer, I want an AgentCore Gateway configured with an API Gateway target, so that the Gateway auto-discovers weather operations and proxies tool calls through the API Gateway REST API.

#### Acceptance Criteria

1. THE CloudFormation_Stack SHALL define an AWS::BedrockAgentCore::Gateway resource with AuthorizerType set to CUSTOM_JWT
2. THE CloudFormation_Stack SHALL configure JwtConfiguration on the Gateway with Issuer, Audience, and JwksUri referencing the Cognito_User_Pool
3. THE CloudFormation_Stack SHALL define an AWS::BedrockAgentCore::GatewayTarget resource with TargetConfiguration using the ApiGateway block (not OpenApiSchema)
4. THE GatewayTarget SHALL reference the API_Gateway_REST_API by ApiId and Stage
5. THE GatewayTarget SHALL configure CredentialProviderConfigurations with CredentialProviderType set to API_KEY and a ProviderArn referencing the Credential_Provider
6. THE CloudFormation_Stack SHALL output the Gateway ID for use by the Agent_Lambda and Deployment_Script 

### Requirement 4: Cognito User Pool for Authentication

**User Story:** As a developer, I want a Cognito User Pool for JWT authentication, so that users can authenticate and the AgentCore Gateway can validate their tokens.

#### Acceptance Criteria

1. THE CloudFormation_Stack SHALL define an AWS::Cognito::UserPool resource
2. THE CloudFormation_Stack SHALL define an AWS::Cognito::UserPoolClient resource with ExplicitAuthFlows including ALLOW_USER_PASSWORD_AUTH and ALLOW_REFRESH_TOKEN_AUTH
3. THE CloudFormation_Stack SHALL output the User Pool ID, Client ID, and JWKS URL for use by the Agent_Lambda and Deployment_Script

### Requirement 5: Agent Lambda Function

**User Story:** As a developer, I want a Lambda function running the Strands SDK agent, so that users can send natural language weather queries and receive AI-processed responses.

#### Acceptance Criteria

1. THE CloudFormation_Stack SHALL define an AWS::Lambda::Function resource with Runtime set to python3.12 and Architecture set to x86_64
2. THE CloudFormation_Stack SHALL configure the Agent_Lambda with a minimum timeout of 120 seconds and a minimum memory of 1024 MB
3. THE CloudFormation_Stack SHALL set environment variables on the Agent_Lambda for GATEWAY_ID, COGNITO_JWKS_URL, BEDROCK_MODEL_ID, and AWS_REGION
4. THE Agent_Lambda SHALL reuse the existing handler, agent_processor, and strands_client code from `handoff/src/agent/`
5. THE Agent_Lambda SHALL reuse the existing shared utilities from `handoff/src/shared/`

### Requirement 6: IAM Roles and Permissions

**User Story:** As a developer, I want correctly scoped IAM roles, so that each component has the minimum permissions required to function.

#### Acceptance Criteria

1. THE CloudFormation_Stack SHALL define an IAM execution role for the Agent_Lambda with permissions for bedrock:InvokeModel, bedrock:InvokeModelWithResponseStream, bedrock:Converse, and bedrock:ConverseStream
2. THE CloudFormation_Stack SHALL grant the Agent_Lambda role permission to call bedrock-agentcore:GetGateway on the Gateway resource
3. THE CloudFormation_Stack SHALL define an IAM execution role for the AgentCore_Gateway with permissions for bedrock-agentcore:GetWorkloadAccessToken on the workload-identity-directory resources
4. THE CloudFormation_Stack SHALL grant the Gateway execution role bedrock-agentcore:GetResourceApiKey permission on all four required ARN patterns: token-vault/default, token-vault/default/apikeycredentialprovider/*, workload-identity-directory/default, and workload-identity-directory/default/workload-identity/{GatewayName}-*
5. THE CloudFormation_Stack SHALL grant the Gateway execution role secretsmanager:GetSecretValue permission on the bedrock-agentcore-identity secret path
6. THE CloudFormation_Stack SHALL grant the Gateway execution role apigateway:GET permission on the REST API exports resource for GetExportAPI access
7. THE CloudFormation_Stack SHALL grant the Agent_Lambda role permission to write logs to CloudWatch Logs

### Requirement 7: Deployment Script

**User Story:** As a developer, I want an automated deployment script, so that I can deploy the full stack in the correct order accounting for resources that cannot be created via CloudFormation.

#### Acceptance Criteria

1. THE Deployment_Script SHALL validate the CloudFormation template before deploying
2. THE Deployment_Script SHALL create Secrets Manager secrets for the WeatherAPI_Key and a placeholder AgentCore_API_Key before stack creation
3. THE Deployment_Script SHALL deploy the CloudFormation_Stack and wait for completion
4. THE Deployment_Script SHALL retrieve the actual API Gateway API key value from the stack after deployment
5. THE Deployment_Script SHALL update the Secrets Manager secret for the AgentCore_API_Key with the real API Gateway key value
6. THE Deployment_Script SHALL output instructions for manually creating the Credential_Provider via the AWS Console, since the Credential_Provider cannot be created via CloudFormation
7. THE Deployment_Script SHALL package the Agent_Lambda code with dependencies targeting python3.12 and x86_64 platform, preserving .dist-info directories
8. WHEN the packaged Lambda zip exceeds 50 MB, THE Deployment_Script SHALL upload the zip to S3 and update the Lambda function code from S3
9. THE Deployment_Script SHALL accept an environment name parameter to support multiple deployment environments

### Requirement 8: CloudFormation Template Structure

**User Story:** As a developer, I want a well-structured CloudFormation template, so that all resources are created with correct dependency ordering and parameterization.

#### Acceptance Criteria

1. THE CloudFormation_Stack SHALL accept parameters for EnvironmentName, WeatherApiKeySecretArn, and CredentialProviderArn
2. THE CloudFormation_Stack SHALL use the EnvironmentName parameter to namespace all resource names
3. THE CloudFormation_Stack SHALL define all resources in us-east-1 region due to BedrockAgentCore service availability
4. THE CloudFormation_Stack SHALL define Outputs for GatewayId, RestApiId, ApiKeyId, UserPoolId, UserPoolClientId, CognitoJwksUrl, AgentLambdaArn, and ApiEndpointUrl

### Requirement 9: Testing

**User Story:** As a developer, I want tests that verify the infrastructure configuration and agent integration, so that I can validate the deployment before and after going live.

#### Acceptance Criteria

1. THE test suite SHALL include unit tests that validate the CloudFormation template structure including resource types, dependency chains, and required properties
2. THE test suite SHALL include unit tests that verify the API Gateway deployment depends on all method resources
3. THE test suite SHALL include unit tests that verify the Gateway execution role includes all four required ARN patterns for GetResourceApiKey
4. THE test suite SHALL include an integration test script that authenticates via Cognito, obtains a JWT, sends a weather query to the Agent_Lambda, and validates the response contains weather data
5. THE test suite SHALL include a test that verifies the API Gateway returns 403 when called without an API key

