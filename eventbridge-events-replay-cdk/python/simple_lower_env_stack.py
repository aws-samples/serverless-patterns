from aws_cdk import Stack, aws_events as events, CfnOutput, aws_iam, aws_sns
import os
from constructs import Construct

dirname = os.path.dirname(__file__)


class SimpleLowerEnvironmentStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, prod_account_id: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lower_env_event_bus = events.EventBus(
            self, "ReceivingEventBus", event_bus_name="LowerEnvEventBus"
        )
        sns_target_for_testing = aws_sns.Topic(
            self, "SNSTarget", topic_name="SNSTargetForTesting"
        )

        cfn_event_bus_policy = events.CfnEventBusPolicy(
            self,
            "AllowProdAccountsToSendEvents",
            statement_id="AllowProdAccountsToSendEventsStatementId",
            # the properties below are optional
            action="events:PutEvents",
            event_bus_name="LowerEnvEventBus",
            principal=prod_account_id,
        )

        cfn_event_bus_policy.node.add_dependency(lower_env_event_bus)

        event_pattern = {"account": [{"exists": True}]}

        sns_write_role = aws_iam.Role(
            self,
            "SnsWriteRole",
            assumed_by=aws_iam.ServicePrincipal(f"events.amazonaws.com"),
            role_name="sns_write_role",
        )
        sns_write_role.attach_inline_policy(
            aws_iam.Policy(
                self,
                "write_to_sns",
                statements=[
                    aws_iam.PolicyStatement(actions=["sns:*"], resources=["*"])
                ],
            )
        )
        test_rule = events.CfnRule(
            self,
            id="TestRule",
            description="Test Rule with SNS target to confirm the receipt of events",
            event_bus_name="LowerEnvEventBus",
            event_pattern=event_pattern,
            name="test_rule",
            role_arn=sns_write_role.role_arn,
            targets=[
                events.CfnRule.TargetProperty(
                    id="SnsTargetProperty", arn=sns_target_for_testing.topic_arn
                )
            ],
        )

        CfnOutput(
            scope=self,
            id="LowerEnvironmentEventBusArn",
            value=lower_env_event_bus.event_bus_arn,
            description="EventBus ARN to receive events from higher environments",
        )
