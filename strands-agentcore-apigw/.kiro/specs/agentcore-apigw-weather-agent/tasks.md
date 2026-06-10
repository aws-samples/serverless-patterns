# Implementation Tasks

## Task 1: CloudFormation Template — API Gateway Resources
- [x] 1.1 Create `infrastructure/cloudformation-template.yaml` with Parameters (EnvironmentName, WeatherApiKeySecretArn, CredentialProviderArn)
- [x] 1.2 Define RestApi resource with `ApiKeySourceType: HEADER`
- [x] 1.3 Define WeatherResource (`/weather`) and WeatherCurrentResource (`/weather/current`) path resources
- [x] 1.4 Define GetCurrentWeatherMethod (GET, `ApiKeyRequired: true`, `AuthorizationType: NONE`) with HTTP_PROXY integration to `https://api.weatherapi.com/v1/current.json`, mapping `q` query param and injecting WeatherAPI key via `stageVariables.weatherApiKey`
- [x] 1.5 Define ApiDeployment with `DependsOn: GetCurrentWeatherMethod`
- [x] 1.6 Define ApiStage with stage variable for WeatherAPI key
- [x] 1.7 Define ApiKey (DependsOn ApiStage), UsagePlan (DependsOn ApiStage), and UsagePlanKey


**Requirements: 1, 2, 8**

## Task 2: CloudFormation Template — AgentCore, Cognito, Lambda, IAM
- [x] 2.1 Define CognitoUserPool and CognitoUserPoolClient with ALLOW_USER_PASSWORD_AUTH and ALLOW_REFRESH_TOKEN_AUTH
- [x] 2.2 Define AgentCoreGateway with `AuthorizerType: CUSTOM_JWT` and JwtConfiguration referencing Cognito
- [x] 2.3 Define WeatherAPITarget with `ApiGateway` block (not OpenApiSchema), referencing RestApi and ApiStage, with API_KEY credential provider config
- [x] 2.4 Define AgentLambdaFunction (python3.12, x86_64, 120s timeout, 1024MB memory) with environment variables (GATEWAY_ID, COGNITO_JWKS_URL, BEDROCK_MODEL_ID, AWS_REGION)
- [x] 2.5 Define AgentLambdaRole with Bedrock permissions (InvokeModel, InvokeModelWithResponseStream, Converse, ConverseStream), bedrock-agentcore:GetGateway, and CloudWatch Logs permissions
- [x] 2.6 Define GatewayExecutionRole with GetWorkloadAccessToken (2 ARN patterns), GetResourceApiKey (all 4 ARN patterns), secretsmanager:GetSecretValue on bedrock-agentcore-identity path, and apigateway:GET on REST API exports
- [x] 2.7 Define all Outputs: GatewayId, RestApiId, ApiKeyId, UserPoolId, UserPoolClientId, CognitoJwksUrl, AgentLambdaArn, ApiEndpointUrl

**Requirements: 3, 4, 5, 6, 8**

## Task 3: Copy Existing Agent Code
- [x] 3.1 Copy `handoff/src/agent/` to `src/agent/` (handler.py, agent_processor.py, strands_client.py)
- [x] 3.2 Copy `handoff/src/shared/` to `src/shared/` (models.py, logging_utils.py, error_utils.py, jwt_utils.py)
- [x] 3.3 Create `requirements.txt` with `strands-agents>=1.0.0` and `mcp>=1.0.0`

**Requirements: 5**

## Task 4: Deployment Script
- [x] 4.1 Create `scripts/deploy.sh` accepting `--environment-name`, `--weather-api-key`, `--region` (default us-east-1), `--s3-bucket` parameters
- [x] 4.2 Implement template validation step
- [x] 4.3 Implement Secrets Manager secret creation/update for WeatherAPI key and placeholder APIGW key
- [x] 4.4 Implement CloudFormation stack deploy with wait
- [x] 4.5 Implement API Gateway key retrieval and Secrets Manager update with real value
- [x] 4.6 Implement credential provider manual setup instructions output
- [x] 4.7 Implement Lambda packaging (pip install --platform manylinux2014_x86_64 --python-version 3.12, preserve .dist-info, remove .egg-info only)
- [x] 4.8 Implement Lambda deploy with S3 fallback for packages >50MB

**Requirements: 7**

## Task 5: Unit Tests — CloudFormation Template Validation
- [x] 5.1 Create `tests/unit/test_cloudformation_template.py` with pytest tests validating all API Gateway resources, dependencies, and properties
- [x] 5.2 Add tests for AgentCore Gateway, GatewayTarget (ApiGateway block, not OpenApiSchema), and Cognito resources
- [x] 5.3 Add tests for Lambda config (python3.12, x86_64, timeout >= 120, memory >= 1024, env vars)
- [x] 5.4 Add tests for IAM roles — Lambda role has all 4 Bedrock actions + GetGateway + CloudWatch Logs; Gateway role has all 4 GetResourceApiKey ARN patterns + GetWorkloadAccessToken + secretsmanager + apigateway:GET
- [x] 5.5 Add tests for template parameters and all 8 outputs

**Requirements: 9.1, 9.2, 9.3**

## Task 6: Property-Based Tests
- [ ]* 6.1 Create `tests/unit/test_properties.py` — Property 1: Deployment DependsOn includes all method logical IDs (hypothesis, 100 iterations)
- [ ]* 6.2 Property 2: Lambda role includes all 4 required Bedrock actions (hypothesis, 100 iterations)
- [ ]* 6.3 Property 3: Gateway role includes all 4 GetResourceApiKey ARN patterns (hypothesis, 100 iterations)
- [ ]* 6.4 Property 4: All named resources use EnvironmentName for namespacing (hypothesis, 100 iterations)
- [ ]* 6.5 Property 5: All 8 required outputs are defined (hypothesis, 100 iterations)

**Requirements: 9.1, 9.2, 9.3 | Design Properties: 1-5**

## Task 7: Integration Tests
- [x]* 7.1 Create `tests/integration/test_e2e.py` — API Gateway 403 test (call without API key, verify 403)
- [x]* 7.2 End-to-end agent test (Cognito auth → JWT → Agent Lambda → weather response validation)

**Requirements: 9.4, 9.5**

## Task 8: Validation Checkpoint
- [x] 8.1 Run unit tests and property-based tests: `pytest tests/unit/ -v`
- [x] 8.2 Validate CloudFormation template: `aws cloudformation validate-template --template-body file://infrastructure/cloudformation-template.yaml`
