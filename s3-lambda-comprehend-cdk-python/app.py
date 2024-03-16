#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_s3 as s3,
    aws_lambda_event_sources as eventsources,
    aws_dynamodb as dynamodb,
    CfnOutput,
)
from constructs import Construct
from aws_cdk.aws_dynamodb import (
    Attribute,
    AttributeType,
    Billing,
    TableV2,
    TableEncryptionV2,
)

DIRNAME = os.path.dirname(__file__)


class S3LambdaComprehendServerless(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Replace the bucket name with a preferred unique name, since S3 bucket names are globally unique.
        self.user_input_bucket = s3.Bucket(
            self,
            "s3-upload-input-text",
            versioned=True,
            bucket_name="s3-upload-input-text",
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
        )
        dynamodb_table = dynamodb.TableV2(
            self,
            "SentimentAnalysis",
            partition_key=Attribute(
                name="InputFile", type=dynamodb.AttributeType.STRING
            ),
            table_class=dynamodb.TableClass.STANDARD,
            billing=Billing.on_demand(),
            encryption=TableEncryptionV2.dynamo_owned_key(),
            point_in_time_recovery=True,
        )

        # Iam role to invoke lambda
        lambda_cfn_role = iam.Role(
            self,
            "CfnRole",
            assumed_by=iam.ServicePrincipal("s3.amazonaws.com"),
        )
        lambda_cfn_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaExecute")
        )

        # lambda function for processing the incoming request from S3 bucket
        lambda_function = lambda_.Function(
            self,
            "DetectSentimentLambda",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="lambda_function.lambda_handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src")),
            timeout=Duration.minutes(1),
            memory_size=512,
            environment={
                "environment": "dev",
                "dynamodb_table": dynamodb_table.table_name,
            },
        )

        # lambda version
        version = lambda_function.current_version

        # lambda policy
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "comprehend:DetectSentiment",
                    "comprehend:BatchDetectSentiment",
                    "s3:GetObject",
                    "dynamodb:PutItem",
                ],
                resources=["*"],
            )
        )

        lambda_function.add_event_source(
            eventsources.S3EventSource(
                self.user_input_bucket, events=[s3.EventType.OBJECT_CREATED]
            )
        )

        # Outputs
        CfnOutput(
            self,
            "S3 Bucket",
            description="S3 Bucket",
            value=self.user_input_bucket.bucket_name,
        )


app = cdk.App()
filestack = S3LambdaComprehendServerless(app, "S3LambdaComprehendServerless")

app.synth()
