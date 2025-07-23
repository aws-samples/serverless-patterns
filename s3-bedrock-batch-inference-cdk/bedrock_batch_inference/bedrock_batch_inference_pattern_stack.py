#!/usr/bin/env python3
import time

from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    CfnOutput, CfnParameter,
)
from aws_cdk.aws_iam import PolicyStatement
from constructs import Construct


class BedrockBatchInferencePatternStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Accept the model id as a parameter
        model_id = CfnParameter(self, "ModelARN",
                                type="String",
                                description="ARN of the the Claude model that you want to use for batch inference. ",
                                )

        # Create an S3 bucket with default encryption
        bucket = s3.Bucket(
            self,
            "BatchInfBucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            versioned=True,
            event_bridge_enabled=True,  # Enable EventBridge notifications
        )

        # Create IAM role for Bedrock
        bedrock_role = iam.Role(
            self,
            "BedrockBatchInferenceRole",
            assumed_by=iam.ServicePrincipal("bedrock.amazonaws.com")
        )

        # Add S3 permissions to the role
        bedrock_role.add_to_policy(iam.PolicyStatement(
            actions=["s3:GetObject", "s3:PutObject", "s3:ListBucket"],
            resources=[
                f"{bucket.bucket_arn}",
                f"{bucket.bucket_arn}/*",
            ]
        ))

        statement = PolicyStatement(
            actions=["bedrock:CreateModelInvocationJob", "iam:PassRole"],
            resources=[f"arn:aws:bedrock:{Stack.of(self).region}:{Stack.of(self).account}:model-invocation-job/*",
                       model_id.value_as_string,
                       bedrock_role.role_arn],
            effect=iam.Effect.ALLOW
        )

        # Create EventBridge rule to trigger Bedrock model invocation when input.jsonl file is
        # uploaded to S3 under /input prefix
        # Note: The AwsApi target creates an AWS-managed Lambda function that makes the actual API call
        events.Rule(
            self,
            "S3ToBedrockBatchInferenceRule",
            event_pattern=events.EventPattern(
                source=["aws.s3"],
                detail_type=["Object Created"],
                detail={
                    "bucket": {
                        "name": [bucket.bucket_name]
                    },
                    "object": {
                        "key": ["input/input.jsonl"]
                    }
                }
            ),

            targets=[targets.AwsApi(
                service="bedrock",
                action="createModelInvocationJob",
                parameters={
                    "modelId": model_id.value_as_string,
                    "jobName": f"batch-inference-job-{int(time.time())}",
                    "inputDataConfig": {
                        "s3InputDataConfig": {
                            "s3Uri": f"s3://{bucket.bucket_name}/input/input.jsonl"
                        }
                    },
                    "outputDataConfig": {
                        "s3OutputDataConfig": {
                            "s3Uri": f"s3://{bucket.bucket_name}/output/"
                        }
                    },
                    "roleArn": bedrock_role.role_arn
                },
                policy_statement=statement
            )]
        )

        # Output the bucket name
        CfnOutput(
            self,
            "BatchInferenceBucketName",
            value=bucket.bucket_name,
            description="S3 bucket to store the batch inference input and output"
        )
