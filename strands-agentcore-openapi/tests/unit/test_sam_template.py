"""Unit tests for the AWS SAM template (template.yaml)."""

import yaml
import pytest
from pathlib import Path


def cloudformation_constructor(loader, tag_suffix, node):
    """Handle CloudFormation/SAM intrinsic functions like !Ref, !GetAtt, !Sub."""
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    elif isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    elif isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    return None


yaml.add_multi_constructor('!', cloudformation_constructor, Loader=yaml.SafeLoader)


@pytest.fixture
def sam_template():
    """Load the SAM template from the project root."""
    template_path = Path(__file__).parent.parent.parent / 'template.yaml'
    with open(template_path, 'r') as f:
        return yaml.safe_load(f)


class TestSamTemplate:
    """Test SAM template structure and content."""

    def test_template_has_required_sections(self, sam_template):
        assert sam_template['AWSTemplateFormatVersion'] == '2010-09-09'
        assert sam_template['Transform'] == 'AWS::Serverless-2016-10-31'
        assert 'Parameters' in sam_template
        assert 'Resources' in sam_template
        assert 'Outputs' in sam_template

    def test_parameters_defined(self, sam_template):
        params = sam_template['Parameters']
        assert 'EnvironmentName' in params
        assert 'WeatherApiKeySecretArn' in params
        assert 'CredentialProviderArn' in params
        assert 'BedrockModelId' in params

    def test_default_model_id(self, sam_template):
        default_model = sam_template['Parameters']['BedrockModelId']['Default']
        assert default_model == 'us.anthropic.claude-sonnet-4-5-20250929-v1:0'

    def test_agent_function_is_serverless(self, sam_template):
        resources = sam_template['Resources']
        assert 'AgentFunction' in resources
        assert resources['AgentFunction']['Type'] == 'AWS::Serverless::Function'

    def test_agent_function_configuration(self, sam_template):
        props = sam_template['Resources']['AgentFunction']['Properties']

        assert props['Runtime'] == 'python3.12'
        assert props['Handler'] == 'agent.handler.lambda_handler'
        assert props['CodeUri'] == 'src/'
        assert props['MemorySize'] == 1024
        assert props['Timeout'] == 120

        env_vars = props['Environment']['Variables']
        assert 'COGNITO_JWKS_URL' in env_vars
        assert 'GATEWAY_ID' in env_vars
        assert 'BEDROCK_MODEL_ID' in env_vars

    def test_log_group_retention(self, sam_template):
        resources = sam_template['Resources']
        assert 'AgentFunctionLogGroup' in resources
        assert resources['AgentFunctionLogGroup']['Properties']['RetentionInDays'] == 30

    def test_cognito_configuration(self, sam_template):
        resources = sam_template['Resources']
        assert resources['CognitoUserPool']['Type'] == 'AWS::Cognito::UserPool'

        client = resources['CognitoUserPoolClient']
        assert client['Type'] == 'AWS::Cognito::UserPoolClient'
        assert 'ALLOW_USER_PASSWORD_AUTH' in client['Properties']['ExplicitAuthFlows']

    def test_gateway_configuration(self, sam_template):
        gateway = sam_template['Resources']['AgentCoreGateway']
        assert gateway['Type'] == 'AWS::BedrockAgentCore::Gateway'
        assert gateway['Properties']['AuthorizerType'] == 'CUSTOM_JWT'
        assert gateway['Properties']['ProtocolType'] == 'MCP'

    def test_gateway_target_is_openapi(self, sam_template):
        resources = sam_template['Resources']
        assert 'WeatherAPITarget' in resources

        target = resources['WeatherAPITarget']
        assert target['Type'] == 'AWS::BedrockAgentCore::GatewayTarget'
        # Only created once the credential provider ARN is supplied
        assert target['Condition'] == 'HasCredentialProvider'

        target_config = target['Properties']['TargetConfiguration']['Mcp']
        assert 'OpenApiSchema' in target_config
        inline_schema = target_config['OpenApiSchema']['InlinePayload']
        assert 'getCurrentWeather' in inline_schema
        assert 'api.weatherapi.com' in inline_schema

    def test_gateway_target_uses_api_key_credential(self, sam_template):
        target = sam_template['Resources']['WeatherAPITarget']
        cred_configs = target['Properties']['CredentialProviderConfigurations']
        assert cred_configs[0]['CredentialProviderType'] == 'API_KEY'

    def test_stack_outputs(self, sam_template):
        outputs = sam_template['Outputs']
        assert 'GatewayId' in outputs
        assert 'CognitoUserPoolId' in outputs
        assert 'CognitoClientId' in outputs
        assert 'AgentLambdaArn' in outputs
