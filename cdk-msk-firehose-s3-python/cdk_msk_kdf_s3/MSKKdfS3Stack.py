import os as os

from aws_cdk import (
    Stack,
    aws_ssm as ssm,
    aws_s3 as s3, RemovalPolicy,
    aws_iam as iam,
)
from aws_cdk import aws_kinesisfirehose as kinesisfirehose
from constructs import Construct


class CdkMSKKdfS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        accountId = os.environ['ACCOUNT_ID']
        topicName = os.environ['TOPIC_NAME']
        desBucketName = os.environ['S3_NAME']
        clusterArn = ssm.StringParameter.value_for_string_parameter(
            self, '/mskcluster/clusterArnNew')

        noOfChars = 39

        clusterId = ssm.StringParameter.value_from_lookup(
            self, '/mskcluster/clusterId')
        clusterIdStr = clusterId[-noOfChars::]
        clusterName = ssm.StringParameter.value_for_string_parameter(
            self, '/mskcluster/clusterName')
        kinesisfirehose.CfnDeliveryStream.delivery_stream_type = 'MSKAsSource'
        kinesisfirehose.CfnDeliveryStream.delivery_stream_name = 'MSKAsSourceFirehose'

        bucketName = s3.Bucket(self, 'Bucket',
                               # block_public_access=[s3.BlockPublicAccess.BLOCK_ALL],
                               encryption=s3.BucketEncryption.S3_MANAGED,
                               bucket_name=desBucketName,
                               versioned=True,
                               removal_policy=RemovalPolicy.DESTROY
                               ).bucket_name
        srArn = 'arn:aws:s3:::' + bucketName

        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "",
                    "Effect": "Allow",
                    "Action": [
                        "kafka:GetBootstrapBrokers",
                        "kafka:DescribeCluster",
                        "kafka:DescribeClusterV2",
                        "kafka-cluster:Connect"
                    ],
                    "Resource": "arn:aws:kafka:us-east-1:" + accountId + ":cluster/" + clusterName + "/" + clusterIdStr
                },
                {
                    "Sid": "",
                    "Effect": "Allow",
                    "Action": [
                        "kafka-cluster:DescribeTopic",
                        "kafka-cluster:CreateTopic",
                        "kafka-cluster:DescribeTopicDynamicConfiguration",
                        "kafka-cluster:ReadData"
                    ],
                    "Resource": "arn:aws:kafka:us-east-1:" + accountId + ":topic/" + clusterName + "/" + clusterIdStr + "/" + topicName
                },
                {
                    "Sid": "",
                    "Effect": "Allow",
                    "Action": [
                        "kafka-cluster:DescribeGroup"
                    ],
                    "Resource": "arn:aws:kafka:us-east-1:" + accountId + ":group/" + clusterName + "/" + clusterIdStr + "/*"
                },
                {
                    "Sid": "",
                    "Effect": "Allow",
                    "Action": [
                        "s3:AbortMultipartUpload",
                        "s3:GetBucketLocation",
                        "s3:GetObject",
                        "s3:ListBucket",
                        "s3:ListBucketMultipartUploads",
                        "s3:PutObject"
                    ],
                    "Resource": [
                        "arn:aws:s3:::" + desBucketName,
                        "arn:aws:s3:::" + desBucketName + "/*"
                    ]
                },
                {
                    "Sid": "",
                    "Effect": "Allow",
                    "Action": [
                        "logs:PutLogEvents"
                    ],
                    "Resource": [
                        "arn:aws:logs:us-east-1:" + accountId + ":log-group:/aws/kinesisfirehose/*:log-stream:*",
                        "arn:aws:logs:us-east-1:" + accountId + ":log-group:*:log-stream:*"
                    ]
                }
            ]
        }

        policyDoc = iam.PolicyDocument.from_json(policy)

        firehoseRole = iam.Role(self, 'Role',
                                assumed_by=iam.ServicePrincipal('firehose.amazonaws.com'),
                                role_name='MskKdfS3Role'
                                )

        policy = iam.Policy(self, "MSKRolePolicy", policy_name="FireHoseRolePolicy", document=policyDoc)
        policy.attach_to_role(role=firehoseRole)

        ssm.StringParameter(self, 'firehoseRole.role_arns',
                            string_value=firehoseRole.role_arn,
                            parameter_name='/mskcluster/role_arn')

        msk_source_configuration_property = kinesisfirehose.CfnDeliveryStream.MSKSourceConfigurationProperty(
            topic_name=topicName,
            msk_cluster_arn=clusterArn,
            authentication_configuration=kinesisfirehose.CfnDeliveryStream.AuthenticationConfigurationProperty(
                connectivity="PRIVATE",
                role_arn=firehoseRole.role_arn
            )
        )
        s3_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(
            bucket_arn=srArn,
            role_arn=firehoseRole.role_arn,
            cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                enabled=False,
                log_group_name="msk-firehose-s3-log-group",
                log_stream_name="msk-firehose-s3-log-stream"
            ),
            encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                no_encryption_config="NoEncryption"
            )
        )

        kinesisfirehose.CfnDeliveryStream(self, "MSKSourceKDFStreams", delivery_stream_type="MSKAsSource",
                                          msk_source_configuration=msk_source_configuration_property,
                                          extended_s3_destination_configuration=s3_destination_configuration_property)
