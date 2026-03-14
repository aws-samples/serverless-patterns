#!/usr/bin/env python3
from aws_cdk import (
    App, CfnOutput,
    Duration,
    Stack,
    RemovalPolicy,
    aws_apigateway as apigw,
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
)
from constructs import Construct

class CarStoreStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        car_table = dynamodb.Table(
            self,
            "CarTable",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )

        car_function = _lambda.Function(
            self,
            "CarStoreFunction",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.handler",
            code=_lambda.Code.from_asset("CarHandler/"),
            timeout=Duration.seconds(10),
            snap_start=_lambda.SnapStartConf.ON_PUBLISHED_VERSIONS,
            memory_size=256,
            environment={
                "CAR_TABLE_NAME": car_table.table_name,
                "LOG_LEVEL": "INFO",
            }
        )
        car_table.grant_read_write_data(car_function)

        live_alias = _lambda.Alias(
            self,
            "CarStoreLiveAlias",
            alias_name="live",
            version=car_function.current_version,
        )

        car_api = apigw.RestApi(
            self,
            "CarStoreApi",
            deploy_options=apigw.StageOptions(stage_name="prod"),
        )

        integration = apigw.LambdaIntegration(live_alias, proxy=True)
        car_api.root.add_method("ANY", integration)
        car_api.root.add_resource("{proxy+}").add_method("ANY", integration)

        CfnOutput(
            self,
            "CarEndpoint",
            description="API Gateway Car Endpoint",
            value=car_api.url,
        )
        CfnOutput(self, "CarTableName", value=car_table.table_name)

app = App()
CarStoreStack(app, "CarStoreStack")
app.synth()
