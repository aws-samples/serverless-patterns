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
import aws_cdk.aws_apigatewayv2_alpha as _apigw
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration
from constructs import Construct

DIRNAME = os.path.dirname(__file__)


class ApigwLambdaTranslateServerless(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # IAM role to invoke lambda
        lambda_cfn_role = iam.Role(
            self,
            "CfnRole",
            assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com"),
        )
        lambda_cfn_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaExecute")
        )

        # Lambda function for processing the incoming request from API Gateway. Source and Target language are passed as environment variables to the Lambda function.
        lambda_function = lambda_.Function(
            self,
            "TranslateTextLambda",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="lambda_function.lambda_handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src")),
            timeout=Duration.minutes(1),
            memory_size=256,
            environment={
                "environment": "dev",
                "src_lang": "auto",
                "target_lang": "fr"
            },
        )

        # lambda policy
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "translate:TranslateText",
                    "comprehend:DetectDominantLanguage"
                ],
                resources=["*"],
            )
        )

        # api gateway with http
        http_api = _apigw.HttpApi(self, "TranslateTextApi")

        # added routes with POST method and integrated with the lambda function
        http_api.add_routes(
            path="/TranslateText",
            methods=[_apigw.HttpMethod.ANY],
            integration=HttpLambdaIntegration("TranslateTextIntegration", lambda_function)
        )

        # Outputs
        CfnOutput(self, "API Endpoint", description="API Endpoint", value=http_api.api_endpoint)


app = cdk.App()
filestack = ApigwLambdaTranslateServerless(app, "ApigwLambdaTranslateServerless")

app.synth()
