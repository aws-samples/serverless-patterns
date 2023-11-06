'''
# AWS::DocDBElastic Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_docdbelastic as docdbelastic
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DocDBElastic construct libraries](https://constructs.dev/search?q=docdbelastic)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DocDBElastic resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DocDBElastic.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DocDBElastic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DocDBElastic.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdbelastic.CfnCluster",
):
    '''Creates a new Amazon DocumentDB elastic cluster and returns its cluster structure.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdbelastic as docdbelastic
        
        cfn_cluster = docdbelastic.CfnCluster(self, "MyCfnCluster",
            admin_user_name="adminUserName",
            auth_type="authType",
            cluster_name="clusterName",
            shard_capacity=123,
            shard_count=123,
        
            # the properties below are optional
            admin_user_password="adminUserPassword",
            kms_key_id="kmsKeyId",
            preferred_maintenance_window="preferredMaintenanceWindow",
            subnet_ids=["subnetIds"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        admin_user_name: builtins.str,
        auth_type: builtins.str,
        cluster_name: builtins.str,
        shard_capacity: jsii.Number,
        shard_count: jsii.Number,
        admin_user_password: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param admin_user_name: The name of the Amazon DocumentDB elastic clusters administrator. *Constraints* : - Must be from 1 to 63 letters or numbers. - The first character must be a letter. - Cannot be a reserved word.
        :param auth_type: The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are ``PLAIN_TEXT`` or ``SECRET_ARN`` .
        :param cluster_name: The name of the new elastic cluster. This parameter is stored as a lowercase string. *Constraints* : - Must contain from 1 to 63 letters, numbers, or hyphens. - The first character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. *Example* : ``my-cluster``
        :param shard_capacity: The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        :param shard_count: The number of shards assigned to the elastic cluster. Maximum is 32.
        :param admin_user_password: The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters. *Constraints* : - Must contain from 8 to 100 characters. - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@). - A valid ``AdminUserName`` entry is also required.
        :param kms_key_id: The KMS key identifier to use to encrypt the new elastic cluster. The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). *Format* : ``ddd:hh24:mi-ddd:hh24:mi`` *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week. *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun *Constraints* : Minimum 30-minute window.
        :param subnet_ids: The Amazon EC2 subnet IDs for the new elastic cluster.
        :param tags: The tags to be assigned to the new elastic cluster.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with the new elastic cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d18e65300a117432acf21688bd5e6ea35e026a31a5e4e4867ff7ee2d8db5564d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            admin_user_name=admin_user_name,
            auth_type=auth_type,
            cluster_name=cluster_name,
            shard_capacity=shard_capacity,
            shard_count=shard_count,
            admin_user_password=admin_user_password,
            kms_key_id=kms_key_id,
            preferred_maintenance_window=preferred_maintenance_window,
            subnet_ids=subnet_ids,
            tags=tags,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aec8e551077c21913b737a2bbc888da7a50a3375755b5e68b19b767f593e0257)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a898906295d082897a7970db90e4e30b3fa698fffb4c8731a51f9a15878288a2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterArn")
    def attr_cluster_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ClusterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterArn"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterEndpoint")
    def attr_cluster_endpoint(self) -> builtins.str:
        '''
        :cloudformationAttribute: ClusterEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterEndpoint"))

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
    @jsii.member(jsii_name="adminUserName")
    def admin_user_name(self) -> builtins.str:
        '''The name of the Amazon DocumentDB elastic clusters administrator.'''
        return typing.cast(builtins.str, jsii.get(self, "adminUserName"))

    @admin_user_name.setter
    def admin_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75e884ad993b4ce5fe022eb51a18cbb8f74e5912e83a15d50d9899aa3445bdcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUserName", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        '''The authentication type used to determine where to fetch the password used for accessing the elastic cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25c0c8636d6a5305b5ec107b1ced064baa846fc551d5b0ff94f55596f60cceef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The name of the new elastic cluster.

        This parameter is stored as a lowercase string.
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35b5d057407f61272e574c114a6e28178b7fcb07d1c9cbe8c7ba5996a0be5262)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="shardCapacity")
    def shard_capacity(self) -> jsii.Number:
        '''The number of vCPUs assigned to each elastic cluster shard.'''
        return typing.cast(jsii.Number, jsii.get(self, "shardCapacity"))

    @shard_capacity.setter
    def shard_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd6ddfaad6dd710cf923e794e6d68545333af2222ee08e33f275b5aeffaa20bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shardCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="shardCount")
    def shard_count(self) -> jsii.Number:
        '''The number of shards assigned to the elastic cluster.'''
        return typing.cast(jsii.Number, jsii.get(self, "shardCount"))

    @shard_count.setter
    def shard_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfcef7bfb595bba74106d2b94ae9ee7fde3cfc22a3ea86d938c1f50bc2c7966e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shardCount", value)

    @builtins.property
    @jsii.member(jsii_name="adminUserPassword")
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUserPassword"))

    @admin_user_password.setter
    def admin_user_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470579f0ad58114a88b5ed48276c3b18996b7302a73c462a28c5fe499da47fc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The KMS key identifier to use to encrypt the new elastic cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0953a51d1454415947e4ab62061cf85963bc67eaf8b442f55611367c42e51638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ffa8d3c73f9cb8dbb10a83c94105842d5c99d4532516cfb2e94ac10a5760cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon EC2 subnet IDs for the new elastic cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59fae2991fdf99f407d97835ea06b1afbfc6a97c5607c1b1b36dfc5aad6bb97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the new elastic cluster.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f105da06d91ef171ed924155e7737cd00df9c3b1289c1c0098e9af8a494bdb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of EC2 VPC security groups to associate with the new elastic cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712dc02a5b00741b7b19719e7c7ce31507c5058d6a956dc9dd8e9d609da8dde3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdbelastic.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "admin_user_name": "adminUserName",
        "auth_type": "authType",
        "cluster_name": "clusterName",
        "shard_capacity": "shardCapacity",
        "shard_count": "shardCount",
        "admin_user_password": "adminUserPassword",
        "kms_key_id": "kmsKeyId",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        admin_user_name: builtins.str,
        auth_type: builtins.str,
        cluster_name: builtins.str,
        shard_capacity: jsii.Number,
        shard_count: jsii.Number,
        admin_user_password: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param admin_user_name: The name of the Amazon DocumentDB elastic clusters administrator. *Constraints* : - Must be from 1 to 63 letters or numbers. - The first character must be a letter. - Cannot be a reserved word.
        :param auth_type: The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are ``PLAIN_TEXT`` or ``SECRET_ARN`` .
        :param cluster_name: The name of the new elastic cluster. This parameter is stored as a lowercase string. *Constraints* : - Must contain from 1 to 63 letters, numbers, or hyphens. - The first character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. *Example* : ``my-cluster``
        :param shard_capacity: The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        :param shard_count: The number of shards assigned to the elastic cluster. Maximum is 32.
        :param admin_user_password: The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters. *Constraints* : - Must contain from 8 to 100 characters. - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@). - A valid ``AdminUserName`` entry is also required.
        :param kms_key_id: The KMS key identifier to use to encrypt the new elastic cluster. The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). *Format* : ``ddd:hh24:mi-ddd:hh24:mi`` *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week. *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun *Constraints* : Minimum 30-minute window.
        :param subnet_ids: The Amazon EC2 subnet IDs for the new elastic cluster.
        :param tags: The tags to be assigned to the new elastic cluster.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with the new elastic cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdbelastic as docdbelastic
            
            cfn_cluster_props = docdbelastic.CfnClusterProps(
                admin_user_name="adminUserName",
                auth_type="authType",
                cluster_name="clusterName",
                shard_capacity=123,
                shard_count=123,
            
                # the properties below are optional
                admin_user_password="adminUserPassword",
                kms_key_id="kmsKeyId",
                preferred_maintenance_window="preferredMaintenanceWindow",
                subnet_ids=["subnetIds"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b5fe934af328fd508365294b2de9cfcaa71e04fad229d22243ec4156b7f0441)
            check_type(argname="argument admin_user_name", value=admin_user_name, expected_type=type_hints["admin_user_name"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument shard_capacity", value=shard_capacity, expected_type=type_hints["shard_capacity"])
            check_type(argname="argument shard_count", value=shard_count, expected_type=type_hints["shard_count"])
            check_type(argname="argument admin_user_password", value=admin_user_password, expected_type=type_hints["admin_user_password"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_user_name": admin_user_name,
            "auth_type": auth_type,
            "cluster_name": cluster_name,
            "shard_capacity": shard_capacity,
            "shard_count": shard_count,
        }
        if admin_user_password is not None:
            self._values["admin_user_password"] = admin_user_password
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def admin_user_name(self) -> builtins.str:
        '''The name of the Amazon DocumentDB elastic clusters administrator.

        *Constraints* :

        - Must be from 1 to 63 letters or numbers.
        - The first character must be a letter.
        - Cannot be a reserved word.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-adminusername
        '''
        result = self._values.get("admin_user_name")
        assert result is not None, "Required property 'admin_user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_type(self) -> builtins.str:
        '''The authentication type used to determine where to fetch the password used for accessing the elastic cluster.

        Valid types are ``PLAIN_TEXT`` or ``SECRET_ARN`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-authtype
        '''
        result = self._values.get("auth_type")
        assert result is not None, "Required property 'auth_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the new elastic cluster. This parameter is stored as a lowercase string.

        *Constraints* :

        - Must contain from 1 to 63 letters, numbers, or hyphens.
        - The first character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        *Example* : ``my-cluster``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shard_capacity(self) -> jsii.Number:
        '''The number of vCPUs assigned to each elastic cluster shard.

        Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-shardcapacity
        '''
        result = self._values.get("shard_capacity")
        assert result is not None, "Required property 'shard_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def shard_count(self) -> jsii.Number:
        '''The number of shards assigned to the elastic cluster.

        Maximum is 32.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-shardcount
        '''
        result = self._values.get("shard_count")
        assert result is not None, "Required property 'shard_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.

        *Constraints* :

        - Must contain from 8 to 100 characters.
        - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).
        - A valid ``AdminUserName`` entry is also required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-adminuserpassword
        '''
        result = self._values.get("admin_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The KMS key identifier to use to encrypt the new elastic cluster.

        The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.

        If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        *Format* : ``ddd:hh24:mi-ddd:hh24:mi``

        *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week.

        *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun

        *Constraints* : Minimum 30-minute window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon EC2 subnet IDs for the new elastic cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the new elastic cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of EC2 VPC security groups to associate with the new elastic cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
]

publication.publish()

def _typecheckingstub__d18e65300a117432acf21688bd5e6ea35e026a31a5e4e4867ff7ee2d8db5564d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    admin_user_name: builtins.str,
    auth_type: builtins.str,
    cluster_name: builtins.str,
    shard_capacity: jsii.Number,
    shard_count: jsii.Number,
    admin_user_password: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec8e551077c21913b737a2bbc888da7a50a3375755b5e68b19b767f593e0257(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a898906295d082897a7970db90e4e30b3fa698fffb4c8731a51f9a15878288a2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e884ad993b4ce5fe022eb51a18cbb8f74e5912e83a15d50d9899aa3445bdcd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c0c8636d6a5305b5ec107b1ced064baa846fc551d5b0ff94f55596f60cceef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35b5d057407f61272e574c114a6e28178b7fcb07d1c9cbe8c7ba5996a0be5262(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd6ddfaad6dd710cf923e794e6d68545333af2222ee08e33f275b5aeffaa20bb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfcef7bfb595bba74106d2b94ae9ee7fde3cfc22a3ea86d938c1f50bc2c7966e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470579f0ad58114a88b5ed48276c3b18996b7302a73c462a28c5fe499da47fc2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0953a51d1454415947e4ab62061cf85963bc67eaf8b442f55611367c42e51638(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffa8d3c73f9cb8dbb10a83c94105842d5c99d4532516cfb2e94ac10a5760cd3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59fae2991fdf99f407d97835ea06b1afbfc6a97c5607c1b1b36dfc5aad6bb97(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f105da06d91ef171ed924155e7737cd00df9c3b1289c1c0098e9af8a494bdb6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712dc02a5b00741b7b19719e7c7ce31507c5058d6a956dc9dd8e9d609da8dde3(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5fe934af328fd508365294b2de9cfcaa71e04fad229d22243ec4156b7f0441(
    *,
    admin_user_name: builtins.str,
    auth_type: builtins.str,
    cluster_name: builtins.str,
    shard_capacity: jsii.Number,
    shard_count: jsii.Number,
    admin_user_password: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
