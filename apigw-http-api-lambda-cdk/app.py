#!/usr/bin/env python3
import os
from constructs import Construct
from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    Duration,
    aws_lambda as lambda_
)
import aws_cdk.aws_apigatewayv2_alpha as _apigw
import aws_cdk.aws_apigatewayv2_integrations_alpha as _integrations


DIRNAME = os.path.dirname(__file__)

class ApigwHttpApiLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the Lambda function to receive the request
        # The source code is in './src' directory
        lambda_fn = lambda_.Function(
            self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src")),
            environment={
                "env_var1": "value 1",
                "env_var2": "value 2",
            }
        )

        # Create the HTTP API with CORS
        http_api = _apigw.HttpApi(
            self, "MyHttpApi",
            cors_preflight=_apigw.CorsPreflightOptions(
                allow_methods=[_apigw.CorsHttpMethod.GET],
                allow_origins=["*"],
                max_age=Duration.days(10),
            )
        )

        # Add a route to GET /
        http_api.add_routes(
            path="/",
            methods=[_apigw.HttpMethod.GET],
            integration=_integrations.HttpLambdaIntegration("LambdaProxyIntegration", handler=lambda_fn),
        )

        # Outputs
        CfnOutput(self, "API Endpoint", description="API Endpoint", value=http_api.api_endpoint)

app = App()
ApigwHttpApiLambdaStack(app, "ApigwHttpApiLambdaStack")
app.synth()
