from aws_cdk import (
    CfnOutput,
    Stack,
    aws_msk as msk,
    aws_ec2 as ec2,
    aws_ssm as ssm,
)

from constructs import Construct


# def getclusterid(text):
#
#     return clusterId


class CdkMSKServerlessVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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
                           # nat_gateway_provider=ec2.NatProvider.gateway(),
                           # nat_gateways=2,
                           )

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
                                                          )],

                                                          # the properties below are optional
                                                          tags={
                                                              "tags_key": "tags"
                                                          }
                                                          )
        clusterArn = str(cfn_serverless_cluster.attr_arn + "")
        accountId = 816085599212
        # splitArn = clusterArn.split("/")
        # clusterId = cfn_serverless_cluster.get_att
        clusterName = cfn_serverless_cluster.cluster_name
        clusterId = ""
        clusterStringId = clusterArn[-39::]
        text = str(cfn_serverless_cluster.attr_arn)
        # text = "arn:aws:kafka:us-east-1:816085599212:cluster/MSKFirehoseS3DeliveryCluster/d5550dbb-29f5-412f-990b-45733e6f56ef-s1"

        # n = 12
        # for i in range(len(text) - 1, len(text) - n - 1, -1):
        #     clusterId = text[i] + clusterId
        #
        # ssmValue = clusterId
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

        rolePolicyStr = '''{
                              "Version": "2012-10-17",
                              "Statement": [
                                {
                                  "Effect": "Allow",
                                  "Action": [
                                    "kafka-cluster:*"
                                  ],
                                  "Resource":''' + clusterArn + '''
                                },
                                {
                                  "Effect": "Allow",
                                  "Action": [
                                    "kafka-cluster:*"
                                  ],
                                  "Resource":''' + clusterArn + '''/*"
                                },
                                {
                                  "Effect": "Allow",
                                  "Action": [
                                    "kafka-cluster:*"
                                  ],
                                  "Resource": ''' + clusterArn + '''/*"
                                }
                              ]
                            }'''

        ssm.StringParameter(self, 'clusterArn',
                            string_value=clusterArn,
                            parameter_name='/mskcluster/clusterArnNew')
        ssm.StringParameter(self, 'rolePolicyStr',
                            string_value=rolePolicyStr,
                            parameter_name='/ec2/assumerole/policy')
        CfnOutput(self, "vpcIdOutput", value=self.vpc.vpc_id)
        CfnOutput(self, "ec2AssumeRolePolicy", value=rolePolicyStr)
