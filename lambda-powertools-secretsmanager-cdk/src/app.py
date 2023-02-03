#!/usr/bin/env python3
import os
from constructs import Construct
from aws_cdk import (
    App,
    CfnOutput,
    Environment,
    Stack,
    aws_secretsmanager as secretsmanager,
    SecretValue as secretvalue,
    aws_kms as kms,
    aws_lambda as lambda_,
    aws_apigateway as apigateway
)


class TestAPIStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create API Gateway
        api = apigateway.RestApi(self, "test-api")

        # Add a mock ANY method to the API
        api.root.add_method("ANY",
            apigateway.MockIntegration(
                integration_responses = [
                    apigateway.IntegrationResponse(
                        status_code = "200",
                        response_templates = {
                            "application/json": "{ \"response\": \"Successfully authenticated using API Key from Secrets Manager.\" }"
                        }
                    )
                ],
                passthrough_behavior = apigateway.PassthroughBehavior.NEVER,
                request_templates = {
                    "application/json": "{ \"statusCode\": 200 }"
                }
            ),
            method_responses = [
                apigateway.MethodResponse(status_code = "200")
            ],
            api_key_required = True
        )

        # Configure the API key/secret
        secret = secretsmanager.Secret(self, 'api_key')

        plan = api.add_usage_plan("usage-plan")
        key = api.add_api_key("ApiKey", value = secret.secret_value.unsafe_unwrap())
        plan.add_api_key(key)
        plan.add_api_stage(stage = api.deployment_stage)

        self.api_url = api.url
        self.secret_name = secret.secret_arn


class LambdaServiceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, secret_arn: str, api_url: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        region = Stack.of(self).region
        secret = secretsmanager.Secret.from_secret_complete_arn(self, "api-key", secret_arn)


        # Create lambda that will interface with secrets manager with powertools layer
        # Powertools documentation: https://awslabs.github.io/aws-lambda-powertools-python/
        layer = lambda_.LayerVersion.from_layer_version_arn(self, "power-tools-layer",
            layer_version_arn = "arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV2:17".format(region = region)
        )

        lambda_handler = lambda_.Function(self, 'lambda-handler',
            runtime = lambda_.Runtime.PYTHON_3_9,
            handler = 'handler.handler',
            code = lambda_.Code.from_asset('lambda'),
            layers = [ layer ],
            tracing = lambda_.Tracing.ACTIVE,
            environment = {
                "API_KEY_SECRET": secret_arn,
                "API_URL": api_url
            }
        )

        secret.grant_read(lambda_handler) # Assign permissions to read secret


        # Output the Lambda's function URL
        # Internet facing for testing purposes only, remove/change to private in production
        fn_url = lambda_handler.add_function_url(auth_type = lambda_.FunctionUrlAuthType.NONE)
        CfnOutput(self, "LambdaURL", value = fn_url.url)


app = App()

api_stack   = TestAPIStack(app, "TestAPIStack") # Test Target API
secret_name = api_stack.secret_name             # API Key secret
api_url     = api_stack.api_url                 # API URL

LambdaServiceStack(app, "LambdaServiceStack", secret_name, api_url)

app.synth()
