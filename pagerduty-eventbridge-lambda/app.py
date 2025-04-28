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

class PagerdutyIntegrationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #stack inputs
        PAGERDUTY_PARTNER_EVENT_BUS = CfnParameter(self,id="pagerdutyEventBusName", type="String",
            description="The name of event bus the the PagerDuty Partner EventSource is associated with.")
        
        #turn partner event bus from string to IEventBus object
        partner_event_bus = events.EventBus.from_event_bus_name(scope=self,id='partner-event-bus',event_bus_name=PAGERDUTY_PARTNER_EVENT_BUS.value_as_string)

        # CloudWatch Logs Group that stores all events sent by PagerDuty debugging or archive
        log_group = logs.LogGroup(
            self, "Pagerduty-all-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy = RemovalPolicy.DESTROY
        )

        # CloudWatch Logs Group that stores all incident acknowledgement events from PagerDuty for debugging or archive
        log_group_acknowledgements = logs.LogGroup(
            self, "Pagerduty-acknowledgement-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy = RemovalPolicy.DESTROY
        )

        lambda_role = iam.Role(scope=self, id='pagerduty-cdk-lambda-role',
            assumed_by =iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
            iam.ManagedPolicy.from_aws_managed_policy_name(
                'service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        # A Lambda function to consume and process incident acknowledgement events 
        pagerduty_acknowledgement_lambda = _lambda.Function(
            self, 
            id='PagerdutyAcknowledgementLambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('src'),
            handler='PagerdutyAcknowledgement.handler',
            role=lambda_role,
            timeout=Duration.seconds(15)
        )

        #EventBridge Auth0 all events rule
        pagerduty_all_events_rule = events.Rule(
            self,
            id="PagerdutyAllEventsRule", 
            event_bus=partner_event_bus     
            )

        #add event pattern to rule
        pagerduty_all_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/pagerduty.com'),
        )

        #CloudWatch Log Group as target for EventBridge Rule
        pagerduty_all_events_rule.add_target(targets.CloudWatchLogGroup(log_group))


        #EventBridge PagerDuty acknowledgement events
        pagerduty_acknowledgement_events_rule = events.Rule(
            self, 
            id="PagerdutyAcknowledgementEventsRule",
            event_bus=partner_event_bus     
        )

        #Add rule to the event bus for the "limit_wc" pattern created above
        pagerduty_acknowledgement_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/pagerduty.com'),
            detail_type=["PagerDuty log"],
            detail={
                "connection": ["Username-Password-Authentication"],
                "type":["limit_wc"]
            }
        )

        # Lambda as target for EventBridge Rule
        pagerduty_acknowledgement_events_rule.add_target(targets.LambdaFunction(pagerduty_acknowledgement_lambda))

        #CloudWatch Log Group as target for EventBridge Rule
        pagerduty_acknowledgement_events_rule.add_target(targets.CloudWatchLogGroup(log_group_acknowledgements))

        # print the IAM role arn for this service account
        CfnOutput(self, "PagerdutyAcknowledgementLambdaOutput", value=pagerduty_acknowledgement_lambda.function_name)

app = cdk.App()
description = (
    "PagerDuty EventBridge Integration (uksb-1tthgi812) (tag:pagerduty-eventbridge-lambda)"
)
PagerDutyIntegrationStack(app, "PagerDutyIntegrationStack", description=description)
app.synth()
