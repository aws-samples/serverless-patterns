'''
# AWS::KafkaConnect Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_kafkaconnect as kafkaconnect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for KafkaConnect construct libraries](https://constructs.dev/search?q=kafkaconnect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::KafkaConnect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KafkaConnect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::KafkaConnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KafkaConnect.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

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
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnConnector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector",
):
    '''Creates a connector using the specified properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html
    :cloudformationResource: AWS::KafkaConnect::Connector
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kafkaconnect as kafkaconnect
        
        cfn_connector = kafkaconnect.CfnConnector(self, "MyCfnConnector",
            capacity=kafkaconnect.CfnConnector.CapacityProperty(
                auto_scaling=kafkaconnect.CfnConnector.AutoScalingProperty(
                    max_worker_count=123,
                    mcu_count=123,
                    min_worker_count=123,
                    scale_in_policy=kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                        cpu_utilization_percentage=123
                    ),
                    scale_out_policy=kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                        cpu_utilization_percentage=123
                    )
                ),
                provisioned_capacity=kafkaconnect.CfnConnector.ProvisionedCapacityProperty(
                    worker_count=123,
        
                    # the properties below are optional
                    mcu_count=123
                )
            ),
            connector_configuration={
                "connector_configuration_key": "connectorConfiguration"
            },
            connector_name="connectorName",
            kafka_cluster=kafkaconnect.CfnConnector.KafkaClusterProperty(
                apache_kafka_cluster=kafkaconnect.CfnConnector.ApacheKafkaClusterProperty(
                    bootstrap_servers="bootstrapServers",
                    vpc=kafkaconnect.CfnConnector.VpcProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            ),
            kafka_cluster_client_authentication=kafkaconnect.CfnConnector.KafkaClusterClientAuthenticationProperty(
                authentication_type="authenticationType"
            ),
            kafka_cluster_encryption_in_transit=kafkaconnect.CfnConnector.KafkaClusterEncryptionInTransitProperty(
                encryption_type="encryptionType"
            ),
            kafka_connect_version="kafkaConnectVersion",
            plugins=[kafkaconnect.CfnConnector.PluginProperty(
                custom_plugin=kafkaconnect.CfnConnector.CustomPluginProperty(
                    custom_plugin_arn="customPluginArn",
                    revision=123
                )
            )],
            service_execution_role_arn="serviceExecutionRoleArn",
        
            # the properties below are optional
            connector_description="connectorDescription",
            log_delivery=kafkaconnect.CfnConnector.LogDeliveryProperty(
                worker_log_delivery=kafkaconnect.CfnConnector.WorkerLogDeliveryProperty(
                    cloud_watch_logs=kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                        enabled=False,
        
                        # the properties below are optional
                        log_group="logGroup"
                    ),
                    firehose=kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                        enabled=False,
        
                        # the properties below are optional
                        delivery_stream="deliveryStream"
                    ),
                    s3=kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                        enabled=False,
        
                        # the properties below are optional
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            worker_configuration=kafkaconnect.CfnConnector.WorkerConfigurationProperty(
                revision=123,
                worker_configuration_arn="workerConfigurationArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        capacity: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.CapacityProperty", typing.Dict[builtins.str, typing.Any]]],
        connector_configuration: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
        connector_name: builtins.str,
        kafka_cluster: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.KafkaClusterProperty", typing.Dict[builtins.str, typing.Any]]],
        kafka_cluster_client_authentication: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.KafkaClusterClientAuthenticationProperty", typing.Dict[builtins.str, typing.Any]]],
        kafka_cluster_encryption_in_transit: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.KafkaClusterEncryptionInTransitProperty", typing.Dict[builtins.str, typing.Any]]],
        kafka_connect_version: builtins.str,
        plugins: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.PluginProperty", typing.Dict[builtins.str, typing.Any]]]]],
        service_execution_role_arn: builtins.str,
        connector_description: typing.Optional[builtins.str] = None,
        log_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.LogDeliveryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        worker_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.WorkerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param capacity: The connector's compute capacity settings.
        :param connector_configuration: The configuration of the connector.
        :param connector_name: The name of the connector.
        :param kafka_cluster: The details of the Apache Kafka cluster to which the connector is connected.
        :param kafka_cluster_client_authentication: The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used.
        :param kafka_cluster_encryption_in_transit: Details of encryption in transit to the Apache Kafka cluster.
        :param kafka_connect_version: The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.
        :param plugins: Specifies which plugin to use for the connector. You must specify a single-element list. Amazon MSK Connect does not currently support specifying multiple plugins.
        :param service_execution_role_arn: The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.
        :param connector_description: The description of the connector.
        :param log_delivery: The settings for delivering connector logs to Amazon CloudWatch Logs.
        :param tags: A collection of tags associated with a resource.
        :param worker_configuration: The worker configurations that are in use with the connector.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300d015169800cb7d305cead5c1382d5e67bfb30617c5f51d4668a050b2ea78d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorProps(
            capacity=capacity,
            connector_configuration=connector_configuration,
            connector_name=connector_name,
            kafka_cluster=kafka_cluster,
            kafka_cluster_client_authentication=kafka_cluster_client_authentication,
            kafka_cluster_encryption_in_transit=kafka_cluster_encryption_in_transit,
            kafka_connect_version=kafka_connect_version,
            plugins=plugins,
            service_execution_role_arn=service_execution_role_arn,
            connector_description=connector_description,
            log_delivery=log_delivery,
            tags=tags,
            worker_configuration=worker_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb0c1ffc0dc04852e83fc99bfa9b4c62b202fe4532ee5ffc6e7aa8228f636a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb09bf3c15238ce83b49323b5b92307ae56d22b52e1f4faa4a9efecdf68eab79)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectorArn")
    def attr_connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the newly created connector.

        :cloudformationAttribute: ConnectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectorArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.CapacityProperty"]:
        '''The connector's compute capacity settings.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.CapacityProperty"], jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConnector.CapacityProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93190e39585ede0b426e62964acf4d1946b2270b8cdf90fd760fca16bb13e558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="connectorConfiguration")
    def connector_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
        '''The configuration of the connector.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "connectorConfiguration"))

    @connector_configuration.setter
    def connector_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__405d7e0ae6f7748331d41486bdc7f8856109d58d35c557e79a28b1b86a730e8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="connectorName")
    def connector_name(self) -> builtins.str:
        '''The name of the connector.'''
        return typing.cast(builtins.str, jsii.get(self, "connectorName"))

    @connector_name.setter
    def connector_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5542c73b8c63853663f0c9121c83145b07f4ffbb01dcb93d19e627c8684748f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorName", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaCluster")
    def kafka_cluster(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterProperty"]:
        '''The details of the Apache Kafka cluster to which the connector is connected.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterProperty"], jsii.get(self, "kafkaCluster"))

    @kafka_cluster.setter
    def kafka_cluster(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb859f7d210b463ce7d87e19c928b68134af5a207e21f3d0b913b811695dfad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaCluster", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterClientAuthentication")
    def kafka_cluster_client_authentication(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterClientAuthenticationProperty"]:
        '''The type of client authentication used to connect to the Apache Kafka cluster.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterClientAuthenticationProperty"], jsii.get(self, "kafkaClusterClientAuthentication"))

    @kafka_cluster_client_authentication.setter
    def kafka_cluster_client_authentication(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterClientAuthenticationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7859bcdf95e20025063609459542a94ce1364b2b031ffa476d5bbd530daa22c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaClusterClientAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterEncryptionInTransit")
    def kafka_cluster_encryption_in_transit(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterEncryptionInTransitProperty"]:
        '''Details of encryption in transit to the Apache Kafka cluster.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterEncryptionInTransitProperty"], jsii.get(self, "kafkaClusterEncryptionInTransit"))

    @kafka_cluster_encryption_in_transit.setter
    def kafka_cluster_encryption_in_transit(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConnector.KafkaClusterEncryptionInTransitProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__431b322bcb07c1c51a8b9a735113100e17fffb620cca37b220e3b3aec73425d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaClusterEncryptionInTransit", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaConnectVersion")
    def kafka_connect_version(self) -> builtins.str:
        '''The version of Kafka Connect.'''
        return typing.cast(builtins.str, jsii.get(self, "kafkaConnectVersion"))

    @kafka_connect_version.setter
    def kafka_connect_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a647a1aefe3d2975c3f4cbdccb1be43429421c71bd6f2c868cdb7b3aa7dc46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaConnectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="plugins")
    def plugins(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnector.PluginProperty"]]]:
        '''Specifies which plugin to use for the connector.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnector.PluginProperty"]]], jsii.get(self, "plugins"))

    @plugins.setter
    def plugins(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnector.PluginProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccf2fe35d5eab3697adb8d50736b2ecb8b794ef8d48f98745b61d6534ad954b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plugins", value)

    @builtins.property
    @jsii.member(jsii_name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceExecutionRoleArn"))

    @service_execution_role_arn.setter
    def service_execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__440f19fcd0ca16de4301284405228f6ff797ea28c72dd5e6fd26e3f04b170b1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceExecutionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="connectorDescription")
    def connector_description(self) -> typing.Optional[builtins.str]:
        '''The description of the connector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorDescription"))

    @connector_description.setter
    def connector_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__729e3b6e3d1046550d05c40ab52749c149a4f3f01ce2c03e0daa86cc3ac03d1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorDescription", value)

    @builtins.property
    @jsii.member(jsii_name="logDelivery")
    def log_delivery(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.LogDeliveryProperty"]]:
        '''The settings for delivering connector logs to Amazon CloudWatch Logs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.LogDeliveryProperty"]], jsii.get(self, "logDelivery"))

    @log_delivery.setter
    def log_delivery(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.LogDeliveryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a29da785c6c8f30f5fc4ffcb9320d7a0377e8c1032eb5ff26ba046ae554772)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6afece2b4589a6c48de5a35d55d9159549277f37f560c619fd1daf8392fd3534)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="workerConfiguration")
    def worker_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.WorkerConfigurationProperty"]]:
        '''The worker configurations that are in use with the connector.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.WorkerConfigurationProperty"]], jsii.get(self, "workerConfiguration"))

    @worker_configuration.setter
    def worker_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.WorkerConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17aecc33a40fa4008d52fdd6c617a4bffcf013ba695a96ef9a4694b70b03b576)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.ApacheKafkaClusterProperty",
        jsii_struct_bases=[],
        name_mapping={"bootstrap_servers": "bootstrapServers", "vpc": "vpc"},
    )
    class ApacheKafkaClusterProperty:
        def __init__(
            self,
            *,
            bootstrap_servers: builtins.str,
            vpc: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.VpcProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The details of the Apache Kafka cluster to which the connector is connected.

            :param bootstrap_servers: The bootstrap servers of the cluster.
            :param vpc: Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                apache_kafka_cluster_property = kafkaconnect.CfnConnector.ApacheKafkaClusterProperty(
                    bootstrap_servers="bootstrapServers",
                    vpc=kafkaconnect.CfnConnector.VpcProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__444403cd6207a1a5de68bc9f8e594e52824efdb9ff844ec369a71f064a2d1dcc)
                check_type(argname="argument bootstrap_servers", value=bootstrap_servers, expected_type=type_hints["bootstrap_servers"])
                check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bootstrap_servers": bootstrap_servers,
                "vpc": vpc,
            }

        @builtins.property
        def bootstrap_servers(self) -> builtins.str:
            '''The bootstrap servers of the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-bootstrapservers
            '''
            result = self._values.get("bootstrap_servers")
            assert result is not None, "Required property 'bootstrap_servers' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.VpcProperty"]:
            '''Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-vpc
            '''
            result = self._values.get("vpc")
            assert result is not None, "Required property 'vpc' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.VpcProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApacheKafkaClusterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.AutoScalingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_worker_count": "maxWorkerCount",
            "mcu_count": "mcuCount",
            "min_worker_count": "minWorkerCount",
            "scale_in_policy": "scaleInPolicy",
            "scale_out_policy": "scaleOutPolicy",
        },
    )
    class AutoScalingProperty:
        def __init__(
            self,
            *,
            max_worker_count: jsii.Number,
            mcu_count: jsii.Number,
            min_worker_count: jsii.Number,
            scale_in_policy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.ScaleInPolicyProperty", typing.Dict[builtins.str, typing.Any]]],
            scale_out_policy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.ScaleOutPolicyProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies how the connector scales.

            :param max_worker_count: The maximum number of workers allocated to the connector.
            :param mcu_count: The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.
            :param min_worker_count: The minimum number of workers allocated to the connector.
            :param scale_in_policy: The sacle-in policy for the connector.
            :param scale_out_policy: The sacle-out policy for the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                auto_scaling_property = kafkaconnect.CfnConnector.AutoScalingProperty(
                    max_worker_count=123,
                    mcu_count=123,
                    min_worker_count=123,
                    scale_in_policy=kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                        cpu_utilization_percentage=123
                    ),
                    scale_out_policy=kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                        cpu_utilization_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a7fa0788a72b5a8759557a835e00eec9afbe34fb926c3c0b410cccf6e8c51c7b)
                check_type(argname="argument max_worker_count", value=max_worker_count, expected_type=type_hints["max_worker_count"])
                check_type(argname="argument mcu_count", value=mcu_count, expected_type=type_hints["mcu_count"])
                check_type(argname="argument min_worker_count", value=min_worker_count, expected_type=type_hints["min_worker_count"])
                check_type(argname="argument scale_in_policy", value=scale_in_policy, expected_type=type_hints["scale_in_policy"])
                check_type(argname="argument scale_out_policy", value=scale_out_policy, expected_type=type_hints["scale_out_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_worker_count": max_worker_count,
                "mcu_count": mcu_count,
                "min_worker_count": min_worker_count,
                "scale_in_policy": scale_in_policy,
                "scale_out_policy": scale_out_policy,
            }

        @builtins.property
        def max_worker_count(self) -> jsii.Number:
            '''The maximum number of workers allocated to the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-maxworkercount
            '''
            result = self._values.get("max_worker_count")
            assert result is not None, "Required property 'max_worker_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def mcu_count(self) -> jsii.Number:
            '''The number of microcontroller units (MCUs) allocated to each connector worker.

            The valid values are 1,2,4,8.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-mcucount
            '''
            result = self._values.get("mcu_count")
            assert result is not None, "Required property 'mcu_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_worker_count(self) -> jsii.Number:
            '''The minimum number of workers allocated to the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-minworkercount
            '''
            result = self._values.get("min_worker_count")
            assert result is not None, "Required property 'min_worker_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def scale_in_policy(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.ScaleInPolicyProperty"]:
            '''The sacle-in policy for the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleinpolicy
            '''
            result = self._values.get("scale_in_policy")
            assert result is not None, "Required property 'scale_in_policy' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.ScaleInPolicyProperty"], result)

        @builtins.property
        def scale_out_policy(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.ScaleOutPolicyProperty"]:
            '''The sacle-out policy for the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleoutpolicy
            '''
            result = self._values.get("scale_out_policy")
            assert result is not None, "Required property 'scale_out_policy' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.ScaleOutPolicyProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.CapacityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_scaling": "autoScaling",
            "provisioned_capacity": "provisionedCapacity",
        },
    )
    class CapacityProperty:
        def __init__(
            self,
            *,
            auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.AutoScalingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            provisioned_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.ProvisionedCapacityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information about the capacity of the connector, whether it is auto scaled or provisioned.

            :param auto_scaling: Information about the auto scaling parameters for the connector.
            :param provisioned_capacity: Details about a fixed capacity allocated to a connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                capacity_property = kafkaconnect.CfnConnector.CapacityProperty(
                    auto_scaling=kafkaconnect.CfnConnector.AutoScalingProperty(
                        max_worker_count=123,
                        mcu_count=123,
                        min_worker_count=123,
                        scale_in_policy=kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                            cpu_utilization_percentage=123
                        ),
                        scale_out_policy=kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                            cpu_utilization_percentage=123
                        )
                    ),
                    provisioned_capacity=kafkaconnect.CfnConnector.ProvisionedCapacityProperty(
                        worker_count=123,
                
                        # the properties below are optional
                        mcu_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b215f78afaf806b39553a8a9676f96dddcb2b0c3c6a8d0b8fde6902bf4f381e)
                check_type(argname="argument auto_scaling", value=auto_scaling, expected_type=type_hints["auto_scaling"])
                check_type(argname="argument provisioned_capacity", value=provisioned_capacity, expected_type=type_hints["provisioned_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_scaling is not None:
                self._values["auto_scaling"] = auto_scaling
            if provisioned_capacity is not None:
                self._values["provisioned_capacity"] = provisioned_capacity

        @builtins.property
        def auto_scaling(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.AutoScalingProperty"]]:
            '''Information about the auto scaling parameters for the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-autoscaling
            '''
            result = self._values.get("auto_scaling")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.AutoScalingProperty"]], result)

        @builtins.property
        def provisioned_capacity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.ProvisionedCapacityProperty"]]:
            '''Details about a fixed capacity allocated to a connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-provisionedcapacity
            '''
            result = self._values.get("provisioned_capacity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.ProvisionedCapacityProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "log_group": "logGroup"},
    )
    class CloudWatchLogsLogDeliveryProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            log_group: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for delivering connector logs to Amazon CloudWatch Logs.

            :param enabled: Whether log delivery to Amazon CloudWatch Logs is enabled.
            :param log_group: The name of the CloudWatch log group that is the destination for log delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                cloud_watch_logs_log_delivery_property = kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                    enabled=False,
                
                    # the properties below are optional
                    log_group="logGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce12248bee2c36568fe0e7c8306e19879a8018f4d2f68bc94d16564982c8c14f)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if log_group is not None:
                self._values["log_group"] = log_group

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Whether log delivery to Amazon CloudWatch Logs is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def log_group(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch log group that is the destination for log delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-loggroup
            '''
            result = self._values.get("log_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsLogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.CustomPluginProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_plugin_arn": "customPluginArn", "revision": "revision"},
    )
    class CustomPluginProperty:
        def __init__(
            self,
            *,
            custom_plugin_arn: builtins.str,
            revision: jsii.Number,
        ) -> None:
            '''A plugin is an AWS resource that contains the code that defines a connector's logic.

            :param custom_plugin_arn: The Amazon Resource Name (ARN) of the custom plugin.
            :param revision: The revision of the custom plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                custom_plugin_property = kafkaconnect.CfnConnector.CustomPluginProperty(
                    custom_plugin_arn="customPluginArn",
                    revision=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__939037365c43c9a72b3c37dadef4cee49c45d340b13988d36aec42da17639cb6)
                check_type(argname="argument custom_plugin_arn", value=custom_plugin_arn, expected_type=type_hints["custom_plugin_arn"])
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_plugin_arn": custom_plugin_arn,
                "revision": revision,
            }

        @builtins.property
        def custom_plugin_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the custom plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-custompluginarn
            '''
            result = self._values.get("custom_plugin_arn")
            assert result is not None, "Required property 'custom_plugin_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def revision(self) -> jsii.Number:
            '''The revision of the custom plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomPluginProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "delivery_stream": "deliveryStream"},
    )
    class FirehoseLogDeliveryProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            delivery_stream: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for delivering logs to Amazon Kinesis Data Firehose.

            :param enabled: Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.
            :param delivery_stream: The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                firehose_log_delivery_property = kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                    enabled=False,
                
                    # the properties below are optional
                    delivery_stream="deliveryStream"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5d7349fb5eb5a9a9ec0860e8dad23b287cb3cd62e184b233fee93c0a26a0d51)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if delivery_stream is not None:
                self._values["delivery_stream"] = delivery_stream

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def delivery_stream(self) -> typing.Optional[builtins.str]:
            '''The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-deliverystream
            '''
            result = self._values.get("delivery_stream")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseLogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.KafkaClusterClientAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"authentication_type": "authenticationType"},
    )
    class KafkaClusterClientAuthenticationProperty:
        def __init__(self, *, authentication_type: builtins.str) -> None:
            '''The client authentication information used in order to authenticate with the Apache Kafka cluster.

            :param authentication_type: The type of client authentication used to connect to the Apache Kafka cluster. Value NONE means that no client authentication is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                kafka_cluster_client_authentication_property = kafkaconnect.CfnConnector.KafkaClusterClientAuthenticationProperty(
                    authentication_type="authenticationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7108764262b68e3cecbc01f6bb39c0838e2f09c63cf4785609dc2eb2db70f1b2)
                check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authentication_type": authentication_type,
            }

        @builtins.property
        def authentication_type(self) -> builtins.str:
            '''The type of client authentication used to connect to the Apache Kafka cluster.

            Value NONE means that no client authentication is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication-authenticationtype
            '''
            result = self._values.get("authentication_type")
            assert result is not None, "Required property 'authentication_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaClusterClientAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.KafkaClusterEncryptionInTransitProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_type": "encryptionType"},
    )
    class KafkaClusterEncryptionInTransitProperty:
        def __init__(self, *, encryption_type: builtins.str) -> None:
            '''Details of encryption in transit to the Apache Kafka cluster.

            :param encryption_type: The type of encryption in transit to the Apache Kafka cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                kafka_cluster_encryption_in_transit_property = kafkaconnect.CfnConnector.KafkaClusterEncryptionInTransitProperty(
                    encryption_type="encryptionType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0cecc14be0c2fb246e15a4608e4bdd7b9eac2e2126f98c4fff5625c81b616bf9)
                check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_type": encryption_type,
            }

        @builtins.property
        def encryption_type(self) -> builtins.str:
            '''The type of encryption in transit to the Apache Kafka cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit-encryptiontype
            '''
            result = self._values.get("encryption_type")
            assert result is not None, "Required property 'encryption_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaClusterEncryptionInTransitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.KafkaClusterProperty",
        jsii_struct_bases=[],
        name_mapping={"apache_kafka_cluster": "apacheKafkaCluster"},
    )
    class KafkaClusterProperty:
        def __init__(
            self,
            *,
            apache_kafka_cluster: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.ApacheKafkaClusterProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The details of the Apache Kafka cluster to which the connector is connected.

            :param apache_kafka_cluster: The Apache Kafka cluster to which the connector is connected.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                kafka_cluster_property = kafkaconnect.CfnConnector.KafkaClusterProperty(
                    apache_kafka_cluster=kafkaconnect.CfnConnector.ApacheKafkaClusterProperty(
                        bootstrap_servers="bootstrapServers",
                        vpc=kafkaconnect.CfnConnector.VpcProperty(
                            security_groups=["securityGroups"],
                            subnets=["subnets"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e45630a977bbe5bbdad20f00c55a2b6d7b863f0ebdd96b83af5d59aeeac6fda2)
                check_type(argname="argument apache_kafka_cluster", value=apache_kafka_cluster, expected_type=type_hints["apache_kafka_cluster"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "apache_kafka_cluster": apache_kafka_cluster,
            }

        @builtins.property
        def apache_kafka_cluster(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.ApacheKafkaClusterProperty"]:
            '''The Apache Kafka cluster to which the connector is connected.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html#cfn-kafkaconnect-connector-kafkacluster-apachekafkacluster
            '''
            result = self._values.get("apache_kafka_cluster")
            assert result is not None, "Required property 'apache_kafka_cluster' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.ApacheKafkaClusterProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaClusterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.LogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"worker_log_delivery": "workerLogDelivery"},
    )
    class LogDeliveryProperty:
        def __init__(
            self,
            *,
            worker_log_delivery: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.WorkerLogDeliveryProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Details about log delivery.

            :param worker_log_delivery: The workers can send worker logs to different destination types. This configuration specifies the details of these destinations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                log_delivery_property = kafkaconnect.CfnConnector.LogDeliveryProperty(
                    worker_log_delivery=kafkaconnect.CfnConnector.WorkerLogDeliveryProperty(
                        cloud_watch_logs=kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                            enabled=False,
                
                            # the properties below are optional
                            log_group="logGroup"
                        ),
                        firehose=kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                            enabled=False,
                
                            # the properties below are optional
                            delivery_stream="deliveryStream"
                        ),
                        s3=kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                            enabled=False,
                
                            # the properties below are optional
                            bucket="bucket",
                            prefix="prefix"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24fd0806b35f57962768914d0194bea1b40b93b71c0c3dd6d6a8aad5d85e5b3d)
                check_type(argname="argument worker_log_delivery", value=worker_log_delivery, expected_type=type_hints["worker_log_delivery"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "worker_log_delivery": worker_log_delivery,
            }

        @builtins.property
        def worker_log_delivery(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.WorkerLogDeliveryProperty"]:
            '''The workers can send worker logs to different destination types.

            This configuration specifies the details of these destinations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html#cfn-kafkaconnect-connector-logdelivery-workerlogdelivery
            '''
            result = self._values.get("worker_log_delivery")
            assert result is not None, "Required property 'worker_log_delivery' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.WorkerLogDeliveryProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.PluginProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_plugin": "customPlugin"},
    )
    class PluginProperty:
        def __init__(
            self,
            *,
            custom_plugin: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.CustomPluginProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A plugin is an AWS resource that contains the code that defines your connector logic.

            :param custom_plugin: Details about a custom plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                plugin_property = kafkaconnect.CfnConnector.PluginProperty(
                    custom_plugin=kafkaconnect.CfnConnector.CustomPluginProperty(
                        custom_plugin_arn="customPluginArn",
                        revision=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35948a4a66b01f82e5bedaf253946f464f4c86608300c9773f71dce120de9f0d)
                check_type(argname="argument custom_plugin", value=custom_plugin, expected_type=type_hints["custom_plugin"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_plugin": custom_plugin,
            }

        @builtins.property
        def custom_plugin(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.CustomPluginProperty"]:
            '''Details about a custom plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html#cfn-kafkaconnect-connector-plugin-customplugin
            '''
            result = self._values.get("custom_plugin")
            assert result is not None, "Required property 'custom_plugin' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.CustomPluginProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PluginProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.ProvisionedCapacityProperty",
        jsii_struct_bases=[],
        name_mapping={"worker_count": "workerCount", "mcu_count": "mcuCount"},
    )
    class ProvisionedCapacityProperty:
        def __init__(
            self,
            *,
            worker_count: jsii.Number,
            mcu_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Details about a connector's provisioned capacity.

            :param worker_count: The number of workers that are allocated to the connector.
            :param mcu_count: The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                provisioned_capacity_property = kafkaconnect.CfnConnector.ProvisionedCapacityProperty(
                    worker_count=123,
                
                    # the properties below are optional
                    mcu_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf9af2fbdc2eecf97de30bc43ea6a6be8266e58490ff4a55318a2c6b110af1b8)
                check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
                check_type(argname="argument mcu_count", value=mcu_count, expected_type=type_hints["mcu_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "worker_count": worker_count,
            }
            if mcu_count is not None:
                self._values["mcu_count"] = mcu_count

        @builtins.property
        def worker_count(self) -> jsii.Number:
            '''The number of workers that are allocated to the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-workercount
            '''
            result = self._values.get("worker_count")
            assert result is not None, "Required property 'worker_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def mcu_count(self) -> typing.Optional[jsii.Number]:
            '''The number of microcontroller units (MCUs) allocated to each connector worker.

            The valid values are 1,2,4,8.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-mcucount
            '''
            result = self._values.get("mcu_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedCapacityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.S3LogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "bucket": "bucket", "prefix": "prefix"},
    )
    class S3LogDeliveryProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            bucket: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details about delivering logs to Amazon S3.

            :param enabled: Specifies whether connector logs get sent to the specified Amazon S3 destination.
            :param bucket: The name of the S3 bucket that is the destination for log delivery.
            :param prefix: The S3 prefix that is the destination for log delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                s3_log_delivery_property = kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                    enabled=False,
                
                    # the properties below are optional
                    bucket="bucket",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__991b0af73117e26499c590fefbda601c1fa27a956d8ed920c29dddf6e3942d9b)
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
            '''Specifies whether connector logs get sent to the specified Amazon S3 destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def bucket(self) -> typing.Optional[builtins.str]:
            '''The name of the S3 bucket that is the destination for log delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-bucket
            '''
            result = self._values.get("bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 prefix that is the destination for log delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.ScaleInPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu_utilization_percentage": "cpuUtilizationPercentage"},
    )
    class ScaleInPolicyProperty:
        def __init__(self, *, cpu_utilization_percentage: jsii.Number) -> None:
            '''The scale-in policy for the connector.

            :param cpu_utilization_percentage: Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                scale_in_policy_property = kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                    cpu_utilization_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__12883647368b045af218938a85170c504e2ac16d35c5b7f6abdc33dcfd0b38aa)
                check_type(argname="argument cpu_utilization_percentage", value=cpu_utilization_percentage, expected_type=type_hints["cpu_utilization_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cpu_utilization_percentage": cpu_utilization_percentage,
            }

        @builtins.property
        def cpu_utilization_percentage(self) -> jsii.Number:
            '''Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html#cfn-kafkaconnect-connector-scaleinpolicy-cpuutilizationpercentage
            '''
            result = self._values.get("cpu_utilization_percentage")
            assert result is not None, "Required property 'cpu_utilization_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScaleInPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.ScaleOutPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu_utilization_percentage": "cpuUtilizationPercentage"},
    )
    class ScaleOutPolicyProperty:
        def __init__(self, *, cpu_utilization_percentage: jsii.Number) -> None:
            '''The scale-out policy for the connector.

            :param cpu_utilization_percentage: The CPU utilization percentage threshold at which you want connector scale out to be triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                scale_out_policy_property = kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                    cpu_utilization_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab985ea028517aece904c3e9a620409a4917dc5407933921e63629b65eccaf8f)
                check_type(argname="argument cpu_utilization_percentage", value=cpu_utilization_percentage, expected_type=type_hints["cpu_utilization_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cpu_utilization_percentage": cpu_utilization_percentage,
            }

        @builtins.property
        def cpu_utilization_percentage(self) -> jsii.Number:
            '''The CPU utilization percentage threshold at which you want connector scale out to be triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html#cfn-kafkaconnect-connector-scaleoutpolicy-cpuutilizationpercentage
            '''
            result = self._values.get("cpu_utilization_percentage")
            assert result is not None, "Required property 'cpu_utilization_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScaleOutPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.VpcProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
    )
    class VpcProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Information about the VPC in which the connector resides.

            :param security_groups: The security groups for the connector.
            :param subnets: The subnets for the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                vpc_property = kafkaconnect.CfnConnector.VpcProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a2e175ee9bba2b6ccb5fe61627e4539b807b2696754acbc03a8c398ebe32a25)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_groups": security_groups,
                "subnets": subnets,
            }

        @builtins.property
        def security_groups(self) -> typing.List[builtins.str]:
            '''The security groups for the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-securitygroups
            '''
            result = self._values.get("security_groups")
            assert result is not None, "Required property 'security_groups' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''The subnets for the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.WorkerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "revision": "revision",
            "worker_configuration_arn": "workerConfigurationArn",
        },
    )
    class WorkerConfigurationProperty:
        def __init__(
            self,
            *,
            revision: jsii.Number,
            worker_configuration_arn: builtins.str,
        ) -> None:
            '''The configuration of the workers, which are the processes that run the connector logic.

            :param revision: The revision of the worker configuration.
            :param worker_configuration_arn: The Amazon Resource Name (ARN) of the worker configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                worker_configuration_property = kafkaconnect.CfnConnector.WorkerConfigurationProperty(
                    revision=123,
                    worker_configuration_arn="workerConfigurationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__410d90caf1544bb4b43be0646f325702b7ea82434e28ebcb5440055410c0f6bf)
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
                check_type(argname="argument worker_configuration_arn", value=worker_configuration_arn, expected_type=type_hints["worker_configuration_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "revision": revision,
                "worker_configuration_arn": worker_configuration_arn,
            }

        @builtins.property
        def revision(self) -> jsii.Number:
            '''The revision of the worker configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def worker_configuration_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the worker configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-workerconfigurationarn
            '''
            result = self._values.get("worker_configuration_arn")
            assert result is not None, "Required property 'worker_configuration_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.WorkerLogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs": "cloudWatchLogs",
            "firehose": "firehose",
            "s3": "s3",
        },
    )
    class WorkerLogDeliveryProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.CloudWatchLogsLogDeliveryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.FirehoseLogDeliveryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.S3LogDeliveryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Workers can send worker logs to different destination types.

            This configuration specifies the details of these destinations.

            :param cloud_watch_logs: Details about delivering logs to Amazon CloudWatch Logs.
            :param firehose: Details about delivering logs to Amazon Kinesis Data Firehose.
            :param s3: Details about delivering logs to Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                worker_log_delivery_property = kafkaconnect.CfnConnector.WorkerLogDeliveryProperty(
                    cloud_watch_logs=kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                        enabled=False,
                
                        # the properties below are optional
                        log_group="logGroup"
                    ),
                    firehose=kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                        enabled=False,
                
                        # the properties below are optional
                        delivery_stream="deliveryStream"
                    ),
                    s3=kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                        enabled=False,
                
                        # the properties below are optional
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc89e20cb6ae15c383691c63107a6550accceb0bd180b844f01270a6c026e02a)
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
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.CloudWatchLogsLogDeliveryProperty"]]:
            '''Details about delivering logs to Amazon CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.CloudWatchLogsLogDeliveryProperty"]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.FirehoseLogDeliveryProperty"]]:
            '''Details about delivering logs to Amazon Kinesis Data Firehose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.FirehoseLogDeliveryProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.S3LogDeliveryProperty"]]:
            '''Details about delivering logs to Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.S3LogDeliveryProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkerLogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "connector_configuration": "connectorConfiguration",
        "connector_name": "connectorName",
        "kafka_cluster": "kafkaCluster",
        "kafka_cluster_client_authentication": "kafkaClusterClientAuthentication",
        "kafka_cluster_encryption_in_transit": "kafkaClusterEncryptionInTransit",
        "kafka_connect_version": "kafkaConnectVersion",
        "plugins": "plugins",
        "service_execution_role_arn": "serviceExecutionRoleArn",
        "connector_description": "connectorDescription",
        "log_delivery": "logDelivery",
        "tags": "tags",
        "worker_configuration": "workerConfiguration",
    },
)
class CfnConnectorProps:
    def __init__(
        self,
        *,
        capacity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.CapacityProperty, typing.Dict[builtins.str, typing.Any]]],
        connector_configuration: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
        connector_name: builtins.str,
        kafka_cluster: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterProperty, typing.Dict[builtins.str, typing.Any]]],
        kafka_cluster_client_authentication: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]],
        kafka_cluster_encryption_in_transit: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterEncryptionInTransitProperty, typing.Dict[builtins.str, typing.Any]]],
        kafka_connect_version: builtins.str,
        plugins: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.PluginProperty, typing.Dict[builtins.str, typing.Any]]]]],
        service_execution_role_arn: builtins.str,
        connector_description: typing.Optional[builtins.str] = None,
        log_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.LogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        worker_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.WorkerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnector``.

        :param capacity: The connector's compute capacity settings.
        :param connector_configuration: The configuration of the connector.
        :param connector_name: The name of the connector.
        :param kafka_cluster: The details of the Apache Kafka cluster to which the connector is connected.
        :param kafka_cluster_client_authentication: The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used.
        :param kafka_cluster_encryption_in_transit: Details of encryption in transit to the Apache Kafka cluster.
        :param kafka_connect_version: The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.
        :param plugins: Specifies which plugin to use for the connector. You must specify a single-element list. Amazon MSK Connect does not currently support specifying multiple plugins.
        :param service_execution_role_arn: The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.
        :param connector_description: The description of the connector.
        :param log_delivery: The settings for delivering connector logs to Amazon CloudWatch Logs.
        :param tags: A collection of tags associated with a resource.
        :param worker_configuration: The worker configurations that are in use with the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kafkaconnect as kafkaconnect
            
            cfn_connector_props = kafkaconnect.CfnConnectorProps(
                capacity=kafkaconnect.CfnConnector.CapacityProperty(
                    auto_scaling=kafkaconnect.CfnConnector.AutoScalingProperty(
                        max_worker_count=123,
                        mcu_count=123,
                        min_worker_count=123,
                        scale_in_policy=kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                            cpu_utilization_percentage=123
                        ),
                        scale_out_policy=kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                            cpu_utilization_percentage=123
                        )
                    ),
                    provisioned_capacity=kafkaconnect.CfnConnector.ProvisionedCapacityProperty(
                        worker_count=123,
            
                        # the properties below are optional
                        mcu_count=123
                    )
                ),
                connector_configuration={
                    "connector_configuration_key": "connectorConfiguration"
                },
                connector_name="connectorName",
                kafka_cluster=kafkaconnect.CfnConnector.KafkaClusterProperty(
                    apache_kafka_cluster=kafkaconnect.CfnConnector.ApacheKafkaClusterProperty(
                        bootstrap_servers="bootstrapServers",
                        vpc=kafkaconnect.CfnConnector.VpcProperty(
                            security_groups=["securityGroups"],
                            subnets=["subnets"]
                        )
                    )
                ),
                kafka_cluster_client_authentication=kafkaconnect.CfnConnector.KafkaClusterClientAuthenticationProperty(
                    authentication_type="authenticationType"
                ),
                kafka_cluster_encryption_in_transit=kafkaconnect.CfnConnector.KafkaClusterEncryptionInTransitProperty(
                    encryption_type="encryptionType"
                ),
                kafka_connect_version="kafkaConnectVersion",
                plugins=[kafkaconnect.CfnConnector.PluginProperty(
                    custom_plugin=kafkaconnect.CfnConnector.CustomPluginProperty(
                        custom_plugin_arn="customPluginArn",
                        revision=123
                    )
                )],
                service_execution_role_arn="serviceExecutionRoleArn",
            
                # the properties below are optional
                connector_description="connectorDescription",
                log_delivery=kafkaconnect.CfnConnector.LogDeliveryProperty(
                    worker_log_delivery=kafkaconnect.CfnConnector.WorkerLogDeliveryProperty(
                        cloud_watch_logs=kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                            enabled=False,
            
                            # the properties below are optional
                            log_group="logGroup"
                        ),
                        firehose=kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                            enabled=False,
            
                            # the properties below are optional
                            delivery_stream="deliveryStream"
                        ),
                        s3=kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                            enabled=False,
            
                            # the properties below are optional
                            bucket="bucket",
                            prefix="prefix"
                        )
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                worker_configuration=kafkaconnect.CfnConnector.WorkerConfigurationProperty(
                    revision=123,
                    worker_configuration_arn="workerConfigurationArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12463a17cb9c37949b260894212e085ba134c7ff0644cf3913b56f022b888c0b)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument connector_configuration", value=connector_configuration, expected_type=type_hints["connector_configuration"])
            check_type(argname="argument connector_name", value=connector_name, expected_type=type_hints["connector_name"])
            check_type(argname="argument kafka_cluster", value=kafka_cluster, expected_type=type_hints["kafka_cluster"])
            check_type(argname="argument kafka_cluster_client_authentication", value=kafka_cluster_client_authentication, expected_type=type_hints["kafka_cluster_client_authentication"])
            check_type(argname="argument kafka_cluster_encryption_in_transit", value=kafka_cluster_encryption_in_transit, expected_type=type_hints["kafka_cluster_encryption_in_transit"])
            check_type(argname="argument kafka_connect_version", value=kafka_connect_version, expected_type=type_hints["kafka_connect_version"])
            check_type(argname="argument plugins", value=plugins, expected_type=type_hints["plugins"])
            check_type(argname="argument service_execution_role_arn", value=service_execution_role_arn, expected_type=type_hints["service_execution_role_arn"])
            check_type(argname="argument connector_description", value=connector_description, expected_type=type_hints["connector_description"])
            check_type(argname="argument log_delivery", value=log_delivery, expected_type=type_hints["log_delivery"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument worker_configuration", value=worker_configuration, expected_type=type_hints["worker_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity": capacity,
            "connector_configuration": connector_configuration,
            "connector_name": connector_name,
            "kafka_cluster": kafka_cluster,
            "kafka_cluster_client_authentication": kafka_cluster_client_authentication,
            "kafka_cluster_encryption_in_transit": kafka_cluster_encryption_in_transit,
            "kafka_connect_version": kafka_connect_version,
            "plugins": plugins,
            "service_execution_role_arn": service_execution_role_arn,
        }
        if connector_description is not None:
            self._values["connector_description"] = connector_description
        if log_delivery is not None:
            self._values["log_delivery"] = log_delivery
        if tags is not None:
            self._values["tags"] = tags
        if worker_configuration is not None:
            self._values["worker_configuration"] = worker_configuration

    @builtins.property
    def capacity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConnector.CapacityProperty]:
        '''The connector's compute capacity settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-capacity
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConnector.CapacityProperty], result)

    @builtins.property
    def connector_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
        '''The configuration of the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorconfiguration
        '''
        result = self._values.get("connector_configuration")
        assert result is not None, "Required property 'connector_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def connector_name(self) -> builtins.str:
        '''The name of the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorname
        '''
        result = self._values.get("connector_name")
        assert result is not None, "Required property 'connector_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kafka_cluster(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterProperty]:
        '''The details of the Apache Kafka cluster to which the connector is connected.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkacluster
        '''
        result = self._values.get("kafka_cluster")
        assert result is not None, "Required property 'kafka_cluster' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterProperty], result)

    @builtins.property
    def kafka_cluster_client_authentication(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterClientAuthenticationProperty]:
        '''The type of client authentication used to connect to the Apache Kafka cluster.

        The value is NONE when no client authentication is used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication
        '''
        result = self._values.get("kafka_cluster_client_authentication")
        assert result is not None, "Required property 'kafka_cluster_client_authentication' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterClientAuthenticationProperty], result)

    @builtins.property
    def kafka_cluster_encryption_in_transit(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterEncryptionInTransitProperty]:
        '''Details of encryption in transit to the Apache Kafka cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit
        '''
        result = self._values.get("kafka_cluster_encryption_in_transit")
        assert result is not None, "Required property 'kafka_cluster_encryption_in_transit' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterEncryptionInTransitProperty], result)

    @builtins.property
    def kafka_connect_version(self) -> builtins.str:
        '''The version of Kafka Connect.

        It has to be compatible with both the Apache Kafka cluster's version and the plugins.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaconnectversion
        '''
        result = self._values.get("kafka_connect_version")
        assert result is not None, "Required property 'kafka_connect_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugins(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConnector.PluginProperty]]]:
        '''Specifies which plugin to use for the connector.

        You must specify a single-element list. Amazon MSK Connect does not currently support specifying multiple plugins.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-plugins
        '''
        result = self._values.get("plugins")
        assert result is not None, "Required property 'plugins' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConnector.PluginProperty]]], result)

    @builtins.property
    def service_execution_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-serviceexecutionrolearn
        '''
        result = self._values.get("service_execution_role_arn")
        assert result is not None, "Required property 'service_execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_description(self) -> typing.Optional[builtins.str]:
        '''The description of the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectordescription
        '''
        result = self._values.get("connector_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.LogDeliveryProperty]]:
        '''The settings for delivering connector logs to Amazon CloudWatch Logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-logdelivery
        '''
        result = self._values.get("log_delivery")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.LogDeliveryProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def worker_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.WorkerConfigurationProperty]]:
        '''The worker configurations that are in use with the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-workerconfiguration
        '''
        result = self._values.get("worker_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.WorkerConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCustomPlugin(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnCustomPlugin",
):
    '''Creates a custom plugin using the specified properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-customplugin.html
    :cloudformationResource: AWS::KafkaConnect::CustomPlugin
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kafkaconnect as kafkaconnect
        
        cfn_custom_plugin = kafkaconnect.CfnCustomPlugin(self, "MyCfnCustomPlugin",
            content_type="contentType",
            location=kafkaconnect.CfnCustomPlugin.CustomPluginLocationProperty(
                s3_location=kafkaconnect.CfnCustomPlugin.S3LocationProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey",
        
                    # the properties below are optional
                    object_version="objectVersion"
                )
            ),
            name="name",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        content_type: builtins.str,
        location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCustomPlugin.CustomPluginLocationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content_type: The format of the plugin file.
        :param location: Information about the location of the custom plugin.
        :param name: The name of the custom plugin.
        :param description: The description of the custom plugin.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c82cbd22c9261a35dcdabc1becaf63f49b9257f7d5508ee8aa43d6a285cf574)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomPluginProps(
            content_type=content_type,
            location=location,
            name=name,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2de4a61cefe6c2d25a1cb343ddd4a22e10b259b61229c873a373b2fa9d057114)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f576b3a446b38f6f20978c3517504ba7babed66f64bc5fb21b1c950bc4a6872a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCustomPluginArn")
    def attr_custom_plugin_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the custom plugin.

        :cloudformationAttribute: CustomPluginArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCustomPluginArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFileDescription")
    def attr_file_description(self) -> _IResolvable_da3f097b:
        '''Details about the custom plugin file.

        :cloudformationAttribute: FileDescription
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrFileDescription"))

    @builtins.property
    @jsii.member(jsii_name="attrRevision")
    def attr_revision(self) -> jsii.Number:
        '''The revision of the custom plugin.

        :cloudformationAttribute: Revision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRevision"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        '''The format of the plugin file.'''
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba10e1ed6d2bc46a1ed1d1fe0ea02869794128cfcb6ebd5cadbefe02bc0a548f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCustomPlugin.CustomPluginLocationProperty"]:
        '''Information about the location of the custom plugin.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCustomPlugin.CustomPluginLocationProperty"], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCustomPlugin.CustomPluginLocationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dc28b9198145db094f79802e21f70587ba9ea39d8bf86eecd4baa600f164d5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the custom plugin.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22b7cdbcdbf1c6aca15574793b79bc5bcd1b238c5d20012e24075b2de3c3e1f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the custom plugin.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48e19fd5c93da0b6a93cdfdf44392a652cad52a2c961aef8c3e0a76eff5052e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11b359e6a300e42bfcb9aa594841d75ad92accb911de61cc64790b7fc061f9fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnCustomPlugin.CustomPluginFileDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={"file_md5": "fileMd5", "file_size": "fileSize"},
    )
    class CustomPluginFileDescriptionProperty:
        def __init__(
            self,
            *,
            file_md5: typing.Optional[builtins.str] = None,
            file_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Details about a custom plugin file.

            :param file_md5: The hex-encoded MD5 checksum of the custom plugin file. You can use it to validate the file.
            :param file_size: The size in bytes of the custom plugin file. You can use it to validate the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-custompluginfiledescription.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                custom_plugin_file_description_property = kafkaconnect.CfnCustomPlugin.CustomPluginFileDescriptionProperty(
                    file_md5="fileMd5",
                    file_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3f77f7d7b096911e70040b0039d61af28b26c9bc89fb1faf76b0717d7c9e18b)
                check_type(argname="argument file_md5", value=file_md5, expected_type=type_hints["file_md5"])
                check_type(argname="argument file_size", value=file_size, expected_type=type_hints["file_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if file_md5 is not None:
                self._values["file_md5"] = file_md5
            if file_size is not None:
                self._values["file_size"] = file_size

        @builtins.property
        def file_md5(self) -> typing.Optional[builtins.str]:
            '''The hex-encoded MD5 checksum of the custom plugin file.

            You can use it to validate the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-custompluginfiledescription.html#cfn-kafkaconnect-customplugin-custompluginfiledescription-filemd5
            '''
            result = self._values.get("file_md5")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_size(self) -> typing.Optional[jsii.Number]:
            '''The size in bytes of the custom plugin file.

            You can use it to validate the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-custompluginfiledescription.html#cfn-kafkaconnect-customplugin-custompluginfiledescription-filesize
            '''
            result = self._values.get("file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomPluginFileDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnCustomPlugin.CustomPluginLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_location": "s3Location"},
    )
    class CustomPluginLocationProperty:
        def __init__(
            self,
            *,
            s3_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCustomPlugin.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Information about the location of a custom plugin.

            :param s3_location: The S3 bucket Amazon Resource Name (ARN), file key, and object version of the plugin file stored in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-custompluginlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                custom_plugin_location_property = kafkaconnect.CfnCustomPlugin.CustomPluginLocationProperty(
                    s3_location=kafkaconnect.CfnCustomPlugin.S3LocationProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey",
                
                        # the properties below are optional
                        object_version="objectVersion"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63bbd79857b9bcc2770666f84b8116fcd6735c81fd0e1e465634b4002d175383)
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_location": s3_location,
            }

        @builtins.property
        def s3_location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCustomPlugin.S3LocationProperty"]:
            '''The S3 bucket Amazon Resource Name (ARN), file key, and object version of the plugin file stored in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-custompluginlocation.html#cfn-kafkaconnect-customplugin-custompluginlocation-s3location
            '''
            result = self._values.get("s3_location")
            assert result is not None, "Required property 's3_location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCustomPlugin.S3LocationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomPluginLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnCustomPlugin.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "file_key": "fileKey",
            "object_version": "objectVersion",
        },
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            file_key: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location of an object in Amazon S3.

            :param bucket_arn: The Amazon Resource Name (ARN) of an S3 bucket.
            :param file_key: The file key for an object in an S3 bucket.
            :param object_version: The version of an object in an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                s3_location_property = kafkaconnect.CfnCustomPlugin.S3LocationProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey",
                
                    # the properties below are optional
                    object_version="objectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__781a268ba9bfa781e533379ca4a5047660328871695af7ae3feb962865170db2)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
                check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "file_key": file_key,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-s3location.html#cfn-kafkaconnect-customplugin-s3location-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def file_key(self) -> builtins.str:
            '''The file key for an object in an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-s3location.html#cfn-kafkaconnect-customplugin-s3location-filekey
            '''
            result = self._values.get("file_key")
            assert result is not None, "Required property 'file_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''The version of an object in an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-customplugin-s3location.html#cfn-kafkaconnect-customplugin-s3location-objectversion
            '''
            result = self._values.get("object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnCustomPluginProps",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "location": "location",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnCustomPluginProps:
    def __init__(
        self,
        *,
        content_type: builtins.str,
        location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomPlugin.CustomPluginLocationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomPlugin``.

        :param content_type: The format of the plugin file.
        :param location: Information about the location of the custom plugin.
        :param name: The name of the custom plugin.
        :param description: The description of the custom plugin.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-customplugin.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kafkaconnect as kafkaconnect
            
            cfn_custom_plugin_props = kafkaconnect.CfnCustomPluginProps(
                content_type="contentType",
                location=kafkaconnect.CfnCustomPlugin.CustomPluginLocationProperty(
                    s3_location=kafkaconnect.CfnCustomPlugin.S3LocationProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey",
            
                        # the properties below are optional
                        object_version="objectVersion"
                    )
                ),
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff983745d275d6d3a1389c6b1984a735ff1815dde7d1308c56b56268157c0bac)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content_type": content_type,
            "location": location,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content_type(self) -> builtins.str:
        '''The format of the plugin file.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-customplugin.html#cfn-kafkaconnect-customplugin-contenttype
        '''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCustomPlugin.CustomPluginLocationProperty]:
        '''Information about the location of the custom plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-customplugin.html#cfn-kafkaconnect-customplugin-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCustomPlugin.CustomPluginLocationProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the custom plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-customplugin.html#cfn-kafkaconnect-customplugin-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the custom plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-customplugin.html#cfn-kafkaconnect-customplugin-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-customplugin.html#cfn-kafkaconnect-customplugin-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomPluginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnWorkerConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnWorkerConfiguration",
):
    '''Creates a worker configuration using the specified properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-workerconfiguration.html
    :cloudformationResource: AWS::KafkaConnect::WorkerConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kafkaconnect as kafkaconnect
        
        cfn_worker_configuration = kafkaconnect.CfnWorkerConfiguration(self, "MyCfnWorkerConfiguration",
            name="name",
            properties_file_content="propertiesFileContent",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        properties_file_content: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the worker configuration.
        :param properties_file_content: Base64 encoded contents of the connect-distributed.properties file.
        :param description: The description of a worker configuration.
        :param tags: A collection of tags associated with a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b9b69a356034dd45c5e800dbc80d6a39a12c1880a5d436867eade4d8465fab4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkerConfigurationProps(
            name=name,
            properties_file_content=properties_file_content,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e9312db5b66d689fcbfe5175a48113463e0ed07e92a59d8aa13bf6e7cc2e5ba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a145561100ff01cc7ff59a55ef33e73905f7091cbb20b0211c8b6706473d8db)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRevision")
    def attr_revision(self) -> jsii.Number:
        '''The revision of the worker configuration.

        :cloudformationAttribute: Revision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRevision"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkerConfigurationArn")
    def attr_worker_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the worker configuration.

        :cloudformationAttribute: WorkerConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkerConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the worker configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc71d30a2d2b5a6b21933eb20d227cc7424b5194fb7804fa4cb3d77dd657dbb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="propertiesFileContent")
    def properties_file_content(self) -> builtins.str:
        '''Base64 encoded contents of the connect-distributed.properties file.'''
        return typing.cast(builtins.str, jsii.get(self, "propertiesFileContent"))

    @properties_file_content.setter
    def properties_file_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdac93459bf92083dd5049beb4d514f22fddfa0bd9d388dc1ef3385ce63b1af0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertiesFileContent", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a worker configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30511563247fe50c21e1853ef081844489c75d4646bdd82b0b64165734629e02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a36569b41baa16c75dbfb344c8382fd94b5dc82a3a87fd538c07957efff63b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnWorkerConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "properties_file_content": "propertiesFileContent",
        "description": "description",
        "tags": "tags",
    },
)
class CfnWorkerConfigurationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        properties_file_content: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkerConfiguration``.

        :param name: The name of the worker configuration.
        :param properties_file_content: Base64 encoded contents of the connect-distributed.properties file.
        :param description: The description of a worker configuration.
        :param tags: A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-workerconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kafkaconnect as kafkaconnect
            
            cfn_worker_configuration_props = kafkaconnect.CfnWorkerConfigurationProps(
                name="name",
                properties_file_content="propertiesFileContent",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b5e8a900e9ebee6da2f64fb77eb98c44d23ed30e4b800a7e67486fadb71f6ae)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument properties_file_content", value=properties_file_content, expected_type=type_hints["properties_file_content"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "properties_file_content": properties_file_content,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the worker configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-workerconfiguration.html#cfn-kafkaconnect-workerconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def properties_file_content(self) -> builtins.str:
        '''Base64 encoded contents of the connect-distributed.properties file.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-workerconfiguration.html#cfn-kafkaconnect-workerconfiguration-propertiesfilecontent
        '''
        result = self._values.get("properties_file_content")
        assert result is not None, "Required property 'properties_file_content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a worker configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-workerconfiguration.html#cfn-kafkaconnect-workerconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-workerconfiguration.html#cfn-kafkaconnect-workerconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkerConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnector",
    "CfnConnectorProps",
    "CfnCustomPlugin",
    "CfnCustomPluginProps",
    "CfnWorkerConfiguration",
    "CfnWorkerConfigurationProps",
]

publication.publish()

def _typecheckingstub__300d015169800cb7d305cead5c1382d5e67bfb30617c5f51d4668a050b2ea78d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    capacity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.CapacityProperty, typing.Dict[builtins.str, typing.Any]]],
    connector_configuration: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    connector_name: builtins.str,
    kafka_cluster: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterProperty, typing.Dict[builtins.str, typing.Any]]],
    kafka_cluster_client_authentication: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]],
    kafka_cluster_encryption_in_transit: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterEncryptionInTransitProperty, typing.Dict[builtins.str, typing.Any]]],
    kafka_connect_version: builtins.str,
    plugins: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.PluginProperty, typing.Dict[builtins.str, typing.Any]]]]],
    service_execution_role_arn: builtins.str,
    connector_description: typing.Optional[builtins.str] = None,
    log_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.LogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.WorkerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb0c1ffc0dc04852e83fc99bfa9b4c62b202fe4532ee5ffc6e7aa8228f636a2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb09bf3c15238ce83b49323b5b92307ae56d22b52e1f4faa4a9efecdf68eab79(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93190e39585ede0b426e62964acf4d1946b2270b8cdf90fd760fca16bb13e558(
    value: typing.Union[_IResolvable_da3f097b, CfnConnector.CapacityProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405d7e0ae6f7748331d41486bdc7f8856109d58d35c557e79a28b1b86a730e8d(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5542c73b8c63853663f0c9121c83145b07f4ffbb01dcb93d19e627c8684748f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb859f7d210b463ce7d87e19c928b68134af5a207e21f3d0b913b811695dfad(
    value: typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7859bcdf95e20025063609459542a94ce1364b2b031ffa476d5bbd530daa22c(
    value: typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterClientAuthenticationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__431b322bcb07c1c51a8b9a735113100e17fffb620cca37b220e3b3aec73425d2(
    value: typing.Union[_IResolvable_da3f097b, CfnConnector.KafkaClusterEncryptionInTransitProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a647a1aefe3d2975c3f4cbdccb1be43429421c71bd6f2c868cdb7b3aa7dc46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf2fe35d5eab3697adb8d50736b2ecb8b794ef8d48f98745b61d6534ad954b6(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConnector.PluginProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__440f19fcd0ca16de4301284405228f6ff797ea28c72dd5e6fd26e3f04b170b1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__729e3b6e3d1046550d05c40ab52749c149a4f3f01ce2c03e0daa86cc3ac03d1e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a29da785c6c8f30f5fc4ffcb9320d7a0377e8c1032eb5ff26ba046ae554772(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.LogDeliveryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6afece2b4589a6c48de5a35d55d9159549277f37f560c619fd1daf8392fd3534(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17aecc33a40fa4008d52fdd6c617a4bffcf013ba695a96ef9a4694b70b03b576(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.WorkerConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444403cd6207a1a5de68bc9f8e594e52824efdb9ff844ec369a71f064a2d1dcc(
    *,
    bootstrap_servers: builtins.str,
    vpc: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.VpcProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7fa0788a72b5a8759557a835e00eec9afbe34fb926c3c0b410cccf6e8c51c7b(
    *,
    max_worker_count: jsii.Number,
    mcu_count: jsii.Number,
    min_worker_count: jsii.Number,
    scale_in_policy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.ScaleInPolicyProperty, typing.Dict[builtins.str, typing.Any]]],
    scale_out_policy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.ScaleOutPolicyProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b215f78afaf806b39553a8a9676f96dddcb2b0c3c6a8d0b8fde6902bf4f381e(
    *,
    auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.AutoScalingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    provisioned_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.ProvisionedCapacityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce12248bee2c36568fe0e7c8306e19879a8018f4d2f68bc94d16564982c8c14f(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    log_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939037365c43c9a72b3c37dadef4cee49c45d340b13988d36aec42da17639cb6(
    *,
    custom_plugin_arn: builtins.str,
    revision: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d7349fb5eb5a9a9ec0860e8dad23b287cb3cd62e184b233fee93c0a26a0d51(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    delivery_stream: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7108764262b68e3cecbc01f6bb39c0838e2f09c63cf4785609dc2eb2db70f1b2(
    *,
    authentication_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cecc14be0c2fb246e15a4608e4bdd7b9eac2e2126f98c4fff5625c81b616bf9(
    *,
    encryption_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e45630a977bbe5bbdad20f00c55a2b6d7b863f0ebdd96b83af5d59aeeac6fda2(
    *,
    apache_kafka_cluster: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.ApacheKafkaClusterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24fd0806b35f57962768914d0194bea1b40b93b71c0c3dd6d6a8aad5d85e5b3d(
    *,
    worker_log_delivery: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.WorkerLogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35948a4a66b01f82e5bedaf253946f464f4c86608300c9773f71dce120de9f0d(
    *,
    custom_plugin: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.CustomPluginProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf9af2fbdc2eecf97de30bc43ea6a6be8266e58490ff4a55318a2c6b110af1b8(
    *,
    worker_count: jsii.Number,
    mcu_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991b0af73117e26499c590fefbda601c1fa27a956d8ed920c29dddf6e3942d9b(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    bucket: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12883647368b045af218938a85170c504e2ac16d35c5b7f6abdc33dcfd0b38aa(
    *,
    cpu_utilization_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab985ea028517aece904c3e9a620409a4917dc5407933921e63629b65eccaf8f(
    *,
    cpu_utilization_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2e175ee9bba2b6ccb5fe61627e4539b807b2696754acbc03a8c398ebe32a25(
    *,
    security_groups: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__410d90caf1544bb4b43be0646f325702b7ea82434e28ebcb5440055410c0f6bf(
    *,
    revision: jsii.Number,
    worker_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc89e20cb6ae15c383691c63107a6550accceb0bd180b844f01270a6c026e02a(
    *,
    cloud_watch_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.CloudWatchLogsLogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.FirehoseLogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.S3LogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12463a17cb9c37949b260894212e085ba134c7ff0644cf3913b56f022b888c0b(
    *,
    capacity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.CapacityProperty, typing.Dict[builtins.str, typing.Any]]],
    connector_configuration: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    connector_name: builtins.str,
    kafka_cluster: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterProperty, typing.Dict[builtins.str, typing.Any]]],
    kafka_cluster_client_authentication: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterClientAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]],
    kafka_cluster_encryption_in_transit: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.KafkaClusterEncryptionInTransitProperty, typing.Dict[builtins.str, typing.Any]]],
    kafka_connect_version: builtins.str,
    plugins: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.PluginProperty, typing.Dict[builtins.str, typing.Any]]]]],
    service_execution_role_arn: builtins.str,
    connector_description: typing.Optional[builtins.str] = None,
    log_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.LogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.WorkerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c82cbd22c9261a35dcdabc1becaf63f49b9257f7d5508ee8aa43d6a285cf574(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content_type: builtins.str,
    location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomPlugin.CustomPluginLocationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de4a61cefe6c2d25a1cb343ddd4a22e10b259b61229c873a373b2fa9d057114(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f576b3a446b38f6f20978c3517504ba7babed66f64bc5fb21b1c950bc4a6872a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba10e1ed6d2bc46a1ed1d1fe0ea02869794128cfcb6ebd5cadbefe02bc0a548f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dc28b9198145db094f79802e21f70587ba9ea39d8bf86eecd4baa600f164d5b(
    value: typing.Union[_IResolvable_da3f097b, CfnCustomPlugin.CustomPluginLocationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22b7cdbcdbf1c6aca15574793b79bc5bcd1b238c5d20012e24075b2de3c3e1f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e19fd5c93da0b6a93cdfdf44392a652cad52a2c961aef8c3e0a76eff5052e0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11b359e6a300e42bfcb9aa594841d75ad92accb911de61cc64790b7fc061f9fd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f77f7d7b096911e70040b0039d61af28b26c9bc89fb1faf76b0717d7c9e18b(
    *,
    file_md5: typing.Optional[builtins.str] = None,
    file_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63bbd79857b9bcc2770666f84b8116fcd6735c81fd0e1e465634b4002d175383(
    *,
    s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomPlugin.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__781a268ba9bfa781e533379ca4a5047660328871695af7ae3feb962865170db2(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff983745d275d6d3a1389c6b1984a735ff1815dde7d1308c56b56268157c0bac(
    *,
    content_type: builtins.str,
    location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomPlugin.CustomPluginLocationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b9b69a356034dd45c5e800dbc80d6a39a12c1880a5d436867eade4d8465fab4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    properties_file_content: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e9312db5b66d689fcbfe5175a48113463e0ed07e92a59d8aa13bf6e7cc2e5ba(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a145561100ff01cc7ff59a55ef33e73905f7091cbb20b0211c8b6706473d8db(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc71d30a2d2b5a6b21933eb20d227cc7424b5194fb7804fa4cb3d77dd657dbb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdac93459bf92083dd5049beb4d514f22fddfa0bd9d388dc1ef3385ce63b1af0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30511563247fe50c21e1853ef081844489c75d4646bdd82b0b64165734629e02(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a36569b41baa16c75dbfb344c8382fd94b5dc82a3a87fd538c07957efff63b2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5e8a900e9ebee6da2f64fb77eb98c44d23ed30e4b800a7e67486fadb71f6ae(
    *,
    name: builtins.str,
    properties_file_content: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
