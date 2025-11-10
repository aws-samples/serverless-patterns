import json

# from aws_cdk import aws_sqs as sqs
from aws_cdk import (
    Duration,
    Stack,
)
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_logs as logs
from aws_cdk import aws_ssm as ssm
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks
from constructs import Construct
from cdk_nag import NagSuppressions

LAMBDA_RUNTIME = _lambda.Runtime.PYTHON_3_13
STACK_RESOURCE_PREFIX = "KbSyncPipeline"


def gen_logical_id(suffix: str) -> str:
    return f"{STACK_RESOURCE_PREFIX}{suffix}"


class KbSyncPipelineStack(Stack):
    def __init__(
        self,
        scope: Construct,
        stack_id: str,
        params: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope=scope, id=stack_id, **kwargs)

        self.aws_partition = Stack.of(self).partition
        self.aws_region = Stack.of(self).region
        self.account_id = Stack.of(self).account
        self.embedding_model_id = params["embedding_model_id"]

        self.common_lambda_layer_arn = ssm.StringParameter.from_string_parameter_attributes(
            self, "CommonLambdaLayerVersion", parameter_name="/common-lambda-layer-arn"
        ).string_value

        self.kb_id = ssm.StringParameter.from_string_parameter_attributes(
            self, "KbId", parameter_name="/kb-id"
        ).string_value

        # Import Lambda Layer
        self.common_lambda_layer = _lambda.LayerVersion.from_layer_version_arn(
            self, "SharedLambdaLayerVersion", self.common_lambda_layer_arn
        )

        # Create Lambda functions for the workflow
        self.lambda_execution_role = self.create_lambda_execution_role()
        self.list_kb_lambda = self.create_list_kb_lambda()
        self.list_datasources_lambda = self.create_list_datasources_lambda()
        self.start_sync_lambda = self.create_start_sync_lambda()
        self.check_sync_status_lambda = self.create_check_sync_status_lambda()

        # Create Step Function
        self.sync_state_machine = self.create_sync_state_machine()

        # Create EventBridge schedule every 15 mins
        self.create_sync_schedule()

    def create_lambda_execution_role(self) -> iam.Role:
        role = iam.Role(
            self,
            gen_logical_id("KBLambdaExecRole"),
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name="kb-sync-handler-exec-role",
            description="Lambda Exec Role for Handling KB Sync Operations",
        )

        # Specific CloudWatch Logs permissions
        role.add_to_policy(
            iam.PolicyStatement(
                sid="CloudwatchLogsPermissions",
                effect=iam.Effect.ALLOW,
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                ],
                resources=[
                    f"arn:{self.aws_partition}:logs:{self.aws_region}:{self.account_id}:log-group:/aws/lambda/kb-*",
                    f"arn:{self.aws_partition}:logs:{self.aws_region}:{self.account_id}:log-group:/aws/lambda/kb-*:*",
                ],
            )
        )

        # Specific Bedrock KB permissions
        role.add_to_policy(
            iam.PolicyStatement(
                sid="BedrockKBPermissions",
                effect=iam.Effect.ALLOW,
                actions=[
                    "bedrock:ListDataSources",
                    "bedrock:StartIngestionJob",
                    "bedrock:GetIngestionJob",
                ],
                resources=[
                    f"arn:{self.aws_partition}:bedrock:{self.aws_region}:{self.account_id}:knowledge-base/{self.kb_id}",
                    f"arn:{self.aws_partition}:bedrock:{self.aws_region}:{self.account_id}:knowledge-base/{self.kb_id}/*",
                ],
            )
        )

        # Add suppressions for necessary wildcards
        NagSuppressions.add_resource_suppressions(
            role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "CloudWatch Logs requires wildcard for log stream creation within specific log groups. Scoped to kb-* Lambda functions only."
                }
            ],
            apply_to_children=True,
        )

        return role

    def create_list_kb_lambda(self) -> _lambda.Function:

        list_lambda_execution_role = iam.Role(
            self,
            gen_logical_id("ListRequestHandlerLambdaExecRole"),
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name="list-kb-lambda-exec-role",
            description="Lambda Exec Role for KB List Handler",
        )

        # Specific CloudWatch Logs permissions
        list_lambda_execution_role.add_to_policy(
            iam.PolicyStatement(
                sid="CloudwatchLogsPermissions",
                effect=iam.Effect.ALLOW,
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                ],
                resources=[
                    f"arn:{self.aws_partition}:logs:{self.aws_region}:{self.account_id}:log-group:/aws/lambda/kb-list-request-handler",
                    f"arn:{self.aws_partition}:logs:{self.aws_region}:{self.account_id}:log-group:/aws/lambda/kb-list-request-handler:*",
                ],
            )
        )

        # Add suppressions
        NagSuppressions.add_resource_suppressions(
            list_lambda_execution_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "CloudWatch Logs requires wildcard for log stream creation. Scoped to specific Lambda function log group.",
                }
            ],
            apply_to_children=True,
        )

        function = _lambda.Function(
            self,
            id=gen_logical_id("KnowledgeBaseListRequestFunction"),
            function_name="kb-list-request-handler",
            description="Knowledge Base List Function.",
            role=list_lambda_execution_role,
            runtime=LAMBDA_RUNTIME,
            memory_size=512,
            tracing=_lambda.Tracing.ACTIVE,
            logging_format=_lambda.LoggingFormat.JSON,
            code=_lambda.Code.from_asset(
                path="src/lambdas/kb_list_request_handler",
            ),
            handler="index.handler",
            layers=[self.common_lambda_layer],
            environment={
                "KNOWLEDGE_BASE_IDS": json.dumps([self.kb_id]),
            },
            timeout=Duration.seconds(300),
        )

        return function

    def create_list_datasources_lambda(self) -> _lambda.Function:
        return _lambda.Function(
            self,
            id=gen_logical_id("ListDataSourcesFunction"),
            function_name="kb-list-datasources-handler",
            description="Knowledge Base List DataSources Function.",
            role=self.lambda_execution_role,
            runtime=LAMBDA_RUNTIME,
            memory_size=512,
            tracing=_lambda.Tracing.ACTIVE,
            logging_format=_lambda.LoggingFormat.JSON,
            code=_lambda.Code.from_asset(
                path="src/lambdas/kb_list_datasources_handler",
            ),
            handler="index.handler",
            layers=[self.common_lambda_layer],
            timeout=Duration.seconds(300),
        )

    def create_start_sync_lambda(self) -> _lambda.Function:
        return _lambda.Function(
            self,
            id=gen_logical_id("StartSyncFunction"),
            function_name="kb-start-sync-handler",
            description="Knowledge Base Start Sync Function.",
            role=self.lambda_execution_role,
            runtime=LAMBDA_RUNTIME,
            memory_size=512,
            tracing=_lambda.Tracing.ACTIVE,
            logging_format=_lambda.LoggingFormat.JSON,
            code=_lambda.Code.from_asset(
                path="src/lambdas/kb_start_sync_handler",
            ),
            handler="index.handler",
            layers=[self.common_lambda_layer],
            timeout=Duration.seconds(300),
        )

    def create_check_sync_status_lambda(self) -> _lambda.Function:
        return _lambda.Function(
            self,
            id=gen_logical_id("SyncStatusCheckFunction"),
            function_name="kb-sync-status-check-handler",
            description="Knowledge Base Sync Status Check Function.",
            role=self.lambda_execution_role,
            runtime=LAMBDA_RUNTIME,
            memory_size=512,
            tracing=_lambda.Tracing.ACTIVE,
            logging_format=_lambda.LoggingFormat.JSON,
            code=_lambda.Code.from_asset(
                path="src/lambdas/kb_sync_status_check_handler",
            ),
            handler="index.handler",
            layers=[self.common_lambda_layer],
            timeout=Duration.seconds(300),
        )

    def create_sync_state_machine(self) -> sfn.StateMachine:
        # List Knowledge Bases
        list_kb_task = tasks.LambdaInvoke(
            self, "ProcessRequestAndListKnowledgeBases", lambda_function=self.list_kb_lambda, output_path="$.Payload"
        )

        # Map over Knowledge Bases
        kb_map = sfn.Map(self, "ProcessKnowledgeBases", max_concurrency=2, items_path="$.knowledgeBaseIds")

        # List Data Sources for each KB
        list_datasources_task = tasks.LambdaInvoke(
            self, "ListDataSources", lambda_function=self.list_datasources_lambda, output_path="$.Payload"
        )

        # Map over Data Sources
        datasource_map = sfn.Map(self, "ProcessDataSources", max_concurrency=1, items_path="$.dataSources")

        # Start Sync for each Data Source
        start_sync_task = tasks.LambdaInvoke(
            self, "StartSync", lambda_function=self.start_sync_lambda, output_path="$.Payload"
        )

        # Check Sync Status with retry
        check_sync_status = tasks.LambdaInvoke(
            self, "CheckSyncStatus", lambda_function=self.check_sync_status_lambda, output_path="$.Payload"
        )

        # Wait state
        wait_state = sfn.Wait(self, "StatusWait30Seconds", time=sfn.WaitTime.duration(Duration.seconds(30)))

        # Create choice state
        is_complete = sfn.Choice(self, "IsSyncComplete")
        sync_complete = sfn.Succeed(self, "SyncComplete")

        # Build the workflow
        check_status_flow = check_sync_status.next(
            is_complete.when(sfn.Condition.string_equals("$.status", "COMPLETE"), sync_complete)
            .when(sfn.Condition.string_equals("$.status", "FAILED"), sfn.Fail(self, "SyncFailed"))
            .otherwise(wait_state.next(check_sync_status))
        )

        datasource_workflow = start_sync_task.next(check_status_flow)
        datasource_map.iterator(datasource_workflow)

        kb_workflow = list_datasources_task.next(datasource_map)
        kb_map.iterator(kb_workflow)

        # Main workflow definition
        workflow_definition = list_kb_task.next(kb_map)

        sf_kb_pipeline_log_group = logs.LogGroup(
            self,
            "KbSyncPipelineLogGroup",
            log_group_name=f"/aws/vendedlogs/states/{self.stack_name}-Kb-data-sync-pipeline",
            retention=logs.RetentionDays.THREE_MONTHS,
        )

        state_machine = sfn.StateMachine(
            self,
            "KnowledgeBaseSyncStateMachine",
            state_machine_name="KnowledgeBaseSyncStateMachine",
            state_machine_type=sfn.StateMachineType.STANDARD,
            definition=workflow_definition,
            logs={"destination": sf_kb_pipeline_log_group, "level": sfn.LogLevel.ALL},
            timeout=Duration.hours(1),  # FAIL ME After 1 hour
            tracing_enabled=True,
        )
                # Add suppressions for Lambda ARN wildcards (CDK auto-generates these)
        NagSuppressions.add_resource_suppressions(
            state_machine,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Step Functions requires wildcard permissions to invoke Lambda function versions and aliases. This is a CDK-generated policy and follows AWS best practices for Step Functions Lambda integration.",
                    "appliesTo": [
                        "Resource::<KbSyncPipelineKnowledgeBaseListRequestFunctionF2ADAB6C.Arn>:*",
                        "Resource::<KbSyncPipelineListDataSourcesFunctionB35719E6.Arn>:*",
                        "Resource::<KbSyncPipelineStartSyncFunction4D3412CD.Arn>:*",
                        "Resource::<KbSyncPipelineSyncStatusCheckFunction7B2E9B12.Arn>:*",
                    ],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Step Functions requires permissions for X-Ray tracing across all resources. This is required for distributed tracing and follows AWS Step Functions best practices.",
                    "appliesTo": ["Resource::*"],
                },
            ],
            apply_to_children=True,
        )

        return state_machine

    def create_sync_schedule(self):
        # Create EventBridge rule to trigger Step Function
        rule = events.Rule(
            self,
            "KBSyncSchedule",
            rule_name="KBSyncSchedule",
            # Schedule for every 15 minutes
            schedule=events.Schedule.rate(Duration.minutes(15)),
        )

        # Define the input payload for the Step Function
        step_function_input = {
            "scheduled": True,
            "knowledgeBaseId": self.kb_id,
        }

        rule.add_target(
            targets.SfnStateMachine(self.sync_state_machine, input=events.RuleTargetInput.from_object(step_function_input))
        )
