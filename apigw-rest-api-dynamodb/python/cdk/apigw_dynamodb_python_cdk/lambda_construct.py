from constructs import Construct
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_iam as iam

class LambdaConstruct(Construct):
    def __init__(self, scope: Construct, id: str ,**kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create lambda execution role 
        lambda_execution_role = iam.Role(
            self,
            "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ], 
            inline_policies={
                "LambdaPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            effect=iam.Effect.ALLOW,
                            actions=["apigateway:GET"],
                            resources=["*"]
                        )
                    ]
                )
            }
        )

        # Create lambda function.
        self.lambda_function = lambda_.Function(self, "LambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_14,
            handler="lambda_function.lambda_handler",
            role=lambda_execution_role,
            code=lambda_.Code.from_asset("src/lambda.zip")
        )

        