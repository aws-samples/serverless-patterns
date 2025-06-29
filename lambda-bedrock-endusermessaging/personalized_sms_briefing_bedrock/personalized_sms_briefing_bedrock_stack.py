from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_logs as logs,
    CfnOutput,
    aws_secretsmanager as secretsmanager
)
from constructs import Construct
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from personalized_sms_briefing_bedrock import constants
import json

class PersonalizedSmsBriefingBedrockStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create IAM role for Weather Agent Lambda
        weather_agent_role = iam.Role(
            self, "WeatherAgentRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # Add Bedrock permissions to Weather Agent
        weather_agent_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "bedrock:InvokeModel",
                    "bedrock:InvokeModelWithResponseStream"
                ],
                resources=[
                    f"arn:aws:bedrock:{self.region}::foundation-model/*"
                ]
            )
        )
        # Add Secrets Manager permissions for Weather Agent
        weather_agent_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "secretsmanager:GetSecretValue"
                ],
                resources=[
                    constants.WEATHER_API_KEY_SECRET_ARN
                ]
            )
        )

        # Create Weather Agent Lambda Function
        weather_agent_function = PythonFunction(
            self, "WeatherAgentFunction",
            entry="lambda/weather_agent",  # Directory containing your code and requirements.txt
            runtime=_lambda.Runtime.PYTHON_3_11,
            index="weather_agent.py",  # The file containing your handler function
            handler="lambda_handler",  # The name of your handler function
            timeout=Duration.seconds(30),
            memory_size=256,
            role=weather_agent_role,
            environment={
                "WEATHER_API_KEY_SECRET_ARN": constants.WEATHER_API_KEY_SECRET_ARN,
                "AWS_BEDROCK_MODEL_ID": constants.AWS_BEDROCK_MODEL_ID,
                "LOCATION": constants.LOCATION
            },
            log_retention=logs.RetentionDays.ONE_WEEK
        )

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
                    "pinpoint:SendMessages"
                ],
                resources=["*"]
            )
        )

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

        sms_sender_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "lambda:InvokeFunction"
                ],
                resources=[weather_agent_function.function_arn]
            )
        )

        # Create SMS Sender Lambda Function
        sms_sender_function = _lambda.Function(
            self, "SmsSenderFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="personalize_daily_briefing.lambda_handler",
            code=_lambda.Code.from_asset("lambda/sms_sender"),
            timeout=Duration.seconds(60),
            memory_size=256,
            role=sms_sender_role,
            environment={
                "DESTINATION_PHONE_SECRET_ARN": constants.DESTINATION_PHONE_SECRET_ARN,
                "ORIGINATION_PHONE_SECRET_ARN":constants.ORIGINATION_PHONE_SECRET_ARN,
                "LOCATION": constants.LOCATION,
                "WEATHER_AGENT_FUNCTION_NAME": weather_agent_function.function_name
            },
            log_retention=logs.RetentionDays.ONE_WEEK
        )

         # Create EventBridge rule for scheduling
        schedule_rule = events.Rule(
            self, "DailyBriefingSchedule",
            schedule=events.Schedule.cron(
                minute=str(constants.SCHEDULE_MINUTE),
                hour=str(constants.SCHEDULE_HOUR),
                day="*",
                month="*",
                year="*"
            ),
            description="Personalized Daily briefing SMS schedule"
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
            self, "WeatherAgentFunctionName",
            value=weather_agent_function.function_name,
            description="Weather Agent Lambda Function Name"
        )

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
