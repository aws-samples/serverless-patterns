import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_glue_alpha as glue_alpha,
    aws_glue as glue,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks
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

        output_bucket = s3.Bucket(self, "output-bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.DESTROY       
        )

        script_bucket = s3.Bucket(self, "script-bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.DESTROY       
        )

        s3deploy.BucketDeployment(self, "Deploy glue script",
            sources=[s3deploy.Source.asset("./lib/")],
            destination_bucket=script_bucket
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
            actions=["s3:GetObject"]
        ))

        input_crawler = glue.CfnCrawler(self, "input-crawler",
            name="input-crawler",
            role=input_crawler_role.role_arn,
            database_name=glue_db.database_name,
            targets={
                "s3Targets": [{"path": f"s3://{input_bucket.bucket_name}/"}]
            }
        )

        #Glue Job
        glue_job_role = iam.Role(self, "glue-job-role",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole"),
            ]
        )

        glue_job_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[f"{input_bucket.bucket_arn}/*", f"{script_bucket.bucket_arn}/*"],
            actions=["s3:GetObject"]
        ))

        glue_job_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[f"{output_bucket.bucket_arn}/*"],
            actions=["s3:PutObject"]
        ))

        glue_job = glue.CfnJob(self, 'Glue-job', name="Drop empty columns",
            role=glue_job_role.role_name,
            command=glue.CfnJob.JobCommandProperty(
                name='glueetl',
                script_location=f"s3://{script_bucket.bucket_name}/glue_job.py"
            ),
            glue_version="4.0"
        )

        #State machine
        crawler_input_task = tasks.GlueStartCrawlerRun(self, "Crawl input bucket", 
            crawler_name=input_crawler.name
        )

        job_task = tasks.GlueStartJobRun(self, "Run glue job",
            glue_job_name=glue_job.name,
            integration_pattern=sfn.IntegrationPattern.RUN_JOB,
            arguments=sfn.TaskInput.from_object({
                "--input_bucket": input_bucket.bucket_name,
                "--output_bucket": output_bucket.bucket_name
            })
        )

        definition = crawler_input_task.next(job_task)

        sfn_role = iam.Role(self, "state_machine_role",
            assumed_by=iam.ServicePrincipal("states.amazonaws.com")
        )

        sfn_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[f"arn:aws:glue:{self.region}:{self.account}:crawler/input_crawler"],
            actions=["glue:StartCrawler"],
        ))

        sfn_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[f"arn:aws:glue:{self.region}:{self.account}:job/{glue_job.name}"],
            actions=["glue:StartJobRun"],
        ))

        sfn_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=[
                "xray:PutTraceSegments",
                "xray:PutTelemetryRecords",
                "xray:GetSamplingRules",
                "xray:GetSamplingTargets"
            ],
        ))

        state_machine = sfn.StateMachine(self, "state-machine",
            definition_body=sfn.DefinitionBody.from_chainable(definition),
            role=sfn_role
        )

        #Eventbridge rules
        rule = events.Rule(self, "s3-create-object-event-rule",
            event_pattern=events.EventPattern(
                source=["aws.s3"],
                detail_type=["Object Created"]
            )
        )

        eb_role = iam.Role(self, "eb_role",
            assumed_by=iam.ServicePrincipal("events.amazonaws.com")
        )

        eb_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[state_machine.state_machine_arn],
            actions=["states:StartExecution"]
        ))

        rule.add_target(targets.SfnStateMachine(
            state_machine, 
            role=eb_role
        ))
