from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_sqs as _sqs,
    aws_lambda as _lambda,
    aws_logs as logs,
    aws_stepfunctions_tasks as tasks,
    aws_stepfunctions as sf,
)
from constructs import Construct

class StepFunctionCallbackStack(Stack):

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
            handler="send_callback_token.handler",
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

        step_function_definition = tasks.SqsSendMessage(self, "SendToSQS",
            integration_pattern = sf.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
            queue=queue,
            message_body=sf.TaskInput.from_object({
              "input.$" : "$",
              "token" : sf.JsonPath.task_token
              }
            )
        )
        step_function = sf.StateMachine(self, "StepFunction",
                definition=step_function_definition,
                timeout=Duration.minutes(60)
        )

        #grant permission to Lambda function to send the token to the Step Function
        step_function.grant_task_response(lambda_function)

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

        CfnOutput(self, "StepFunctionArn",
            value = step_function.state_machine_arn,
            export_name = 'StepFunctionArn',
            description = 'Step Function arn')
