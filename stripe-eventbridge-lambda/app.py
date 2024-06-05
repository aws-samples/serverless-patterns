
import os
import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_logs as logs,
    CfnOutput,
    CfnParameter,
    Duration,
    RemovalPolicy
)
from constructs import Construct

class StripeIntegrationStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Stack inputs
        STRIPE_PARTNER_EVENT_BUS = CfnParameter(
            self, id="stripeEventBusName", type="String",
            description="The name of event bus the the Stripe Partner EventSource is associated with."
        )

        # Turn partner event bus from string to IEventBus object
        partner_event_bus = events.EventBus.from_event_bus_name(
            scope=self, id='partner-event-bus', event_bus_name=STRIPE_PARTNER_EVENT_BUS.value_as_string
        )

        # CloudWatch Logs Group that stores all events sent by Stripe for debugging or archive
        log_group_all_events = logs.LogGroup(
            self, "Stripe-all-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy=RemovalPolicy.DESTROY
        )

        # CloudWatch Logs Group that stores all failed payment events from Stripe for debugging or archive
        log_group_failed_payments = logs.LogGroup(
            self, "Stripe-failedpayment-events",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy=RemovalPolicy.DESTROY
        )

        lambda_role = iam.Role(
            scope=self, id='stripe-cdk-lambda-role',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    'service-role/AWSLambdaBasicExecutionRole'
                )
            ]
        )

        # DynamoDB table to store failed payment events
        stripe_failed_payments_table = dynamodb.Table(
            self, "StripeFailedPaymentsTable",
            partition_key=dynamodb.Attribute(name="payment_intent_id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )

        # A Lambda function to consume and process failed payment events
        stripe_process_failed_payment_lambda = _lambda.Function(
            self,
            id='StripeProcessFailedPaymentLambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('src'),
            handler='StripeProcessFailedPayment.handler',
            role=lambda_role,
            timeout=Duration.seconds(15),
            environment={
                "StripeFailedPayments": stripe_failed_payments_table.table_name
            }
        )

        # EventBridge Stripe all events rule
        stripe_all_events_rule = events.Rule(
            self,
            id="StripeAllEventsRule",
            event_bus=partner_event_bus
        )

        # Add event pattern to rule
        stripe_all_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/stripe.com')
        )

        # CloudWatch Log Group as target for EventBridge Rule
        stripe_all_events_rule.add_target(targets.CloudWatchLogGroup(log_group_all_events))

        # EventBridge Stripe failed payment events
        stripe_failed_payment_events_rule = events.Rule(
            self,
            id="StripeFailedPaymentEventsRule",
            event_bus=partner_event_bus
        )

        # Add rule to the event bus for the "failed_payment" pattern
        stripe_failed_payment_events_rule.add_event_pattern(
            source=events.Match.prefix('aws.partner/stripe.com'),
            detail_type=["charge.failed"],
        )

        # Lambda as target for EventBridge Rule
        stripe_failed_payment_events_rule.add_target(targets.LambdaFunction(stripe_process_failed_payment_lambda))

        # CloudWatch Log Group as target for EventBridge Rule
        stripe_failed_payment_events_rule.add_target(targets.CloudWatchLogGroup(log_group_failed_payments))

        # Output the IAM role ARN for the Lambda function
        CfnOutput(self, "StripeProcessFailedPaymentLambdaOutput", value=stripe_process_failed_payment_lambda.function_name)

        # Output the DynamoDB table name
        CfnOutput(self, "StripeFailedPaymentsTableOutput", value=stripe_failed_payments_table.table_name)

app = cdk.App()
description = "Stripe EventBridge Integration"
StripeIntegrationStack(app, "StripeIntegrationStack", description=description)
app.synth()