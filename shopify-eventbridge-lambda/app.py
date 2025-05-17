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

class ShopifyIntegrationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Stack inputs
        SHOPIFY_PARTNER_EVENT_BUS = CfnParameter(self, id="shopifyEventBusName", type="String",
            description="The name of event bus the Shopify Partner EventSource is associated with.")
        
        # Turn partner event bus from string to IEventBus object
        partner_event_bus = events.EventBus.from_event_bus_name(scope=self, id='partner-event-bus', event_bus_name=SHOPIFY_PARTNER_EVENT_BUS.value_as_string)

        # CloudWatch Logs Group that stores all events sent by Shopify for debugging or archive
        log_group = logs.LogGroup(
            self, "Shopify-all-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy=RemovalPolicy.DESTROY
        )

        # CloudWatch Logs Group that stores specific events from Shopify for debugging or archive
        log_group_product_updated = logs.LogGroup(
            self, "Shopify-product-updated-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy=RemovalPolicy.DESTROY
        )

        lambda_role = iam.Role(scope=self, id='shopify-cdk-lambda-role',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    'service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        # A Lambda function to consume and process specific events
        shopify_process_product_updated_events_lambda = _lambda.Function(
            self,
            id='ShopifyProcessProductUpdatedLambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('src'),
            handler='ShopifyProcessProductUpdated.handler',
            role=lambda_role,
            timeout=Duration.seconds(15)
        )

        # EventBridge Shopify all events rule
        shopify_all_events_rule = events.Rule(
            self,
            id="ShopifyAllEventsRule",
            event_bus=partner_event_bus
        )

        # Add event pattern to rule
        shopify_all_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/shopify.com'),
        )

        # CloudWatch Log Group as target for EventBridge Rule
        shopify_all_events_rule.add_target(targets.CloudWatchLogGroup(log_group))

        # EventBridge Shopify product updated events
        shopify_product_updated_rule = events.Rule(
            self,
            id="ShopifyProductUpdatedEventsRule",
            event_bus=partner_event_bus
        )

        # Add rule to the event bus for specific events  
        shopify_product_updated_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/shopify.com/shop-event-bus'),
            detail_type=["shopifyWebhook"],
            detail={
                "metadata": {
                    "X-Shopify-Topic": ["products/update"]
                }
            }
        )

        # Lambda as target for EventBridge Rule
        shopify_product_updated_rule.add_target(targets.LambdaFunction(shopify_process_product_updated_events_lambda))

        # CloudWatch Log Group as target for EventBridge Rule
        shopify_product_updated_rule.add_target(targets.CloudWatchLogGroup(log_group_product_updated))

        # Print the Lambda function name
        CfnOutput(self, "ShopifyProductUpdatedEventsLambdaOutput", value=shopify_process_product_updated_events_lambda.function_name)

app = cdk.App()
description = (
    "Shopify EventBridge Integration (uksb-1tthgi812) (tag:shopify-eventbridge-lambda)"
)
ShopifyIntegrationStack(app, "ShopifyIntegrationStack", description=description)
app.synth()