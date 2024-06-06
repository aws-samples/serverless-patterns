import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_events as events,
    aws_iam as iam,
    aws_glue_alpha as glue_alpha,
    aws_glue as glue,
    aws_s3 as s3,
)
from constructs import Construct

class S3EventbridgeGluecrawlerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #S3 buckets
        input_bucket = s3.Bucket(self, "input-bucket",
            event_bridge_enabled=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.DESTROY       
        )

        #Eventbridge rules
        rule = events.Rule(self, "s3-create-object-event-rule",
            event_pattern=events.EventPattern(
                source=["aws.s3"],
                detail_type=["Object Created"]
            )
        )

        #Glue crawler and database
        glue_db = glue_alpha.Database(self, "s3_eventbridge_glue_db",
            database_name="s3_eventbridge_glue_db",
            description="Database to store the results of the glue crawler"
        )

        input_crawler_role = iam.Role(self, "input-crawler-role",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole"),
            ]
        )

        input_crawler_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[f"{input_bucket.bucket_arn}*"],
            actions=["s3:GetObject", "s3:PutObject"]
        ))

        input_crawler = glue.CfnCrawler(self, "input-crawler",
            name="input-crawler",
            role=input_crawler_role.role_arn,
            database_name=glue_db.database_name,
            targets={
                "s3Targets": [{"path": f"s3://{input_bucket.bucket_name}/"}]
            }
        )

        #State machine
    
