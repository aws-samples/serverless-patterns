#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    # Duration,
    Stack,
    aws_iam as iam,
    aws_kendra as kendra,
    aws_lambda as lambda_,
    aws_s3 as s3,
    RemovalPolicy,
    Duration,
    CfnParameter,
    CfnOutput,
    triggers

)

from constructs import Construct

class BedrockKendraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define parameters
        model_id_param = CfnParameter(
            self, "ModelId",
            type="String",
            default="anthropic.claude-instant-v1",
            allowed_values=[
                "anthropic.claude-instant-v1",
                "anthropic.claude-3-sonnet-20240229-v1:0",
                "anthropic.claude-3-haiku-20240307-v1:0",
                "anthropic.claude-v2"
            ],
            description="Enter the Model Id of the Anthropic LLM"
        )

        confluence_url_param = CfnParameter(
            self, "ConfluenceUrl",
            type="String",
            description="Enter the Confluence instance URL"
        )

        confluence_version_param = CfnParameter(
            self, "ConfluenceVersion",
            type="String",
            default="CLOUD",
            allowed_values=["CLOUD", "SERVER"],
            description="Confluence version (CLOUD or SERVER)"
        )

        # Secret ARN parameter for Confluence credentials
        confluence_secret_arn_param = CfnParameter(
            self, "ConfluenceSecretArn",
            type="String",
            description="ARN of the secret containing Confluence credentials"
        )

        kendra_edition_param = CfnParameter(
            self, "KendraEdition",
            type="String",
            default="DEVELOPER_EDITION",
            allowed_values=[
                "DEVELOPER_EDITION",
                "ENTERPRISE_EDITION"
            ],
            description="Kendra edition (DEVELOPER_EDITION, ENTERPRISE_EDITION)"
        )

        # Use the parameter values in your stack
        model_id = model_id_param.value_as_string
        kendra_edition = kendra_edition_param.value_as_string

        # Create Kendra index role
        kendra_index_role = iam.Role(
            self, "KendraIndexRole",
            assumed_by=iam.ServicePrincipal("kendra.amazonaws.com"),
            role_name=f"{construct_id}-KendraIndexRole",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess")
            ]
        )

        # Create Kendra index
        kendra_index = kendra.CfnIndex(
            self, "KendraIndex",
            name=f"{construct_id}-KendraIndex",
            role_arn=kendra_index_role.role_arn,
            edition=kendra_edition
        )

        # Create Kendra data source role
        kendra_ds_role = iam.Role(
            self, "KendraDSRole",
            assumed_by=iam.ServicePrincipal("kendra.amazonaws.com"),
            role_name=f"{construct_id}-ConfluenceDSRole",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess")
            ],
            inline_policies={
                "KendraDataSourcePolicy": iam.PolicyDocument(
                    statements=[ 
                        iam.PolicyStatement(
                            actions=["kendra:BatchPutDocument", "kendra:BatchDeleteDocument"],
                            resources=[kendra_index.attr_arn]
                        )
                    ]
                ),
                "SecretsManagerPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["secretsmanager:GetSecretValue"],
                            resources=[confluence_secret_arn_param.value_as_string]
                        )
                    ]
                )
            }
        )

        # Create Kendra Confluence data source
        kendra_ds = kendra.CfnDataSource(
            self, "KendraDS",
            index_id=kendra_index.attr_id,
            name=f"{construct_id}-ConfluenceDS",
            type='CONFLUENCE',
            data_source_configuration=kendra.CfnDataSource.DataSourceConfigurationProperty(
                confluence_configuration=kendra.CfnDataSource.ConfluenceConfigurationProperty(
                    server_url=confluence_url_param.value_as_string,
                    secret_arn=confluence_secret_arn_param.value_as_string,
                    version=confluence_version_param.value_as_string,
                    # Optional configurations
                    vpc_configuration=None,  # Add if needed
                    inclusion_patterns=[],    # Add if needed
                    exclusion_patterns=[],    # Add if needed
                )
            ),
            role_arn=kendra_ds_role.role_arn
        )

        # Add dependency
        kendra_ds.node.add_dependency(kendra_index)

        # Create a role for the DataSourceSyncLambda
        data_source_sync_lambda_role = iam.Role(
            self, "DataSourceSyncLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess")],
                inline_policies={
                "KendraDataSourceSyncPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=[
                                "kendra:StartDataSourceSyncJob",
                                "kendra:StopDataSourceSyncJob"
                            ],
                            resources=[
                                kendra_index.attr_arn,
                                f"{kendra_index.attr_arn}/*"]
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
                "INDEX_ID": kendra_index.attr_id,
                "DS_ID": kendra_ds.attr_id
            }
        )

        # Trigger data source sync lambda
        triggers.Trigger(self, "data_source_sync_lambda_trigger",
            handler=data_source_sync_lambda,
            timeout=Duration.minutes(10),
            invocation_type=triggers.InvocationType.EVENT
        )

        # Create the IAM role
        invoke_bedrock_lambda_role = iam.Role(
            self, "InvokeBedRockLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess")
            ],
            inline_policies={
                "InvokeBedRockPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["bedrock:InvokeModel"],
                            resources=[f"arn:aws:bedrock:{self.region}::foundation-model/{model_id}"]
                        )
                    ]
                ),
                "KendraRetrievalPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["kendra:Retrieve"],
                            resources=[kendra_index.attr_arn]
                        )
                    ]
                )
            }
        )
        
        # Lambda function for invoking Bedrock
        invoke_bedrock_lambda = lambda_.Function(
            self, "InvokeBedrockLambda",
            runtime=lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_asset("src/invokeBedrockLambda"),
            handler="invokeBedrockLambda.lambda_handler",
            timeout=Duration.seconds(120),
            memory_size=3008,
            role = invoke_bedrock_lambda_role,
            tracing=lambda_.Tracing.ACTIVE,
            environment={
                "INDEX_ID": kendra_index.attr_id,
                "MODEL_ID": model_id
            }
        )

        # Output values
        CfnOutput(self, "KendraIndexRoleArn", value=kendra_index_role.role_arn, description="Kendra index role ARN")
        CfnOutput(self, "KendraIndexID", value=kendra_index.attr_id, description="Kendra index ID")
        CfnOutput(self, "KendraConfluenceDataSourceArn", value=kendra_ds.attr_arn, description="Kendra Confluence data source ARN")
        CfnOutput(self, "DataSourceSyncLambdaArn", value=data_source_sync_lambda.function_arn, description="Data source sync lambda function ARN")
        CfnOutput(self, "InvokeBedrockLambdaArn", value=invoke_bedrock_lambda.function_arn, description="Invoke bedrock lambda function ARN")

app = cdk.App()
BedrockKendraStack(app, "BedrockKendraStack")

app.synth()
