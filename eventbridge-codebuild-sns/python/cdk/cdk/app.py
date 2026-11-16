#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import (
    aws_s3,
    aws_events,
    aws_codebuild,
    aws_sns,
    aws_events_targets as targets,
    Stack
)
from constructs import Construct

class EventBridgeCodeBuildSNSStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create s3 bucket for artifacts
        artifacts_bucket = aws_s3.Bucket(self, "artifacts-bucket",
            block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            encryption=aws_s3.BucketEncryption.S3_MANAGED)

        # create codebuild project that executes a long-running script
        build_project = aws_codebuild.Project(self, "long-running-script-build-project",
                environment_variables={
                        "S3_ARTIFACTS_BUCKET": {
                            "value": artifacts_bucket.bucket_name
                        },
                        "S3_ARTIFACTS_OBJECT": {
                            "value": "script.py"
                        }
                    },
                environment=aws_codebuild.BuildEnvironment(
                    build_image=aws_codebuild.LinuxBuildImage.STANDARD_3_0,
                ),
                timeout=cdk.Duration.hours(1),
                build_spec=aws_codebuild.BuildSpec.from_object({
                    "version": "0.2",
                    "phases": {    
                        "install": {
                            "runtime-versions":{
                                "python": 3.8
                            }
                        },
                        "build": { 
                            "commands": [
                                "aws s3 cp s3://$S3_ARTIFACTS_BUCKET/$S3_ARTIFACTS_OBJECT $S3_ARTIFACTS_OBJECT",
                                "python $S3_ARTIFACTS_OBJECT"
                            ]
                        }
                    }
                }))
        # grant read access of the artifacts bucket to the codebuild role      
        artifacts_bucket.grant_read(build_project.role)

        # create eventbridge rule to trigger codebuild project
        long_running_script_rule =  aws_events.Rule(self, "long-running-script-build-trigger",
            schedule=aws_events.Schedule.rate(cdk.Duration.hours(1)))
        long_running_script_rule.add_target(targets.CodeBuildProject(build_project))

        # create sns topic as part of downstream services after codebuild project completes
        sns_topic = aws_sns.Topic(self, "script-completes-topic")

        # create eventbridge rule to publish to sns topic once codebuild project finishes (either succeeded, failed or stopped)
        codebuild_completes_rule = aws_events.Rule(self, "codebuild-scripts-complete-rule",
            event_pattern=aws_events.EventPattern(
                source=["aws.codebuild"],
                detail_type=["CodeBuild Build State Change"],
                detail={
                    "build-status": ["SUCCEEDED", "FAILED", "STOPPED"],
                    "project-name": [build_project.project_name]
                }
            )
            )
        codebuild_completes_rule.add_target(targets.SnsTopic(sns_topic))
    
        cdk.CfnOutput(self, "artifacts-bucket-output", value=artifacts_bucket.bucket_name)
        cdk.CfnOutput(self, "script-complete-topic-output", value=sns_topic.topic_arn)

app = cdk.App()
EventBridgeCodeBuildSNSStack(app, "EventBridgeCodeBuildSNSStack")

app.synth()
