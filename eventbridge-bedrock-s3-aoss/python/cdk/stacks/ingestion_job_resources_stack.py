from aws_cdk import (
    CfnOutput,
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_scheduler as scheduler,
    aws_sqs as sqs,
    aws_logs as logs,
)
from constructs import Construct

class IngestionJobResourcesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str,
                 knowledge_base_id, 
                 data_source_id, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Create an IAM Service Role for Bedrock Knowledge Base
        eventbridge_scheduler_role = iam.Role(self, "EventBridgeSchedulerRole",
            role_name="EventBridgeSchedulerRole",
            inline_policies={
                "BedrockKBSyncPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["bedrock:StartIngestionJob"],
                            resources=["*"]
                        )
                    ]
                )
            },
            assumed_by=iam.ServicePrincipal("scheduler.amazonaws.com",
                conditions={
                    "StringEquals": {
                        "aws:SourceAccount": self.account
                    }
                }
            )
        )
        
        cfn_schedule_group = scheduler.CfnScheduleGroup(self, 
                                                        "BedrockKBSyncScheduleGroup",
                                                        name="BedrockKBSyncScheduleGroup")
        cfn_schedule = scheduler.CfnSchedule(self, "BedrockKBDataSourceSyncSchedule",
            name="BedrockKBDataSourceSyncSchedule",
            description="Schedule to Sync Bedrock Knowledge Base Data Source Periodically",
            group_name=cfn_schedule_group.name,
            flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                mode="OFF"
            ),
            schedule_expression="rate(5 minutes)",
            schedule_expression_timezone="UTC+01:00",
            target=scheduler.CfnSchedule.TargetProperty(
                arn="arn:aws:scheduler:::aws-sdk:bedrockagent:startIngestionJob",
                role_arn=eventbridge_scheduler_role.role_arn,
                input="{\"KnowledgeBaseId\":\""+knowledge_base_id+"\",\"DataSourceId\":\""+data_source_id+"\"}"
            )
        ) 
