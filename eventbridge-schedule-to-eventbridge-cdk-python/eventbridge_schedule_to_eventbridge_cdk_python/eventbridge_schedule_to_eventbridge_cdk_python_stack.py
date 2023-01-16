from aws_cdk import (
    CfnOutput,
    Stack,
    aws_events as events,
    aws_events_targets as event_target,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_scheduler as scheduler,
)
from constructs import Construct
import json

class EventbridgeScheduleToEventbridgeCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## Add event bus, rule and target Lambda function
        event_bus = events.EventBus(self, "my-event-bus")

        my_lambda_function = _lambda.Function(
            self, 'MyLambdaFunction',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='index.handler',
            retry_attempts=0,
        )

        my_event_rule = events.Rule(self, 'my-event-rule',
            event_bus=event_bus,
            event_pattern=events.EventPattern(
                source=['scheduled.events']
            ),
        );

        my_event_rule.add_target(event_target.LambdaFunction(my_lambda_function))

        ## Create schedule role
        scheduler_role = iam.Role(self, "scheduler-role",
            assumed_by=iam.ServicePrincipal("scheduler.amazonaws.com"),
        )

        scheduler_events_policy = iam.PolicyStatement(
                actions=["events:PutEvents"],
                resources=[event_bus.event_bus_arn],
                effect=iam.Effect.ALLOW,
        )

        scheduler_role.add_to_policy(scheduler_events_policy)
        
        # Create a group for the schedule (maybe you want to add more scheudles to this group the future?)
        schedule_group = scheduler.CfnScheduleGroup(self, "my-schedule-group", 
            name="my-schedule-group",
        );

        ## Create schedule
        my_schedule = scheduler.CfnSchedule(self, "my-schedule",
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="OFF",
                ),
                schedule_expression="rate(5 minute)",
                group_name=schedule_group.name,
                target=scheduler.CfnSchedule.TargetProperty(
                    arn=event_bus.event_bus_arn,
                    role_arn=scheduler_role.role_arn,
                    event_bridge_parameters=scheduler.CfnSchedule.EventBridgeParametersProperty(
                        detail_type="ScheduleTriggered",
                        source="scheduled.events"
                    ),
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
        CfnOutput(self, "EVENT_BUS_NAME", value=event_bus.event_bus_name)
        CfnOutput(self, "LAMBDA_FUNCTION_NAME", value=my_lambda_function.function_name)
