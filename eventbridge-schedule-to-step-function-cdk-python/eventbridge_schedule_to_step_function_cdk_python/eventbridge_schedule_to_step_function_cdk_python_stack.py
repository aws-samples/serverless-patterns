from aws_cdk import (
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_scheduler as scheduler,
    aws_stepfunctions as sfn,
)
from constructs import Construct
import json

class EventbridgeScheduleToStepFunctionCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## State machine
        state_machine = sfn.StateMachine(self, "state-machine",
            definition=sfn.Pass(self, "start-state")
        )

        ## Add scheduler permissions
        scheduler_role = iam.Role(self, "scheduler-role",
            assumed_by=iam.ServicePrincipal("scheduler.amazonaws.com"),
        )

        scheduler_sf_execution_policy = iam.PolicyStatement(
                actions=["states:StartExecution"],
                resources=[state_machine.state_machine_arn],
                effect=iam.Effect.ALLOW,
        )

        scheduler_role.add_to_policy(scheduler_sf_execution_policy)

        ## Add schedule group
        schedule_group = scheduler.CfnScheduleGroup(self, "my-schedule-group", 
            name="my-schedule-group",
        );

        ## Add schedule
        my_schedule = scheduler.CfnSchedule(self, "my-schedule",
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="OFF",
                ),
                schedule_expression="rate(5 minute)",
                group_name=schedule_group.name,
                target=scheduler.CfnSchedule.TargetProperty(
                    arn=state_machine.state_machine_arn,
                    role_arn=scheduler_role.role_arn,
                    input=json.dumps({
                        "metadata": {
                            "eventId": "MY_SCHEDULED_EVENT",
                        },
                        "data" : {
                            "firstName": "Pubudu",
                            "lastName": "Jayawardana"            
                        }
                    })
                )
            )

        ## Output
        CfnOutput(self, "SCHEDULE_NAME", value=my_schedule.ref)
        CfnOutput(self, "STATE_MACHINE_ARN", value=state_machine.state_machine_arn)
