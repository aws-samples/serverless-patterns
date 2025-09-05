from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_logs as logs,
    CfnOutput,
)
from constructs import Construct
from simple_sms_messaging import constants

class SimpleSmSMessagingStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create IAM role for SMS Sender Lambda
        sms_sender_role = iam.Role(
            self, "SmsSenderRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # Add SMS permissions
        sms_sender_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "sms-voice:SendTextMessage",
                ],
                resources=["*"]
            )
        )

        # Add Secrets Manager permissions
        sms_sender_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "secretsmanager:GetSecretValue"
                ],
                resources=[
                    constants.DESTINATION_PHONE_SECRET_ARN,
                    constants.ORIGINATION_PHONE_SECRET_ARN
                ]
             )
        )

        # Create SMS Sender Lambda Function
        sms_sender_function = _lambda.Function(
            self, "SmsSenderFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="send_sms.lambda_handler",
            code=_lambda.Code.from_asset("lambda/simple_sms_sender"),
            timeout=Duration.seconds(30),
            memory_size=128,
            role=sms_sender_role,
            environment={
                "DESTINATION_PHONE_SECRET_ARN": constants.DESTINATION_PHONE_SECRET_ARN,
                "ORIGINATION_PHONE_SECRET_ARN": constants.ORIGINATION_PHONE_SECRET_ARN,
                "MESSAGE": constants.MESSAGE
            },
            log_retention=logs.RetentionDays.ONE_WEEK
        )

        # Create EventBridge rule for scheduling
        schedule_rule = events.Rule(
            self, "DailyMessageSchedule",
            schedule=events.Schedule.cron(
                minute=str(constants.SCHEDULE_MINUTE),
                hour=str(constants.SCHEDULE_HOUR),
                day="*",
                month="*",
                year="*"
            ),
            description="Simple daily SMS message schedule"
        )

        # Add SMS sender function as target
        schedule_rule.add_target(
            targets.LambdaFunction(sms_sender_function)
        )

        # Grant EventBridge permission to invoke Lambda
        sms_sender_function.add_permission(
            "AllowEventBridge",
            principal=iam.ServicePrincipal("events.amazonaws.com"),
            source_arn=schedule_rule.rule_arn
        )

        # Outputs
        CfnOutput(
            self, "SmsSenderFunctionName",
            value=sms_sender_function.function_name,
            description="SMS Sender Lambda Function Name"
        )

        CfnOutput(
            self, "ScheduleRuleArn",
            value=schedule_rule.rule_arn,
            description="EventBridge Schedule Rule ARN"
        )

        CfnOutput(
            self, "ScheduleExpression",
            value=f"cron({constants.SCHEDULE_MINUTE} {constants.SCHEDULE_HOUR} * * ? *)",
            description="Schedule Expression (UTC)"
        )