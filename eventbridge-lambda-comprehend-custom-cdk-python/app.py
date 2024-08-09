#!/usr/bin/env python3
import os
import aws_cdk as cdk
import json
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_dynamodb as dynamodb,
    aws_events_targets as targets,
    aws_scheduler as scheduler,
    CfnOutput,
)
from aws_cdk.aws_dynamodb import (
    Attribute,
    AttributeType,
    Billing,
    TableV2,
    TableEncryptionV2,
)
from constructs import Construct

DIRNAME = os.path.dirname(__file__)


class EventBridgeLambdaComprehendCustomServerless(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamodb_table = dynamodb.TableV2(
            self,
            "ComprehendCustomModelTracking",
            partition_key=Attribute(
                name="CustomModelType", type=dynamodb.AttributeType.STRING
            ),
            sort_key=Attribute(name="CustomEndpointName", type=dynamodb.AttributeType.STRING),
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

        # Lambda function for processing the incoming request from EventBridge Scheduler
        lambda_function = lambda_.Function(
            self,
            "ComprehendCustomEndpoint",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src")),
            timeout=Duration.minutes(1),
            memory_size=512
        )

        # lambda policy
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["comprehend:CreateEndpoint", "comprehend:DeleteEndpoint", "comprehend:TagResource", "dynamodb:PutItem", "dynamodb:GetItem", "dynamodb:DeleteItem", "dynamodb:Query"],
                resources=["*"],
            )
        )

        ## Create schedule role
        scheduler_role = iam.Role(
            self,
            "scheduler-role",
            assumed_by=iam.ServicePrincipal("scheduler.amazonaws.com"),
        )

        scheduler_events_policy = iam.PolicyStatement(
            actions=["lambda:InvokeFunction"],
            resources=[lambda_function.function_arn],
            effect=iam.Effect.ALLOW,
        )

        scheduler_role.add_to_policy(scheduler_events_policy)
        schedule_group = scheduler.CfnScheduleGroup(
            self,
            "schedule-group",
            name="schedule-group",
        )

        # Create a schedule to invoke a lambda function from EventBridge scheduler, for endpoint creation
        create_schedule = scheduler.CfnSchedule(
            self,
            "CreateSchedule",
            flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                mode="OFF",
            ),
            schedule_expression="cron(30 11 ? * MON-FRI *)",
            group_name=schedule_group.name,
            target=scheduler.CfnSchedule.TargetProperty(
                arn=lambda_function.function_arn,
                role_arn=scheduler_role.role_arn,
                input=json.dumps(
                    {
                        'eventType': 'CreateEndpoint', #DO NOT MODIFY THIS FIELD
                        'modelType': 'CustomClassifier',
                        'customEndpoint': 'CustomClassifierEndpoint',
                        'customModelArn': 'arn:aws:comprehend:<region_name>:<aws account number>:<document-classifier or entity-recognizer>/<custom model name>/version/<version name>',
                        'dynamoDBTable': dynamodb_table.table_name
                    }
                ),
            ),
        )

        # Create a schedule to invoke a lambda function from EventBridge scheduler, for endpoint deletion
        delete_schedule = scheduler.CfnSchedule(
            self,
            "DeleteSchedule",
            flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                mode="OFF",
            ),
            schedule_expression="cron(50 11 ? * MON-FRI *)",
            group_name=schedule_group.name,
            target=scheduler.CfnSchedule.TargetProperty(
                arn=lambda_function.function_arn,
                role_arn=scheduler_role.role_arn,
                input=json.dumps(
                    {
                        'eventType': 'DeleteEndpoint',  #DO NOT MODIFY THIS FIELD
                        'modelType': 'CustomClassifier',
                        'customEndpoint': 'CustomClassifierEndpoint',
                        'dynamoDBTable': dynamodb_table.table_name
                    }
                ),
            ),
        )

        # Outputs
        CfnOutput(
            self,
            "DynamoDB",
            description="DynamoDB",
            value=dynamodb_table.table_name,
        )


app = cdk.App()
filestack = EventBridgeLambdaComprehendCustomServerless(app, "EventBridgeLambdaComprehendCustomServerless")
app.synth()
