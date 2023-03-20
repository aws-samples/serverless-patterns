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
    Duration
)

from constructs import Construct

class InspectorCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # CloudWatch Logs Group
        log_group = logs.LogGroup(
            self, "InitialScanLogs",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy = RemovalPolicy.DESTROY
        )

        # CloudWatch Logs Group
        log_group_findings = logs.LogGroup(
            self, "FindingsLogs",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy = RemovalPolicy.DESTROY
        )

        # S3 bucket that stores inspector initial scans and inspector findings
        inspector_results_bucket = s3.Bucket(
            self, 
            "InspectorResultsBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            encryption=s3.BucketEncryption.S3_MANAGED
        )

        lambda_role = iam.Role(scope=self, id='cdk-lambda-role',
            assumed_by =iam.ServicePrincipal('lambda.amazonaws.com'),
            role_name='cdk-lambda-role',
            managed_policies=[
            iam.ManagedPolicy.from_aws_managed_policy_name(
                'service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        lambda_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[inspector_results_bucket.bucket_arn, inspector_results_bucket.bucket_arn + "/*"],
            actions=[
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ]
        ))

         #Initial Scans Processing Lambda function
        inspector_initial_scan_lambda = _lambda.Function(
            self, 
            id='InspectorInitialScanLambda',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('src'),
            handler='InspectorInitialScan.handler',
            role=lambda_role,
            timeout=Duration.seconds(30),
            environment={"S3_BUCKET": inspector_results_bucket.bucket_name}
        )

        #Findings Processing Lambda function
        inspector_findings_lambda = _lambda.Function(
            self, 
            id='InspectorFindingsLambda',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('src'),
            handler='InspectorFindings.handler',
            role=lambda_role,
            timeout=Duration.seconds(30),
            environment={"S3_BUCKET": inspector_results_bucket.bucket_name, "QS_TAG":"QuickStartID"}
        )

        #EventBridge Initial Scan Rule
        init_scan_rule = events.Rule(
            self, "InspectorInitialScanRule"        
            )

        #add event pattern to rule
        init_scan_rule.add_event_pattern(
            source=["aws.inspector2"],
            detail_type=["Inspector2 Scan"]
        )

        # Lambda as target for EventBridge Rule
        init_scan_rule.add_target(targets.LambdaFunction(inspector_initial_scan_lambda))

        #CloudWatch Log Group as target for EventBridge Rule
        init_scan_rule.add_target(targets.CloudWatchLogGroup(log_group))


        #EventBridge Findings Rule
        findings_rule = events.Rule(
            self, "InspectorFindingsRule"
        )

        #add event pattern to rule
        findings_rule.add_event_pattern(
            source=["aws.inspector2"],
            detail_type=["Inspector2 Finding"]
        )

        # Lambda as target for EventBridge Rule
        findings_rule.add_target(targets.LambdaFunction(inspector_findings_lambda))

        #CloudWatch Log Group as target for EventBridge Rule
        findings_rule.add_target(targets.CloudWatchLogGroup(log_group_findings))


app = cdk.App()
InspectorCdkStack(app, "InspectorCdkStack")

app.synth()
