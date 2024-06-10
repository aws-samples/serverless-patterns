'''
# Amazon ElastiCache Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_elasticache as elasticache
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ElastiCache construct libraries](https://constructs.dev/search?q=elasticache)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ElastiCache resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElastiCache.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ElastiCache](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElastiCache.html).

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
    ITaggable as _ITaggable_36806126,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCacheCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnCacheCluster",
):
    '''The ``AWS::ElastiCache::CacheCluster`` type creates an Amazon ElastiCache cache cluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html
    :cloudformationResource: AWS::ElastiCache::CacheCluster
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_cache_cluster = elasticache.CfnCacheCluster(self, "MyCfnCacheCluster",
            cache_node_type="cacheNodeType",
            engine="engine",
            num_cache_nodes=123,
        
            # the properties below are optional
            auto_minor_version_upgrade=False,
            az_mode="azMode",
            cache_parameter_group_name="cacheParameterGroupName",
            cache_security_group_names=["cacheSecurityGroupNames"],
            cache_subnet_group_name="cacheSubnetGroupName",
            cluster_name="clusterName",
            engine_version="engineVersion",
            ip_discovery="ipDiscovery",
            log_delivery_configurations=[elasticache.CfnCacheCluster.LogDeliveryConfigurationRequestProperty(
                destination_details=elasticache.CfnCacheCluster.DestinationDetailsProperty(
                    cloud_watch_logs_details=elasticache.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty(
                        log_group="logGroup"
                    ),
                    kinesis_firehose_details=elasticache.CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty(
                        delivery_stream="deliveryStream"
                    )
                ),
                destination_type="destinationType",
                log_format="logFormat",
                log_type="logType"
            )],
            network_type="networkType",
            notification_topic_arn="notificationTopicArn",
            port=123,
            preferred_availability_zone="preferredAvailabilityZone",
            preferred_availability_zones=["preferredAvailabilityZones"],
            preferred_maintenance_window="preferredMaintenanceWindow",
            snapshot_arns=["snapshotArns"],
            snapshot_name="snapshotName",
            snapshot_retention_limit=123,
            snapshot_window="snapshotWindow",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            transit_encryption_enabled=False,
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cache_node_type: builtins.str,
        engine: builtins.str,
        num_cache_nodes: jsii.Number,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        az_mode: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        ip_discovery: typing.Optional[builtins.str] = None,
        log_delivery_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCacheCluster.LogDeliveryConfigurationRequestProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        network_type: typing.Optional[builtins.str] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_availability_zone: typing.Optional[builtins.str] = None,
        preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cache_node_type: The compute and memory capacity of the nodes in the node group (shard). The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts. Changing the CacheNodeType of a Memcached instance is currently not supported. If you need to scale using Memcached, we recommend forcing a replacement update by changing the ``LogicalResourceId`` of the resource. - General purpose: - Current generation: *M6g node types:* ``cache.m6g.large`` , ``cache.m6g.xlarge`` , ``cache.m6g.2xlarge`` , ``cache.m6g.4xlarge`` , ``cache.m6g.8xlarge`` , ``cache.m6g.12xlarge`` , ``cache.m6g.16xlarge`` , ``cache.m6g.24xlarge`` *M5 node types:* ``cache.m5.large`` , ``cache.m5.xlarge`` , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge`` *M4 node types:* ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge`` *T4g node types:* ``cache.t4g.micro`` , ``cache.t4g.small`` , ``cache.t4g.medium`` *T3 node types:* ``cache.t3.micro`` , ``cache.t3.small`` , ``cache.t3.medium`` *T2 node types:* ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium`` - Previous generation: (not recommended) *T1 node types:* ``cache.t1.micro`` *M1 node types:* ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge`` *M3 node types:* ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge`` - Compute optimized: - Previous generation: (not recommended) *C1 node types:* ``cache.c1.xlarge`` - Memory optimized: - Current generation: *R6gd node types:* ``cache.r6gd.xlarge`` , ``cache.r6gd.2xlarge`` , ``cache.r6gd.4xlarge`` , ``cache.r6gd.8xlarge`` , ``cache.r6gd.12xlarge`` , ``cache.r6gd.16xlarge`` .. epigraph:: The ``r6gd`` family is available in the following regions: ``us-east-2`` , ``us-east-1`` , ``us-west-2`` , ``us-west-1`` , ``eu-west-1`` , ``eu-central-1`` , ``ap-northeast-1`` , ``ap-southeast-1`` , ``ap-southeast-2`` . *R6g node types:* ``cache.r6g.large`` , ``cache.r6g.xlarge`` , ``cache.r6g.2xlarge`` , ``cache.r6g.4xlarge`` , ``cache.r6g.8xlarge`` , ``cache.r6g.12xlarge`` , ``cache.r6g.16xlarge`` , ``cache.r6g.24xlarge`` *R5 node types:* ``cache.r5.large`` , ``cache.r5.xlarge`` , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge`` *R4 node types:* ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge`` - Previous generation: (not recommended) *M2 node types:* ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge`` *R3 node types:* ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge`` For region availability, see `Supported Node Types by Region <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion>`_ *Additional node type info* - All current generation instance types are created in Amazon VPC by default. - Redis append-only files (AOF) are not supported for T1 or T2 instances. - Redis Multi-AZ with automatic failover is not supported on T1 instances. - Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on Redis version 2.8.22 and later.
        :param engine: The name of the cache engine to be used for this cluster. Valid values for this parameter are: ``memcached`` | ``redis``
        :param num_cache_nodes: The number of cache nodes that the cache cluster should have. .. epigraph:: However, if the ``PreferredAvailabilityZone`` and ``PreferredAvailabilityZones`` properties were not previously specified and you don't specify any new values, an update requires `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param auto_minor_version_upgrade: If you are running Redis engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.
        :param az_mode: Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. This parameter is only supported for Memcached clusters. If the ``AZMode`` and ``PreferredAvailabilityZones`` are not specified, ElastiCache assumes ``single-az`` mode.
        :param cache_parameter_group_name: The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has ``cluster-enabled='yes'`` when creating a cluster.
        :param cache_security_group_names: A list of security group names to associate with this cluster. Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).
        :param cache_subnet_group_name: The name of the subnet group to be used for the cluster. Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC). .. epigraph:: If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see ``[AWS::ElastiCache::SubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html) .``
        :param cluster_name: A name for the cache cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the cache cluster. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . The name must contain 1 to 50 alphanumeric characters or hyphens. The name must start with a letter and cannot end with a hyphen or contain two consecutive hyphens.
        :param engine_version: The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation. *Important:* You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`_ ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.
        :param ip_discovery: The network type you choose when modifying a cluster, either ``ipv4`` | ``ipv6`` . IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .
        :param log_delivery_configurations: Specifies the destination, format and type of the logs.
        :param network_type: Must be either ``ipv4`` | ``ipv6`` | ``dual_stack`` . IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .
        :param notification_topic_arn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent. .. epigraph:: The Amazon SNS topic owner must be the same as the cluster owner.
        :param port: The port number on which each of the cache nodes accepts connections.
        :param preferred_availability_zone: The EC2 Availability Zone in which the cluster is created. All nodes belonging to this cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use ``PreferredAvailabilityZones`` . Default: System chosen Availability Zone.
        :param preferred_availability_zones: A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important. This option is only supported on Memcached. .. epigraph:: If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of ``NumCacheNodes`` . If you want all the nodes in the same Availability Zone, use ``PreferredAvailabilityZone`` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones.
        :param preferred_maintenance_window: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ``ddd`` are: - ``sun`` - ``mon`` - ``tue`` - ``wed`` - ``thu`` - ``fri`` - ``sat`` Example: ``sun:23:00-mon:01:30``
        :param snapshot_arns: A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas. .. epigraph:: This parameter is only valid if the ``Engine`` parameter is ``redis`` . Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``
        :param snapshot_name: The name of a Redis snapshot from which to restore data into the new node group (shard). The snapshot status changes to ``restoring`` while the new node group (shard) is being created. .. epigraph:: This parameter is only valid if the ``Engine`` parameter is ``redis`` .
        :param snapshot_retention_limit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot taken today is retained for 5 days before being deleted. .. epigraph:: This parameter is only valid if the ``Engine`` parameter is ``redis`` . Default: 0 (i.e., automatic backups are disabled for this cache cluster).
        :param snapshot_window: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard). Example: ``05:00-09:00`` If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range. .. epigraph:: This parameter is only valid if the ``Engine`` parameter is ``redis`` .
        :param tags: A list of tags to be added to this resource.
        :param transit_encryption_enabled: A flag that enables in-transit encryption when set to true.
        :param vpc_security_group_ids: One or more VPC security groups associated with the cluster. Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b878d00130d900710d9efbde27b5162741ad68343a5e4b8b7283244b24aa2b8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCacheClusterProps(
            cache_node_type=cache_node_type,
            engine=engine,
            num_cache_nodes=num_cache_nodes,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            az_mode=az_mode,
            cache_parameter_group_name=cache_parameter_group_name,
            cache_security_group_names=cache_security_group_names,
            cache_subnet_group_name=cache_subnet_group_name,
            cluster_name=cluster_name,
            engine_version=engine_version,
            ip_discovery=ip_discovery,
            log_delivery_configurations=log_delivery_configurations,
            network_type=network_type,
            notification_topic_arn=notification_topic_arn,
            port=port,
            preferred_availability_zone=preferred_availability_zone,
            preferred_availability_zones=preferred_availability_zones,
            preferred_maintenance_window=preferred_maintenance_window,
            snapshot_arns=snapshot_arns,
            snapshot_name=snapshot_name,
            snapshot_retention_limit=snapshot_retention_limit,
            snapshot_window=snapshot_window,
            tags=tags,
            transit_encryption_enabled=transit_encryption_enabled,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae530a9eb0474b9ffc367e7c2714f1d8b14943c9354c6c91d798290bf12e70ef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4dec52b5b4ebdf39402ca71f50f4dc30da259049be70433e6c00efc9ea6aba16)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationEndpointAddress")
    def attr_configuration_endpoint_address(self) -> builtins.str:
        '''The DNS hostname of the cache node.

        .. epigraph::

           Redis (cluster mode disabled) replication groups don't have this attribute. Therefore, ``Fn::GetAtt`` returns a value for this attribute only if the replication group is clustered. Otherwise, ``Fn::GetAtt`` fails.

        :cloudformationAttribute: ConfigurationEndpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationEndpointPort")
    def attr_configuration_endpoint_port(self) -> builtins.str:
        '''The port number of the configuration endpoint for the Memcached cache cluster.

        .. epigraph::

           Redis (cluster mode disabled) replication groups don't have this attribute. Therefore, ``Fn::GetAtt`` returns a value for this attribute only if the replication group is clustered. Otherwise, ``Fn::GetAtt`` fails.

        :cloudformationAttribute: ConfigurationEndpoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The resource name.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRedisEndpointAddress")
    def attr_redis_endpoint_address(self) -> builtins.str:
        '''The DNS address of the configuration endpoint for the Redis cache cluster.

        :cloudformationAttribute: RedisEndpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRedisEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrRedisEndpointPort")
    def attr_redis_endpoint_port(self) -> builtins.str:
        '''The port number of the configuration endpoint for the Redis cache cluster.

        :cloudformationAttribute: RedisEndpoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRedisEndpointPort"))

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
    @jsii.member(jsii_name="cacheNodeType")
    def cache_node_type(self) -> builtins.str:
        '''The compute and memory capacity of the nodes in the node group (shard).'''
        return typing.cast(builtins.str, jsii.get(self, "cacheNodeType"))

    @cache_node_type.setter
    def cache_node_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32d9802d6751a916028ade8020c1b88f4de76492648ad82353d20bc756837067)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheNodeType", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        '''The name of the cache engine to be used for this cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b478c5471c9d0a76c5100e39ca78b723b0c0df15786d8701347d9cb5eabbdf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="numCacheNodes")
    def num_cache_nodes(self) -> jsii.Number:
        '''The number of cache nodes that the cache cluster should have.'''
        return typing.cast(jsii.Number, jsii.get(self, "numCacheNodes"))

    @num_cache_nodes.setter
    def num_cache_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3efa7fe979ad2ca65054b031fb5cd53cdae6a1094de4cdb6bc9c480d5b2d7a9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numCacheNodes", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you are running Redis engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b74ab91b309fe8b033442df78ec7c947ef8b8ceac25b5fb4347e7e697fb388da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="azMode")
    def az_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azMode"))

    @az_mode.setter
    def az_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a44d250f986c389a2d9f94d9cca8adc9e59c15e75d4c051e15c57482b9ae9f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azMode", value)

    @builtins.property
    @jsii.member(jsii_name="cacheParameterGroupName")
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group to associate with this cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheParameterGroupName"))

    @cache_parameter_group_name.setter
    def cache_parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc3ac1b1f30d407a5545f9f5024999aba8b2072b3d9b7d1c0941506aa6431636)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="cacheSecurityGroupNames")
    def cache_security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group names to associate with this cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cacheSecurityGroupNames"))

    @cache_security_group_names.setter
    def cache_security_group_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83da5de50c36f6b8acecefb71f2d1985a98bac5b47b9355f1e680a968d3b916a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheSecurityGroupNames", value)

    @builtins.property
    @jsii.member(jsii_name="cacheSubnetGroupName")
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subnet group to be used for the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheSubnetGroupName"))

    @cache_subnet_group_name.setter
    def cache_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9b8dc42c226f2bde38136c38ed0888aa8016a952545561870cd97fdb1756c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''A name for the cache cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__411d6faf725ba835ededa6d23d62caaccc85488363ac53847d26489a9b698e4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version number of the cache engine to be used for this cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c11aa65ad582a06f82ee3dccb397779d9465180eeb2cc3743f037d45678b9315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="ipDiscovery")
    def ip_discovery(self) -> typing.Optional[builtins.str]:
        '''The network type you choose when modifying a cluster, either ``ipv4`` | ``ipv6`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipDiscovery"))

    @ip_discovery.setter
    def ip_discovery(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d9fae8437c1df5da80ef1dcc1d540757d3eeed744bbf8056a118a155cda7c0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipDiscovery", value)

    @builtins.property
    @jsii.member(jsii_name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.LogDeliveryConfigurationRequestProperty"]]]]:
        '''Specifies the destination, format and type of the logs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.LogDeliveryConfigurationRequestProperty"]]]], jsii.get(self, "logDeliveryConfigurations"))

    @log_delivery_configurations.setter
    def log_delivery_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.LogDeliveryConfigurationRequestProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92cc1290aacd3e87fdb8540c5a430dd3781b4d21f64685730ff4176b05840454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDeliveryConfigurations", value)

    @builtins.property
    @jsii.member(jsii_name="networkType")
    def network_type(self) -> typing.Optional[builtins.str]:
        '''Must be either ``ipv4`` | ``ipv6`` | ``dual_stack`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkType"))

    @network_type.setter
    def network_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fef16cd8be345649445baed2ab221599bc312c701ed3cae8a08ca0202aedbbe0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkType", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArn")
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTopicArn"))

    @notification_topic_arn.setter
    def notification_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0e5b55a4eeff9a98884374f1fb103e28154e68b08e9c604194db4263d8d260c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number on which each of the cache nodes accepts connections.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c52a7b53b9de4c47324594ae4fcae12b0f548358d236a57d0d8180b7a52eb525)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferredAvailabilityZone")
    def preferred_availability_zone(self) -> typing.Optional[builtins.str]:
        '''The EC2 Availability Zone in which the cluster is created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredAvailabilityZone"))

    @preferred_availability_zone.setter
    def preferred_availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba8deec010d483a5b4cccad86835cc42901ab76f481c5140bf432d398851cab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredAvailabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="preferredAvailabilityZones")
    def preferred_availability_zones(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the Availability Zones in which cache nodes are created.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preferredAvailabilityZones"))

    @preferred_availability_zones.setter
    def preferred_availability_zones(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdfef5e25f162b7075022826fc8305415c9b26eba0d5f6a128a30b8e191ecf2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredAvailabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which maintenance on the cluster is performed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c036bebdfade47bb20565d6116e08cbc6b2c289599c511df24ad3ec9395670fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotArns")
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snapshotArns"))

    @snapshot_arns.setter
    def snapshot_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce434b0b24d4c0aed191822a2ef96062ce0e4f82dde36706dda0cb9378020e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotArns", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of a Redis snapshot from which to restore data into the new node group (shard).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ade889ee7923a82577f80b57aeef301ae196124bdb4d5ec2cd87c371be03e5a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which ElastiCache retains automatic snapshots before deleting them.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotRetentionLimit"))

    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36088ccf4e3bb96fca149a1dc57264e825a3fdf78d280f320127ed72733b6ef2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotRetentionLimit", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotWindow")
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotWindow"))

    @snapshot_window.setter
    def snapshot_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00985af0e32e63259c356a919afbcf2f8aec8c2faedaece96112bbb03f945239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotWindow", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be added to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb033789ee709e38cf2df5c67f41474c2337ba8ce07eac9ee4a2c714fc9bc989)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag that enables in-transit encryption when set to true.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "transitEncryptionEnabled"))

    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b5c36f3eb4db3de564bb875816a147602a4348d296a24fafccdae0acba9440b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more VPC security groups associated with the cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca563dd75820580354392265b3bdcb759aaa1e66fadcc95daa9e8b3b8bc892d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group": "logGroup"},
    )
    class CloudWatchLogsDestinationDetailsProperty:
        def __init__(self, *, log_group: builtins.str) -> None:
            '''Configuration details of a CloudWatch Logs destination.

            Note that this field is marked as required but only if CloudWatch Logs was chosen as the destination.

            :param log_group: The name of the CloudWatch Logs log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                cloud_watch_logs_destination_details_property = elasticache.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty(
                    log_group="logGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b917ac927a2387372c693a2f8b0fcb5f6774e69a0fe6f786bb4da65afb46978c)
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group": log_group,
            }

        @builtins.property
        def log_group(self) -> builtins.str:
            '''The name of the CloudWatch Logs log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails.html#cfn-elasticache-cachecluster-cloudwatchlogsdestinationdetails-loggroup
            '''
            result = self._values.get("log_group")
            assert result is not None, "Required property 'log_group' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsDestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnCacheCluster.DestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_details": "cloudWatchLogsDetails",
            "kinesis_firehose_details": "kinesisFirehoseDetails",
        },
    )
    class DestinationDetailsProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_firehose_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.

            :param cloud_watch_logs_details: The configuration details of the CloudWatch Logs destination. Note that this field is marked as required but only if CloudWatch Logs was chosen as the destination.
            :param kinesis_firehose_details: The configuration details of the Kinesis Data Firehose destination. Note that this field is marked as required but only if Kinesis Data Firehose was chosen as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                destination_details_property = elasticache.CfnCacheCluster.DestinationDetailsProperty(
                    cloud_watch_logs_details=elasticache.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty(
                        log_group="logGroup"
                    ),
                    kinesis_firehose_details=elasticache.CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty(
                        delivery_stream="deliveryStream"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__000cbd02f7786299cee1e93bf5afb34c16e6ab92a2447aa9f4bf42256a0a51f1)
                check_type(argname="argument cloud_watch_logs_details", value=cloud_watch_logs_details, expected_type=type_hints["cloud_watch_logs_details"])
                check_type(argname="argument kinesis_firehose_details", value=kinesis_firehose_details, expected_type=type_hints["kinesis_firehose_details"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs_details is not None:
                self._values["cloud_watch_logs_details"] = cloud_watch_logs_details
            if kinesis_firehose_details is not None:
                self._values["kinesis_firehose_details"] = kinesis_firehose_details

        @builtins.property
        def cloud_watch_logs_details(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty"]]:
            '''The configuration details of the CloudWatch Logs destination.

            Note that this field is marked as required but only if CloudWatch Logs was chosen as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html#cfn-elasticache-cachecluster-destinationdetails-cloudwatchlogsdetails
            '''
            result = self._values.get("cloud_watch_logs_details")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty"]], result)

        @builtins.property
        def kinesis_firehose_details(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty"]]:
            '''The configuration details of the Kinesis Data Firehose destination.

            Note that this field is marked as required but only if Kinesis Data Firehose was chosen as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html#cfn-elasticache-cachecluster-destinationdetails-kinesisfirehosedetails
            '''
            result = self._values.get("kinesis_firehose_details")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"delivery_stream": "deliveryStream"},
    )
    class KinesisFirehoseDestinationDetailsProperty:
        def __init__(self, *, delivery_stream: builtins.str) -> None:
            '''The configuration details of the Kinesis Data Firehose destination.

            Note that this field is marked as required but only if Kinesis Data Firehose was chosen as the destination.

            :param delivery_stream: The name of the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                kinesis_firehose_destination_details_property = elasticache.CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty(
                    delivery_stream="deliveryStream"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5cae1eb34767a8b034d88d62d4b6f18e4d990339139fe3e1e6652a41616e9435)
                check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream": delivery_stream,
            }

        @builtins.property
        def delivery_stream(self) -> builtins.str:
            '''The name of the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails.html#cfn-elasticache-cachecluster-kinesisfirehosedestinationdetails-deliverystream
            '''
            result = self._values.get("delivery_stream")
            assert result is not None, "Required property 'delivery_stream' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnCacheCluster.LogDeliveryConfigurationRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_details": "destinationDetails",
            "destination_type": "destinationType",
            "log_format": "logFormat",
            "log_type": "logType",
        },
    )
    class LogDeliveryConfigurationRequestProperty:
        def __init__(
            self,
            *,
            destination_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCacheCluster.DestinationDetailsProperty", typing.Dict[builtins.str, typing.Any]]],
            destination_type: builtins.str,
            log_format: builtins.str,
            log_type: builtins.str,
        ) -> None:
            '''Specifies the destination, format and type of the logs.

            :param destination_details: Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.
            :param destination_type: Specify either CloudWatch Logs or Kinesis Data Firehose as the destination type. Valid values are either ``cloudwatch-logs`` or ``kinesis-firehose`` .
            :param log_format: Valid values are either ``json`` or ``text`` .
            :param log_type: Valid value is either ``slow-log`` , which refers to `slow-log <https://docs.aws.amazon.com/https://redis.io/commands/slowlog>`_ or ``engine-log`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                log_delivery_configuration_request_property = elasticache.CfnCacheCluster.LogDeliveryConfigurationRequestProperty(
                    destination_details=elasticache.CfnCacheCluster.DestinationDetailsProperty(
                        cloud_watch_logs_details=elasticache.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty(
                            log_group="logGroup"
                        ),
                        kinesis_firehose_details=elasticache.CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty(
                            delivery_stream="deliveryStream"
                        )
                    ),
                    destination_type="destinationType",
                    log_format="logFormat",
                    log_type="logType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11fd3bc6d619f2fdddcc4d0adb3f2c760e25cb0796cacc1c490de7b091ee75a0)
                check_type(argname="argument destination_details", value=destination_details, expected_type=type_hints["destination_details"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
                check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
                check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_details": destination_details,
                "destination_type": destination_type,
                "log_format": log_format,
                "log_type": log_type,
            }

        @builtins.property
        def destination_details(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.DestinationDetailsProperty"]:
            '''Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-destinationdetails
            '''
            result = self._values.get("destination_details")
            assert result is not None, "Required property 'destination_details' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCacheCluster.DestinationDetailsProperty"], result)

        @builtins.property
        def destination_type(self) -> builtins.str:
            '''Specify either CloudWatch Logs or Kinesis Data Firehose as the destination type.

            Valid values are either ``cloudwatch-logs`` or ``kinesis-firehose`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-destinationtype
            '''
            result = self._values.get("destination_type")
            assert result is not None, "Required property 'destination_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_format(self) -> builtins.str:
            '''Valid values are either ``json`` or ``text`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-logformat
            '''
            result = self._values.get("log_format")
            assert result is not None, "Required property 'log_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_type(self) -> builtins.str:
            '''Valid value is either ``slow-log`` , which refers to `slow-log <https://docs.aws.amazon.com/https://redis.io/commands/slowlog>`_ or ``engine-log`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-logtype
            '''
            result = self._values.get("log_type")
            assert result is not None, "Required property 'log_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDeliveryConfigurationRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnCacheClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "cache_node_type": "cacheNodeType",
        "engine": "engine",
        "num_cache_nodes": "numCacheNodes",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "az_mode": "azMode",
        "cache_parameter_group_name": "cacheParameterGroupName",
        "cache_security_group_names": "cacheSecurityGroupNames",
        "cache_subnet_group_name": "cacheSubnetGroupName",
        "cluster_name": "clusterName",
        "engine_version": "engineVersion",
        "ip_discovery": "ipDiscovery",
        "log_delivery_configurations": "logDeliveryConfigurations",
        "network_type": "networkType",
        "notification_topic_arn": "notificationTopicArn",
        "port": "port",
        "preferred_availability_zone": "preferredAvailabilityZone",
        "preferred_availability_zones": "preferredAvailabilityZones",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "snapshot_arns": "snapshotArns",
        "snapshot_name": "snapshotName",
        "snapshot_retention_limit": "snapshotRetentionLimit",
        "snapshot_window": "snapshotWindow",
        "tags": "tags",
        "transit_encryption_enabled": "transitEncryptionEnabled",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnCacheClusterProps:
    def __init__(
        self,
        *,
        cache_node_type: builtins.str,
        engine: builtins.str,
        num_cache_nodes: jsii.Number,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        az_mode: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        ip_discovery: typing.Optional[builtins.str] = None,
        log_delivery_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCacheCluster.LogDeliveryConfigurationRequestProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        network_type: typing.Optional[builtins.str] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_availability_zone: typing.Optional[builtins.str] = None,
        preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCacheCluster``.

        :param cache_node_type: The compute and memory capacity of the nodes in the node group (shard). The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts. Changing the CacheNodeType of a Memcached instance is currently not supported. If you need to scale using Memcached, we recommend forcing a replacement update by changing the ``LogicalResourceId`` of the resource. - General purpose: - Current generation: *M6g node types:* ``cache.m6g.large`` , ``cache.m6g.xlarge`` , ``cache.m6g.2xlarge`` , ``cache.m6g.4xlarge`` , ``cache.m6g.8xlarge`` , ``cache.m6g.12xlarge`` , ``cache.m6g.16xlarge`` , ``cache.m6g.24xlarge`` *M5 node types:* ``cache.m5.large`` , ``cache.m5.xlarge`` , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge`` *M4 node types:* ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge`` *T4g node types:* ``cache.t4g.micro`` , ``cache.t4g.small`` , ``cache.t4g.medium`` *T3 node types:* ``cache.t3.micro`` , ``cache.t3.small`` , ``cache.t3.medium`` *T2 node types:* ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium`` - Previous generation: (not recommended) *T1 node types:* ``cache.t1.micro`` *M1 node types:* ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge`` *M3 node types:* ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge`` - Compute optimized: - Previous generation: (not recommended) *C1 node types:* ``cache.c1.xlarge`` - Memory optimized: - Current generation: *R6gd node types:* ``cache.r6gd.xlarge`` , ``cache.r6gd.2xlarge`` , ``cache.r6gd.4xlarge`` , ``cache.r6gd.8xlarge`` , ``cache.r6gd.12xlarge`` , ``cache.r6gd.16xlarge`` .. epigraph:: The ``r6gd`` family is available in the following regions: ``us-east-2`` , ``us-east-1`` , ``us-west-2`` , ``us-west-1`` , ``eu-west-1`` , ``eu-central-1`` , ``ap-northeast-1`` , ``ap-southeast-1`` , ``ap-southeast-2`` . *R6g node types:* ``cache.r6g.large`` , ``cache.r6g.xlarge`` , ``cache.r6g.2xlarge`` , ``cache.r6g.4xlarge`` , ``cache.r6g.8xlarge`` , ``cache.r6g.12xlarge`` , ``cache.r6g.16xlarge`` , ``cache.r6g.24xlarge`` *R5 node types:* ``cache.r5.large`` , ``cache.r5.xlarge`` , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge`` *R4 node types:* ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge`` - Previous generation: (not recommended) *M2 node types:* ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge`` *R3 node types:* ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge`` For region availability, see `Supported Node Types by Region <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion>`_ *Additional node type info* - All current generation instance types are created in Amazon VPC by default. - Redis append-only files (AOF) are not supported for T1 or T2 instances. - Redis Multi-AZ with automatic failover is not supported on T1 instances. - Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on Redis version 2.8.22 and later.
        :param engine: The name of the cache engine to be used for this cluster. Valid values for this parameter are: ``memcached`` | ``redis``
        :param num_cache_nodes: The number of cache nodes that the cache cluster should have. .. epigraph:: However, if the ``PreferredAvailabilityZone`` and ``PreferredAvailabilityZones`` properties were not previously specified and you don't specify any new values, an update requires `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param auto_minor_version_upgrade: If you are running Redis engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.
        :param az_mode: Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. This parameter is only supported for Memcached clusters. If the ``AZMode`` and ``PreferredAvailabilityZones`` are not specified, ElastiCache assumes ``single-az`` mode.
        :param cache_parameter_group_name: The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has ``cluster-enabled='yes'`` when creating a cluster.
        :param cache_security_group_names: A list of security group names to associate with this cluster. Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).
        :param cache_subnet_group_name: The name of the subnet group to be used for the cluster. Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC). .. epigraph:: If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see ``[AWS::ElastiCache::SubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html) .``
        :param cluster_name: A name for the cache cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the cache cluster. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . The name must contain 1 to 50 alphanumeric characters or hyphens. The name must start with a letter and cannot end with a hyphen or contain two consecutive hyphens.
        :param engine_version: The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation. *Important:* You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`_ ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.
        :param ip_discovery: The network type you choose when modifying a cluster, either ``ipv4`` | ``ipv6`` . IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .
        :param log_delivery_configurations: Specifies the destination, format and type of the logs.
        :param network_type: Must be either ``ipv4`` | ``ipv6`` | ``dual_stack`` . IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .
        :param notification_topic_arn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent. .. epigraph:: The Amazon SNS topic owner must be the same as the cluster owner.
        :param port: The port number on which each of the cache nodes accepts connections.
        :param preferred_availability_zone: The EC2 Availability Zone in which the cluster is created. All nodes belonging to this cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use ``PreferredAvailabilityZones`` . Default: System chosen Availability Zone.
        :param preferred_availability_zones: A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important. This option is only supported on Memcached. .. epigraph:: If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of ``NumCacheNodes`` . If you want all the nodes in the same Availability Zone, use ``PreferredAvailabilityZone`` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones.
        :param preferred_maintenance_window: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ``ddd`` are: - ``sun`` - ``mon`` - ``tue`` - ``wed`` - ``thu`` - ``fri`` - ``sat`` Example: ``sun:23:00-mon:01:30``
        :param snapshot_arns: A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas. .. epigraph:: This parameter is only valid if the ``Engine`` parameter is ``redis`` . Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``
        :param snapshot_name: The name of a Redis snapshot from which to restore data into the new node group (shard). The snapshot status changes to ``restoring`` while the new node group (shard) is being created. .. epigraph:: This parameter is only valid if the ``Engine`` parameter is ``redis`` .
        :param snapshot_retention_limit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot taken today is retained for 5 days before being deleted. .. epigraph:: This parameter is only valid if the ``Engine`` parameter is ``redis`` . Default: 0 (i.e., automatic backups are disabled for this cache cluster).
        :param snapshot_window: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard). Example: ``05:00-09:00`` If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range. .. epigraph:: This parameter is only valid if the ``Engine`` parameter is ``redis`` .
        :param tags: A list of tags to be added to this resource.
        :param transit_encryption_enabled: A flag that enables in-transit encryption when set to true.
        :param vpc_security_group_ids: One or more VPC security groups associated with the cluster. Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_cache_cluster_props = elasticache.CfnCacheClusterProps(
                cache_node_type="cacheNodeType",
                engine="engine",
                num_cache_nodes=123,
            
                # the properties below are optional
                auto_minor_version_upgrade=False,
                az_mode="azMode",
                cache_parameter_group_name="cacheParameterGroupName",
                cache_security_group_names=["cacheSecurityGroupNames"],
                cache_subnet_group_name="cacheSubnetGroupName",
                cluster_name="clusterName",
                engine_version="engineVersion",
                ip_discovery="ipDiscovery",
                log_delivery_configurations=[elasticache.CfnCacheCluster.LogDeliveryConfigurationRequestProperty(
                    destination_details=elasticache.CfnCacheCluster.DestinationDetailsProperty(
                        cloud_watch_logs_details=elasticache.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty(
                            log_group="logGroup"
                        ),
                        kinesis_firehose_details=elasticache.CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty(
                            delivery_stream="deliveryStream"
                        )
                    ),
                    destination_type="destinationType",
                    log_format="logFormat",
                    log_type="logType"
                )],
                network_type="networkType",
                notification_topic_arn="notificationTopicArn",
                port=123,
                preferred_availability_zone="preferredAvailabilityZone",
                preferred_availability_zones=["preferredAvailabilityZones"],
                preferred_maintenance_window="preferredMaintenanceWindow",
                snapshot_arns=["snapshotArns"],
                snapshot_name="snapshotName",
                snapshot_retention_limit=123,
                snapshot_window="snapshotWindow",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                transit_encryption_enabled=False,
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d011d844fc37e1278b56242476eb6678a2ec76110ae295205b57260221f991ae)
            check_type(argname="argument cache_node_type", value=cache_node_type, expected_type=type_hints["cache_node_type"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument num_cache_nodes", value=num_cache_nodes, expected_type=type_hints["num_cache_nodes"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument az_mode", value=az_mode, expected_type=type_hints["az_mode"])
            check_type(argname="argument cache_parameter_group_name", value=cache_parameter_group_name, expected_type=type_hints["cache_parameter_group_name"])
            check_type(argname="argument cache_security_group_names", value=cache_security_group_names, expected_type=type_hints["cache_security_group_names"])
            check_type(argname="argument cache_subnet_group_name", value=cache_subnet_group_name, expected_type=type_hints["cache_subnet_group_name"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument ip_discovery", value=ip_discovery, expected_type=type_hints["ip_discovery"])
            check_type(argname="argument log_delivery_configurations", value=log_delivery_configurations, expected_type=type_hints["log_delivery_configurations"])
            check_type(argname="argument network_type", value=network_type, expected_type=type_hints["network_type"])
            check_type(argname="argument notification_topic_arn", value=notification_topic_arn, expected_type=type_hints["notification_topic_arn"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_availability_zone", value=preferred_availability_zone, expected_type=type_hints["preferred_availability_zone"])
            check_type(argname="argument preferred_availability_zones", value=preferred_availability_zones, expected_type=type_hints["preferred_availability_zones"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument snapshot_arns", value=snapshot_arns, expected_type=type_hints["snapshot_arns"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument snapshot_retention_limit", value=snapshot_retention_limit, expected_type=type_hints["snapshot_retention_limit"])
            check_type(argname="argument snapshot_window", value=snapshot_window, expected_type=type_hints["snapshot_window"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transit_encryption_enabled", value=transit_encryption_enabled, expected_type=type_hints["transit_encryption_enabled"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cache_node_type": cache_node_type,
            "engine": engine,
            "num_cache_nodes": num_cache_nodes,
        }
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if az_mode is not None:
            self._values["az_mode"] = az_mode
        if cache_parameter_group_name is not None:
            self._values["cache_parameter_group_name"] = cache_parameter_group_name
        if cache_security_group_names is not None:
            self._values["cache_security_group_names"] = cache_security_group_names
        if cache_subnet_group_name is not None:
            self._values["cache_subnet_group_name"] = cache_subnet_group_name
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if ip_discovery is not None:
            self._values["ip_discovery"] = ip_discovery
        if log_delivery_configurations is not None:
            self._values["log_delivery_configurations"] = log_delivery_configurations
        if network_type is not None:
            self._values["network_type"] = network_type
        if notification_topic_arn is not None:
            self._values["notification_topic_arn"] = notification_topic_arn
        if port is not None:
            self._values["port"] = port
        if preferred_availability_zone is not None:
            self._values["preferred_availability_zone"] = preferred_availability_zone
        if preferred_availability_zones is not None:
            self._values["preferred_availability_zones"] = preferred_availability_zones
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if snapshot_arns is not None:
            self._values["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if snapshot_retention_limit is not None:
            self._values["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshot_window is not None:
            self._values["snapshot_window"] = snapshot_window
        if tags is not None:
            self._values["tags"] = tags
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def cache_node_type(self) -> builtins.str:
        '''The compute and memory capacity of the nodes in the node group (shard).

        The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts. Changing the CacheNodeType of a Memcached instance is currently not supported. If you need to scale using Memcached, we recommend forcing a replacement update by changing the ``LogicalResourceId`` of the resource.

        - General purpose:
        - Current generation:

        *M6g node types:* ``cache.m6g.large`` , ``cache.m6g.xlarge`` , ``cache.m6g.2xlarge`` , ``cache.m6g.4xlarge`` , ``cache.m6g.8xlarge`` , ``cache.m6g.12xlarge`` , ``cache.m6g.16xlarge`` , ``cache.m6g.24xlarge``

        *M5 node types:* ``cache.m5.large`` , ``cache.m5.xlarge`` , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge``

        *M4 node types:* ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``

        *T4g node types:* ``cache.t4g.micro`` , ``cache.t4g.small`` , ``cache.t4g.medium``

        *T3 node types:* ``cache.t3.micro`` , ``cache.t3.small`` , ``cache.t3.medium``

        *T2 node types:* ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        - Previous generation: (not recommended)

        *T1 node types:* ``cache.t1.micro``

        *M1 node types:* ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``

        *M3 node types:* ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        - Compute optimized:
        - Previous generation: (not recommended)

        *C1 node types:* ``cache.c1.xlarge``

        - Memory optimized:
        - Current generation:

        *R6gd node types:* ``cache.r6gd.xlarge`` , ``cache.r6gd.2xlarge`` , ``cache.r6gd.4xlarge`` , ``cache.r6gd.8xlarge`` , ``cache.r6gd.12xlarge`` , ``cache.r6gd.16xlarge``
        .. epigraph::

           The ``r6gd`` family is available in the following regions: ``us-east-2`` , ``us-east-1`` , ``us-west-2`` , ``us-west-1`` , ``eu-west-1`` , ``eu-central-1`` , ``ap-northeast-1`` , ``ap-southeast-1`` , ``ap-southeast-2`` .

        *R6g node types:* ``cache.r6g.large`` , ``cache.r6g.xlarge`` , ``cache.r6g.2xlarge`` , ``cache.r6g.4xlarge`` , ``cache.r6g.8xlarge`` , ``cache.r6g.12xlarge`` , ``cache.r6g.16xlarge`` , ``cache.r6g.24xlarge``

        *R5 node types:* ``cache.r5.large`` , ``cache.r5.xlarge`` , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge``

        *R4 node types:* ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        - Previous generation: (not recommended)

        *M2 node types:* ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``

        *R3 node types:* ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

        For region availability, see `Supported Node Types by Region <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion>`_

        *Additional node type info*

        - All current generation instance types are created in Amazon VPC by default.
        - Redis append-only files (AOF) are not supported for T1 or T2 instances.
        - Redis Multi-AZ with automatic failover is not supported on T1 instances.
        - Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on Redis version 2.8.22 and later.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-cachenodetype
        '''
        result = self._values.get("cache_node_type")
        assert result is not None, "Required property 'cache_node_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine(self) -> builtins.str:
        '''The name of the cache engine to be used for this cluster.

        Valid values for this parameter are: ``memcached`` | ``redis``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-engine
        '''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def num_cache_nodes(self) -> jsii.Number:
        '''The number of cache nodes that the cache cluster should have.

        .. epigraph::

           However, if the ``PreferredAvailabilityZone`` and ``PreferredAvailabilityZones`` properties were not previously specified and you don't specify any new values, an update requires `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-numcachenodes
        '''
        result = self._values.get("num_cache_nodes")
        assert result is not None, "Required property 'num_cache_nodes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you are running Redis engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def az_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.

        This parameter is only supported for Memcached clusters.

        If the ``AZMode`` and ``PreferredAvailabilityZones`` are not specified, ElastiCache assumes ``single-az`` mode.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-azmode
        '''
        result = self._values.get("az_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group to associate with this cluster.

        If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has ``cluster-enabled='yes'`` when creating a cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-cacheparametergroupname
        '''
        result = self._values.get("cache_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group names to associate with this cluster.

        Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-cachesecuritygroupnames
        '''
        result = self._values.get("cache_security_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subnet group to be used for the cluster.

        Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).
        .. epigraph::

           If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see ``[AWS::ElastiCache::SubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html) .``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-cachesubnetgroupname
        '''
        result = self._values.get("cache_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''A name for the cache cluster.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the cache cluster. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        The name must contain 1 to 50 alphanumeric characters or hyphens. The name must start with a letter and cannot end with a hyphen or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-clustername
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version number of the cache engine to be used for this cluster.

        To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.

        *Important:* You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`_ ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_discovery(self) -> typing.Optional[builtins.str]:
        '''The network type you choose when modifying a cluster, either ``ipv4`` | ``ipv6`` .

        IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-ipdiscovery
        '''
        result = self._values.get("ip_discovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCacheCluster.LogDeliveryConfigurationRequestProperty]]]]:
        '''Specifies the destination, format and type of the logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-logdeliveryconfigurations
        '''
        result = self._values.get("log_delivery_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCacheCluster.LogDeliveryConfigurationRequestProperty]]]], result)

    @builtins.property
    def network_type(self) -> typing.Optional[builtins.str]:
        '''Must be either ``ipv4`` | ``ipv6`` | ``dual_stack`` .

        IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-networktype
        '''
        result = self._values.get("network_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.

        .. epigraph::

           The Amazon SNS topic owner must be the same as the cluster owner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-notificationtopicarn
        '''
        result = self._values.get("notification_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number on which each of the cache nodes accepts connections.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_availability_zone(self) -> typing.Optional[builtins.str]:
        '''The EC2 Availability Zone in which the cluster is created.

        All nodes belonging to this cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use ``PreferredAvailabilityZones`` .

        Default: System chosen Availability Zone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-preferredavailabilityzone
        '''
        result = self._values.get("preferred_availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_availability_zones(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the Availability Zones in which cache nodes are created.

        The order of the zones in the list is not important.

        This option is only supported on Memcached.
        .. epigraph::

           If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.

           The number of Availability Zones listed must equal the value of ``NumCacheNodes`` .

        If you want all the nodes in the same Availability Zone, use ``PreferredAvailabilityZone`` instead, or repeat the Availability Zone multiple times in the list.

        Default: System chosen Availability Zones.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-preferredavailabilityzones
        '''
        result = self._values.get("preferred_availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which maintenance on the cluster is performed.

        It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        - ``sun``
        - ``mon``
        - ``tue``
        - ``wed``
        - ``thu``
        - ``fri``
        - ``sat``

        Example: ``sun:23:00-mon:01:30``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3.

        The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.
        .. epigraph::

           This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-snapshotarns
        '''
        result = self._values.get("snapshot_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of a Redis snapshot from which to restore data into the new node group (shard).

        The snapshot status changes to ``restoring`` while the new node group (shard) is being created.
        .. epigraph::

           This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-snapshotname
        '''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which ElastiCache retains automatic snapshots before deleting them.

        For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot taken today is retained for 5 days before being deleted.
        .. epigraph::

           This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        Default: 0 (i.e., automatic backups are disabled for this cache cluster).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-snapshotretentionlimit
        '''
        result = self._values.get("snapshot_retention_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
        .. epigraph::

           This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-snapshotwindow
        '''
        result = self._values.get("snapshot_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be added to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag that enables in-transit encryption when set to true.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-transitencryptionenabled
        '''
        result = self._values.get("transit_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more VPC security groups associated with the cluster.

        Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html#cfn-elasticache-cachecluster-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCacheClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGlobalReplicationGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnGlobalReplicationGroup",
):
    '''Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different Amazon region.

    The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

    - The *GlobalReplicationGroupIdSuffix* represents the name of the Global datastore, which is what you use to associate a secondary cluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html
    :cloudformationResource: AWS::ElastiCache::GlobalReplicationGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_global_replication_group = elasticache.CfnGlobalReplicationGroup(self, "MyCfnGlobalReplicationGroup",
            members=[elasticache.CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty(
                replication_group_id="replicationGroupId",
                replication_group_region="replicationGroupRegion",
                role="role"
            )],
        
            # the properties below are optional
            automatic_failover_enabled=False,
            cache_node_type="cacheNodeType",
            cache_parameter_group_name="cacheParameterGroupName",
            engine_version="engineVersion",
            global_node_group_count=123,
            global_replication_group_description="globalReplicationGroupDescription",
            global_replication_group_id_suffix="globalReplicationGroupIdSuffix",
            regional_configurations=[elasticache.CfnGlobalReplicationGroup.RegionalConfigurationProperty(
                replication_group_id="replicationGroupId",
                replication_group_region="replicationGroupRegion",
                resharding_configurations=[elasticache.CfnGlobalReplicationGroup.ReshardingConfigurationProperty(
                    node_group_id="nodeGroupId",
                    preferred_availability_zones=["preferredAvailabilityZones"]
                )]
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        members: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty", typing.Dict[builtins.str, typing.Any]]]]],
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cache_node_type: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        global_node_group_count: typing.Optional[jsii.Number] = None,
        global_replication_group_description: typing.Optional[builtins.str] = None,
        global_replication_group_id_suffix: typing.Optional[builtins.str] = None,
        regional_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGlobalReplicationGroup.RegionalConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param members: The replication groups that comprise the Global datastore.
        :param automatic_failover_enabled: Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails. ``AutomaticFailoverEnabled`` must be enabled for Redis (cluster mode enabled) replication groups.
        :param cache_node_type: The cache node type of the Global datastore.
        :param cache_parameter_group_name: The name of the cache parameter group to use with the Global datastore. It must be compatible with the major engine version used by the Global datastore.
        :param engine_version: The Elasticache Redis engine version.
        :param global_node_group_count: The number of node groups that comprise the Global Datastore.
        :param global_replication_group_description: The optional description of the Global datastore.
        :param global_replication_group_id_suffix: The suffix name of a Global Datastore. The suffix guarantees uniqueness of the Global Datastore name across multiple regions.
        :param regional_configurations: The Regions that comprise the Global Datastore.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b347e00f869706c90d3dc918dc3fb240c81a3a2e15ca55cb3a114e779ebe3be)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGlobalReplicationGroupProps(
            members=members,
            automatic_failover_enabled=automatic_failover_enabled,
            cache_node_type=cache_node_type,
            cache_parameter_group_name=cache_parameter_group_name,
            engine_version=engine_version,
            global_node_group_count=global_node_group_count,
            global_replication_group_description=global_replication_group_description,
            global_replication_group_id_suffix=global_replication_group_id_suffix,
            regional_configurations=regional_configurations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__884a154d8b8e4d93c61fe6b39de707bf773a6d1033e974181f93658b1039c0c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab038bf042b008b9efadcbadf432cd0ac40752df55c21a630a9780aae3ef72f0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGlobalReplicationGroupId")
    def attr_global_replication_group_id(self) -> builtins.str:
        '''The ID used to associate a secondary cluster to the Global Replication Group.

        :cloudformationAttribute: GlobalReplicationGroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGlobalReplicationGroupId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the Global Datastore.

        Can be ``Creating`` , ``Modifying`` , ``Available`` , ``Deleting`` or ``Primary-Only`` . Primary-only status indicates the global datastore contains only a primary cluster. Either all secondary clusters are deleted or not successfully created.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty"]]]:
        '''The replication groups that comprise the Global datastore.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty"]]], jsii.get(self, "members"))

    @members.setter
    def members(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e868e518f50b5b48c699f872e36b8e20be2702ad6acf8d5f4500e986aac55b3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value)

    @builtins.property
    @jsii.member(jsii_name="automaticFailoverEnabled")
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "automaticFailoverEnabled"))

    @automatic_failover_enabled.setter
    def automatic_failover_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f937e9779d5fe5d88540d353152c5e7637a4c898506e495763dc389bca1a193)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticFailoverEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cacheNodeType")
    def cache_node_type(self) -> typing.Optional[builtins.str]:
        '''The cache node type of the Global datastore.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheNodeType"))

    @cache_node_type.setter
    def cache_node_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc0668ac08361dfeaf1c9d3b63f4ce55339cbac4acdba22253a2c6a39440c9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheNodeType", value)

    @builtins.property
    @jsii.member(jsii_name="cacheParameterGroupName")
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cache parameter group to use with the Global datastore.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheParameterGroupName"))

    @cache_parameter_group_name.setter
    def cache_parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0848ddc407bc59c23bb3f0758cd29c2ca80ecb4af0b703cfbabe761143efb996)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The Elasticache Redis engine version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6d37e14147abb9446aa94586bbfdc04bcc4cbad9c87b170bc3c934223a3dc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="globalNodeGroupCount")
    def global_node_group_count(self) -> typing.Optional[jsii.Number]:
        '''The number of node groups that comprise the Global Datastore.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "globalNodeGroupCount"))

    @global_node_group_count.setter
    def global_node_group_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96e8402ce6e7036902a30a006b2e3b7c82ed86d4655e500c78d0ae603a7929b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNodeGroupCount", value)

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupDescription")
    def global_replication_group_description(self) -> typing.Optional[builtins.str]:
        '''The optional description of the Global datastore.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupDescription"))

    @global_replication_group_description.setter
    def global_replication_group_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb8c976f8e943135a48d97d88bf3d8b7dd5f17fcd2b8759518b8b204056bba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalReplicationGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupIdSuffix")
    def global_replication_group_id_suffix(self) -> typing.Optional[builtins.str]:
        '''The suffix name of a Global Datastore.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupIdSuffix"))

    @global_replication_group_id_suffix.setter
    def global_replication_group_id_suffix(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65acba21207d62e08b1c8c4c4f55ea3089c76799e113952d0b5f8bd4e6ee53d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalReplicationGroupIdSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="regionalConfigurations")
    def regional_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGlobalReplicationGroup.RegionalConfigurationProperty"]]]]:
        '''The Regions that comprise the Global Datastore.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGlobalReplicationGroup.RegionalConfigurationProperty"]]]], jsii.get(self, "regionalConfigurations"))

    @regional_configurations.setter
    def regional_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGlobalReplicationGroup.RegionalConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efeee031dd310c05cefd1733ccdb9d7b436fc018669200525c6f11542ae97dac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionalConfigurations", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty",
        jsii_struct_bases=[],
        name_mapping={
            "replication_group_id": "replicationGroupId",
            "replication_group_region": "replicationGroupRegion",
            "role": "role",
        },
    )
    class GlobalReplicationGroupMemberProperty:
        def __init__(
            self,
            *,
            replication_group_id: typing.Optional[builtins.str] = None,
            replication_group_region: typing.Optional[builtins.str] = None,
            role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A member of a Global datastore.

            It contains the Replication Group Id, the Amazon region and the role of the replication group.

            :param replication_group_id: The replication group id of the Global datastore member.
            :param replication_group_region: The Amazon region of the Global datastore member.
            :param role: Indicates the role of the replication group, ``PRIMARY`` or ``SECONDARY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                global_replication_group_member_property = elasticache.CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty(
                    replication_group_id="replicationGroupId",
                    replication_group_region="replicationGroupRegion",
                    role="role"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d920057dfab2caaf1f89662c7570bd431d43559ca99a0846f6d46dae7369f9eb)
                check_type(argname="argument replication_group_id", value=replication_group_id, expected_type=type_hints["replication_group_id"])
                check_type(argname="argument replication_group_region", value=replication_group_region, expected_type=type_hints["replication_group_region"])
                check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if replication_group_id is not None:
                self._values["replication_group_id"] = replication_group_id
            if replication_group_region is not None:
                self._values["replication_group_region"] = replication_group_region
            if role is not None:
                self._values["role"] = role

        @builtins.property
        def replication_group_id(self) -> typing.Optional[builtins.str]:
            '''The replication group id of the Global datastore member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-replicationgroupid
            '''
            result = self._values.get("replication_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replication_group_region(self) -> typing.Optional[builtins.str]:
            '''The Amazon region of the Global datastore member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-replicationgroupregion
            '''
            result = self._values.get("replication_group_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role(self) -> typing.Optional[builtins.str]:
            '''Indicates the role of the replication group, ``PRIMARY`` or ``SECONDARY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-role
            '''
            result = self._values.get("role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlobalReplicationGroupMemberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnGlobalReplicationGroup.RegionalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "replication_group_id": "replicationGroupId",
            "replication_group_region": "replicationGroupRegion",
            "resharding_configurations": "reshardingConfigurations",
        },
    )
    class RegionalConfigurationProperty:
        def __init__(
            self,
            *,
            replication_group_id: typing.Optional[builtins.str] = None,
            replication_group_region: typing.Optional[builtins.str] = None,
            resharding_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGlobalReplicationGroup.ReshardingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A list of the replication groups.

            :param replication_group_id: The name of the secondary cluster.
            :param replication_group_region: The Amazon region where the cluster is stored.
            :param resharding_configurations: A list of PreferredAvailabilityZones objects that specifies the configuration of a node group in the resharded cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                regional_configuration_property = elasticache.CfnGlobalReplicationGroup.RegionalConfigurationProperty(
                    replication_group_id="replicationGroupId",
                    replication_group_region="replicationGroupRegion",
                    resharding_configurations=[elasticache.CfnGlobalReplicationGroup.ReshardingConfigurationProperty(
                        node_group_id="nodeGroupId",
                        preferred_availability_zones=["preferredAvailabilityZones"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aeaef8528e85da7f76144633387f423a352cf7a00b93f64470683d2a67c7bd57)
                check_type(argname="argument replication_group_id", value=replication_group_id, expected_type=type_hints["replication_group_id"])
                check_type(argname="argument replication_group_region", value=replication_group_region, expected_type=type_hints["replication_group_region"])
                check_type(argname="argument resharding_configurations", value=resharding_configurations, expected_type=type_hints["resharding_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if replication_group_id is not None:
                self._values["replication_group_id"] = replication_group_id
            if replication_group_region is not None:
                self._values["replication_group_region"] = replication_group_region
            if resharding_configurations is not None:
                self._values["resharding_configurations"] = resharding_configurations

        @builtins.property
        def replication_group_id(self) -> typing.Optional[builtins.str]:
            '''The name of the secondary cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-replicationgroupid
            '''
            result = self._values.get("replication_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replication_group_region(self) -> typing.Optional[builtins.str]:
            '''The Amazon region where the cluster is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-replicationgroupregion
            '''
            result = self._values.get("replication_group_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resharding_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGlobalReplicationGroup.ReshardingConfigurationProperty"]]]]:
            '''A list of PreferredAvailabilityZones objects that specifies the configuration of a node group in the resharded cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-reshardingconfigurations
            '''
            result = self._values.get("resharding_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGlobalReplicationGroup.ReshardingConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegionalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnGlobalReplicationGroup.ReshardingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "node_group_id": "nodeGroupId",
            "preferred_availability_zones": "preferredAvailabilityZones",
        },
    )
    class ReshardingConfigurationProperty:
        def __init__(
            self,
            *,
            node_group_id: typing.Optional[builtins.str] = None,
            preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A list of ``PreferredAvailabilityZones`` objects that specifies the configuration of a node group in the resharded cluster.

            :param node_group_id: Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.
            :param preferred_availability_zones: A list of preferred availability zones for the nodes in this cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                resharding_configuration_property = elasticache.CfnGlobalReplicationGroup.ReshardingConfigurationProperty(
                    node_group_id="nodeGroupId",
                    preferred_availability_zones=["preferredAvailabilityZones"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f5a9e68366040209fa4fb9f8e50eff4e9b1ae9ea0da836153a13ff22b2202ad5)
                check_type(argname="argument node_group_id", value=node_group_id, expected_type=type_hints["node_group_id"])
                check_type(argname="argument preferred_availability_zones", value=preferred_availability_zones, expected_type=type_hints["preferred_availability_zones"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if node_group_id is not None:
                self._values["node_group_id"] = node_group_id
            if preferred_availability_zones is not None:
                self._values["preferred_availability_zones"] = preferred_availability_zones

        @builtins.property
        def node_group_id(self) -> typing.Optional[builtins.str]:
            '''Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-nodegroupid
            '''
            result = self._values.get("node_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preferred_availability_zones(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of preferred availability zones for the nodes in this cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-preferredavailabilityzones
            '''
            result = self._values.get("preferred_availability_zones")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReshardingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnGlobalReplicationGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "members": "members",
        "automatic_failover_enabled": "automaticFailoverEnabled",
        "cache_node_type": "cacheNodeType",
        "cache_parameter_group_name": "cacheParameterGroupName",
        "engine_version": "engineVersion",
        "global_node_group_count": "globalNodeGroupCount",
        "global_replication_group_description": "globalReplicationGroupDescription",
        "global_replication_group_id_suffix": "globalReplicationGroupIdSuffix",
        "regional_configurations": "regionalConfigurations",
    },
)
class CfnGlobalReplicationGroupProps:
    def __init__(
        self,
        *,
        members: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty, typing.Dict[builtins.str, typing.Any]]]]],
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cache_node_type: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        global_node_group_count: typing.Optional[jsii.Number] = None,
        global_replication_group_description: typing.Optional[builtins.str] = None,
        global_replication_group_id_suffix: typing.Optional[builtins.str] = None,
        regional_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGlobalReplicationGroup.RegionalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGlobalReplicationGroup``.

        :param members: The replication groups that comprise the Global datastore.
        :param automatic_failover_enabled: Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails. ``AutomaticFailoverEnabled`` must be enabled for Redis (cluster mode enabled) replication groups.
        :param cache_node_type: The cache node type of the Global datastore.
        :param cache_parameter_group_name: The name of the cache parameter group to use with the Global datastore. It must be compatible with the major engine version used by the Global datastore.
        :param engine_version: The Elasticache Redis engine version.
        :param global_node_group_count: The number of node groups that comprise the Global Datastore.
        :param global_replication_group_description: The optional description of the Global datastore.
        :param global_replication_group_id_suffix: The suffix name of a Global Datastore. The suffix guarantees uniqueness of the Global Datastore name across multiple regions.
        :param regional_configurations: The Regions that comprise the Global Datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_global_replication_group_props = elasticache.CfnGlobalReplicationGroupProps(
                members=[elasticache.CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty(
                    replication_group_id="replicationGroupId",
                    replication_group_region="replicationGroupRegion",
                    role="role"
                )],
            
                # the properties below are optional
                automatic_failover_enabled=False,
                cache_node_type="cacheNodeType",
                cache_parameter_group_name="cacheParameterGroupName",
                engine_version="engineVersion",
                global_node_group_count=123,
                global_replication_group_description="globalReplicationGroupDescription",
                global_replication_group_id_suffix="globalReplicationGroupIdSuffix",
                regional_configurations=[elasticache.CfnGlobalReplicationGroup.RegionalConfigurationProperty(
                    replication_group_id="replicationGroupId",
                    replication_group_region="replicationGroupRegion",
                    resharding_configurations=[elasticache.CfnGlobalReplicationGroup.ReshardingConfigurationProperty(
                        node_group_id="nodeGroupId",
                        preferred_availability_zones=["preferredAvailabilityZones"]
                    )]
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265dda90953e13518f66b5357e00050b92a09e4dfb295f7b765b5b5d55951ace)
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument automatic_failover_enabled", value=automatic_failover_enabled, expected_type=type_hints["automatic_failover_enabled"])
            check_type(argname="argument cache_node_type", value=cache_node_type, expected_type=type_hints["cache_node_type"])
            check_type(argname="argument cache_parameter_group_name", value=cache_parameter_group_name, expected_type=type_hints["cache_parameter_group_name"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument global_node_group_count", value=global_node_group_count, expected_type=type_hints["global_node_group_count"])
            check_type(argname="argument global_replication_group_description", value=global_replication_group_description, expected_type=type_hints["global_replication_group_description"])
            check_type(argname="argument global_replication_group_id_suffix", value=global_replication_group_id_suffix, expected_type=type_hints["global_replication_group_id_suffix"])
            check_type(argname="argument regional_configurations", value=regional_configurations, expected_type=type_hints["regional_configurations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "members": members,
        }
        if automatic_failover_enabled is not None:
            self._values["automatic_failover_enabled"] = automatic_failover_enabled
        if cache_node_type is not None:
            self._values["cache_node_type"] = cache_node_type
        if cache_parameter_group_name is not None:
            self._values["cache_parameter_group_name"] = cache_parameter_group_name
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if global_node_group_count is not None:
            self._values["global_node_group_count"] = global_node_group_count
        if global_replication_group_description is not None:
            self._values["global_replication_group_description"] = global_replication_group_description
        if global_replication_group_id_suffix is not None:
            self._values["global_replication_group_id_suffix"] = global_replication_group_id_suffix
        if regional_configurations is not None:
            self._values["regional_configurations"] = regional_configurations

    @builtins.property
    def members(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty]]]:
        '''The replication groups that comprise the Global datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-members
        '''
        result = self._values.get("members")
        assert result is not None, "Required property 'members' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty]]], result)

    @builtins.property
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.

        ``AutomaticFailoverEnabled`` must be enabled for Redis (cluster mode enabled) replication groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-automaticfailoverenabled
        '''
        result = self._values.get("automatic_failover_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def cache_node_type(self) -> typing.Optional[builtins.str]:
        '''The cache node type of the Global datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-cachenodetype
        '''
        result = self._values.get("cache_node_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cache parameter group to use with the Global datastore.

        It must be compatible with the major engine version used by the Global datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-cacheparametergroupname
        '''
        result = self._values.get("cache_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The Elasticache Redis engine version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_node_group_count(self) -> typing.Optional[jsii.Number]:
        '''The number of node groups that comprise the Global Datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalnodegroupcount
        '''
        result = self._values.get("global_node_group_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def global_replication_group_description(self) -> typing.Optional[builtins.str]:
        '''The optional description of the Global datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupdescription
        '''
        result = self._values.get("global_replication_group_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_replication_group_id_suffix(self) -> typing.Optional[builtins.str]:
        '''The suffix name of a Global Datastore.

        The suffix guarantees uniqueness of the Global Datastore name across multiple regions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupidsuffix
        '''
        result = self._values.get("global_replication_group_id_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regional_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGlobalReplicationGroup.RegionalConfigurationProperty]]]]:
        '''The Regions that comprise the Global Datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-regionalconfigurations
        '''
        result = self._values.get("regional_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGlobalReplicationGroup.RegionalConfigurationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGlobalReplicationGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnParameterGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnParameterGroup",
):
    '''The ``AWS::ElastiCache::ParameterGroup`` type creates a new cache parameter group.

    Cache parameter groups control the parameters for a cache cluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-parametergroup.html
    :cloudformationResource: AWS::ElastiCache::ParameterGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_parameter_group = elasticache.CfnParameterGroup(self, "MyCfnParameterGroup",
            cache_parameter_group_family="cacheParameterGroupFamily",
            description="description",
        
            # the properties below are optional
            properties={
                "properties_key": "properties"
            },
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
        cache_parameter_group_family: builtins.str,
        description: builtins.str,
        properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cache_parameter_group_family: The name of the cache parameter group family that this cache parameter group is compatible with. Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``memcached1.6`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2`` | ``redis4.0`` | ``redis5.0`` | ``redis6.x`` | ``redis7``
        :param description: The description for this cache parameter group.
        :param properties: A comma-delimited list of parameter name/value pairs. For example:: "Properties" : { "cas_disabled" : "1", "chunk_size_growth_factor" : "1.02" }
        :param tags: A tag that can be added to an ElastiCache parameter group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your parameter groups. A tag with a null Value is permitted.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86f3b322f4ea3d0cc63e18e1b285cc656e6d789289e29668aa7acce95fdb892d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnParameterGroupProps(
            cache_parameter_group_family=cache_parameter_group_family,
            description=description,
            properties=properties,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4df9ac5cd73e00bfbbdce4db59984040d76705d9fed6f259b98c08569946c00b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2ce285a081ee552c80c88bf27503daba85ce16849e3599360c22241be30e55e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCacheParameterGroupName")
    def attr_cache_parameter_group_name(self) -> builtins.str:
        '''A user-specified name for the cache parameter group.

        :cloudformationAttribute: CacheParameterGroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCacheParameterGroupName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="cacheParameterGroupFamily")
    def cache_parameter_group_family(self) -> builtins.str:
        '''The name of the cache parameter group family that this cache parameter group is compatible with.'''
        return typing.cast(builtins.str, jsii.get(self, "cacheParameterGroupFamily"))

    @cache_parameter_group_family.setter
    def cache_parameter_group_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c887b1c7836e155f15fbcb98f5393a2b92b4a33873814732bea60f4f1b225f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheParameterGroupFamily", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description for this cache parameter group.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__131595ea286a946147c38535eb5fcf0537b68b2132e909e191998a1e3f21d5f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''A comma-delimited list of parameter name/value pairs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "properties"))

    @properties.setter
    def properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad995d05e00fe4d7296f16776a975d33eb5d75180391440607e5d71ae30d1f08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A tag that can be added to an ElastiCache parameter group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f00caea2443ab3a4d0d9d2f1836e1d360d238f759643e2af050c00c5ea4f3efb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "cache_parameter_group_family": "cacheParameterGroupFamily",
        "description": "description",
        "properties": "properties",
        "tags": "tags",
    },
)
class CfnParameterGroupProps:
    def __init__(
        self,
        *,
        cache_parameter_group_family: builtins.str,
        description: builtins.str,
        properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnParameterGroup``.

        :param cache_parameter_group_family: The name of the cache parameter group family that this cache parameter group is compatible with. Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``memcached1.6`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2`` | ``redis4.0`` | ``redis5.0`` | ``redis6.x`` | ``redis7``
        :param description: The description for this cache parameter group.
        :param properties: A comma-delimited list of parameter name/value pairs. For example:: "Properties" : { "cas_disabled" : "1", "chunk_size_growth_factor" : "1.02" }
        :param tags: A tag that can be added to an ElastiCache parameter group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your parameter groups. A tag with a null Value is permitted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-parametergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_parameter_group_props = elasticache.CfnParameterGroupProps(
                cache_parameter_group_family="cacheParameterGroupFamily",
                description="description",
            
                # the properties below are optional
                properties={
                    "properties_key": "properties"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56da2ad187e00defe2d3a6812e7eea3611b1990da4526952f58e2f80cfa1c36b)
            check_type(argname="argument cache_parameter_group_family", value=cache_parameter_group_family, expected_type=type_hints["cache_parameter_group_family"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cache_parameter_group_family": cache_parameter_group_family,
            "description": description,
        }
        if properties is not None:
            self._values["properties"] = properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cache_parameter_group_family(self) -> builtins.str:
        '''The name of the cache parameter group family that this cache parameter group is compatible with.

        Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``memcached1.6`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2`` | ``redis4.0`` | ``redis5.0`` | ``redis6.x`` | ``redis7``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-parametergroup.html#cfn-elasticache-parametergroup-cacheparametergroupfamily
        '''
        result = self._values.get("cache_parameter_group_family")
        assert result is not None, "Required property 'cache_parameter_group_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''The description for this cache parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-parametergroup.html#cfn-elasticache-parametergroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''A comma-delimited list of parameter name/value pairs.

        For example::

           "Properties" : { "cas_disabled" : "1", "chunk_size_growth_factor" : "1.02"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-parametergroup.html#cfn-elasticache-parametergroup-properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A tag that can be added to an ElastiCache parameter group.

        Tags are composed of a Key/Value pair. You can use tags to categorize and track all your parameter groups. A tag with a null Value is permitted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-parametergroup.html#cfn-elasticache-parametergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnReplicationGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnReplicationGroup",
):
    '''The ``AWS::ElastiCache::ReplicationGroup`` resource creates an Amazon ElastiCache Redis replication group.

    A Redis (cluster mode disabled) replication group is a collection of cache clusters, where one of the clusters is a primary read-write cluster and the others are read-only replicas.

    A Redis (cluster mode enabled) cluster is comprised of from 1 to 90 shards (API/CLI: node groups). Each shard has a primary node and up to 5 read-only replica nodes. The configuration can range from 90 shards and 0 replicas to 15 shards and 5 replicas, which is the maximum number or replicas allowed.

    The node or shard limit can be increased to a maximum of 500 per cluster if the Redis engine version is 5.0.6 or higher. For example, you can choose to configure a 500 node cluster that ranges between 83 shards (one primary and 5 replicas per shard) and 500 shards (single primary and no replicas). Make sure there are enough available IP addresses to accommodate the increase. Common pitfalls include the subnets in the subnet group have too small a CIDR range or the subnets are shared and heavily used by other clusters. For more information, see `Creating a Subnet Group <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SubnetGroups.Creating.html>`_ . For versions below 5.0.6, the limit is 250 per cluster.

    To request a limit increase, see `Amazon Service Limits <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>`_ and choose the limit type *Nodes per cluster per instance type* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html
    :cloudformationResource: AWS::ElastiCache::ReplicationGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_replication_group = elasticache.CfnReplicationGroup(self, "MyCfnReplicationGroup",
            replication_group_description="replicationGroupDescription",
        
            # the properties below are optional
            at_rest_encryption_enabled=False,
            auth_token="authToken",
            automatic_failover_enabled=False,
            auto_minor_version_upgrade=False,
            cache_node_type="cacheNodeType",
            cache_parameter_group_name="cacheParameterGroupName",
            cache_security_group_names=["cacheSecurityGroupNames"],
            cache_subnet_group_name="cacheSubnetGroupName",
            cluster_mode="clusterMode",
            data_tiering_enabled=False,
            engine="engine",
            engine_version="engineVersion",
            global_replication_group_id="globalReplicationGroupId",
            ip_discovery="ipDiscovery",
            kms_key_id="kmsKeyId",
            log_delivery_configurations=[elasticache.CfnReplicationGroup.LogDeliveryConfigurationRequestProperty(
                destination_details=elasticache.CfnReplicationGroup.DestinationDetailsProperty(
                    cloud_watch_logs_details=elasticache.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty(
                        log_group="logGroup"
                    ),
                    kinesis_firehose_details=elasticache.CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty(
                        delivery_stream="deliveryStream"
                    )
                ),
                destination_type="destinationType",
                log_format="logFormat",
                log_type="logType"
            )],
            multi_az_enabled=False,
            network_type="networkType",
            node_group_configuration=[elasticache.CfnReplicationGroup.NodeGroupConfigurationProperty(
                node_group_id="nodeGroupId",
                primary_availability_zone="primaryAvailabilityZone",
                replica_availability_zones=["replicaAvailabilityZones"],
                replica_count=123,
                slots="slots"
            )],
            notification_topic_arn="notificationTopicArn",
            num_cache_clusters=123,
            num_node_groups=123,
            port=123,
            preferred_cache_cluster_aZs=["preferredCacheClusterAZs"],
            preferred_maintenance_window="preferredMaintenanceWindow",
            primary_cluster_id="primaryClusterId",
            replicas_per_node_group=123,
            replication_group_id="replicationGroupId",
            security_group_ids=["securityGroupIds"],
            snapshot_arns=["snapshotArns"],
            snapshot_name="snapshotName",
            snapshot_retention_limit=123,
            snapshotting_cluster_id="snapshottingClusterId",
            snapshot_window="snapshotWindow",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            transit_encryption_enabled=False,
            transit_encryption_mode="transitEncryptionMode",
            user_group_ids=["userGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        replication_group_description: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cache_node_type: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_mode: typing.Optional[builtins.str] = None,
        data_tiering_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        global_replication_group_id: typing.Optional[builtins.str] = None,
        ip_discovery: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_delivery_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationGroup.LogDeliveryConfigurationRequestProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        multi_az_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        network_type: typing.Optional[builtins.str] = None,
        node_group_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationGroup.NodeGroupConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        num_cache_clusters: typing.Optional[jsii.Number] = None,
        num_node_groups: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_cache_cluster_a_zs: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        primary_cluster_id: typing.Optional[builtins.str] = None,
        replicas_per_node_group: typing.Optional[jsii.Number] = None,
        replication_group_id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshotting_cluster_id: typing.Optional[builtins.str] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        transit_encryption_mode: typing.Optional[builtins.str] = None,
        user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param replication_group_description: A user-created description for the replication group.
        :param at_rest_encryption_enabled: A flag that enables encryption at rest when set to ``true`` . You cannot modify the value of ``AtRestEncryptionEnabled`` after the replication group is created. To enable encryption at rest on a replication group you must set ``AtRestEncryptionEnabled`` to ``true`` when you create the replication group. *Required:* Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` onward. Default: ``false``
        :param auth_token: *Reserved parameter.* The password used to access a password protected server. ``AuthToken`` can be specified only on replication groups where ``TransitEncryptionEnabled`` is ``true`` . For more information, see `Authenticating Users with the Redis AUTH Command <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html>`_ . .. epigraph:: For HIPAA compliance, you must specify ``TransitEncryptionEnabled`` as ``true`` , an ``AuthToken`` , and a ``CacheSubnetGroup`` . Password constraints: - Must be only printable ASCII characters. - Must be at least 16 characters and no more than 128 characters in length. - Nonalphanumeric characters are restricted to (!, &, #, $, ^, <, >, -, ). For more information, see `AUTH password <https://docs.aws.amazon.com/http://redis.io/commands/AUTH>`_ at http://redis.io/commands/AUTH. .. epigraph:: If ADDING the AuthToken, update requires `Replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param automatic_failover_enabled: Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails. ``AutomaticFailoverEnabled`` must be enabled for Redis (cluster mode enabled) replication groups. Default: false
        :param auto_minor_version_upgrade: If you are running Redis engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.
        :param cache_node_type: The compute and memory capacity of the nodes in the node group (shard). The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts. - General purpose: - Current generation: *M6g node types:* ``cache.m6g.large`` , ``cache.m6g.xlarge`` , ``cache.m6g.2xlarge`` , ``cache.m6g.4xlarge`` , ``cache.m6g.12xlarge`` , ``cache.m6g.24xlarge`` *M5 node types:* ``cache.m5.large`` , ``cache.m5.xlarge`` , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge`` *M4 node types:* ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge`` *T4g node types:* ``cache.t4g.micro`` , ``cache.t4g.small`` , ``cache.t4g.medium`` *T3 node types:* ``cache.t3.micro`` , ``cache.t3.small`` , ``cache.t3.medium`` *T2 node types:* ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium`` - Previous generation: (not recommended) *T1 node types:* ``cache.t1.micro`` *M1 node types:* ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge`` *M3 node types:* ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge`` - Compute optimized: - Previous generation: (not recommended) *C1 node types:* ``cache.c1.xlarge`` - Memory optimized: - Current generation: *R6gd node types:* ``cache.r6gd.xlarge`` , ``cache.r6gd.2xlarge`` , ``cache.r6gd.4xlarge`` , ``cache.r6gd.8xlarge`` , ``cache.r6gd.12xlarge`` , ``cache.r6gd.16xlarge`` .. epigraph:: The ``r6gd`` family is available in the following regions: ``us-east-2`` , ``us-east-1`` , ``us-west-2`` , ``us-west-1`` , ``eu-west-1`` , ``eu-central-1`` , ``ap-northeast-1`` , ``ap-southeast-1`` , ``ap-southeast-2`` . *R6g node types:* ``cache.r6g.large`` , ``cache.r6g.xlarge`` , ``cache.r6g.2xlarge`` , ``cache.r6g.4xlarge`` , ``cache.r6g.12xlarge`` , ``cache.r6g.24xlarge`` *R5 node types:* ``cache.r5.large`` , ``cache.r5.xlarge`` , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge`` *R4 node types:* ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge`` - Previous generation: (not recommended) *M2 node types:* ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge`` *R3 node types:* ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge`` For region availability, see `Supported Node Types by Amazon Region <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion>`_
        :param cache_parameter_group_name: The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used. If you are running Redis version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name. - To create a Redis (cluster mode disabled) replication group, use ``CacheParameterGroupName=default.redis3.2`` . - To create a Redis (cluster mode enabled) replication group, use ``CacheParameterGroupName=default.redis3.2.cluster.on`` .
        :param cache_security_group_names: A list of cache security group names to associate with this replication group.
        :param cache_subnet_group_name: The name of the cache subnet group to be used for the replication group. .. epigraph:: If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see `AWS::ElastiCache::SubnetGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html>`_ .
        :param cluster_mode: Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Redis clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Redis clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled. For more information, see `Modify cluster mode <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/modify-cluster-mode.html>`_ .
        :param data_tiering_enabled: Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see `Data tiering <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/data-tiering.html>`_ .
        :param engine: The name of the cache engine to be used for the clusters in this replication group. The value must be set to ``Redis`` .
        :param engine_version: The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the ``DescribeCacheEngineVersions`` operation. *Important:* You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`_ ) in the *ElastiCache User Guide* , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.
        :param global_replication_group_id: The name of the Global datastore.
        :param ip_discovery: The network type you choose when creating a replication group, either ``ipv4`` | ``ipv6`` . IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .
        :param kms_key_id: The ID of the KMS key used to encrypt the disk on the cluster.
        :param log_delivery_configurations: Specifies the destination, format and type of the logs.
        :param multi_az_enabled: A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see `Minimizing Downtime: Multi-AZ <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/AutoFailover.html>`_ .
        :param network_type: Must be either ``ipv4`` | ``ipv6`` | ``dual_stack`` . IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .
        :param node_group_configuration: ``NodeGroupConfiguration`` is a property of the ``AWS::ElastiCache::ReplicationGroup`` resource that configures an Amazon ElastiCache (ElastiCache) Redis cluster node group. If you set `UseOnlineResharding <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding>`_ to ``true`` , you can update ``NodeGroupConfiguration`` without interruption. When ``UseOnlineResharding`` is set to ``false`` , or is not specified, updating ``NodeGroupConfiguration`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param notification_topic_arn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent. .. epigraph:: The Amazon SNS topic owner must be the same as the cluster owner.
        :param num_cache_clusters: The number of clusters this replication group initially has. This parameter is not used if there is more than one node group (shard). You should use ``ReplicasPerNodeGroup`` instead. If ``AutomaticFailoverEnabled`` is ``true`` , the value of this parameter must be at least 2. If ``AutomaticFailoverEnabled`` is ``false`` you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6. The maximum permitted value for ``NumCacheClusters`` is 6 (1 primary plus 5 replicas).
        :param num_node_groups: An optional parameter that specifies the number of node groups (shards) for this Redis (cluster mode enabled) replication group. For Redis (cluster mode disabled) either omit this parameter or set it to 1. If you set `UseOnlineResharding <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding>`_ to ``true`` , you can update ``NumNodeGroups`` without interruption. When ``UseOnlineResharding`` is set to ``false`` , or is not specified, updating ``NumNodeGroups`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ . Default: 1
        :param port: The port number on which each member of the replication group accepts connections.
        :param preferred_cache_cluster_a_zs: A list of EC2 Availability Zones in which the replication group's clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list. This parameter is not used if there is more than one node group (shard). You should use ``NodeGroupConfiguration`` instead. .. epigraph:: If you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of ``NumCacheClusters`` . Default: system chosen Availability Zones.
        :param preferred_maintenance_window: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ``ddd`` are: - ``sun`` - ``mon`` - ``tue`` - ``wed`` - ``thu`` - ``fri`` - ``sat`` Example: ``sun:23:00-mon:01:30``
        :param primary_cluster_id: The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of ``available`` . This parameter is not required if ``NumCacheClusters`` , ``NumNodeGroups`` , or ``ReplicasPerNodeGroup`` is specified.
        :param replicas_per_node_group: An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.
        :param replication_group_id: 
        :param security_group_ids: One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).
        :param snapshot_arns: A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter *NumNodeGroups* or the number of node groups configured by *NodeGroupConfiguration* regardless of the number of ARNs specified here. Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``
        :param snapshot_name: The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to ``restoring`` while the new replication group is being created.
        :param snapshot_retention_limit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted. Default: 0 (i.e., automatic backups are disabled for this cluster).
        :param snapshotting_cluster_id: The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Redis (cluster mode enabled) replication groups.
        :param snapshot_window: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard). Example: ``05:00-09:00`` If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
        :param tags: A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key= ``myKey`` , Value= ``myKeyValue`` . You can include multiple tags as shown following: Key= ``myKey`` , Value= ``myKeyValue`` Key= ``mySecondKey`` , Value= ``mySecondKeyValue`` . Tags on replication groups will be replicated to all nodes.
        :param transit_encryption_enabled: A flag that enables in-transit encryption when set to ``true`` . You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster. This parameter is valid only if the ``Engine`` parameter is ``redis`` , the ``EngineVersion`` parameter is ``3.2.6`` or ``4.x`` onward, and the cluster is being created in an Amazon VPC. If you enable in-transit encryption, you must also specify a value for ``CacheSubnetGroup`` . *Required:* Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` onward. Default: ``false`` .. epigraph:: For HIPAA compliance, you must specify ``TransitEncryptionEnabled`` as ``true`` , an ``AuthToken`` , and a ``CacheSubnetGroup`` .
        :param transit_encryption_mode: A setting that allows you to migrate your clients to use in-transit encryption, with no downtime. When setting ``TransitEncryptionEnabled`` to ``true`` , you can set your ``TransitEncryptionMode`` to ``preferred`` in the same request, to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Redis clients to use encrypted connections you can modify the value to ``required`` to allow encrypted connections only. Setting ``TransitEncryptionMode`` to ``required`` is a two-step process that requires you to first set the ``TransitEncryptionMode`` to ``preferred`` , after that you can set ``TransitEncryptionMode`` to ``required`` . This process will not trigger the replacement of the replication group.
        :param user_group_ids: The ID of user group to associate with the replication group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be27fffa79ab6bf194b2d0d4de1313299c709e45a12e57a99e85fb26cf0e5f50)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationGroupProps(
            replication_group_description=replication_group_description,
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            auth_token=auth_token,
            automatic_failover_enabled=automatic_failover_enabled,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            cache_node_type=cache_node_type,
            cache_parameter_group_name=cache_parameter_group_name,
            cache_security_group_names=cache_security_group_names,
            cache_subnet_group_name=cache_subnet_group_name,
            cluster_mode=cluster_mode,
            data_tiering_enabled=data_tiering_enabled,
            engine=engine,
            engine_version=engine_version,
            global_replication_group_id=global_replication_group_id,
            ip_discovery=ip_discovery,
            kms_key_id=kms_key_id,
            log_delivery_configurations=log_delivery_configurations,
            multi_az_enabled=multi_az_enabled,
            network_type=network_type,
            node_group_configuration=node_group_configuration,
            notification_topic_arn=notification_topic_arn,
            num_cache_clusters=num_cache_clusters,
            num_node_groups=num_node_groups,
            port=port,
            preferred_cache_cluster_a_zs=preferred_cache_cluster_a_zs,
            preferred_maintenance_window=preferred_maintenance_window,
            primary_cluster_id=primary_cluster_id,
            replicas_per_node_group=replicas_per_node_group,
            replication_group_id=replication_group_id,
            security_group_ids=security_group_ids,
            snapshot_arns=snapshot_arns,
            snapshot_name=snapshot_name,
            snapshot_retention_limit=snapshot_retention_limit,
            snapshotting_cluster_id=snapshotting_cluster_id,
            snapshot_window=snapshot_window,
            tags=tags,
            transit_encryption_enabled=transit_encryption_enabled,
            transit_encryption_mode=transit_encryption_mode,
            user_group_ids=user_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93d988a8a188908fd1e785a707cc68edf28a1ba53bd404b971490bcb7100e29a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e69031f1e65767cd224fc587374f20072359815a32df0eaa95f2428da70c2e0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationEndPointAddress")
    def attr_configuration_end_point_address(self) -> builtins.str:
        '''The DNS hostname of the cache node.

        .. epigraph::

           Redis (cluster mode disabled) replication groups don't have this attribute. Therefore, ``Fn::GetAtt`` returns a value for this attribute only if the replication group is clustered. Otherwise, ``Fn::GetAtt`` fails. For Redis (cluster mode disabled) replication groups, use the ``PrimaryEndpoint`` or ``ReadEndpoint`` attributes.

        :cloudformationAttribute: ConfigurationEndPoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationEndPointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationEndPointPort")
    def attr_configuration_end_point_port(self) -> builtins.str:
        '''The port number that the cache engine is listening on.

        :cloudformationAttribute: ConfigurationEndPoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationEndPointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrPrimaryEndPointAddress")
    def attr_primary_end_point_address(self) -> builtins.str:
        '''The DNS address of the primary read-write cache node.

        :cloudformationAttribute: PrimaryEndPoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrimaryEndPointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrPrimaryEndPointPort")
    def attr_primary_end_point_port(self) -> builtins.str:
        '''The number of the port that the primary read-write cache engine is listening on.

        :cloudformationAttribute: PrimaryEndPoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrimaryEndPointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrReadEndPointAddresses")
    def attr_read_end_point_addresses(self) -> builtins.str:
        '''A string with a list of endpoints for the primary and read-only replicas.

        The order of the addresses maps to the order of the ports from the ``ReadEndPoint.Ports`` attribute.

        :cloudformationAttribute: ReadEndPoint.Addresses
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReadEndPointAddresses"))

    @builtins.property
    @jsii.member(jsii_name="attrReadEndPointAddressesList")
    def attr_read_end_point_addresses_list(self) -> typing.List[builtins.str]:
        '''A string with a list of endpoints for the read-only replicas.

        The order of the addresses maps to the order of the ports from the ``ReadEndPoint.Ports`` attribute.

        :cloudformationAttribute: ReadEndPoint.Addresses.List
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrReadEndPointAddressesList"))

    @builtins.property
    @jsii.member(jsii_name="attrReadEndPointPorts")
    def attr_read_end_point_ports(self) -> builtins.str:
        '''A string with a list of ports for the read-only replicas.

        The order of the ports maps to the order of the addresses from the ``ReadEndPoint.Addresses`` attribute.

        :cloudformationAttribute: ReadEndPoint.Ports
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReadEndPointPorts"))

    @builtins.property
    @jsii.member(jsii_name="attrReadEndPointPortsList")
    def attr_read_end_point_ports_list(self) -> typing.List[builtins.str]:
        '''A string with a list of ports for the read-only replicas.

        The order of the ports maps to the order of the addresses from the ReadEndPoint.Addresses attribute.

        :cloudformationAttribute: ReadEndPoint.Ports.List
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrReadEndPointPortsList"))

    @builtins.property
    @jsii.member(jsii_name="attrReaderEndPointAddress")
    def attr_reader_end_point_address(self) -> builtins.str:
        '''The address of the reader endpoint.

        :cloudformationAttribute: ReaderEndPoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReaderEndPointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrReaderEndPointPort")
    def attr_reader_end_point_port(self) -> builtins.str:
        '''The port used by the reader endpoint.

        :cloudformationAttribute: ReaderEndPoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReaderEndPointPort"))

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
    @jsii.member(jsii_name="replicationGroupDescription")
    def replication_group_description(self) -> builtins.str:
        '''A user-created description for the replication group.'''
        return typing.cast(builtins.str, jsii.get(self, "replicationGroupDescription"))

    @replication_group_description.setter
    def replication_group_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c907ced1d032518ebc8883a36eb0edf181bc2da76408e75eb584c864b5fefc9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag that enables encryption at rest when set to ``true`` .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "atRestEncryptionEnabled"))

    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa546aa730ad1a4db1a42606474b6045ffc32ec777b50d6ba31f3dbdab3a48df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "atRestEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> typing.Optional[builtins.str]:
        '''*Reserved parameter.* The password used to access a password protected server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea5f85de07d00909dedcebd441b02e117efc2077a1e3d87f54c5a27f5206a2f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authToken", value)

    @builtins.property
    @jsii.member(jsii_name="automaticFailoverEnabled")
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "automaticFailoverEnabled"))

    @automatic_failover_enabled.setter
    def automatic_failover_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b966eb1df615199d14bbc7fd9f3b39c9f4709837783a9a97f8945e6c623dc56d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticFailoverEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you are running Redis engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b4cffb8c5e43d27133f190ebeba6d314ad935e730a8628bef824306d4d6356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="cacheNodeType")
    def cache_node_type(self) -> typing.Optional[builtins.str]:
        '''The compute and memory capacity of the nodes in the node group (shard).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheNodeType"))

    @cache_node_type.setter
    def cache_node_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed33482a5f3a397014d26a736ced8371cfd5f7dcf12071c4629c9100b4d0c3cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheNodeType", value)

    @builtins.property
    @jsii.member(jsii_name="cacheParameterGroupName")
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group to associate with this replication group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheParameterGroupName"))

    @cache_parameter_group_name.setter
    def cache_parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62c80def577fbbf2efb0e92fb3bd6946c8ffca559bbc2222843991c0c59a8e05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="cacheSecurityGroupNames")
    def cache_security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of cache security group names to associate with this replication group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cacheSecurityGroupNames"))

    @cache_security_group_names.setter
    def cache_security_group_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a35e383106650eefc6c3b806779d5aa3ad36ed505bd7313e11d94c5942d9c7b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheSecurityGroupNames", value)

    @builtins.property
    @jsii.member(jsii_name="cacheSubnetGroupName")
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cache subnet group to be used for the replication group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheSubnetGroupName"))

    @cache_subnet_group_name.setter
    def cache_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b7e9b4af342ce71884b10c5713679cc1987727399ee466ef6c6e86653dcb21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterMode")
    def cluster_mode(self) -> typing.Optional[builtins.str]:
        '''Enabled or Disabled.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterMode"))

    @cluster_mode.setter
    def cluster_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843c2d711df69b9b78c5297321a7377fd4d364b0b8b228ae665fcbdffa0084f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterMode", value)

    @builtins.property
    @jsii.member(jsii_name="dataTieringEnabled")
    def data_tiering_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables data tiering.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "dataTieringEnabled"))

    @data_tiering_enabled.setter
    def data_tiering_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4366a0fcdd44e261b8f1399689f3ac4bb635223727a5c70ecced2835cb18c15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTieringEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> typing.Optional[builtins.str]:
        '''The name of the cache engine to be used for the clusters in this replication group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43efae7f07eb2d768b51436a460dd83ae934b30a7e7cc3f3b825cfd6e5ece68d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version number of the cache engine to be used for the clusters in this replication group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5337b37fc62ed19c046ae6e4e85b8fe97cdcd4eb2fd571decbfe563e2f9bbcf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupId")
    def global_replication_group_id(self) -> typing.Optional[builtins.str]:
        '''The name of the Global datastore.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupId"))

    @global_replication_group_id.setter
    def global_replication_group_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf74e5c2399e48c43d257f5ef3f61c24fce45668db9e5f6d537ce076f935f780)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalReplicationGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="ipDiscovery")
    def ip_discovery(self) -> typing.Optional[builtins.str]:
        '''The network type you choose when creating a replication group, either ``ipv4`` | ``ipv6`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipDiscovery"))

    @ip_discovery.setter
    def ip_discovery(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea227ab737c3768eb9268ca4b7aad2a651bd5c80b060dd89e792f94c91fce7f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipDiscovery", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key used to encrypt the disk on the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dda541c47a7be91143fbe227b05e172ef4b46d5657366c1ffff09fbb9c0c5c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.LogDeliveryConfigurationRequestProperty"]]]]:
        '''Specifies the destination, format and type of the logs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.LogDeliveryConfigurationRequestProperty"]]]], jsii.get(self, "logDeliveryConfigurations"))

    @log_delivery_configurations.setter
    def log_delivery_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.LogDeliveryConfigurationRequestProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6abdf1dfe7ce2cb6bd74fcf5e71f8d01354d2ebe730f2f8811c7cca3c29115c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDeliveryConfigurations", value)

    @builtins.property
    @jsii.member(jsii_name="multiAzEnabled")
    def multi_az_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag indicating if you have Multi-AZ enabled to enhance fault tolerance.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "multiAzEnabled"))

    @multi_az_enabled.setter
    def multi_az_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ea9e8732e19a78795fe185be2450c918f0ad9505938ce18be98a47595e698f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiAzEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="networkType")
    def network_type(self) -> typing.Optional[builtins.str]:
        '''Must be either ``ipv4`` | ``ipv6`` | ``dual_stack`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkType"))

    @network_type.setter
    def network_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83454ca7ec99c5872b43df5ecd3a494e042cd44f7b50d58f4bf1e6e8b660215d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkType", value)

    @builtins.property
    @jsii.member(jsii_name="nodeGroupConfiguration")
    def node_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.NodeGroupConfigurationProperty"]]]]:
        '''``NodeGroupConfiguration`` is a property of the ``AWS::ElastiCache::ReplicationGroup`` resource that configures an Amazon ElastiCache (ElastiCache) Redis cluster node group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.NodeGroupConfigurationProperty"]]]], jsii.get(self, "nodeGroupConfiguration"))

    @node_group_configuration.setter
    def node_group_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.NodeGroupConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__063232de740d4c4cf752ba9532e0b046f204c4d85a17ea560f3688d5c78d5126)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeGroupConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArn")
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTopicArn"))

    @notification_topic_arn.setter
    def notification_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afad0ef82bb9acf280293dc8234bcbfb68b0aee8e38631e29e8b0f5c0edf6436)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="numCacheClusters")
    def num_cache_clusters(self) -> typing.Optional[jsii.Number]:
        '''The number of clusters this replication group initially has.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numCacheClusters"))

    @num_cache_clusters.setter
    def num_cache_clusters(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3effd0ee3abc632945998cd5c58c40c2e61c166d48aeaff02c46cb4fe172fa68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numCacheClusters", value)

    @builtins.property
    @jsii.member(jsii_name="numNodeGroups")
    def num_node_groups(self) -> typing.Optional[jsii.Number]:
        '''An optional parameter that specifies the number of node groups (shards) for this Redis (cluster mode enabled) replication group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numNodeGroups"))

    @num_node_groups.setter
    def num_node_groups(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06693a02af2ea54d169b325b01dbc6b4f0fac1ded78e060c7120b709bf82ffd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numNodeGroups", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number on which each member of the replication group accepts connections.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77a4995911ee86ef96fab9b8d7683bd6b21726901334b6e0f5b1cd65c358352)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferredCacheClusterAZs")
    def preferred_cache_cluster_a_zs(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of EC2 Availability Zones in which the replication group's clusters are created.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preferredCacheClusterAZs"))

    @preferred_cache_cluster_a_zs.setter
    def preferred_cache_cluster_a_zs(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3b98acbb3854c5584ac0d1b3f958aaab9acda203560a42576b7da590dd3efbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredCacheClusterAZs", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which maintenance on the cluster is performed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f06ffee046ee6aaf7c317d0ec481f014335323a835adf240ab1d537b192e36e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="primaryClusterId")
    def primary_cluster_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the cluster that serves as the primary for this replication group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryClusterId"))

    @primary_cluster_id.setter
    def primary_cluster_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6512d6a9d409265e09a0a87e261fcba517621c20846549f6b30152801b2e3dee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> typing.Optional[jsii.Number]:
        '''An optional parameter that specifies the number of replica nodes in each node group (shard).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicasPerNodeGroup"))

    @replicas_per_node_group.setter
    def replicas_per_node_group(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cf71395d4de3cd4ca74d713e8070b525f88cd095892c0b97826bec127eea35d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicasPerNodeGroup", value)

    @builtins.property
    @jsii.member(jsii_name="replicationGroupId")
    def replication_group_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationGroupId"))

    @replication_group_id.setter
    def replication_group_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e382d1b245c43974606107b80af8da9323e7d5a4ec30a874e85fd0d8383a979)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more Amazon VPC security groups associated with this replication group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4bf0b926d5ed122589bca93144684bbbc765d5b48d2b43dc65e20ac75999870)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotArns")
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored in Amazon S3.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snapshotArns"))

    @snapshot_arns.setter
    def snapshot_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__402bbedebe63e1639250243d98564e9d2abaf2ea4be044a6e822afb9573ba83b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotArns", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of a snapshot from which to restore data into the new replication group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf64b55611f1dcd1385926cc1344d345fe6bb1210d40fc47034fe65bbdb3da34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which ElastiCache retains automatic snapshots before deleting them.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotRetentionLimit"))

    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca3b912d486d6471befbdcc0a4f6371d9c6d4fce14489c5c146523f37b67d03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotRetentionLimit", value)

    @builtins.property
    @jsii.member(jsii_name="snapshottingClusterId")
    def snapshotting_cluster_id(self) -> typing.Optional[builtins.str]:
        '''The cluster ID that is used as the daily snapshot source for the replication group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshottingClusterId"))

    @snapshotting_cluster_id.setter
    def snapshotting_cluster_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04e859b223e2f5a28ae2572ed09bf8cef9bbf00ed7571a437a364307bc63f338)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshottingClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotWindow")
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotWindow"))

    @snapshot_window.setter
    def snapshot_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eca3a583f11466198815da8e0f733144c677e601f7fbc08ff2f53b0f251ce1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotWindow", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be added to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd34df081f3adeec74e0b10c42a2c6579d5328d707ac88af6a4c22338f3c9035)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag that enables in-transit encryption when set to ``true`` .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "transitEncryptionEnabled"))

    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af0273d0b69e8bd3f65054f8d56651f1f9d315c9e60fa092dd4b8e4e8844e85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionMode")
    def transit_encryption_mode(self) -> typing.Optional[builtins.str]:
        '''A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitEncryptionMode"))

    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e42c150539724e50fcb5c3e35f3cc6d260890eb3e8dedeaaac606a9539b75a56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="userGroupIds")
    def user_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ID of user group to associate with the replication group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "userGroupIds"))

    @user_group_ids.setter
    def user_group_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52e181f655740159c1c7f60264045e188418edbe6d092594dbf15cce26263f01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroupIds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group": "logGroup"},
    )
    class CloudWatchLogsDestinationDetailsProperty:
        def __init__(self, *, log_group: builtins.str) -> None:
            '''The configuration details of the CloudWatch Logs destination.

            Note that this field is marked as required but only if CloudWatch Logs was chosen as the destination.

            :param log_group: The name of the CloudWatch Logs log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-cloudwatchlogsdestinationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                cloud_watch_logs_destination_details_property = elasticache.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty(
                    log_group="logGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d33b9d3b5876c576f6687dd170e2161cb8acc01f4eeae0ae299a3a279b24467d)
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group": log_group,
            }

        @builtins.property
        def log_group(self) -> builtins.str:
            '''The name of the CloudWatch Logs log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-cloudwatchlogsdestinationdetails.html#cfn-elasticache-replicationgroup-cloudwatchlogsdestinationdetails-loggroup
            '''
            result = self._values.get("log_group")
            assert result is not None, "Required property 'log_group' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsDestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnReplicationGroup.DestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_details": "cloudWatchLogsDetails",
            "kinesis_firehose_details": "kinesisFirehoseDetails",
        },
    )
    class DestinationDetailsProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_firehose_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.

            :param cloud_watch_logs_details: The configuration details of the CloudWatch Logs destination. Note that this field is marked as required but only if CloudWatch Logs was chosen as the destination.
            :param kinesis_firehose_details: The configuration details of the Kinesis Data Firehose destination. Note that this field is marked as required but only if Kinesis Data Firehose was chosen as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                destination_details_property = elasticache.CfnReplicationGroup.DestinationDetailsProperty(
                    cloud_watch_logs_details=elasticache.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty(
                        log_group="logGroup"
                    ),
                    kinesis_firehose_details=elasticache.CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty(
                        delivery_stream="deliveryStream"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6393b162360e08ba34e1e81372da9a50f39c9a0cc3e234d4de5535a2bb554fe6)
                check_type(argname="argument cloud_watch_logs_details", value=cloud_watch_logs_details, expected_type=type_hints["cloud_watch_logs_details"])
                check_type(argname="argument kinesis_firehose_details", value=kinesis_firehose_details, expected_type=type_hints["kinesis_firehose_details"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs_details is not None:
                self._values["cloud_watch_logs_details"] = cloud_watch_logs_details
            if kinesis_firehose_details is not None:
                self._values["kinesis_firehose_details"] = kinesis_firehose_details

        @builtins.property
        def cloud_watch_logs_details(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty"]]:
            '''The configuration details of the CloudWatch Logs destination.

            Note that this field is marked as required but only if CloudWatch Logs was chosen as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html#cfn-elasticache-replicationgroup-destinationdetails-cloudwatchlogsdetails
            '''
            result = self._values.get("cloud_watch_logs_details")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty"]], result)

        @builtins.property
        def kinesis_firehose_details(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty"]]:
            '''The configuration details of the Kinesis Data Firehose destination.

            Note that this field is marked as required but only if Kinesis Data Firehose was chosen as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html#cfn-elasticache-replicationgroup-destinationdetails-kinesisfirehosedetails
            '''
            result = self._values.get("kinesis_firehose_details")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"delivery_stream": "deliveryStream"},
    )
    class KinesisFirehoseDestinationDetailsProperty:
        def __init__(self, *, delivery_stream: builtins.str) -> None:
            '''The configuration details of the Kinesis Data Firehose destination.

            Note that this field is marked as required but only if Kinesis Data Firehose was chosen as the destination.

            :param delivery_stream: The name of the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-kinesisfirehosedestinationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                kinesis_firehose_destination_details_property = elasticache.CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty(
                    delivery_stream="deliveryStream"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fdcf378b5d4262b2df61cdeb35e6e804ff747472fc30e69109cb47a8aed0fbad)
                check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream": delivery_stream,
            }

        @builtins.property
        def delivery_stream(self) -> builtins.str:
            '''The name of the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-kinesisfirehosedestinationdetails.html#cfn-elasticache-replicationgroup-kinesisfirehosedestinationdetails-deliverystream
            '''
            result = self._values.get("delivery_stream")
            assert result is not None, "Required property 'delivery_stream' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnReplicationGroup.LogDeliveryConfigurationRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_details": "destinationDetails",
            "destination_type": "destinationType",
            "log_format": "logFormat",
            "log_type": "logType",
        },
    )
    class LogDeliveryConfigurationRequestProperty:
        def __init__(
            self,
            *,
            destination_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationGroup.DestinationDetailsProperty", typing.Dict[builtins.str, typing.Any]]],
            destination_type: builtins.str,
            log_format: builtins.str,
            log_type: builtins.str,
        ) -> None:
            '''Specifies the destination, format and type of the logs.

            :param destination_details: Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.
            :param destination_type: Specify either CloudWatch Logs or Kinesis Data Firehose as the destination type. Valid values are either ``cloudwatch-logs`` or ``kinesis-firehose`` .
            :param log_format: Valid values are either ``json`` or ``text`` .
            :param log_type: Valid value is either ``slow-log`` , which refers to `slow-log <https://docs.aws.amazon.com/https://redis.io/commands/slowlog>`_ or ``engine-log`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                log_delivery_configuration_request_property = elasticache.CfnReplicationGroup.LogDeliveryConfigurationRequestProperty(
                    destination_details=elasticache.CfnReplicationGroup.DestinationDetailsProperty(
                        cloud_watch_logs_details=elasticache.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty(
                            log_group="logGroup"
                        ),
                        kinesis_firehose_details=elasticache.CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty(
                            delivery_stream="deliveryStream"
                        )
                    ),
                    destination_type="destinationType",
                    log_format="logFormat",
                    log_type="logType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9ff12d17e85eb513ea31c4f6d81c908ca6208f607b8673aa2d7c7e0a9fe4706)
                check_type(argname="argument destination_details", value=destination_details, expected_type=type_hints["destination_details"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
                check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
                check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_details": destination_details,
                "destination_type": destination_type,
                "log_format": log_format,
                "log_type": log_type,
            }

        @builtins.property
        def destination_details(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.DestinationDetailsProperty"]:
            '''Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationdetails
            '''
            result = self._values.get("destination_details")
            assert result is not None, "Required property 'destination_details' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnReplicationGroup.DestinationDetailsProperty"], result)

        @builtins.property
        def destination_type(self) -> builtins.str:
            '''Specify either CloudWatch Logs or Kinesis Data Firehose as the destination type.

            Valid values are either ``cloudwatch-logs`` or ``kinesis-firehose`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationtype
            '''
            result = self._values.get("destination_type")
            assert result is not None, "Required property 'destination_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_format(self) -> builtins.str:
            '''Valid values are either ``json`` or ``text`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logformat
            '''
            result = self._values.get("log_format")
            assert result is not None, "Required property 'log_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_type(self) -> builtins.str:
            '''Valid value is either ``slow-log`` , which refers to `slow-log <https://docs.aws.amazon.com/https://redis.io/commands/slowlog>`_ or ``engine-log`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logtype
            '''
            result = self._values.get("log_type")
            assert result is not None, "Required property 'log_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDeliveryConfigurationRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnReplicationGroup.NodeGroupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "node_group_id": "nodeGroupId",
            "primary_availability_zone": "primaryAvailabilityZone",
            "replica_availability_zones": "replicaAvailabilityZones",
            "replica_count": "replicaCount",
            "slots": "slots",
        },
    )
    class NodeGroupConfigurationProperty:
        def __init__(
            self,
            *,
            node_group_id: typing.Optional[builtins.str] = None,
            primary_availability_zone: typing.Optional[builtins.str] = None,
            replica_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
            replica_count: typing.Optional[jsii.Number] = None,
            slots: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``NodeGroupConfiguration`` is a property of the ``AWS::ElastiCache::ReplicationGroup`` resource that configures an Amazon ElastiCache (ElastiCache) Redis cluster node group.

            :param node_group_id: Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.
            :param primary_availability_zone: The Availability Zone where the primary node of this node group (shard) is launched.
            :param replica_availability_zones: A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.
            :param replica_count: The number of read replica nodes in this node group (shard).
            :param slots: A string of comma-separated values where the first set of values are the slot numbers (zero based), and the second set of values are the keyspaces for each slot. The following example specifies three slots (numbered 0, 1, and 2): ``0,1,2,0-4999,5000-9999,10000-16,383`` . If you don't specify a value, ElastiCache allocates keys equally among each slot. When you use an ``UseOnlineResharding`` update policy to update the number of node groups without interruption, ElastiCache evenly distributes the keyspaces between the specified number of slots. This cannot be updated later. Therefore, after updating the number of node groups in this way, you should remove the value specified for the ``Slots`` property of each ``NodeGroupConfiguration`` from the stack template, as it no longer reflects the actual values in each node group. For more information, see `UseOnlineResharding Policy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                node_group_configuration_property = elasticache.CfnReplicationGroup.NodeGroupConfigurationProperty(
                    node_group_id="nodeGroupId",
                    primary_availability_zone="primaryAvailabilityZone",
                    replica_availability_zones=["replicaAvailabilityZones"],
                    replica_count=123,
                    slots="slots"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b71a634ea38148f00c55a6a55d2a07c87ecfd6d6fbdd46f7603a23c08772dfb5)
                check_type(argname="argument node_group_id", value=node_group_id, expected_type=type_hints["node_group_id"])
                check_type(argname="argument primary_availability_zone", value=primary_availability_zone, expected_type=type_hints["primary_availability_zone"])
                check_type(argname="argument replica_availability_zones", value=replica_availability_zones, expected_type=type_hints["replica_availability_zones"])
                check_type(argname="argument replica_count", value=replica_count, expected_type=type_hints["replica_count"])
                check_type(argname="argument slots", value=slots, expected_type=type_hints["slots"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if node_group_id is not None:
                self._values["node_group_id"] = node_group_id
            if primary_availability_zone is not None:
                self._values["primary_availability_zone"] = primary_availability_zone
            if replica_availability_zones is not None:
                self._values["replica_availability_zones"] = replica_availability_zones
            if replica_count is not None:
                self._values["replica_count"] = replica_count
            if slots is not None:
                self._values["slots"] = slots

        @builtins.property
        def node_group_id(self) -> typing.Optional[builtins.str]:
            '''Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-nodegroupid
            '''
            result = self._values.get("node_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary_availability_zone(self) -> typing.Optional[builtins.str]:
            '''The Availability Zone where the primary node of this node group (shard) is launched.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-primaryavailabilityzone
            '''
            result = self._values.get("primary_availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replica_availability_zones(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of Availability Zones to be used for the read replicas.

            The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-replicaavailabilityzones
            '''
            result = self._values.get("replica_availability_zones")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def replica_count(self) -> typing.Optional[jsii.Number]:
            '''The number of read replica nodes in this node group (shard).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-replicacount
            '''
            result = self._values.get("replica_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def slots(self) -> typing.Optional[builtins.str]:
            '''A string of comma-separated values where the first set of values are the slot numbers (zero based), and the second set of values are the keyspaces for each slot.

            The following example specifies three slots (numbered 0, 1, and 2): ``0,1,2,0-4999,5000-9999,10000-16,383`` .

            If you don't specify a value, ElastiCache allocates keys equally among each slot.

            When you use an ``UseOnlineResharding`` update policy to update the number of node groups without interruption, ElastiCache evenly distributes the keyspaces between the specified number of slots. This cannot be updated later. Therefore, after updating the number of node groups in this way, you should remove the value specified for the ``Slots`` property of each ``NodeGroupConfiguration`` from the stack template, as it no longer reflects the actual values in each node group. For more information, see `UseOnlineResharding Policy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-slots
            '''
            result = self._values.get("slots")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeGroupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnReplicationGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "replication_group_description": "replicationGroupDescription",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "auth_token": "authToken",
        "automatic_failover_enabled": "automaticFailoverEnabled",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "cache_node_type": "cacheNodeType",
        "cache_parameter_group_name": "cacheParameterGroupName",
        "cache_security_group_names": "cacheSecurityGroupNames",
        "cache_subnet_group_name": "cacheSubnetGroupName",
        "cluster_mode": "clusterMode",
        "data_tiering_enabled": "dataTieringEnabled",
        "engine": "engine",
        "engine_version": "engineVersion",
        "global_replication_group_id": "globalReplicationGroupId",
        "ip_discovery": "ipDiscovery",
        "kms_key_id": "kmsKeyId",
        "log_delivery_configurations": "logDeliveryConfigurations",
        "multi_az_enabled": "multiAzEnabled",
        "network_type": "networkType",
        "node_group_configuration": "nodeGroupConfiguration",
        "notification_topic_arn": "notificationTopicArn",
        "num_cache_clusters": "numCacheClusters",
        "num_node_groups": "numNodeGroups",
        "port": "port",
        "preferred_cache_cluster_a_zs": "preferredCacheClusterAZs",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "primary_cluster_id": "primaryClusterId",
        "replicas_per_node_group": "replicasPerNodeGroup",
        "replication_group_id": "replicationGroupId",
        "security_group_ids": "securityGroupIds",
        "snapshot_arns": "snapshotArns",
        "snapshot_name": "snapshotName",
        "snapshot_retention_limit": "snapshotRetentionLimit",
        "snapshotting_cluster_id": "snapshottingClusterId",
        "snapshot_window": "snapshotWindow",
        "tags": "tags",
        "transit_encryption_enabled": "transitEncryptionEnabled",
        "transit_encryption_mode": "transitEncryptionMode",
        "user_group_ids": "userGroupIds",
    },
)
class CfnReplicationGroupProps:
    def __init__(
        self,
        *,
        replication_group_description: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cache_node_type: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_mode: typing.Optional[builtins.str] = None,
        data_tiering_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        global_replication_group_id: typing.Optional[builtins.str] = None,
        ip_discovery: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_delivery_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.LogDeliveryConfigurationRequestProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        multi_az_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        network_type: typing.Optional[builtins.str] = None,
        node_group_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.NodeGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        num_cache_clusters: typing.Optional[jsii.Number] = None,
        num_node_groups: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_cache_cluster_a_zs: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        primary_cluster_id: typing.Optional[builtins.str] = None,
        replicas_per_node_group: typing.Optional[jsii.Number] = None,
        replication_group_id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshotting_cluster_id: typing.Optional[builtins.str] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        transit_encryption_mode: typing.Optional[builtins.str] = None,
        user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationGroup``.

        :param replication_group_description: A user-created description for the replication group.
        :param at_rest_encryption_enabled: A flag that enables encryption at rest when set to ``true`` . You cannot modify the value of ``AtRestEncryptionEnabled`` after the replication group is created. To enable encryption at rest on a replication group you must set ``AtRestEncryptionEnabled`` to ``true`` when you create the replication group. *Required:* Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` onward. Default: ``false``
        :param auth_token: *Reserved parameter.* The password used to access a password protected server. ``AuthToken`` can be specified only on replication groups where ``TransitEncryptionEnabled`` is ``true`` . For more information, see `Authenticating Users with the Redis AUTH Command <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html>`_ . .. epigraph:: For HIPAA compliance, you must specify ``TransitEncryptionEnabled`` as ``true`` , an ``AuthToken`` , and a ``CacheSubnetGroup`` . Password constraints: - Must be only printable ASCII characters. - Must be at least 16 characters and no more than 128 characters in length. - Nonalphanumeric characters are restricted to (!, &, #, $, ^, <, >, -, ). For more information, see `AUTH password <https://docs.aws.amazon.com/http://redis.io/commands/AUTH>`_ at http://redis.io/commands/AUTH. .. epigraph:: If ADDING the AuthToken, update requires `Replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param automatic_failover_enabled: Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails. ``AutomaticFailoverEnabled`` must be enabled for Redis (cluster mode enabled) replication groups. Default: false
        :param auto_minor_version_upgrade: If you are running Redis engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.
        :param cache_node_type: The compute and memory capacity of the nodes in the node group (shard). The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts. - General purpose: - Current generation: *M6g node types:* ``cache.m6g.large`` , ``cache.m6g.xlarge`` , ``cache.m6g.2xlarge`` , ``cache.m6g.4xlarge`` , ``cache.m6g.12xlarge`` , ``cache.m6g.24xlarge`` *M5 node types:* ``cache.m5.large`` , ``cache.m5.xlarge`` , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge`` *M4 node types:* ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge`` *T4g node types:* ``cache.t4g.micro`` , ``cache.t4g.small`` , ``cache.t4g.medium`` *T3 node types:* ``cache.t3.micro`` , ``cache.t3.small`` , ``cache.t3.medium`` *T2 node types:* ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium`` - Previous generation: (not recommended) *T1 node types:* ``cache.t1.micro`` *M1 node types:* ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge`` *M3 node types:* ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge`` - Compute optimized: - Previous generation: (not recommended) *C1 node types:* ``cache.c1.xlarge`` - Memory optimized: - Current generation: *R6gd node types:* ``cache.r6gd.xlarge`` , ``cache.r6gd.2xlarge`` , ``cache.r6gd.4xlarge`` , ``cache.r6gd.8xlarge`` , ``cache.r6gd.12xlarge`` , ``cache.r6gd.16xlarge`` .. epigraph:: The ``r6gd`` family is available in the following regions: ``us-east-2`` , ``us-east-1`` , ``us-west-2`` , ``us-west-1`` , ``eu-west-1`` , ``eu-central-1`` , ``ap-northeast-1`` , ``ap-southeast-1`` , ``ap-southeast-2`` . *R6g node types:* ``cache.r6g.large`` , ``cache.r6g.xlarge`` , ``cache.r6g.2xlarge`` , ``cache.r6g.4xlarge`` , ``cache.r6g.12xlarge`` , ``cache.r6g.24xlarge`` *R5 node types:* ``cache.r5.large`` , ``cache.r5.xlarge`` , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge`` *R4 node types:* ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge`` - Previous generation: (not recommended) *M2 node types:* ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge`` *R3 node types:* ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge`` For region availability, see `Supported Node Types by Amazon Region <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion>`_
        :param cache_parameter_group_name: The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used. If you are running Redis version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name. - To create a Redis (cluster mode disabled) replication group, use ``CacheParameterGroupName=default.redis3.2`` . - To create a Redis (cluster mode enabled) replication group, use ``CacheParameterGroupName=default.redis3.2.cluster.on`` .
        :param cache_security_group_names: A list of cache security group names to associate with this replication group.
        :param cache_subnet_group_name: The name of the cache subnet group to be used for the replication group. .. epigraph:: If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see `AWS::ElastiCache::SubnetGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html>`_ .
        :param cluster_mode: Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Redis clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Redis clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled. For more information, see `Modify cluster mode <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/modify-cluster-mode.html>`_ .
        :param data_tiering_enabled: Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see `Data tiering <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/data-tiering.html>`_ .
        :param engine: The name of the cache engine to be used for the clusters in this replication group. The value must be set to ``Redis`` .
        :param engine_version: The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the ``DescribeCacheEngineVersions`` operation. *Important:* You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`_ ) in the *ElastiCache User Guide* , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.
        :param global_replication_group_id: The name of the Global datastore.
        :param ip_discovery: The network type you choose when creating a replication group, either ``ipv4`` | ``ipv6`` . IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .
        :param kms_key_id: The ID of the KMS key used to encrypt the disk on the cluster.
        :param log_delivery_configurations: Specifies the destination, format and type of the logs.
        :param multi_az_enabled: A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see `Minimizing Downtime: Multi-AZ <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/AutoFailover.html>`_ .
        :param network_type: Must be either ``ipv4`` | ``ipv6`` | ``dual_stack`` . IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .
        :param node_group_configuration: ``NodeGroupConfiguration`` is a property of the ``AWS::ElastiCache::ReplicationGroup`` resource that configures an Amazon ElastiCache (ElastiCache) Redis cluster node group. If you set `UseOnlineResharding <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding>`_ to ``true`` , you can update ``NodeGroupConfiguration`` without interruption. When ``UseOnlineResharding`` is set to ``false`` , or is not specified, updating ``NodeGroupConfiguration`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param notification_topic_arn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent. .. epigraph:: The Amazon SNS topic owner must be the same as the cluster owner.
        :param num_cache_clusters: The number of clusters this replication group initially has. This parameter is not used if there is more than one node group (shard). You should use ``ReplicasPerNodeGroup`` instead. If ``AutomaticFailoverEnabled`` is ``true`` , the value of this parameter must be at least 2. If ``AutomaticFailoverEnabled`` is ``false`` you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6. The maximum permitted value for ``NumCacheClusters`` is 6 (1 primary plus 5 replicas).
        :param num_node_groups: An optional parameter that specifies the number of node groups (shards) for this Redis (cluster mode enabled) replication group. For Redis (cluster mode disabled) either omit this parameter or set it to 1. If you set `UseOnlineResharding <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding>`_ to ``true`` , you can update ``NumNodeGroups`` without interruption. When ``UseOnlineResharding`` is set to ``false`` , or is not specified, updating ``NumNodeGroups`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ . Default: 1
        :param port: The port number on which each member of the replication group accepts connections.
        :param preferred_cache_cluster_a_zs: A list of EC2 Availability Zones in which the replication group's clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list. This parameter is not used if there is more than one node group (shard). You should use ``NodeGroupConfiguration`` instead. .. epigraph:: If you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of ``NumCacheClusters`` . Default: system chosen Availability Zones.
        :param preferred_maintenance_window: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ``ddd`` are: - ``sun`` - ``mon`` - ``tue`` - ``wed`` - ``thu`` - ``fri`` - ``sat`` Example: ``sun:23:00-mon:01:30``
        :param primary_cluster_id: The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of ``available`` . This parameter is not required if ``NumCacheClusters`` , ``NumNodeGroups`` , or ``ReplicasPerNodeGroup`` is specified.
        :param replicas_per_node_group: An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.
        :param replication_group_id: 
        :param security_group_ids: One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).
        :param snapshot_arns: A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter *NumNodeGroups* or the number of node groups configured by *NodeGroupConfiguration* regardless of the number of ARNs specified here. Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``
        :param snapshot_name: The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to ``restoring`` while the new replication group is being created.
        :param snapshot_retention_limit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted. Default: 0 (i.e., automatic backups are disabled for this cluster).
        :param snapshotting_cluster_id: The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Redis (cluster mode enabled) replication groups.
        :param snapshot_window: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard). Example: ``05:00-09:00`` If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
        :param tags: A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key= ``myKey`` , Value= ``myKeyValue`` . You can include multiple tags as shown following: Key= ``myKey`` , Value= ``myKeyValue`` Key= ``mySecondKey`` , Value= ``mySecondKeyValue`` . Tags on replication groups will be replicated to all nodes.
        :param transit_encryption_enabled: A flag that enables in-transit encryption when set to ``true`` . You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster. This parameter is valid only if the ``Engine`` parameter is ``redis`` , the ``EngineVersion`` parameter is ``3.2.6`` or ``4.x`` onward, and the cluster is being created in an Amazon VPC. If you enable in-transit encryption, you must also specify a value for ``CacheSubnetGroup`` . *Required:* Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` onward. Default: ``false`` .. epigraph:: For HIPAA compliance, you must specify ``TransitEncryptionEnabled`` as ``true`` , an ``AuthToken`` , and a ``CacheSubnetGroup`` .
        :param transit_encryption_mode: A setting that allows you to migrate your clients to use in-transit encryption, with no downtime. When setting ``TransitEncryptionEnabled`` to ``true`` , you can set your ``TransitEncryptionMode`` to ``preferred`` in the same request, to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Redis clients to use encrypted connections you can modify the value to ``required`` to allow encrypted connections only. Setting ``TransitEncryptionMode`` to ``required`` is a two-step process that requires you to first set the ``TransitEncryptionMode`` to ``preferred`` , after that you can set ``TransitEncryptionMode`` to ``required`` . This process will not trigger the replacement of the replication group.
        :param user_group_ids: The ID of user group to associate with the replication group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_replication_group_props = elasticache.CfnReplicationGroupProps(
                replication_group_description="replicationGroupDescription",
            
                # the properties below are optional
                at_rest_encryption_enabled=False,
                auth_token="authToken",
                automatic_failover_enabled=False,
                auto_minor_version_upgrade=False,
                cache_node_type="cacheNodeType",
                cache_parameter_group_name="cacheParameterGroupName",
                cache_security_group_names=["cacheSecurityGroupNames"],
                cache_subnet_group_name="cacheSubnetGroupName",
                cluster_mode="clusterMode",
                data_tiering_enabled=False,
                engine="engine",
                engine_version="engineVersion",
                global_replication_group_id="globalReplicationGroupId",
                ip_discovery="ipDiscovery",
                kms_key_id="kmsKeyId",
                log_delivery_configurations=[elasticache.CfnReplicationGroup.LogDeliveryConfigurationRequestProperty(
                    destination_details=elasticache.CfnReplicationGroup.DestinationDetailsProperty(
                        cloud_watch_logs_details=elasticache.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty(
                            log_group="logGroup"
                        ),
                        kinesis_firehose_details=elasticache.CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty(
                            delivery_stream="deliveryStream"
                        )
                    ),
                    destination_type="destinationType",
                    log_format="logFormat",
                    log_type="logType"
                )],
                multi_az_enabled=False,
                network_type="networkType",
                node_group_configuration=[elasticache.CfnReplicationGroup.NodeGroupConfigurationProperty(
                    node_group_id="nodeGroupId",
                    primary_availability_zone="primaryAvailabilityZone",
                    replica_availability_zones=["replicaAvailabilityZones"],
                    replica_count=123,
                    slots="slots"
                )],
                notification_topic_arn="notificationTopicArn",
                num_cache_clusters=123,
                num_node_groups=123,
                port=123,
                preferred_cache_cluster_aZs=["preferredCacheClusterAZs"],
                preferred_maintenance_window="preferredMaintenanceWindow",
                primary_cluster_id="primaryClusterId",
                replicas_per_node_group=123,
                replication_group_id="replicationGroupId",
                security_group_ids=["securityGroupIds"],
                snapshot_arns=["snapshotArns"],
                snapshot_name="snapshotName",
                snapshot_retention_limit=123,
                snapshotting_cluster_id="snapshottingClusterId",
                snapshot_window="snapshotWindow",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                transit_encryption_enabled=False,
                transit_encryption_mode="transitEncryptionMode",
                user_group_ids=["userGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8dbf3d422d5fea6e04cfbc10e81904d384dc2c210952911caaa5ab7eefa3a3d)
            check_type(argname="argument replication_group_description", value=replication_group_description, expected_type=type_hints["replication_group_description"])
            check_type(argname="argument at_rest_encryption_enabled", value=at_rest_encryption_enabled, expected_type=type_hints["at_rest_encryption_enabled"])
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument automatic_failover_enabled", value=automatic_failover_enabled, expected_type=type_hints["automatic_failover_enabled"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument cache_node_type", value=cache_node_type, expected_type=type_hints["cache_node_type"])
            check_type(argname="argument cache_parameter_group_name", value=cache_parameter_group_name, expected_type=type_hints["cache_parameter_group_name"])
            check_type(argname="argument cache_security_group_names", value=cache_security_group_names, expected_type=type_hints["cache_security_group_names"])
            check_type(argname="argument cache_subnet_group_name", value=cache_subnet_group_name, expected_type=type_hints["cache_subnet_group_name"])
            check_type(argname="argument cluster_mode", value=cluster_mode, expected_type=type_hints["cluster_mode"])
            check_type(argname="argument data_tiering_enabled", value=data_tiering_enabled, expected_type=type_hints["data_tiering_enabled"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument global_replication_group_id", value=global_replication_group_id, expected_type=type_hints["global_replication_group_id"])
            check_type(argname="argument ip_discovery", value=ip_discovery, expected_type=type_hints["ip_discovery"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_delivery_configurations", value=log_delivery_configurations, expected_type=type_hints["log_delivery_configurations"])
            check_type(argname="argument multi_az_enabled", value=multi_az_enabled, expected_type=type_hints["multi_az_enabled"])
            check_type(argname="argument network_type", value=network_type, expected_type=type_hints["network_type"])
            check_type(argname="argument node_group_configuration", value=node_group_configuration, expected_type=type_hints["node_group_configuration"])
            check_type(argname="argument notification_topic_arn", value=notification_topic_arn, expected_type=type_hints["notification_topic_arn"])
            check_type(argname="argument num_cache_clusters", value=num_cache_clusters, expected_type=type_hints["num_cache_clusters"])
            check_type(argname="argument num_node_groups", value=num_node_groups, expected_type=type_hints["num_node_groups"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_cache_cluster_a_zs", value=preferred_cache_cluster_a_zs, expected_type=type_hints["preferred_cache_cluster_a_zs"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument primary_cluster_id", value=primary_cluster_id, expected_type=type_hints["primary_cluster_id"])
            check_type(argname="argument replicas_per_node_group", value=replicas_per_node_group, expected_type=type_hints["replicas_per_node_group"])
            check_type(argname="argument replication_group_id", value=replication_group_id, expected_type=type_hints["replication_group_id"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument snapshot_arns", value=snapshot_arns, expected_type=type_hints["snapshot_arns"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument snapshot_retention_limit", value=snapshot_retention_limit, expected_type=type_hints["snapshot_retention_limit"])
            check_type(argname="argument snapshotting_cluster_id", value=snapshotting_cluster_id, expected_type=type_hints["snapshotting_cluster_id"])
            check_type(argname="argument snapshot_window", value=snapshot_window, expected_type=type_hints["snapshot_window"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transit_encryption_enabled", value=transit_encryption_enabled, expected_type=type_hints["transit_encryption_enabled"])
            check_type(argname="argument transit_encryption_mode", value=transit_encryption_mode, expected_type=type_hints["transit_encryption_mode"])
            check_type(argname="argument user_group_ids", value=user_group_ids, expected_type=type_hints["user_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_group_description": replication_group_description,
        }
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if auth_token is not None:
            self._values["auth_token"] = auth_token
        if automatic_failover_enabled is not None:
            self._values["automatic_failover_enabled"] = automatic_failover_enabled
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if cache_node_type is not None:
            self._values["cache_node_type"] = cache_node_type
        if cache_parameter_group_name is not None:
            self._values["cache_parameter_group_name"] = cache_parameter_group_name
        if cache_security_group_names is not None:
            self._values["cache_security_group_names"] = cache_security_group_names
        if cache_subnet_group_name is not None:
            self._values["cache_subnet_group_name"] = cache_subnet_group_name
        if cluster_mode is not None:
            self._values["cluster_mode"] = cluster_mode
        if data_tiering_enabled is not None:
            self._values["data_tiering_enabled"] = data_tiering_enabled
        if engine is not None:
            self._values["engine"] = engine
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if global_replication_group_id is not None:
            self._values["global_replication_group_id"] = global_replication_group_id
        if ip_discovery is not None:
            self._values["ip_discovery"] = ip_discovery
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_delivery_configurations is not None:
            self._values["log_delivery_configurations"] = log_delivery_configurations
        if multi_az_enabled is not None:
            self._values["multi_az_enabled"] = multi_az_enabled
        if network_type is not None:
            self._values["network_type"] = network_type
        if node_group_configuration is not None:
            self._values["node_group_configuration"] = node_group_configuration
        if notification_topic_arn is not None:
            self._values["notification_topic_arn"] = notification_topic_arn
        if num_cache_clusters is not None:
            self._values["num_cache_clusters"] = num_cache_clusters
        if num_node_groups is not None:
            self._values["num_node_groups"] = num_node_groups
        if port is not None:
            self._values["port"] = port
        if preferred_cache_cluster_a_zs is not None:
            self._values["preferred_cache_cluster_a_zs"] = preferred_cache_cluster_a_zs
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if primary_cluster_id is not None:
            self._values["primary_cluster_id"] = primary_cluster_id
        if replicas_per_node_group is not None:
            self._values["replicas_per_node_group"] = replicas_per_node_group
        if replication_group_id is not None:
            self._values["replication_group_id"] = replication_group_id
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if snapshot_arns is not None:
            self._values["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if snapshot_retention_limit is not None:
            self._values["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshotting_cluster_id is not None:
            self._values["snapshotting_cluster_id"] = snapshotting_cluster_id
        if snapshot_window is not None:
            self._values["snapshot_window"] = snapshot_window
        if tags is not None:
            self._values["tags"] = tags
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled
        if transit_encryption_mode is not None:
            self._values["transit_encryption_mode"] = transit_encryption_mode
        if user_group_ids is not None:
            self._values["user_group_ids"] = user_group_ids

    @builtins.property
    def replication_group_description(self) -> builtins.str:
        '''A user-created description for the replication group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicationgroupdescription
        '''
        result = self._values.get("replication_group_description")
        assert result is not None, "Required property 'replication_group_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag that enables encryption at rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the replication group is created. To enable encryption at rest on a replication group you must set ``AtRestEncryptionEnabled`` to ``true`` when you create the replication group.

        *Required:* Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` onward.

        Default: ``false``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-atrestencryptionenabled
        '''
        result = self._values.get("at_rest_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def auth_token(self) -> typing.Optional[builtins.str]:
        '''*Reserved parameter.* The password used to access a password protected server.

        ``AuthToken`` can be specified only on replication groups where ``TransitEncryptionEnabled`` is ``true`` . For more information, see `Authenticating Users with the Redis AUTH Command <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html>`_ .
        .. epigraph::

           For HIPAA compliance, you must specify ``TransitEncryptionEnabled`` as ``true`` , an ``AuthToken`` , and a ``CacheSubnetGroup`` .

        Password constraints:

        - Must be only printable ASCII characters.
        - Must be at least 16 characters and no more than 128 characters in length.
        - Nonalphanumeric characters are restricted to (!, &, #, $, ^, <, >, -, ).

        For more information, see `AUTH password <https://docs.aws.amazon.com/http://redis.io/commands/AUTH>`_ at http://redis.io/commands/AUTH.
        .. epigraph::

           If ADDING the AuthToken, update requires `Replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-authtoken
        '''
        result = self._values.get("auth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.

        ``AutomaticFailoverEnabled`` must be enabled for Redis (cluster mode enabled) replication groups.

        Default: false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-automaticfailoverenabled
        '''
        result = self._values.get("automatic_failover_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you are running Redis engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def cache_node_type(self) -> typing.Optional[builtins.str]:
        '''The compute and memory capacity of the nodes in the node group (shard).

        The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

        - General purpose:
        - Current generation:

        *M6g node types:* ``cache.m6g.large`` , ``cache.m6g.xlarge`` , ``cache.m6g.2xlarge`` , ``cache.m6g.4xlarge`` , ``cache.m6g.12xlarge`` , ``cache.m6g.24xlarge``

        *M5 node types:* ``cache.m5.large`` , ``cache.m5.xlarge`` , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` , ``cache.m5.24xlarge``

        *M4 node types:* ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``

        *T4g node types:* ``cache.t4g.micro`` , ``cache.t4g.small`` , ``cache.t4g.medium``

        *T3 node types:* ``cache.t3.micro`` , ``cache.t3.small`` , ``cache.t3.medium``

        *T2 node types:* ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        - Previous generation: (not recommended)

        *T1 node types:* ``cache.t1.micro``

        *M1 node types:* ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``

        *M3 node types:* ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        - Compute optimized:
        - Previous generation: (not recommended)

        *C1 node types:* ``cache.c1.xlarge``

        - Memory optimized:
        - Current generation:

        *R6gd node types:* ``cache.r6gd.xlarge`` , ``cache.r6gd.2xlarge`` , ``cache.r6gd.4xlarge`` , ``cache.r6gd.8xlarge`` , ``cache.r6gd.12xlarge`` , ``cache.r6gd.16xlarge``
        .. epigraph::

           The ``r6gd`` family is available in the following regions: ``us-east-2`` , ``us-east-1`` , ``us-west-2`` , ``us-west-1`` , ``eu-west-1`` , ``eu-central-1`` , ``ap-northeast-1`` , ``ap-southeast-1`` , ``ap-southeast-2`` .

        *R6g node types:* ``cache.r6g.large`` , ``cache.r6g.xlarge`` , ``cache.r6g.2xlarge`` , ``cache.r6g.4xlarge`` , ``cache.r6g.12xlarge`` , ``cache.r6g.24xlarge``

        *R5 node types:* ``cache.r5.large`` , ``cache.r5.xlarge`` , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` , ``cache.r5.24xlarge``

        *R4 node types:* ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        - Previous generation: (not recommended)

        *M2 node types:* ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``

        *R3 node types:* ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

        For region availability, see `Supported Node Types by Amazon Region <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachenodetype
        '''
        result = self._values.get("cache_node_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group to associate with this replication group.

        If this argument is omitted, the default cache parameter group for the specified engine is used.

        If you are running Redis version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name.

        - To create a Redis (cluster mode disabled) replication group, use ``CacheParameterGroupName=default.redis3.2`` .
        - To create a Redis (cluster mode enabled) replication group, use ``CacheParameterGroupName=default.redis3.2.cluster.on`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cacheparametergroupname
        '''
        result = self._values.get("cache_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of cache security group names to associate with this replication group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachesecuritygroupnames
        '''
        result = self._values.get("cache_security_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cache subnet group to be used for the replication group.

        .. epigraph::

           If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see `AWS::ElastiCache::SubnetGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachesubnetgroupname
        '''
        result = self._values.get("cache_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_mode(self) -> typing.Optional[builtins.str]:
        '''Enabled or Disabled.

        To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Redis clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Redis clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled. For more information, see `Modify cluster mode <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/modify-cluster-mode.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-clustermode
        '''
        result = self._values.get("cluster_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_tiering_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables data tiering.

        Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see `Data tiering <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/data-tiering.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-datatieringenabled
        '''
        result = self._values.get("data_tiering_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''The name of the cache engine to be used for the clusters in this replication group.

        The value must be set to ``Redis`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-engine
        '''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version number of the cache engine to be used for the clusters in this replication group.

        To view the supported cache engine versions, use the ``DescribeCacheEngineVersions`` operation.

        *Important:* You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html#VersionManagement>`_ ) in the *ElastiCache User Guide* , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_replication_group_id(self) -> typing.Optional[builtins.str]:
        '''The name of the Global datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-globalreplicationgroupid
        '''
        result = self._values.get("global_replication_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_discovery(self) -> typing.Optional[builtins.str]:
        '''The network type you choose when creating a replication group, either ``ipv4`` | ``ipv6`` .

        IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-ipdiscovery
        '''
        result = self._values.get("ip_discovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key used to encrypt the disk on the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnReplicationGroup.LogDeliveryConfigurationRequestProperty]]]]:
        '''Specifies the destination, format and type of the logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-logdeliveryconfigurations
        '''
        result = self._values.get("log_delivery_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnReplicationGroup.LogDeliveryConfigurationRequestProperty]]]], result)

    @builtins.property
    def multi_az_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag indicating if you have Multi-AZ enabled to enhance fault tolerance.

        For more information, see `Minimizing Downtime: Multi-AZ <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/AutoFailover.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-multiazenabled
        '''
        result = self._values.get("multi_az_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def network_type(self) -> typing.Optional[builtins.str]:
        '''Must be either ``ipv4`` | ``ipv6`` | ``dual_stack`` .

        IPv6 is supported for workloads using Redis engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the `Nitro system <https://docs.aws.amazon.com/ec2/nitro/>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-networktype
        '''
        result = self._values.get("network_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnReplicationGroup.NodeGroupConfigurationProperty]]]]:
        '''``NodeGroupConfiguration`` is a property of the ``AWS::ElastiCache::ReplicationGroup`` resource that configures an Amazon ElastiCache (ElastiCache) Redis cluster node group.

        If you set `UseOnlineResharding <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding>`_ to ``true`` , you can update ``NodeGroupConfiguration`` without interruption. When ``UseOnlineResharding`` is set to ``false`` , or is not specified, updating ``NodeGroupConfiguration`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-nodegroupconfiguration
        '''
        result = self._values.get("node_group_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnReplicationGroup.NodeGroupConfigurationProperty]]]], result)

    @builtins.property
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.

        .. epigraph::

           The Amazon SNS topic owner must be the same as the cluster owner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-notificationtopicarn
        '''
        result = self._values.get("notification_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_cache_clusters(self) -> typing.Optional[jsii.Number]:
        '''The number of clusters this replication group initially has.

        This parameter is not used if there is more than one node group (shard). You should use ``ReplicasPerNodeGroup`` instead.

        If ``AutomaticFailoverEnabled`` is ``true`` , the value of this parameter must be at least 2. If ``AutomaticFailoverEnabled`` is ``false`` you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6.

        The maximum permitted value for ``NumCacheClusters`` is 6 (1 primary plus 5 replicas).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-numcacheclusters
        '''
        result = self._values.get("num_cache_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_node_groups(self) -> typing.Optional[jsii.Number]:
        '''An optional parameter that specifies the number of node groups (shards) for this Redis (cluster mode enabled) replication group.

        For Redis (cluster mode disabled) either omit this parameter or set it to 1.

        If you set `UseOnlineResharding <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding>`_ to ``true`` , you can update ``NumNodeGroups`` without interruption. When ``UseOnlineResharding`` is set to ``false`` , or is not specified, updating ``NumNodeGroups`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .

        Default: 1

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-numnodegroups
        '''
        result = self._values.get("num_node_groups")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number on which each member of the replication group accepts connections.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_cache_cluster_a_zs(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of EC2 Availability Zones in which the replication group's clusters are created.

        The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.

        This parameter is not used if there is more than one node group (shard). You should use ``NodeGroupConfiguration`` instead.
        .. epigraph::

           If you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group.

           The number of Availability Zones listed must equal the value of ``NumCacheClusters`` .

        Default: system chosen Availability Zones.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-preferredcacheclusterazs
        '''
        result = self._values.get("preferred_cache_cluster_a_zs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which maintenance on the cluster is performed.

        It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        - ``sun``
        - ``mon``
        - ``tue``
        - ``wed``
        - ``thu``
        - ``fri``
        - ``sat``

        Example: ``sun:23:00-mon:01:30``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_cluster_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the cluster that serves as the primary for this replication group.

        This cluster must already exist and have a status of ``available`` .

        This parameter is not required if ``NumCacheClusters`` , ``NumNodeGroups`` , or ``ReplicasPerNodeGroup`` is specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-primaryclusterid
        '''
        result = self._values.get("primary_cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replicas_per_node_group(self) -> typing.Optional[jsii.Number]:
        '''An optional parameter that specifies the number of replica nodes in each node group (shard).

        Valid values are 0 to 5.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicaspernodegroup
        '''
        result = self._values.get("replicas_per_node_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replication_group_id(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicationgroupid
        '''
        result = self._values.get("replication_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more Amazon VPC security groups associated with this replication group.

        Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored in Amazon S3.

        The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter *NumNodeGroups* or the number of node groups configured by *NodeGroupConfiguration* regardless of the number of ARNs specified here.

        Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotarns
        '''
        result = self._values.get("snapshot_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of a snapshot from which to restore data into the new replication group.

        The snapshot status changes to ``restoring`` while the new replication group is being created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotname
        '''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which ElastiCache retains automatic snapshots before deleting them.

        For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

        Default: 0 (i.e., automatic backups are disabled for this cluster).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotretentionlimit
        '''
        result = self._values.get("snapshot_retention_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshotting_cluster_id(self) -> typing.Optional[builtins.str]:
        '''The cluster ID that is used as the daily snapshot source for the replication group.

        This parameter cannot be set for Redis (cluster mode enabled) replication groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshottingclusterid
        '''
        result = self._values.get("snapshotting_cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotwindow
        '''
        result = self._values.get("snapshot_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be added to this resource.

        Tags are comma-separated key,value pairs (e.g. Key= ``myKey`` , Value= ``myKeyValue`` . You can include multiple tags as shown following: Key= ``myKey`` , Value= ``myKeyValue`` Key= ``mySecondKey`` , Value= ``mySecondKeyValue`` . Tags on replication groups will be replicated to all nodes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

        This parameter is valid only if the ``Engine`` parameter is ``redis`` , the ``EngineVersion`` parameter is ``3.2.6`` or ``4.x`` onward, and the cluster is being created in an Amazon VPC.

        If you enable in-transit encryption, you must also specify a value for ``CacheSubnetGroup`` .

        *Required:* Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` onward.

        Default: ``false``
        .. epigraph::

           For HIPAA compliance, you must specify ``TransitEncryptionEnabled`` as ``true`` , an ``AuthToken`` , and a ``CacheSubnetGroup`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-transitencryptionenabled
        '''
        result = self._values.get("transit_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def transit_encryption_mode(self) -> typing.Optional[builtins.str]:
        '''A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.

        When setting ``TransitEncryptionEnabled`` to ``true`` , you can set your ``TransitEncryptionMode`` to ``preferred`` in the same request, to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Redis clients to use encrypted connections you can modify the value to ``required`` to allow encrypted connections only.

        Setting ``TransitEncryptionMode`` to ``required`` is a two-step process that requires you to first set the ``TransitEncryptionMode`` to ``preferred`` , after that you can set ``TransitEncryptionMode`` to ``required`` .

        This process will not trigger the replacement of the replication group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-transitencryptionmode
        '''
        result = self._values.get("transit_encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ID of user group to associate with the replication group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-usergroupids
        '''
        result = self._values.get("user_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSecurityGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnSecurityGroup",
):
    '''The ``AWS::ElastiCache::SecurityGroup`` resource creates a cache security group.

    For more information about cache security groups, go to `CacheSecurityGroups <https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/VPCs.html>`_ in the *Amazon ElastiCache User Guide* or go to `CreateCacheSecurityGroup <https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSecurityGroup.html>`_ in the *Amazon ElastiCache API Reference Guide* .

    For more information, see `CreateCacheSubnetGroup <https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSubnetGroup.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroup.html
    :cloudformationResource: AWS::ElastiCache::SecurityGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_security_group = elasticache.CfnSecurityGroup(self, "MyCfnSecurityGroup",
            description="description",
        
            # the properties below are optional
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
        description: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description for the cache security group.
        :param tags: A tag that can be added to an ElastiCache security group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your security groups. A tag with a null Value is permitted.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a123177a3bb81237f7f7f549a05ee3a5234df818c52d76546ff68a80c39ddaed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityGroupProps(description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e59b6770093fdec8763d8d7b39b7d6466bc5e469d75d9f211e118781440edec1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2eb62adc1dfae487cca927c94c6b4ad1904c89719a572bef2994345a5d039ef0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description for the cache security group.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a58aa3e47b676ffbd43668bc6e1d2c79b30df11d4e23ee80c4bdefdb1e2e460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A tag that can be added to an ElastiCache security group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d0db95241a79cc90ce9ac36752f3ee20a66c04797f992822d1387e95ab0d3dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.implements(_IInspectable_c2943556)
class CfnSecurityGroupIngress(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnSecurityGroupIngress",
):
    '''The AWS::ElastiCache::SecurityGroupIngress type authorizes ingress to a cache security group from hosts in specified Amazon EC2 security groups.

    For more information about ElastiCache security group ingress, go to `AuthorizeCacheSecurityGroupIngress <https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_AuthorizeCacheSecurityGroupIngress.html>`_ in the *Amazon ElastiCache API Reference Guide* .
    .. epigraph::

       Updates are not supported.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroupingress.html
    :cloudformationResource: AWS::ElastiCache::SecurityGroupIngress
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_security_group_ingress = elasticache.CfnSecurityGroupIngress(self, "MyCfnSecurityGroupIngress",
            cache_security_group_name="cacheSecurityGroupName",
            ec2_security_group_name="ec2SecurityGroupName",
        
            # the properties below are optional
            ec2_security_group_owner_id="ec2SecurityGroupOwnerId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cache_security_group_name: builtins.str,
        ec2_security_group_name: builtins.str,
        ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cache_security_group_name: The name of the Cache Security Group to authorize.
        :param ec2_security_group_name: Name of the EC2 Security Group to include in the authorization.
        :param ec2_security_group_owner_id: Specifies the Amazon Account ID of the owner of the EC2 security group specified in the EC2SecurityGroupName property. The Amazon access key ID is not an acceptable value.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9fec253fa52a5ea3d4371f10b9ad50ca4993c9f60ac895b0fef6575e1ced177)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityGroupIngressProps(
            cache_security_group_name=cache_security_group_name,
            ec2_security_group_name=ec2_security_group_name,
            ec2_security_group_owner_id=ec2_security_group_owner_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce56443f7fa86a2c85da65d4fe1945a48bacd9a42111d28731fb9be03ebd3098)
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
            type_hints = typing.get_type_hints(_typecheckingstub__69468cc5d27117dacd7aa3deb279d35fa03dabbd826bb6290d084f5b9f359705)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cacheSecurityGroupName")
    def cache_security_group_name(self) -> builtins.str:
        '''The name of the Cache Security Group to authorize.'''
        return typing.cast(builtins.str, jsii.get(self, "cacheSecurityGroupName"))

    @cache_security_group_name.setter
    def cache_security_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__439c20ee90e3a27653353314240f9637cdf95b53b1cd23e4aaec9d21b5d568c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheSecurityGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="ec2SecurityGroupName")
    def ec2_security_group_name(self) -> builtins.str:
        '''Name of the EC2 Security Group to include in the authorization.'''
        return typing.cast(builtins.str, jsii.get(self, "ec2SecurityGroupName"))

    @ec2_security_group_name.setter
    def ec2_security_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0abb1fc13eea94e08b452064202975643af441a003c80b20a2dd84ee151b33ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2SecurityGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="ec2SecurityGroupOwnerId")
    def ec2_security_group_owner_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Account ID of the owner of the EC2 security group specified in the EC2SecurityGroupName property.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2SecurityGroupOwnerId"))

    @ec2_security_group_owner_id.setter
    def ec2_security_group_owner_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d69c9ced7a396b23c621165b2be40f28744ce4080f376459c1fec4f135a9d8a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2SecurityGroupOwnerId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnSecurityGroupIngressProps",
    jsii_struct_bases=[],
    name_mapping={
        "cache_security_group_name": "cacheSecurityGroupName",
        "ec2_security_group_name": "ec2SecurityGroupName",
        "ec2_security_group_owner_id": "ec2SecurityGroupOwnerId",
    },
)
class CfnSecurityGroupIngressProps:
    def __init__(
        self,
        *,
        cache_security_group_name: builtins.str,
        ec2_security_group_name: builtins.str,
        ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityGroupIngress``.

        :param cache_security_group_name: The name of the Cache Security Group to authorize.
        :param ec2_security_group_name: Name of the EC2 Security Group to include in the authorization.
        :param ec2_security_group_owner_id: Specifies the Amazon Account ID of the owner of the EC2 security group specified in the EC2SecurityGroupName property. The Amazon access key ID is not an acceptable value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroupingress.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_security_group_ingress_props = elasticache.CfnSecurityGroupIngressProps(
                cache_security_group_name="cacheSecurityGroupName",
                ec2_security_group_name="ec2SecurityGroupName",
            
                # the properties below are optional
                ec2_security_group_owner_id="ec2SecurityGroupOwnerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbdf58872e9544b14b7cd19f9a883c3e1c2fcad8d855805f476f813cea0882e6)
            check_type(argname="argument cache_security_group_name", value=cache_security_group_name, expected_type=type_hints["cache_security_group_name"])
            check_type(argname="argument ec2_security_group_name", value=ec2_security_group_name, expected_type=type_hints["ec2_security_group_name"])
            check_type(argname="argument ec2_security_group_owner_id", value=ec2_security_group_owner_id, expected_type=type_hints["ec2_security_group_owner_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cache_security_group_name": cache_security_group_name,
            "ec2_security_group_name": ec2_security_group_name,
        }
        if ec2_security_group_owner_id is not None:
            self._values["ec2_security_group_owner_id"] = ec2_security_group_owner_id

    @builtins.property
    def cache_security_group_name(self) -> builtins.str:
        '''The name of the Cache Security Group to authorize.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroupingress.html#cfn-elasticache-securitygroupingress-cachesecuritygroupname
        '''
        result = self._values.get("cache_security_group_name")
        assert result is not None, "Required property 'cache_security_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ec2_security_group_name(self) -> builtins.str:
        '''Name of the EC2 Security Group to include in the authorization.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroupingress.html#cfn-elasticache-securitygroupingress-ec2securitygroupname
        '''
        result = self._values.get("ec2_security_group_name")
        assert result is not None, "Required property 'ec2_security_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ec2_security_group_owner_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Account ID of the owner of the EC2 security group specified in the EC2SecurityGroupName property.

        The Amazon access key ID is not an acceptable value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroupingress.html#cfn-elasticache-securitygroupingress-ec2securitygroupownerid
        '''
        result = self._values.get("ec2_security_group_owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityGroupIngressProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnSecurityGroupProps",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "tags": "tags"},
)
class CfnSecurityGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityGroup``.

        :param description: A description for the cache security group.
        :param tags: A tag that can be added to an ElastiCache security group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your security groups. A tag with a null Value is permitted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_security_group_props = elasticache.CfnSecurityGroupProps(
                description="description",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__188ce8daf68355e05c89377b875f68542bb67a42ce5afc30df7473e1420abce9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''A description for the cache security group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroup.html#cfn-elasticache-securitygroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A tag that can be added to an ElastiCache security group.

        Tags are composed of a Key/Value pair. You can use tags to categorize and track all your security groups. A tag with a null Value is permitted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-securitygroup.html#cfn-elasticache-securitygroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnServerlessCache(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnServerlessCache",
):
    '''The resource representing a serverless cache.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html
    :cloudformationResource: AWS::ElastiCache::ServerlessCache
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_serverless_cache = elasticache.CfnServerlessCache(self, "MyCfnServerlessCache",
            engine="engine",
            serverless_cache_name="serverlessCacheName",
        
            # the properties below are optional
            cache_usage_limits=elasticache.CfnServerlessCache.CacheUsageLimitsProperty(
                data_storage=elasticache.CfnServerlessCache.DataStorageProperty(
                    unit="unit",
        
                    # the properties below are optional
                    maximum=123,
                    minimum=123
                ),
                ecpu_per_second=elasticache.CfnServerlessCache.ECPUPerSecondProperty(
                    maximum=123,
                    minimum=123
                )
            ),
            daily_snapshot_time="dailySnapshotTime",
            description="description",
            endpoint=elasticache.CfnServerlessCache.EndpointProperty(
                address="address",
                port="port"
            ),
            final_snapshot_name="finalSnapshotName",
            kms_key_id="kmsKeyId",
            major_engine_version="majorEngineVersion",
            reader_endpoint=elasticache.CfnServerlessCache.EndpointProperty(
                address="address",
                port="port"
            ),
            security_group_ids=["securityGroupIds"],
            snapshot_arns_to_restore=["snapshotArnsToRestore"],
            snapshot_retention_limit=123,
            subnet_ids=["subnetIds"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_group_id="userGroupId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        engine: builtins.str,
        serverless_cache_name: builtins.str,
        cache_usage_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCache.CacheUsageLimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        daily_snapshot_time: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCache.EndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        major_engine_version: typing.Optional[builtins.str] = None,
        reader_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCache.EndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns_to_restore: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param engine: The engine the serverless cache is compatible with.
        :param serverless_cache_name: The unique identifier of the serverless cache.
        :param cache_usage_limits: The cache usage limit for the serverless cache.
        :param daily_snapshot_time: The daily time that a cache snapshot will be created. Default is NULL, i.e. snapshots will not be created at a specific time on a daily basis. Available for Redis only.
        :param description: A description of the serverless cache.
        :param endpoint: Represents the information required for client programs to connect to a cache node. This value is read-only.
        :param final_snapshot_name: The name of the final snapshot taken of a cache before the cache is deleted.
        :param kms_key_id: The ID of the AWS Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.
        :param major_engine_version: The version number of the engine the serverless cache is compatible with.
        :param reader_endpoint: Represents the information required for client programs to connect to a cache node. This value is read-only.
        :param security_group_ids: The IDs of the EC2 security groups associated with the serverless cache.
        :param snapshot_arns_to_restore: The ARN of the snapshot from which to restore data into the new cache.
        :param snapshot_retention_limit: The current setting for the number of serverless cache snapshots the system will retain. Available for Redis only.
        :param subnet_ids: If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC. For all other Regions, if no subnet IDs are given then ElastiCache will select 3 default subnets across AZs in your default VPC.
        :param tags: A list of tags to be added to this resource.
        :param user_group_id: The identifier of the user group associated with the serverless cache. Available for Redis only. Default is NULL.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f204522453489e8198605933b3b942062e9c202c1099285663a7d772a3e94ba7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServerlessCacheProps(
            engine=engine,
            serverless_cache_name=serverless_cache_name,
            cache_usage_limits=cache_usage_limits,
            daily_snapshot_time=daily_snapshot_time,
            description=description,
            endpoint=endpoint,
            final_snapshot_name=final_snapshot_name,
            kms_key_id=kms_key_id,
            major_engine_version=major_engine_version,
            reader_endpoint=reader_endpoint,
            security_group_ids=security_group_ids,
            snapshot_arns_to_restore=snapshot_arns_to_restore,
            snapshot_retention_limit=snapshot_retention_limit,
            subnet_ids=subnet_ids,
            tags=tags,
            user_group_id=user_group_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7012476fc1dcf708502c3a40812f4ced90af74571a021bfa5091171717291b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b2123590dc90b36de3e39588015991928ac6ad2f7a93f300e83a897fbcd82d5)
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
        '''The Amazon Resource Name (ARN) of the serverless cache.

        :cloudformationAttribute: ARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''When the serverless cache was created.

        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointAddress")
    def attr_endpoint_address(self) -> builtins.str:
        '''The DNS hostname of the cache node.

        :cloudformationAttribute: Endpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointPort")
    def attr_endpoint_port(self) -> builtins.str:
        '''The port number that the cache engine is listening on.

        :cloudformationAttribute: Endpoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrFullEngineVersion")
    def attr_full_engine_version(self) -> builtins.str:
        '''The name and version number of the engine the serverless cache is compatible with.

        :cloudformationAttribute: FullEngineVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFullEngineVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrReaderEndpointAddress")
    def attr_reader_endpoint_address(self) -> builtins.str:
        '''The DNS hostname of the cache node.

        :cloudformationAttribute: ReaderEndpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReaderEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrReaderEndpointPort")
    def attr_reader_endpoint_port(self) -> builtins.str:
        '''The port number that the cache engine is listening on.

        :cloudformationAttribute: ReaderEndpoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReaderEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the serverless cache.

        The allowed values are CREATING, AVAILABLE, DELETING, CREATE-FAILED and MODIFYING.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        '''The engine the serverless cache is compatible with.'''
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db64b6c69d929608090194c9d83216677c91f2080ab6d4f59737f93d2e492503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="serverlessCacheName")
    def serverless_cache_name(self) -> builtins.str:
        '''The unique identifier of the serverless cache.'''
        return typing.cast(builtins.str, jsii.get(self, "serverlessCacheName"))

    @serverless_cache_name.setter
    def serverless_cache_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c553e861158121ce7a0545fdcf543b7615bf13ddc0bbd93cb52e72e27acd09d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverlessCacheName", value)

    @builtins.property
    @jsii.member(jsii_name="cacheUsageLimits")
    def cache_usage_limits(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.CacheUsageLimitsProperty"]]:
        '''The cache usage limit for the serverless cache.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.CacheUsageLimitsProperty"]], jsii.get(self, "cacheUsageLimits"))

    @cache_usage_limits.setter
    def cache_usage_limits(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.CacheUsageLimitsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a90cce9924849d9cc9e8f897f51cd6502787503e9fe6f9c0b146111c1c445aa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheUsageLimits", value)

    @builtins.property
    @jsii.member(jsii_name="dailySnapshotTime")
    def daily_snapshot_time(self) -> typing.Optional[builtins.str]:
        '''The daily time that a cache snapshot will be created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dailySnapshotTime"))

    @daily_snapshot_time.setter
    def daily_snapshot_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4072f21fb5867be241aa2784268fe8e3463d10cd511019b8f3599ec5d5c2cd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dailySnapshotTime", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the serverless cache.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6ee9bbb29fab9e6641d85980e882cc3db988c37421cc1d376048cdf7dfdcb06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.EndpointProperty"]]:
        '''Represents the information required for client programs to connect to a cache node.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.EndpointProperty"]], jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.EndpointProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf26818381fc6b07f8a2615330e14830cc8722c7bea067d80e6017ceab59af6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotName")
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of the final snapshot taken of a cache before the cache is deleted.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "finalSnapshotName"))

    @final_snapshot_name.setter
    def final_snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62246ee954ddcb344e45c430ef7cbe75d5a3b692a00d6e538baa399c5cab349a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8cc8a3d052be3fabfdfe466bf509434f5707efc6a6dcd0770cc1a1b97e07a80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="majorEngineVersion")
    def major_engine_version(self) -> typing.Optional[builtins.str]:
        '''The version number of the engine the serverless cache is compatible with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "majorEngineVersion"))

    @major_engine_version.setter
    def major_engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__618e7242f4c8d6ea2092e93310602455166596d1a96215a2fb33d826bbe5fd29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "majorEngineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="readerEndpoint")
    def reader_endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.EndpointProperty"]]:
        '''Represents the information required for client programs to connect to a cache node.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.EndpointProperty"]], jsii.get(self, "readerEndpoint"))

    @reader_endpoint.setter
    def reader_endpoint(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.EndpointProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e3145e59d2b03c61c29dd7fc18ce6d775561dcfa018b131c81d1f6e06fcd65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readerEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IDs of the EC2 security groups associated with the serverless cache.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c96776cfdc2836177648dc34a892d382e760b03e46d603807886c25a9fc1d103)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotArnsToRestore")
    def snapshot_arns_to_restore(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the snapshot from which to restore data into the new cache.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snapshotArnsToRestore"))

    @snapshot_arns_to_restore.setter
    def snapshot_arns_to_restore(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e490a4ceeec73f3d373a179650cfec51a7cf58d7c4e7f5b06544dd1a2df316)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotArnsToRestore", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''The current setting for the number of serverless cache snapshots the system will retain.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotRetentionLimit"))

    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fe4130c8869d67e8891f2bbbc10c149c15af0b801a4c9393fe4b4bcc848e3f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotRetentionLimit", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca2b56b13f3d8c09fd6a0e74df162e790fe2013d9a8d3d546b7b1aa5af8b507)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be added to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2054e990234791671dd0f6c1b491baebdfaaa093bc590373b8cbe5d6a7dec291)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="userGroupId")
    def user_group_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the user group associated with the serverless cache.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userGroupId"))

    @user_group_id.setter
    def user_group_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b592bfec207d3f2428902a54fb8adfacc60bdb7a83c47e12c1b4d76ac68444ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroupId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnServerlessCache.CacheUsageLimitsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_storage": "dataStorage",
            "ecpu_per_second": "ecpuPerSecond",
        },
    )
    class CacheUsageLimitsProperty:
        def __init__(
            self,
            *,
            data_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCache.DataStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ecpu_per_second: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServerlessCache.ECPUPerSecondProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The usage limits for storage and ElastiCache Processing Units for the cache.

            :param data_storage: The maximum data storage limit in the cache, expressed in Gigabytes.
            :param ecpu_per_second: The number of ElastiCache Processing Units (ECPU) the cache can consume per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-cacheusagelimits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                cache_usage_limits_property = elasticache.CfnServerlessCache.CacheUsageLimitsProperty(
                    data_storage=elasticache.CfnServerlessCache.DataStorageProperty(
                        unit="unit",
                
                        # the properties below are optional
                        maximum=123,
                        minimum=123
                    ),
                    ecpu_per_second=elasticache.CfnServerlessCache.ECPUPerSecondProperty(
                        maximum=123,
                        minimum=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__77ebaaf0b703f3ff0164d4845d37449699aec6cbe500ff6d63278a3a64427450)
                check_type(argname="argument data_storage", value=data_storage, expected_type=type_hints["data_storage"])
                check_type(argname="argument ecpu_per_second", value=ecpu_per_second, expected_type=type_hints["ecpu_per_second"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_storage is not None:
                self._values["data_storage"] = data_storage
            if ecpu_per_second is not None:
                self._values["ecpu_per_second"] = ecpu_per_second

        @builtins.property
        def data_storage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.DataStorageProperty"]]:
            '''The maximum data storage limit in the cache, expressed in Gigabytes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-cacheusagelimits.html#cfn-elasticache-serverlesscache-cacheusagelimits-datastorage
            '''
            result = self._values.get("data_storage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.DataStorageProperty"]], result)

        @builtins.property
        def ecpu_per_second(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.ECPUPerSecondProperty"]]:
            '''The number of ElastiCache Processing Units (ECPU) the cache can consume per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-cacheusagelimits.html#cfn-elasticache-serverlesscache-cacheusagelimits-ecpupersecond
            '''
            result = self._values.get("ecpu_per_second")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServerlessCache.ECPUPerSecondProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CacheUsageLimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnServerlessCache.DataStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "maximum": "maximum", "minimum": "minimum"},
    )
    class DataStorageProperty:
        def __init__(
            self,
            *,
            unit: builtins.str,
            maximum: typing.Optional[jsii.Number] = None,
            minimum: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The data storage limit.

            :param unit: The unit that the storage is measured in, in GB.
            :param maximum: The upper limit for data storage the cache is set to use.
            :param minimum: The lower limit for data storage the cache is set to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-datastorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                data_storage_property = elasticache.CfnServerlessCache.DataStorageProperty(
                    unit="unit",
                
                    # the properties below are optional
                    maximum=123,
                    minimum=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__14470b22401430bce81195b8e644412f38b76011c8cab7fa8399081bd44b546d)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
                check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
            }
            if maximum is not None:
                self._values["maximum"] = maximum
            if minimum is not None:
                self._values["minimum"] = minimum

        @builtins.property
        def unit(self) -> builtins.str:
            '''The unit that the storage is measured in, in GB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-datastorage.html#cfn-elasticache-serverlesscache-datastorage-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maximum(self) -> typing.Optional[jsii.Number]:
            '''The upper limit for data storage the cache is set to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-datastorage.html#cfn-elasticache-serverlesscache-datastorage-maximum
            '''
            result = self._values.get("maximum")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum(self) -> typing.Optional[jsii.Number]:
            '''The lower limit for data storage the cache is set to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-datastorage.html#cfn-elasticache-serverlesscache-datastorage-minimum
            '''
            result = self._values.get("minimum")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnServerlessCache.ECPUPerSecondProperty",
        jsii_struct_bases=[],
        name_mapping={"maximum": "maximum", "minimum": "minimum"},
    )
    class ECPUPerSecondProperty:
        def __init__(
            self,
            *,
            maximum: typing.Optional[jsii.Number] = None,
            minimum: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The configuration for the number of ElastiCache Processing Units (ECPU) the cache can consume per second.

            :param maximum: The configuration for the maximum number of ECPUs the cache can consume per second.
            :param minimum: The configuration for the minimum number of ECPUs the cache should be able consume per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-ecpupersecond.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                e_cPUPer_second_property = elasticache.CfnServerlessCache.ECPUPerSecondProperty(
                    maximum=123,
                    minimum=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4a85c1f856007000025702b1b01488e1f0726e767adf52fbf709f88ed3720f1)
                check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
                check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if maximum is not None:
                self._values["maximum"] = maximum
            if minimum is not None:
                self._values["minimum"] = minimum

        @builtins.property
        def maximum(self) -> typing.Optional[jsii.Number]:
            '''The configuration for the maximum number of ECPUs the cache can consume per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-ecpupersecond.html#cfn-elasticache-serverlesscache-ecpupersecond-maximum
            '''
            result = self._values.get("maximum")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum(self) -> typing.Optional[jsii.Number]:
            '''The configuration for the minimum number of ECPUs the cache should be able consume per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-ecpupersecond.html#cfn-elasticache-serverlesscache-ecpupersecond-minimum
            '''
            result = self._values.get("minimum")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ECPUPerSecondProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnServerlessCache.EndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "port": "port"},
    )
    class EndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents the information required for client programs to connect to a cache node.

            This value is read-only.

            :param address: The DNS hostname of the cache node.
            :param port: The port number that the cache engine is listening on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-endpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                endpoint_property = elasticache.CfnServerlessCache.EndpointProperty(
                    address="address",
                    port="port"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e66cf1143a0bb8344a2f8dd0d18b42b664e7256d7ac1eb56ff9cab6b66fff5d5)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The DNS hostname of the cache node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-endpoint.html#cfn-elasticache-serverlesscache-endpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The port number that the cache engine is listening on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-serverlesscache-endpoint.html#cfn-elasticache-serverlesscache-endpoint-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnServerlessCacheProps",
    jsii_struct_bases=[],
    name_mapping={
        "engine": "engine",
        "serverless_cache_name": "serverlessCacheName",
        "cache_usage_limits": "cacheUsageLimits",
        "daily_snapshot_time": "dailySnapshotTime",
        "description": "description",
        "endpoint": "endpoint",
        "final_snapshot_name": "finalSnapshotName",
        "kms_key_id": "kmsKeyId",
        "major_engine_version": "majorEngineVersion",
        "reader_endpoint": "readerEndpoint",
        "security_group_ids": "securityGroupIds",
        "snapshot_arns_to_restore": "snapshotArnsToRestore",
        "snapshot_retention_limit": "snapshotRetentionLimit",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "user_group_id": "userGroupId",
    },
)
class CfnServerlessCacheProps:
    def __init__(
        self,
        *,
        engine: builtins.str,
        serverless_cache_name: builtins.str,
        cache_usage_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.CacheUsageLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        daily_snapshot_time: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        major_engine_version: typing.Optional[builtins.str] = None,
        reader_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns_to_restore: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnServerlessCache``.

        :param engine: The engine the serverless cache is compatible with.
        :param serverless_cache_name: The unique identifier of the serverless cache.
        :param cache_usage_limits: The cache usage limit for the serverless cache.
        :param daily_snapshot_time: The daily time that a cache snapshot will be created. Default is NULL, i.e. snapshots will not be created at a specific time on a daily basis. Available for Redis only.
        :param description: A description of the serverless cache.
        :param endpoint: Represents the information required for client programs to connect to a cache node. This value is read-only.
        :param final_snapshot_name: The name of the final snapshot taken of a cache before the cache is deleted.
        :param kms_key_id: The ID of the AWS Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.
        :param major_engine_version: The version number of the engine the serverless cache is compatible with.
        :param reader_endpoint: Represents the information required for client programs to connect to a cache node. This value is read-only.
        :param security_group_ids: The IDs of the EC2 security groups associated with the serverless cache.
        :param snapshot_arns_to_restore: The ARN of the snapshot from which to restore data into the new cache.
        :param snapshot_retention_limit: The current setting for the number of serverless cache snapshots the system will retain. Available for Redis only.
        :param subnet_ids: If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC. For all other Regions, if no subnet IDs are given then ElastiCache will select 3 default subnets across AZs in your default VPC.
        :param tags: A list of tags to be added to this resource.
        :param user_group_id: The identifier of the user group associated with the serverless cache. Available for Redis only. Default is NULL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_serverless_cache_props = elasticache.CfnServerlessCacheProps(
                engine="engine",
                serverless_cache_name="serverlessCacheName",
            
                # the properties below are optional
                cache_usage_limits=elasticache.CfnServerlessCache.CacheUsageLimitsProperty(
                    data_storage=elasticache.CfnServerlessCache.DataStorageProperty(
                        unit="unit",
            
                        # the properties below are optional
                        maximum=123,
                        minimum=123
                    ),
                    ecpu_per_second=elasticache.CfnServerlessCache.ECPUPerSecondProperty(
                        maximum=123,
                        minimum=123
                    )
                ),
                daily_snapshot_time="dailySnapshotTime",
                description="description",
                endpoint=elasticache.CfnServerlessCache.EndpointProperty(
                    address="address",
                    port="port"
                ),
                final_snapshot_name="finalSnapshotName",
                kms_key_id="kmsKeyId",
                major_engine_version="majorEngineVersion",
                reader_endpoint=elasticache.CfnServerlessCache.EndpointProperty(
                    address="address",
                    port="port"
                ),
                security_group_ids=["securityGroupIds"],
                snapshot_arns_to_restore=["snapshotArnsToRestore"],
                snapshot_retention_limit=123,
                subnet_ids=["subnetIds"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_group_id="userGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b8c0bd8ed5d4d4b90b896e92a64fc113ba2b7b80dfa7075b8fad4b02f5886c)
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument serverless_cache_name", value=serverless_cache_name, expected_type=type_hints["serverless_cache_name"])
            check_type(argname="argument cache_usage_limits", value=cache_usage_limits, expected_type=type_hints["cache_usage_limits"])
            check_type(argname="argument daily_snapshot_time", value=daily_snapshot_time, expected_type=type_hints["daily_snapshot_time"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument final_snapshot_name", value=final_snapshot_name, expected_type=type_hints["final_snapshot_name"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument major_engine_version", value=major_engine_version, expected_type=type_hints["major_engine_version"])
            check_type(argname="argument reader_endpoint", value=reader_endpoint, expected_type=type_hints["reader_endpoint"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument snapshot_arns_to_restore", value=snapshot_arns_to_restore, expected_type=type_hints["snapshot_arns_to_restore"])
            check_type(argname="argument snapshot_retention_limit", value=snapshot_retention_limit, expected_type=type_hints["snapshot_retention_limit"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_group_id", value=user_group_id, expected_type=type_hints["user_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "engine": engine,
            "serverless_cache_name": serverless_cache_name,
        }
        if cache_usage_limits is not None:
            self._values["cache_usage_limits"] = cache_usage_limits
        if daily_snapshot_time is not None:
            self._values["daily_snapshot_time"] = daily_snapshot_time
        if description is not None:
            self._values["description"] = description
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if final_snapshot_name is not None:
            self._values["final_snapshot_name"] = final_snapshot_name
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if major_engine_version is not None:
            self._values["major_engine_version"] = major_engine_version
        if reader_endpoint is not None:
            self._values["reader_endpoint"] = reader_endpoint
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if snapshot_arns_to_restore is not None:
            self._values["snapshot_arns_to_restore"] = snapshot_arns_to_restore
        if snapshot_retention_limit is not None:
            self._values["snapshot_retention_limit"] = snapshot_retention_limit
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags
        if user_group_id is not None:
            self._values["user_group_id"] = user_group_id

    @builtins.property
    def engine(self) -> builtins.str:
        '''The engine the serverless cache is compatible with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-engine
        '''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def serverless_cache_name(self) -> builtins.str:
        '''The unique identifier of the serverless cache.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-serverlesscachename
        '''
        result = self._values.get("serverless_cache_name")
        assert result is not None, "Required property 'serverless_cache_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_usage_limits(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.CacheUsageLimitsProperty]]:
        '''The cache usage limit for the serverless cache.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-cacheusagelimits
        '''
        result = self._values.get("cache_usage_limits")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.CacheUsageLimitsProperty]], result)

    @builtins.property
    def daily_snapshot_time(self) -> typing.Optional[builtins.str]:
        '''The daily time that a cache snapshot will be created.

        Default is NULL, i.e. snapshots will not be created at a specific time on a daily basis. Available for Redis only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-dailysnapshottime
        '''
        result = self._values.get("daily_snapshot_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the serverless cache.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.EndpointProperty]]:
        '''Represents the information required for client programs to connect to a cache node.

        This value is read-only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-endpoint
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.EndpointProperty]], result)

    @builtins.property
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of the final snapshot taken of a cache before the cache is deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-finalsnapshotname
        '''
        result = self._values.get("final_snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def major_engine_version(self) -> typing.Optional[builtins.str]:
        '''The version number of the engine the serverless cache is compatible with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-majorengineversion
        '''
        result = self._values.get("major_engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reader_endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.EndpointProperty]]:
        '''Represents the information required for client programs to connect to a cache node.

        This value is read-only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-readerendpoint
        '''
        result = self._values.get("reader_endpoint")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.EndpointProperty]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IDs of the EC2 security groups associated with the serverless cache.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_arns_to_restore(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the snapshot from which to restore data into the new cache.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-snapshotarnstorestore
        '''
        result = self._values.get("snapshot_arns_to_restore")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''The current setting for the number of serverless cache snapshots the system will retain.

        Available for Redis only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-snapshotretentionlimit
        '''
        result = self._values.get("snapshot_retention_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC.

        For all other Regions, if no subnet IDs are given then ElastiCache will select 3 default subnets across AZs in your default VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be added to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_group_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the user group associated with the serverless cache.

        Available for Redis only. Default is NULL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscache.html#cfn-elasticache-serverlesscache-usergroupid
        '''
        result = self._values.get("user_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerlessCacheProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSubnetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnSubnetGroup",
):
    '''Creates a cache subnet group.

    For more information about cache subnet groups, go to Cache Subnet Groups in the *Amazon ElastiCache User Guide* or go to `CreateCacheSubnetGroup <https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSubnetGroup.html>`_ in the *Amazon ElastiCache API Reference Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html
    :cloudformationResource: AWS::ElastiCache::SubnetGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_subnet_group = elasticache.CfnSubnetGroup(self, "MyCfnSubnetGroup",
            description="description",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            cache_subnet_group_name="cacheSubnetGroupName",
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
        description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: The description for the cache subnet group.
        :param subnet_ids: The EC2 subnet IDs for the cache subnet group.
        :param cache_subnet_group_name: The name for the cache subnet group. This value is stored as a lowercase string. Constraints: Must contain no more than 255 alphanumeric characters or hyphens. Example: ``mysubnetgroup``
        :param tags: A tag that can be added to an ElastiCache subnet group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your subnet groups. A tag with a null Value is permitted.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d31f960507f2c9e3587baf93d99fa25f2747d0865408ff081e5c5230bf44b04)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubnetGroupProps(
            description=description,
            subnet_ids=subnet_ids,
            cache_subnet_group_name=cache_subnet_group_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e74c02a4794273fd857125de793130ad00a35e7107b9a052fd9729c834e8c03)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c394e0da879e36e1158aa11a6d2a3848b9c833cd6c8b791f2a306dcd1d6bc39)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description for the cache subnet group.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c5ab35ff7baba1205becdb157e37a43b2ffdb8d78b6a89812dec13e870110ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The EC2 subnet IDs for the cache subnet group.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__406b48aa434500b28470efd76a3cfb00968662ddd966571565ba3c47788bd26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="cacheSubnetGroupName")
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name for the cache subnet group.

        This value is stored as a lowercase string.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheSubnetGroupName"))

    @cache_subnet_group_name.setter
    def cache_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26295a8a2dc7d2b6948d4efdcca51f3722ed36bec5ced2fbf24d774ea7b28163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A tag that can be added to an ElastiCache subnet group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f6670815d10d752e7b16bcf0f681bfa6e802161e1b1eba4c63dd3a6d9846719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "subnet_ids": "subnetIds",
        "cache_subnet_group_name": "cacheSubnetGroupName",
        "tags": "tags",
    },
)
class CfnSubnetGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubnetGroup``.

        :param description: The description for the cache subnet group.
        :param subnet_ids: The EC2 subnet IDs for the cache subnet group.
        :param cache_subnet_group_name: The name for the cache subnet group. This value is stored as a lowercase string. Constraints: Must contain no more than 255 alphanumeric characters or hyphens. Example: ``mysubnetgroup``
        :param tags: A tag that can be added to an ElastiCache subnet group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your subnet groups. A tag with a null Value is permitted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_subnet_group_props = elasticache.CfnSubnetGroupProps(
                description="description",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                cache_subnet_group_name="cacheSubnetGroupName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b45c5c5c7c2f90c8c0fc4304349cfb95eff57e46669706a32a0b5b73fc2139)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument cache_subnet_group_name", value=cache_subnet_group_name, expected_type=type_hints["cache_subnet_group_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "subnet_ids": subnet_ids,
        }
        if cache_subnet_group_name is not None:
            self._values["cache_subnet_group_name"] = cache_subnet_group_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''The description for the cache subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The EC2 subnet IDs for the cache subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name for the cache subnet group. This value is stored as a lowercase string.

        Constraints: Must contain no more than 255 alphanumeric characters or hyphens.

        Example: ``mysubnetgroup``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-cachesubnetgroupname
        '''
        result = self._values.get("cache_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A tag that can be added to an ElastiCache subnet group.

        Tags are composed of a Key/Value pair. You can use tags to categorize and track all your subnet groups. A tag with a null Value is permitted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnUser(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnUser",
):
    '''For Redis engine version 6.0 onwards: Creates a Redis user. For more information, see `Using Role Based Access Control (RBAC) <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html
    :cloudformationResource: AWS::ElastiCache::User
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        # authentication_mode: Any
        
        cfn_user = elasticache.CfnUser(self, "MyCfnUser",
            engine="engine",
            user_id="userId",
            user_name="userName",
        
            # the properties below are optional
            access_string="accessString",
            authentication_mode=authentication_mode,
            no_password_required=False,
            passwords=["passwords"],
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
        engine: builtins.str,
        user_id: builtins.str,
        user_name: builtins.str,
        access_string: typing.Optional[builtins.str] = None,
        authentication_mode: typing.Any = None,
        no_password_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param engine: The current supported value is redis.
        :param user_id: The ID of the user.
        :param user_name: The username of the user.
        :param access_string: Access permissions string used for this user.
        :param authentication_mode: Specifies the authentication mode to use. Below is an example of the possible JSON values:. Example:: { Passwords: ["*****", "******"] // If Type is password. }
        :param no_password_required: Indicates a password is not required for this user.
        :param passwords: Passwords used for this user. You can create up to two passwords for each user.
        :param tags: An array of key-value pairs to apply to this user.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3690e849b3e5bf7f482e77652d683906b1133738dbc72aea39d0186729f84fd0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            engine=engine,
            user_id=user_id,
            user_name=user_name,
            access_string=access_string,
            authentication_mode=authentication_mode,
            no_password_required=no_password_required,
            passwords=passwords,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8027fd2dc9d1d9c383f787790509ce0a31493b0c5928b63706caf8cd2096acf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d2c24ac7e99a31a4e0d4135ea5447976f3d5233d9d0e77c498d74df49e859a5)
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
        '''The Amazon Resource Name (ARN) of the user.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Indicates the user status.

        Can be "active", "modifying" or "deleting".

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        '''The current supported value is redis.'''
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74df73fc62abe9fa1155cea79085975215d2cc3a30983f4b784d74b2d8dafec0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        '''The ID of the user.'''
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45b8eb0ca4560239c33c66aef6a7b3087bdea40d47268790b66085c594bb3ae1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The username of the user.'''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82b6eed2d66e57932003ce447ee4a3219513ca0c8161fae47c096809d764af5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="accessString")
    def access_string(self) -> typing.Optional[builtins.str]:
        '''Access permissions string used for this user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessString"))

    @access_string.setter
    def access_string(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb7549e3e6dbe94afa410bffc87623817e4cb26f90efb581b9a8d6dfcea71b64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessString", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationMode")
    def authentication_mode(self) -> typing.Any:
        '''Specifies the authentication mode to use.

        Below is an example of the possible JSON values:.
        '''
        return typing.cast(typing.Any, jsii.get(self, "authenticationMode"))

    @authentication_mode.setter
    def authentication_mode(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08a67425ea4c8dcb1628c0ebb391eb9d3ca8fd07b5c6306f039cb531a05565d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationMode", value)

    @builtins.property
    @jsii.member(jsii_name="noPasswordRequired")
    def no_password_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates a password is not required for this user.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "noPasswordRequired"))

    @no_password_required.setter
    def no_password_required(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dc0162c51746ac68f8e6c599bd425920aec49776f251d176073c998647b402e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noPasswordRequired", value)

    @builtins.property
    @jsii.member(jsii_name="passwords")
    def passwords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Passwords used for this user.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "passwords"))

    @passwords.setter
    def passwords(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd01953837fe46505e356e5e6f503c48a5037161ed165b5dfa3d2124c10bf225)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwords", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this user.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda53c926e8acd673280fda87bee7f7bcf1def006ab1883b24a6a077e43b7449)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticache.CfnUser.AuthenticationModeProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "passwords": "passwords"},
    )
    class AuthenticationModeProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the authentication mode to use.

            :param type: Specifies the authentication type. Possible options are IAM authentication, password and no password.
            :param passwords: Specifies the passwords to use for authentication if ``Type`` is set to ``password`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-user-authenticationmode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticache as elasticache
                
                authentication_mode_property = elasticache.CfnUser.AuthenticationModeProperty(
                    type="type",
                
                    # the properties below are optional
                    passwords=["passwords"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec04d0248d22cdd45ac6431c550d1bdf03740a43412b686373b189e770fd0d91)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument passwords", value=passwords, expected_type=type_hints["passwords"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if passwords is not None:
                self._values["passwords"] = passwords

        @builtins.property
        def type(self) -> builtins.str:
            '''Specifies the authentication type.

            Possible options are IAM authentication, password and no password.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-user-authenticationmode.html#cfn-elasticache-user-authenticationmode-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def passwords(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the passwords to use for authentication if ``Type`` is set to ``password`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-user-authenticationmode.html#cfn-elasticache-user-authenticationmode-passwords
            '''
            result = self._values.get("passwords")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationModeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnUserGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticache.CfnUserGroup",
):
    '''For Redis engine version 6.0 onwards: Creates a Redis user group. For more information, see `Using Role Based Access Control (RBAC) <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html>`_.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html
    :cloudformationResource: AWS::ElastiCache::UserGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticache as elasticache
        
        cfn_user_group = elasticache.CfnUserGroup(self, "MyCfnUserGroup",
            engine="engine",
            user_group_id="userGroupId",
            user_ids=["userIds"],
        
            # the properties below are optional
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
        engine: builtins.str,
        user_group_id: builtins.str,
        user_ids: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param engine: The current supported value is redis.
        :param user_group_id: The ID of the user group.
        :param user_ids: The list of user IDs that belong to the user group. A user named ``default`` must be included.
        :param tags: An array of key-value pairs to apply to this user.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc142924e04b2348d54a42d3f1272d7a6d9f1886d6e9133f1a0ed55abcda10a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserGroupProps(
            engine=engine, user_group_id=user_group_id, user_ids=user_ids, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a5d03fb1ca11359d2e12cf9829f5c78e442be6d3175a5f56c52bd5c800742a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__450a9b959ab13e887b9b352f9708de268fb109cca3789dc4eeea0989d1c33d28)
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
        '''The Amazon Resource Name (ARN) of the user group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Indicates user group status.

        Can be "creating", "active", "modifying", "deleting".

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        '''The current supported value is redis.'''
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e431968f516bc728e154bbd117b40cd38af16bf361c399b85db4f54094ac994)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="userGroupId")
    def user_group_id(self) -> builtins.str:
        '''The ID of the user group.'''
        return typing.cast(builtins.str, jsii.get(self, "userGroupId"))

    @user_group_id.setter
    def user_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2d97633ea9a0c04b7eee81db8315453f4d5e7436b511bc476886df00a72145)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="userIds")
    def user_ids(self) -> typing.List[builtins.str]:
        '''The list of user IDs that belong to the user group.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "userIds"))

    @user_ids.setter
    def user_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537c18038663c50194ccf261d54d663088b0bde017663b14868ca50759a76109)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this user.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f91d8988fa4ff59ae0f0f6e912aaa87f88df9ee98afddb86934a2611c1d0da39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnUserGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "engine": "engine",
        "user_group_id": "userGroupId",
        "user_ids": "userIds",
        "tags": "tags",
    },
)
class CfnUserGroupProps:
    def __init__(
        self,
        *,
        engine: builtins.str,
        user_group_id: builtins.str,
        user_ids: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUserGroup``.

        :param engine: The current supported value is redis.
        :param user_group_id: The ID of the user group.
        :param user_ids: The list of user IDs that belong to the user group. A user named ``default`` must be included.
        :param tags: An array of key-value pairs to apply to this user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            cfn_user_group_props = elasticache.CfnUserGroupProps(
                engine="engine",
                user_group_id="userGroupId",
                user_ids=["userIds"],
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__781d57350a7876de81adb05f4b5f1c6a6733fe48684f64bf990d3377377290ab)
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument user_group_id", value=user_group_id, expected_type=type_hints["user_group_id"])
            check_type(argname="argument user_ids", value=user_ids, expected_type=type_hints["user_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "engine": engine,
            "user_group_id": user_group_id,
            "user_ids": user_ids,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def engine(self) -> builtins.str:
        '''The current supported value is redis.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-engine
        '''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_group_id(self) -> builtins.str:
        '''The ID of the user group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-usergroupid
        '''
        result = self._values.get("user_group_id")
        assert result is not None, "Required property 'user_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_ids(self) -> typing.List[builtins.str]:
        '''The list of user IDs that belong to the user group.

        A user named ``default`` must be included.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-userids
        '''
        result = self._values.get("user_ids")
        assert result is not None, "Required property 'user_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticache.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "engine": "engine",
        "user_id": "userId",
        "user_name": "userName",
        "access_string": "accessString",
        "authentication_mode": "authenticationMode",
        "no_password_required": "noPasswordRequired",
        "passwords": "passwords",
        "tags": "tags",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        engine: builtins.str,
        user_id: builtins.str,
        user_name: builtins.str,
        access_string: typing.Optional[builtins.str] = None,
        authentication_mode: typing.Any = None,
        no_password_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUser``.

        :param engine: The current supported value is redis.
        :param user_id: The ID of the user.
        :param user_name: The username of the user.
        :param access_string: Access permissions string used for this user.
        :param authentication_mode: Specifies the authentication mode to use. Below is an example of the possible JSON values:. Example:: { Passwords: ["*****", "******"] // If Type is password. }
        :param no_password_required: Indicates a password is not required for this user.
        :param passwords: Passwords used for this user. You can create up to two passwords for each user.
        :param tags: An array of key-value pairs to apply to this user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticache as elasticache
            
            # authentication_mode: Any
            
            cfn_user_props = elasticache.CfnUserProps(
                engine="engine",
                user_id="userId",
                user_name="userName",
            
                # the properties below are optional
                access_string="accessString",
                authentication_mode=authentication_mode,
                no_password_required=False,
                passwords=["passwords"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd58f3eed78cb4ce0cff0a0f48e20670425d5891d9c8b2bd0b6006a78cfe7ab5)
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument access_string", value=access_string, expected_type=type_hints["access_string"])
            check_type(argname="argument authentication_mode", value=authentication_mode, expected_type=type_hints["authentication_mode"])
            check_type(argname="argument no_password_required", value=no_password_required, expected_type=type_hints["no_password_required"])
            check_type(argname="argument passwords", value=passwords, expected_type=type_hints["passwords"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "engine": engine,
            "user_id": user_id,
            "user_name": user_name,
        }
        if access_string is not None:
            self._values["access_string"] = access_string
        if authentication_mode is not None:
            self._values["authentication_mode"] = authentication_mode
        if no_password_required is not None:
            self._values["no_password_required"] = no_password_required
        if passwords is not None:
            self._values["passwords"] = passwords
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def engine(self) -> builtins.str:
        '''The current supported value is redis.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-engine
        '''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_id(self) -> builtins.str:
        '''The ID of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-userid
        '''
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The username of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_string(self) -> typing.Optional[builtins.str]:
        '''Access permissions string used for this user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-accessstring
        '''
        result = self._values.get("access_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication_mode(self) -> typing.Any:
        '''Specifies the authentication mode to use. Below is an example of the possible JSON values:.

        Example::

           { Passwords: ["*****", "******"] // If Type is password.
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-authenticationmode
        '''
        result = self._values.get("authentication_mode")
        return typing.cast(typing.Any, result)

    @builtins.property
    def no_password_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates a password is not required for this user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-nopasswordrequired
        '''
        result = self._values.get("no_password_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def passwords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Passwords used for this user.

        You can create up to two passwords for each user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-passwords
        '''
        result = self._values.get("passwords")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCacheCluster",
    "CfnCacheClusterProps",
    "CfnGlobalReplicationGroup",
    "CfnGlobalReplicationGroupProps",
    "CfnParameterGroup",
    "CfnParameterGroupProps",
    "CfnReplicationGroup",
    "CfnReplicationGroupProps",
    "CfnSecurityGroup",
    "CfnSecurityGroupIngress",
    "CfnSecurityGroupIngressProps",
    "CfnSecurityGroupProps",
    "CfnServerlessCache",
    "CfnServerlessCacheProps",
    "CfnSubnetGroup",
    "CfnSubnetGroupProps",
    "CfnUser",
    "CfnUserGroup",
    "CfnUserGroupProps",
    "CfnUserProps",
]

publication.publish()

def _typecheckingstub__4b878d00130d900710d9efbde27b5162741ad68343a5e4b8b7283244b24aa2b8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cache_node_type: builtins.str,
    engine: builtins.str,
    num_cache_nodes: jsii.Number,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    az_mode: typing.Optional[builtins.str] = None,
    cache_parameter_group_name: typing.Optional[builtins.str] = None,
    cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    cache_subnet_group_name: typing.Optional[builtins.str] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    ip_discovery: typing.Optional[builtins.str] = None,
    log_delivery_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCacheCluster.LogDeliveryConfigurationRequestProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_type: typing.Optional[builtins.str] = None,
    notification_topic_arn: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_availability_zone: typing.Optional[builtins.str] = None,
    preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    snapshot_window: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae530a9eb0474b9ffc367e7c2714f1d8b14943c9354c6c91d798290bf12e70ef(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dec52b5b4ebdf39402ca71f50f4dc30da259049be70433e6c00efc9ea6aba16(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d9802d6751a916028ade8020c1b88f4de76492648ad82353d20bc756837067(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b478c5471c9d0a76c5100e39ca78b723b0c0df15786d8701347d9cb5eabbdf7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3efa7fe979ad2ca65054b031fb5cd53cdae6a1094de4cdb6bc9c480d5b2d7a9f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b74ab91b309fe8b033442df78ec7c947ef8b8ceac25b5fb4347e7e697fb388da(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a44d250f986c389a2d9f94d9cca8adc9e59c15e75d4c051e15c57482b9ae9f1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc3ac1b1f30d407a5545f9f5024999aba8b2072b3d9b7d1c0941506aa6431636(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83da5de50c36f6b8acecefb71f2d1985a98bac5b47b9355f1e680a968d3b916a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9b8dc42c226f2bde38136c38ed0888aa8016a952545561870cd97fdb1756c48(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__411d6faf725ba835ededa6d23d62caaccc85488363ac53847d26489a9b698e4c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c11aa65ad582a06f82ee3dccb397779d9465180eeb2cc3743f037d45678b9315(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d9fae8437c1df5da80ef1dcc1d540757d3eeed744bbf8056a118a155cda7c0b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92cc1290aacd3e87fdb8540c5a430dd3781b4d21f64685730ff4176b05840454(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCacheCluster.LogDeliveryConfigurationRequestProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fef16cd8be345649445baed2ab221599bc312c701ed3cae8a08ca0202aedbbe0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e5b55a4eeff9a98884374f1fb103e28154e68b08e9c604194db4263d8d260c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52a7b53b9de4c47324594ae4fcae12b0f548358d236a57d0d8180b7a52eb525(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba8deec010d483a5b4cccad86835cc42901ab76f481c5140bf432d398851cab3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdfef5e25f162b7075022826fc8305415c9b26eba0d5f6a128a30b8e191ecf2d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c036bebdfade47bb20565d6116e08cbc6b2c289599c511df24ad3ec9395670fc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce434b0b24d4c0aed191822a2ef96062ce0e4f82dde36706dda0cb9378020e9d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade889ee7923a82577f80b57aeef301ae196124bdb4d5ec2cd87c371be03e5a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36088ccf4e3bb96fca149a1dc57264e825a3fdf78d280f320127ed72733b6ef2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00985af0e32e63259c356a919afbcf2f8aec8c2faedaece96112bbb03f945239(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb033789ee709e38cf2df5c67f41474c2337ba8ce07eac9ee4a2c714fc9bc989(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5c36f3eb4db3de564bb875816a147602a4348d296a24fafccdae0acba9440b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca563dd75820580354392265b3bdcb759aaa1e66fadcc95daa9e8b3b8bc892d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b917ac927a2387372c693a2f8b0fcb5f6774e69a0fe6f786bb4da65afb46978c(
    *,
    log_group: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000cbd02f7786299cee1e93bf5afb34c16e6ab92a2447aa9f4bf42256a0a51f1(
    *,
    cloud_watch_logs_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_firehose_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cae1eb34767a8b034d88d62d4b6f18e4d990339139fe3e1e6652a41616e9435(
    *,
    delivery_stream: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11fd3bc6d619f2fdddcc4d0adb3f2c760e25cb0796cacc1c490de7b091ee75a0(
    *,
    destination_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCacheCluster.DestinationDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    destination_type: builtins.str,
    log_format: builtins.str,
    log_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d011d844fc37e1278b56242476eb6678a2ec76110ae295205b57260221f991ae(
    *,
    cache_node_type: builtins.str,
    engine: builtins.str,
    num_cache_nodes: jsii.Number,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    az_mode: typing.Optional[builtins.str] = None,
    cache_parameter_group_name: typing.Optional[builtins.str] = None,
    cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    cache_subnet_group_name: typing.Optional[builtins.str] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    ip_discovery: typing.Optional[builtins.str] = None,
    log_delivery_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCacheCluster.LogDeliveryConfigurationRequestProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_type: typing.Optional[builtins.str] = None,
    notification_topic_arn: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_availability_zone: typing.Optional[builtins.str] = None,
    preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    snapshot_window: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b347e00f869706c90d3dc918dc3fb240c81a3a2e15ca55cb3a114e779ebe3be(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    members: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty, typing.Dict[builtins.str, typing.Any]]]]],
    automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cache_node_type: typing.Optional[builtins.str] = None,
    cache_parameter_group_name: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    global_node_group_count: typing.Optional[jsii.Number] = None,
    global_replication_group_description: typing.Optional[builtins.str] = None,
    global_replication_group_id_suffix: typing.Optional[builtins.str] = None,
    regional_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGlobalReplicationGroup.RegionalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__884a154d8b8e4d93c61fe6b39de707bf773a6d1033e974181f93658b1039c0c4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab038bf042b008b9efadcbadf432cd0ac40752df55c21a630a9780aae3ef72f0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e868e518f50b5b48c699f872e36b8e20be2702ad6acf8d5f4500e986aac55b3d(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f937e9779d5fe5d88540d353152c5e7637a4c898506e495763dc389bca1a193(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc0668ac08361dfeaf1c9d3b63f4ce55339cbac4acdba22253a2c6a39440c9c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0848ddc407bc59c23bb3f0758cd29c2ca80ecb4af0b703cfbabe761143efb996(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6d37e14147abb9446aa94586bbfdc04bcc4cbad9c87b170bc3c934223a3dc1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e8402ce6e7036902a30a006b2e3b7c82ed86d4655e500c78d0ae603a7929b0(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb8c976f8e943135a48d97d88bf3d8b7dd5f17fcd2b8759518b8b204056bba0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65acba21207d62e08b1c8c4c4f55ea3089c76799e113952d0b5f8bd4e6ee53d5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efeee031dd310c05cefd1733ccdb9d7b436fc018669200525c6f11542ae97dac(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGlobalReplicationGroup.RegionalConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d920057dfab2caaf1f89662c7570bd431d43559ca99a0846f6d46dae7369f9eb(
    *,
    replication_group_id: typing.Optional[builtins.str] = None,
    replication_group_region: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeaef8528e85da7f76144633387f423a352cf7a00b93f64470683d2a67c7bd57(
    *,
    replication_group_id: typing.Optional[builtins.str] = None,
    replication_group_region: typing.Optional[builtins.str] = None,
    resharding_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGlobalReplicationGroup.ReshardingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5a9e68366040209fa4fb9f8e50eff4e9b1ae9ea0da836153a13ff22b2202ad5(
    *,
    node_group_id: typing.Optional[builtins.str] = None,
    preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265dda90953e13518f66b5357e00050b92a09e4dfb295f7b765b5b5d55951ace(
    *,
    members: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty, typing.Dict[builtins.str, typing.Any]]]]],
    automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cache_node_type: typing.Optional[builtins.str] = None,
    cache_parameter_group_name: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    global_node_group_count: typing.Optional[jsii.Number] = None,
    global_replication_group_description: typing.Optional[builtins.str] = None,
    global_replication_group_id_suffix: typing.Optional[builtins.str] = None,
    regional_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGlobalReplicationGroup.RegionalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f3b322f4ea3d0cc63e18e1b285cc656e6d789289e29668aa7acce95fdb892d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cache_parameter_group_family: builtins.str,
    description: builtins.str,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4df9ac5cd73e00bfbbdce4db59984040d76705d9fed6f259b98c08569946c00b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2ce285a081ee552c80c88bf27503daba85ce16849e3599360c22241be30e55e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c887b1c7836e155f15fbcb98f5393a2b92b4a33873814732bea60f4f1b225f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__131595ea286a946147c38535eb5fcf0537b68b2132e909e191998a1e3f21d5f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad995d05e00fe4d7296f16776a975d33eb5d75180391440607e5d71ae30d1f08(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f00caea2443ab3a4d0d9d2f1836e1d360d238f759643e2af050c00c5ea4f3efb(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56da2ad187e00defe2d3a6812e7eea3611b1990da4526952f58e2f80cfa1c36b(
    *,
    cache_parameter_group_family: builtins.str,
    description: builtins.str,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be27fffa79ab6bf194b2d0d4de1313299c709e45a12e57a99e85fb26cf0e5f50(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    replication_group_description: builtins.str,
    at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    auth_token: typing.Optional[builtins.str] = None,
    automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cache_node_type: typing.Optional[builtins.str] = None,
    cache_parameter_group_name: typing.Optional[builtins.str] = None,
    cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    cache_subnet_group_name: typing.Optional[builtins.str] = None,
    cluster_mode: typing.Optional[builtins.str] = None,
    data_tiering_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    engine: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    global_replication_group_id: typing.Optional[builtins.str] = None,
    ip_discovery: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_delivery_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.LogDeliveryConfigurationRequestProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    multi_az_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    network_type: typing.Optional[builtins.str] = None,
    node_group_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.NodeGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    notification_topic_arn: typing.Optional[builtins.str] = None,
    num_cache_clusters: typing.Optional[jsii.Number] = None,
    num_node_groups: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_cache_cluster_a_zs: typing.Optional[typing.Sequence[builtins.str]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    primary_cluster_id: typing.Optional[builtins.str] = None,
    replicas_per_node_group: typing.Optional[jsii.Number] = None,
    replication_group_id: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    snapshotting_cluster_id: typing.Optional[builtins.str] = None,
    snapshot_window: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    transit_encryption_mode: typing.Optional[builtins.str] = None,
    user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d988a8a188908fd1e785a707cc68edf28a1ba53bd404b971490bcb7100e29a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e69031f1e65767cd224fc587374f20072359815a32df0eaa95f2428da70c2e0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c907ced1d032518ebc8883a36eb0edf181bc2da76408e75eb584c864b5fefc9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa546aa730ad1a4db1a42606474b6045ffc32ec777b50d6ba31f3dbdab3a48df(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5f85de07d00909dedcebd441b02e117efc2077a1e3d87f54c5a27f5206a2f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b966eb1df615199d14bbc7fd9f3b39c9f4709837783a9a97f8945e6c623dc56d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b4cffb8c5e43d27133f190ebeba6d314ad935e730a8628bef824306d4d6356(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed33482a5f3a397014d26a736ced8371cfd5f7dcf12071c4629c9100b4d0c3cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c80def577fbbf2efb0e92fb3bd6946c8ffca559bbc2222843991c0c59a8e05(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a35e383106650eefc6c3b806779d5aa3ad36ed505bd7313e11d94c5942d9c7b1(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b7e9b4af342ce71884b10c5713679cc1987727399ee466ef6c6e86653dcb21(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843c2d711df69b9b78c5297321a7377fd4d364b0b8b228ae665fcbdffa0084f2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4366a0fcdd44e261b8f1399689f3ac4bb635223727a5c70ecced2835cb18c15(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43efae7f07eb2d768b51436a460dd83ae934b30a7e7cc3f3b825cfd6e5ece68d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5337b37fc62ed19c046ae6e4e85b8fe97cdcd4eb2fd571decbfe563e2f9bbcf5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf74e5c2399e48c43d257f5ef3f61c24fce45668db9e5f6d537ce076f935f780(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea227ab737c3768eb9268ca4b7aad2a651bd5c80b060dd89e792f94c91fce7f1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dda541c47a7be91143fbe227b05e172ef4b46d5657366c1ffff09fbb9c0c5c7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6abdf1dfe7ce2cb6bd74fcf5e71f8d01354d2ebe730f2f8811c7cca3c29115c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnReplicationGroup.LogDeliveryConfigurationRequestProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ea9e8732e19a78795fe185be2450c918f0ad9505938ce18be98a47595e698f(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83454ca7ec99c5872b43df5ecd3a494e042cd44f7b50d58f4bf1e6e8b660215d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__063232de740d4c4cf752ba9532e0b046f204c4d85a17ea560f3688d5c78d5126(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnReplicationGroup.NodeGroupConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afad0ef82bb9acf280293dc8234bcbfb68b0aee8e38631e29e8b0f5c0edf6436(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3effd0ee3abc632945998cd5c58c40c2e61c166d48aeaff02c46cb4fe172fa68(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06693a02af2ea54d169b325b01dbc6b4f0fac1ded78e060c7120b709bf82ffd1(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77a4995911ee86ef96fab9b8d7683bd6b21726901334b6e0f5b1cd65c358352(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b98acbb3854c5584ac0d1b3f958aaab9acda203560a42576b7da590dd3efbb(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f06ffee046ee6aaf7c317d0ec481f014335323a835adf240ab1d537b192e36e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6512d6a9d409265e09a0a87e261fcba517621c20846549f6b30152801b2e3dee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cf71395d4de3cd4ca74d713e8070b525f88cd095892c0b97826bec127eea35d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e382d1b245c43974606107b80af8da9323e7d5a4ec30a874e85fd0d8383a979(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4bf0b926d5ed122589bca93144684bbbc765d5b48d2b43dc65e20ac75999870(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__402bbedebe63e1639250243d98564e9d2abaf2ea4be044a6e822afb9573ba83b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf64b55611f1dcd1385926cc1344d345fe6bb1210d40fc47034fe65bbdb3da34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca3b912d486d6471befbdcc0a4f6371d9c6d4fce14489c5c146523f37b67d03(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04e859b223e2f5a28ae2572ed09bf8cef9bbf00ed7571a437a364307bc63f338(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eca3a583f11466198815da8e0f733144c677e601f7fbc08ff2f53b0f251ce1c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd34df081f3adeec74e0b10c42a2c6579d5328d707ac88af6a4c22338f3c9035(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af0273d0b69e8bd3f65054f8d56651f1f9d315c9e60fa092dd4b8e4e8844e85(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e42c150539724e50fcb5c3e35f3cc6d260890eb3e8dedeaaac606a9539b75a56(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e181f655740159c1c7f60264045e188418edbe6d092594dbf15cce26263f01(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d33b9d3b5876c576f6687dd170e2161cb8acc01f4eeae0ae299a3a279b24467d(
    *,
    log_group: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6393b162360e08ba34e1e81372da9a50f39c9a0cc3e234d4de5535a2bb554fe6(
    *,
    cloud_watch_logs_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_firehose_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdcf378b5d4262b2df61cdeb35e6e804ff747472fc30e69109cb47a8aed0fbad(
    *,
    delivery_stream: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9ff12d17e85eb513ea31c4f6d81c908ca6208f607b8673aa2d7c7e0a9fe4706(
    *,
    destination_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.DestinationDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    destination_type: builtins.str,
    log_format: builtins.str,
    log_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b71a634ea38148f00c55a6a55d2a07c87ecfd6d6fbdd46f7603a23c08772dfb5(
    *,
    node_group_id: typing.Optional[builtins.str] = None,
    primary_availability_zone: typing.Optional[builtins.str] = None,
    replica_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
    slots: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8dbf3d422d5fea6e04cfbc10e81904d384dc2c210952911caaa5ab7eefa3a3d(
    *,
    replication_group_description: builtins.str,
    at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    auth_token: typing.Optional[builtins.str] = None,
    automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cache_node_type: typing.Optional[builtins.str] = None,
    cache_parameter_group_name: typing.Optional[builtins.str] = None,
    cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    cache_subnet_group_name: typing.Optional[builtins.str] = None,
    cluster_mode: typing.Optional[builtins.str] = None,
    data_tiering_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    engine: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    global_replication_group_id: typing.Optional[builtins.str] = None,
    ip_discovery: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_delivery_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.LogDeliveryConfigurationRequestProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    multi_az_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    network_type: typing.Optional[builtins.str] = None,
    node_group_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationGroup.NodeGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    notification_topic_arn: typing.Optional[builtins.str] = None,
    num_cache_clusters: typing.Optional[jsii.Number] = None,
    num_node_groups: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_cache_cluster_a_zs: typing.Optional[typing.Sequence[builtins.str]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    primary_cluster_id: typing.Optional[builtins.str] = None,
    replicas_per_node_group: typing.Optional[jsii.Number] = None,
    replication_group_id: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    snapshotting_cluster_id: typing.Optional[builtins.str] = None,
    snapshot_window: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    transit_encryption_mode: typing.Optional[builtins.str] = None,
    user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a123177a3bb81237f7f7f549a05ee3a5234df818c52d76546ff68a80c39ddaed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e59b6770093fdec8763d8d7b39b7d6466bc5e469d75d9f211e118781440edec1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb62adc1dfae487cca927c94c6b4ad1904c89719a572bef2994345a5d039ef0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a58aa3e47b676ffbd43668bc6e1d2c79b30df11d4e23ee80c4bdefdb1e2e460(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d0db95241a79cc90ce9ac36752f3ee20a66c04797f992822d1387e95ab0d3dc(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9fec253fa52a5ea3d4371f10b9ad50ca4993c9f60ac895b0fef6575e1ced177(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cache_security_group_name: builtins.str,
    ec2_security_group_name: builtins.str,
    ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce56443f7fa86a2c85da65d4fe1945a48bacd9a42111d28731fb9be03ebd3098(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69468cc5d27117dacd7aa3deb279d35fa03dabbd826bb6290d084f5b9f359705(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__439c20ee90e3a27653353314240f9637cdf95b53b1cd23e4aaec9d21b5d568c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0abb1fc13eea94e08b452064202975643af441a003c80b20a2dd84ee151b33ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69c9ced7a396b23c621165b2be40f28744ce4080f376459c1fec4f135a9d8a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbdf58872e9544b14b7cd19f9a883c3e1c2fcad8d855805f476f813cea0882e6(
    *,
    cache_security_group_name: builtins.str,
    ec2_security_group_name: builtins.str,
    ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__188ce8daf68355e05c89377b875f68542bb67a42ce5afc30df7473e1420abce9(
    *,
    description: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f204522453489e8198605933b3b942062e9c202c1099285663a7d772a3e94ba7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    engine: builtins.str,
    serverless_cache_name: builtins.str,
    cache_usage_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.CacheUsageLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    daily_snapshot_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    final_snapshot_name: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    major_engine_version: typing.Optional[builtins.str] = None,
    reader_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arns_to_restore: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7012476fc1dcf708502c3a40812f4ced90af74571a021bfa5091171717291b4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2123590dc90b36de3e39588015991928ac6ad2f7a93f300e83a897fbcd82d5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db64b6c69d929608090194c9d83216677c91f2080ab6d4f59737f93d2e492503(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c553e861158121ce7a0545fdcf543b7615bf13ddc0bbd93cb52e72e27acd09d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90cce9924849d9cc9e8f897f51cd6502787503e9fe6f9c0b146111c1c445aa8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.CacheUsageLimitsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4072f21fb5867be241aa2784268fe8e3463d10cd511019b8f3599ec5d5c2cd2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6ee9bbb29fab9e6641d85980e882cc3db988c37421cc1d376048cdf7dfdcb06(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf26818381fc6b07f8a2615330e14830cc8722c7bea067d80e6017ceab59af6a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.EndpointProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62246ee954ddcb344e45c430ef7cbe75d5a3b692a00d6e538baa399c5cab349a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8cc8a3d052be3fabfdfe466bf509434f5707efc6a6dcd0770cc1a1b97e07a80(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618e7242f4c8d6ea2092e93310602455166596d1a96215a2fb33d826bbe5fd29(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e3145e59d2b03c61c29dd7fc18ce6d775561dcfa018b131c81d1f6e06fcd65(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServerlessCache.EndpointProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96776cfdc2836177648dc34a892d382e760b03e46d603807886c25a9fc1d103(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e490a4ceeec73f3d373a179650cfec51a7cf58d7c4e7f5b06544dd1a2df316(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fe4130c8869d67e8891f2bbbc10c149c15af0b801a4c9393fe4b4bcc848e3f0(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca2b56b13f3d8c09fd6a0e74df162e790fe2013d9a8d3d546b7b1aa5af8b507(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2054e990234791671dd0f6c1b491baebdfaaa093bc590373b8cbe5d6a7dec291(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b592bfec207d3f2428902a54fb8adfacc60bdb7a83c47e12c1b4d76ac68444ff(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77ebaaf0b703f3ff0164d4845d37449699aec6cbe500ff6d63278a3a64427450(
    *,
    data_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.DataStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ecpu_per_second: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.ECPUPerSecondProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14470b22401430bce81195b8e644412f38b76011c8cab7fa8399081bd44b546d(
    *,
    unit: builtins.str,
    maximum: typing.Optional[jsii.Number] = None,
    minimum: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4a85c1f856007000025702b1b01488e1f0726e767adf52fbf709f88ed3720f1(
    *,
    maximum: typing.Optional[jsii.Number] = None,
    minimum: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e66cf1143a0bb8344a2f8dd0d18b42b664e7256d7ac1eb56ff9cab6b66fff5d5(
    *,
    address: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58b8c0bd8ed5d4d4b90b896e92a64fc113ba2b7b80dfa7075b8fad4b02f5886c(
    *,
    engine: builtins.str,
    serverless_cache_name: builtins.str,
    cache_usage_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.CacheUsageLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    daily_snapshot_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    final_snapshot_name: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    major_engine_version: typing.Optional[builtins.str] = None,
    reader_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServerlessCache.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arns_to_restore: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d31f960507f2c9e3587baf93d99fa25f2747d0865408ff081e5c5230bf44b04(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    cache_subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e74c02a4794273fd857125de793130ad00a35e7107b9a052fd9729c834e8c03(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c394e0da879e36e1158aa11a6d2a3848b9c833cd6c8b791f2a306dcd1d6bc39(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c5ab35ff7baba1205becdb157e37a43b2ffdb8d78b6a89812dec13e870110ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__406b48aa434500b28470efd76a3cfb00968662ddd966571565ba3c47788bd26d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26295a8a2dc7d2b6948d4efdcca51f3722ed36bec5ced2fbf24d774ea7b28163(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f6670815d10d752e7b16bcf0f681bfa6e802161e1b1eba4c63dd3a6d9846719(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b45c5c5c7c2f90c8c0fc4304349cfb95eff57e46669706a32a0b5b73fc2139(
    *,
    description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    cache_subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3690e849b3e5bf7f482e77652d683906b1133738dbc72aea39d0186729f84fd0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    engine: builtins.str,
    user_id: builtins.str,
    user_name: builtins.str,
    access_string: typing.Optional[builtins.str] = None,
    authentication_mode: typing.Any = None,
    no_password_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8027fd2dc9d1d9c383f787790509ce0a31493b0c5928b63706caf8cd2096acf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d2c24ac7e99a31a4e0d4135ea5447976f3d5233d9d0e77c498d74df49e859a5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74df73fc62abe9fa1155cea79085975215d2cc3a30983f4b784d74b2d8dafec0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b8eb0ca4560239c33c66aef6a7b3087bdea40d47268790b66085c594bb3ae1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82b6eed2d66e57932003ce447ee4a3219513ca0c8161fae47c096809d764af5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb7549e3e6dbe94afa410bffc87623817e4cb26f90efb581b9a8d6dfcea71b64(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a67425ea4c8dcb1628c0ebb391eb9d3ca8fd07b5c6306f039cb531a05565d4(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dc0162c51746ac68f8e6c599bd425920aec49776f251d176073c998647b402e(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd01953837fe46505e356e5e6f503c48a5037161ed165b5dfa3d2124c10bf225(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda53c926e8acd673280fda87bee7f7bcf1def006ab1883b24a6a077e43b7449(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec04d0248d22cdd45ac6431c550d1bdf03740a43412b686373b189e770fd0d91(
    *,
    type: builtins.str,
    passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc142924e04b2348d54a42d3f1272d7a6d9f1886d6e9133f1a0ed55abcda10a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    engine: builtins.str,
    user_group_id: builtins.str,
    user_ids: typing.Sequence[builtins.str],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a5d03fb1ca11359d2e12cf9829f5c78e442be6d3175a5f56c52bd5c800742a5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450a9b959ab13e887b9b352f9708de268fb109cca3789dc4eeea0989d1c33d28(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e431968f516bc728e154bbd117b40cd38af16bf361c399b85db4f54094ac994(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2d97633ea9a0c04b7eee81db8315453f4d5e7436b511bc476886df00a72145(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537c18038663c50194ccf261d54d663088b0bde017663b14868ca50759a76109(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f91d8988fa4ff59ae0f0f6e912aaa87f88df9ee98afddb86934a2611c1d0da39(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__781d57350a7876de81adb05f4b5f1c6a6733fe48684f64bf990d3377377290ab(
    *,
    engine: builtins.str,
    user_group_id: builtins.str,
    user_ids: typing.Sequence[builtins.str],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd58f3eed78cb4ce0cff0a0f48e20670425d5891d9c8b2bd0b6006a78cfe7ab5(
    *,
    engine: builtins.str,
    user_id: builtins.str,
    user_name: builtins.str,
    access_string: typing.Optional[builtins.str] = None,
    authentication_mode: typing.Any = None,
    no_password_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
