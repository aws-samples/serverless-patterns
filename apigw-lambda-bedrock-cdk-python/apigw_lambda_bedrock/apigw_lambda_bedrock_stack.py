from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    Duration,
    aws_apigateway as apigw
)
from constructs import Construct

class ApigwLambdaBedrockStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #lambda layer containing boto
        layer = _lambda.LayerVersion(self, "Boto3Layer",
            code=_lambda.Code.from_asset("./boto_layer.zip"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_10]
        )

        #add policy to invoke bedrock model
        invoke_model_policy = iam.Policy(self, "InvokeModelPolicy",
            statements=[
                iam.PolicyStatement(
                    actions=["bedrock:InvokeModel"],
                    resources=[f"arn:aws:bedrock:{self.region}::foundation-model/anthropic.claude-v2"]
                )
            ]
        )

        # Create the Lambda function and attach the layer
        lambda_function = _lambda.Function(self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="index.handler",
            code=_lambda.Code.from_asset("./function_code"),
            layers=[layer],
            timeout=Duration.seconds(30)
            )

        invoke_model_policy.attach_to_role(lambda_function.role)

        #create api gateway
        api = apigw.RestApi(self, "ServerlessLandGenAI",)

        #create a new resource
        text_gen_resource = api.root.add_resource("text_gen")
        text_gen_resource.add_method("POST", apigw.LambdaIntegration(lambda_function))
