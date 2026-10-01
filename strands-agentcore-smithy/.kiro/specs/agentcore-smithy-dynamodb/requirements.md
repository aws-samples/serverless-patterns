# Requirements Document

## Introduction

This feature builds a serverless AI agent that exposes DynamoDB operations (GetItem, PutItem, Query) through AWS Bedrock AgentCore Gateway using a Smithy model target type. Users interact with the agent via natural language, and the Strands SDK with Claude 3 Sonnet determines which DynamoDB operation to invoke. Authentication is handled via Cognito JWT tokens with a CUSTOM_JWT authorizer on the gateway. The gateway uses GATEWAY_IAM_ROLE credentials to access DynamoDB directly, eliminating the need for API keys or credential provider configuration. The entire stack deploys via a single bash script and targets the us-east-1 region.

## Glossary

- **Agent_Lambda**: The AWS Lambda function (Python 3.12, x86_64) running the Strands SDK agent that processes user requests via Bedrock Claude 3 Sonnet and communicates with AgentCore Gateway over MCP protocol
- **AgentCore_Gateway**: The AWS Bedrock AgentCore Gateway resource configured with MCP protocol, CUSTOM_JWT authorizer, and a Smithy model target pointing to DynamoDB
- **Smithy_Model**: A JSON-format Smithy 2.0 API model using the aws.protocols#restJson1 trait that defines the DynamoDB operations (GetItem, PutItem, Query) exposed through the gateway
- **Cognito_Pool**: The Amazon Cognito User Pool and User Pool Client used to authenticate users and issue JWT ID tokens for the CUSTOM_JWT authorizer
- **Gateway_Execution_Role**: The IAM role assumed by AgentCore Gateway that includes the four core AgentCore ARN patterns and DynamoDB access permissions
- **Product_Table**: The DynamoDB table storing product data with a partition key and optional sort key, used as the target data store
- **Deploy_Script**: The bash script (scripts/deploy.sh) that orchestrates CloudFormation deployment, Lambda packaging, DynamoDB seeding, Cognito user creation, and test script generation
- **Test_Script**: The generated bash script (scripts/test.sh) with baked-in environment values for invoking the agent with natural language prompts
- **MCP_Client**: The Model Context Protocol client within the agent that connects to AgentCore Gateway to discover and invoke tools
- **Lambda_Package**: The deployment artifact containing the agent source code and pip-installed dependencies, packaged as a zip file with a two-step pip install process

## Requirements

### Requirement 1: Smithy Model Definition for DynamoDB Operations

**User Story:** As a developer, I want a Smithy model that defines GetItem, PutItem, and Query operations for DynamoDB, so that AgentCore Gateway can translate MCP tool calls into DynamoDB API requests.

#### Acceptance Criteria

1. THE Smithy_Model SHALL define a service shape with the `aws.protocols#restJson1` trait and a version of "1.0.0"
2. THE Smithy_Model SHALL define a GetItem operation with an HTTP trait specifying a POST method and a URI path
3. THE Smithy_Model SHALL define a PutItem operation with an HTTP trait specifying a POST method and a URI path
4. THE Smithy_Model SHALL define a Query operation with an HTTP trait specifying a POST method and a URI path
5. THE Smithy_Model SHALL define input structures for each operation with required members marked using the `smithy.api#required` trait
6. THE Smithy_Model SHALL define output structures for each operation that capture the DynamoDB response shape
7. THE Smithy_Model SHALL include `smithy.api#documentation` traits on the service, each operation, and each input/output member to enable the LLM to select the correct tool
8. THE Smithy_Model SHALL be provided as an InlinePayload in the CloudFormation template and remain under 10MB in size
9. THE Smithy_Model SHALL NOT include streaming operations or custom protocols

### Requirement 2: AgentCore Gateway Configuration

**User Story:** As a developer, I want the AgentCore Gateway configured with MCP protocol, CUSTOM_JWT authentication, and a Smithy model target, so that the agent can securely invoke DynamoDB operations through the gateway.

#### Acceptance Criteria

1. THE AgentCore_Gateway SHALL use `ProtocolType: MCP` as the protocol configuration
2. THE AgentCore_Gateway SHALL use `AuthorizerType: CUSTOM_JWT` with a `CustomJWTAuthorizer` configuration block (all caps JWT)
3. WHEN configuring the CustomJWTAuthorizer, THE AgentCore_Gateway SHALL set the DiscoveryUrl to the Cognito User Pool OIDC endpoint ending with `/.well-known/openid-configuration`
4. WHEN configuring the CustomJWTAuthorizer, THE AgentCore_Gateway SHALL use `AllowedAudience` (not `Audience`) set to the Cognito User Pool Client ID
5. THE AgentCore_Gateway SHALL reference the Gateway_Execution_Role using the `RoleArn` property (not `ExecutionRoleArn`)
6. THE AgentCore_Gateway SHALL have a GatewayTarget resource with TargetConfiguration nested as `Mcp.SmithyModel.InlinePayload`
7. THE AgentCore_Gateway SHALL use `GATEWAY_IAM_ROLE` as the CredentialProviderType on the target (not `API_KEY`)

### Requirement 3: Gateway Execution Role with DynamoDB Permissions

**User Story:** As a developer, I want the gateway execution role to include all required AgentCore ARN patterns and DynamoDB permissions, so that tool invocations succeed without "Internal Error" responses.

#### Acceptance Criteria

1. THE Gateway_Execution_Role SHALL include a policy granting `bedrock-agentcore:*` access to the token-vault default ARN pattern (`arn:aws:bedrock-agentcore:{region}:{account}:token-vault/default`)
2. THE Gateway_Execution_Role SHALL include a policy granting access to the apikeycredentialprovider wildcard ARN pattern (`arn:aws:bedrock-agentcore:{region}:{account}:token-vault/default/apikeycredentialprovider/*`)
3. THE Gateway_Execution_Role SHALL include a policy granting access to the workload-identity-directory default ARN pattern (`arn:aws:bedrock-agentcore:{region}:{account}:workload-identity-directory/default`)
4. THE Gateway_Execution_Role SHALL include a policy granting access to the workload-identity-directory wildcard ARN pattern (`arn:aws:bedrock-agentcore:{region}:{account}:workload-identity-directory/default/workload-identity/{gateway-name}-*`)
5. THE Gateway_Execution_Role SHALL include a policy granting `dynamodb:GetItem`, `dynamodb:PutItem`, and `dynamodb:Query` actions on the Product_Table ARN
6. THE Gateway_Execution_Role SHALL NOT include `apigateway:GET` permissions

### Requirement 4: Cognito Authentication

**User Story:** As a developer, I want Cognito-based JWT authentication, so that only authenticated users can invoke the agent and access DynamoDB data through the gateway.

#### Acceptance Criteria

1. THE Cognito_Pool SHALL create a User Pool with `USER_PASSWORD_AUTH` as an explicit authentication flow
2. THE Cognito_Pool SHALL create a User Pool Client associated with the User Pool
3. WHEN a user authenticates, THE Cognito_Pool SHALL issue a JWT ID token that the CUSTOM_JWT authorizer validates
4. THE Agent_Lambda SHALL validate incoming JWT tokens by accepting both `token_use: access` and `token_use: id` claim values
5. THE Agent_Lambda SHALL disable audience verification (`verify_aud: False`) during JWT validation since the gateway handles audience validation via AllowedAudience
6. THE Agent_Lambda SHALL extract the username from the `cognito:username` claim (not the `username` claim) when processing ID tokens

### Requirement 5: Agent Lambda with Strands SDK

**User Story:** As a developer, I want a Lambda function running the Strands SDK with Claude 3 Sonnet that connects to AgentCore Gateway via MCP, so that users can interact with DynamoDB through natural language.

#### Acceptance Criteria

1. THE Agent_Lambda SHALL use Python 3.12 runtime with x86_64 architecture
2. THE Agent_Lambda SHALL have a minimum timeout of 120 seconds and minimum memory of 1024 MB
3. THE Agent_Lambda SHALL use the Strands SDK with Bedrock Claude 3 Sonnet as the LLM provider
4. THE Agent_Lambda SHALL connect to the AgentCore_Gateway using the MCP_Client to discover and invoke tools
5. THE Agent_Lambda SHALL NOT use a `with mcp_client:` context manager; the Agent manages the MCP session and cleanup occurs in a `finally` block
6. THE Agent_Lambda SHALL have IAM permissions for `bedrock:InvokeModel`, `bedrock:InvokeModelWithResponseStream`, `bedrock:Converse`, and `bedrock:ConverseStream`
7. THE Agent_Lambda SHALL have IAM permissions for `bedrock-agentcore:InvokeGateway` on the AgentCore_Gateway resource

### Requirement 6: DynamoDB Table and Sample Data

**User Story:** As a developer, I want a DynamoDB table with sample product data, so that the agent has data to query and demonstrate all three operations.

#### Acceptance Criteria

1. THE Product_Table SHALL be created as a DynamoDB table with a partition key and an optional sort key
2. THE Product_Table SHALL use PAY_PER_REQUEST billing mode
3. WHEN the Deploy_Script runs, THE Deploy_Script SHALL seed the Product_Table with sample product records covering multiple partition key values
4. THE Product_Table SHALL store items with attributes sufficient to demonstrate GetItem (single item retrieval), PutItem (item creation), and Query (partition key filtering) operations

### Requirement 7: CloudFormation Infrastructure

**User Story:** As a developer, I want all infrastructure defined in a single CloudFormation template, so that the entire stack can be deployed and torn down as a unit.

#### Acceptance Criteria

1. THE CloudFormation template SHALL define all resources in a single file at `infrastructure/cloudformation-template.yaml`
2. THE CloudFormation template SHALL deploy all resources in the us-east-1 region
3. THE CloudFormation template SHALL include the Product_Table, AgentCore_Gateway, GatewayTarget, Cognito_Pool, Agent_Lambda, and all IAM roles
4. THE CloudFormation template SHALL NOT include any API Gateway resources (RestApi, ApiKey, UsagePlan, stages, deployments, methods)
5. THE CloudFormation template SHALL NOT include Secrets Manager secrets for target authentication
6. THE CloudFormation template SHALL export the Gateway ID, Cognito User Pool ID, Cognito Client ID, and Lambda function name as stack outputs

### Requirement 8: Lambda Packaging with Two-Step pip Install

**User Story:** As a developer, I want Lambda dependencies packaged correctly using a two-step pip install, so that both binary and pure Python packages are included in the deployment artifact.

#### Acceptance Criteria

1. WHEN packaging the Lambda, THE Deploy_Script SHALL execute a first pip install step with `--only-binary=:all:` and `--platform manylinux2014_x86_64` and `--python-version 3.12` to install binary packages
2. WHEN packaging the Lambda, THE Deploy_Script SHALL execute a second pip install step with `--no-deps` to install pure Python packages that the first step silently skips (requests, urllib3, charset-normalizer, idna, certifi, PyJWT, cryptography, cffi)
3. THE Deploy_Script SHALL NOT remove `.dist-info` directories from the Lambda_Package (opentelemetry requires them)
4. IF the Lambda_Package zip file exceeds 50MB, THEN THE Deploy_Script SHALL upload the zip to S3 and update the Lambda function from the S3 location
5. THE Lambda_Package SHALL include all four dependencies: strands-agents, mcp, requests, and PyJWT with crypto extras

### Requirement 9: Deployment Script

**User Story:** As a developer, I want a single deploy script that handles the full deployment lifecycle, so that I can deploy the entire stack with one command.

#### Acceptance Criteria

1. THE Deploy_Script SHALL validate the CloudFormation template before deployment
2. THE Deploy_Script SHALL detect whether the CloudFormation stack exists and perform a create or update accordingly (checking for `DOES_NOT_EXIST` pattern)
3. THE Deploy_Script SHALL package and deploy the Lambda code after the CloudFormation stack is created
4. THE Deploy_Script SHALL seed the Product_Table with sample data after stack deployment
5. THE Deploy_Script SHALL create a test user in the Cognito_Pool with a predefined username and password
6. THE Deploy_Script SHALL generate the Test_Script at `scripts/test.sh` with baked-in values for gateway endpoint, Cognito pool ID, client ID, username, and password
7. THE Deploy_Script SHALL use `pip3` (not `pip`) for all package installation commands
8. THE Deploy_Script SHALL NOT include credential provider CLI commands, API key retrieval, or stack re-update steps

### Requirement 10: Test Script Generation

**User Story:** As a developer, I want a generated test script with baked-in configuration values, so that I can test the agent immediately after deployment without manual configuration.

#### Acceptance Criteria

1. WHEN the Deploy_Script completes, THE Deploy_Script SHALL generate `scripts/test.sh` with executable permissions
2. THE Test_Script SHALL accept an optional natural language prompt as a command-line argument and use a default prompt when none is provided
3. THE Test_Script SHALL authenticate with the Cognito_Pool to obtain a JWT ID token before invoking the agent
4. THE Test_Script SHALL invoke the Agent_Lambda with the JWT token and the user prompt
5. THE Test_Script SHALL NOT use nested JSON echo commands that break shell variable substitution for `${ID_TOKEN}`

### Requirement 11: Reusable Agent Code

**User Story:** As a developer, I want the agent code to be target-type agnostic, so that the same handler, agent processor, MCP client, and shared modules work regardless of whether the gateway target is API Gateway, Smithy, or another type.

#### Acceptance Criteria

1. THE Agent_Lambda handler, agent processor, MCP client factory, and shared modules SHALL NOT contain any DynamoDB-specific or Smithy-specific logic
2. THE Agent_Lambda source code SHALL be organized into `src/agent/` (handler.py, agent_processor.py, strands_client.py) and `src/shared/` (models.py, jwt_utils.py, error_utils.py, logging_utils.py)
3. THE Agent_Lambda shared modules SHALL include structured logging, error handling utilities, JWT validation, and data models for UserContext, AgentRequest, and AgentResponse
