from aws_cdk import (
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_lambda as _lambda,
)
from constructs import Construct


class LambdaManagedInstancesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Step 1: Create the required IAM roles (following instructions exactly)
        
        # Lambda execution role
        lambda_execution_role = iam.Role(
            self, "LambdaExecutionRole",
            role_name="MyLambdaExecutionRolePython",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # Capacity provider operator role
        capacity_provider_operator_role = iam.Role(
            self, "CapacityProviderOperatorRole",
            role_name="MyCapacityProviderOperatorRolePython",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaManagedEC2ResourceOperator")
            ]
        )

        # Step 2: Set up VPC resources (following instructions exactly)
        
        # Create VPC with CIDR 10.0.0.0/16
        vpc = ec2.Vpc(
            self, "LambdaManagedInstancesVpc",
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            max_azs=1,  # Instructions show single subnet
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    cidr_mask=24,
                    name="lambda-subnet",
                    subnet_type=ec2.SubnetType.PUBLIC,  # Instructions create in public for simplicity
                )
            ],
            nat_gateways=0  # No NAT needed for public subnet
        )

        # Create security group (following instructions exactly)
        security_group = ec2.SecurityGroup(
            self, "LambdaManagedInstancesSecurityGroup",
            vpc=vpc,
            description="Security group for Lambda Managed Instances",
            security_group_name="my-capacity-provider-sg-python"
        )

        # Step 3: Create capacity provider (using native CDK L1 construct)
        capacity_provider = _lambda.CfnCapacityProvider(
            self, "CapacityProvider",
            capacity_provider_name="my-capacity-provider-python",
            vpc_config={
                "subnetIds": [vpc.public_subnets[0].subnet_id],
                "securityGroupIds": [security_group.security_group_id]
            },
            permissions_config={
                "capacityProviderOperatorRoleArn": capacity_provider_operator_role.role_arn
            },
            instance_requirements={
                "architectures": ["x86_64"]
            },
            capacity_provider_scaling_config={
                "maxVCpuCount": 30
            }
        )

        # Step 4: Create Lambda function with managed instances
        managed_instance_function = _lambda.CfnFunction(
            self, "ManagedInstanceFunction",
            function_name="my-managed-instance-function-python",
            runtime="python3.13",  # Using python3.13 as requested  
            handler="index.handler",
            code={
                "zipFile": """
import json

def handler(event, context):
    print('Event:', json.dumps(event, indent=2))
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Lambda Managed Instances!',
            'event': event
        })
    }
"""
            },
            role=lambda_execution_role.role_arn,
            architectures=["x86_64"],
            memory_size=2048,
            ephemeral_storage={
                "size": 512
            },
            capacity_provider_config={
                "lambdaManagedInstancesCapacityProviderConfig": {
                    "capacityProviderArn": capacity_provider.capacity_provider_ref.capacity_provider_arn
                }
            }
        )

        # Step 5: Publish function version (following instructions exactly)
        function_version = _lambda.CfnVersion(
            self, "ManagedInstanceFunctionVersion",
            function_name=managed_instance_function.ref,
            description="Version 1 of Lambda Managed Instance function"
        )

        # Outputs (matching the instructions)
        CfnOutput(
            self, "VpcId",
            value=vpc.vpc_id,
            description="VPC ID for Lambda Managed Instances"
        )

        CfnOutput(
            self, "SubnetId",
            value=vpc.public_subnets[0].subnet_id,
            description="Subnet ID for Lambda Managed Instances"
        )

        CfnOutput(
            self, "SecurityGroupId",
            value=security_group.security_group_id,
            description="Security Group ID for Lambda Managed Instances"
        )

        CfnOutput(
            self, "LambdaFunctionName",
            value=managed_instance_function.ref,
            description="Lambda function name"
        )

        CfnOutput(
            self, "LambdaFunctionArn",
            value=managed_instance_function.attr_arn,
            description="Lambda function ARN"
        )

        CfnOutput(
            self, "CapacityProviderOperatorRoleArn",
            value=capacity_provider_operator_role.role_arn,
            description="Capacity Provider Operator Role ARN"
        )