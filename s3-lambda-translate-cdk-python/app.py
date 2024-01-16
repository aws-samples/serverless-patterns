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
    CfnOutput,
)
from constructs import Construct

DIRNAME = os.path.dirname(__file__)


class S3LambdaTranslateServerless(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Replace the input bucket name with a preferred unique name, since S3 bucket names are globally unique.
        self.user_input_bucket = s3.Bucket(
            self,
            "s3-translate-input-bucket",
            versioned=True,
            bucket_name="s3-translate-input-bucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
        )

        # Replace the output bucket name with a preferred unique name, since S3 bucket names are globally unique.
        self.user_output_bucket = s3.Bucket(
            self,
            "s3-translate-output-bucket",
            versioned=True,
            bucket_name="s3-translate-output-bucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
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

        # lambda layer containing boto3, Pillow for image processing, and Pyshortener for shortening the pre-signed
        # s3 url.
        layer = lambda_.LayerVersion(
            self,
            "Boto3Layer",
            code=lambda_.Code.from_asset("./python.zip"),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_10],
        )

        # Lambda function for processing the incoming request triggered as part of S3 upload. Source and Target language are passed as environment variables to the Lambda function.
        lambda_function = lambda_.Function(
            self,
            "TranslateTextLambda",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="lambda_function.lambda_handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src")),
            timeout=Duration.minutes(1),
            layers=[layer],
            memory_size=256,
            environment={
                "environment": "dev",
                "src_lang": "auto",
                "target_lang": "fr",
                "destination_bucket": self.user_output_bucket.bucket_name,
            },
        )

        # lambda policy
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "translate:TranslateText",
                    "translate:TranslateDocument",
                    "comprehend:DetectDominantLanguage",
                    "s3:PutObject",
                    "s3:GetObject",
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
            "S3 Output Bucket",
            description="S3 Translated Output Bucket",
            value=self.user_output_bucket.bucket_name,
        )
        CfnOutput(
            self,
            "S3 Input Bucket",
            description="S3 Input Bucket",
            value=self.user_input_bucket.bucket_name,
        )


app = cdk.App()
filestack = S3LambdaTranslateServerless(app, "S3LambdaTranslateServerless")

app.synth()
