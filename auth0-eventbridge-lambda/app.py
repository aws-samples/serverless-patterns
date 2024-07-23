#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    RemovalPolicy,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_logs as logs,
    Duration,
    CfnParameter,
    CfnOutput
)

from constructs import Construct

class Auth0IntegrationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #stack inputs
        AUTH0_PARTNER_EVENT_BUS = CfnParameter(self,id="auth0EventBusName", type="String",
            description="The name of event bus the the Auth0 Partner EventSource is associated with.")
        
        #turn partner event bus from string to IEventBus object
        partner_event_bus = events.EventBus.from_event_bus_name(scope=self,id='partner-event-bus',event_bus_name=AUTH0_PARTNER_EVENT_BUS.value_as_string)

        # CloudWatch Logs Group that stores all events sent by Auth0 debugging or archive
        log_group = logs.LogGroup(
            self, "Auth0-all-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy = RemovalPolicy.DESTROY
        )

        # CloudWatch Logs Group that stores all failed login events from Auth0 for debugging or archive
        log_group_failed_logins = logs.LogGroup(
            self, "Auth0-failedlogin-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy = RemovalPolicy.DESTROY
        )

        lambda_role = iam.Role(scope=self, id='auth0-cdk-lambda-role',
            assumed_by =iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
            iam.ManagedPolicy.from_aws_managed_policy_name(
                'service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        # A Lambda function to consume and process failed login events 
        auth0_process_failed_login_lambda = _lambda.Function(
            self, 
            id='Auth0ProcessFailedLoginLambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('src'),
            handler='Auth0ProcessFailedLogin.handler',
            role=lambda_role,
            timeout=Duration.seconds(15)
        )

        #EventBridge Auth0 all events rule
        auth0_all_events_rule = events.Rule(
            self,
            id="Auth0AllEventsRule", 
            event_bus=partner_event_bus     
            )

        #add event pattern to rule
        auth0_all_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/auth0.com'),
        )

        #CloudWatch Log Group as target for EventBridge Rule
        auth0_all_events_rule.add_target(targets.CloudWatchLogGroup(log_group))


        #EventBridge Auth0 failed login events
        auth0_failed_login_events_rule = events.Rule(
            self, 
            id="Auth0FailedLoginEventsRule",
            event_bus=partner_event_bus     
        )

        #Add rule to the event bus for the "limit_wc" pattern created above
        auth0_failed_login_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/auth0.com'),
            detail_type=["Auth0 log"],
            detail={
                "connection": ["Username-Password-Authentication"],
                "type":["limit_wc"]
            }
        )

        # Lambda as target for EventBridge Rule
        auth0_failed_login_events_rule.add_target(targets.LambdaFunction(auth0_process_failed_login_lambda))

        #CloudWatch Log Group as target for EventBridge Rule
        auth0_failed_login_events_rule.add_target(targets.CloudWatchLogGroup(log_group_failed_logins))

        # print the IAM role arn for this service account
        CfnOutput(self, "Auth0ProcessFailedLoginLambdaOutput", value=auth0_process_failed_login_lambda.function_name)

app = cdk.App()
description = (
    "Auth0 EventBridge Integration (uksb-1tthgi812) (tag:auth0-eventbridge-lambda)"
)
Auth0IntegrationStack(app, "Auth0IntegrationStack", description=description)
app.synth()
