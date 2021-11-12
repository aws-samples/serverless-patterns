#!/usr/bin/env python3
import os

from aws_cdk import (
    core as cdk,
    aws_apigatewayv2 as apigatewayv2,
    aws_apigatewayv2_integrations as integrations,
    aws_lambda as lambda_,
)

DIRNAME = os.path.dirname(__file__)

class ApigwHttpApiLambdaStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
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
        http_api = apigatewayv2.HttpApi(
            self, "MyHttpApi",
            cors_preflight=apigatewayv2.CorsPreflightOptions(
                allow_methods=[apigatewayv2.CorsHttpMethod.GET],
                allow_origins=["*"],
                max_age=cdk.Duration.days(10),
            )
        )

        # Add a route to GET /
        http_api.add_routes(
            path="/",
            methods=[apigatewayv2.HttpMethod.GET],
            integration=integrations.LambdaProxyIntegration(handler=lambda_fn),
        )

        # Outputs
        cdk.CfnOutput(self, "API Endpoint", description="API Endpoint", value=http_api.api_endpoint)

app = cdk.App()
ApigwHttpApiLambdaStack(app, "ApigwHttpApiLambdaStack")
app.synth()
