import os

from aws_cdk import (
    CfnOutput,
    Stack,
    aws_msk as msk,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_iam as iam, )
from constructs import Construct


class CdkMSKServerlessVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        accountId = os.environ['ACCOUNT_ID']
        self.vpc = ec2.Vpc(self, "VPC",
                           max_azs=2,
                           ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/16"),
                           # configuration will create 3 groups in 2 AZs = 6 subnets.
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="PUBLIC",
                               cidr_mask=24
                           )
                           ],
                           )
        mskSecurityGroup = ec2.SecurityGroup(self, "mskSecurityGroupAllowAll",
                                             vpc=self.vpc,
                                             description="Allow ssh access to ec2 instances",
                                             allow_all_outbound=True,
                                             disable_inline_rules=False,
                                             security_group_name="mskSecurityGroup"
                                             )
        mskSecurityGroup.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.all_traffic(),
                                          "allow all access from the world")

        sgId = mskSecurityGroup.security_group_id

        pub_subnets = self.vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC)

        subnetIds = []

        count = 1
        for psub in pub_subnets.subnets:
            subnetIds.append(psub.subnet_id)
            count += 1

        cfn_serverless_cluster = msk.CfnServerlessCluster(self, "MyCfnServerlessCluster",
                                                          client_authentication=msk.CfnServerlessCluster.ClientAuthenticationProperty(
                                                              sasl=msk.CfnServerlessCluster.SaslProperty(
                                                                  iam=msk.CfnServerlessCluster.IamProperty(
                                                                      enabled=True
                                                                  )
                                                              )
                                                          ),
                                                          cluster_name="MSKFirehoseS3DeliveryCluster",
                                                          vpc_configs=[msk.CfnServerlessCluster.VpcConfigProperty(
                                                              subnet_ids=subnetIds
                                                              , security_groups=[sgId]
                                                          )],

                                                          # the properties below are optional
                                                          tags={
                                                              "pattern": "msk-kdf-s3-delivery"
                                                          }
                                                          )
        clusterArn = str(cfn_serverless_cluster.attr_arn + "")
        accountId = os.environ['ACCOUNT_ID']
        clusterName = cfn_serverless_cluster.cluster_name
        ssm.StringParameter(self, 'clusterId',
                            string_value=clusterArn,
                            parameter_name='/mskcluster/clusterId')
        ssm.StringParameter(self, 'clusterName',
                            string_value=clusterName,
                            parameter_name='/mskcluster/clusterName')

        serviceName = "firehose.amazonaws.com"
        clusterPolicy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": [
                            accountId
                        ]
                    },
                    "Action": [
                        "kafka:*"
                    ],
                    "Resource": [clusterArn]
                },
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": serviceName
                    },
                    "Action": [
                        "kafka:*"
                    ],
                    "Resource": [clusterArn]
                }
            ]
        }
        msk.CfnClusterPolicy(self, "MyCfnClusterPolicy",
                             cluster_arn=clusterArn,
                             policy=clusterPolicy
                             )

        rolePolicyStr = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "kafka-cluster:Connect",
                        "kafka-cluster:AlterCluster",
                        "kafka-cluster:DescribeCluster"
                    ],
                    "Resource": "arn:aws:kafka:us-east-1:" + accountId + ":cluster/" + clusterName + "/*"
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "kafka-cluster:*Topic*",
                        "kafka-cluster:WriteData",
                        "kafka-cluster:ReadData"
                    ],
                    "Resource": "arn:aws:kafka:us-east-1:" + accountId + ":topic/" + clusterName + "/*"
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "kafka-cluster:AlterGroup",
                        "kafka-cluster:DescribeGroup"
                    ],
                    "Resource": "arn:aws:kafka:us-east-1:" + accountId + ":group/" + clusterName + "/*"
                }
            ]
        }

        policyDoc = iam.PolicyDocument.from_json(rolePolicyStr)

        ssm.StringParameter(self, 'clusterArn',
                            string_value=clusterArn,
                            parameter_name='/mskcluster/clusterArnNew')
        CfnOutput(self, "vpcIdOutput", value=self.vpc.vpc_id)

        # f = open("user_data.sh", "x")

        lines = (
            "sudo yum -y install java-11 \n wget https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz "
            "\n tar -xzf kafka_2.12-2.8.1.tgz \n rm -rf kafka_2.12-2.8.1.tgz \n cd ./kafka_2.12-2.8.1/libs \n "
            "wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.1/aws-msk-iam-auth-1.1.1-all"
            ".jar \n  cd ../bin \n touch client.properties \n echo \"security.protocol=SASL_SSL\n sasl.mechanism=AWS_MSK_IAM\nsasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required;\nsasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler\" > client.properties")

        # f.writelines(lines)
        # f.close()

        # with open("user_data.sh") as f:
        #     user_data = f.read()
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))
        policy = iam.Policy(self, "EC2RolePolicy", policy_name="EC2RolePolicy", document=policyDoc)
        policy.attach_to_role(role=role)

        commands_user_data = ec2.UserData.for_linux()
        commands_user_data.add_commands(lines)

        instance = ec2.Instance(self, "Instance",
                                instance_type=ec2.InstanceType("t3.medium"),
                                machine_image=amzn_linux,
                                vpc=self.vpc,
                                role=role,
                                user_data=commands_user_data
                                )
        # instance.add_security_group(security_group=sgId)
        # Instance Role and SSM Managed Policy
