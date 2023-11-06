'''
# Amazon Managed Streaming for Apache Kafka Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_msk as msk
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MSK construct libraries](https://constructs.dev/search?q=msk)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MSK resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MSK.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-msk-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MSK](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MSK.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnBatchScramSecret(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_msk.CfnBatchScramSecret",
):
    '''Resource Type definition for AWS::MSK::BatchScramSecret.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_msk as msk
        
        cfn_batch_scram_secret = msk.CfnBatchScramSecret(self, "MyCfnBatchScramSecret",
            cluster_arn="clusterArn",
        
            # the properties below are optional
            secret_arn_list=["secretArnList"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_arn: builtins.str,
        secret_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_arn: 
        :param secret_arn_list: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7520d411e2ff468c392c477234cb67e342bdaac914895933d982e659ed9e98a4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBatchScramSecretProps(
            cluster_arn=cluster_arn, secret_arn_list=secret_arn_list
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__679b387dd09502af5e68247cbc9ed47cc232efe312a69c5e818c44c3f82bcee8)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e8eba3e20dbf60522bfba10c756fea4acf485adb651a7cd021b3f5ceccf21f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb6bef82c23e1fc360009001db2ac936df9869c3c9c3008b243c52c51886fb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="secretArnList")
    def secret_arn_list(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secretArnList"))

    @secret_arn_list.setter
    def secret_arn_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef33f5d92a61738839f87ca9e67498a1c64fa095dbc67d26fe3e3ae929735e2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretArnList", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_msk.CfnBatchScramSecretProps",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn", "secret_arn_list": "secretArnList"},
)
class CfnBatchScramSecretProps:
    def __init__(
        self,
        *,
        cluster_arn: builtins.str,
        secret_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBatchScramSecret``.

        :param cluster_arn: 
        :param secret_arn_list: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_msk as msk
            
            cfn_batch_scram_secret_props = msk.CfnBatchScramSecretProps(
                cluster_arn="clusterArn",
            
                # the properties below are optional
                secret_arn_list=["secretArnList"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f9f8128f7dc818d3ee4d75c78613bf29636c365b9489e1c33d4a21448b3e2ea)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument secret_arn_list", value=secret_arn_list, expected_type=type_hints["secret_arn_list"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
        }
        if secret_arn_list is not None:
            self._values["secret_arn_list"] = secret_arn_list

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-clusterarn
        '''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_arn_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-secretarnlist
        '''
        result = self._values.get("secret_arn_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBatchScramSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_msk.CfnCluster",
):
    '''Creates a new MSK cluster.

    The following Python 3.6 examples shows how you can create a cluster that's distributed over two Availability Zones. Before you run this Python script, replace the example subnet and security-group IDs with the IDs of your subnets and security group. When you create an MSK cluster, its brokers get evenly distributed over a number of Availability Zones that's equal to the number of subnets that you specify in the ``BrokerNodeGroupInfo`` parameter. In this example, you can add a third subnet to get a cluster that's distributed over three Availability Zones::

       import boto3 client = boto3.client('kafka') response = client.create_cluster( BrokerNodeGroupInfo={ 'BrokerAZDistribution': 'DEFAULT', 'ClientSubnets': [ 'subnet-012345678901fedcba', 'subnet-9876543210abcdef01' ], 'InstanceType': 'kafka.m5.large', 'SecurityGroups': [ 'sg-012345abcdef789789' ] }, ClusterName='SalesCluster', EncryptionInfo={ 'EncryptionInTransit': { 'ClientBroker': 'TLS_PLAINTEXT', 'InCluster': True } }, EnhancedMonitoring='PER_TOPIC_PER_BROKER', KafkaVersion='2.2.1', NumberOfBrokerNodes=2
       ) print(response)

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_msk as msk
        
        cfn_cluster = msk.CfnCluster(self, "MyCfnCluster",
            broker_node_group_info=msk.CfnCluster.BrokerNodeGroupInfoProperty(
                client_subnets=["clientSubnets"],
                instance_type="instanceType",
        
                # the properties below are optional
                broker_az_distribution="brokerAzDistribution",
                connectivity_info=msk.CfnCluster.ConnectivityInfoProperty(
                    public_access=msk.CfnCluster.PublicAccessProperty(
                        type="type"
                    ),
                    vpc_connectivity=msk.CfnCluster.VpcConnectivityProperty(
                        client_authentication=msk.CfnCluster.VpcConnectivityClientAuthenticationProperty(
                            sasl=msk.CfnCluster.VpcConnectivitySaslProperty(
                                iam=msk.CfnCluster.VpcConnectivityIamProperty(
                                    enabled=False
                                ),
                                scram=msk.CfnCluster.VpcConnectivityScramProperty(
                                    enabled=False
                                )
                            ),
                            tls=msk.CfnCluster.VpcConnectivityTlsProperty(
                                enabled=False
                            )
                        )
                    )
                ),
                security_groups=["securityGroups"],
                storage_info=msk.CfnCluster.StorageInfoProperty(
                    ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                        provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                            enabled=False,
                            volume_throughput=123
                        ),
                        volume_size=123
                    )
                )
            ),
            cluster_name="clusterName",
            kafka_version="kafkaVersion",
            number_of_broker_nodes=123,
        
            # the properties below are optional
            client_authentication=msk.CfnCluster.ClientAuthenticationProperty(
                sasl=msk.CfnCluster.SaslProperty(
                    iam=msk.CfnCluster.IamProperty(
                        enabled=False
                    ),
                    scram=msk.CfnCluster.ScramProperty(
                        enabled=False
                    )
                ),
                tls=msk.CfnCluster.TlsProperty(
                    certificate_authority_arn_list=["certificateAuthorityArnList"],
                    enabled=False
                ),
                unauthenticated=msk.CfnCluster.UnauthenticatedProperty(
                    enabled=False
                )
            ),
            configuration_info=msk.CfnCluster.ConfigurationInfoProperty(
                arn="arn",
                revision=123
            ),
            current_version="currentVersion",
            encryption_info=msk.CfnCluster.EncryptionInfoProperty(
                encryption_at_rest=msk.CfnCluster.EncryptionAtRestProperty(
                    data_volume_kms_key_id="dataVolumeKmsKeyId"
                ),
                encryption_in_transit=msk.CfnCluster.EncryptionInTransitProperty(
                    client_broker="clientBroker",
                    in_cluster=False
                )
            ),
            enhanced_monitoring="enhancedMonitoring",
            logging_info=msk.CfnCluster.LoggingInfoProperty(
                broker_logs=msk.CfnCluster.BrokerLogsProperty(
                    cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                        enabled=False,
        
                        # the properties below are optional
                        log_group="logGroup"
                    ),
                    firehose=msk.CfnCluster.FirehoseProperty(
                        enabled=False,
        
                        # the properties below are optional
                        delivery_stream="deliveryStream"
                    ),
                    s3=msk.CfnCluster.S3Property(
                        enabled=False,
        
                        # the properties below are optional
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            ),
            open_monitoring=msk.CfnCluster.OpenMonitoringProperty(
                prometheus=msk.CfnCluster.PrometheusProperty(
                    jmx_exporter=msk.CfnCluster.JmxExporterProperty(
                        enabled_in_broker=False
                    ),
                    node_exporter=msk.CfnCluster.NodeExporterProperty(
                        enabled_in_broker=False
                    )
                )
            ),
            storage_mode="storageMode",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        broker_node_group_info: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.BrokerNodeGroupInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        cluster_name: builtins.str,
        kafka_version: builtins.str,
        number_of_broker_nodes: jsii.Number,
        client_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ClientAuthenticationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        configuration_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ConfigurationInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        current_version: typing.Optional[builtins.str] = None,
        encryption_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EncryptionInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        enhanced_monitoring: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.LoggingInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        open_monitoring: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.OpenMonitoringProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        storage_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param broker_node_group_info: Information about the broker nodes in the cluster.
        :param cluster_name: The name of the cluster.
        :param kafka_version: The version of Apache Kafka. You can use Amazon MSK to create clusters that use Apache Kafka versions 1.1.1 and 2.2.1.
        :param number_of_broker_nodes: The number of broker nodes in the cluster.
        :param client_authentication: Includes all client authentication related information.
        :param configuration_info: Represents the configuration that you want MSK to use for the cluster.
        :param current_version: The version of the cluster that you want to update.
        :param encryption_info: Includes all encryption-related information.
        :param enhanced_monitoring: Specifies the level of monitoring for the MSK cluster. The possible values are ``DEFAULT`` , ``PER_BROKER`` , and ``PER_TOPIC_PER_BROKER`` .
        :param logging_info: Logging Info details.
        :param open_monitoring: The settings for open monitoring.
        :param storage_mode: This controls storage mode for supported storage tiers.
        :param tags: Create tags when creating the cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d267b4b2dcfdda539084655e7a1234ffaf8e77376f37d4914abbcef6c64e9f1c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            broker_node_group_info=broker_node_group_info,
            cluster_name=cluster_name,
            kafka_version=kafka_version,
            number_of_broker_nodes=number_of_broker_nodes,
            client_authentication=client_authentication,
            configuration_info=configuration_info,
            current_version=current_version,
            encryption_info=encryption_info,
            enhanced_monitoring=enhanced_monitoring,
            logging_info=logging_info,
            open_monitoring=open_monitoring,
            storage_mode=storage_mode,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb968e1959d50cf1bb135024a884cb1b17c21f705387b0b62807f105e8a0d30)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df344cadfa45c9bb1712b8cad17b0d6602d82780e8cbec4bb3b2a50415412457)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="brokerNodeGroupInfo")
    def broker_node_group_info(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.BrokerNodeGroupInfoProperty"]:
        '''Information about the broker nodes in the cluster.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.BrokerNodeGroupInfoProperty"], jsii.get(self, "brokerNodeGroupInfo"))

    @broker_node_group_info.setter
    def broker_node_group_info(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCluster.BrokerNodeGroupInfoProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeca16d7c9434917e084167a4ad53ae5c40e801a27aef3671a5877ed561da8a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "brokerNodeGroupInfo", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The name of the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcdf905665c7a5fe4197fd1e4b97211937857f4e1c57b49a985ba6d4d9945dbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaVersion")
    def kafka_version(self) -> builtins.str:
        '''The version of Apache Kafka.'''
        return typing.cast(builtins.str, jsii.get(self, "kafkaVersion"))

    @kafka_version.setter
    def kafka_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41bb94e6290c69323fb75c013c4b7142158d540e2c1ec140bb735044d90aa917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> jsii.Number:
        '''The number of broker nodes in the cluster.'''
        return typing.cast(jsii.Number, jsii.get(self, "numberOfBrokerNodes"))

    @number_of_broker_nodes.setter
    def number_of_broker_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__871153d778d14d527bd03c5c339f4f5c01216c5dcf58a168dbc3acf07aa35aaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfBrokerNodes", value)

    @builtins.property
    @jsii.member(jsii_name="clientAuthentication")
    def client_authentication(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ClientAuthenticationProperty"]]:
        '''Includes all client authentication related information.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ClientAuthenticationProperty"]], jsii.get(self, "clientAuthentication"))

    @client_authentication.setter
    def client_authentication(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ClientAuthenticationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999b897b28c870a68a155dbce687b5d48e1be0223338cc26b1ccdaa28b955337)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="configurationInfo")
    def configuration_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationInfoProperty"]]:
        '''Represents the configuration that you want MSK to use for the cluster.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationInfoProperty"]], jsii.get(self, "configurationInfo"))

    @configuration_info.setter
    def configuration_info(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68aea3aaba18dee8b678c7f7677ecae9ed107f4b596657a2f2b8f07f997fd4b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationInfo", value)

    @builtins.property
    @jsii.member(jsii_name="currentVersion")
    def current_version(self) -> typing.Optional[builtins.str]:
        '''The version of the cluster that you want to update.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentVersion"))

    @current_version.setter
    def current_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63a8f0655017a6d4bd71c8a5f323f7ff60bcb57c9c789abc6ca61aae0054113c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionInfo")
    def encryption_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EncryptionInfoProperty"]]:
        '''Includes all encryption-related information.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EncryptionInfoProperty"]], jsii.get(self, "encryptionInfo"))

    @encryption_info.setter
    def encryption_info(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EncryptionInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cf20bb9e6c8edb93f172bf898cbe430e546eddc2d98fe341b62587d35bfcc26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionInfo", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedMonitoring")
    def enhanced_monitoring(self) -> typing.Optional[builtins.str]:
        '''Specifies the level of monitoring for the MSK cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enhancedMonitoring"))

    @enhanced_monitoring.setter
    def enhanced_monitoring(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a39e87ead1cc0622445b0fffb621eed514d654f142e65433d0ddca8025d62a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="loggingInfo")
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.LoggingInfoProperty"]]:
        '''Logging Info details.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.LoggingInfoProperty"]], jsii.get(self, "loggingInfo"))

    @logging_info.setter
    def logging_info(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.LoggingInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d382c4554000521a60f4a1e25f292506a5889f9f704479e32e61cccc944357e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingInfo", value)

    @builtins.property
    @jsii.member(jsii_name="openMonitoring")
    def open_monitoring(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.OpenMonitoringProperty"]]:
        '''The settings for open monitoring.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.OpenMonitoringProperty"]], jsii.get(self, "openMonitoring"))

    @open_monitoring.setter
    def open_monitoring(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.OpenMonitoringProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75fe28c1f9a57617ff0d6a9ccd61b13cd12fe2b29f73cace2349bfc4cd46f2d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="storageMode")
    def storage_mode(self) -> typing.Optional[builtins.str]:
        '''This controls storage mode for supported storage tiers.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageMode"))

    @storage_mode.setter
    def storage_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbed80e4a8389757f50e4ac3a00ab70f0b1864d27b5014ae9d52159bbb42ee2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageMode", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Create tags when creating the cluster.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25d99a2495a599ba3309403ed99fa0b41d839c07974463afbd155e81c63d4c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.BrokerLogsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs": "cloudWatchLogs",
            "firehose": "firehose",
            "s3": "s3",
        },
    )
    class BrokerLogsProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.CloudWatchLogsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.FirehoseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.S3Property", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The broker logs configuration for this MSK cluster.

            :param cloud_watch_logs: Details of the CloudWatch Logs destination for broker logs.
            :param firehose: Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs.
            :param s3: Details of the Amazon S3 destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                broker_logs_property = msk.CfnCluster.BrokerLogsProperty(
                    cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                        enabled=False,
                
                        # the properties below are optional
                        log_group="logGroup"
                    ),
                    firehose=msk.CfnCluster.FirehoseProperty(
                        enabled=False,
                
                        # the properties below are optional
                        delivery_stream="deliveryStream"
                    ),
                    s3=msk.CfnCluster.S3Property(
                        enabled=False,
                
                        # the properties below are optional
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbd8029dbfc62bcbd4abadd3745c2e188c7166e8208e634cad8832a450ab294f)
                check_type(argname="argument cloud_watch_logs", value=cloud_watch_logs, expected_type=type_hints["cloud_watch_logs"])
                check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs is not None:
                self._values["cloud_watch_logs"] = cloud_watch_logs
            if firehose is not None:
                self._values["firehose"] = firehose
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.CloudWatchLogsProperty"]]:
            '''Details of the CloudWatch Logs destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.CloudWatchLogsProperty"]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.FirehoseProperty"]]:
            '''Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.FirehoseProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.S3Property"]]:
            '''Details of the Amazon S3 destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.S3Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrokerLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.BrokerNodeGroupInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_subnets": "clientSubnets",
            "instance_type": "instanceType",
            "broker_az_distribution": "brokerAzDistribution",
            "connectivity_info": "connectivityInfo",
            "security_groups": "securityGroups",
            "storage_info": "storageInfo",
        },
    )
    class BrokerNodeGroupInfoProperty:
        def __init__(
            self,
            *,
            client_subnets: typing.Sequence[builtins.str],
            instance_type: builtins.str,
            broker_az_distribution: typing.Optional[builtins.str] = None,
            connectivity_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ConnectivityInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            storage_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.StorageInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the setup to be used for the broker nodes in the cluster.

            :param client_subnets: The list of subnets to connect to in the client virtual private cloud (VPC). Amazon creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. If you use the US West (N. California) Region, specify exactly two subnets. For other Regions where Amazon MSK is available, you can specify either two or three subnets. The subnets that you specify must be in distinct Availability Zones. When you create a cluster, Amazon MSK distributes the broker nodes evenly across the subnets that you specify. Client subnets can't occupy the Availability Zone with ID ``use1-az3`` .
            :param instance_type: The type of Amazon EC2 instances to use for brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.8xlarge, kafka.m5.12xlarge, kafka.m5.16xlarge, and kafka.m5.24xlarge, and kafka.t3.small.
            :param broker_az_distribution: This parameter is currently not in use.
            :param connectivity_info: Information about the cluster's connectivity setting.
            :param security_groups: The security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don't specify a security group, Amazon MSK uses the default security group associated with the VPC. If you specify security groups that were shared with you, you must ensure that you have permissions to them. Specifically, you need the ``ec2:DescribeSecurityGroups`` permission.
            :param storage_info: Contains information about storage volumes attached to Amazon MSK broker nodes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                broker_node_group_info_property = msk.CfnCluster.BrokerNodeGroupInfoProperty(
                    client_subnets=["clientSubnets"],
                    instance_type="instanceType",
                
                    # the properties below are optional
                    broker_az_distribution="brokerAzDistribution",
                    connectivity_info=msk.CfnCluster.ConnectivityInfoProperty(
                        public_access=msk.CfnCluster.PublicAccessProperty(
                            type="type"
                        ),
                        vpc_connectivity=msk.CfnCluster.VpcConnectivityProperty(
                            client_authentication=msk.CfnCluster.VpcConnectivityClientAuthenticationProperty(
                                sasl=msk.CfnCluster.VpcConnectivitySaslProperty(
                                    iam=msk.CfnCluster.VpcConnectivityIamProperty(
                                        enabled=False
                                    ),
                                    scram=msk.CfnCluster.VpcConnectivityScramProperty(
                                        enabled=False
                                    )
                                ),
                                tls=msk.CfnCluster.VpcConnectivityTlsProperty(
                                    enabled=False
                                )
                            )
                        )
                    ),
                    security_groups=["securityGroups"],
                    storage_info=msk.CfnCluster.StorageInfoProperty(
                        ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                            provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                                enabled=False,
                                volume_throughput=123
                            ),
                            volume_size=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__047ba5870776adf805ab38c9eed596d6715e6bfa45af6eaf20ea7bd91858fe82)
                check_type(argname="argument client_subnets", value=client_subnets, expected_type=type_hints["client_subnets"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument broker_az_distribution", value=broker_az_distribution, expected_type=type_hints["broker_az_distribution"])
                check_type(argname="argument connectivity_info", value=connectivity_info, expected_type=type_hints["connectivity_info"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument storage_info", value=storage_info, expected_type=type_hints["storage_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_subnets": client_subnets,
                "instance_type": instance_type,
            }
            if broker_az_distribution is not None:
                self._values["broker_az_distribution"] = broker_az_distribution
            if connectivity_info is not None:
                self._values["connectivity_info"] = connectivity_info
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if storage_info is not None:
                self._values["storage_info"] = storage_info

        @builtins.property
        def client_subnets(self) -> typing.List[builtins.str]:
            '''The list of subnets to connect to in the client virtual private cloud (VPC).

            Amazon creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data.

            If you use the US West (N. California) Region, specify exactly two subnets. For other Regions where Amazon MSK is available, you can specify either two or three subnets. The subnets that you specify must be in distinct Availability Zones. When you create a cluster, Amazon MSK distributes the broker nodes evenly across the subnets that you specify.

            Client subnets can't occupy the Availability Zone with ID ``use1-az3`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-clientsubnets
            '''
            result = self._values.get("client_subnets")
            assert result is not None, "Required property 'client_subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''The type of Amazon EC2 instances to use for brokers.

            The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.8xlarge, kafka.m5.12xlarge, kafka.m5.16xlarge, and kafka.m5.24xlarge, and kafka.t3.small.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def broker_az_distribution(self) -> typing.Optional[builtins.str]:
            '''This parameter is currently not in use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution
            '''
            result = self._values.get("broker_az_distribution")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connectivity_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConnectivityInfoProperty"]]:
            '''Information about the cluster's connectivity setting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-connectivityinfo
            '''
            result = self._values.get("connectivity_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConnectivityInfoProperty"]], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster.

            If you don't specify a security group, Amazon MSK uses the default security group associated with the VPC. If you specify security groups that were shared with you, you must ensure that you have permissions to them. Specifically, you need the ``ec2:DescribeSecurityGroups`` permission.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def storage_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.StorageInfoProperty"]]:
            '''Contains information about storage volumes attached to Amazon MSK broker nodes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-storageinfo
            '''
            result = self._values.get("storage_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.StorageInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrokerNodeGroupInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.ClientAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sasl": "sasl",
            "tls": "tls",
            "unauthenticated": "unauthenticated",
        },
    )
    class ClientAuthenticationProperty:
        def __init__(
            self,
            *,
            sasl: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.SaslProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            tls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.TlsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            unauthenticated: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.UnauthenticatedProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Includes all client authentication information.

            :param sasl: Details for client authentication using SASL. To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.
            :param tls: Details for ClientAuthentication using TLS. To turn on TLS access control, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true and ``clientBroker`` to ``TLS`` .
            :param unauthenticated: Details for ClientAuthentication using no authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                client_authentication_property = msk.CfnCluster.ClientAuthenticationProperty(
                    sasl=msk.CfnCluster.SaslProperty(
                        iam=msk.CfnCluster.IamProperty(
                            enabled=False
                        ),
                        scram=msk.CfnCluster.ScramProperty(
                            enabled=False
                        )
                    ),
                    tls=msk.CfnCluster.TlsProperty(
                        certificate_authority_arn_list=["certificateAuthorityArnList"],
                        enabled=False
                    ),
                    unauthenticated=msk.CfnCluster.UnauthenticatedProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe35787c5f8943b4dbd478e4334e34a43f1b34cb667d5f716a5cc08d74b0c36f)
                check_type(argname="argument sasl", value=sasl, expected_type=type_hints["sasl"])
                check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
                check_type(argname="argument unauthenticated", value=unauthenticated, expected_type=type_hints["unauthenticated"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sasl is not None:
                self._values["sasl"] = sasl
            if tls is not None:
                self._values["tls"] = tls
            if unauthenticated is not None:
                self._values["unauthenticated"] = unauthenticated

        @builtins.property
        def sasl(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SaslProperty"]]:
            '''Details for client authentication using SASL.

            To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-sasl
            '''
            result = self._values.get("sasl")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SaslProperty"]], result)

        @builtins.property
        def tls(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.TlsProperty"]]:
            '''Details for ClientAuthentication using TLS.

            To turn on TLS access control, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true and ``clientBroker`` to ``TLS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-tls
            '''
            result = self._values.get("tls")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.TlsProperty"]], result)

        @builtins.property
        def unauthenticated(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.UnauthenticatedProperty"]]:
            '''Details for ClientAuthentication using no authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-unauthenticated
            '''
            result = self._values.get("unauthenticated")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.UnauthenticatedProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.CloudWatchLogsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "log_group": "logGroup"},
    )
    class CloudWatchLogsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            log_group: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details of the CloudWatch Logs destination for broker logs.

            :param enabled: Specifies whether broker logs get sent to the specified CloudWatch Logs destination.
            :param log_group: The CloudWatch log group that is the destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                cloud_watch_logs_property = msk.CfnCluster.CloudWatchLogsProperty(
                    enabled=False,
                
                    # the properties below are optional
                    log_group="logGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ae6e10d35688641429fe8898b54dccb7dea8409c6cbb770ae30bfd8f89d95f2)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if log_group is not None:
                self._values["log_group"] = log_group

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether broker logs get sent to the specified CloudWatch Logs destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def log_group(self) -> typing.Optional[builtins.str]:
            '''The CloudWatch log group that is the destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-loggroup
            '''
            result = self._values.get("log_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.ConfigurationInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "revision": "revision"},
    )
    class ConfigurationInfoProperty:
        def __init__(self, *, arn: builtins.str, revision: jsii.Number) -> None:
            '''Specifies the configuration to use for the brokers.

            :param arn: ARN of the configuration to use.
            :param revision: The revision of the configuration to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                configuration_info_property = msk.CfnCluster.ConfigurationInfoProperty(
                    arn="arn",
                    revision=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__978657c9cf18466215b38a251ae4816196dcec1b76c8a82c67f970ce40d345d6)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
                "revision": revision,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''ARN of the configuration to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def revision(self) -> jsii.Number:
            '''The revision of the configuration to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.ConnectivityInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "public_access": "publicAccess",
            "vpc_connectivity": "vpcConnectivity",
        },
    )
    class ConnectivityInfoProperty:
        def __init__(
            self,
            *,
            public_access: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.PublicAccessProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            vpc_connectivity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.VpcConnectivityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Broker access controls.

            :param public_access: Access control settings for the cluster's brokers.
            :param vpc_connectivity: VPC connection control settings for brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                connectivity_info_property = msk.CfnCluster.ConnectivityInfoProperty(
                    public_access=msk.CfnCluster.PublicAccessProperty(
                        type="type"
                    ),
                    vpc_connectivity=msk.CfnCluster.VpcConnectivityProperty(
                        client_authentication=msk.CfnCluster.VpcConnectivityClientAuthenticationProperty(
                            sasl=msk.CfnCluster.VpcConnectivitySaslProperty(
                                iam=msk.CfnCluster.VpcConnectivityIamProperty(
                                    enabled=False
                                ),
                                scram=msk.CfnCluster.VpcConnectivityScramProperty(
                                    enabled=False
                                )
                            ),
                            tls=msk.CfnCluster.VpcConnectivityTlsProperty(
                                enabled=False
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d1ba9dbd3fe54fc52707e8245c99f4e132a975a1ea7784a9e8d49cfc50fc4d71)
                check_type(argname="argument public_access", value=public_access, expected_type=type_hints["public_access"])
                check_type(argname="argument vpc_connectivity", value=vpc_connectivity, expected_type=type_hints["vpc_connectivity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if public_access is not None:
                self._values["public_access"] = public_access
            if vpc_connectivity is not None:
                self._values["vpc_connectivity"] = vpc_connectivity

        @builtins.property
        def public_access(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.PublicAccessProperty"]]:
            '''Access control settings for the cluster's brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html#cfn-msk-cluster-connectivityinfo-publicaccess
            '''
            result = self._values.get("public_access")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.PublicAccessProperty"]], result)

        @builtins.property
        def vpc_connectivity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityProperty"]]:
            '''VPC connection control settings for brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html#cfn-msk-cluster-connectivityinfo-vpcconnectivity
            '''
            result = self._values.get("vpc_connectivity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectivityInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.EBSStorageInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provisioned_throughput": "provisionedThroughput",
            "volume_size": "volumeSize",
        },
    )
    class EBSStorageInfoProperty:
        def __init__(
            self,
            *,
            provisioned_throughput: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ProvisionedThroughputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            volume_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about the EBS storage volumes attached to the broker nodes.

            :param provisioned_throughput: EBS volume provisioned throughput information.
            :param volume_size: The size in GiB of the EBS volume for the data drive on each broker node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                e_bSStorage_info_property = msk.CfnCluster.EBSStorageInfoProperty(
                    provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                        enabled=False,
                        volume_throughput=123
                    ),
                    volume_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d93be124fa1756365f8d601bf56551024d16dd8697368298f887f35cf9197d1)
                check_type(argname="argument provisioned_throughput", value=provisioned_throughput, expected_type=type_hints["provisioned_throughput"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if provisioned_throughput is not None:
                self._values["provisioned_throughput"] = provisioned_throughput
            if volume_size is not None:
                self._values["volume_size"] = volume_size

        @builtins.property
        def provisioned_throughput(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ProvisionedThroughputProperty"]]:
            '''EBS volume provisioned throughput information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-provisionedthroughput
            '''
            result = self._values.get("provisioned_throughput")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ProvisionedThroughputProperty"]], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''The size in GiB of the EBS volume for the data drive on each broker node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EBSStorageInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.EncryptionAtRestProperty",
        jsii_struct_bases=[],
        name_mapping={"data_volume_kms_key_id": "dataVolumeKmsKeyId"},
    )
    class EncryptionAtRestProperty:
        def __init__(self, *, data_volume_kms_key_id: builtins.str) -> None:
            '''The data-volume encryption details.

            You can't update encryption at rest settings for existing clusters.

            :param data_volume_kms_key_id: The ARN of the Amazon KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                encryption_at_rest_property = msk.CfnCluster.EncryptionAtRestProperty(
                    data_volume_kms_key_id="dataVolumeKmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__601ca97f7a025a112252de96abad1ce870ae78db8a5372a4f216bbcf2cd01cd0)
                check_type(argname="argument data_volume_kms_key_id", value=data_volume_kms_key_id, expected_type=type_hints["data_volume_kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_volume_kms_key_id": data_volume_kms_key_id,
            }

        @builtins.property
        def data_volume_kms_key_id(self) -> builtins.str:
            '''The ARN of the Amazon KMS key for encrypting data at rest.

            If you don't specify a KMS key, MSK creates one for you and uses it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html#cfn-msk-cluster-encryptionatrest-datavolumekmskeyid
            '''
            result = self._values.get("data_volume_kms_key_id")
            assert result is not None, "Required property 'data_volume_kms_key_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionAtRestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.EncryptionInTransitProperty",
        jsii_struct_bases=[],
        name_mapping={"client_broker": "clientBroker", "in_cluster": "inCluster"},
    )
    class EncryptionInTransitProperty:
        def __init__(
            self,
            *,
            client_broker: typing.Optional[builtins.str] = None,
            in_cluster: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The settings for encrypting data in transit.

            :param client_broker: Indicates the encryption setting for data in transit between clients and brokers. You must set it to one of the following values. ``TLS`` means that client-broker communication is enabled with TLS only. ``TLS_PLAINTEXT`` means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data. ``PLAINTEXT`` means that client-broker communication is enabled in plaintext only. The default value is ``TLS`` .
            :param in_cluster: When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext. The default value is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                encryption_in_transit_property = msk.CfnCluster.EncryptionInTransitProperty(
                    client_broker="clientBroker",
                    in_cluster=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8817cd1ddb22712cb54e76ff0e0f3ebc61e27a1912efefd032c5a2f9dcc2038d)
                check_type(argname="argument client_broker", value=client_broker, expected_type=type_hints["client_broker"])
                check_type(argname="argument in_cluster", value=in_cluster, expected_type=type_hints["in_cluster"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if client_broker is not None:
                self._values["client_broker"] = client_broker
            if in_cluster is not None:
                self._values["in_cluster"] = in_cluster

        @builtins.property
        def client_broker(self) -> typing.Optional[builtins.str]:
            '''Indicates the encryption setting for data in transit between clients and brokers.

            You must set it to one of the following values.

            ``TLS`` means that client-broker communication is enabled with TLS only.

            ``TLS_PLAINTEXT`` means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.

            ``PLAINTEXT`` means that client-broker communication is enabled in plaintext only.

            The default value is ``TLS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-clientbroker
            '''
            result = self._values.get("client_broker")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def in_cluster(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted.

            When set to false, the communication happens in plaintext.

            The default value is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-incluster
            '''
            result = self._values.get("in_cluster")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionInTransitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.EncryptionInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_at_rest": "encryptionAtRest",
            "encryption_in_transit": "encryptionInTransit",
        },
    )
    class EncryptionInfoProperty:
        def __init__(
            self,
            *,
            encryption_at_rest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EncryptionAtRestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            encryption_in_transit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EncryptionInTransitProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Includes encryption-related information, such as the Amazon KMS key used for encrypting data at rest and whether you want MSK to encrypt your data in transit.

            :param encryption_at_rest: The data-volume encryption details.
            :param encryption_in_transit: The details for encryption in transit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                encryption_info_property = msk.CfnCluster.EncryptionInfoProperty(
                    encryption_at_rest=msk.CfnCluster.EncryptionAtRestProperty(
                        data_volume_kms_key_id="dataVolumeKmsKeyId"
                    ),
                    encryption_in_transit=msk.CfnCluster.EncryptionInTransitProperty(
                        client_broker="clientBroker",
                        in_cluster=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__82b72539c93ffe289109f6da6a4a0dc5b1c4add6c3a5cbe84285e37c9b72ff69)
                check_type(argname="argument encryption_at_rest", value=encryption_at_rest, expected_type=type_hints["encryption_at_rest"])
                check_type(argname="argument encryption_in_transit", value=encryption_in_transit, expected_type=type_hints["encryption_in_transit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption_at_rest is not None:
                self._values["encryption_at_rest"] = encryption_at_rest
            if encryption_in_transit is not None:
                self._values["encryption_in_transit"] = encryption_in_transit

        @builtins.property
        def encryption_at_rest(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EncryptionAtRestProperty"]]:
            '''The data-volume encryption details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionatrest
            '''
            result = self._values.get("encryption_at_rest")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EncryptionAtRestProperty"]], result)

        @builtins.property
        def encryption_in_transit(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EncryptionInTransitProperty"]]:
            '''The details for encryption in transit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionintransit
            '''
            result = self._values.get("encryption_in_transit")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EncryptionInTransitProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.FirehoseProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "delivery_stream": "deliveryStream"},
    )
    class FirehoseProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            delivery_stream: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Firehose details for BrokerLogs.

            :param enabled: Specifies whether broker logs get send to the specified Kinesis Data Firehose delivery stream.
            :param delivery_stream: The Kinesis Data Firehose delivery stream that is the destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                firehose_property = msk.CfnCluster.FirehoseProperty(
                    enabled=False,
                
                    # the properties below are optional
                    delivery_stream="deliveryStream"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__79bdccdd0f4d9e13c3d92e4a9740538786951fc032dbc4c30a6c9c2d68bd88fb)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if delivery_stream is not None:
                self._values["delivery_stream"] = delivery_stream

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether broker logs get send to the specified Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def delivery_stream(self) -> typing.Optional[builtins.str]:
            '''The Kinesis Data Firehose delivery stream that is the destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-deliverystream
            '''
            result = self._values.get("delivery_stream")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.IamProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class IamProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Details for SASL/IAM client authentication.

            :param enabled: SASL/IAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                iam_property = msk.CfnCluster.IamProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c9d17d5e61df7419a4db466a2ddaea0429b28f4b26e639fb8a605c2a99675af)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''SASL/IAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html#cfn-msk-cluster-iam-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.JmxExporterProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled_in_broker": "enabledInBroker"},
    )
    class JmxExporterProperty:
        def __init__(
            self,
            *,
            enabled_in_broker: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Indicates whether you want to enable or disable the JMX Exporter.

            :param enabled_in_broker: Indicates whether you want to enable or disable the JMX Exporter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                jmx_exporter_property = msk.CfnCluster.JmxExporterProperty(
                    enabled_in_broker=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4eaa737fdd4b761b60d33bd8c66551298c9e7beeb94798e2b9eb9a3cba4f2ba2)
                check_type(argname="argument enabled_in_broker", value=enabled_in_broker, expected_type=type_hints["enabled_in_broker"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled_in_broker": enabled_in_broker,
            }

        @builtins.property
        def enabled_in_broker(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether you want to enable or disable the JMX Exporter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html#cfn-msk-cluster-jmxexporter-enabledinbroker
            '''
            result = self._values.get("enabled_in_broker")
            assert result is not None, "Required property 'enabled_in_broker' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JmxExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.LoggingInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"broker_logs": "brokerLogs"},
    )
    class LoggingInfoProperty:
        def __init__(
            self,
            *,
            broker_logs: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.BrokerLogsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''You can configure your MSK cluster to send broker logs to different destination types.

            This is a container for the configuration details related to broker logs.

            :param broker_logs: You can configure your MSK cluster to send broker logs to different destination types. This configuration specifies the details of these destinations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                logging_info_property = msk.CfnCluster.LoggingInfoProperty(
                    broker_logs=msk.CfnCluster.BrokerLogsProperty(
                        cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                            enabled=False,
                
                            # the properties below are optional
                            log_group="logGroup"
                        ),
                        firehose=msk.CfnCluster.FirehoseProperty(
                            enabled=False,
                
                            # the properties below are optional
                            delivery_stream="deliveryStream"
                        ),
                        s3=msk.CfnCluster.S3Property(
                            enabled=False,
                
                            # the properties below are optional
                            bucket="bucket",
                            prefix="prefix"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb34e9e4e6ea2dca1d1d7c205b60cf5fc069f6150273b5e5c14b565ef784c6cb)
                check_type(argname="argument broker_logs", value=broker_logs, expected_type=type_hints["broker_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "broker_logs": broker_logs,
            }

        @builtins.property
        def broker_logs(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.BrokerLogsProperty"]:
            '''You can configure your MSK cluster to send broker logs to different destination types.

            This configuration specifies the details of these destinations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html#cfn-msk-cluster-logginginfo-brokerlogs
            '''
            result = self._values.get("broker_logs")
            assert result is not None, "Required property 'broker_logs' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.BrokerLogsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.NodeExporterProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled_in_broker": "enabledInBroker"},
    )
    class NodeExporterProperty:
        def __init__(
            self,
            *,
            enabled_in_broker: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Indicates whether you want to enable or disable the Node Exporter.

            :param enabled_in_broker: Indicates whether you want to enable or disable the Node Exporter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                node_exporter_property = msk.CfnCluster.NodeExporterProperty(
                    enabled_in_broker=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d21596c86d0237daafa3a630b632d9dd4d16bbca82f174eed700401353061e16)
                check_type(argname="argument enabled_in_broker", value=enabled_in_broker, expected_type=type_hints["enabled_in_broker"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled_in_broker": enabled_in_broker,
            }

        @builtins.property
        def enabled_in_broker(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether you want to enable or disable the Node Exporter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html#cfn-msk-cluster-nodeexporter-enabledinbroker
            '''
            result = self._values.get("enabled_in_broker")
            assert result is not None, "Required property 'enabled_in_broker' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.OpenMonitoringProperty",
        jsii_struct_bases=[],
        name_mapping={"prometheus": "prometheus"},
    )
    class OpenMonitoringProperty:
        def __init__(
            self,
            *,
            prometheus: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.PrometheusProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''JMX and Node monitoring for the MSK cluster.

            :param prometheus: Prometheus exporter settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                open_monitoring_property = msk.CfnCluster.OpenMonitoringProperty(
                    prometheus=msk.CfnCluster.PrometheusProperty(
                        jmx_exporter=msk.CfnCluster.JmxExporterProperty(
                            enabled_in_broker=False
                        ),
                        node_exporter=msk.CfnCluster.NodeExporterProperty(
                            enabled_in_broker=False
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe3d6046a8f5a7d026e4209e2c3faee856baceff5b3f885a18150ec399cb71fc)
                check_type(argname="argument prometheus", value=prometheus, expected_type=type_hints["prometheus"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "prometheus": prometheus,
            }

        @builtins.property
        def prometheus(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.PrometheusProperty"]:
            '''Prometheus exporter settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html#cfn-msk-cluster-openmonitoring-prometheus
            '''
            result = self._values.get("prometheus")
            assert result is not None, "Required property 'prometheus' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.PrometheusProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenMonitoringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.PrometheusProperty",
        jsii_struct_bases=[],
        name_mapping={"jmx_exporter": "jmxExporter", "node_exporter": "nodeExporter"},
    )
    class PrometheusProperty:
        def __init__(
            self,
            *,
            jmx_exporter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.JmxExporterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            node_exporter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.NodeExporterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Prometheus settings for open monitoring.

            :param jmx_exporter: Indicates whether you want to enable or disable the JMX Exporter.
            :param node_exporter: Indicates whether you want to enable or disable the Node Exporter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                prometheus_property = msk.CfnCluster.PrometheusProperty(
                    jmx_exporter=msk.CfnCluster.JmxExporterProperty(
                        enabled_in_broker=False
                    ),
                    node_exporter=msk.CfnCluster.NodeExporterProperty(
                        enabled_in_broker=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c00cf2d2430d38c9e9785d442acfabb344902a11bc9223bd80e26d7f514ec937)
                check_type(argname="argument jmx_exporter", value=jmx_exporter, expected_type=type_hints["jmx_exporter"])
                check_type(argname="argument node_exporter", value=node_exporter, expected_type=type_hints["node_exporter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if jmx_exporter is not None:
                self._values["jmx_exporter"] = jmx_exporter
            if node_exporter is not None:
                self._values["node_exporter"] = node_exporter

        @builtins.property
        def jmx_exporter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.JmxExporterProperty"]]:
            '''Indicates whether you want to enable or disable the JMX Exporter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-jmxexporter
            '''
            result = self._values.get("jmx_exporter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.JmxExporterProperty"]], result)

        @builtins.property
        def node_exporter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.NodeExporterProperty"]]:
            '''Indicates whether you want to enable or disable the Node Exporter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-nodeexporter
            '''
            result = self._values.get("node_exporter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.NodeExporterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrometheusProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.ProvisionedThroughputProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "volume_throughput": "volumeThroughput"},
    )
    class ProvisionedThroughputProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            volume_throughput: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about provisioned throughput for EBS storage volumes attached to kafka broker nodes.

            :param enabled: Provisioned throughput is enabled or not.
            :param volume_throughput: Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                provisioned_throughput_property = msk.CfnCluster.ProvisionedThroughputProperty(
                    enabled=False,
                    volume_throughput=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9bf430fec171ea7e825c41378e4aa35d667362efc4d0d9740db3be3e7115fc9)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument volume_throughput", value=volume_throughput, expected_type=type_hints["volume_throughput"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if volume_throughput is not None:
                self._values["volume_throughput"] = volume_throughput

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Provisioned throughput is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def volume_throughput(self) -> typing.Optional[jsii.Number]:
            '''Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-volumethroughput
            '''
            result = self._values.get("volume_throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedThroughputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.PublicAccessProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class PublicAccessProperty:
        def __init__(self, *, type: typing.Optional[builtins.str] = None) -> None:
            '''Broker access controls.

            :param type: DISABLED means that public access is turned off. SERVICE_PROVIDED_EIPS means that public access is turned on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                public_access_property = msk.CfnCluster.PublicAccessProperty(
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03c0f11124e397d2c64c42ed84e0f41e63fe036a5dbb8354d7b0a83fdda7780e)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''DISABLED means that public access is turned off.

            SERVICE_PROVIDED_EIPS means that public access is turned on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html#cfn-msk-cluster-publicaccess-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublicAccessProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.S3Property",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "bucket": "bucket", "prefix": "prefix"},
    )
    class S3Property:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            bucket: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the Amazon S3 destination for broker logs.

            :param enabled: Specifies whether broker logs get sent to the specified Amazon S3 destination.
            :param bucket: The name of the S3 bucket that is the destination for broker logs.
            :param prefix: The S3 prefix that is the destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                s3_property = msk.CfnCluster.S3Property(
                    enabled=False,
                
                    # the properties below are optional
                    bucket="bucket",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__802632a907f2036c840a19e8b3c37b50084fc2617376e08f1ea1e98f4a19a35b)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if bucket is not None:
                self._values["bucket"] = bucket
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether broker logs get sent to the specified Amazon S3 destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def bucket(self) -> typing.Optional[builtins.str]:
            '''The name of the S3 bucket that is the destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-bucket
            '''
            result = self._values.get("bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 prefix that is the destination for broker logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.SaslProperty",
        jsii_struct_bases=[],
        name_mapping={"iam": "iam", "scram": "scram"},
    )
    class SaslProperty:
        def __init__(
            self,
            *,
            iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.IamProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scram: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ScramProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Details for client authentication using SASL.

            To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :param iam: Details for ClientAuthentication using IAM.
            :param scram: Details for SASL/SCRAM client authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                sasl_property = msk.CfnCluster.SaslProperty(
                    iam=msk.CfnCluster.IamProperty(
                        enabled=False
                    ),
                    scram=msk.CfnCluster.ScramProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__23ccb244e3353b35264d16f3e5f20f74f507bc5860a069055a60699937fe795f)
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
                check_type(argname="argument scram", value=scram, expected_type=type_hints["scram"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam is not None:
                self._values["iam"] = iam
            if scram is not None:
                self._values["scram"] = scram

        @builtins.property
        def iam(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.IamProperty"]]:
            '''Details for ClientAuthentication using IAM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-iam
            '''
            result = self._values.get("iam")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.IamProperty"]], result)

        @builtins.property
        def scram(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ScramProperty"]]:
            '''Details for SASL/SCRAM client authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-scram
            '''
            result = self._values.get("scram")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ScramProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SaslProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.ScramProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class ScramProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Details for SASL/SCRAM client authentication.

            :param enabled: SASL/SCRAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                scram_property = msk.CfnCluster.ScramProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1632715500ba54afdd5784104a92272b1cfc744370d3cd691bf47a18a76a51bf)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''SASL/SCRAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html#cfn-msk-cluster-scram-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScramProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.StorageInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"ebs_storage_info": "ebsStorageInfo"},
    )
    class StorageInfoProperty:
        def __init__(
            self,
            *,
            ebs_storage_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EBSStorageInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about storage volumes attached to Amazon MSK broker nodes.

            :param ebs_storage_info: EBS volume information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                storage_info_property = msk.CfnCluster.StorageInfoProperty(
                    ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                        provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                            enabled=False,
                            volume_throughput=123
                        ),
                        volume_size=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80e19ae4f693f8d16bb984b14c4e276ce1ffdc97a798ba373aec65fa283e8287)
                check_type(argname="argument ebs_storage_info", value=ebs_storage_info, expected_type=type_hints["ebs_storage_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ebs_storage_info is not None:
                self._values["ebs_storage_info"] = ebs_storage_info

        @builtins.property
        def ebs_storage_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EBSStorageInfoProperty"]]:
            '''EBS volume information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html#cfn-msk-cluster-storageinfo-ebsstorageinfo
            '''
            result = self._values.get("ebs_storage_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EBSStorageInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.TlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_authority_arn_list": "certificateAuthorityArnList",
            "enabled": "enabled",
        },
    )
    class TlsProperty:
        def __init__(
            self,
            *,
            certificate_authority_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Details for client authentication using TLS.

            :param certificate_authority_arn_list: List of AWS Private CA ARNs.
            :param enabled: TLS authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                tls_property = msk.CfnCluster.TlsProperty(
                    certificate_authority_arn_list=["certificateAuthorityArnList"],
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__201ae89a334d1d435bfafb97fb7a10c1da455123e9315bef634f525af54ad4c3)
                check_type(argname="argument certificate_authority_arn_list", value=certificate_authority_arn_list, expected_type=type_hints["certificate_authority_arn_list"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_authority_arn_list is not None:
                self._values["certificate_authority_arn_list"] = certificate_authority_arn_list
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def certificate_authority_arn_list(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''List of AWS Private CA ARNs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-certificateauthorityarnlist
            '''
            result = self._values.get("certificate_authority_arn_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''TLS authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.UnauthenticatedProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class UnauthenticatedProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Details for allowing no client authentication.

            :param enabled: Unauthenticated is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                unauthenticated_property = msk.CfnCluster.UnauthenticatedProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__627a4f01251f0f7c34b63f12ac75b6581855292444a20ea6f8073e1881f3e9ff)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Unauthenticated is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html#cfn-msk-cluster-unauthenticated-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UnauthenticatedProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.VpcConnectivityClientAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"sasl": "sasl", "tls": "tls"},
    )
    class VpcConnectivityClientAuthenticationProperty:
        def __init__(
            self,
            *,
            sasl: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.VpcConnectivitySaslProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            tls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.VpcConnectivityTlsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Includes all client authentication information for VpcConnectivity.

            :param sasl: Details for VpcConnectivity ClientAuthentication using SASL.
            :param tls: Details for VpcConnectivity ClientAuthentication using TLS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityclientauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                vpc_connectivity_client_authentication_property = msk.CfnCluster.VpcConnectivityClientAuthenticationProperty(
                    sasl=msk.CfnCluster.VpcConnectivitySaslProperty(
                        iam=msk.CfnCluster.VpcConnectivityIamProperty(
                            enabled=False
                        ),
                        scram=msk.CfnCluster.VpcConnectivityScramProperty(
                            enabled=False
                        )
                    ),
                    tls=msk.CfnCluster.VpcConnectivityTlsProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b5aa63eea4121f8cf76d7698bbb8b609934b88b26b3bd2f092229d6eeefb620c)
                check_type(argname="argument sasl", value=sasl, expected_type=type_hints["sasl"])
                check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sasl is not None:
                self._values["sasl"] = sasl
            if tls is not None:
                self._values["tls"] = tls

        @builtins.property
        def sasl(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivitySaslProperty"]]:
            '''Details for VpcConnectivity ClientAuthentication using SASL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityclientauthentication.html#cfn-msk-cluster-vpcconnectivityclientauthentication-sasl
            '''
            result = self._values.get("sasl")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivitySaslProperty"]], result)

        @builtins.property
        def tls(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityTlsProperty"]]:
            '''Details for VpcConnectivity ClientAuthentication using TLS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityclientauthentication.html#cfn-msk-cluster-vpcconnectivityclientauthentication-tls
            '''
            result = self._values.get("tls")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityTlsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConnectivityClientAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.VpcConnectivityIamProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class VpcConnectivityIamProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Details for SASL/IAM client authentication for VpcConnectivity.

            :param enabled: SASL/IAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityiam.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                vpc_connectivity_iam_property = msk.CfnCluster.VpcConnectivityIamProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d2babe34af394074220ca9baba7827ab597d8d49eb25997ebb1c5b9df10f5e9)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''SASL/IAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityiam.html#cfn-msk-cluster-vpcconnectivityiam-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConnectivityIamProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.VpcConnectivityProperty",
        jsii_struct_bases=[],
        name_mapping={"client_authentication": "clientAuthentication"},
    )
    class VpcConnectivityProperty:
        def __init__(
            self,
            *,
            client_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.VpcConnectivityClientAuthenticationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''VPC connection control settings for brokers.

            :param client_authentication: VPC connection control settings for brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                vpc_connectivity_property = msk.CfnCluster.VpcConnectivityProperty(
                    client_authentication=msk.CfnCluster.VpcConnectivityClientAuthenticationProperty(
                        sasl=msk.CfnCluster.VpcConnectivitySaslProperty(
                            iam=msk.CfnCluster.VpcConnectivityIamProperty(
                                enabled=False
                            ),
                            scram=msk.CfnCluster.VpcConnectivityScramProperty(
                                enabled=False
                            )
                        ),
                        tls=msk.CfnCluster.VpcConnectivityTlsProperty(
                            enabled=False
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__81a77b1701714a33de616ece55afe0c2081e30511acc3ac1fe97c941379866c1)
                check_type(argname="argument client_authentication", value=client_authentication, expected_type=type_hints["client_authentication"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if client_authentication is not None:
                self._values["client_authentication"] = client_authentication

        @builtins.property
        def client_authentication(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityClientAuthenticationProperty"]]:
            '''VPC connection control settings for brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivity.html#cfn-msk-cluster-vpcconnectivity-clientauthentication
            '''
            result = self._values.get("client_authentication")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityClientAuthenticationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConnectivityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.VpcConnectivitySaslProperty",
        jsii_struct_bases=[],
        name_mapping={"iam": "iam", "scram": "scram"},
    )
    class VpcConnectivitySaslProperty:
        def __init__(
            self,
            *,
            iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.VpcConnectivityIamProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scram: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.VpcConnectivityScramProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Details for client authentication using SASL for VpcConnectivity.

            :param iam: Details for ClientAuthentication using IAM for VpcConnectivity.
            :param scram: Details for SASL/SCRAM client authentication for VpcConnectivity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitysasl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                vpc_connectivity_sasl_property = msk.CfnCluster.VpcConnectivitySaslProperty(
                    iam=msk.CfnCluster.VpcConnectivityIamProperty(
                        enabled=False
                    ),
                    scram=msk.CfnCluster.VpcConnectivityScramProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4def981e5112f53e8d00d2d997ca4fc2dced1503609d5d3dbf0ada48233955c9)
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
                check_type(argname="argument scram", value=scram, expected_type=type_hints["scram"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam is not None:
                self._values["iam"] = iam
            if scram is not None:
                self._values["scram"] = scram

        @builtins.property
        def iam(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityIamProperty"]]:
            '''Details for ClientAuthentication using IAM for VpcConnectivity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitysasl.html#cfn-msk-cluster-vpcconnectivitysasl-iam
            '''
            result = self._values.get("iam")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityIamProperty"]], result)

        @builtins.property
        def scram(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityScramProperty"]]:
            '''Details for SASL/SCRAM client authentication for VpcConnectivity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitysasl.html#cfn-msk-cluster-vpcconnectivitysasl-scram
            '''
            result = self._values.get("scram")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.VpcConnectivityScramProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConnectivitySaslProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.VpcConnectivityScramProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class VpcConnectivityScramProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Details for SASL/SCRAM client authentication for vpcConnectivity.

            :param enabled: SASL/SCRAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityscram.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                vpc_connectivity_scram_property = msk.CfnCluster.VpcConnectivityScramProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__590953329462cef4268f1836b866c7762497b37a8fb927c40904bd970a43a093)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''SASL/SCRAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityscram.html#cfn-msk-cluster-vpcconnectivityscram-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConnectivityScramProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnCluster.VpcConnectivityTlsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class VpcConnectivityTlsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Details for client authentication using TLS for vpcConnectivity.

            :param enabled: TLS authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitytls.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                vpc_connectivity_tls_property = msk.CfnCluster.VpcConnectivityTlsProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1ebbb8eb7816ab0289a799ad732a769be10fd2ffc65eb2b9063e29926b8c666)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''TLS authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitytls.html#cfn-msk-cluster-vpcconnectivitytls-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConnectivityTlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnClusterPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_msk.CfnClusterPolicy",
):
    '''Create or update cluster policy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-clusterpolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_msk as msk
        
        # policy: Any
        
        cfn_cluster_policy = msk.CfnClusterPolicy(self, "MyCfnClusterPolicy",
            cluster_arn="clusterArn",
            policy=policy
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_arn: builtins.str,
        policy: typing.Any,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_arn: The Amazon Resource Name (ARN) that uniquely identifies the cluster.
        :param policy: Resource policy for the cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44054483e71e00fc0cc8de4a0043676504f8ba8eaef21e7597ca21b373e44603)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterPolicyProps(cluster_arn=cluster_arn, policy=policy)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e41ea5fb477004886aab316f78fa36c6fd72bf6557b1aea9f0737df5334430)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21fbce7be053dc3f37ff6c8f36600bf6a0504c9f6d8d09dba26e4a3b285eac97)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCurrentVersion")
    def attr_current_version(self) -> builtins.str:
        '''The current version of the policy attached to the specified cluster.

        :cloudformationAttribute: CurrentVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCurrentVersion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that uniquely identifies the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09b7d2ce80727605483c1cca4ed70ac9461a14d815999af721ff88f333a832ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''Resource policy for the cluster.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aef09b3a5d4bfa3988541299905c0c1343ea985547573352e5a08b0a13c9243)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_msk.CfnClusterPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn", "policy": "policy"},
)
class CfnClusterPolicyProps:
    def __init__(self, *, cluster_arn: builtins.str, policy: typing.Any) -> None:
        '''Properties for defining a ``CfnClusterPolicy``.

        :param cluster_arn: The Amazon Resource Name (ARN) that uniquely identifies the cluster.
        :param policy: Resource policy for the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-clusterpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_msk as msk
            
            # policy: Any
            
            cfn_cluster_policy_props = msk.CfnClusterPolicyProps(
                cluster_arn="clusterArn",
                policy=policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38038309c072b4b939104fe0c0f44c2fecc6424084abe3716435939cb1b8c00)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
            "policy": policy,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that uniquely identifies the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-clusterpolicy.html#cfn-msk-clusterpolicy-clusterarn
        '''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''Resource policy for the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-clusterpolicy.html#cfn-msk-clusterpolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_msk.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "broker_node_group_info": "brokerNodeGroupInfo",
        "cluster_name": "clusterName",
        "kafka_version": "kafkaVersion",
        "number_of_broker_nodes": "numberOfBrokerNodes",
        "client_authentication": "clientAuthentication",
        "configuration_info": "configurationInfo",
        "current_version": "currentVersion",
        "encryption_info": "encryptionInfo",
        "enhanced_monitoring": "enhancedMonitoring",
        "logging_info": "loggingInfo",
        "open_monitoring": "openMonitoring",
        "storage_mode": "storageMode",
        "tags": "tags",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        broker_node_group_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, typing.Dict[builtins.str, typing.Any]]],
        cluster_name: builtins.str,
        kafka_version: builtins.str,
        number_of_broker_nodes: jsii.Number,
        client_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        configuration_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        current_version: typing.Optional[builtins.str] = None,
        encryption_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EncryptionInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        enhanced_monitoring: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.LoggingInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        open_monitoring: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.OpenMonitoringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        storage_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param broker_node_group_info: Information about the broker nodes in the cluster.
        :param cluster_name: The name of the cluster.
        :param kafka_version: The version of Apache Kafka. You can use Amazon MSK to create clusters that use Apache Kafka versions 1.1.1 and 2.2.1.
        :param number_of_broker_nodes: The number of broker nodes in the cluster.
        :param client_authentication: Includes all client authentication related information.
        :param configuration_info: Represents the configuration that you want MSK to use for the cluster.
        :param current_version: The version of the cluster that you want to update.
        :param encryption_info: Includes all encryption-related information.
        :param enhanced_monitoring: Specifies the level of monitoring for the MSK cluster. The possible values are ``DEFAULT`` , ``PER_BROKER`` , and ``PER_TOPIC_PER_BROKER`` .
        :param logging_info: Logging Info details.
        :param open_monitoring: The settings for open monitoring.
        :param storage_mode: This controls storage mode for supported storage tiers.
        :param tags: Create tags when creating the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_msk as msk
            
            cfn_cluster_props = msk.CfnClusterProps(
                broker_node_group_info=msk.CfnCluster.BrokerNodeGroupInfoProperty(
                    client_subnets=["clientSubnets"],
                    instance_type="instanceType",
            
                    # the properties below are optional
                    broker_az_distribution="brokerAzDistribution",
                    connectivity_info=msk.CfnCluster.ConnectivityInfoProperty(
                        public_access=msk.CfnCluster.PublicAccessProperty(
                            type="type"
                        ),
                        vpc_connectivity=msk.CfnCluster.VpcConnectivityProperty(
                            client_authentication=msk.CfnCluster.VpcConnectivityClientAuthenticationProperty(
                                sasl=msk.CfnCluster.VpcConnectivitySaslProperty(
                                    iam=msk.CfnCluster.VpcConnectivityIamProperty(
                                        enabled=False
                                    ),
                                    scram=msk.CfnCluster.VpcConnectivityScramProperty(
                                        enabled=False
                                    )
                                ),
                                tls=msk.CfnCluster.VpcConnectivityTlsProperty(
                                    enabled=False
                                )
                            )
                        )
                    ),
                    security_groups=["securityGroups"],
                    storage_info=msk.CfnCluster.StorageInfoProperty(
                        ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                            provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                                enabled=False,
                                volume_throughput=123
                            ),
                            volume_size=123
                        )
                    )
                ),
                cluster_name="clusterName",
                kafka_version="kafkaVersion",
                number_of_broker_nodes=123,
            
                # the properties below are optional
                client_authentication=msk.CfnCluster.ClientAuthenticationProperty(
                    sasl=msk.CfnCluster.SaslProperty(
                        iam=msk.CfnCluster.IamProperty(
                            enabled=False
                        ),
                        scram=msk.CfnCluster.ScramProperty(
                            enabled=False
                        )
                    ),
                    tls=msk.CfnCluster.TlsProperty(
                        certificate_authority_arn_list=["certificateAuthorityArnList"],
                        enabled=False
                    ),
                    unauthenticated=msk.CfnCluster.UnauthenticatedProperty(
                        enabled=False
                    )
                ),
                configuration_info=msk.CfnCluster.ConfigurationInfoProperty(
                    arn="arn",
                    revision=123
                ),
                current_version="currentVersion",
                encryption_info=msk.CfnCluster.EncryptionInfoProperty(
                    encryption_at_rest=msk.CfnCluster.EncryptionAtRestProperty(
                        data_volume_kms_key_id="dataVolumeKmsKeyId"
                    ),
                    encryption_in_transit=msk.CfnCluster.EncryptionInTransitProperty(
                        client_broker="clientBroker",
                        in_cluster=False
                    )
                ),
                enhanced_monitoring="enhancedMonitoring",
                logging_info=msk.CfnCluster.LoggingInfoProperty(
                    broker_logs=msk.CfnCluster.BrokerLogsProperty(
                        cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                            enabled=False,
            
                            # the properties below are optional
                            log_group="logGroup"
                        ),
                        firehose=msk.CfnCluster.FirehoseProperty(
                            enabled=False,
            
                            # the properties below are optional
                            delivery_stream="deliveryStream"
                        ),
                        s3=msk.CfnCluster.S3Property(
                            enabled=False,
            
                            # the properties below are optional
                            bucket="bucket",
                            prefix="prefix"
                        )
                    )
                ),
                open_monitoring=msk.CfnCluster.OpenMonitoringProperty(
                    prometheus=msk.CfnCluster.PrometheusProperty(
                        jmx_exporter=msk.CfnCluster.JmxExporterProperty(
                            enabled_in_broker=False
                        ),
                        node_exporter=msk.CfnCluster.NodeExporterProperty(
                            enabled_in_broker=False
                        )
                    )
                ),
                storage_mode="storageMode",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da9c2c389b7fb44efe639e45c2911a96139b86d7a936606322d8605aedb52b8b)
            check_type(argname="argument broker_node_group_info", value=broker_node_group_info, expected_type=type_hints["broker_node_group_info"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument kafka_version", value=kafka_version, expected_type=type_hints["kafka_version"])
            check_type(argname="argument number_of_broker_nodes", value=number_of_broker_nodes, expected_type=type_hints["number_of_broker_nodes"])
            check_type(argname="argument client_authentication", value=client_authentication, expected_type=type_hints["client_authentication"])
            check_type(argname="argument configuration_info", value=configuration_info, expected_type=type_hints["configuration_info"])
            check_type(argname="argument current_version", value=current_version, expected_type=type_hints["current_version"])
            check_type(argname="argument encryption_info", value=encryption_info, expected_type=type_hints["encryption_info"])
            check_type(argname="argument enhanced_monitoring", value=enhanced_monitoring, expected_type=type_hints["enhanced_monitoring"])
            check_type(argname="argument logging_info", value=logging_info, expected_type=type_hints["logging_info"])
            check_type(argname="argument open_monitoring", value=open_monitoring, expected_type=type_hints["open_monitoring"])
            check_type(argname="argument storage_mode", value=storage_mode, expected_type=type_hints["storage_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "broker_node_group_info": broker_node_group_info,
            "cluster_name": cluster_name,
            "kafka_version": kafka_version,
            "number_of_broker_nodes": number_of_broker_nodes,
        }
        if client_authentication is not None:
            self._values["client_authentication"] = client_authentication
        if configuration_info is not None:
            self._values["configuration_info"] = configuration_info
        if current_version is not None:
            self._values["current_version"] = current_version
        if encryption_info is not None:
            self._values["encryption_info"] = encryption_info
        if enhanced_monitoring is not None:
            self._values["enhanced_monitoring"] = enhanced_monitoring
        if logging_info is not None:
            self._values["logging_info"] = logging_info
        if open_monitoring is not None:
            self._values["open_monitoring"] = open_monitoring
        if storage_mode is not None:
            self._values["storage_mode"] = storage_mode
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def broker_node_group_info(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCluster.BrokerNodeGroupInfoProperty]:
        '''Information about the broker nodes in the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-brokernodegroupinfo
        '''
        result = self._values.get("broker_node_group_info")
        assert result is not None, "Required property 'broker_node_group_info' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCluster.BrokerNodeGroupInfoProperty], result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kafka_version(self) -> builtins.str:
        '''The version of Apache Kafka.

        You can use Amazon MSK to create clusters that use Apache Kafka versions 1.1.1 and 2.2.1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-kafkaversion
        '''
        result = self._values.get("kafka_version")
        assert result is not None, "Required property 'kafka_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_of_broker_nodes(self) -> jsii.Number:
        '''The number of broker nodes in the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-numberofbrokernodes
        '''
        result = self._values.get("number_of_broker_nodes")
        assert result is not None, "Required property 'number_of_broker_nodes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def client_authentication(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ClientAuthenticationProperty]]:
        '''Includes all client authentication related information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication
        '''
        result = self._values.get("client_authentication")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ClientAuthenticationProperty]], result)

    @builtins.property
    def configuration_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ConfigurationInfoProperty]]:
        '''Represents the configuration that you want MSK to use for the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo
        '''
        result = self._values.get("configuration_info")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ConfigurationInfoProperty]], result)

    @builtins.property
    def current_version(self) -> typing.Optional[builtins.str]:
        '''The version of the cluster that you want to update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-currentversion
        '''
        result = self._values.get("current_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EncryptionInfoProperty]]:
        '''Includes all encryption-related information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo
        '''
        result = self._values.get("encryption_info")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EncryptionInfoProperty]], result)

    @builtins.property
    def enhanced_monitoring(self) -> typing.Optional[builtins.str]:
        '''Specifies the level of monitoring for the MSK cluster.

        The possible values are ``DEFAULT`` , ``PER_BROKER`` , and ``PER_TOPIC_PER_BROKER`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring
        '''
        result = self._values.get("enhanced_monitoring")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.LoggingInfoProperty]]:
        '''Logging Info details.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo
        '''
        result = self._values.get("logging_info")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.LoggingInfoProperty]], result)

    @builtins.property
    def open_monitoring(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.OpenMonitoringProperty]]:
        '''The settings for open monitoring.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring
        '''
        result = self._values.get("open_monitoring")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.OpenMonitoringProperty]], result)

    @builtins.property
    def storage_mode(self) -> typing.Optional[builtins.str]:
        '''This controls storage mode for supported storage tiers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-storagemode
        '''
        result = self._values.get("storage_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Create tags when creating the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_msk.CfnConfiguration",
):
    '''Creates a new MSK configuration.

    To see an example of how to use this operation, first save the following text to a file and name the file config-file.txt .

    ``auto.create.topics.enable = true zookeeper.connection.timeout.ms = 1000 log.roll.ms = 604800000``

    Now run the following Python 3.6 script in the folder where you saved config-file.txt . This script uses the properties specified in config-file.txt to create a configuration named ``SalesClusterConfiguration`` . This configuration can work with Apache Kafka versions 1.1.1 and 2.1.0::

       import boto3 client = boto3.client('kafka') config_file = open('config-file.txt', 'r') server_properties = config_file.read() response = client.create_configuration( Name='SalesClusterConfiguration', Description='The configuration to use on all sales clusters.', KafkaVersions=['1.1.1', '2.1.0'], ServerProperties=server_properties
       ) print(response)

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_msk as msk
        
        cfn_configuration = msk.CfnConfiguration(self, "MyCfnConfiguration",
            name="name",
            server_properties="serverProperties",
        
            # the properties below are optional
            description="description",
            kafka_versions_list=["kafkaVersionsList"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        server_properties: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kafka_versions_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".
        :param server_properties: Contents of the server.properties file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of server.properties can be in plaintext.
        :param description: The description of the configuration.
        :param kafka_versions_list: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4496d16ab1313e2d6e75f55fc7cdb170962f756c6dc1149245dde1aba3113278)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationProps(
            name=name,
            server_properties=server_properties,
            description=description,
            kafka_versions_list=kafka_versions_list,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b6ce2f411d76bf4b2b3474cef8479b35e9ee5b510006374b01da6c190c75122)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16507eb4f28818c143dcf5097c6c3698548e9010896ca453caaba8d8485407ea)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__695b362a9c27a703acdb4ba2dc747ecd9bf0d1b9ee70bd3ddb5779e480e245b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serverProperties")
    def server_properties(self) -> builtins.str:
        '''Contents of the server.properties file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of server.properties can be in plaintext.'''
        return typing.cast(builtins.str, jsii.get(self, "serverProperties"))

    @server_properties.setter
    def server_properties(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08908c3ec78b02789cf18a674a51767e0dc8877a5b7ac431220532a095ede42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverProperties", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3501ea47e4e919fbc2daf2fd53e8984fb942ca686b649caea79b13ce7ab95a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaVersionsList")
    def kafka_versions_list(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "kafkaVersionsList"))

    @kafka_versions_list.setter
    def kafka_versions_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663ee4ade66592e09fdfc891c94c07473d9e23f4b22eb0b252881053695ff63b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaVersionsList", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_msk.CfnConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "server_properties": "serverProperties",
        "description": "description",
        "kafka_versions_list": "kafkaVersionsList",
    },
)
class CfnConfigurationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        server_properties: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kafka_versions_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguration``.

        :param name: The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".
        :param server_properties: Contents of the server.properties file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of server.properties can be in plaintext.
        :param description: The description of the configuration.
        :param kafka_versions_list: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_msk as msk
            
            cfn_configuration_props = msk.CfnConfigurationProps(
                name="name",
                server_properties="serverProperties",
            
                # the properties below are optional
                description="description",
                kafka_versions_list=["kafkaVersionsList"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b67dfeeec9a4e27fb21b4b14fa3d51255f49590431c2ab861b81fad91473dd5)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument server_properties", value=server_properties, expected_type=type_hints["server_properties"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kafka_versions_list", value=kafka_versions_list, expected_type=type_hints["kafka_versions_list"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "server_properties": server_properties,
        }
        if description is not None:
            self._values["description"] = description
        if kafka_versions_list is not None:
            self._values["kafka_versions_list"] = kafka_versions_list

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the configuration.

        Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_properties(self) -> builtins.str:
        '''Contents of the server.properties file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of server.properties can be in plaintext.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-serverproperties
        '''
        result = self._values.get("server_properties")
        assert result is not None, "Required property 'server_properties' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kafka_versions_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-kafkaversionslist
        '''
        result = self._values.get("kafka_versions_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnServerlessCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_msk.CfnServerlessCluster",
):
    '''Resource Type definition for AWS::MSK::ServerlessCluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_msk as msk
        
        cfn_serverless_cluster = msk.CfnServerlessCluster(self, "MyCfnServerlessCluster",
            client_authentication=msk.CfnServerlessCluster.ClientAuthenticationProperty(
                sasl=msk.CfnServerlessCluster.SaslProperty(
                    iam=msk.CfnServerlessCluster.IamProperty(
                        enabled=False
                    )
                )
            ),
            cluster_name="clusterName",
            vpc_configs=[msk.CfnServerlessCluster.VpcConfigProperty(
                subnet_ids=["subnetIds"],
        
                # the properties below are optional
                security_groups=["securityGroups"]
            )],
        
            # the properties below are optional
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        client_authentication: typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCluster.ClientAuthenticationProperty", typing.Dict[builtins.str, typing.Any]]],
        cluster_name: builtins.str,
        vpc_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCluster.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param client_authentication: 
        :param cluster_name: 
        :param vpc_configs: 
        :param tags: A key-value pair to associate with a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef99cf7cce653b94ea5543af8d6966cab3ba1c8ff81b50f8736048fff8227ff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServerlessClusterProps(
            client_authentication=client_authentication,
            cluster_name=cluster_name,
            vpc_configs=vpc_configs,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6fcda27bf38beaaece2345e24c9ba42a7a611c55e20c87352dcd2f48c3d3b8c)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da58f0cde72fe87dba0e293a65768a7fe5d722e0a1db075b46ff438eff4833d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="clientAuthentication")
    def client_authentication(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.ClientAuthenticationProperty"]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.ClientAuthenticationProperty"], jsii.get(self, "clientAuthentication"))

    @client_authentication.setter
    def client_authentication(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.ClientAuthenticationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa89ccfc74c544ca6be404bf89aba0bb0165e1448da8fe2625fe0b16b1233007)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f72f4a1e482f09869114e6642c0c6d4876a0d1f1f71f63585d48a4947074646e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfigs")
    def vpc_configs(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.VpcConfigProperty"]]]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.VpcConfigProperty"]]], jsii.get(self, "vpcConfigs"))

    @vpc_configs.setter
    def vpc_configs(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.VpcConfigProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb1ce933052056e6636b2d8196e831285d5d488108aa04cd5e5edf99126c9ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A key-value pair to associate with a resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3b6a10ef556854108c6599fa2fb551287d8a71429ee2a81ceed14943ec4254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnServerlessCluster.ClientAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"sasl": "sasl"},
    )
    class ClientAuthenticationProperty:
        def __init__(
            self,
            *,
            sasl: typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCluster.SaslProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Includes all client authentication information.

            :param sasl: Details for client authentication using SASL. To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                client_authentication_property = msk.CfnServerlessCluster.ClientAuthenticationProperty(
                    sasl=msk.CfnServerlessCluster.SaslProperty(
                        iam=msk.CfnServerlessCluster.IamProperty(
                            enabled=False
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67169aa496dc60cc3cf56e6d1e02f1b57752bd808270ae972957475903226523)
                check_type(argname="argument sasl", value=sasl, expected_type=type_hints["sasl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sasl": sasl,
            }

        @builtins.property
        def sasl(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.SaslProperty"]:
            '''Details for client authentication using SASL.

            To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html#cfn-msk-serverlesscluster-clientauthentication-sasl
            '''
            result = self._values.get("sasl")
            assert result is not None, "Required property 'sasl' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.SaslProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnServerlessCluster.IamProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class IamProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Details for SASL/IAM client authentication.

            :param enabled: SASL/IAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                iam_property = msk.CfnServerlessCluster.IamProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab5f4c28a418e764a406acaca2f69f2e571164e27a81e4f6f0465c591d1c296e)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''SASL/IAM authentication is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html#cfn-msk-serverlesscluster-iam-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnServerlessCluster.SaslProperty",
        jsii_struct_bases=[],
        name_mapping={"iam": "iam"},
    )
    class SaslProperty:
        def __init__(
            self,
            *,
            iam: typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCluster.IamProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Details for client authentication using SASL.

            To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :param iam: Details for ClientAuthentication using IAM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                sasl_property = msk.CfnServerlessCluster.SaslProperty(
                    iam=msk.CfnServerlessCluster.IamProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c1db2d2fc97ad455dce26d20c405cce704978d11074860fa04724f7c3bedba46)
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "iam": iam,
            }

        @builtins.property
        def iam(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.IamProperty"]:
            '''Details for ClientAuthentication using IAM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html#cfn-msk-serverlesscluster-sasl-iam
            '''
            result = self._values.get("iam")
            assert result is not None, "Required property 'iam' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnServerlessCluster.IamProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SaslProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_msk.CfnServerlessCluster.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "security_groups": "securityGroups"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param subnet_ids: 
            :param security_groups: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_msk as msk
                
                vpc_config_property = msk.CfnServerlessCluster.VpcConfigProperty(
                    subnet_ids=["subnetIds"],
                
                    # the properties below are optional
                    security_groups=["securityGroups"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e04f40675549e758de2257c70e72d28f4b93b50c2c684c533c793f5712b0c42b)
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_ids": subnet_ids,
            }
            if security_groups is not None:
                self._values["security_groups"] = security_groups

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html#cfn-msk-serverlesscluster-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html#cfn-msk-serverlesscluster-vpcconfig-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_msk.CfnServerlessClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "client_authentication": "clientAuthentication",
        "cluster_name": "clusterName",
        "vpc_configs": "vpcConfigs",
        "tags": "tags",
    },
)
class CfnServerlessClusterProps:
    def __init__(
        self,
        *,
        client_authentication: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCluster.ClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]],
        cluster_name: builtins.str,
        vpc_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCluster.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServerlessCluster``.

        :param client_authentication: 
        :param cluster_name: 
        :param vpc_configs: 
        :param tags: A key-value pair to associate with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_msk as msk
            
            cfn_serverless_cluster_props = msk.CfnServerlessClusterProps(
                client_authentication=msk.CfnServerlessCluster.ClientAuthenticationProperty(
                    sasl=msk.CfnServerlessCluster.SaslProperty(
                        iam=msk.CfnServerlessCluster.IamProperty(
                            enabled=False
                        )
                    )
                ),
                cluster_name="clusterName",
                vpc_configs=[msk.CfnServerlessCluster.VpcConfigProperty(
                    subnet_ids=["subnetIds"],
            
                    # the properties below are optional
                    security_groups=["securityGroups"]
                )],
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c714eb0299c64ab481c3d39d1e14117755189081833a87372e9f1a245f1ecadc)
            check_type(argname="argument client_authentication", value=client_authentication, expected_type=type_hints["client_authentication"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument vpc_configs", value=vpc_configs, expected_type=type_hints["vpc_configs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_authentication": client_authentication,
            "cluster_name": cluster_name,
            "vpc_configs": vpc_configs,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def client_authentication(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnServerlessCluster.ClientAuthenticationProperty]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-clientauthentication
        '''
        result = self._values.get("client_authentication")
        assert result is not None, "Required property 'client_authentication' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnServerlessCluster.ClientAuthenticationProperty], result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_configs(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnServerlessCluster.VpcConfigProperty]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-vpcconfigs
        '''
        result = self._values.get("vpc_configs")
        assert result is not None, "Required property 'vpc_configs' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnServerlessCluster.VpcConfigProperty]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A key-value pair to associate with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerlessClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVpcConnection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_msk.CfnVpcConnection",
):
    '''Create remote VPC connection.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_msk as msk
        
        cfn_vpc_connection = msk.CfnVpcConnection(self, "MyCfnVpcConnection",
            authentication="authentication",
            client_subnets=["clientSubnets"],
            security_groups=["securityGroups"],
            target_cluster_arn="targetClusterArn",
            vpc_id="vpcId",
        
            # the properties below are optional
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authentication: builtins.str,
        client_subnets: typing.Sequence[builtins.str],
        security_groups: typing.Sequence[builtins.str],
        target_cluster_arn: builtins.str,
        vpc_id: builtins.str,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authentication: The type of private link authentication.
        :param client_subnets: The list of subnets in the client VPC to connect to.
        :param security_groups: The security groups to attach to the ENIs for the broker nodes.
        :param target_cluster_arn: The Amazon Resource Name (ARN) of the cluster.
        :param vpc_id: The VPC id of the remote client.
        :param tags: Create tags when creating the VPC connection.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__910be42f1d726644d84801975cd038e26103e9dbcfb02007fe4ebdbeb62c3af8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcConnectionProps(
            authentication=authentication,
            client_subnets=client_subnets,
            security_groups=security_groups,
            target_cluster_arn=target_cluster_arn,
            vpc_id=vpc_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f62710c804cf37e90d67ca3091c8bf2c71fdbad4e6eb3fc7637201e5e0c4da4)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b69e634ecb8c0c7b4c669a0bfa1d695be753962b5974c42bd0023a5d04676b6b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the VPC connection.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="authentication")
    def authentication(self) -> builtins.str:
        '''The type of private link authentication.'''
        return typing.cast(builtins.str, jsii.get(self, "authentication"))

    @authentication.setter
    def authentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4bd4b61163da39025a8cd09f1db5ecb199b74eb65e9556bf978064fa079e367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authentication", value)

    @builtins.property
    @jsii.member(jsii_name="clientSubnets")
    def client_subnets(self) -> typing.List[builtins.str]:
        '''The list of subnets in the client VPC to connect to.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clientSubnets"))

    @client_subnets.setter
    def client_subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a077d01ed7d7a5f35c6b0cc72e4a77856d510210db08615ab88c969362c05d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSubnets", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        '''The security groups to attach to the ENIs for the broker nodes.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2ef79840a03fa0d4be5b71a3f639c366a7f8df914fc8ec7f54b778fc71ed809)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="targetClusterArn")
    def target_cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "targetClusterArn"))

    @target_cluster_arn.setter
    def target_cluster_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c908df90f79d47c80725c4c1a1ab47b0a3101ba904f6bbb93e09324deb30d3ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetClusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The VPC id of the remote client.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7312d322f4e2b55e3a62ef768de9469e6ea2f6745665206380cde67b5c1212a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Create tags when creating the VPC connection.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41badc74ff47dd490e87b936855f3c939b6636c7093dafa31681ef018b5a53f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_msk.CfnVpcConnectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication": "authentication",
        "client_subnets": "clientSubnets",
        "security_groups": "securityGroups",
        "target_cluster_arn": "targetClusterArn",
        "vpc_id": "vpcId",
        "tags": "tags",
    },
)
class CfnVpcConnectionProps:
    def __init__(
        self,
        *,
        authentication: builtins.str,
        client_subnets: typing.Sequence[builtins.str],
        security_groups: typing.Sequence[builtins.str],
        target_cluster_arn: builtins.str,
        vpc_id: builtins.str,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVpcConnection``.

        :param authentication: The type of private link authentication.
        :param client_subnets: The list of subnets in the client VPC to connect to.
        :param security_groups: The security groups to attach to the ENIs for the broker nodes.
        :param target_cluster_arn: The Amazon Resource Name (ARN) of the cluster.
        :param vpc_id: The VPC id of the remote client.
        :param tags: Create tags when creating the VPC connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_msk as msk
            
            cfn_vpc_connection_props = msk.CfnVpcConnectionProps(
                authentication="authentication",
                client_subnets=["clientSubnets"],
                security_groups=["securityGroups"],
                target_cluster_arn="targetClusterArn",
                vpc_id="vpcId",
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9e41b66e732883ec8194c58e0cffc38f5c68ed0844d8a4d98e59893d73fcc20)
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument client_subnets", value=client_subnets, expected_type=type_hints["client_subnets"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument target_cluster_arn", value=target_cluster_arn, expected_type=type_hints["target_cluster_arn"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication": authentication,
            "client_subnets": client_subnets,
            "security_groups": security_groups,
            "target_cluster_arn": target_cluster_arn,
            "vpc_id": vpc_id,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def authentication(self) -> builtins.str:
        '''The type of private link authentication.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-authentication
        '''
        result = self._values.get("authentication")
        assert result is not None, "Required property 'authentication' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_subnets(self) -> typing.List[builtins.str]:
        '''The list of subnets in the client VPC to connect to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-clientsubnets
        '''
        result = self._values.get("client_subnets")
        assert result is not None, "Required property 'client_subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.List[builtins.str]:
        '''The security groups to attach to the ENIs for the broker nodes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-securitygroups
        '''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target_cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-targetclusterarn
        '''
        result = self._values.get("target_cluster_arn")
        assert result is not None, "Required property 'target_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VPC id of the remote client.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Create tags when creating the VPC connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBatchScramSecret",
    "CfnBatchScramSecretProps",
    "CfnCluster",
    "CfnClusterPolicy",
    "CfnClusterPolicyProps",
    "CfnClusterProps",
    "CfnConfiguration",
    "CfnConfigurationProps",
    "CfnServerlessCluster",
    "CfnServerlessClusterProps",
    "CfnVpcConnection",
    "CfnVpcConnectionProps",
]

publication.publish()

def _typecheckingstub__7520d411e2ff468c392c477234cb67e342bdaac914895933d982e659ed9e98a4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_arn: builtins.str,
    secret_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__679b387dd09502af5e68247cbc9ed47cc232efe312a69c5e818c44c3f82bcee8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e8eba3e20dbf60522bfba10c756fea4acf485adb651a7cd021b3f5ceccf21f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb6bef82c23e1fc360009001db2ac936df9869c3c9c3008b243c52c51886fb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef33f5d92a61738839f87ca9e67498a1c64fa095dbc67d26fe3e3ae929735e2d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f9f8128f7dc818d3ee4d75c78613bf29636c365b9489e1c33d4a21448b3e2ea(
    *,
    cluster_arn: builtins.str,
    secret_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d267b4b2dcfdda539084655e7a1234ffaf8e77376f37d4914abbcef6c64e9f1c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    broker_node_group_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    cluster_name: builtins.str,
    kafka_version: builtins.str,
    number_of_broker_nodes: jsii.Number,
    client_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    configuration_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    current_version: typing.Optional[builtins.str] = None,
    encryption_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EncryptionInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enhanced_monitoring: typing.Optional[builtins.str] = None,
    logging_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.LoggingInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_monitoring: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.OpenMonitoringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    storage_mode: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb968e1959d50cf1bb135024a884cb1b17c21f705387b0b62807f105e8a0d30(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df344cadfa45c9bb1712b8cad17b0d6602d82780e8cbec4bb3b2a50415412457(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeca16d7c9434917e084167a4ad53ae5c40e801a27aef3671a5877ed561da8a0(
    value: typing.Union[_IResolvable_da3f097b, CfnCluster.BrokerNodeGroupInfoProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcdf905665c7a5fe4197fd1e4b97211937857f4e1c57b49a985ba6d4d9945dbb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41bb94e6290c69323fb75c013c4b7142158d540e2c1ec140bb735044d90aa917(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__871153d778d14d527bd03c5c339f4f5c01216c5dcf58a168dbc3acf07aa35aaa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999b897b28c870a68a155dbce687b5d48e1be0223338cc26b1ccdaa28b955337(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ClientAuthenticationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68aea3aaba18dee8b678c7f7677ecae9ed107f4b596657a2f2b8f07f997fd4b9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ConfigurationInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a8f0655017a6d4bd71c8a5f323f7ff60bcb57c9c789abc6ca61aae0054113c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cf20bb9e6c8edb93f172bf898cbe430e546eddc2d98fe341b62587d35bfcc26(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EncryptionInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a39e87ead1cc0622445b0fffb621eed514d654f142e65433d0ddca8025d62a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d382c4554000521a60f4a1e25f292506a5889f9f704479e32e61cccc944357e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.LoggingInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75fe28c1f9a57617ff0d6a9ccd61b13cd12fe2b29f73cace2349bfc4cd46f2d8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.OpenMonitoringProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbed80e4a8389757f50e4ac3a00ab70f0b1864d27b5014ae9d52159bbb42ee2d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25d99a2495a599ba3309403ed99fa0b41d839c07974463afbd155e81c63d4c5(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd8029dbfc62bcbd4abadd3745c2e188c7166e8208e634cad8832a450ab294f(
    *,
    cloud_watch_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.CloudWatchLogsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.FirehoseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.S3Property, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__047ba5870776adf805ab38c9eed596d6715e6bfa45af6eaf20ea7bd91858fe82(
    *,
    client_subnets: typing.Sequence[builtins.str],
    instance_type: builtins.str,
    broker_az_distribution: typing.Optional[builtins.str] = None,
    connectivity_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConnectivityInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.StorageInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe35787c5f8943b4dbd478e4334e34a43f1b34cb667d5f716a5cc08d74b0c36f(
    *,
    sasl: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SaslProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.TlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    unauthenticated: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.UnauthenticatedProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ae6e10d35688641429fe8898b54dccb7dea8409c6cbb770ae30bfd8f89d95f2(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    log_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978657c9cf18466215b38a251ae4816196dcec1b76c8a82c67f970ce40d345d6(
    *,
    arn: builtins.str,
    revision: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ba9dbd3fe54fc52707e8245c99f4e132a975a1ea7784a9e8d49cfc50fc4d71(
    *,
    public_access: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.PublicAccessProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_connectivity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.VpcConnectivityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d93be124fa1756365f8d601bf56551024d16dd8697368298f887f35cf9197d1(
    *,
    provisioned_throughput: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ProvisionedThroughputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    volume_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__601ca97f7a025a112252de96abad1ce870ae78db8a5372a4f216bbcf2cd01cd0(
    *,
    data_volume_kms_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8817cd1ddb22712cb54e76ff0e0f3ebc61e27a1912efefd032c5a2f9dcc2038d(
    *,
    client_broker: typing.Optional[builtins.str] = None,
    in_cluster: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82b72539c93ffe289109f6da6a4a0dc5b1c4add6c3a5cbe84285e37c9b72ff69(
    *,
    encryption_at_rest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EncryptionAtRestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_in_transit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EncryptionInTransitProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79bdccdd0f4d9e13c3d92e4a9740538786951fc032dbc4c30a6c9c2d68bd88fb(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    delivery_stream: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9d17d5e61df7419a4db466a2ddaea0429b28f4b26e639fb8a605c2a99675af(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eaa737fdd4b761b60d33bd8c66551298c9e7beeb94798e2b9eb9a3cba4f2ba2(
    *,
    enabled_in_broker: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb34e9e4e6ea2dca1d1d7c205b60cf5fc069f6150273b5e5c14b565ef784c6cb(
    *,
    broker_logs: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.BrokerLogsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d21596c86d0237daafa3a630b632d9dd4d16bbca82f174eed700401353061e16(
    *,
    enabled_in_broker: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3d6046a8f5a7d026e4209e2c3faee856baceff5b3f885a18150ec399cb71fc(
    *,
    prometheus: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.PrometheusProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00cf2d2430d38c9e9785d442acfabb344902a11bc9223bd80e26d7f514ec937(
    *,
    jmx_exporter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.JmxExporterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    node_exporter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.NodeExporterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9bf430fec171ea7e825c41378e4aa35d667362efc4d0d9740db3be3e7115fc9(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    volume_throughput: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c0f11124e397d2c64c42ed84e0f41e63fe036a5dbb8354d7b0a83fdda7780e(
    *,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802632a907f2036c840a19e8b3c37b50084fc2617376e08f1ea1e98f4a19a35b(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    bucket: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23ccb244e3353b35264d16f3e5f20f74f507bc5860a069055a60699937fe795f(
    *,
    iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.IamProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scram: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ScramProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1632715500ba54afdd5784104a92272b1cfc744370d3cd691bf47a18a76a51bf(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e19ae4f693f8d16bb984b14c4e276ce1ffdc97a798ba373aec65fa283e8287(
    *,
    ebs_storage_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EBSStorageInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201ae89a334d1d435bfafb97fb7a10c1da455123e9315bef634f525af54ad4c3(
    *,
    certificate_authority_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627a4f01251f0f7c34b63f12ac75b6581855292444a20ea6f8073e1881f3e9ff(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5aa63eea4121f8cf76d7698bbb8b609934b88b26b3bd2f092229d6eeefb620c(
    *,
    sasl: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.VpcConnectivitySaslProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.VpcConnectivityTlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d2babe34af394074220ca9baba7827ab597d8d49eb25997ebb1c5b9df10f5e9(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81a77b1701714a33de616ece55afe0c2081e30511acc3ac1fe97c941379866c1(
    *,
    client_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.VpcConnectivityClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4def981e5112f53e8d00d2d997ca4fc2dced1503609d5d3dbf0ada48233955c9(
    *,
    iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.VpcConnectivityIamProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scram: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.VpcConnectivityScramProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590953329462cef4268f1836b866c7762497b37a8fb927c40904bd970a43a093(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ebbb8eb7816ab0289a799ad732a769be10fd2ffc65eb2b9063e29926b8c666(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44054483e71e00fc0cc8de4a0043676504f8ba8eaef21e7597ca21b373e44603(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_arn: builtins.str,
    policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e41ea5fb477004886aab316f78fa36c6fd72bf6557b1aea9f0737df5334430(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21fbce7be053dc3f37ff6c8f36600bf6a0504c9f6d8d09dba26e4a3b285eac97(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09b7d2ce80727605483c1cca4ed70ac9461a14d815999af721ff88f333a832ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aef09b3a5d4bfa3988541299905c0c1343ea985547573352e5a08b0a13c9243(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38038309c072b4b939104fe0c0f44c2fecc6424084abe3716435939cb1b8c00(
    *,
    cluster_arn: builtins.str,
    policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da9c2c389b7fb44efe639e45c2911a96139b86d7a936606322d8605aedb52b8b(
    *,
    broker_node_group_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    cluster_name: builtins.str,
    kafka_version: builtins.str,
    number_of_broker_nodes: jsii.Number,
    client_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    configuration_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    current_version: typing.Optional[builtins.str] = None,
    encryption_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EncryptionInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enhanced_monitoring: typing.Optional[builtins.str] = None,
    logging_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.LoggingInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_monitoring: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.OpenMonitoringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    storage_mode: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4496d16ab1313e2d6e75f55fc7cdb170962f756c6dc1149245dde1aba3113278(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    server_properties: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kafka_versions_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6ce2f411d76bf4b2b3474cef8479b35e9ee5b510006374b01da6c190c75122(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16507eb4f28818c143dcf5097c6c3698548e9010896ca453caaba8d8485407ea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__695b362a9c27a703acdb4ba2dc747ecd9bf0d1b9ee70bd3ddb5779e480e245b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08908c3ec78b02789cf18a674a51767e0dc8877a5b7ac431220532a095ede42e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3501ea47e4e919fbc2daf2fd53e8984fb942ca686b649caea79b13ce7ab95a5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663ee4ade66592e09fdfc891c94c07473d9e23f4b22eb0b252881053695ff63b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b67dfeeec9a4e27fb21b4b14fa3d51255f49590431c2ab861b81fad91473dd5(
    *,
    name: builtins.str,
    server_properties: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kafka_versions_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef99cf7cce653b94ea5543af8d6966cab3ba1c8ff81b50f8736048fff8227ff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    client_authentication: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCluster.ClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]],
    cluster_name: builtins.str,
    vpc_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCluster.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6fcda27bf38beaaece2345e24c9ba42a7a611c55e20c87352dcd2f48c3d3b8c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da58f0cde72fe87dba0e293a65768a7fe5d722e0a1db075b46ff438eff4833d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa89ccfc74c544ca6be404bf89aba0bb0165e1448da8fe2625fe0b16b1233007(
    value: typing.Union[_IResolvable_da3f097b, CfnServerlessCluster.ClientAuthenticationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72f4a1e482f09869114e6642c0c6d4876a0d1f1f71f63585d48a4947074646e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1ce933052056e6636b2d8196e831285d5d488108aa04cd5e5edf99126c9ae4(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnServerlessCluster.VpcConfigProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3b6a10ef556854108c6599fa2fb551287d8a71429ee2a81ceed14943ec4254(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67169aa496dc60cc3cf56e6d1e02f1b57752bd808270ae972957475903226523(
    *,
    sasl: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCluster.SaslProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab5f4c28a418e764a406acaca2f69f2e571164e27a81e4f6f0465c591d1c296e(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1db2d2fc97ad455dce26d20c405cce704978d11074860fa04724f7c3bedba46(
    *,
    iam: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCluster.IamProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04f40675549e758de2257c70e72d28f4b93b50c2c684c533c793f5712b0c42b(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c714eb0299c64ab481c3d39d1e14117755189081833a87372e9f1a245f1ecadc(
    *,
    client_authentication: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCluster.ClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]],
    cluster_name: builtins.str,
    vpc_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCluster.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910be42f1d726644d84801975cd038e26103e9dbcfb02007fe4ebdbeb62c3af8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authentication: builtins.str,
    client_subnets: typing.Sequence[builtins.str],
    security_groups: typing.Sequence[builtins.str],
    target_cluster_arn: builtins.str,
    vpc_id: builtins.str,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f62710c804cf37e90d67ca3091c8bf2c71fdbad4e6eb3fc7637201e5e0c4da4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69e634ecb8c0c7b4c669a0bfa1d695be753962b5974c42bd0023a5d04676b6b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4bd4b61163da39025a8cd09f1db5ecb199b74eb65e9556bf978064fa079e367(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a077d01ed7d7a5f35c6b0cc72e4a77856d510210db08615ab88c969362c05d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2ef79840a03fa0d4be5b71a3f639c366a7f8df914fc8ec7f54b778fc71ed809(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c908df90f79d47c80725c4c1a1ab47b0a3101ba904f6bbb93e09324deb30d3ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7312d322f4e2b55e3a62ef768de9469e6ea2f6745665206380cde67b5c1212a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41badc74ff47dd490e87b936855f3c939b6636c7093dafa31681ef018b5a53f5(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9e41b66e732883ec8194c58e0cffc38f5c68ed0844d8a4d98e59893d73fcc20(
    *,
    authentication: builtins.str,
    client_subnets: typing.Sequence[builtins.str],
    security_groups: typing.Sequence[builtins.str],
    target_cluster_arn: builtins.str,
    vpc_id: builtins.str,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
