import os

from aws_cdk import (
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_ssm as ssm, RemovalPolicy,

)
from constructs import Construct


class CdkMSKServerlessVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # VPC
        vpc = ec2.Vpc(self, "VPC",
                      nat_gateways=0,
                      subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
                      )

        # AMI
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        # Instance Role and SSM Managed Policy
        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))

        # Instance
        instance = ec2.Instance(self, "Instance",
                                instance_type=ec2.InstanceType("t3.nano"),
                                machine_image=amzn_linux,
                                vpc = vpc,
                                role = role
                                )

        # Script in S3 as Asset
        # asset = Asset(self, "Asset", path=os.path.join(dirname, "configure.sh"))
        # local_path = instance.user_data.add_s3_download_command(
        #     bucket=asset.bucket,
        #     bucket_key=asset.s3_object_key
        # )
        #
        # # Userdata executes script from S3
        # instance.user_data.add_execute_file_command(
        #     file_path=local_path
        # )
        # asset.grant_read(instance.role)
        multipart_user_data = ec2.MultipartUserData()
        commands_user_data = ec2.UserData.for_linux()
        multipart_user_data.add_user_data_part(commands_user_data, ec2.MultipartBody.SHELL_SCRIPT, True)

        # Adding commands to the multipartUserData adds them to commandsUserData, and vice-versa.
        multipart_user_data.add_commands("touch /root/multi.txt")
        commands_user_data.add_commands("touch /root/userdata.txt")