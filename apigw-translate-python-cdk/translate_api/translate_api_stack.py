from aws_cdk import (
    Stack,
    CfnOutput,
    aws_iam as iam,
    aws_apigateway as apigateway,
)
from constructs import Construct

class TranslateApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create IAM Role for API Gateway
        api_gateway_role = iam.Role(
            self, 'ApiGatewayIAMRole',
            assumed_by=iam.ServicePrincipal('apigateway.amazonaws.com'),
        )

        # Add policy to the role
        api_gateway_role.add_to_policy(
            iam.PolicyStatement(
                actions=['translate:TranslateText'],
                resources=['*']
            )
        )

        # Create API Gateway
        api = apigateway.RestApi(
            self, 'TranslateApi',
            rest_api_name='TranslateAPI',
            description='API Gateway with direct integration to Amazon Translate\'s TranslateText API.',
            deploy_options=apigateway.StageOptions(stage_name='Prod')
        )

        # Create /translate resource
        translate_resource = api.root.add_resource('translate')

        # Add POST method with AWS integration
        translate_resource.add_method(
            'POST',
            apigateway.AwsIntegration(
                service='translate',
                action='TranslateText',
                integration_http_method='POST',
                options=apigateway.IntegrationOptions(
                    credentials_role=api_gateway_role,
                    request_templates={
                        'application/json': '''{
                            "Text": $input.json('$.text'),
                            "SourceLanguageCode": $input.json('$.sourceLanguageCode'),
                            "TargetLanguageCode": $input.json('$.targetLanguageCode')
                        }'''
                    },
                    passthrough_behavior=apigateway.PassthroughBehavior.NEVER,
                    request_parameters={
                        'integration.request.header.Content-Type': "'application/x-amz-json-1.1'",
                        'integration.request.header.X-Amz-Target': "'AWSShineFrontendService_20170701.TranslateText'"
                    },
                    integration_responses=[
                        apigateway.IntegrationResponse(
                            status_code='200',
                        )
                    ]
                )
            ),
            method_responses=[
                apigateway.MethodResponse(
                    status_code='200',
                    response_models={
                        'application/json': apigateway.Model.EMPTY_MODEL
                    }
                )
            ]
        )

        # Output the API endpoint URL
        CfnOutput(
            self, 'ApiEndpoint',
            value=f'{api.url}translate',
            description='API Gateway Endpoint URL'
        )
