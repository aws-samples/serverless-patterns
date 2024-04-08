import json
from aws_cdk import (
    Stack,
    aws_ssm as ssm,
    aws_iam as iam,
    aws_scheduler as scheduler
)
from constructs import Construct

class EventbridgeSchedulerSsmCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create an association to update SSM agent on all instances
        cfnAssociation = ssm.CfnAssociation(self, "SSMAssociation",
            name="AWS-UpdateSSMAgent",
            association_name="UpdateSSMAgent",
            targets=[ssm.CfnAssociation.TargetProperty(
                key="instanceids",
                values=['*']
            )],
            wait_for_success_timeout_seconds=120)
        
        # create a role and a policy to allow running associations
        schedulerRole = iam.Role(self, 'scheduler-role',
            assumed_by=iam.ServicePrincipal('scheduler.amazonaws.com'))
        
        schedulerRole.add_to_policy(iam.PolicyStatement(
            resources=['*'],
            actions=['ssm:StartAssociationsOnce']
        ))

        # schedule to run every Sunday at 2:00am
        schedule = scheduler.CfnSchedule(self, 'run-command',
            flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                mode="OFF"
            ),
            schedule_expression='cron(0 2 ? * SUN *)',
            target=scheduler.CfnSchedule.TargetProperty(
                    arn='arn:aws:scheduler:::aws-sdk:ssm:startAssociationsOnce',
                    role_arn=schedulerRole.role_arn,
                    input=json.dumps({"AssociationIds": [cfnAssociation.attr_association_id]})
            )
        )


        
