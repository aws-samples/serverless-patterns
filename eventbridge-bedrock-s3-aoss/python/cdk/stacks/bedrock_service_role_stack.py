import json
from aws_cdk import (
    Stack,
    aws_opensearchserverless as aoss,
    aws_iam as iam,
)
from constructs import Construct

class BedrockServiceRoleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Create an IAM Service Role for Bedrock Knowledge Base
        bedrock_kb_service_role = iam.Role(self, "BedrockKBServiceRole",
            role_name="BedrockKBServiceRole",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"),
            ],
            inline_policies={
                "StartIngestionJob": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["bedrock:StartIngestionJob"],
                            resources=["*"]
                        )
                    ]
                ),
                "EmbeddingModelAccess": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["bedrock:InvokeModel"],
                            resources=[f"arn:aws:bedrock:{self.region}::foundation-model/*"]
                        )
                    ]
                ),
                "OpenSearchServerlessAccess": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["aoss:APIAccessAll"],
                            resources=[f"arn:aws:aoss:{self.region}:{self.account}:collection/*"]
                        )
                    ]
                )
            },
            assumed_by=iam.ServicePrincipal("bedrock.amazonaws.com",
                conditions={
                    "StringEquals": {
                        "aws:SourceAccount": self.account
                    },
                    "ArnLike": {
                        "aws:SourceArn": f"arn:aws:bedrock:{self.region}:{self.account}:knowledge-base/*"
                    }
                }
            )
        )
        self.bedrock_kb_service_role_arn = bedrock_kb_service_role.role_arn

