from constructs import Construct
from aws_cdk import (
    Stack,
    Duration,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_rds as rds,
    aws_lambda as _lambda,
    # core
)
from aws_cdk.aws_lambda_event_sources import S3EventSource

class AuroraServerlessIngestionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creates a S3 Bucket
        s3bucket = s3.Bucket(self, "AuroraIngestionBucket")
        s3bucketarn = s3bucket.bucket_arn

        # Creates a new VPC
        vpc = ec2.Vpc(self, "VPC")
        vpc_cidr = vpc.vpc_cidr_block

        # Create a security group

        aurora_sg = ec2.SecurityGroup(self, "SecurityGroup", 
            vpc=vpc,
            description="Allow ssh access to aurora cluster",
            allow_all_outbound=True
        )
        aurora_sg.add_ingress_rule(
            ec2.Peer.ipv4(vpc_cidr),
            ec2.Port.tcp(3306)
        )

        # Creates a new Aurora Serverless database
        cluster = rds.ServerlessCluster(self, "MyAuroraCluster",
            engine = rds.DatabaseClusterEngine.AURORA_MYSQL,
            vpc = vpc,
            enable_data_api = True,
            default_database_name = "mydatabase",
            security_groups = [aurora_sg]
        )

        # Creates a IAM policy to be used by lambda
        my_custom_policy = iam.PolicyDocument(
            statements=[iam.PolicyStatement(
            actions=["s3-object-lambda:GetObject",
                    "s3-object-lambda:ListBucketMultipartUploads",
                    "s3-object-lambda:GetObjectRetention",
                    "s3-object-lambda:GetObjectLegalHold",
                    "s3-object-lambda:GetObjectAcl",
                    "s3-object-lambda:GetObjectTagging",
                    "s3-object-lambda:ListBucket",
                    "s3-object-lambda:GetObjectVersion",
                    "s3-object-lambda:ListBucketVersions",
                    "s3:ListBucketMultipartUploads",
                    "s3:ListAccessPoints",
                    "s3:ListJobs",
                    "s3:GetObject",
                    "s3:ListBucket",
                    "s3:ListBucketVersions",
                    "s3:ListAccessPointsForObjectLambda",
                    "rds-data:*",
                    "secretsmanager:GetResourcePolicy",
                    "secretsmanager:DescribeSecret",
                    "secretsmanager:GetSecretValue",      
                    "secretsmanager:ListSecretVersionIds",
                    "secretsmanager:GetRandomPassword",
                    "secretsmanager:ListSecrets",
                    "ec2:DescribeNetworkInterfaces",
                    "ec2:CreateNetworkInterface",
                    "ec2:DeleteNetworkInterface",
                    "ec2:DescribeInstances",
                    "ec2:AttachNetworkInterface"
            ],
            resources=["*"]
            )]
        )

        lambda_role = iam.Role(self, "LambdaDataIngestionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            description="Role to be assumed by lambda data ingestion",
            inline_policies = [my_custom_policy]
        )

        # Creates a lambda function to ingest data from S3 to Aurora

        fn = _lambda.Function(self, "Function",
            code=_lambda.Code.from_asset('./lambda'),
            runtime = _lambda.Runtime.PYTHON_3_9,
            handler = 'DataIngest.lambda_handler',
            vpc = vpc,
            timeout = Duration.seconds(600),
            role = lambda_role,
            # security_group =
            environment = {
                "BUCKET": s3bucketarn,
                "CLUSTER_ARN": cluster.cluster_arn,
                "SECRET_ARN": cluster.secret.secret_arn,
                "DATABASE": "mydatabase"
            }
        )

        # Add a S3 event to lambda
        fn.add_event_source(
            S3EventSource(s3bucket,
            events=[s3.EventType.OBJECT_CREATED]
        ))
