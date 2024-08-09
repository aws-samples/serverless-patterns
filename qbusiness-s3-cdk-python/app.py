#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    Stack,
    aws_qbusiness as qbusiness,
    aws_iam as iam,
    CfnParameter,
    CfnOutput,
    triggers,
    aws_lambda as lambda_,
    Duration
)
from constructs import Construct

class QBusinessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Parameters
        s3_bucket_name = CfnParameter(self, "S3DSBucketName", type="String", description="Enter the S3 bucket name where the contents you want to be indexed are stored.")
        identity_center_arn = CfnParameter(self, "IdentityCenterInstanceArn", type="String", description="Enter the ARN of the Amazon Q Business Identity Center instance.")

        # Q Business Application
        qbusiness_app = qbusiness.CfnApplication(
            self, "QBusinessApplication",
            display_name=f"MyQBusinessApp-{self.stack_name}",
            description="Amazon Q Business Application",
            identity_center_instance_arn=identity_center_arn.value_as_string
        )

        # Web Experience Role
        web_exp_role = iam.Role(
            self, "QBusinessWebExperienceRole",
            assumed_by=iam.ServicePrincipal("application.qbusiness.amazonaws.com"),
            role_name=f"QBusinessWebExperienceRole-{self.stack_name}",
            description="IAM role for Q Business Web Experience",
            inline_policies={"WebExperiencePolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            sid="QBusinessConversationPermission",
                            actions=[
                                "qbusiness:Chat",
                                "qbusiness:ChatSync",
                                "qbusiness:ListMessages",
                                "qbusiness:ListConversations",
                                "qbusiness:DeleteConversation",
                                "qbusiness:PutFeedback",
                                "qbusiness:GetWebExperience",
                                "qbusiness:GetApplication",
                                "qbusiness:ListPlugins",
                                "qbusiness:GetChatControlsConfiguration"
                            ],
                            resources=[qbusiness_app.attr_application_arn]
                        ),
                        iam.PolicyStatement(
                            sid="QBusinessKMSDecryptPermissions",
                            actions=["kms:Decrypt"],
                            resources=[f"arn:{self.partition}:kms:{self.region}:{self.account}:key/*"],
                            conditions={
                                "StringLike": {
                                    "kms:ViaService": f"qbusiness.{self.region}.amazonaws.com"
                                }
                            }
                        ),
                        iam.PolicyStatement(
                            sid="QBusinessSetContextPermissions",
                            actions=["sts:SetContext"],
                            resources=["arn:aws:sts::*:self"],
                            conditions={
                                "StringLike": {
                                    "aws:CalledViaLast": "qbusiness.amazonaws.com"
                                }
                            }
                        )
                    ]
                )
            }
        )

        # Adding set context action to web experience role
        web_exp_role.assume_role_policy.add_statements(iam.PolicyStatement(
            sid="QBusinessSetContextPermissions",
            actions=["sts:SetContext"],
            principals=[iam.ServicePrincipal("application.qbusiness.amazonaws.com")]
        ))

        # Web Experience
        qbusiness.CfnWebExperience(
            self, "QBusinessWebExperience",
            application_id=qbusiness_app.ref,
            role_arn=web_exp_role.role_arn
        )

        # Index
        qbusiness_index = qbusiness.CfnIndex(
            self, "QBusinessIndex",
            display_name="MyQBusinessIndex",
            description="My Amazon Q Business Index",
            application_id=qbusiness_app.ref
        )

        # Retriever
        qbusiness.CfnRetriever(
            self, "QBusinessRetriever",
            application_id=qbusiness_app.ref,
            configuration=qbusiness.CfnRetriever.RetrieverConfigurationProperty(
            native_index_configuration=qbusiness.CfnRetriever.NativeIndexConfigurationProperty(
            index_id=qbusiness_index.attr_index_id)
            ),  
            display_name="MyQBusinessRetriever",
            type="NATIVE_INDEX"
        )

        # S3 Data Source Role
        s3_data_source_role = iam.Role(
            self, "S3DataSourceRole",
            assumed_by=iam.ServicePrincipal("qbusiness.amazonaws.com"),
            inline_policies={"S3DataSourcePolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["s3:GetObject"],
                            resources=[f"arn:aws:s3:::{s3_bucket_name.value_as_string}/*"],
                            conditions={
                                "StringEquals": {
                                    "aws:ResourceAccount": [self.account]
                                }
                            }
                        ),
                        iam.PolicyStatement(
                            actions=["s3:ListBucket"],
                            resources=[f"arn:aws:s3:::{s3_bucket_name.value_as_string}"],
                            conditions={
                                "StringEquals": {
                                    "aws:ResourceAccount": [self.account]
                                }
                            }
                        ),
                        iam.PolicyStatement(
                            actions=[
                                "qbusiness:BatchPutDocument",
                                "qbusiness:BatchDeleteDocument"
                            ],
                            resources=[f"arn:aws:qbusiness:{self.region}:{self.account}:application/{qbusiness_app.ref}/index/*"]
                        ),
                        iam.PolicyStatement(
                            actions=[
                                "qbusiness:PutGroup",
                                "qbusiness:CreateUser",
                                "qbusiness:DeleteGroup",
                                "qbusiness:UpdateUser",
                                "qbusiness:ListGroups"
                            ],
                            resources=[
                                f"arn:aws:qbusiness:{self.region}:{self.account}:application/{qbusiness_app.ref}",
                                f"arn:aws:qbusiness:{self.region}:{self.account}:application/{qbusiness_app.ref}/index/*"]
                            )
                        ]
                    )
                }
            )

        # S3 Data Source
        s3_data_source = qbusiness.CfnDataSource(
            self, "S3DataSource",
            application_id=qbusiness_app.ref,
            display_name="MyS3DataSource",
            description="S3 Data Source for Amazon Q Business",
            role_arn=s3_data_source_role.role_arn,
            configuration={
                "connectionConfiguration": {
                    "repositoryEndpointMetadata": {
                        "BucketName": s3_bucket_name.value_as_string
                    }
                },
                "repositoryConfigurations": {
                    "document": {
                        "fieldMappings": [
                            {
                                "indexFieldName": "s3_document_id",
                                "indexFieldType": "STRING",
                                "dataSourceFieldName": "s3_document_id"
                            }
                        ]
                    }
                },
                "syncMode": "FULL_CRAWL",
                "type": "S3",
                "version": "1.0.0"
            },
            index_id=qbusiness_index.attr_index_id,
        )

        s3_data_source.node.add_dependency(qbusiness_index)

        # Create a role for the DataSourceSyncLambda
        data_source_sync_lambda_role = iam.Role(
            self, "DataSourceSyncLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess")],
                inline_policies={
                "QBusinessDataSourceSyncPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=[
                                "qbusiness:StartDataSourceSyncJob",
                                "qbusiness:StopDataSourceSyncJob"
                            ],
                            resources=[
                                qbusiness_app.attr_application_arn,
                                f"{qbusiness_app.attr_application_arn}/*"]
                            )
                        ]
                    )
                }
            )

        # Lambda function for initiating data source sync
        data_source_sync_lambda = lambda_.Function(
            self, "DataSourceSyncLambda",
            runtime=lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_asset("src/dataSourceSync"),
            handler="dataSourceSyncLambda.lambda_handler",
            timeout=Duration.minutes(15),
            memory_size=1024,
            role = data_source_sync_lambda_role,
            environment={
                "INDEX_ID": qbusiness_index.attr_index_id,
                "DS_ID": s3_data_source.attr_data_source_id,
                "APP_ID": qbusiness_app.ref
            }
        )

        # Trigger data source sync lambda
        triggers.Trigger(self, "data_source_sync_lambda_trigger",
            handler=data_source_sync_lambda,
            timeout=Duration.minutes(10),
            invocation_type=triggers.InvocationType.EVENT
        )

        # Define the outputs
        qbusiness_app_id_output = CfnOutput(
            self, "QBusinessApplicationId",
            value=qbusiness_app.ref,
            description="Amazon Q Business Application ID"
        )

        s3_data_source_id_output = CfnOutput(
            self, "S3DataSourceId",
            value=s3_data_source.ref,
            description="S3 Data Source ID"
        )

app = cdk.App()
QBusinessStack(app, "QBusinessStack")

app.synth()