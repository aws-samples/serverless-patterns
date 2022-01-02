from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_sqs as _sqs,
    aws_lambda as _lambda,
    aws_logs as logs,
    aws_events as events,
    aws_events_targets as events_target
)
from constructs import Construct

class SqsLambdaEbCdkStack(Stack):

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
            handler="submit_job.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment = {
            'QUEUE_URL': queue.queue_url
          }
        )

        # Set Lambda Logs Retention and Removal Policy
        logs.LogGroup(
            self,
            'logs',
            log_group_name = f"/aws/lambda/{lambda_function.function_name}",
            removal_policy = RemovalPolicy.DESTROY,
            retention = logs.RetentionDays.ONE_DAY
        )

        #Event Bridge rule
        #Change the rate according to your needs
        rule = events.Rule(self, 'Rule',
           description = "Trigger Lambda function every 2 minutes",
           schedule = events.Schedule.expression('rate(2 minutes)')
        )

        rule.add_target(events_target.LambdaFunction(lambda_function));

        #Grant permission to AWS Lambda function to consume messages from the Amazon SQS queue
        queue.grant_consume_messages(lambda_function)

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

        CfnOutput(self, "RuleName",
            value = rule.rule_name,
            export_name = 'RuleName',
            description = 'EventBridge rule name')