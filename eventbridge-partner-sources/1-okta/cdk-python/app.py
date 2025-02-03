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

class OktaIntegrationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Stack inputs
        OKTA_PARTNER_EVENT_BUS = CfnParameter(self, id="oktaEventBusName", type="String",
            description="The name of event bus the Okta Partner EventSource is associated with.")
        
        # Turn partner event bus from string to IEventBus object
        partner_event_bus = events.EventBus.from_event_bus_name(scope=self, id='partner-event-bus', event_bus_name=OKTA_PARTNER_EVENT_BUS.value_as_string)

        # CloudWatch Logs Group that stores all events sent by Okta for debugging or archive
        log_group = logs.LogGroup(
            self, "Okta-all-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy=RemovalPolicy.DESTROY
        )

        # CloudWatch Logs Group that stores specific login location events from Okta for debugging or archive
        log_group_user_login_unusual_location_app = logs.LogGroup(
            self, "Okta-user-login-unusual-location-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy=RemovalPolicy.DESTROY
        )

        lambda_role = iam.Role(scope=self, id='okta-cdk-lambda-role',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    'service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        # A Lambda function to consume and process specific events
        okta_process_user_login_unusual_location_events_lambda = _lambda.Function(
            self,
            id='OktaProcessUserLoginUnusualLocation',
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset('src'),
            handler='OktaProcessUserLoginUnusualLocation.handler',
            role=lambda_role,
            timeout=Duration.seconds(15)
        )

        # EventBridge Okta all events rule
        okta_all_events_rule = events.Rule(
            self,
            id="OktaAllEventsRule",
            event_bus=partner_event_bus
        )

        # Add event pattern to rule
        okta_all_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/okta.com/evership/evershipsecuritylake'),
        )

        # CloudWatch Log Group as target for EventBridge Rule
        okta_all_events_rule.add_target(targets.CloudWatchLogGroup(log_group))

        # EventBridge Okta user unusual login location events
        okta_user_access_admin_app_rule = events.Rule(
            self,
            id="OktaUnusualLoginEventsRule",
            event_bus=partner_event_bus
        )

        # Add rule to the event bus for specific events  
        okta_user_access_admin_app_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/okta.com/evership/evershipsecuritylake'),
            detail_type=["SystemLog"],
            detail={
                "eventType": ["user.session.access_admin_app"]
            }
        )

        # Lambda as target for EventBridge Rule
        okta_user_access_admin_app_rule.add_target(targets.LambdaFunction(okta_process_user_login_unusual_location_events_lambda))

        # CloudWatch Log Group as target for EventBridge Rule
        okta_user_access_admin_app_rule.add_target(targets.CloudWatchLogGroup(log_group_user_login_unusual_location_app))

        # Print the Lambda function name
        CfnOutput(self, "OktaProcessUserLoginUnusualLocationLambdaOutput", value=okta_process_user_login_unusual_location_events_lambda.function_name)

app = cdk.App()
description = (
    "Okta EventBridge Integration (uksb-1tthgi812) (tag:eventbridge-partner-sources-okta-cdk-python)"
)
OktaIntegrationStack(app, "OktaIntegrationStack", description=description)
app.synth()
