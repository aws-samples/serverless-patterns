
from constructs import Construct
from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_iam as iam,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_glue as glue,
    aws_lambda as _lambda, CfnParameter
)


class CdkGlueStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # set the unique bucket name below
        s3_bucket_name = "my-glue-job-bucket";

        # Glue job execution IAM Role
        glue_job_role = iam.Role(
            self,
            'Glue-Job-Role',
            assumed_by=iam.ServicePrincipal('glue.amazonaws.com'),
            managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSGlueServiceRole')]
        )

        # S3 Bucket to host glue scripts
        bucket = s3.Bucket(self, "MyGlueJobBucket", bucket_name=s3_bucket_name,  versioned=True,
                           removal_policy=RemovalPolicy.DESTROY,
                           auto_delete_objects=True, block_public_access=s3.BlockPublicAccess.BLOCK_ALL)

        # asset to sync local scripts folder with S3 bucket
        asset = s3deploy.Source.asset("./assets")

        # Sync local scripts with S3 bucket
        s3deploy.BucketDeployment(self, "DeployGlueJobScripts",
                                  sources=[asset],
                                  destination_bucket=bucket,
                                  destination_key_prefix="glue-python-assets"
                                  )

        # Grant read write access for glue execution IAM role for S3 bucket
        bucket.grant_read_write(glue_job_role)

        script_location = 's3://' + bucket.bucket_name + '/glue-python-assets/script.py'

        # Glue-ETL  job
        job = glue.CfnJob(self, 'Glue-job', name='cdk-glue-etl-job',
                          role=glue_job_role.role_arn,
                          command=glue.CfnJob.JobCommandProperty(
                              name='glueetl',
                              script_location=script_location
                          ))

        my_lambda = _lambda.Function(
            self, 'GlueHandler',
            function_name="MyGlueHandler",
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('functions'),
            handler='glue.handler',
            environment={
                'JOB_NAME': job.name
            }
        )
        # Add InLine Policy to Lambda to provide access to start the jobs
        accountID = Stack.of(self).account
        region = Stack.of(self).region
        customPolicy = iam.PolicyStatement(
            actions=['glue:StartJobRun'],
            resources=[f"arn:aws:glue:{region}:{accountID}:job/{job.name}"]
        )

        my_lambda.role.attach_inline_policy(
            iam.Policy(self, "gluePolicyPermission", statements=[customPolicy])
        )

        # CDK Outputs
        CfnOutput(scope=self, id='LambdaFunctionName', value=my_lambda.function_name)
        CfnOutput(scope=self, id='GlueJobName', value=job.name)
        CfnOutput(scope=self, id='S3BucketName', value=bucket.bucket_name)


app = App()
CdkGlueStack(app, "CdkLambdaGlueS3Stack")
app.synth()
