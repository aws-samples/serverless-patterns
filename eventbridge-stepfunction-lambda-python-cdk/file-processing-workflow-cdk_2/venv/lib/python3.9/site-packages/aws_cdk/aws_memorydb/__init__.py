'''
# AWS::MemoryDB Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_memorydb as memorydb
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MemoryDB construct libraries](https://constructs.dev/search?q=memorydb)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MemoryDB resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MemoryDB.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MemoryDB](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MemoryDB.html).

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
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnACL(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_memorydb.CfnACL",
):
    '''Specifies an Access Control List.

    For more information, see `Authenticating users with Access Contol Lists (ACLs) <https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_memorydb as memorydb
        
        cfn_aCL = memorydb.CfnACL(self, "MyCfnACL",
            acl_name="aclName",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_names=["userNames"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        acl_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param acl_name: The name of the Access Control List.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param user_names: The list of users that belong to the Access Control List.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9484fd1d572431ae11bb12955c007dddcddc12b2666a5855747b0a1acb261875)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnACLProps(acl_name=acl_name, tags=tags, user_names=user_names)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc6a711d3d8a9748de4a3ff47996a84e749aad94d25a5dda512b2da78cc1038)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4acff847fe3f6b78cef61522d272a00a00cc6e9e52bdeb53d457a7ef9445111)
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
        '''When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the Access Control List, such as ``arn:aws:memorydb:us-east-1:123456789012:acl/my-acl``.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Indicates ACL status.

        *Valid values* : ``creating`` | ``active`` | ``modifying`` | ``deleting``

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
    @jsii.member(jsii_name="aclName")
    def acl_name(self) -> builtins.str:
        '''The name of the Access Control List.'''
        return typing.cast(builtins.str, jsii.get(self, "aclName"))

    @acl_name.setter
    def acl_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f59d44321ba67be64a21cd7280a133eb5eafce74ce555870a7e52de3bbadcbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aclName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19dfb38b66bc6a76c22f50b7a62a4979bd2a681026ccd6e3e50920eb6c5cf6f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="userNames")
    def user_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of users that belong to the Access Control List.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "userNames"))

    @user_names.setter
    def user_names(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f042edf87d33b30ef4ba034b5cf40ac2a7656eb3997bb3b2744a40f2166de66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userNames", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_memorydb.CfnACLProps",
    jsii_struct_bases=[],
    name_mapping={"acl_name": "aclName", "tags": "tags", "user_names": "userNames"},
)
class CfnACLProps:
    def __init__(
        self,
        *,
        acl_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnACL``.

        :param acl_name: The name of the Access Control List.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param user_names: The list of users that belong to the Access Control List.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_memorydb as memorydb
            
            cfn_aCLProps = memorydb.CfnACLProps(
                acl_name="aclName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_names=["userNames"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__848e1428f1884a88285ca152ff429f50733c57eca32906e1deaae2e8b3f4cd9a)
            check_type(argname="argument acl_name", value=acl_name, expected_type=type_hints["acl_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_names", value=user_names, expected_type=type_hints["user_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acl_name": acl_name,
        }
        if tags is not None:
            self._values["tags"] = tags
        if user_names is not None:
            self._values["user_names"] = user_names

    @builtins.property
    def acl_name(self) -> builtins.str:
        '''The name of the Access Control List.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-aclname
        '''
        result = self._values.get("acl_name")
        assert result is not None, "Required property 'acl_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of users that belong to the Access Control List.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-usernames
        '''
        result = self._values.get("user_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnACLProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_memorydb.CfnCluster",
):
    '''Specifies a cluster .

    All nodes in the cluster run the same protocol-compliant engine software.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_memorydb as memorydb
        
        cfn_cluster = memorydb.CfnCluster(self, "MyCfnCluster",
            acl_name="aclName",
            cluster_name="clusterName",
            node_type="nodeType",
        
            # the properties below are optional
            auto_minor_version_upgrade=False,
            cluster_endpoint=memorydb.CfnCluster.EndpointProperty(
                address="address",
                port=123
            ),
            data_tiering="dataTiering",
            description="description",
            engine_version="engineVersion",
            final_snapshot_name="finalSnapshotName",
            kms_key_id="kmsKeyId",
            maintenance_window="maintenanceWindow",
            num_replicas_per_shard=123,
            num_shards=123,
            parameter_group_name="parameterGroupName",
            port=123,
            security_group_ids=["securityGroupIds"],
            snapshot_arns=["snapshotArns"],
            snapshot_name="snapshotName",
            snapshot_retention_limit=123,
            snapshot_window="snapshotWindow",
            sns_topic_arn="snsTopicArn",
            sns_topic_status="snsTopicStatus",
            subnet_group_name="subnetGroupName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            tls_enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        acl_name: builtins.str,
        cluster_name: builtins.str,
        node_type: builtins.str,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cluster_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        data_tiering: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[builtins.str] = None,
        num_replicas_per_shard: typing.Optional[jsii.Number] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        sns_topic_status: typing.Optional[builtins.str] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        tls_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param acl_name: The name of the Access Control List to associate with the cluster .
        :param cluster_name: The name of the cluster .
        :param node_type: The cluster 's node type.
        :param auto_minor_version_upgrade: When set to true, the cluster will automatically receive minor engine version upgrades after launch.
        :param cluster_endpoint: The cluster 's configuration endpoint.
        :param data_tiering: Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see `Data tiering <https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html>`_ .
        :param description: A description of the cluster .
        :param engine_version: The Redis engine version used by the cluster .
        :param final_snapshot_name: The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.
        :param kms_key_id: The ID of the KMS key used to encrypt the cluster .
        :param maintenance_window: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ``ddd:hh24:mi-ddd:hh24:mi`` (24H Clock UTC). The minimum maintenance window is a 60 minute period. *Pattern* : ``ddd:hh24:mi-ddd:hh24:mi``
        :param num_replicas_per_shard: The number of replicas to apply to each shard. *Default value* : ``1`` *Maximum value* : ``5``
        :param num_shards: The number of shards in the cluster .
        :param parameter_group_name: The name of the parameter group used by the cluster .
        :param port: The port used by the cluster .
        :param security_group_ids: A list of security group names to associate with this cluster .
        :param snapshot_arns: A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster . The Amazon S3 object name in the ARN cannot contain any commas.
        :param snapshot_name: The name of a snapshot from which to restore data into the new cluster . The snapshot status changes to restoring while the new cluster is being created.
        :param snapshot_retention_limit: The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
        :param snapshot_window: The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard. Example: 05:00-09:00 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.
        :param sns_topic_arn: When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the SNS topic, such as ``arn:aws:memorydb:us-east-1:123456789012:mySNSTopic``.
        :param sns_topic_status: The SNS topic must be in Active status to receive notifications.
        :param subnet_group_name: The name of the subnet group used by the cluster .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param tls_enabled: A flag to indicate if In-transit encryption is enabled.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2be3fd9830386937ed856721b0282cb7c4bcfb48ca212a069ae310ef4612235b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            acl_name=acl_name,
            cluster_name=cluster_name,
            node_type=node_type,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            cluster_endpoint=cluster_endpoint,
            data_tiering=data_tiering,
            description=description,
            engine_version=engine_version,
            final_snapshot_name=final_snapshot_name,
            kms_key_id=kms_key_id,
            maintenance_window=maintenance_window,
            num_replicas_per_shard=num_replicas_per_shard,
            num_shards=num_shards,
            parameter_group_name=parameter_group_name,
            port=port,
            security_group_ids=security_group_ids,
            snapshot_arns=snapshot_arns,
            snapshot_name=snapshot_name,
            snapshot_retention_limit=snapshot_retention_limit,
            snapshot_window=snapshot_window,
            sns_topic_arn=sns_topic_arn,
            sns_topic_status=sns_topic_status,
            subnet_group_name=subnet_group_name,
            tags=tags,
            tls_enabled=tls_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76cb969e4927216a06a434c27c39efb5cdd385529b9ea5e0319d2951238e010e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c01db201d255a330f5adbc767e7d8534c144fe92bcc19d9c60759ff18a74cd98)
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
        '''When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the cluster , such as ``arn:aws:memorydb:us-east-1:123456789012:cluster/my-cluster``.

        :cloudformationAttribute: ARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterEndpointAddress")
    def attr_cluster_endpoint_address(self) -> builtins.str:
        '''The address of the cluster 's configuration endpoint.

        :cloudformationAttribute: ClusterEndpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterEndpointPort")
    def attr_cluster_endpoint_port(self) -> jsii.Number:
        '''The port used by the cluster configuration endpoint.

        :cloudformationAttribute: ClusterEndpoint.Port
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrClusterEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrParameterGroupStatus")
    def attr_parameter_group_status(self) -> builtins.str:
        '''The status of the parameter group used by the cluster , for example ``active`` or ``applying`` .

        :cloudformationAttribute: ParameterGroupStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrParameterGroupStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the cluster.

        For example, 'available', 'updating' or 'creating'.

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
    @jsii.member(jsii_name="aclName")
    def acl_name(self) -> builtins.str:
        '''The name of the Access Control List to associate with the cluster .'''
        return typing.cast(builtins.str, jsii.get(self, "aclName"))

    @acl_name.setter
    def acl_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c3c2eddecf623588f80ccc7dc138eb7bbc48ab8fb8408ae9fce592041db4684)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aclName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The name of the cluster .'''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa662ca2d6af7f3a9fcaf06f14705152ff3589c084e25ab2f001d9e1b25c26d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> builtins.str:
        '''The cluster 's node type.'''
        return typing.cast(builtins.str, jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaa925a9d7f42afc3b5dfd02b1e7d763fb4a92eaa811c0f438b6b77f5b2d2d16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When set to true, the cluster will automatically receive minor engine version upgrades after launch.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85ceb7f4779e4cc3158fd10ae0f789f977bf4ec7b305427de026b71410314aa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EndpointProperty"]]:
        '''The cluster 's configuration endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EndpointProperty"]], jsii.get(self, "clusterEndpoint"))

    @cluster_endpoint.setter
    def cluster_endpoint(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EndpointProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cb933d0258a10b86325bdd089031bbb07512679b44ad9da34f9d222d2a6f441)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="dataTiering")
    def data_tiering(self) -> typing.Optional[builtins.str]:
        '''Enables data tiering.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTiering"))

    @data_tiering.setter
    def data_tiering(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10d5c055bea0f63e6e3a2941e61801b460bb5413a94982bc6c27b2009874a78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTiering", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the cluster .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53812133543a07114ef48993753a17493cf0eaec35b4f165d5b5360b4c26b52f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The Redis engine version used by the cluster .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__169ccd9bb3c17f7e26324bbd84534aada6e77306d49160dd24968619a98599f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotName")
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The user-supplied name of a final cluster snapshot.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "finalSnapshotName"))

    @final_snapshot_name.setter
    def final_snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__301d4a99b6e66b0220c0a2c677e41494ec8f873a343c7550ef2a5a37c2b926fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key used to encrypt the cluster .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a09adc41454c2729b7ba3708a53bab49bfe2b1339006a09bcdd1059df89bb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which maintenance on the cluster is performed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceWindow"))

    @maintenance_window.setter
    def maintenance_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09056b85563d6a2905d89569ae90fbdb30eac108e48fcbb7dd5f0ebd2fadb818)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="numReplicasPerShard")
    def num_replicas_per_shard(self) -> typing.Optional[jsii.Number]:
        '''The number of replicas to apply to each shard.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numReplicasPerShard"))

    @num_replicas_per_shard.setter
    def num_replicas_per_shard(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479de98a506cf9095cbe7cc894a5d9900271b75b5ba2f28140084d5f265184a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numReplicasPerShard", value)

    @builtins.property
    @jsii.member(jsii_name="numShards")
    def num_shards(self) -> typing.Optional[jsii.Number]:
        '''The number of shards in the cluster .'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numShards"))

    @num_shards.setter
    def num_shards(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9135b8b8321239dd0eec70d6b0b8e9c9786b7f31b39fca12acff646ca5ac847a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numShards", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group used by the cluster .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterGroupName"))

    @parameter_group_name.setter
    def parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afe7bb6b934e8c26f66b356ef270e262cafc5cb83f3ccd7f2c0e73e7a8c53a86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port used by the cluster .'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__514c944046b7e1b4d74e9f68444e13be7441e98d16292246e9e63d3a03acf09e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group names to associate with this cluster .'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c15744036c88b29c766bdf4d57428776ee376a9c3a84a09d0d2b17f1691ce873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotArns")
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snapshotArns"))

    @snapshot_arns.setter
    def snapshot_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8318d1f21d46a1ae1d8dd7ef1d3bffaf1187d17aa4b3e86a78283323fcbc00ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotArns", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of a snapshot from which to restore data into the new cluster .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__804f6c88ce3d1f28a2ee2674d669c579358fa826656fb307dfb51d0218e29253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which MemoryDB retains automatic snapshots before deleting them.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotRetentionLimit"))

    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a974ab4488e4f73743ed4fde25eaf3834528b3a7c7cbaec76bc82aa64b3f38f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotRetentionLimit", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotWindow")
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotWindow"))

    @snapshot_window.setter
    def snapshot_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25236d19ef16b48436cefd0501c036250a6efde6040b75c7c137f53c18680083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotWindow", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the SNS topic, such as ``arn:aws:memorydb:us-east-1:123456789012:mySNSTopic``.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b881a509aa28847923e821bbd39f9fe72db3a10833d11edf261679abeffffcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicStatus")
    def sns_topic_status(self) -> typing.Optional[builtins.str]:
        '''The SNS topic must be in Active status to receive notifications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicStatus"))

    @sns_topic_status.setter
    def sns_topic_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537157a3978a51b06802ba8f249faf9b7508885f9892ec03421fcbb0b008a92c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicStatus", value)

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subnet group used by the cluster .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetGroupName"))

    @subnet_group_name.setter
    def subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ec6f6b0257f531ddbc438480683e55ab4636f2133f40c6730f1fef7235204e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb518ff45629b2fc5f7488c33f7e4de652dc27f32c98792c355068710db9cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="tlsEnabled")
    def tls_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag to indicate if In-transit encryption is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "tlsEnabled"))

    @tls_enabled.setter
    def tls_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c35c0a09eb3a078c7c40fabc044eb0877fe7280b70079614ef1383d482cdaa0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsEnabled", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_memorydb.CfnCluster.EndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "port": "port"},
    )
    class EndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Represents the information required for client programs to connect to the cluster and its nodes.

            :param address: The DNS hostname of the node.
            :param port: The port number that the engine is listening on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_memorydb as memorydb
                
                endpoint_property = memorydb.CfnCluster.EndpointProperty(
                    address="address",
                    port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a97cbfefa1a4fe0796786c02815b29787b8019f1c83531b4338dd5b4d2c2ddbd)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The DNS hostname of the node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html#cfn-memorydb-cluster-endpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port number that the engine is listening on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html#cfn-memorydb-cluster-endpoint-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_memorydb.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "acl_name": "aclName",
        "cluster_name": "clusterName",
        "node_type": "nodeType",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "cluster_endpoint": "clusterEndpoint",
        "data_tiering": "dataTiering",
        "description": "description",
        "engine_version": "engineVersion",
        "final_snapshot_name": "finalSnapshotName",
        "kms_key_id": "kmsKeyId",
        "maintenance_window": "maintenanceWindow",
        "num_replicas_per_shard": "numReplicasPerShard",
        "num_shards": "numShards",
        "parameter_group_name": "parameterGroupName",
        "port": "port",
        "security_group_ids": "securityGroupIds",
        "snapshot_arns": "snapshotArns",
        "snapshot_name": "snapshotName",
        "snapshot_retention_limit": "snapshotRetentionLimit",
        "snapshot_window": "snapshotWindow",
        "sns_topic_arn": "snsTopicArn",
        "sns_topic_status": "snsTopicStatus",
        "subnet_group_name": "subnetGroupName",
        "tags": "tags",
        "tls_enabled": "tlsEnabled",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        acl_name: builtins.str,
        cluster_name: builtins.str,
        node_type: builtins.str,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cluster_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        data_tiering: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[builtins.str] = None,
        num_replicas_per_shard: typing.Optional[jsii.Number] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        sns_topic_status: typing.Optional[builtins.str] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        tls_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param acl_name: The name of the Access Control List to associate with the cluster .
        :param cluster_name: The name of the cluster .
        :param node_type: The cluster 's node type.
        :param auto_minor_version_upgrade: When set to true, the cluster will automatically receive minor engine version upgrades after launch.
        :param cluster_endpoint: The cluster 's configuration endpoint.
        :param data_tiering: Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see `Data tiering <https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html>`_ .
        :param description: A description of the cluster .
        :param engine_version: The Redis engine version used by the cluster .
        :param final_snapshot_name: The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.
        :param kms_key_id: The ID of the KMS key used to encrypt the cluster .
        :param maintenance_window: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ``ddd:hh24:mi-ddd:hh24:mi`` (24H Clock UTC). The minimum maintenance window is a 60 minute period. *Pattern* : ``ddd:hh24:mi-ddd:hh24:mi``
        :param num_replicas_per_shard: The number of replicas to apply to each shard. *Default value* : ``1`` *Maximum value* : ``5``
        :param num_shards: The number of shards in the cluster .
        :param parameter_group_name: The name of the parameter group used by the cluster .
        :param port: The port used by the cluster .
        :param security_group_ids: A list of security group names to associate with this cluster .
        :param snapshot_arns: A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster . The Amazon S3 object name in the ARN cannot contain any commas.
        :param snapshot_name: The name of a snapshot from which to restore data into the new cluster . The snapshot status changes to restoring while the new cluster is being created.
        :param snapshot_retention_limit: The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
        :param snapshot_window: The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard. Example: 05:00-09:00 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.
        :param sns_topic_arn: When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the SNS topic, such as ``arn:aws:memorydb:us-east-1:123456789012:mySNSTopic``.
        :param sns_topic_status: The SNS topic must be in Active status to receive notifications.
        :param subnet_group_name: The name of the subnet group used by the cluster .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param tls_enabled: A flag to indicate if In-transit encryption is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_memorydb as memorydb
            
            cfn_cluster_props = memorydb.CfnClusterProps(
                acl_name="aclName",
                cluster_name="clusterName",
                node_type="nodeType",
            
                # the properties below are optional
                auto_minor_version_upgrade=False,
                cluster_endpoint=memorydb.CfnCluster.EndpointProperty(
                    address="address",
                    port=123
                ),
                data_tiering="dataTiering",
                description="description",
                engine_version="engineVersion",
                final_snapshot_name="finalSnapshotName",
                kms_key_id="kmsKeyId",
                maintenance_window="maintenanceWindow",
                num_replicas_per_shard=123,
                num_shards=123,
                parameter_group_name="parameterGroupName",
                port=123,
                security_group_ids=["securityGroupIds"],
                snapshot_arns=["snapshotArns"],
                snapshot_name="snapshotName",
                snapshot_retention_limit=123,
                snapshot_window="snapshotWindow",
                sns_topic_arn="snsTopicArn",
                sns_topic_status="snsTopicStatus",
                subnet_group_name="subnetGroupName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                tls_enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e34c4b7ef2f8328b2d19e6f768b6f44c55efea16824463c1ed0f3497299f1e8)
            check_type(argname="argument acl_name", value=acl_name, expected_type=type_hints["acl_name"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument cluster_endpoint", value=cluster_endpoint, expected_type=type_hints["cluster_endpoint"])
            check_type(argname="argument data_tiering", value=data_tiering, expected_type=type_hints["data_tiering"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument final_snapshot_name", value=final_snapshot_name, expected_type=type_hints["final_snapshot_name"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument num_replicas_per_shard", value=num_replicas_per_shard, expected_type=type_hints["num_replicas_per_shard"])
            check_type(argname="argument num_shards", value=num_shards, expected_type=type_hints["num_shards"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument snapshot_arns", value=snapshot_arns, expected_type=type_hints["snapshot_arns"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument snapshot_retention_limit", value=snapshot_retention_limit, expected_type=type_hints["snapshot_retention_limit"])
            check_type(argname="argument snapshot_window", value=snapshot_window, expected_type=type_hints["snapshot_window"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument sns_topic_status", value=sns_topic_status, expected_type=type_hints["sns_topic_status"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tls_enabled", value=tls_enabled, expected_type=type_hints["tls_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acl_name": acl_name,
            "cluster_name": cluster_name,
            "node_type": node_type,
        }
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if cluster_endpoint is not None:
            self._values["cluster_endpoint"] = cluster_endpoint
        if data_tiering is not None:
            self._values["data_tiering"] = data_tiering
        if description is not None:
            self._values["description"] = description
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if final_snapshot_name is not None:
            self._values["final_snapshot_name"] = final_snapshot_name
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if num_replicas_per_shard is not None:
            self._values["num_replicas_per_shard"] = num_replicas_per_shard
        if num_shards is not None:
            self._values["num_shards"] = num_shards
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name
        if port is not None:
            self._values["port"] = port
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if snapshot_arns is not None:
            self._values["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if snapshot_retention_limit is not None:
            self._values["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshot_window is not None:
            self._values["snapshot_window"] = snapshot_window
        if sns_topic_arn is not None:
            self._values["sns_topic_arn"] = sns_topic_arn
        if sns_topic_status is not None:
            self._values["sns_topic_status"] = sns_topic_status
        if subnet_group_name is not None:
            self._values["subnet_group_name"] = subnet_group_name
        if tags is not None:
            self._values["tags"] = tags
        if tls_enabled is not None:
            self._values["tls_enabled"] = tls_enabled

    @builtins.property
    def acl_name(self) -> builtins.str:
        '''The name of the Access Control List to associate with the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-aclname
        '''
        result = self._values.get("acl_name")
        assert result is not None, "Required property 'acl_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_type(self) -> builtins.str:
        '''The cluster 's node type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-nodetype
        '''
        result = self._values.get("node_type")
        assert result is not None, "Required property 'node_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When set to true, the cluster will automatically receive minor engine version upgrades after launch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def cluster_endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EndpointProperty]]:
        '''The cluster 's configuration endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-clusterendpoint
        '''
        result = self._values.get("cluster_endpoint")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EndpointProperty]], result)

    @builtins.property
    def data_tiering(self) -> typing.Optional[builtins.str]:
        '''Enables data tiering.

        Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see `Data tiering <https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-datatiering
        '''
        result = self._values.get("data_tiering")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The Redis engine version used by the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The user-supplied name of a final cluster snapshot.

        This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-finalsnapshotname
        '''
        result = self._values.get("final_snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key used to encrypt the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which maintenance on the cluster is performed.

        It is specified as a range in the format ``ddd:hh24:mi-ddd:hh24:mi`` (24H Clock UTC). The minimum maintenance window is a 60 minute period.

        *Pattern* : ``ddd:hh24:mi-ddd:hh24:mi``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-maintenancewindow
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_replicas_per_shard(self) -> typing.Optional[jsii.Number]:
        '''The number of replicas to apply to each shard.

        *Default value* : ``1``

        *Maximum value* : ``5``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-numreplicaspershard
        '''
        result = self._values.get("num_replicas_per_shard")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_shards(self) -> typing.Optional[jsii.Number]:
        '''The number of shards in the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-numshards
        '''
        result = self._values.get("num_shards")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group used by the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-parametergroupname
        '''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port used by the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group names to associate with this cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3.

        The snapshot files are used to populate the new cluster . The Amazon S3 object name in the ARN cannot contain any commas.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotarns
        '''
        result = self._values.get("snapshot_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of a snapshot from which to restore data into the new cluster .

        The snapshot status changes to restoring while the new cluster is being created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotname
        '''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which MemoryDB retains automatic snapshots before deleting them.

        For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotretentionlimit
        '''
        result = self._values.get("snapshot_retention_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard.

        Example: 05:00-09:00 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotwindow
        '''
        result = self._values.get("snapshot_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the SNS topic, such as ``arn:aws:memorydb:us-east-1:123456789012:mySNSTopic``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_status(self) -> typing.Optional[builtins.str]:
        '''The SNS topic must be in Active status to receive notifications.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snstopicstatus
        '''
        result = self._values.get("sns_topic_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subnet group used by the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-subnetgroupname
        '''
        result = self._values.get("subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def tls_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag to indicate if In-transit encryption is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-tlsenabled
        '''
        result = self._values.get("tls_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnParameterGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_memorydb.CfnParameterGroup",
):
    '''Specifies a new MemoryDB parameter group.

    A parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster . For more information, see `Configuring engine parameters using parameter groups <https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_memorydb as memorydb
        
        # parameters: Any
        
        cfn_parameter_group = memorydb.CfnParameterGroup(self, "MyCfnParameterGroup",
            family="family",
            parameter_group_name="parameterGroupName",
        
            # the properties below are optional
            description="description",
            parameters=parameters,
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
        family: builtins.str,
        parameter_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        parameters: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param family: The name of the parameter group family that this parameter group is compatible with.
        :param parameter_group_name: The name of the parameter group.
        :param description: A description of the parameter group.
        :param parameters: Returns the detailed parameter list for the parameter group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61162072dcce7ce6eaedeac288d04351f356c4501c7c00303d65b4be539cccbc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnParameterGroupProps(
            family=family,
            parameter_group_name=parameter_group_name,
            description=description,
            parameters=parameters,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7debe0fab7bb59dfcf15f4175e0f474c741a7964960dcbe155b0c5efbd1e09f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2849ec1f4498474dd393323e9addf1ae2cfcd99fed5607fae0ca019224dba56c)
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
        '''When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the parameter group, such as ``arn:aws:memorydb:us-east-1:123456789012:parametergroup/my-parameter-group``.

        :cloudformationAttribute: ARN
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
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        '''The name of the parameter group family that this parameter group is compatible with.'''
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2327ef6bcccd65d07bebc4ca23b1ce3d974747ae6a1bfc2e9bc11ca9d854f937)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''The name of the parameter group.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))

    @parameter_group_name.setter
    def parameter_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a79238fbac363251cbc8f245e05b8ca03c8a64c30125e3c5e45dde648dbc297c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the parameter group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feaa80d0267309e0293955eef98ea054278b3743ff2e229578818e3f85c41274)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''Returns the detailed parameter list for the parameter group.'''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__073902d6d488ba79aa229654bc7ef8389dbcbbfdc460e3df4c719249bbebc807)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c759a2a9795495d5bfdf5e24f113bc8b0166dd214c06992783c7263752a055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_memorydb.CfnParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "family": "family",
        "parameter_group_name": "parameterGroupName",
        "description": "description",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnParameterGroupProps:
    def __init__(
        self,
        *,
        family: builtins.str,
        parameter_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        parameters: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnParameterGroup``.

        :param family: The name of the parameter group family that this parameter group is compatible with.
        :param parameter_group_name: The name of the parameter group.
        :param description: A description of the parameter group.
        :param parameters: Returns the detailed parameter list for the parameter group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_memorydb as memorydb
            
            # parameters: Any
            
            cfn_parameter_group_props = memorydb.CfnParameterGroupProps(
                family="family",
                parameter_group_name="parameterGroupName",
            
                # the properties below are optional
                description="description",
                parameters=parameters,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be6b7833c24ddd9e0e309e9aaec933dfc2aeac5e49f40692fef7c14f6f5014f4)
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "family": family,
            "parameter_group_name": parameter_group_name,
        }
        if description is not None:
            self._values["description"] = description
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def family(self) -> builtins.str:
        '''The name of the parameter group family that this parameter group is compatible with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-family
        '''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_group_name(self) -> builtins.str:
        '''The name of the parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-parametergroupname
        '''
        result = self._values.get("parameter_group_name")
        assert result is not None, "Required property 'parameter_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''Returns the detailed parameter list for the parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-tags
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
class CfnSubnetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_memorydb.CfnSubnetGroup",
):
    '''Specifies a subnet group.

    A subnet group is a collection of subnets (typically private) that you can designate for your cluster s running in an Amazon Virtual Private Cloud (VPC) environment. When you create a cluster in an Amazon VPC , you must specify a subnet group. MemoryDB uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes. For more information, see `Subnets and subnet groups <https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_memorydb as memorydb
        
        cfn_subnet_group = memorydb.CfnSubnetGroup(self, "MyCfnSubnetGroup",
            subnet_group_name="subnetGroupName",
            subnet_ids=["subnetIds"],
        
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
        subnet_group_name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param subnet_group_name: The name of the subnet group to be used for the cluster .
        :param subnet_ids: A list of Amazon VPC subnet IDs for the subnet group.
        :param description: A description of the subnet group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b3dd027b7c51d2057be81ff17bfef3dbfbd3522767ca600f468a0d67ff1212e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubnetGroupProps(
            subnet_group_name=subnet_group_name,
            subnet_ids=subnet_ids,
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
            type_hints = typing.get_type_hints(_typecheckingstub__3145bbd399c6ddffdc2666544781343f26eb710bec8432513151b15f3216473b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__810a98a25d7c87dba6cc582df35eb455e83853a112a565ad67819e6c431f55d4)
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
        '''When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the subnet group, such as ``arn:aws:memorydb:us-east-1:123456789012:subnetgroup/my-subnet-group``.

        :cloudformationAttribute: ARN
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
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''The name of the subnet group to be used for the cluster .'''
        return typing.cast(builtins.str, jsii.get(self, "subnetGroupName"))

    @subnet_group_name.setter
    def subnet_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__303ad17b502aa93b1d211d7399cadc117544aadb4bee45b9c7c626efaa2319c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''A list of Amazon VPC subnet IDs for the subnet group.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72108b7d31976f953c8fa13d3a84ced5445347ca890c80e5a6da1fcaf1ccd5e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the subnet group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f54a9326815fe3c9ee63863201b4f4e885ed0e38d3788845c6f3ba942c143885)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__085e1da0c8228c03b5e87f741c2983f9ac01339c717a01009e150bd087ab288f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_memorydb.CfnSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "subnet_group_name": "subnetGroupName",
        "subnet_ids": "subnetIds",
        "description": "description",
        "tags": "tags",
    },
)
class CfnSubnetGroupProps:
    def __init__(
        self,
        *,
        subnet_group_name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubnetGroup``.

        :param subnet_group_name: The name of the subnet group to be used for the cluster .
        :param subnet_ids: A list of Amazon VPC subnet IDs for the subnet group.
        :param description: A description of the subnet group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_memorydb as memorydb
            
            cfn_subnet_group_props = memorydb.CfnSubnetGroupProps(
                subnet_group_name="subnetGroupName",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9355391d833b76afd63e1ea2e6ccb22ce04e5360c7352ef34ee698b3d16fa6c1)
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_group_name": subnet_group_name,
            "subnet_ids": subnet_ids,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def subnet_group_name(self) -> builtins.str:
        '''The name of the subnet group to be used for the cluster .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-subnetgroupname
        '''
        result = self._values.get("subnet_group_name")
        assert result is not None, "Required property 'subnet_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''A list of Amazon VPC subnet IDs for the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-tags
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
    jsii_type="aws-cdk-lib.aws_memorydb.CfnUser",
):
    '''Specifies a MemoryDB user.

    For more information, see `Authenticating users with Access Contol Lists (ACLs) <https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_memorydb as memorydb
        
        # authentication_mode: Any
        
        cfn_user = memorydb.CfnUser(self, "MyCfnUser",
            user_name="userName",
        
            # the properties below are optional
            access_string="accessString",
            authentication_mode=authentication_mode,
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
        user_name: builtins.str,
        access_string: typing.Optional[builtins.str] = None,
        authentication_mode: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param user_name: The name of the user.
        :param access_string: Access permissions string used for this user.
        :param authentication_mode: Denotes whether the user requires a password to authenticate. *Example:* ``mynewdbuser: Type: AWS::MemoryDB::User Properties: AccessString: on ~* &* +@all AuthenticationMode: Passwords: '1234567890123456' Type: password UserName: mynewdbuser AuthenticationMode: { "Passwords": ["1234567890123456"], "Type": "Password" }``
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52b4cd545a9f18f09898b753580c602cd4bd6e39c07e6a1f9e34f4fb928fb1dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            user_name=user_name,
            access_string=access_string,
            authentication_mode=authentication_mode,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c3bb35282143a9481bb5124eb626806569dc76eef119d8888c4373701fb4dd9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b8a18b12b6297a5b86c733efcf9f7c32315d3c27a2246b6428be84b10a621b1)
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
        '''When you pass the logical ID of this resource to the intrinsic ``Ref`` function, Ref returns the ARN of the user, such as ``arn:aws:memorydb:us-east-1:123456789012:user/user1``.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Indicates the user status.

        *Valid values* : ``active`` | ``modifying`` | ``deleting``

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
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The name of the user.'''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05f26f858b02f3b8efd6dc74353dbccbfa9f7dd93142545509b690f9bb6283d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5328fc755bfd9d9f30b338838f998fbf324c3bf12aaf33c79a23dedd4cb14f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessString", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationMode")
    def authentication_mode(self) -> typing.Any:
        '''Denotes whether the user requires a password to authenticate.'''
        return typing.cast(typing.Any, jsii.get(self, "authenticationMode"))

    @authentication_mode.setter
    def authentication_mode(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4785cb3838ab67f42c8f81c4a572fab61ddb9b328d731d82b7cd05ae96e1d834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationMode", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1caf541d919490fde818383ad7111c6060c95572004849b73f36d7935d02afe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_memorydb.CfnUser.AuthenticationModeProperty",
        jsii_struct_bases=[],
        name_mapping={"passwords": "passwords", "type": "type"},
    )
    class AuthenticationModeProperty:
        def __init__(
            self,
            *,
            passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param passwords: Passwords used for this user account. You can create up to two passwords for each user.
            :param type: Type of authentication strategy for this user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-user-authenticationmode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_memorydb as memorydb
                
                authentication_mode_property = memorydb.CfnUser.AuthenticationModeProperty(
                    passwords=["passwords"],
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7829a96cb7f6a4249d594f7be104bbd66d8afd40591a46c942d55bbdbbbe048c)
                check_type(argname="argument passwords", value=passwords, expected_type=type_hints["passwords"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if passwords is not None:
                self._values["passwords"] = passwords
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def passwords(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Passwords used for this user account.

            You can create up to two passwords for each user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-user-authenticationmode.html#cfn-memorydb-user-authenticationmode-passwords
            '''
            result = self._values.get("passwords")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''Type of authentication strategy for this user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-user-authenticationmode.html#cfn-memorydb-user-authenticationmode-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationModeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_memorydb.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "user_name": "userName",
        "access_string": "accessString",
        "authentication_mode": "authenticationMode",
        "tags": "tags",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        user_name: builtins.str,
        access_string: typing.Optional[builtins.str] = None,
        authentication_mode: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUser``.

        :param user_name: The name of the user.
        :param access_string: Access permissions string used for this user.
        :param authentication_mode: Denotes whether the user requires a password to authenticate. *Example:* ``mynewdbuser: Type: AWS::MemoryDB::User Properties: AccessString: on ~* &* +@all AuthenticationMode: Passwords: '1234567890123456' Type: password UserName: mynewdbuser AuthenticationMode: { "Passwords": ["1234567890123456"], "Type": "Password" }``
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_memorydb as memorydb
            
            # authentication_mode: Any
            
            cfn_user_props = memorydb.CfnUserProps(
                user_name="userName",
            
                # the properties below are optional
                access_string="accessString",
                authentication_mode=authentication_mode,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f925a1d7d83bd8482a242ecda1a708d70eb49d2ad0cffde56363c3e0dd9b19a2)
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument access_string", value=access_string, expected_type=type_hints["access_string"])
            check_type(argname="argument authentication_mode", value=authentication_mode, expected_type=type_hints["authentication_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_name": user_name,
        }
        if access_string is not None:
            self._values["access_string"] = access_string
        if authentication_mode is not None:
            self._values["authentication_mode"] = authentication_mode
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The name of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_string(self) -> typing.Optional[builtins.str]:
        '''Access permissions string used for this user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-accessstring
        '''
        result = self._values.get("access_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication_mode(self) -> typing.Any:
        '''Denotes whether the user requires a password to authenticate.

        *Example:*

        ``mynewdbuser: Type: AWS::MemoryDB::User Properties: AccessString: on ~* &* +@all AuthenticationMode: Passwords: '1234567890123456' Type: password UserName: mynewdbuser AuthenticationMode: { "Passwords": ["1234567890123456"], "Type": "Password" }``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-authenticationmode
        '''
        result = self._values.get("authentication_mode")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-tags
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
    "CfnACL",
    "CfnACLProps",
    "CfnCluster",
    "CfnClusterProps",
    "CfnParameterGroup",
    "CfnParameterGroupProps",
    "CfnSubnetGroup",
    "CfnSubnetGroupProps",
    "CfnUser",
    "CfnUserProps",
]

publication.publish()

def _typecheckingstub__9484fd1d572431ae11bb12955c007dddcddc12b2666a5855747b0a1acb261875(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    acl_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc6a711d3d8a9748de4a3ff47996a84e749aad94d25a5dda512b2da78cc1038(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4acff847fe3f6b78cef61522d272a00a00cc6e9e52bdeb53d457a7ef9445111(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f59d44321ba67be64a21cd7280a133eb5eafce74ce555870a7e52de3bbadcbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19dfb38b66bc6a76c22f50b7a62a4979bd2a681026ccd6e3e50920eb6c5cf6f4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f042edf87d33b30ef4ba034b5cf40ac2a7656eb3997bb3b2744a40f2166de66(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__848e1428f1884a88285ca152ff429f50733c57eca32906e1deaae2e8b3f4cd9a(
    *,
    acl_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2be3fd9830386937ed856721b0282cb7c4bcfb48ca212a069ae310ef4612235b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    acl_name: builtins.str,
    cluster_name: builtins.str,
    node_type: builtins.str,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cluster_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_tiering: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    final_snapshot_name: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[builtins.str] = None,
    num_replicas_per_shard: typing.Optional[jsii.Number] = None,
    num_shards: typing.Optional[jsii.Number] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    snapshot_window: typing.Optional[builtins.str] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
    sns_topic_status: typing.Optional[builtins.str] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    tls_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76cb969e4927216a06a434c27c39efb5cdd385529b9ea5e0319d2951238e010e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01db201d255a330f5adbc767e7d8534c144fe92bcc19d9c60759ff18a74cd98(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c3c2eddecf623588f80ccc7dc138eb7bbc48ab8fb8408ae9fce592041db4684(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa662ca2d6af7f3a9fcaf06f14705152ff3589c084e25ab2f001d9e1b25c26d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaa925a9d7f42afc3b5dfd02b1e7d763fb4a92eaa811c0f438b6b77f5b2d2d16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ceb7f4779e4cc3158fd10ae0f789f977bf4ec7b305427de026b71410314aa2(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb933d0258a10b86325bdd089031bbb07512679b44ad9da34f9d222d2a6f441(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EndpointProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d10d5c055bea0f63e6e3a2941e61801b460bb5413a94982bc6c27b2009874a78(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53812133543a07114ef48993753a17493cf0eaec35b4f165d5b5360b4c26b52f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169ccd9bb3c17f7e26324bbd84534aada6e77306d49160dd24968619a98599f9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__301d4a99b6e66b0220c0a2c677e41494ec8f873a343c7550ef2a5a37c2b926fb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a09adc41454c2729b7ba3708a53bab49bfe2b1339006a09bcdd1059df89bb7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09056b85563d6a2905d89569ae90fbdb30eac108e48fcbb7dd5f0ebd2fadb818(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479de98a506cf9095cbe7cc894a5d9900271b75b5ba2f28140084d5f265184a7(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9135b8b8321239dd0eec70d6b0b8e9c9786b7f31b39fca12acff646ca5ac847a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afe7bb6b934e8c26f66b356ef270e262cafc5cb83f3ccd7f2c0e73e7a8c53a86(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__514c944046b7e1b4d74e9f68444e13be7441e98d16292246e9e63d3a03acf09e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c15744036c88b29c766bdf4d57428776ee376a9c3a84a09d0d2b17f1691ce873(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8318d1f21d46a1ae1d8dd7ef1d3bffaf1187d17aa4b3e86a78283323fcbc00ed(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__804f6c88ce3d1f28a2ee2674d669c579358fa826656fb307dfb51d0218e29253(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a974ab4488e4f73743ed4fde25eaf3834528b3a7c7cbaec76bc82aa64b3f38f5(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25236d19ef16b48436cefd0501c036250a6efde6040b75c7c137f53c18680083(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b881a509aa28847923e821bbd39f9fe72db3a10833d11edf261679abeffffcb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537157a3978a51b06802ba8f249faf9b7508885f9892ec03421fcbb0b008a92c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ec6f6b0257f531ddbc438480683e55ab4636f2133f40c6730f1fef7235204e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb518ff45629b2fc5f7488c33f7e4de652dc27f32c98792c355068710db9cbd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c35c0a09eb3a078c7c40fabc044eb0877fe7280b70079614ef1383d482cdaa0c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a97cbfefa1a4fe0796786c02815b29787b8019f1c83531b4338dd5b4d2c2ddbd(
    *,
    address: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e34c4b7ef2f8328b2d19e6f768b6f44c55efea16824463c1ed0f3497299f1e8(
    *,
    acl_name: builtins.str,
    cluster_name: builtins.str,
    node_type: builtins.str,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cluster_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_tiering: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    final_snapshot_name: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[builtins.str] = None,
    num_replicas_per_shard: typing.Optional[jsii.Number] = None,
    num_shards: typing.Optional[jsii.Number] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    snapshot_window: typing.Optional[builtins.str] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
    sns_topic_status: typing.Optional[builtins.str] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    tls_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61162072dcce7ce6eaedeac288d04351f356c4501c7c00303d65b4be539cccbc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    family: builtins.str,
    parameter_group_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7debe0fab7bb59dfcf15f4175e0f474c741a7964960dcbe155b0c5efbd1e09f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2849ec1f4498474dd393323e9addf1ae2cfcd99fed5607fae0ca019224dba56c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2327ef6bcccd65d07bebc4ca23b1ce3d974747ae6a1bfc2e9bc11ca9d854f937(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a79238fbac363251cbc8f245e05b8ca03c8a64c30125e3c5e45dde648dbc297c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feaa80d0267309e0293955eef98ea054278b3743ff2e229578818e3f85c41274(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__073902d6d488ba79aa229654bc7ef8389dbcbbfdc460e3df4c719249bbebc807(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c759a2a9795495d5bfdf5e24f113bc8b0166dd214c06992783c7263752a055(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be6b7833c24ddd9e0e309e9aaec933dfc2aeac5e49f40692fef7c14f6f5014f4(
    *,
    family: builtins.str,
    parameter_group_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3dd027b7c51d2057be81ff17bfef3dbfbd3522767ca600f468a0d67ff1212e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    subnet_group_name: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3145bbd399c6ddffdc2666544781343f26eb710bec8432513151b15f3216473b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__810a98a25d7c87dba6cc582df35eb455e83853a112a565ad67819e6c431f55d4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__303ad17b502aa93b1d211d7399cadc117544aadb4bee45b9c7c626efaa2319c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72108b7d31976f953c8fa13d3a84ced5445347ca890c80e5a6da1fcaf1ccd5e2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f54a9326815fe3c9ee63863201b4f4e885ed0e38d3788845c6f3ba942c143885(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__085e1da0c8228c03b5e87f741c2983f9ac01339c717a01009e150bd087ab288f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9355391d833b76afd63e1ea2e6ccb22ce04e5360c7352ef34ee698b3d16fa6c1(
    *,
    subnet_group_name: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b4cd545a9f18f09898b753580c602cd4bd6e39c07e6a1f9e34f4fb928fb1dc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    user_name: builtins.str,
    access_string: typing.Optional[builtins.str] = None,
    authentication_mode: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c3bb35282143a9481bb5124eb626806569dc76eef119d8888c4373701fb4dd9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b8a18b12b6297a5b86c733efcf9f7c32315d3c27a2246b6428be84b10a621b1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f26f858b02f3b8efd6dc74353dbccbfa9f7dd93142545509b690f9bb6283d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5328fc755bfd9d9f30b338838f998fbf324c3bf12aaf33c79a23dedd4cb14f34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4785cb3838ab67f42c8f81c4a572fab61ddb9b328d731d82b7cd05ae96e1d834(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1caf541d919490fde818383ad7111c6060c95572004849b73f36d7935d02afe(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7829a96cb7f6a4249d594f7be104bbd66d8afd40591a46c942d55bbdbbbe048c(
    *,
    passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f925a1d7d83bd8482a242ecda1a708d70eb49d2ad0cffde56363c3e0dd9b19a2(
    *,
    user_name: builtins.str,
    access_string: typing.Optional[builtins.str] = None,
    authentication_mode: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
