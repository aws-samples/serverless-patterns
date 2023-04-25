from aws_cdk import (
    Stack,
    aws_kinesis as kinesis,
    Duration,
    aws_stepfunctions as stepfunctions,
    aws_stepfunctions_tasks as tasks,
    aws_lambda,
    aws_events as events,
    aws_iam,
    Aws,
    aws_pipes,
    CfnOutput,
)
import os
from constructs import Construct

dirname = os.path.dirname(__file__)


class EventbridgeEventsReplayStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        cross_account_eventbus_arn: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # kinesis stream to hold  replayed and sampled events
        replayed_events_stream = kinesis.Stream(
            self, "ReplayedEventsStream", stream_name="ReplayedEventsStream"
        )

        # Main event bus with actual business transactions
        main_bus = events.EventBus(
            self, "MainEventBus", event_bus_name="EventBusWithBizTransactions"
        )

        main_bus_archive = main_bus.archive(
            "main_bus_archive",
            archive_name="ArhiveOfMainBus",
            description="EventBusWithBizTransactions Archive",
            event_pattern=events.EventPattern(region=[Aws.REGION]),
            retention=Duration.days(30),
        )

        event_pattern = {"replay-name": [{"exists": True}]}

        kinesis_write_role = aws_iam.Role(
            self,
            "KinesisWriteRole",
            assumed_by=aws_iam.ServicePrincipal(f"events.amazonaws.com"),
            role_name="kinesis_write_role_for_events_rule",
        )
        kinesis_write_role.attach_inline_policy(
            aws_iam.Policy(
                self,
                "write_to_kinesis_policy",
                statements=[
                    aws_iam.PolicyStatement(actions=["kinesis:*"], resources=["*"])
                ],
            )
        )
        allow_replay_only_events_rule = events.CfnRule(
            self,
            id="AllowReplayOnlyEventsRule",
            description="Allow only replayed events so they can be mirrored to lower environments",
            event_bus_name="EventBusWithBizTransactions",
            event_pattern=event_pattern,
            name="allow_replay_only_events_rule",
            role_arn=kinesis_write_role.role_arn,
            targets=[
                events.CfnRule.TargetProperty(
                    id="KinesisTargetProperty", arn=replayed_events_stream.stream_arn
                )
            ],
        )

        # Event bus to hold post processed events before sending to lower environments
        post_enrichment_bus = events.EventBus(
            self, "PostEnrichmentBus", event_bus_name="PostEnrichmentBus"
        )

        event_pattern = {"account": [{"exists": True}]}

        cross_account_put_events_role = aws_iam.Role(
            self,
            "CrossAccountPutEventsRole",
            assumed_by=aws_iam.ServicePrincipal(f"events.amazonaws.com"),
            role_name="cross_account_put_events_role",
        )
        cross_account_put_events_role.attach_inline_policy(
            aws_iam.Policy(
                self,
                "cross_account_put_events_policy",
                statements=[
                    aws_iam.PolicyStatement(
                        actions=["events:PutEvents"],
                        resources=[cross_account_eventbus_arn],
                    )
                ],
            )
        )

        send_to_another_account_rule = events.CfnRule(
            self,
            id="SendToAnotherAccountEventsRule",
            description="Allow everything in the post enrichment bus to go to an event bus in another account",
            event_bus_name="PostEnrichmentBus",
            event_pattern=event_pattern,
            name="send_to_another_account_events_rule",
            role_arn=cross_account_put_events_role.role_arn,
            targets=[
                events.CfnRule.TargetProperty(
                    id="CrossAccountTargetProperty",
                    arn=cross_account_eventbus_arn,
                    role_arn=cross_account_put_events_role.role_arn,
                )
            ],
        )

        # Eventbridge pipe related resources
        cleanup_lambda = aws_lambda.Function(
            self,
            "CleanupLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset(
                os.path.join(dirname, "functions", "cleanup-events")
            ),
            handler="cleanup_events.handler",
            timeout=Duration.seconds(300),
        )

        eventbridge_pipe_role = aws_iam.Role(
            self,
            "EventBridgePipeRole",
            assumed_by=aws_iam.ServicePrincipal(f"pipes.amazonaws.com"),
        )

        eventbridge_pipe_poicy = aws_iam.Policy(
            self,
            "EventBridgePipePolicy",
            statements=[
                aws_iam.PolicyStatement(
                    effect=aws_iam.Effect.ALLOW,
                    actions=["events:PutEvents"],
                    resources=[post_enrichment_bus.event_bus_arn],
                ),
                aws_iam.PolicyStatement(
                    effect=aws_iam.Effect.ALLOW,
                    actions=[
                        "kinesis:DescribeStream",
                        "kinesis:DescribeStreamSummary",
                        "kinesis:GetRecords",
                        "kinesis:GetShardIterator",
                        "kinesis:ListStreams",
                        "kinesis:ListShards",
                    ],
                    resources=[replayed_events_stream.stream_arn],
                ),
                aws_iam.PolicyStatement(
                    effect=aws_iam.Effect.ALLOW,
                    actions=["lambda:InvokeFunction"],
                    resources=[cleanup_lambda.function_arn],
                ),
            ],
        )

        eventbridge_pipe_role.attach_inline_policy(eventbridge_pipe_poicy)
        aws_pipes.CfnPipe(
            self,
            id="ProcessAndEnrichPipe",
            role_arn=eventbridge_pipe_role.role_arn,
            source=replayed_events_stream.stream_arn,
            target=post_enrichment_bus.event_bus_arn,
            enrichment=cleanup_lambda.function_arn,
            source_parameters=aws_pipes.CfnPipe.PipeSourceParametersProperty(
                kinesis_stream_parameters=aws_pipes.CfnPipe.PipeSourceKinesisStreamParametersProperty(
                    starting_position="LATEST",
                    # the properties below are optional
                    batch_size=1,
                    maximum_retry_attempts=1,
                )
            ),
            target_parameters=aws_pipes.CfnPipe.PipeTargetParametersProperty(
                event_bridge_event_bus_parameters=aws_pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty(
                    detail_type="manualDetailType",
                )
            ),
        )

        # Replay lambda function
        replay_events_lambda = aws_lambda.Function(
            self,
            "ReplayEventsLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset(
                os.path.join(dirname, "functions", "replay-events")
            ),
            handler="replay_events.handler",
            timeout=Duration.seconds(300),
            environment={
                "EVENT_BUS_NAME": main_bus.event_bus_name,
                "EVENT_BUS_ARN": main_bus.event_bus_arn,
                "EVENT_SOURCE_ARN": main_bus_archive.archive_arn,
                "ALLOW_REPLAY_EVENTS_ONLY_RULE_ARN": allow_replay_only_events_rule.attr_arn,
                "SAMPLE_START_EPOCH": "1682009582",
                "SAMPLE_END_EPOCH": "1682700782",
            },
        )
        replay_events_lambda.role.attach_inline_policy(
            aws_iam.Policy(
                self,
                "ReplayEventsPolicy",
                statements=[
                    aws_iam.PolicyStatement(
                        actions=["events:StartReplay"],
                        resources=["*"],
                    )
                ],
            )
        )
        describe_replay_lambda = aws_lambda.Function(
            self,
            "DescribeReplayLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset(
                os.path.join(dirname, "functions", "describe-replay")
            ),
            handler="describe_replay.handler",
            timeout=Duration.seconds(300),
        )
        describe_replay_lambda.role.attach_inline_policy(
            aws_iam.Policy(
                self,
                "DescribeReplayPolicy",
                statements=[
                    aws_iam.PolicyStatement(
                        actions=["events:DescribeReplay"],
                        resources=["*"],
                    )
                ],
            )
        )

        log_replay_status_lambda = aws_lambda.Function(
            self,
            "LogReplayStatusLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset(
                os.path.join(dirname, "functions", "log-replay-status")
            ),
            handler="log_replay_status.handler",
            timeout=Duration.seconds(300),
        )
        # Step function definition
        replay_events_task = tasks.LambdaInvoke(
            self,
            "ReplayEventsTask",
            lambda_function=replay_events_lambda,
            result_path="$.taskresult",
        )
        describe_replay_task = tasks.LambdaInvoke(
            self,
            "DescribeReplayTask",
            lambda_function=describe_replay_lambda,
            result_path="$.taskresult",
        )

        log_replay_status_task = tasks.LambdaInvoke(
            self,
            "LogReplayStatusTask",
            lambda_function=log_replay_status_lambda,
            result_path="$.taskresult",
        )
        retry_replay_status_choice = stepfunctions.Choice(
            self, "RetryReplayStatusChoice"
        )
        retry = stepfunctions.Condition.string_equals(
            variable="$.taskresult.Payload.action", value="recheck"
        )
        no_retry = stepfunctions.Condition.string_equals(
            variable="$.taskresult.Payload.action", value="alert"
        )
        wait_for_replay_complete = stepfunctions.Wait(
            self, "Wait", time=stepfunctions.WaitTime.duration(Duration.seconds(60))
        )

        step_function_def = (
            stepfunctions.Chain.start(replay_events_task)
            .next(describe_replay_task)
            .next(
                retry_replay_status_choice.when(
                    retry, wait_for_replay_complete.next(describe_replay_task)
                ).otherwise(log_replay_status_task)
            )
        )
        states_execution_role = aws_iam.Role(
            self,
            "StatesExecutionRole",
            assumed_by=aws_iam.ServicePrincipal(f"states.{Aws.REGION}.amazonaws.com"),
        )
        states_execution_policy = aws_iam.Policy(
            self,
            "StatesExecutionPolicy",
            statements=[
                aws_iam.PolicyStatement(
                    effect=aws_iam.Effect.ALLOW,
                    actions=["lambda:InvokeFunction"],
                    resources=[
                        replay_events_lambda.function_arn,
                    ],
                ),
            ],
        )

        statemachine = stepfunctions.StateMachine(
            self,
            "EventReplayStepFunction",
            definition=step_function_def,
        )
        statemachine.role.attach_inline_policy(states_execution_policy)
        statemachine.role.grant_assume_role(
            aws_iam.ServicePrincipal(f"states.{Aws.REGION}.amazonaws.com")
        )

        CfnOutput(
            scope=self,
            id="EventBusWithBizTransactionsArn",
            value=main_bus.event_bus_arn,
            description="The main event bus ARN in PROD account where business transaction events exist ",
        )

        CfnOutput(
            scope=self,
            id="ReplayEventsStateMachineArn",
            value=statemachine.state_machine_arn,
            description="ARN of the state machine that triggers replay event",
        )
