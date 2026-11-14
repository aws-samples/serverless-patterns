from aws_cdk import (
    Stack,
    Duration,
    CfnOutput,
    aws_stepfunctions as sfn,
    aws_sqs as sqs,
    aws_stepfunctions_tasks as sfn_tasks
)
from constructs import Construct

class SfnSqsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_queue = sqs.Queue(self, "queue-from-cdk")

        send_to_sqs_task = sfn_tasks.SqsSendMessage(self, id="SendToMyQueue",
                                                    message_body=sfn.TaskInput.
                                                    from_json_path_at("$.message")
                                                    , queue=my_queue)

        definition = send_to_sqs_task
        state_machine = sfn.StateMachine(
            self, "SQSWorkflowStateMachine",
            definition=definition,
            timeout=Duration.minutes(5)
        )


        CfnOutput(scope=self, id='StateMachineArn',
                       value=state_machine.state_machine_arn)
        CfnOutput(scope=self, id='QueueUrl',
                       value=my_queue.queue_url)
