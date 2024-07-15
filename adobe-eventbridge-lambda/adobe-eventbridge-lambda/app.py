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

class AdobeIntegrationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #stack inputs
        ADOBE_PARTNER_EVENT_BUS = CfnParameter(self, id="adobeEventBusName", type="String",
            description="The name of event bus the Adobe Partner EventSource is associated with.")
        
        #turn partner event bus from string to EventBus object
        partner_event_bus = events.EventBus.from_event_bus_name(scope=self, id='partner-event-bus', event_bus_name=ADOBE_PARTNER_EVENT_BUS.value_as_string)

        # CloudWatch Logs Group that stores all events sent by Adobe for debugging or archive
        log_group = logs.LogGroup(
            self, "Adobe-all-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy=RemovalPolicy.DESTROY
        )

        # CloudWatch Logs Group that stores specific events from Adobe for debugging or archive
        log_group_order_events = logs.LogGroup(
            self, "Adobe-specific-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy=RemovalPolicy.DESTROY
        )

        lambda_role = iam.Role(scope=self, id='adobe-cdk-lambda-role',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    'service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        # A Lambda function to consume and process specific events
        adobe_process_order_events_lambda = _lambda.Function(
            self,
            id='AdobeProcessOrderEventsLambda',
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset('src'),
            handler='AdobeProcessOrderEvents.handler',
            role=lambda_role,
            timeout=Duration.seconds(15)
        )

        #EventBridge Adobe all events rule
        adobe_all_events_rule = events.Rule(
            self,
            id="AdobeAllEventsRule",
            event_bus=partner_event_bus
        )

        #add event pattern to rule
        adobe_all_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/developer.adobe.com.test'),
        )

        #CloudWatch Log Group as target for EventBridge Rule
        adobe_all_events_rule.add_target(targets.CloudWatchLogGroup(log_group))

        #EventBridge Adobe photoshop job status events
        adobe_order_events_rule = events.Rule(
            self,
            id="AdobeSpecificEventsRule",
            event_bus=partner_event_bus
        )

        #Add rule to the event bus for specific events change (ex. the status of a PhotoShop job)
        adobe_order_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/developer.adobe.com.test'),
            detail_type=["Imaging API Events:photoshop-job-status"],
            detail={
                "key": ["value"]
            }
        )

        # Lambda as target for EventBridge Rule
        adobe_order_events_rule.add_target(targets.LambdaFunction(adobe_process_order_events_lambda))

        #CloudWatch Log Group as target for EventBridge Rule
        adobe_order_events_rule.add_target(targets.CloudWatchLogGroup(log_group_order_events))

        # Print the Lambda function name
        CfnOutput(self, "AdobeProcessSpecificEventsLambdaOutput", value=adobe_process_order_events_lambda.function_name)

app = cdk.App()
description = (
    "Adobe EventBridge Integration (uksb-1tthgi812) (tag:adobe-eventbridge-lambda)"
)
AdobeIntegrationStack(app, "AdobeIntegrationStack", description=description)
app.synth()