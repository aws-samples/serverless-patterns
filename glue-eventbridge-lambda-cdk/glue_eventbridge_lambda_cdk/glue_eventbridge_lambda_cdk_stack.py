from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_events as events,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_glue as glue,
    aws_events_targets as targets
)

from constructs import Construct

class GlueEventBridgeLambda(Stack):

    S3_BUCKET_NAME = "CdkGlueJobBucket"

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda function
        lambda_fn = _lambda.Function(
            self, "LambdaFunctionFromEventBridge",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambdaFunctionFromEventBridge.handler",
            code=_lambda.Code.from_asset("lambda_fns"),
        )

        # EventBridge Rule
        rule = events.Rule(
            self, "Rule",
        )

        rule.add_event_pattern(
            source=["aws.glue"],
            detail_type=["Glue Job State Change"],
            detail={
                "jobName":["cdk-python-streaming-glue-job"],
                "state": ["TIMEOUT"]
            }
        )
        
        rule.add_target(targets.LambdaFunction(lambda_fn))

        # Glue job execution IAM Role      
        glue_job_role = iam.Role(
            self,
            'Glue-Job-Role',
            assumed_by=iam.ServicePrincipal('glue.amazonaws.com'),
            managed_policies = [iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSGlueServiceRole')]
        )

         # S3 Bucket to host glue scripts
        bucket = s3.Bucket(self, self.S3_BUCKET_NAME, versioned=True, removal_policy=RemovalPolicy.DESTROY,
                    auto_delete_objects=True, block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
        
        # Grant read write access for glue execution IAM role for S3 bucket
        bucket.grant_read_write(glue_job_role)

        # asset to sync local scripts folder with S3 bucket
        asset = s3deploy.Source.asset("./glue-scripts")

        # Sync local scripts with S3 bucket
        s3deploy.BucketDeployment(self, "DeployGlueJobScripts",
            sources=[asset],
            destination_bucket=bucket,
            destination_key_prefix="glue-python-scripts"
            )
        
        scriptLocation = 's3://'+bucket.bucket_name+'/glue-python-scripts/glue-streaming-job.py'
        
        # Glue Streaming Job
        job = glue.CfnJob(self,'Glue-job', name = 'cdk-python-streaming-glue-job',
            role=glue_job_role.role_arn,
            command=glue.CfnJob.JobCommandProperty(
                name='gluestreaming',
                python_version='3',
                script_location=scriptLocation
                ),
            default_arguments={
                "--bucket_name": bucket.bucket_name
                },
            execution_property=glue.CfnJob.ExecutionPropertyProperty(
                max_concurrent_runs=1
                ),
            timeout=1,
            worker_type='G.025X',
            number_of_workers=2,
            glue_version='3.0'
            )

        CfnOutput(scope=self, id='GlueJobName', value=job.name)
        CfnOutput(scope=self, id='S3BucketName', value=bucket.bucket_name)
