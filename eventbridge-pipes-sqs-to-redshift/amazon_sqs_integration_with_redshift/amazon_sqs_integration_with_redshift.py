from aws_cdk import (
    ArnFormat,
    CfnOutput,
    Stack,
    aws_sqs as sqs,
    aws_redshift_alpha as redshift,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_pipes as pipes,
    aws_secretsmanager as sm,
    RemovalPolicy as RP,
)

import os
from constructs import Construct

class AmazonSqsIntegrationWithRedshiftStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC with subnets
        app_vpc = ec2.Vpc(
            self,
            "vpc",
            max_azs=1,
            enable_dns_support=True,
            enable_dns_hostnames=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="private_subnet",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                ),
                ec2.SubnetConfiguration(
                    name="public_subnet", subnet_type=ec2.SubnetType.PUBLIC
                ),
            ],
        )

        # Redshift Cluster
        cluster = redshift.Cluster(
            self,
            "Redshift",
            node_type=redshift.NodeType.DC2_LARGE,
            master_user=redshift.Login(master_username="awsuser"),
            cluster_type=redshift.ClusterType.SINGLE_NODE,
            subnet_group=redshift.ClusterSubnetGroup(
                self,
                "ClusterSubnetGroup",
                vpc_subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
                ),
                description="Cluster Private Subnets",
                vpc=app_vpc,
            ),
            vpc=app_vpc,
            default_database_name="private",
            cluster_name="pipestarget",
            removal_policy=RP.DESTROY,
        )

        # Redshift Table
        redshift.Table(
            self,
            "messages",
            table_columns=[
                redshift.Column(name="message", data_type="super"),
            ],
            cluster=cluster,
            database_name="private",
            table_name="messages",
        )

        # SQS Queues
        transformed_message_sqs_queue = sqs.CfnQueue(
            self,
            "SQSQueue",
            delay_seconds=0,
            receive_message_wait_time_seconds=0,
            visibility_timeout=30,
        )

        sqs_queue_source = sqs.CfnQueue(
            self,
            "SQSQueueSource",
            delay_seconds=0,
            receive_message_wait_time_seconds=0,
            visibility_timeout=30,
        )
        
        cluster_arn = Stack.of(self).format_arn(
            service="redshift",
            resource_name="pipestarget",
            resource="cluster",
            arn_format=ArnFormat.COLON_RESOURCE_NAME
        )
        cluster_db_arn = Stack.of(self).format_arn(
            service="redshift",
            resource_name="pipestarget/private",
            resource="dbname",
            arn_format=ArnFormat.COLON_RESOURCE_NAME
        )
        cluster_user_arn = Stack.of(self).format_arn(
            service="redshift",
            resource_name="pipestarget/awsuser",
            resource="dbuser",
            arn_format=ArnFormat.COLON_RESOURCE_NAME
        )
        
        policy = iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=[
                        "sqs:ReceiveMessage",
                        "sqs:DeleteMessage",
                        "sqs:GetQueueAttributes",
                    ],
                    effect=iam.Effect.ALLOW,
                    resources=[sqs_queue_source.attr_arn],
                ),
                iam.PolicyStatement(
                    actions=[
                        "sqs:ReceiveMessage",
                        "sqs:DeleteMessage",
                        "sqs:GetQueueAttributes",
                        "sqs:SendMessage",
                    ],
                    effect=iam.Effect.ALLOW,
                    resources=[transformed_message_sqs_queue.attr_arn],
                ),
                iam.PolicyStatement(
                    actions=["redshift-data:BatchExecuteStatement"],
                    effect=iam.Effect.ALLOW,
                    resources=[
                        cluster_arn
                    ],
                ),
                iam.PolicyStatement(
                    actions=["redshift:GetClusterCredentials"],
                    effect=iam.Effect.ALLOW,
                    resources=[
                        cluster_db_arn,
                        cluster_user_arn,
                    ],
                ),
                iam.PolicyStatement(
                    actions=[
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeVpcs",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                    ],
                    effect=iam.Effect.ALLOW,
                    resources=["*"],
                ),
            ]
        )
        # Pipe Role
        pipe_role = iam.Role(
            self,
            "PipeRole",
            assumed_by=iam.ServicePrincipal(service="pipes.amazonaws.com"),
            inline_policies={"pipe_policy": policy},
        )
        pipe_source_queue = pipes.CfnPipe.PipeSourceParametersProperty(
            sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                batch_size=1
            )
        )

        pipe_target = pipes.CfnPipe.PipeTargetParametersProperty(
            redshift_data_parameters=pipes.CfnPipe.PipeTargetRedshiftDataParametersProperty(
                database="private", sqls=["$.body"], db_user="awsuser"
            )
        )

        # Redshift Target Pipe
        cfn_pipe = pipes.CfnPipe(
            self,
            "CfnPipeRedshiftTarget",
            role_arn=pipe_role.role_arn,
            source=transformed_message_sqs_queue.attr_arn,
            target=cluster_arn,
            source_parameters=pipe_source_queue,
            target_parameters=pipe_target,
        )

        cfn_pipe.node.add_dependency(cluster)

        sqs_transformer_pipe_source_properties = (
            pipes.CfnPipe.PipeSourceParametersProperty(
                sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                    batch_size=1
                )
            )
        )

        sqs_transformer_pipe_target_properties = pipes.CfnPipe.PipeTargetParametersProperty(
            sqs_queue_parameters=pipes.CfnPipe.PipeTargetSqsQueueParametersProperty(),
            input_template='insert into messages(message) values(JSON_PARSE(\'{"body":"<$.body>"}\'));',
        )

        # SQS Source Pipe
        sqs_transformer_cfn_pipe = pipes.CfnPipe(
            self,
            "CfnPipeSQSSource",
            role_arn=pipe_role.role_arn,
            source=sqs_queue_source.attr_arn,
            target=transformed_message_sqs_queue.attr_arn,
            source_parameters=sqs_transformer_pipe_source_properties,
            target_parameters=sqs_transformer_pipe_target_properties,
        )

        CfnOutput(self, "Source SQS Queue URL: ", value=sqs_queue_source.attr_queue_url)
