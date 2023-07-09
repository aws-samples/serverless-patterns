from aws_cdk import (
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_pipes as pipes,
    aws_sqs as sqs,
    aws_stepfunctions as sfn,
)
from constructs import Construct
import json

class EventbridgePipesSqsToStepfunctionsCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source = sqs.Queue(self, 'sqs-queue')

        target = sfn.StateMachine(self, "state-machine",
            definition=sfn.Pass(self, "start-state")
        )

        source_policy = iam.PolicyStatement(
                actions=['sqs:ReceiveMessage', 'sqs:DeleteMessage', 'sqs:GetQueueAttributes'],
                resources=[source.queue_arn],
                effect=iam.Effect.ALLOW,
        )

        target_policy = iam.PolicyStatement(
                actions=['states:StartExecution'],
                resources=[target.state_machine_arn],
                effect=iam.Effect.ALLOW,
        )

        pipe_role = iam.Role(self, 'pipe-role',
            assumed_by=iam.ServicePrincipal('pipes.amazonaws.com'),
        )

        pipe_role.add_to_policy(source_policy)
        pipe_role.add_to_policy(target_policy)

        pipe = pipes.CfnPipe(self, "pipe",
            role_arn=pipe_role.role_arn,
            source=source.queue_arn,
            source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                    batch_size=1
                )
            ),
            target=target.state_machine_arn,
            target_parameters=pipes.CfnPipe.PipeTargetParametersProperty(
                step_function_state_machine_parameters=pipes.CfnPipe.PipeTargetStateMachineParametersProperty(
                    invocation_type="FIRE_AND_FORGET"
                ),
                input_template=json.dumps({
                    "orderId": "<$.body.orderId>",
                    "customerId": "<$.body.customerId>",
                })
            )
        )

        # Output
        CfnOutput(self, "QUEUE_URL", value=source.queue_url)
        CfnOutput(self, "PIPE_ARN", value=pipe.attr_arn)
        CfnOutput(self, "STATE_MACHINE_ARN", value=target.state_machine_arn)
