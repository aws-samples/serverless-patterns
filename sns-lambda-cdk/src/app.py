from aws_cdk import (
    aws_lambda as _lambda,
    aws_logs as logs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core as cdk,
)


class SNSLambdaStack(cdk.Stack):
    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)

        # Lambda Function
        lambdaFn = _lambda.Function(self, "SNSEventHandler",
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

        # SNS topic
        topic = sns.Topic(self, 'sns-to-lambda-topic-test',
                          display_name='My SNS topic')

        # subscribe Lambda to SNS topic
        topic.add_subscription(subs.LambdaSubscription(lambdaFn))

        # Output information about the created resources
        cdk.CfnOutput(self, 'snsTopicArn',
                      value=topic.topic_arn,
                      description='The arn of the SNS topic')
        cdk.CfnOutput(self, 'functionName',
                      value=lambdaFn.function_name,
                      description='The name of the handler function')


app = cdk.App()
SNSLambdaStack(app, "SNSLambdaStackExample")
app.synth()
