'''
# AWS::QLDB Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_qldb as qldb
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for QLDB construct libraries](https://constructs.dev/search?q=qldb)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::QLDB resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_QLDB.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::QLDB](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_QLDB.html).

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
class CfnLedger(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qldb.CfnLedger",
):
    '''The ``AWS::QLDB::Ledger`` resource specifies a new Amazon Quantum Ledger Database (Amazon QLDB) ledger in your AWS account .

    Amazon QLDB is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log owned by a central trusted authority. You can use QLDB to track all application data changes, and maintain a complete and verifiable history of changes over time.

    For more information, see `CreateLedger <https://docs.aws.amazon.com/qldb/latest/developerguide/API_CreateLedger.html>`_ in the *Amazon QLDB API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qldb as qldb
        
        cfn_ledger = qldb.CfnLedger(self, "MyCfnLedger",
            permissions_mode="permissionsMode",
        
            # the properties below are optional
            deletion_protection=False,
            kms_key="kmsKey",
            name="name",
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
        permissions_mode: builtins.str,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param permissions_mode: The permissions mode to assign to the ledger that you want to create. This parameter can have one of the following values: - ``ALLOW_ALL`` : A legacy permissions mode that enables access control with API-level granularity for ledgers. This mode allows users who have the ``SendCommand`` API permission for this ledger to run all PartiQL commands (hence, ``ALLOW_ALL`` ) on any tables in the specified ledger. This mode disregards any table-level or command-level IAM permissions policies that you create for the ledger. - ``STANDARD`` : ( *Recommended* ) A permissions mode that enables access control with finer granularity for ledgers, tables, and PartiQL commands. By default, this mode denies all user requests to run any PartiQL commands on any tables in this ledger. To allow PartiQL commands to run, you must create IAM permissions policies for specific table resources and PartiQL actions, in addition to the ``SendCommand`` API permission for the ledger. For information, see `Getting started with the standard permissions mode <https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-standard-mode.html>`_ in the *Amazon QLDB Developer Guide* . .. epigraph:: We strongly recommend using the ``STANDARD`` permissions mode to maximize the security of your ledger data.
        :param deletion_protection: Specifies whether the ledger is protected from being deleted by any user. If not defined during ledger creation, this feature is enabled ( ``true`` ) by default. If deletion protection is enabled, you must first disable it before you can delete the ledger. You can disable it by calling the ``UpdateLedger`` operation to set this parameter to ``false`` .
        :param kms_key: The key in AWS Key Management Service ( AWS KMS ) to use for encryption of data at rest in the ledger. For more information, see `Encryption at rest <https://docs.aws.amazon.com/qldb/latest/developerguide/encryption-at-rest.html>`_ in the *Amazon QLDB Developer Guide* . Use one of the following options to specify this parameter: - ``AWS_OWNED_KMS_KEY`` : Use an AWS KMS key that is owned and managed by AWS on your behalf. - *Undefined* : By default, use an AWS owned KMS key. - *A valid symmetric customer managed KMS key* : Use the specified symmetric encryption KMS key in your account that you create, own, and manage. Amazon QLDB does not support asymmetric keys. For more information, see `Using symmetric and asymmetric keys <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`_ in the *AWS Key Management Service Developer Guide* . To specify a customer managed KMS key, you can use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with ``"alias/"`` . To specify a key in a different AWS account , you must use the key ARN or alias ARN. For example: - Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab`` - Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` - Alias name: ``alias/ExampleAlias`` - Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`` For more information, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .
        :param name: The name of the ledger that you want to create. The name must be unique among all of the ledgers in your AWS account in the current Region. Naming constraints for ledger names are defined in `Quotas in Amazon QLDB <https://docs.aws.amazon.com/qldb/latest/developerguide/limits.html#limits.naming>`_ in the *Amazon QLDB Developer Guide* .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c3f292b1a2e3c0b8e03745ad454d7d55c22a260af8318dfec1074e774e646e1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLedgerProps(
            permissions_mode=permissions_mode,
            deletion_protection=deletion_protection,
            kms_key=kms_key,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0621f4368a524c5c6f871fd57788a125a31975fe5179220aa8651a3ab9e950c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1333ad936a34c0eec57e124b0843a7eb33e35176d234b7917f34ff098461d324)
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
    @jsii.member(jsii_name="permissionsMode")
    def permissions_mode(self) -> builtins.str:
        '''The permissions mode to assign to the ledger that you want to create.'''
        return typing.cast(builtins.str, jsii.get(self, "permissionsMode"))

    @permissions_mode.setter
    def permissions_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a89e619bca2f94e6b3db069845ba60ca02914b7a4be30253994fdf3b4d512b31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsMode", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the ledger is protected from being deleted by any user.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3fe377f100037b9cde4aff29cf5c4b1fc32e83c4f45f03c00ecf702acfa3ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The key in AWS Key Management Service ( AWS KMS ) to use for encryption of data at rest in the ledger.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07f645e3cf44ac4a544caad49252b894a50db46388e08cff021fbba2e27eac50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the ledger that you want to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfde1a1589cee060b1bc3f659b346954c99d568692b34716e284f1a4d54819c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58e2cf9516bbbe2dc95bb5894175223984cbea74e4c177e3c5a7db64d7c625c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qldb.CfnLedgerProps",
    jsii_struct_bases=[],
    name_mapping={
        "permissions_mode": "permissionsMode",
        "deletion_protection": "deletionProtection",
        "kms_key": "kmsKey",
        "name": "name",
        "tags": "tags",
    },
)
class CfnLedgerProps:
    def __init__(
        self,
        *,
        permissions_mode: builtins.str,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLedger``.

        :param permissions_mode: The permissions mode to assign to the ledger that you want to create. This parameter can have one of the following values: - ``ALLOW_ALL`` : A legacy permissions mode that enables access control with API-level granularity for ledgers. This mode allows users who have the ``SendCommand`` API permission for this ledger to run all PartiQL commands (hence, ``ALLOW_ALL`` ) on any tables in the specified ledger. This mode disregards any table-level or command-level IAM permissions policies that you create for the ledger. - ``STANDARD`` : ( *Recommended* ) A permissions mode that enables access control with finer granularity for ledgers, tables, and PartiQL commands. By default, this mode denies all user requests to run any PartiQL commands on any tables in this ledger. To allow PartiQL commands to run, you must create IAM permissions policies for specific table resources and PartiQL actions, in addition to the ``SendCommand`` API permission for the ledger. For information, see `Getting started with the standard permissions mode <https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-standard-mode.html>`_ in the *Amazon QLDB Developer Guide* . .. epigraph:: We strongly recommend using the ``STANDARD`` permissions mode to maximize the security of your ledger data.
        :param deletion_protection: Specifies whether the ledger is protected from being deleted by any user. If not defined during ledger creation, this feature is enabled ( ``true`` ) by default. If deletion protection is enabled, you must first disable it before you can delete the ledger. You can disable it by calling the ``UpdateLedger`` operation to set this parameter to ``false`` .
        :param kms_key: The key in AWS Key Management Service ( AWS KMS ) to use for encryption of data at rest in the ledger. For more information, see `Encryption at rest <https://docs.aws.amazon.com/qldb/latest/developerguide/encryption-at-rest.html>`_ in the *Amazon QLDB Developer Guide* . Use one of the following options to specify this parameter: - ``AWS_OWNED_KMS_KEY`` : Use an AWS KMS key that is owned and managed by AWS on your behalf. - *Undefined* : By default, use an AWS owned KMS key. - *A valid symmetric customer managed KMS key* : Use the specified symmetric encryption KMS key in your account that you create, own, and manage. Amazon QLDB does not support asymmetric keys. For more information, see `Using symmetric and asymmetric keys <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`_ in the *AWS Key Management Service Developer Guide* . To specify a customer managed KMS key, you can use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with ``"alias/"`` . To specify a key in a different AWS account , you must use the key ARN or alias ARN. For example: - Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab`` - Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` - Alias name: ``alias/ExampleAlias`` - Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`` For more information, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .
        :param name: The name of the ledger that you want to create. The name must be unique among all of the ledgers in your AWS account in the current Region. Naming constraints for ledger names are defined in `Quotas in Amazon QLDB <https://docs.aws.amazon.com/qldb/latest/developerguide/limits.html#limits.naming>`_ in the *Amazon QLDB Developer Guide* .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qldb as qldb
            
            cfn_ledger_props = qldb.CfnLedgerProps(
                permissions_mode="permissionsMode",
            
                # the properties below are optional
                deletion_protection=False,
                kms_key="kmsKey",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5663dfd1f46a65b8b57ab0b2e5ff5e0c5d475f06d19e33cc58dfbf6d23b9ab6a)
            check_type(argname="argument permissions_mode", value=permissions_mode, expected_type=type_hints["permissions_mode"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permissions_mode": permissions_mode,
        }
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def permissions_mode(self) -> builtins.str:
        '''The permissions mode to assign to the ledger that you want to create.

        This parameter can have one of the following values:

        - ``ALLOW_ALL`` : A legacy permissions mode that enables access control with API-level granularity for ledgers.

        This mode allows users who have the ``SendCommand`` API permission for this ledger to run all PartiQL commands (hence, ``ALLOW_ALL`` ) on any tables in the specified ledger. This mode disregards any table-level or command-level IAM permissions policies that you create for the ledger.

        - ``STANDARD`` : ( *Recommended* ) A permissions mode that enables access control with finer granularity for ledgers, tables, and PartiQL commands.

        By default, this mode denies all user requests to run any PartiQL commands on any tables in this ledger. To allow PartiQL commands to run, you must create IAM permissions policies for specific table resources and PartiQL actions, in addition to the ``SendCommand`` API permission for the ledger. For information, see `Getting started with the standard permissions mode <https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-standard-mode.html>`_ in the *Amazon QLDB Developer Guide* .
        .. epigraph::

           We strongly recommend using the ``STANDARD`` permissions mode to maximize the security of your ledger data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-permissionsmode
        '''
        result = self._values.get("permissions_mode")
        assert result is not None, "Required property 'permissions_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the ledger is protected from being deleted by any user.

        If not defined during ledger creation, this feature is enabled ( ``true`` ) by default.

        If deletion protection is enabled, you must first disable it before you can delete the ledger. You can disable it by calling the ``UpdateLedger`` operation to set this parameter to ``false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-deletionprotection
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The key in AWS Key Management Service ( AWS KMS ) to use for encryption of data at rest in the ledger.

        For more information, see `Encryption at rest <https://docs.aws.amazon.com/qldb/latest/developerguide/encryption-at-rest.html>`_ in the *Amazon QLDB Developer Guide* .

        Use one of the following options to specify this parameter:

        - ``AWS_OWNED_KMS_KEY`` : Use an AWS KMS key that is owned and managed by AWS on your behalf.
        - *Undefined* : By default, use an AWS owned KMS key.
        - *A valid symmetric customer managed KMS key* : Use the specified symmetric encryption KMS key in your account that you create, own, and manage.

        Amazon QLDB does not support asymmetric keys. For more information, see `Using symmetric and asymmetric keys <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`_ in the *AWS Key Management Service Developer Guide* .

        To specify a customer managed KMS key, you can use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with ``"alias/"`` . To specify a key in a different AWS account , you must use the key ARN or alias ARN.

        For example:

        - Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``
        - Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``
        - Alias name: ``alias/ExampleAlias``
        - Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

        For more information, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-kmskey
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the ledger that you want to create.

        The name must be unique among all of the ledgers in your AWS account in the current Region.

        Naming constraints for ledger names are defined in `Quotas in Amazon QLDB <https://docs.aws.amazon.com/qldb/latest/developerguide/limits.html#limits.naming>`_ in the *Amazon QLDB Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLedgerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qldb.CfnStream",
):
    '''The ``AWS::QLDB::Stream`` resource specifies a journal stream for a given Amazon Quantum Ledger Database (Amazon QLDB) ledger.

    The stream captures every document revision that is committed to the ledger's journal and delivers the data to a specified Amazon Kinesis Data Streams resource.

    For more information, see `StreamJournalToKinesis <https://docs.aws.amazon.com/qldb/latest/developerguide/API_StreamJournalToKinesis.html>`_ in the *Amazon QLDB API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qldb as qldb
        
        cfn_stream = qldb.CfnStream(self, "MyCfnStream",
            inclusive_start_time="inclusiveStartTime",
            kinesis_configuration=qldb.CfnStream.KinesisConfigurationProperty(
                aggregation_enabled=False,
                stream_arn="streamArn"
            ),
            ledger_name="ledgerName",
            role_arn="roleArn",
            stream_name="streamName",
        
            # the properties below are optional
            exclusive_end_time="exclusiveEndTime",
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
        inclusive_start_time: builtins.str,
        kinesis_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnStream.KinesisConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ledger_name: builtins.str,
        role_arn: builtins.str,
        stream_name: builtins.str,
        exclusive_end_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param inclusive_start_time: The inclusive start date and time from which to start streaming journal data. This parameter must be in ``ISO 8601`` date and time format and in Universal Coordinated Time (UTC). For example: ``2019-06-13T21:36:34Z`` . The ``InclusiveStartTime`` cannot be in the future and must be before ``ExclusiveEndTime`` . If you provide an ``InclusiveStartTime`` that is before the ledger's ``CreationDateTime`` , QLDB effectively defaults it to the ledger's ``CreationDateTime`` .
        :param kinesis_configuration: The configuration settings of the Kinesis Data Streams destination for your stream request.
        :param ledger_name: The name of the ledger.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource. To pass a role to QLDB when requesting a journal stream, you must have permissions to perform the ``iam:PassRole`` action on the IAM role resource. This is required for all journal stream requests.
        :param stream_name: The name that you want to assign to the QLDB journal stream. User-defined names can help identify and indicate the purpose of a stream. Your stream name must be unique among other *active* streams for a given ledger. Stream names have the same naming constraints as ledger names, as defined in `Quotas in Amazon QLDB <https://docs.aws.amazon.com/qldb/latest/developerguide/limits.html#limits.naming>`_ in the *Amazon QLDB Developer Guide* .
        :param exclusive_end_time: The exclusive date and time that specifies when the stream ends. If you don't define this parameter, the stream runs indefinitely until you cancel it. The ``ExclusiveEndTime`` must be in ``ISO 8601`` date and time format and in Universal Coordinated Time (UTC). For example: ``2019-06-13T21:36:34Z`` .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19df9eb6d681fce76d2012fd0458a104b842f687fd7aed1f8d9228e06237dd81)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStreamProps(
            inclusive_start_time=inclusive_start_time,
            kinesis_configuration=kinesis_configuration,
            ledger_name=ledger_name,
            role_arn=role_arn,
            stream_name=stream_name,
            exclusive_end_time=exclusive_end_time,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c38c9a1489b8399636d442738d91441e35ce1cb927b06d8f5e6f31f309fad04a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d55e80f8f1370044fb71f0be38faec90cf33f456ea63398b22c1c99d0dab1444)
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
        '''The Amazon Resource Name (ARN) of the QLDB journal stream.

        For example: ``arn:aws:qldb:us-east-1:123456789012:stream/exampleLedger/IiPT4brpZCqCq3f4MTHbYy`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique ID that QLDB assigns to each QLDB journal stream.

        For example: ``IiPT4brpZCqCq3f4MTHbYy`` .

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
    @jsii.member(jsii_name="inclusiveStartTime")
    def inclusive_start_time(self) -> builtins.str:
        '''The inclusive start date and time from which to start streaming journal data.'''
        return typing.cast(builtins.str, jsii.get(self, "inclusiveStartTime"))

    @inclusive_start_time.setter
    def inclusive_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98852a683dfa8f48ad68fade55a237fb8421da0a42caa793d1e506b577528b38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inclusiveStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisConfiguration")
    def kinesis_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnStream.KinesisConfigurationProperty"]:
        '''The configuration settings of the Kinesis Data Streams destination for your stream request.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnStream.KinesisConfigurationProperty"], jsii.get(self, "kinesisConfiguration"))

    @kinesis_configuration.setter
    def kinesis_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnStream.KinesisConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc6c4472587c14cb453d825bb83db5d8c8df52f82dc984a4b40efc1c0f286846)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="ledgerName")
    def ledger_name(self) -> builtins.str:
        '''The name of the ledger.'''
        return typing.cast(builtins.str, jsii.get(self, "ledgerName"))

    @ledger_name.setter
    def ledger_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6048b29c86a9998034ea99f673393704baf93a9e74b9f3e2ea5bbe93b50fa0bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ledgerName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd91303c2c186e90b4e369eb657ba366bf0edc3558f26866550b418fe3f583bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> builtins.str:
        '''The name that you want to assign to the QLDB journal stream.'''
        return typing.cast(builtins.str, jsii.get(self, "streamName"))

    @stream_name.setter
    def stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65cc267bb8854cc73f45ea241375801dfe4be3ef971d88b415f3ecccea7af533)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamName", value)

    @builtins.property
    @jsii.member(jsii_name="exclusiveEndTime")
    def exclusive_end_time(self) -> typing.Optional[builtins.str]:
        '''The exclusive date and time that specifies when the stream ends.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exclusiveEndTime"))

    @exclusive_end_time.setter
    def exclusive_end_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b48c9fdb3c49a64c92e0f14d06caf7bccd874ef18eb40d50afff5b659c32f61d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusiveEndTime", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d506c15c7a106af08f12f6afdaa8ae0bdae79b69d9147fee716935cb73e72b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qldb.CfnStream.KinesisConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation_enabled": "aggregationEnabled",
            "stream_arn": "streamArn",
        },
    )
    class KinesisConfigurationProperty:
        def __init__(
            self,
            *,
            aggregation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            stream_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration settings of the Amazon Kinesis Data Streams destination for an Amazon QLDB journal stream.

            :param aggregation_enabled: Enables QLDB to publish multiple data records in a single Kinesis Data Streams record, increasing the number of records sent per API call. Default: ``True`` .. epigraph:: Record aggregation has important implications for processing records and requires de-aggregation in your stream consumer. To learn more, see `KPL Key Concepts <https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-concepts.html>`_ and `Consumer De-aggregation <https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-consumer-deaggregation.html>`_ in the *Amazon Kinesis Data Streams Developer Guide* .
            :param stream_arn: The Amazon Resource Name (ARN) of the Kinesis Data Streams resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qldb as qldb
                
                kinesis_configuration_property = qldb.CfnStream.KinesisConfigurationProperty(
                    aggregation_enabled=False,
                    stream_arn="streamArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__84d94b9a3158f284a06b6624c8254b032e304f833d0a315233a79e237ddb1fa8)
                check_type(argname="argument aggregation_enabled", value=aggregation_enabled, expected_type=type_hints["aggregation_enabled"])
                check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aggregation_enabled is not None:
                self._values["aggregation_enabled"] = aggregation_enabled
            if stream_arn is not None:
                self._values["stream_arn"] = stream_arn

        @builtins.property
        def aggregation_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables QLDB to publish multiple data records in a single Kinesis Data Streams record, increasing the number of records sent per API call.

            Default: ``True``
            .. epigraph::

               Record aggregation has important implications for processing records and requires de-aggregation in your stream consumer. To learn more, see `KPL Key Concepts <https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-concepts.html>`_ and `Consumer De-aggregation <https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-consumer-deaggregation.html>`_ in the *Amazon Kinesis Data Streams Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-aggregationenabled
            '''
            result = self._values.get("aggregation_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def stream_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Kinesis Data Streams resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-streamarn
            '''
            result = self._values.get("stream_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qldb.CfnStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "inclusive_start_time": "inclusiveStartTime",
        "kinesis_configuration": "kinesisConfiguration",
        "ledger_name": "ledgerName",
        "role_arn": "roleArn",
        "stream_name": "streamName",
        "exclusive_end_time": "exclusiveEndTime",
        "tags": "tags",
    },
)
class CfnStreamProps:
    def __init__(
        self,
        *,
        inclusive_start_time: builtins.str,
        kinesis_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStream.KinesisConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        ledger_name: builtins.str,
        role_arn: builtins.str,
        stream_name: builtins.str,
        exclusive_end_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStream``.

        :param inclusive_start_time: The inclusive start date and time from which to start streaming journal data. This parameter must be in ``ISO 8601`` date and time format and in Universal Coordinated Time (UTC). For example: ``2019-06-13T21:36:34Z`` . The ``InclusiveStartTime`` cannot be in the future and must be before ``ExclusiveEndTime`` . If you provide an ``InclusiveStartTime`` that is before the ledger's ``CreationDateTime`` , QLDB effectively defaults it to the ledger's ``CreationDateTime`` .
        :param kinesis_configuration: The configuration settings of the Kinesis Data Streams destination for your stream request.
        :param ledger_name: The name of the ledger.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource. To pass a role to QLDB when requesting a journal stream, you must have permissions to perform the ``iam:PassRole`` action on the IAM role resource. This is required for all journal stream requests.
        :param stream_name: The name that you want to assign to the QLDB journal stream. User-defined names can help identify and indicate the purpose of a stream. Your stream name must be unique among other *active* streams for a given ledger. Stream names have the same naming constraints as ledger names, as defined in `Quotas in Amazon QLDB <https://docs.aws.amazon.com/qldb/latest/developerguide/limits.html#limits.naming>`_ in the *Amazon QLDB Developer Guide* .
        :param exclusive_end_time: The exclusive date and time that specifies when the stream ends. If you don't define this parameter, the stream runs indefinitely until you cancel it. The ``ExclusiveEndTime`` must be in ``ISO 8601`` date and time format and in Universal Coordinated Time (UTC). For example: ``2019-06-13T21:36:34Z`` .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qldb as qldb
            
            cfn_stream_props = qldb.CfnStreamProps(
                inclusive_start_time="inclusiveStartTime",
                kinesis_configuration=qldb.CfnStream.KinesisConfigurationProperty(
                    aggregation_enabled=False,
                    stream_arn="streamArn"
                ),
                ledger_name="ledgerName",
                role_arn="roleArn",
                stream_name="streamName",
            
                # the properties below are optional
                exclusive_end_time="exclusiveEndTime",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93b24971535d3527d042ac4bb7ac175f1193a6f26f891b339dd6cbadd998ce9f)
            check_type(argname="argument inclusive_start_time", value=inclusive_start_time, expected_type=type_hints["inclusive_start_time"])
            check_type(argname="argument kinesis_configuration", value=kinesis_configuration, expected_type=type_hints["kinesis_configuration"])
            check_type(argname="argument ledger_name", value=ledger_name, expected_type=type_hints["ledger_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
            check_type(argname="argument exclusive_end_time", value=exclusive_end_time, expected_type=type_hints["exclusive_end_time"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "inclusive_start_time": inclusive_start_time,
            "kinesis_configuration": kinesis_configuration,
            "ledger_name": ledger_name,
            "role_arn": role_arn,
            "stream_name": stream_name,
        }
        if exclusive_end_time is not None:
            self._values["exclusive_end_time"] = exclusive_end_time
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def inclusive_start_time(self) -> builtins.str:
        '''The inclusive start date and time from which to start streaming journal data.

        This parameter must be in ``ISO 8601`` date and time format and in Universal Coordinated Time (UTC). For example: ``2019-06-13T21:36:34Z`` .

        The ``InclusiveStartTime`` cannot be in the future and must be before ``ExclusiveEndTime`` .

        If you provide an ``InclusiveStartTime`` that is before the ledger's ``CreationDateTime`` , QLDB effectively defaults it to the ledger's ``CreationDateTime`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-inclusivestarttime
        '''
        result = self._values.get("inclusive_start_time")
        assert result is not None, "Required property 'inclusive_start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kinesis_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnStream.KinesisConfigurationProperty]:
        '''The configuration settings of the Kinesis Data Streams destination for your stream request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-kinesisconfiguration
        '''
        result = self._values.get("kinesis_configuration")
        assert result is not None, "Required property 'kinesis_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnStream.KinesisConfigurationProperty], result)

    @builtins.property
    def ledger_name(self) -> builtins.str:
        '''The name of the ledger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-ledgername
        '''
        result = self._values.get("ledger_name")
        assert result is not None, "Required property 'ledger_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource.

        To pass a role to QLDB when requesting a journal stream, you must have permissions to perform the ``iam:PassRole`` action on the IAM role resource. This is required for all journal stream requests.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_name(self) -> builtins.str:
        '''The name that you want to assign to the QLDB journal stream.

        User-defined names can help identify and indicate the purpose of a stream.

        Your stream name must be unique among other *active* streams for a given ledger. Stream names have the same naming constraints as ledger names, as defined in `Quotas in Amazon QLDB <https://docs.aws.amazon.com/qldb/latest/developerguide/limits.html#limits.naming>`_ in the *Amazon QLDB Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-streamname
        '''
        result = self._values.get("stream_name")
        assert result is not None, "Required property 'stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusive_end_time(self) -> typing.Optional[builtins.str]:
        '''The exclusive date and time that specifies when the stream ends.

        If you don't define this parameter, the stream runs indefinitely until you cancel it.

        The ``ExclusiveEndTime`` must be in ``ISO 8601`` date and time format and in Universal Coordinated Time (UTC). For example: ``2019-06-13T21:36:34Z`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-exclusiveendtime
        '''
        result = self._values.get("exclusive_end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLedger",
    "CfnLedgerProps",
    "CfnStream",
    "CfnStreamProps",
]

publication.publish()

def _typecheckingstub__6c3f292b1a2e3c0b8e03745ad454d7d55c22a260af8318dfec1074e774e646e1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    permissions_mode: builtins.str,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0621f4368a524c5c6f871fd57788a125a31975fe5179220aa8651a3ab9e950c7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1333ad936a34c0eec57e124b0843a7eb33e35176d234b7917f34ff098461d324(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a89e619bca2f94e6b3db069845ba60ca02914b7a4be30253994fdf3b4d512b31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3fe377f100037b9cde4aff29cf5c4b1fc32e83c4f45f03c00ecf702acfa3ec(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f645e3cf44ac4a544caad49252b894a50db46388e08cff021fbba2e27eac50(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfde1a1589cee060b1bc3f659b346954c99d568692b34716e284f1a4d54819c5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58e2cf9516bbbe2dc95bb5894175223984cbea74e4c177e3c5a7db64d7c625c6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5663dfd1f46a65b8b57ab0b2e5ff5e0c5d475f06d19e33cc58dfbf6d23b9ab6a(
    *,
    permissions_mode: builtins.str,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19df9eb6d681fce76d2012fd0458a104b842f687fd7aed1f8d9228e06237dd81(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    inclusive_start_time: builtins.str,
    kinesis_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStream.KinesisConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    ledger_name: builtins.str,
    role_arn: builtins.str,
    stream_name: builtins.str,
    exclusive_end_time: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c38c9a1489b8399636d442738d91441e35ce1cb927b06d8f5e6f31f309fad04a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d55e80f8f1370044fb71f0be38faec90cf33f456ea63398b22c1c99d0dab1444(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98852a683dfa8f48ad68fade55a237fb8421da0a42caa793d1e506b577528b38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc6c4472587c14cb453d825bb83db5d8c8df52f82dc984a4b40efc1c0f286846(
    value: typing.Union[_IResolvable_da3f097b, CfnStream.KinesisConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6048b29c86a9998034ea99f673393704baf93a9e74b9f3e2ea5bbe93b50fa0bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd91303c2c186e90b4e369eb657ba366bf0edc3558f26866550b418fe3f583bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65cc267bb8854cc73f45ea241375801dfe4be3ef971d88b415f3ecccea7af533(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b48c9fdb3c49a64c92e0f14d06caf7bccd874ef18eb40d50afff5b659c32f61d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d506c15c7a106af08f12f6afdaa8ae0bdae79b69d9147fee716935cb73e72b1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d94b9a3158f284a06b6624c8254b032e304f833d0a315233a79e237ddb1fa8(
    *,
    aggregation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    stream_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93b24971535d3527d042ac4bb7ac175f1193a6f26f891b339dd6cbadd998ce9f(
    *,
    inclusive_start_time: builtins.str,
    kinesis_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStream.KinesisConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    ledger_name: builtins.str,
    role_arn: builtins.str,
    stream_name: builtins.str,
    exclusive_end_time: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
