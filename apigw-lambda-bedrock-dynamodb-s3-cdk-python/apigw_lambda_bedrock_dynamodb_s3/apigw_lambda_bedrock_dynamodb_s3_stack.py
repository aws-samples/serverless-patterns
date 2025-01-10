from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    Duration,
    aws_apigateway as apigw,
    aws_s3 as s3,
    RemovalPolicy,
    CfnOutput,
    aws_dynamodb as dynamodb
)
from constructs import Construct

class ApigwLambdaBedrockDynamodbS3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create DynamoDB table for job tracking
        job_table = dynamodb.Table(
            self, "JobTrackingTable",
            partition_key=dynamodb.Attribute(
                name="job_id",
                type=dynamodb.AttributeType.STRING
            ),
            time_to_live_attribute="ttl",
            removal_policy=RemovalPolicy.DESTROY
        )

        # Bedrock policy
        invoke_model_policy = iam.Policy(
            self, "InvokeModelPolicy",
            statements=[
                iam.PolicyStatement(
                    actions=[
                        "bedrock:InvokeModel",
                        "bedrock:StartAsyncInvoke",
                        "bedrock:ListAsyncInvokes",
                        "bedrock:GetAsyncInvoke"
                    ],
                    resources=[
                        f"arn:aws:bedrock:{self.region}::foundation-model/amazon.nova-reel-v1:0",
                        f"arn:aws:bedrock:{self.region}:{self.account}:async-invoke/*",
                        f"arn:aws:bedrock:{self.region}:{self.account}:foundation-model/amazon.nova-reel-v1:0"
                    ]
                )
            ]
        )

        # Create S3 bucket
        video_bucket = s3.Bucket(
            self,
            "ReelVideoBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # Define Lambda layers
        boto_layer = _lambda.LayerVersion.from_layer_version_arn(
            self, "Boto3Layer",
            f"arn:aws:lambda:{self.region}:770693421928:layer:Klayers-p311-boto3:19"
        )

        # Create the processing Lambda function FIRST
        process_function = _lambda.Function(
            self, "ProcessReelGeneration",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="process.handler",
            code=_lambda.Code.from_asset("./function_code"),
            layers=[boto_layer],
            timeout=Duration.minutes(15),
            environment={
                "BUCKET": video_bucket.bucket_name,
                "MODEL_ID": "amazon.nova-reel-v1:0",
                "TABLE_NAME": job_table.table_name
            }
        )

        # Then create the submit function with process function name
        submit_function = _lambda.Function(
            self, "SubmitReelGeneration",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="submit.handler",
            code=_lambda.Code.from_asset("./function_code"),
            layers=[boto_layer],
            timeout=Duration.seconds(29),
            environment={
                "BUCKET": video_bucket.bucket_name,
                "MODEL_ID": "amazon.nova-reel-v1:0",
                "TABLE_NAME": job_table.table_name,
                "PROCESS_FUNCTION_NAME": process_function.function_name
            }
        )

        # Grant permissions
        video_bucket.grant_read_write(process_function)
        video_bucket.grant_write(submit_function)
        job_table.grant_read_write_data(submit_function)
        job_table.grant_read_write_data(process_function)
        invoke_model_policy.attach_to_role(process_function.role)
        
        # Grant permission for submit function to invoke process function
        process_function.grant_invoke(submit_function)

        # Create API Gateway
        api = apigw.RestApi(
            self, "ReelGenAPI",
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=['*'],
                allow_methods=['POST', 'GET'],
                allow_headers=['Content-Type']
            )
        )

        # Add resources and methods
        reel_gen = api.root.add_resource("reel_gen")
        reel_gen.add_method("POST", apigw.LambdaIntegration(submit_function))
        
        # Add status check endpoint
        status = api.root.add_resource("status")
        status.add_resource("{jobId}").add_method(
            "GET", 
            apigw.LambdaIntegration(submit_function)
        )

        # Outputs
        CfnOutput(self, "S3-Video-Bucket", value=video_bucket.bucket_name)
        CfnOutput(self, "ApiGatewayUrl", value=api.url)
