#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as lambda_,
    CfnOutput
)
from constructs import Construct

import aws_cdk.aws_apigatewayv2_alpha as _apigw
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration

DIRNAME = os.path.dirname(__file__)


class ApigwLambdaComprehendServerless(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Iam role for bot to invoke lambda
        lambda_cfn_role = iam.Role(
            self,
            "CfnRole",
            assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com"),
        )
        lambda_cfn_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaExecute")
        )

        # lambda function for processing the incoming request from Lex Chatbot
        lambda_function = lambda_.Function(
            self,
            "DetectSentimentLambda",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="lambda_function.lambda_handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src")),
            timeout=Duration.minutes(10),
            memory_size=2048,
            environment={"environment": "dev"},
        )

        # lambda version
        version = lambda_function.current_version

        # lambda alias
        alias = lambda_.Alias(
            self, "Alias",
            alias_name="Prod",
            version=version
        )

        # lambda policy
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "comprehend:DetectSentiment"
                ],
                resources=["*"],
            )
        )

        # api gateway with http
        http_api = _apigw.HttpApi(self, "DetectSentimentApi")

        # added routs with POST method and integrated with the lambda function
        http_api.add_routes(
            path="/DetectSentiment",
            methods=[_apigw.HttpMethod.ANY],
            integration=HttpLambdaIntegration("DetectSentimentIntegration", lambda_function)
        )

        # Outputs
        CfnOutput(self, "API Endpoint", description="API Endpoint", value=http_api.api_endpoint)


app = cdk.App()
filestack = ApigwLambdaComprehendServerless(app, "ApigwLambdaComprehendServerless")

app.synth()
