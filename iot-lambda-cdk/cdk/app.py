import os
import json
from aws_cdk import (
    App,
    Stack,
    Duration,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_logs as logs,
    aws_iam as iam,
    aws_iot as iot
)
from constructs import Construct

class IoTLambdaStack(Stack):
    def __init__(self, app: App, id: str) -> None:
        super().__init__(app, id)


        # Lambda Function
        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()

        lambdaFn = _lambda.Function(
            self, "IoTTriggerLambda",
            code=_lambda.InlineCode(handler_code),
            handler="index.main",
            timeout=Duration.seconds(10),
            runtime=_lambda.Runtime.PYTHON_3_9,
        )

        # Set Lambda Logs Retention and Removal Policy
        logs.LogGroup(
            self,
            'logs',
            log_group_name = f"/aws/lambda/{lambdaFn.function_name}",
            removal_policy = RemovalPolicy.DESTROY,
            retention = logs.RetentionDays.ONE_DAY
        )
        
        # IoT Thing
        iot_thing = iot.CfnThing(
            self, "IoTThing",
            thing_name="MyIotThing"
        )

        
        # IoT Rule with SQL, which invokes a Lambda Function
        iot_topic_rule_sql = 'SELECT * FROM "$aws/things/MyIotThing/*"'
        iot_topic_rule = iot.CfnTopicRule(
            self, "IoTRule",
            topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                sql=iot_topic_rule_sql,
                actions=[iot.CfnTopicRule.ActionProperty(
                    lambda_=iot.CfnTopicRule.LambdaActionProperty(
                        function_arn=lambdaFn.function_arn
                    )
                )]
            )
        )

        # Lambda Resource Policy allows invocation from IoT Rule 
        lambdaFn.add_permission(
            "GrantIoTRule",
            principal=iam.ServicePrincipal("iot.amazonaws.com"),
            source_arn=iot_topic_rule.attr_arn
        )


app = App()
IoTLambdaStack(app, "IoTLambdaStackExample")
app.synth()