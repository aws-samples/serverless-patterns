from aws_cdk import (
    aws_events as events,
    aws_lambda as lambda_,
    aws_events_targets as targets,
    aws_logs as logs,
    core as cdk,
)


class EventBridgeLambdaStack(cdk.Stack):
    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)

        # Lambda Function
        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()

        lambdaFn = lambda_.Function(
            self, "Singleton",
            code=lambda_.InlineCode(handler_code),
            handler="index.main",
            timeout=cdk.Duration.seconds(10),
            runtime=lambda_.Runtime.PYTHON_3_9,
        )

        # Set Lambda Logs Retention and Removal Policy
        logs.LogGroup(
            self,
            'logs',
            log_group_name = f"/aws/lambda/{lambdaFn.function_name}",
            removal_policy = cdk.RemovalPolicy.DESTROY,
            retention = logs.RetentionDays.ONE_DAY
        )

        # EventBridge Rule
        rule = events.Rule(
            self, "Rule",
        )
        rule.add_event_pattern(
            source=["cdk.myApp"],
            detail_type=["transaction"]
        )
        rule.add_target(targets.LambdaFunction(lambdaFn))


app = cdk.App()
EventBridgeLambdaStack(app, "EventBridgeLambdaExample")
app.synth()