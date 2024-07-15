import json
from aws_cdk import (
    Stack,
    aws_opensearchserverless as aoss,
    aws_iam as iam,
)
from constructs import Construct

class BedrockServiceRoleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,
                 stack_suffix,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #setup variables for use in constructs
        BEDROCK_KNOWLEDGEBASE_PARAMS = self.node.try_get_context('bedrock_knowledgebase_params')
        s3_bucket_name = f"{BEDROCK_KNOWLEDGEBASE_PARAMS['s3_bucket_name_prefix']}-{stack_suffix.lower()}"

        #Create an IAM Service Role for Bedrock Knowledge Base
        bedrock_kb_service_role = iam.Role(self, "BedrockKBServiceRole",
            role_name="BedrockKBServiceRole",
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
                "S3DataSourceAccess": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["s3:GetObject", "s3:ListBucket"],
                            resources=[f"arn:aws:s3:::{s3_bucket_name}", f"arn:aws:s3:::{s3_bucket_name}/*"],
                            conditions={
                                "StringEquals": {
                                    "aws:PrincipalAcccount":self.account
                                }
                            }
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

