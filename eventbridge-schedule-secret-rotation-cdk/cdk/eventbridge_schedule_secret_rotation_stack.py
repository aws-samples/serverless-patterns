import json
from aws_cdk import (
    CfnOutput,
    CfnParameter,
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_secretsmanager as secretsmanager,
    aws_events as events,
    aws_scheduler as scheduler
)
from constructs import Construct

class EventbridgeScheduleSecretRotationCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        param_rotation_schedule = CfnParameter(self, "SecretRotationSchedule",
                description="Secret rotation schedule (cron or rate)",
                default="cron(0 0/1 * * ? *)"
            )
        
        secret = secretsmanager.CfnSecret(self, "Secret",
                    secret_string = json.dumps({"value":"initial_value"}),
                    name=f'secret-rotation-demo-secret',
                    description = "Secret Rotation Demo secret")
        
        rotation_lambda = self.create_rotation_lambda(secret)

        self.setup_rotation_schedule(param_rotation_schedule, rotation_lambda)

        CfnOutput(self, "SecretArn", 
                  value=secret.attr_id)

        CfnOutput(self, "SecretRotationLambdaArn",
                  value=rotation_lambda.function_arn)  
        
        CfnOutput(self, "RotationSchedule",
                  value=str(param_rotation_schedule.value_as_string))

    def create_rotation_lambda(self, secret):
        
        rotation_lambda_role = iam.Role(self, "secret-rotator-lambda-role",
                    role_name = f"secret-rotator-lambda-role",
                    assumed_by = iam.ServicePrincipal("lambda.amazonaws.com"),
                    managed_policies = [
                        iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
                    ],
                    inline_policies = {
                        "secret-rotator-policy": 
                            iam.PolicyDocument(                            
                                statements = [
                                    iam.PolicyStatement(
                                        actions = ["secretsmanager:DescribeSecret",
                                                "secretsmanager:GetSecretValue", 
                                                "secretsmanager:PutSecretValue",
                                                "secretsmanager:UpdateSecretVersionStage"],
                                        resources = [secret.attr_id]
                                    ),
                                    iam.PolicyStatement(
                                        actions = ["events:PutEvents"],
                                        resources = [f"arn:aws:events:{Stack.of(self).region}:{Stack.of(self).account}:event-bus/default"])
                                ]
                            )
                    }
                )

        rotation_lambda = lambda_.Function(self, "secret-rotation-lambda",
                role=rotation_lambda_role,
                code=lambda_.Code.from_asset("src//lambda"),
                handler="rotation_lambda.lambda_handler",
                runtime=lambda_.Runtime.PYTHON_3_11,
                environment={
                    "SECRET_ID": secret.attr_id
                },
                timeout=Duration.seconds(120)
            )
        
        lambda_.CfnPermission(self, "events-permission-on-rotator-lambda",
            action="lambda:InvokeFunction",
            function_name=rotation_lambda.function_name,
            principal="events.amazonaws.com")
                    
        return rotation_lambda
    
    def setup_rotation_schedule(self, param_rotation_schedule, rotation_lambda):
        scheduler_role = iam.Role(self, "secret-rotation-scheduler-role",
                    role_name = f"secret-rotation-scheduler-role",
                    assumed_by = iam.ServicePrincipal("scheduler.amazonaws.com"),
                    inline_policies = {
                        "secret-rotation-scheduler-policy":
                            iam.PolicyDocument(
                                statements = [
                                    iam.PolicyStatement(
                                        actions = ["lambda:InvokeFunction"],
                                        resources = [rotation_lambda.function_arn]
                                    )
                                ]
                            )
                    }
                )
        scheduler.CfnSchedule(self, "secret-rotation-scheduler",
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="OFF"
                ),
                schedule_expression=param_rotation_schedule.value_as_string,
                target=scheduler.CfnSchedule.TargetProperty(
                    arn=rotation_lambda.function_arn,
                    role_arn=scheduler_role.role_arn,
                    retry_policy=scheduler.CfnSchedule.RetryPolicyProperty(
                        maximum_retry_attempts=0,
                        maximum_event_age_in_seconds=5 * 60
                    )
                )
            )