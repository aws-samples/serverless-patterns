from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_sqs as _sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _event,
    aws_logs as logs,
)
from constructs import Construct

class SqsLambdaCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = _sqs.Queue(
            self, "MyQueue",
            visibility_timeout=Duration.seconds(300)
            )

        # Create the AWS Lambda function to subscribe to Amazon SQS queue
        # The source code is in './lambda' directory
        lambda_function = _lambda.Function(
            self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="get_messages.handler",
            code=_lambda.Code.from_asset("lambda"),
        )

        # Set Lambda Logs Retention and Removal Policy
        logs.LogGroup(
            self,
            'logs',
            log_group_name = f"/aws/lambda/{lambda_function.function_name}",
            removal_policy = RemovalPolicy.DESTROY,
            retention = logs.RetentionDays.ONE_DAY
        )
        #Grant permission to AWS Lambda function to consume messages from the Amazon SQS queue
        queue.grant_consume_messages(lambda_function)

        #Configure the Amazon SQS queue to trigger the AWS Lambda function
        lambda_function.add_event_source(_event.SqsEventSource(queue))

        CfnOutput(self, "FunctionName",
            value = lambda_function.function_name,
            export_name = 'FunctionName',
            description = 'Function name')

        CfnOutput(self, "QueueName",
            value = queue.queue_name,
            export_name = 'QueueName',
            description = 'SQS queue name')

        CfnOutput(self, "QueueArn",
            value = queue.queue_arn,
            export_name = 'QueueArn',
            description = 'SQS queue ARN')

        CfnOutput(self, "QueueUrl",
            value = queue.queue_url,
            export_name = 'QueueUrl',
            description = 'SQS queue URL')