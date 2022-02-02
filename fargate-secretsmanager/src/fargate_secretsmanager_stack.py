import json
import aws_cdk as cdk
from constructs import Construct

from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_secretsmanager as sm,
    aws_iam as iam
)

class FargateSecretsManagerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Retrieve the first public subnet available in the default VPC in the AWS account. The subnet ID will be used to run a task
        fargate_vpc = ec2.Vpc.from_lookup(self, "Vpc", is_default=True)
        public_subnet = fargate_vpc.public_subnets[0]

        fargate_cluster = ecs.Cluster(self, "FargateCluster", cluster_name="FargateCluster", vpc=fargate_vpc)

        #Generate secret in Secrets Manager (in this example, the password is randomly generated)
        secret = sm.Secret(self, "FargateSecret",
            generate_secret_string=sm.SecretStringGenerator(
                secret_string_template=json.dumps({"username": "user"}),
                generate_string_key="password",
                include_space=False,
                require_each_included_type=True
              )
            )

        #Create Fargate Execution Role
        fargate_role = iam.Role(self, "FargateTaskExecutionRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            description="Fargate Task Execution Role",
            )

        fargate_task_def = ecs.FargateTaskDefinition(self, "FargateTaskDefinition",
            memory_limit_mib=1024,
            cpu=256,
            execution_role=fargate_role
            )

        fargate_container = fargate_task_def.add_container("FargateContainer",
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"),
            memory_limit_mib=512,
            logging=ecs.LogDrivers.aws_logs(stream_prefix="FargateDemo"),
            #Secrets are retrieved from AWS Secrets Manager at container start-up
            secrets={ 
                "USERNAME": ecs.Secret.from_secrets_manager(secret, "username"),
                "PASSWORD": ecs.Secret.from_secrets_manager(secret, "password")  #This syntax will reference a specific JSON field in the secret, i.e. 'password'. (Requires platform version 1.4.0 or later for Fargate tasks)
            },
            command=["printenv"]
        )

        #Print out resource names/ARNs for use in testing
        cdk.CfnOutput(self, "TaskDefinitionName", description="Name of Fargate Task Definition with version", value=fargate_task_def.task_definition_arn)
        cdk.CfnOutput(self, "Cluster", description="Cluster to run Fargate Tasks", value=fargate_cluster.cluster_name)
        cdk.CfnOutput(self, "Task Run Subnet", description="Subnet to run Fargate Tasks", value=public_subnet.subnet_id)