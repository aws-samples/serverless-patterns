from aws_cdk import Stack
from aws_cdk import aws_iam as iam
from aws_cdk import aws_ssm as ssm
from constructs import Construct
from cdk_nag import NagSuppressions

class KbRoleStack(Stack):
    def __init__(
        self,
        scope: Construct,
        stack_id: str,
        params: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope=scope, id=stack_id, **kwargs)

        account_id = Stack.of(self).account
        region = Stack.of(self).region
        partition = Stack.of(self).partition
        kb_role_name = params["kb_role_name"]
        kb_source_bucket = f"kb-data-source-{account_id}"
        kb_source_bucket_arn = f"arn:{partition}:s3:::{kb_source_bucket}"

        intermediate_bucket_name = f"{params['intermediate_bucket_name']}-{account_id}"
        intermediate_bucket_arn = f"arn:{partition}:s3:::{intermediate_bucket_name}"

        # Create KB Role with partition-aware ARNs
        kb_role = iam.Role(
            self,
            "KBRole",
            role_name=kb_role_name,
            assumed_by=iam.ServicePrincipal(
                "bedrock.amazonaws.com",
                conditions={
                    "StringEquals": {"aws:SourceAccount": account_id},
                    "ArnLike": {"aws:SourceArn": f"arn:{partition}:bedrock:{region}:{account_id}:knowledge-base/*"},
                },
            ),
            inline_policies={
                "FoundationModelPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            sid="BedrockInvokeModelStatement",
                            effect=iam.Effect.ALLOW,
                            actions=["bedrock:InvokeModel"],
                            resources=[f"arn:{partition}:bedrock:{region}::foundation-model/*"],
                        )
                    ]
                ),
                "OSSPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            sid="OpenSearchServerlessAPIAccessAllStatement",
                            effect=iam.Effect.ALLOW,
                            actions=["aoss:APIAccessAll"],
                            resources=[f"arn:{partition}:aoss:{region}:{account_id}:collection/*"],
                        )
                    ]
                ),
                "S3Policy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            sid="S3ListBucketStatement",
                            effect=iam.Effect.ALLOW,
                            actions=["s3:ListBucket"],
                            resources=[kb_source_bucket_arn, intermediate_bucket_arn],
                        ),
                        iam.PolicyStatement(
                            sid="S3GetObjectStatement",
                            effect=iam.Effect.ALLOW,
                            actions=["s3:GetObject"],
                            resources=[f"{kb_source_bucket_arn}/*", f"{intermediate_bucket_arn}/*"],
                        ),
                        iam.PolicyStatement(
                            sid="S3PutObjectStatement",
                            effect=iam.Effect.ALLOW,
                            actions=["s3:PutObject"],
                            resources=[f"{intermediate_bucket_arn}/*"],
                        ),
                        iam.PolicyStatement(
                            sid="S3DeleteObjectStatement",
                            effect=iam.Effect.ALLOW,
                            actions=["s3:DeleteObject"],
                            resources=[f"{intermediate_bucket_arn}/*"],
                        ),
                    ]
                ),
                "BDAPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            sid="BDAGetStatement",
                            effect=iam.Effect.ALLOW,
                            actions=["bedrock:GetDataAutomationStatus"],
                            resources=[f"arn:{partition}:bedrock:{region}:{account_id}:data-automation-invocation/*"],
                        ),
                        iam.PolicyStatement(
                            sid="BDAInvokeStatement",
                            effect=iam.Effect.ALLOW,
                            actions=["bedrock:InvokeDataAutomationAsync"],
                            resources=[
                                f"arn:{partition}:bedrock:{region}:aws:data-automation-project/public-rag-default",
                                f"arn:{partition}:bedrock:us-east-1:{account_id}:data-automation-profile/us.data-automation-v1",
                                f"arn:{partition}:bedrock:us-east-2:{account_id}:data-automation-profile/us.data-automation-v1",
                                f"arn:{partition}:bedrock:us-west-1:{account_id}:data-automation-profile/us.data-automation-v1",
                                f"arn:{partition}:bedrock:us-west-2:{account_id}:data-automation-profile/us.data-automation-v1",
                            ],
                        ),
                    ]
                ),
            },
        )

        
        # Add suppressions for necessary wildcards
        NagSuppressions.add_resource_suppressions(
            kb_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "CloudWatch Logs requires wildcard for log stream creation within specific log groups. Scoped to kb-* Lambda functions only."
                }
            ],
            apply_to_children=True,
        )
        # Create an SSM parameter which stores export values
        ssm.StringParameter(
            self,
            "KbRoleArn",
            parameter_name="/role-arn",
            string_value=kb_role.role_arn,
        )
