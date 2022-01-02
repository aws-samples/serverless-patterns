#!/usr/bin/env python3
from aws_cdk import (
    aws_lambda as _lambda,
    aws_logs as logs,
    aws_sns as sns,
    core as cdk
)

from constructs import Construct

class LambdaSnsCdkStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create SNS Topic
        # SNS topic
        topic = sns.Topic(self, 'sns-to-lambda-topic',
                          display_name='My SNS topic')

        # Create Lambda function
        lambdaFn = _lambda.Function(self, "SNSPublisher",
                                    runtime=_lambda.Runtime.PYTHON_3_9,
                                    code=_lambda.Code.from_asset("lambda"),
                                    handler="handler.main",
                                    timeout=cdk.Duration.seconds(10))

        # Set Lambda Logs Retention and Removal Policy
        logs.LogGroup(
            self,
            'logs',
            log_group_name=f"/aws/lambda/{lambdaFn.function_name}",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            retention=logs.RetentionDays.ONE_DAY
        )

        # Grant publish to lambda function
        topic.grant_publish(lambdaFn)

        cdk.CfnOutput(self, 'snsTopicArn',
                      value=topic.topic_arn,
                      description='The arn of the SNS topic')
        cdk.CfnOutput(self, 'functionName',
                      value=lambdaFn.function_name,
                      description='The name of the handler function')


app = cdk.App()
LambdaSnsCdkStack(app, "LambdaSnsCdkStack")
app.synth()
