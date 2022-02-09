from importlib.resources import Package
from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_s3 as s3,
    aws_lambda_event_sources as eventsources
)
from constructs import Construct
import os

class LambdaLayerXRayStackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Change pillow arn to latest version in your region. See https://github.com/keithrozario/Klayers/tree/master/deployments/python3.8/arns
        layerpillow = lambda_.LayerVersion.from_layer_version_arn(self, 'pillowlayerversion', 'Your_Region_Pillow_ARN')

         # --------------------------------------------------------
        # Create buckets for thumbnail 
        # --------------------------------------------------------

        bucket = s3.Bucket(self, 
                            id='SourceBucket',
                            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                            bucket_name='<your-name>-thumbnail-upload-372'
                        ) 

        ResizedBucket = s3.Bucket(self, 
                            id='ResizedBucket',
                            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                            bucket_name='<your-name>-thumbnail-upload-372-resized'
                        )

        # -------------------------------------------------------------------------------------
        # Create IAM role for lambda invocation, write to X-Ray and Get and Put objects into s3
        # -------------------------------------------------------------------------------------
        Role=iam.Role(self, "Lambda-role",
                        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
                        managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"),
                        iam.ManagedPolicy.from_aws_managed_policy_name("AWSXrayWriteOnlyAccess")]
                    )

        Role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources= [ bucket.bucket_arn + "/*"],
            actions= ["s3:GetObject"]
        ))

        Role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources= [ ResizedBucket.bucket_arn + "/*"],
            actions= ["s3:PutObject"]
        ))

        # ------------------------------------------
        # Create a lambda layer for botos3 and X-Ray
        # ------------------------------------------
        layerxray = lambda_.LayerVersion(self, 'xray_layer',
                code=lambda_.Code.from_asset(os.path.join(os.getcwd(), "lambda_layer_x_ray_stack/layers/xray")),
                description="Lambda Layer containing Xray SDK Python Library",
                compatible_runtimes=[
                    lambda_.Runtime.PYTHON_3_7,
                    lambda_.Runtime.PYTHON_3_8,
                ],
                removal_policy=RemovalPolicy.DESTROY,
                )

        # -------------------------------------------
        # Create Lambda Function
        # -------------------------------------------
        xray_trace_lambda = lambda_.Function(
                self,
                id = 'xray-sample-app',
                function_name='xray-handler',
                code=lambda_.Code.from_asset(os.path.join(os.getcwd(), "lambda_code")),
                runtime= lambda_.Runtime.PYTHON_3_8,
                handler="lambda-handler.lambda_handler",
                layers=[layerxray, layerpillow],
                role=Role,
                tracing=lambda_.Tracing.ACTIVE
        )
        
        xray_trace_lambda.add_event_source(eventsources.S3EventSource(bucket,
            events=[s3.EventType.OBJECT_CREATED_PUT],
        ))