from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    aws_lambda as _lambda,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
    aws_iam as iam
)
from constructs import Construct

class CdkStepfunctionDurableLambdaFunctionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        resource_prefix = "sfn-dfn"

        # Create a durable Lambda function with execution timeout > 15 mins   
        async_durable_lambda_fn = _lambda.Function(self, "asyncDurableFunctionInvocation",
            description="Durable Lambda function with execution timeout > 15 mins, invoked asynchronously from Step Function",
            function_name=f"{resource_prefix}-async-durable-fn",
            runtime=_lambda.Runtime.PYTHON_3_14,
            handler="async_durable_function_invocation.lambda_handler",
            architecture=_lambda.Architecture.ARM_64,
            code=_lambda.Code.from_asset("./async-durable-lambda/"),
            timeout=Duration.minutes(15),
            # DurableConfig is what makes a Lambda function "durable"
            durable_config=_lambda.DurableConfig(
                execution_timeout=Duration.hours(1),    # Durable Function duration set to 1 hour, greater than lambda function's 15 mins timeout
                retention_period=Duration.days(3),
            ),
        )
        
        # Create version for async durable function (required for durable functions)
        async_durable_lambda_version = async_durable_lambda_fn.current_version

        # Create a durable Lambda function with execution timeout < 15 mins
        synchronous_durable_lambda_fn = _lambda.Function(self, "synchronousDurableFunctionInvocation",
            description="Durable Lambda function with execution timeout < 15 mins, invoked synchronously from Step Function",
            function_name=f"{resource_prefix}-sync-durable-fn",
            runtime=_lambda.Runtime.PYTHON_3_14,
            handler="synchronous_durable_function_invocation.lambda_handler",
            architecture=_lambda.Architecture.ARM_64,
            code=_lambda.Code.from_asset("./sync-durable-lambda/"),
            timeout=Duration.minutes(15),
            # DurableConfig is what makes a Lambda function "durable"
            durable_config=_lambda.DurableConfig(
                execution_timeout=Duration.minutes(15),    # Durable Function duration set to 15 mins, equal to lambda function's 15 mins timeout
                retention_period=Duration.days(3),
            ),
        )

        # Create version for async durable function (required for durable functions)
        sync_durable_lambda_version = synchronous_durable_lambda_fn.current_version

        invoke_async_durable_function_task = tasks.LambdaInvoke(
            self, "Async Durable Lambda Fn Invoke",
            lambda_function=async_durable_lambda_version,
            integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN, # use this pattern to pass a task token to durable fn invoked asynchronously
            invocation_type=tasks.LambdaInvocationType.EVENT,               # set Lambda invocaton type = Event for async invoke
            payload=sfn.TaskInput.from_object({
                "TaskToken": "{% $states.context.Task.Token %}",
                "minutes_to_wait": "{% $states.input.minutes_to_wait %}"
            }),
            outputs="{% $states.result %}",
            heartbeat_timeout=sfn.Timeout.duration(Duration.hours(1)),      # setting Step Function task heartbeat timeout to 1 hour to match durable function's execution timeout
        )

        invoke_sync_durable_function_task = tasks.LambdaInvoke(
            self, "Synchronous Durable Lambda Fn Invoke",
            lambda_function=sync_durable_lambda_version,
            payload=sfn.TaskInput.from_text("{% $states.input %}"),
            outputs="{% $states.result.Payload %}"
        )

        chain = invoke_async_durable_function_task\
            .next(invoke_sync_durable_function_task
        )
        
        state_machine = sfn.StateMachine(self, "SFnDurableFunctionIntegration",
            definition_body = sfn.DefinitionBody.from_chainable(chain),
            query_language=sfn.QueryLanguage.JSONATA,
            state_machine_name=resource_prefix + "-integration-pattern-cdk",
            timeout=Duration.hours(2)
        )

        # Grant permission to allow durable Lambda function to send the token to
        # the Step Function using send_task_success or send_task_failure API for 
        # WaitForTaskToken pattern
        async_durable_lambda_fn.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "states:SendTaskSuccess",
                    "states:SendTaskFailure",
                    "states:SendTaskHeartbeat"
                ],
                resources=[f"arn:aws:states:{self.region}:{self.account}:stateMachine:*"]
            )
        )

        CfnOutput(self, "StepFunctionDFArn",
            value = state_machine.state_machine_arn,
            export_name = 'StepFunctionDFArn',
            description = 'Step Function arn')

        CfnOutput(self, "AsyncDurableFunctionName",
            value = async_durable_lambda_fn.function_name,
            export_name = 'AsyncDurableFunctionName',
            description = 'Async durable Lambda function name')

        CfnOutput(self, "SyncDurableFunctionName",
            value = synchronous_durable_lambda_fn.function_name,
            export_name = 'SyncDurableFunctionName',
            description = 'Synchronous durable Lambda function name')

