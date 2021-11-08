from aws_cdk import core as cdk

from aws_cdk import (
    aws_stepfunctions as sfn,
    aws_sqs as sqs,
    aws_stepfunctions_tasks as sfn_tasks,
    core
)


class SfnSqsCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
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
            timeout=core.Duration.minutes(5)
        )
