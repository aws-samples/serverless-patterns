#!/usr/bin/env python3
import os
from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    Fn,
    Aws,
    RemovalPolicy,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_iam as iam
)
from constructs import Construct

DIRNAME = os.path.dirname(__file__)

class MyServerlessApplicationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Lambda function
        # Code in ./src directory
        lambda_fn = lambda_.Function(
            self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src"))
        )

        # Function version
        version = lambda_fn.current_version

        # Create function alias
        alias = lambda_.Alias(
            self, "LambdaAlias",
            alias_name="Prod",
            version=version
        )

        # Create the Rest API
        rest_api = apigateway.RestApi(
            self, "RestApi",
            endpoint_types=[apigateway.EndpointType.REGIONAL],
            deploy=False,
            retain_deployments=False
        )

        # Create initial deployment
        deployment = apigateway.Deployment(
            self,
            "Deployment",
            api=rest_api,
            retain_deployments=False
        )

        # Create prod Stage
        stage = apigateway.Stage(
            self,
            "prod",
            deployment=deployment,
            variables={
                "lambdaAlias": "Prod"
            }
        )

        rest_api.deployment_stage = stage

        # Create URI for lambda alias
        stage_uri = f"arn:aws:apigateway:{Aws.REGION}:lambda:path/2015-03-31/functions/{lambda_fn.function_arn}:${{stageVariables.lambdaAlias}}/invocations"

        # Create Lambda Integration
        integration = apigateway.Integration(
            type=apigateway.IntegrationType.AWS_PROXY,
            integration_http_method="POST",
            uri=stage_uri
        )

        # Create APIGW Method
        method = rest_api.root.add_method("GET", integration)

        # Add Lambda permissions
        lambda_fn.add_permission(
            "lambdaPermission",
            action="lambda:InvokeFunction",
            principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
            source_arn=method.method_arn.replace(
                rest_api.deployment_stage.stage_name, "*"
            )
        )

        # Add permissions for Prod alias
        alias.add_permission(
            "aliasPermission",
            action="lambda:InvokeFunction",
            principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
            source_arn=method.method_arn.replace(
                rest_api.deployment_stage.stage_name, "*"
            )
        )

        # OUTPUTS
        CfnOutput(self, "LambdaFunction", export_name="MyLambdaFunction", value=lambda_fn.function_arn)
        CfnOutput(self, "ApigwId", export_name="MyAPIGWID", value=rest_api.rest_api_id)
        CfnOutput(self, "MethodArn", export_name="MyMethodArn", value=method.method_arn)
        CfnOutput(self, "StageName", export_name="MyStageName", value=rest_api.deployment_stage.stage_name)


class CanaryDeploymentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Import Lambda ARN, REST API ID, and Method ARN from stack exports
        LAMBDA_ARN = Fn.import_value("MyLambdaFunction")
        API_ID = Fn.import_value("MyAPIGWID")
        METHOD_ARN = Fn.import_value("MyMethodArn")
        STAGE_NAME = Fn.import_value("MyStageName")

        # Import Lambda function from ARN
        lambda_fn = lambda_.Function.from_function_arn(self, 'lambda_fn', LAMBDA_ARN)

        # Create new function version
        version = lambda_.CfnVersion(
            self, "lambdaVersion",
            function_name=lambda_fn.function_name
        )

        # Save Versions when deleting stack for canary promotion and additional deployments
        version.apply_removal_policy(policy=RemovalPolicy.RETAIN)

        # Create Dev alias
        alias = lambda_.CfnAlias(
            self, "lambdaAlias",
            function_name=lambda_fn.function_name,
            function_version=version.attr_version,
            name="Dev"
        )

        # Add permissions for Dev alias
        permission = lambda_.CfnPermission(
            self, "aliasPermission",
            action="lambda:InvokeFunction",
            function_name=alias.ref,
            principal="apigateway.amazonaws.com",
            source_arn=METHOD_ARN.replace(
                STAGE_NAME, "*"
            )
        )

        # Create a canary deployment
        canary_deployment = apigateway.CfnDeployment(
            self, "CanaryDeployment",
            rest_api_id=API_ID,

            deployment_canary_settings=apigateway.CfnDeployment.DeploymentCanarySettingsProperty(
                percent_traffic=50,
                stage_variable_overrides={
                    "lambdaAlias": "Dev"
                }
            ),
            stage_name="prod"
        )

app = App()
MyServerlessApplicationStack(app, "MyServerlessApplicationStack")
CanaryDeploymentStack(app, "CanaryDeploymentStack")
app.synth()
