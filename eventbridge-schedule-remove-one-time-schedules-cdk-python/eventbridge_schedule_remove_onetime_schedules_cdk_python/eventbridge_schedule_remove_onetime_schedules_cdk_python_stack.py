from aws_cdk import (
    CfnOutput,
    Duration,
    Stack,
    aws_iam as iam,
    aws_sns as _sns,
    aws_sns_subscriptions as snssubscriptions,
    aws_sqs as sqs,
    aws_scheduler as scheduler,
    aws_ec2 as ec2,    
    aws_lambda as _lambda,    
    aws_events as events,
)
from constructs import Construct

#use everybridge scheduler that runs every 5 minutes to remove one time eventbridge schedules completed and not used 
#add lambda to sns subscription 

class EventBridgeRemoveOnetimeSchedulesCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## Create SNS Topic
        my_sns_topic = _sns.Topic(self, "my-sns-topic")
        
        #subscribe an email to the sns topic (optional to replace command like option)
        # my_sns_topic.add_subscription(snssubscriptions.EmailSubscription("EMAIL-XXX"))

        ## Create schedule role
        scheduler_role = iam.Role(self, "scheduler-role",
            assumed_by=iam.ServicePrincipal("scheduler.amazonaws.com")
        )

        ## Create IAM policy
        scheduler_events_policy = iam.PolicyStatement(
                actions=["sns:Publish","lambda:InvokeFunction"],
                resources=[my_sns_topic.topic_arn],
                effect=iam.Effect.ALLOW,
        )
        


        ## Add IAM policy to schedule role
        scheduler_role.add_to_policy(scheduler_events_policy)

        scheduled_event_remover_lambda = _lambda.Function(self, "scheduledEventRemoverLambda",
                                                 runtime=_lambda.Runtime.PYTHON_3_9,
                                                 handler="scheduled_event_remover_lambda.lambda_handler",
                                                 code=_lambda.Code.from_asset("lambda"),
                                                 environment={'TOPIC_ARN': my_sns_topic.topic_arn},
                                                 timeout = Duration.seconds(600)
                                                 )
                                                 
        #add lambda to sns topic 
        my_sns_topic.grant_publish(scheduled_event_remover_lambda)

        event_policy = iam.PolicyStatement(effect=iam.Effect.ALLOW, resources=['*'], actions=['scheduler:*','sns:Publish'])
        scheduled_event_remover_lambda.add_to_role_policy(event_policy)

        ## Create IAM policy
        scheduler_scheduled_events_policy = iam.PolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=[scheduled_event_remover_lambda.function_arn],
                effect=iam.Effect.ALLOW,
        )
               
        scheduler_role.add_to_policy(scheduler_scheduled_events_policy)

        my_schedule_scheduled = scheduler.CfnSchedule(self, "my-schedule-scheduled",
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="OFF",
                ),
                
                schedule_expression="cron(0/5 * * * ? *)",
                schedule_expression_timezone="America/New_York",   
                target=scheduler.CfnSchedule.TargetProperty(
                    arn=scheduled_event_remover_lambda.function_arn,
                    role_arn=scheduler_role.role_arn,
                    input="{\"key\":\"my-schedule\"}"
                )

            )

    

        # Create schedule to send a message to SNS  once on a specific time 
        my_schedule_onetime1 = scheduler.CfnSchedule(self, "my-schedule-onetime1",
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="OFF",
                ),
                schedule_expression="at(2023-10-10T11:47:00)",
                schedule_expression_timezone="America/New_York",   
                target=scheduler.CfnSchedule.TargetProperty(
                    arn=my_sns_topic.topic_arn,
                    role_arn=scheduler_role.role_arn,
                    input="{\"key\":\"my-schedule-onetime1 removed\"}"
                )

            )


        # Create schedule to send a message to SNS  once on a specific time 
        my_schedule_onetime2 = scheduler.CfnSchedule(self, "my-schedule-onetime2",
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="OFF",
                ),
                schedule_expression="at(2023-10-10T11:47:00)",
                schedule_expression_timezone="America/New_York",   
                target=scheduler.CfnSchedule.TargetProperty(
                    arn=my_sns_topic.topic_arn,
                    role_arn=scheduler_role.role_arn,
                    input="{\"key\":\"my-schedule-onetime2 removed\"}"
                )

            )


        environment={ # ADD THIS, FILL IT FOR ACTUAL VALUE 
        "mysns_topic_arn": my_sns_topic.topic_arn,
        "testname": "testvalue"
        }



        ## CloudFormation Stack Outputs
        CfnOutput(self, "LAMBDA_REMOVE_SCHEDULED_EVENTS", value=scheduled_event_remover_lambda.function_arn)
        CfnOutput(self, "SCHEDULE_NAME", value=my_schedule_scheduled.ref)
        CfnOutput(self, "SCHEDULE_ONETIMENAME1", value=my_schedule_onetime1.ref)
        CfnOutput(self, "SCHEDULE_ONETIMENAME2", value=my_schedule_onetime2.ref)
        CfnOutput(self, "SNS_TOPIC_NAME", value=my_sns_topic.topic_arn)


