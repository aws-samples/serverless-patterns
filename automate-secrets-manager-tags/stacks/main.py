from aws_cdk import (
    Stack
)
from constructs import Construct
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_iam as iam


class AutomateSecretsManagerTagsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Lambda function to handle the tagging
        lambda_function = _lambda.Function(self, "MyEventBridgeLambda",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="index.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Grant the Lambda function permission to tag the secret
        lambda_function.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=["secretsmanager:TagResource"],
                resources=["arn:aws:secretsmanager:*:*:*"]
            )
        )
        
        # Create an EventBridge rule to capture SSO login events
        # https://docs.aws.amazon.com/secretsmanager/latest/userguide/cloudtrail_log_entries.html#cloudtrail_log_entries_operations
        rule = events.Rule(self, "CreateSecretsRule",
            event_pattern=events.EventPattern(
                source=["aws.secretsmanager"],
                detail_type=["AWS API Call via CloudTrail"],
                detail={
                    "eventSource": ["secretsmanager.amazonaws.com"],
                    "eventName": ["CreateSecret"]
                }
            )
        )
        # Set the Lambda function as the target for the rule
        rule.add_target(targets.LambdaFunction(lambda_function))
