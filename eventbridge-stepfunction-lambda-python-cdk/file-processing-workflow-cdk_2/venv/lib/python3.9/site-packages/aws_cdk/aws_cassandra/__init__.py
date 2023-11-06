'''
# AWS::Cassandra Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cassandra as cassandra
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Cassandra construct libraries](https://constructs.dev/search?q=cassandra)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Cassandra resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cassandra.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Cassandra](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cassandra.html).

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
class CfnKeyspace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cassandra.CfnKeyspace",
):
    '''You can use the ``AWS::Cassandra::Keyspace`` resource to create a new keyspace in Amazon Keyspaces (for Apache Cassandra).

    For more information, see `Create a keyspace and a table <https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.ddl.html>`_ in the *Amazon Keyspaces Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cassandra as cassandra
        
        cfn_keyspace = cassandra.CfnKeyspace(self, "MyCfnKeyspace",
            keyspace_name="keyspaceName",
            replication_specification=cassandra.CfnKeyspace.ReplicationSpecificationProperty(
                region_list=["regionList"],
                replication_strategy="replicationStrategy"
            ),
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
        keyspace_name: typing.Optional[builtins.str] = None,
        replication_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKeyspace.ReplicationSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param keyspace_name: The name of the keyspace to be created. The keyspace name is case sensitive. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the keyspace name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . *Length constraints:* Minimum length of 3. Maximum length of 255. *Pattern:* ``^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$``
        :param replication_specification: Specifies the ``ReplicationStrategy`` of a keyspace. The options are:. - ``SINGLE_REGION`` for a single Region keyspace (optional) or - ``MULTI_REGION`` for a multi-Region keyspace If no ``ReplicationStrategy`` is provided, the default is ``SINGLE_REGION`` . If you choose ``MULTI_REGION`` , you must also provide a ``RegionList`` with the AWS Regions that the keyspace is replicated in.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cd64888a8d1139f7fef90a6f2cad1bf287a6d09115cfa1d1147c1afd8f5f9e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKeyspaceProps(
            keyspace_name=keyspace_name,
            replication_specification=replication_specification,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ecbad4543180c6cf4913924c148b210c77e3da9a878ec77916ea568a560458b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42f60f7b87e845a932e67441bed6a8227df77e1b7945146e65d3ba8ac68a7960)
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
    @jsii.member(jsii_name="keyspaceName")
    def keyspace_name(self) -> typing.Optional[builtins.str]:
        '''The name of the keyspace to be created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyspaceName"))

    @keyspace_name.setter
    def keyspace_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb7166642fd3aff60742c5e03d8f0094ff2d3ed08ad9f239837dfa2ef308f38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyspaceName", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSpecification")
    def replication_specification(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKeyspace.ReplicationSpecificationProperty"]]:
        '''Specifies the ``ReplicationStrategy`` of a keyspace.

        The options are:.
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKeyspace.ReplicationSpecificationProperty"]], jsii.get(self, "replicationSpecification"))

    @replication_specification.setter
    def replication_specification(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKeyspace.ReplicationSpecificationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb87739fda4abfb9cec927655958eeed2ab44c06374fbd6f52c9ff6c3303247e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bbd84051da75f3e01d5eeefad9f72e1f8f65ba4f3cf7969332aab7dc8d01a19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cassandra.CfnKeyspace.ReplicationSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region_list": "regionList",
            "replication_strategy": "replicationStrategy",
        },
    )
    class ReplicationSpecificationProperty:
        def __init__(
            self,
            *,
            region_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            replication_strategy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''You can use ``ReplicationSpecification`` to configure the ``ReplicationStrategy`` of a keyspace in Amazon Keyspaces.

            The ``ReplicationSpecification`` property is ``CreateOnly`` and cannot be changed after the keyspace has been created. This property applies automatically to all tables in the keyspace.

            For more information, see `Multi-Region Replication <https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication.html>`_ in the *Amazon Keyspaces Developer Guide* .

            :param region_list: Specifies the AWS Regions that the keyspace is replicated in. You must specify at least two and up to six Regions, including the Region that the keyspace is being created in.
            :param replication_strategy: The options are:. - ``SINGLE_REGION`` (optional) - ``MULTI_REGION`` If no value is specified, the default is ``SINGLE_REGION`` . If ``MULTI_REGION`` is specified, ``RegionList`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-keyspace-replicationspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cassandra as cassandra
                
                replication_specification_property = cassandra.CfnKeyspace.ReplicationSpecificationProperty(
                    region_list=["regionList"],
                    replication_strategy="replicationStrategy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e5f12bad7b518911e0710e02ed64e0533c1123f35e304844dab5aaae8383b25a)
                check_type(argname="argument region_list", value=region_list, expected_type=type_hints["region_list"])
                check_type(argname="argument replication_strategy", value=replication_strategy, expected_type=type_hints["replication_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if region_list is not None:
                self._values["region_list"] = region_list
            if replication_strategy is not None:
                self._values["replication_strategy"] = replication_strategy

        @builtins.property
        def region_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the AWS Regions that the keyspace is replicated in.

            You must specify at least two and up to six Regions, including the Region that the keyspace is being created in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-keyspace-replicationspecification.html#cfn-cassandra-keyspace-replicationspecification-regionlist
            '''
            result = self._values.get("region_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def replication_strategy(self) -> typing.Optional[builtins.str]:
            '''The options are:.

            - ``SINGLE_REGION`` (optional)
            - ``MULTI_REGION``

            If no value is specified, the default is ``SINGLE_REGION`` . If ``MULTI_REGION`` is specified, ``RegionList`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-keyspace-replicationspecification.html#cfn-cassandra-keyspace-replicationspecification-replicationstrategy
            '''
            result = self._values.get("replication_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicationSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cassandra.CfnKeyspaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "keyspace_name": "keyspaceName",
        "replication_specification": "replicationSpecification",
        "tags": "tags",
    },
)
class CfnKeyspaceProps:
    def __init__(
        self,
        *,
        keyspace_name: typing.Optional[builtins.str] = None,
        replication_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKeyspace.ReplicationSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnKeyspace``.

        :param keyspace_name: The name of the keyspace to be created. The keyspace name is case sensitive. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the keyspace name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . *Length constraints:* Minimum length of 3. Maximum length of 255. *Pattern:* ``^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$``
        :param replication_specification: Specifies the ``ReplicationStrategy`` of a keyspace. The options are:. - ``SINGLE_REGION`` for a single Region keyspace (optional) or - ``MULTI_REGION`` for a multi-Region keyspace If no ``ReplicationStrategy`` is provided, the default is ``SINGLE_REGION`` . If you choose ``MULTI_REGION`` , you must also provide a ``RegionList`` with the AWS Regions that the keyspace is replicated in.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cassandra as cassandra
            
            cfn_keyspace_props = cassandra.CfnKeyspaceProps(
                keyspace_name="keyspaceName",
                replication_specification=cassandra.CfnKeyspace.ReplicationSpecificationProperty(
                    region_list=["regionList"],
                    replication_strategy="replicationStrategy"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc0263cb98dfdfc7ed9f31cf986359bcc44c1b3f3c733ebb7d3e36b25fb4cea8)
            check_type(argname="argument keyspace_name", value=keyspace_name, expected_type=type_hints["keyspace_name"])
            check_type(argname="argument replication_specification", value=replication_specification, expected_type=type_hints["replication_specification"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if keyspace_name is not None:
            self._values["keyspace_name"] = keyspace_name
        if replication_specification is not None:
            self._values["replication_specification"] = replication_specification
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def keyspace_name(self) -> typing.Optional[builtins.str]:
        '''The name of the keyspace to be created.

        The keyspace name is case sensitive. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the keyspace name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        *Length constraints:* Minimum length of 3. Maximum length of 255.

        *Pattern:* ``^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-keyspacename
        '''
        result = self._values.get("keyspace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_specification(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKeyspace.ReplicationSpecificationProperty]]:
        '''Specifies the ``ReplicationStrategy`` of a keyspace. The options are:.

        - ``SINGLE_REGION`` for a single Region keyspace (optional) or
        - ``MULTI_REGION`` for a multi-Region keyspace

        If no ``ReplicationStrategy`` is provided, the default is ``SINGLE_REGION`` . If you choose ``MULTI_REGION`` , you must also provide a ``RegionList`` with the AWS Regions that the keyspace is replicated in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-replicationspecification
        '''
        result = self._values.get("replication_specification")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKeyspace.ReplicationSpecificationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKeyspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cassandra.CfnTable",
):
    '''You can use the ``AWS::Cassandra::Table`` resource to create a new table in Amazon Keyspaces (for Apache Cassandra).

    For more information, see `Create a keyspace and a table <https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.ddl.html>`_ in the *Amazon Keyspaces Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cassandra as cassandra
        
        cfn_table = cassandra.CfnTable(self, "MyCfnTable",
            keyspace_name="keyspaceName",
            partition_key_columns=[cassandra.CfnTable.ColumnProperty(
                column_name="columnName",
                column_type="columnType"
            )],
        
            # the properties below are optional
            billing_mode=cassandra.CfnTable.BillingModeProperty(
                mode="mode",
        
                # the properties below are optional
                provisioned_throughput=cassandra.CfnTable.ProvisionedThroughputProperty(
                    read_capacity_units=123,
                    write_capacity_units=123
                )
            ),
            client_side_timestamps_enabled=False,
            clustering_key_columns=[cassandra.CfnTable.ClusteringKeyColumnProperty(
                column=cassandra.CfnTable.ColumnProperty(
                    column_name="columnName",
                    column_type="columnType"
                ),
        
                # the properties below are optional
                order_by="orderBy"
            )],
            default_time_to_live=123,
            encryption_specification=cassandra.CfnTable.EncryptionSpecificationProperty(
                encryption_type="encryptionType",
        
                # the properties below are optional
                kms_key_identifier="kmsKeyIdentifier"
            ),
            point_in_time_recovery_enabled=False,
            regular_columns=[cassandra.CfnTable.ColumnProperty(
                column_name="columnName",
                column_type="columnType"
            )],
            table_name="tableName",
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
        keyspace_name: builtins.str,
        partition_key_columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.ColumnProperty", typing.Dict[builtins.str, typing.Any]]]]],
        billing_mode: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.BillingModeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        client_side_timestamps_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        clustering_key_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.ClusteringKeyColumnProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        default_time_to_live: typing.Optional[jsii.Number] = None,
        encryption_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.EncryptionSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        regular_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.ColumnProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param keyspace_name: The name of the keyspace to create the table in. The keyspace must already exist.
        :param partition_key_columns: One or more columns that uniquely identify every row in the table. Every table must have a partition key.
        :param billing_mode: The billing mode for the table, which determines how you'll be charged for reads and writes:. - *On-demand mode* (default) - You pay based on the actual reads and writes your application performs. - *Provisioned mode* - Lets you specify the number of reads and writes per second that you need for your application. If you don't specify a value for this property, then the table will use on-demand mode.
        :param client_side_timestamps_enabled: Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option: - ``status: "enabled"`` After client-side timestamps are enabled for a table, you can't disable this setting.
        :param clustering_key_columns: One or more columns that determine how the table data is sorted.
        :param default_time_to_live: The default Time To Live (TTL) value for all rows in a table in seconds. The maximum configurable value is 630,720,000 seconds, which is the equivalent of 20 years. By default, the TTL value for a table is 0, which means data does not expire. For more information, see `Setting the default TTL value for a table <https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl>`_ in the *Amazon Keyspaces Developer Guide* .
        :param encryption_specification: The encryption at rest options for the table. - *AWS owned key* (default) - The key is owned by Amazon Keyspaces. - *Customer managed key* - The key is stored in your account and is created, owned, and managed by you. .. epigraph:: If you choose encryption with a customer managed key, you must specify a valid customer managed KMS key with permissions granted to Amazon Keyspaces. For more information, see `Encryption at rest in Amazon Keyspaces <https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html>`_ in the *Amazon Keyspaces Developer Guide* .
        :param point_in_time_recovery_enabled: Specifies if point-in-time recovery is enabled or disabled for the table. The options are ``PointInTimeRecoveryEnabled=true`` and ``PointInTimeRecoveryEnabled=false`` . If not specified, the default is ``PointInTimeRecoveryEnabled=false`` .
        :param regular_columns: One or more columns that are not part of the primary key - that is, columns that are *not* defined as partition key columns or clustering key columns. You can add regular columns to existing tables by adding them to the template.
        :param table_name: The name of the table to be created. The table name is case sensitive. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the table name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you can't perform updates that require replacing this resource. You can perform updates that require no interruption or some interruption. If you must replace the resource, specify a new name. *Length constraints:* Minimum length of 3. Maximum length of 255. *Pattern:* ``^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$``
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6fd025c7c0c8d4a27519b568ec6952b027c14ffb932a0cd5e53f0aae4270b3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTableProps(
            keyspace_name=keyspace_name,
            partition_key_columns=partition_key_columns,
            billing_mode=billing_mode,
            client_side_timestamps_enabled=client_side_timestamps_enabled,
            clustering_key_columns=clustering_key_columns,
            default_time_to_live=default_time_to_live,
            encryption_specification=encryption_specification,
            point_in_time_recovery_enabled=point_in_time_recovery_enabled,
            regular_columns=regular_columns,
            table_name=table_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3024cadcd02ed175dead491b1c5e108162ba00bd9697ca0a21957570dcc30963)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2704679b24717c434c4bc09d9ffb9dbc4aee00a7925442e23bb2c107ac7a76b9)
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
    @jsii.member(jsii_name="keyspaceName")
    def keyspace_name(self) -> builtins.str:
        '''The name of the keyspace to create the table in.'''
        return typing.cast(builtins.str, jsii.get(self, "keyspaceName"))

    @keyspace_name.setter
    def keyspace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39801b43f69f67941929194d4199c85a34126143e133e315190906067d512822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyspaceName", value)

    @builtins.property
    @jsii.member(jsii_name="partitionKeyColumns")
    def partition_key_columns(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]]:
        '''One or more columns that uniquely identify every row in the table.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]], jsii.get(self, "partitionKeyColumns"))

    @partition_key_columns.setter
    def partition_key_columns(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1db183d8a51a33cc93b8d90f2611025ff7f3e6539e707de86fd9a5073f0a785)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKeyColumns", value)

    @builtins.property
    @jsii.member(jsii_name="billingMode")
    def billing_mode(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.BillingModeProperty"]]:
        '''The billing mode for the table, which determines how you'll be charged for reads and writes:.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.BillingModeProperty"]], jsii.get(self, "billingMode"))

    @billing_mode.setter
    def billing_mode(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.BillingModeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2219a43361bf3ff1d1bf29e1b2907d75a53df3b7016d534579938eea5d4e91d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingMode", value)

    @builtins.property
    @jsii.member(jsii_name="clientSideTimestampsEnabled")
    def client_side_timestamps_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables client-side timestamps for the table.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "clientSideTimestampsEnabled"))

    @client_side_timestamps_enabled.setter
    def client_side_timestamps_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd9370f4f1ef0d5c1349ef8d576cad345ff735c9ca5c01758d25b48bfb48e5bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSideTimestampsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clusteringKeyColumns")
    def clustering_key_columns(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ClusteringKeyColumnProperty"]]]]:
        '''One or more columns that determine how the table data is sorted.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ClusteringKeyColumnProperty"]]]], jsii.get(self, "clusteringKeyColumns"))

    @clustering_key_columns.setter
    def clustering_key_columns(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ClusteringKeyColumnProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__629a90c3101172766e4de27d7d3ce237b18da87338a09c0e62d788bfeb846292)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusteringKeyColumns", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTimeToLive")
    def default_time_to_live(self) -> typing.Optional[jsii.Number]:
        '''The default Time To Live (TTL) value for all rows in a table in seconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTimeToLive"))

    @default_time_to_live.setter
    def default_time_to_live(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__202d75d85d4343037389d27dd4e5938ef702777fc7f61c15eacbbb8602ec2048)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTimeToLive", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionSpecification")
    def encryption_specification(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.EncryptionSpecificationProperty"]]:
        '''The encryption at rest options for the table.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.EncryptionSpecificationProperty"]], jsii.get(self, "encryptionSpecification"))

    @encryption_specification.setter
    def encryption_specification(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.EncryptionSpecificationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__105d2928be0de10d33f2dd6f9726d0b2413424d98fe5d151ccbce2002420a1f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies if point-in-time recovery is enabled or disabled for the table.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "pointInTimeRecoveryEnabled"))

    @point_in_time_recovery_enabled.setter
    def point_in_time_recovery_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367fd6c13ef0060b69d310dfec8e4128d6d23ab9f7c5c2c6f4fde1840336b733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pointInTimeRecoveryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="regularColumns")
    def regular_columns(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]]]:
        '''One or more columns that are not part of the primary key - that is, columns that are *not* defined as partition key columns or clustering key columns.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]]], jsii.get(self, "regularColumns"))

    @regular_columns.setter
    def regular_columns(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c15490d5659aeda79f13514b12c87f518d6de130270ffd24df4af663b6785f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regularColumns", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> typing.Optional[builtins.str]:
        '''The name of the table to be created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e1536df40ced7d731dcea97d7afa1eab0ec4b34824d105a20130aa6fafe98ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4224e4814f153e9978b91f35f9c02cfe00615e65fb97b060775097a1c70669ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cassandra.CfnTable.BillingModeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mode": "mode",
            "provisioned_throughput": "provisionedThroughput",
        },
    )
    class BillingModeProperty:
        def __init__(
            self,
            *,
            mode: builtins.str,
            provisioned_throughput: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.ProvisionedThroughputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Determines the billing mode for the table - on-demand or provisioned.

            :param mode: The billing mode for the table:. - On-demand mode - ``ON_DEMAND`` - Provisioned mode - ``PROVISIONED`` .. epigraph:: If you choose ``PROVISIONED`` mode, then you also need to specify provisioned throughput (read and write capacity) for the table. Valid values: ``ON_DEMAND`` | ``PROVISIONED`` Default: - "ON_DEMAND"
            :param provisioned_throughput: The provisioned read capacity and write capacity for the table. For more information, see `Provisioned throughput capacity mode <https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html#ReadWriteCapacityMode.Provisioned>`_ in the *Amazon Keyspaces Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cassandra as cassandra
                
                billing_mode_property = cassandra.CfnTable.BillingModeProperty(
                    mode="mode",
                
                    # the properties below are optional
                    provisioned_throughput=cassandra.CfnTable.ProvisionedThroughputProperty(
                        read_capacity_units=123,
                        write_capacity_units=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b57c6da9515480ece2b86b6971f8563bcf0c49dab50c8c6e234c443b8c0f9a0)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument provisioned_throughput", value=provisioned_throughput, expected_type=type_hints["provisioned_throughput"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }
            if provisioned_throughput is not None:
                self._values["provisioned_throughput"] = provisioned_throughput

        @builtins.property
        def mode(self) -> builtins.str:
            '''The billing mode for the table:.

            - On-demand mode - ``ON_DEMAND``
            - Provisioned mode - ``PROVISIONED``

            .. epigraph::

               If you choose ``PROVISIONED`` mode, then you also need to specify provisioned throughput (read and write capacity) for the table.

            Valid values: ``ON_DEMAND`` | ``PROVISIONED``

            :default: - "ON_DEMAND"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def provisioned_throughput(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.ProvisionedThroughputProperty"]]:
            '''The provisioned read capacity and write capacity for the table.

            For more information, see `Provisioned throughput capacity mode <https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html#ReadWriteCapacityMode.Provisioned>`_ in the *Amazon Keyspaces Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-provisionedthroughput
            '''
            result = self._values.get("provisioned_throughput")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.ProvisionedThroughputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BillingModeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cassandra.CfnTable.ClusteringKeyColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"column": "column", "order_by": "orderBy"},
    )
    class ClusteringKeyColumnProperty:
        def __init__(
            self,
            *,
            column: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.ColumnProperty", typing.Dict[builtins.str, typing.Any]]],
            order_by: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines an individual column within the clustering key.

            :param column: The name and data type of this clustering key column.
            :param order_by: The order in which this column's data is stored:. - ``ASC`` (default) - The column's data is stored in ascending order. - ``DESC`` - The column's data is stored in descending order. Default: - "ASC"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cassandra as cassandra
                
                clustering_key_column_property = cassandra.CfnTable.ClusteringKeyColumnProperty(
                    column=cassandra.CfnTable.ColumnProperty(
                        column_name="columnName",
                        column_type="columnType"
                    ),
                
                    # the properties below are optional
                    order_by="orderBy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c4989a761d5af337ce8ad918b2d543390cab5ea5d5ea82741f1c3416e00d794)
                check_type(argname="argument column", value=column, expected_type=type_hints["column"])
                check_type(argname="argument order_by", value=order_by, expected_type=type_hints["order_by"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column": column,
            }
            if order_by is not None:
                self._values["order_by"] = order_by

        @builtins.property
        def column(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]:
            '''The name and data type of this clustering key column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-column
            '''
            result = self._values.get("column")
            assert result is not None, "Required property 'column' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"], result)

        @builtins.property
        def order_by(self) -> typing.Optional[builtins.str]:
            '''The order in which this column's data is stored:.

            - ``ASC`` (default) - The column's data is stored in ascending order.
            - ``DESC`` - The column's data is stored in descending order.

            :default: - "ASC"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-orderby
            '''
            result = self._values.get("order_by")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusteringKeyColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cassandra.CfnTable.ColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"column_name": "columnName", "column_type": "columnType"},
    )
    class ColumnProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            column_type: builtins.str,
        ) -> None:
            '''The name and data type of an individual column in a table.

            :param column_name: The name of the column. For more information, see `Identifiers <https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.elements.identifier>`_ in the *Amazon Keyspaces Developer Guide* .
            :param column_type: The data type of the column. For more information, see `Data types <https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types>`_ in the *Amazon Keyspaces Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cassandra as cassandra
                
                column_property = cassandra.CfnTable.ColumnProperty(
                    column_name="columnName",
                    column_type="columnType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4b165821558e59006460c17fc7bc14e684785b2118bea5b769002a78e310f391)
                check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
                check_type(argname="argument column_type", value=column_type, expected_type=type_hints["column_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_name": column_name,
                "column_type": column_type,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''The name of the column.

            For more information, see `Identifiers <https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.elements.identifier>`_ in the *Amazon Keyspaces Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_type(self) -> builtins.str:
            '''The data type of the column.

            For more information, see `Data types <https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types>`_ in the *Amazon Keyspaces Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columntype
            '''
            result = self._values.get("column_type")
            assert result is not None, "Required property 'column_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cassandra.CfnTable.EncryptionSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_type": "encryptionType",
            "kms_key_identifier": "kmsKeyIdentifier",
        },
    )
    class EncryptionSpecificationProperty:
        def __init__(
            self,
            *,
            encryption_type: builtins.str,
            kms_key_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the encryption at rest option selected for the table.

            :param encryption_type: The encryption at rest options for the table. - *AWS owned key* (default) - ``AWS_OWNED_KMS_KEY`` - *Customer managed key* - ``CUSTOMER_MANAGED_KMS_KEY`` .. epigraph:: If you choose ``CUSTOMER_MANAGED_KMS_KEY`` , a ``kms_key_identifier`` in the format of a key ARN is required. Valid values: ``CUSTOMER_MANAGED_KMS_KEY`` | ``AWS_OWNED_KMS_KEY`` . Default: - "AWS_OWNED_KMS_KEY"
            :param kms_key_identifier: Requires a ``kms_key_identifier`` in the format of a key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cassandra as cassandra
                
                encryption_specification_property = cassandra.CfnTable.EncryptionSpecificationProperty(
                    encryption_type="encryptionType",
                
                    # the properties below are optional
                    kms_key_identifier="kmsKeyIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2366032cc6832a13bbd38729b1c4c9a0a38683ef6ea95cf6f8e29f0356320e0f)
                check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
                check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_type": encryption_type,
            }
            if kms_key_identifier is not None:
                self._values["kms_key_identifier"] = kms_key_identifier

        @builtins.property
        def encryption_type(self) -> builtins.str:
            '''The encryption at rest options for the table.

            - *AWS owned key* (default) - ``AWS_OWNED_KMS_KEY``
            - *Customer managed key* - ``CUSTOMER_MANAGED_KMS_KEY``

            .. epigraph::

               If you choose ``CUSTOMER_MANAGED_KMS_KEY`` , a ``kms_key_identifier`` in the format of a key ARN is required.

            Valid values: ``CUSTOMER_MANAGED_KMS_KEY`` | ``AWS_OWNED_KMS_KEY`` .

            :default: - "AWS_OWNED_KMS_KEY"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-encryptiontype
            '''
            result = self._values.get("encryption_type")
            assert result is not None, "Required property 'encryption_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_identifier(self) -> typing.Optional[builtins.str]:
            '''Requires a ``kms_key_identifier`` in the format of a key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-kmskeyidentifier
            '''
            result = self._values.get("kms_key_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cassandra.CfnTable.ProvisionedThroughputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "read_capacity_units": "readCapacityUnits",
            "write_capacity_units": "writeCapacityUnits",
        },
    )
    class ProvisionedThroughputProperty:
        def __init__(
            self,
            *,
            read_capacity_units: jsii.Number,
            write_capacity_units: jsii.Number,
        ) -> None:
            '''The provisioned throughput for the table, which consists of ``ReadCapacityUnits`` and ``WriteCapacityUnits`` .

            :param read_capacity_units: The amount of read capacity that's provisioned for the table. For more information, see `Read/write capacity mode <https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html>`_ in the *Amazon Keyspaces Developer Guide* .
            :param write_capacity_units: The amount of write capacity that's provisioned for the table. For more information, see `Read/write capacity mode <https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html>`_ in the *Amazon Keyspaces Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cassandra as cassandra
                
                provisioned_throughput_property = cassandra.CfnTable.ProvisionedThroughputProperty(
                    read_capacity_units=123,
                    write_capacity_units=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e82ecde232ad027f79eae23599756ec33659aabf2db7a5ba885d3991735a3971)
                check_type(argname="argument read_capacity_units", value=read_capacity_units, expected_type=type_hints["read_capacity_units"])
                check_type(argname="argument write_capacity_units", value=write_capacity_units, expected_type=type_hints["write_capacity_units"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "read_capacity_units": read_capacity_units,
                "write_capacity_units": write_capacity_units,
            }

        @builtins.property
        def read_capacity_units(self) -> jsii.Number:
            '''The amount of read capacity that's provisioned for the table.

            For more information, see `Read/write capacity mode <https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html>`_ in the *Amazon Keyspaces Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-readcapacityunits
            '''
            result = self._values.get("read_capacity_units")
            assert result is not None, "Required property 'read_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def write_capacity_units(self) -> jsii.Number:
            '''The amount of write capacity that's provisioned for the table.

            For more information, see `Read/write capacity mode <https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html>`_ in the *Amazon Keyspaces Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-writecapacityunits
            '''
            result = self._values.get("write_capacity_units")
            assert result is not None, "Required property 'write_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedThroughputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cassandra.CfnTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "keyspace_name": "keyspaceName",
        "partition_key_columns": "partitionKeyColumns",
        "billing_mode": "billingMode",
        "client_side_timestamps_enabled": "clientSideTimestampsEnabled",
        "clustering_key_columns": "clusteringKeyColumns",
        "default_time_to_live": "defaultTimeToLive",
        "encryption_specification": "encryptionSpecification",
        "point_in_time_recovery_enabled": "pointInTimeRecoveryEnabled",
        "regular_columns": "regularColumns",
        "table_name": "tableName",
        "tags": "tags",
    },
)
class CfnTableProps:
    def __init__(
        self,
        *,
        keyspace_name: builtins.str,
        partition_key_columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
        billing_mode: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.BillingModeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        client_side_timestamps_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        clustering_key_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ClusteringKeyColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        default_time_to_live: typing.Optional[jsii.Number] = None,
        encryption_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.EncryptionSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        regular_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTable``.

        :param keyspace_name: The name of the keyspace to create the table in. The keyspace must already exist.
        :param partition_key_columns: One or more columns that uniquely identify every row in the table. Every table must have a partition key.
        :param billing_mode: The billing mode for the table, which determines how you'll be charged for reads and writes:. - *On-demand mode* (default) - You pay based on the actual reads and writes your application performs. - *Provisioned mode* - Lets you specify the number of reads and writes per second that you need for your application. If you don't specify a value for this property, then the table will use on-demand mode.
        :param client_side_timestamps_enabled: Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option: - ``status: "enabled"`` After client-side timestamps are enabled for a table, you can't disable this setting.
        :param clustering_key_columns: One or more columns that determine how the table data is sorted.
        :param default_time_to_live: The default Time To Live (TTL) value for all rows in a table in seconds. The maximum configurable value is 630,720,000 seconds, which is the equivalent of 20 years. By default, the TTL value for a table is 0, which means data does not expire. For more information, see `Setting the default TTL value for a table <https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl>`_ in the *Amazon Keyspaces Developer Guide* .
        :param encryption_specification: The encryption at rest options for the table. - *AWS owned key* (default) - The key is owned by Amazon Keyspaces. - *Customer managed key* - The key is stored in your account and is created, owned, and managed by you. .. epigraph:: If you choose encryption with a customer managed key, you must specify a valid customer managed KMS key with permissions granted to Amazon Keyspaces. For more information, see `Encryption at rest in Amazon Keyspaces <https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html>`_ in the *Amazon Keyspaces Developer Guide* .
        :param point_in_time_recovery_enabled: Specifies if point-in-time recovery is enabled or disabled for the table. The options are ``PointInTimeRecoveryEnabled=true`` and ``PointInTimeRecoveryEnabled=false`` . If not specified, the default is ``PointInTimeRecoveryEnabled=false`` .
        :param regular_columns: One or more columns that are not part of the primary key - that is, columns that are *not* defined as partition key columns or clustering key columns. You can add regular columns to existing tables by adding them to the template.
        :param table_name: The name of the table to be created. The table name is case sensitive. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the table name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you can't perform updates that require replacing this resource. You can perform updates that require no interruption or some interruption. If you must replace the resource, specify a new name. *Length constraints:* Minimum length of 3. Maximum length of 255. *Pattern:* ``^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$``
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cassandra as cassandra
            
            cfn_table_props = cassandra.CfnTableProps(
                keyspace_name="keyspaceName",
                partition_key_columns=[cassandra.CfnTable.ColumnProperty(
                    column_name="columnName",
                    column_type="columnType"
                )],
            
                # the properties below are optional
                billing_mode=cassandra.CfnTable.BillingModeProperty(
                    mode="mode",
            
                    # the properties below are optional
                    provisioned_throughput=cassandra.CfnTable.ProvisionedThroughputProperty(
                        read_capacity_units=123,
                        write_capacity_units=123
                    )
                ),
                client_side_timestamps_enabled=False,
                clustering_key_columns=[cassandra.CfnTable.ClusteringKeyColumnProperty(
                    column=cassandra.CfnTable.ColumnProperty(
                        column_name="columnName",
                        column_type="columnType"
                    ),
            
                    # the properties below are optional
                    order_by="orderBy"
                )],
                default_time_to_live=123,
                encryption_specification=cassandra.CfnTable.EncryptionSpecificationProperty(
                    encryption_type="encryptionType",
            
                    # the properties below are optional
                    kms_key_identifier="kmsKeyIdentifier"
                ),
                point_in_time_recovery_enabled=False,
                regular_columns=[cassandra.CfnTable.ColumnProperty(
                    column_name="columnName",
                    column_type="columnType"
                )],
                table_name="tableName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd1ff29b1ec22382a7c3d14031657668106b0fcd843c06a96897bcadf10ffa92)
            check_type(argname="argument keyspace_name", value=keyspace_name, expected_type=type_hints["keyspace_name"])
            check_type(argname="argument partition_key_columns", value=partition_key_columns, expected_type=type_hints["partition_key_columns"])
            check_type(argname="argument billing_mode", value=billing_mode, expected_type=type_hints["billing_mode"])
            check_type(argname="argument client_side_timestamps_enabled", value=client_side_timestamps_enabled, expected_type=type_hints["client_side_timestamps_enabled"])
            check_type(argname="argument clustering_key_columns", value=clustering_key_columns, expected_type=type_hints["clustering_key_columns"])
            check_type(argname="argument default_time_to_live", value=default_time_to_live, expected_type=type_hints["default_time_to_live"])
            check_type(argname="argument encryption_specification", value=encryption_specification, expected_type=type_hints["encryption_specification"])
            check_type(argname="argument point_in_time_recovery_enabled", value=point_in_time_recovery_enabled, expected_type=type_hints["point_in_time_recovery_enabled"])
            check_type(argname="argument regular_columns", value=regular_columns, expected_type=type_hints["regular_columns"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "keyspace_name": keyspace_name,
            "partition_key_columns": partition_key_columns,
        }
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if client_side_timestamps_enabled is not None:
            self._values["client_side_timestamps_enabled"] = client_side_timestamps_enabled
        if clustering_key_columns is not None:
            self._values["clustering_key_columns"] = clustering_key_columns
        if default_time_to_live is not None:
            self._values["default_time_to_live"] = default_time_to_live
        if encryption_specification is not None:
            self._values["encryption_specification"] = encryption_specification
        if point_in_time_recovery_enabled is not None:
            self._values["point_in_time_recovery_enabled"] = point_in_time_recovery_enabled
        if regular_columns is not None:
            self._values["regular_columns"] = regular_columns
        if table_name is not None:
            self._values["table_name"] = table_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def keyspace_name(self) -> builtins.str:
        '''The name of the keyspace to create the table in.

        The keyspace must already exist.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-keyspacename
        '''
        result = self._values.get("keyspace_name")
        assert result is not None, "Required property 'keyspace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition_key_columns(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ColumnProperty]]]:
        '''One or more columns that uniquely identify every row in the table.

        Every table must have a partition key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-partitionkeycolumns
        '''
        result = self._values.get("partition_key_columns")
        assert result is not None, "Required property 'partition_key_columns' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ColumnProperty]]], result)

    @builtins.property
    def billing_mode(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.BillingModeProperty]]:
        '''The billing mode for the table, which determines how you'll be charged for reads and writes:.

        - *On-demand mode* (default) - You pay based on the actual reads and writes your application performs.
        - *Provisioned mode* - Lets you specify the number of reads and writes per second that you need for your application.

        If you don't specify a value for this property, then the table will use on-demand mode.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-billingmode
        '''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.BillingModeProperty]], result)

    @builtins.property
    def client_side_timestamps_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables client-side timestamps for the table.

        By default, the setting is disabled. You can enable client-side timestamps with the following option:

        - ``status: "enabled"``

        After client-side timestamps are enabled for a table, you can't disable this setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clientsidetimestampsenabled
        '''
        result = self._values.get("client_side_timestamps_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def clustering_key_columns(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ClusteringKeyColumnProperty]]]]:
        '''One or more columns that determine how the table data is sorted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clusteringkeycolumns
        '''
        result = self._values.get("clustering_key_columns")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ClusteringKeyColumnProperty]]]], result)

    @builtins.property
    def default_time_to_live(self) -> typing.Optional[jsii.Number]:
        '''The default Time To Live (TTL) value for all rows in a table in seconds.

        The maximum configurable value is 630,720,000 seconds, which is the equivalent of 20 years. By default, the TTL value for a table is 0, which means data does not expire.

        For more information, see `Setting the default TTL value for a table <https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl>`_ in the *Amazon Keyspaces Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-defaulttimetolive
        '''
        result = self._values.get("default_time_to_live")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption_specification(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.EncryptionSpecificationProperty]]:
        '''The encryption at rest options for the table.

        - *AWS owned key* (default) - The key is owned by Amazon Keyspaces.
        - *Customer managed key* - The key is stored in your account and is created, owned, and managed by you.

        .. epigraph::

           If you choose encryption with a customer managed key, you must specify a valid customer managed KMS key with permissions granted to Amazon Keyspaces.

        For more information, see `Encryption at rest in Amazon Keyspaces <https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html>`_ in the *Amazon Keyspaces Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-encryptionspecification
        '''
        result = self._values.get("encryption_specification")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.EncryptionSpecificationProperty]], result)

    @builtins.property
    def point_in_time_recovery_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies if point-in-time recovery is enabled or disabled for the table.

        The options are ``PointInTimeRecoveryEnabled=true`` and ``PointInTimeRecoveryEnabled=false`` . If not specified, the default is ``PointInTimeRecoveryEnabled=false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-pointintimerecoveryenabled
        '''
        result = self._values.get("point_in_time_recovery_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def regular_columns(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ColumnProperty]]]]:
        '''One or more columns that are not part of the primary key - that is, columns that are *not* defined as partition key columns or clustering key columns.

        You can add regular columns to existing tables by adding them to the template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-regularcolumns
        '''
        result = self._values.get("regular_columns")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ColumnProperty]]]], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''The name of the table to be created.

        The table name is case sensitive. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the table name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           If you specify a name, you can't perform updates that require replacing this resource. You can perform updates that require no interruption or some interruption. If you must replace the resource, specify a new name.

        *Length constraints:* Minimum length of 3. Maximum length of 255.

        *Pattern:* ``^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tablename
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnKeyspace",
    "CfnKeyspaceProps",
    "CfnTable",
    "CfnTableProps",
]

publication.publish()

def _typecheckingstub__9cd64888a8d1139f7fef90a6f2cad1bf287a6d09115cfa1d1147c1afd8f5f9e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    keyspace_name: typing.Optional[builtins.str] = None,
    replication_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKeyspace.ReplicationSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ecbad4543180c6cf4913924c148b210c77e3da9a878ec77916ea568a560458b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f60f7b87e845a932e67441bed6a8227df77e1b7945146e65d3ba8ac68a7960(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb7166642fd3aff60742c5e03d8f0094ff2d3ed08ad9f239837dfa2ef308f38(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb87739fda4abfb9cec927655958eeed2ab44c06374fbd6f52c9ff6c3303247e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKeyspace.ReplicationSpecificationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bbd84051da75f3e01d5eeefad9f72e1f8f65ba4f3cf7969332aab7dc8d01a19(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f12bad7b518911e0710e02ed64e0533c1123f35e304844dab5aaae8383b25a(
    *,
    region_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    replication_strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0263cb98dfdfc7ed9f31cf986359bcc44c1b3f3c733ebb7d3e36b25fb4cea8(
    *,
    keyspace_name: typing.Optional[builtins.str] = None,
    replication_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKeyspace.ReplicationSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6fd025c7c0c8d4a27519b568ec6952b027c14ffb932a0cd5e53f0aae4270b3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    keyspace_name: builtins.str,
    partition_key_columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
    billing_mode: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.BillingModeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    client_side_timestamps_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    clustering_key_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ClusteringKeyColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    default_time_to_live: typing.Optional[jsii.Number] = None,
    encryption_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.EncryptionSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    regular_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    table_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3024cadcd02ed175dead491b1c5e108162ba00bd9697ca0a21957570dcc30963(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2704679b24717c434c4bc09d9ffb9dbc4aee00a7925442e23bb2c107ac7a76b9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39801b43f69f67941929194d4199c85a34126143e133e315190906067d512822(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1db183d8a51a33cc93b8d90f2611025ff7f3e6539e707de86fd9a5073f0a785(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ColumnProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2219a43361bf3ff1d1bf29e1b2907d75a53df3b7016d534579938eea5d4e91d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.BillingModeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd9370f4f1ef0d5c1349ef8d576cad345ff735c9ca5c01758d25b48bfb48e5bb(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629a90c3101172766e4de27d7d3ce237b18da87338a09c0e62d788bfeb846292(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ClusteringKeyColumnProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__202d75d85d4343037389d27dd4e5938ef702777fc7f61c15eacbbb8602ec2048(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__105d2928be0de10d33f2dd6f9726d0b2413424d98fe5d151ccbce2002420a1f2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.EncryptionSpecificationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367fd6c13ef0060b69d310dfec8e4128d6d23ab9f7c5c2c6f4fde1840336b733(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c15490d5659aeda79f13514b12c87f518d6de130270ffd24df4af663b6785f59(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTable.ColumnProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e1536df40ced7d731dcea97d7afa1eab0ec4b34824d105a20130aa6fafe98ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4224e4814f153e9978b91f35f9c02cfe00615e65fb97b060775097a1c70669ec(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b57c6da9515480ece2b86b6971f8563bcf0c49dab50c8c6e234c443b8c0f9a0(
    *,
    mode: builtins.str,
    provisioned_throughput: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ProvisionedThroughputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4989a761d5af337ce8ad918b2d543390cab5ea5d5ea82741f1c3416e00d794(
    *,
    column: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]],
    order_by: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b165821558e59006460c17fc7bc14e684785b2118bea5b769002a78e310f391(
    *,
    column_name: builtins.str,
    column_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2366032cc6832a13bbd38729b1c4c9a0a38683ef6ea95cf6f8e29f0356320e0f(
    *,
    encryption_type: builtins.str,
    kms_key_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e82ecde232ad027f79eae23599756ec33659aabf2db7a5ba885d3991735a3971(
    *,
    read_capacity_units: jsii.Number,
    write_capacity_units: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd1ff29b1ec22382a7c3d14031657668106b0fcd843c06a96897bcadf10ffa92(
    *,
    keyspace_name: builtins.str,
    partition_key_columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
    billing_mode: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.BillingModeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    client_side_timestamps_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    clustering_key_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ClusteringKeyColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    default_time_to_live: typing.Optional[jsii.Number] = None,
    encryption_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.EncryptionSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    regular_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    table_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
