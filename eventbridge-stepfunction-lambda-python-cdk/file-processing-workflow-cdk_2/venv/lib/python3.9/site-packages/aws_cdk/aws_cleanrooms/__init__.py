'''
# AWS::CleanRooms Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cleanrooms as cleanrooms
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CleanRooms construct libraries](https://constructs.dev/search?q=cleanrooms)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CleanRooms resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRooms.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CleanRooms](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRooms.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnCollaboration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration",
):
    '''Creates a new collaboration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_collaboration = cleanrooms.CfnCollaboration(self, "MyCfnCollaboration",
            creator_display_name="creatorDisplayName",
            creator_member_abilities=["creatorMemberAbilities"],
            description="description",
            members=[cleanrooms.CfnCollaboration.MemberSpecificationProperty(
                account_id="accountId",
                display_name="displayName",
                member_abilities=["memberAbilities"]
            )],
            name="name",
            query_log_status="queryLogStatus",
        
            # the properties below are optional
            data_encryption_metadata=cleanrooms.CfnCollaboration.DataEncryptionMetadataProperty(
                allow_cleartext=False,
                allow_duplicates=False,
                allow_joins_on_columns_with_different_names=False,
                preserve_nulls=False
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
        creator_display_name: builtins.str,
        creator_member_abilities: typing.Sequence[builtins.str],
        description: builtins.str,
        members: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.MemberSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        query_log_status: builtins.str,
        data_encryption_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.DataEncryptionMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param creator_display_name: A display name of the collaboration creator.
        :param creator_member_abilities: The abilities granted to the collaboration creator.
        :param description: A description of the collaboration provided by the collaboration owner.
        :param members: A list of initial members, not including the creator. This list is immutable.
        :param name: A human-readable identifier provided by the collaboration owner. Display names are not unique.
        :param query_log_status: An indicator as to whether query logging has been enabled or disabled for the collaboration.
        :param data_encryption_metadata: The settings for client-side encryption for cryptographic computing.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8995527da9ce4212caf3c1fdf601e4947c02ff1e364e92811ac8635be534111)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCollaborationProps(
            creator_display_name=creator_display_name,
            creator_member_abilities=creator_member_abilities,
            description=description,
            members=members,
            name=name,
            query_log_status=query_log_status,
            data_encryption_metadata=data_encryption_metadata,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b0d208a10b53d5d7bf8e19cff7b1a7be86094960aa43579972861d563de44d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a9705b5c9f28f1d364782d5cb996ee4fe0e93dc0fbee1871bc10feeb5a547d9)
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
        '''Returns the Amazon Resource Name (ARN) of the specified collaboration.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:collaboration/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationIdentifier")
    def attr_collaboration_identifier(self) -> builtins.str:
        '''Returns the unique identifier of the specified collaboration.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: CollaborationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="creatorDisplayName")
    def creator_display_name(self) -> builtins.str:
        '''A display name of the collaboration creator.'''
        return typing.cast(builtins.str, jsii.get(self, "creatorDisplayName"))

    @creator_display_name.setter
    def creator_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9f17060755de314c6aea7e9fe1c03f18e31972fafbe5d1edf10b18250f60ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creatorDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="creatorMemberAbilities")
    def creator_member_abilities(self) -> typing.List[builtins.str]:
        '''The abilities granted to the collaboration creator.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creatorMemberAbilities"))

    @creator_member_abilities.setter
    def creator_member_abilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ee81f8b64fd681cae1a860e0339dfa0ddeb287c4e709f0b34cc3c8bcf9bc6bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creatorMemberAbilities", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description of the collaboration provided by the collaboration owner.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb5edb6a58e1c0f33620eadb56126089a140277fe87954ea4d3a06146b3559ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MemberSpecificationProperty"]]]:
        '''A list of initial members, not including the creator.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MemberSpecificationProperty"]]], jsii.get(self, "members"))

    @members.setter
    def members(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MemberSpecificationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e816963af09a7c3bdf0ca05211222f43d66929e9fa8216fe82e8fb6e27493bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A human-readable identifier provided by the collaboration owner.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__585aa64e1eeaa11003c987d7230a1772b0683c9f8866457214d0242ba9d00d4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="queryLogStatus")
    def query_log_status(self) -> builtins.str:
        '''An indicator as to whether query logging has been enabled or disabled for the collaboration.'''
        return typing.cast(builtins.str, jsii.get(self, "queryLogStatus"))

    @query_log_status.setter
    def query_log_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa852049fd80eee6c2543d7576eb0c8f60a43d90ca97006450c31d8a1ed9df20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryLogStatus", value)

    @builtins.property
    @jsii.member(jsii_name="dataEncryptionMetadata")
    def data_encryption_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.DataEncryptionMetadataProperty"]]:
        '''The settings for client-side encryption for cryptographic computing.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.DataEncryptionMetadataProperty"]], jsii.get(self, "dataEncryptionMetadata"))

    @data_encryption_metadata.setter
    def data_encryption_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.DataEncryptionMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86b18a30aac6a5afc1830c4adb282d4f0f3199f7c3d3ce99ffb24dad829a6eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataEncryptionMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06877122efbe5bc41c92999ba727597f48590c383378ee73a94c91fe43305e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.DataEncryptionMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_cleartext": "allowCleartext",
            "allow_duplicates": "allowDuplicates",
            "allow_joins_on_columns_with_different_names": "allowJoinsOnColumnsWithDifferentNames",
            "preserve_nulls": "preserveNulls",
        },
    )
    class DataEncryptionMetadataProperty:
        def __init__(
            self,
            *,
            allow_cleartext: typing.Union[builtins.bool, _IResolvable_da3f097b],
            allow_duplicates: typing.Union[builtins.bool, _IResolvable_da3f097b],
            allow_joins_on_columns_with_different_names: typing.Union[builtins.bool, _IResolvable_da3f097b],
            preserve_nulls: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''The settings for client-side encryption for cryptographic computing.

            :param allow_cleartext: Indicates whether encrypted tables can contain cleartext data (true) or are to cryptographically process every column (false).
            :param allow_duplicates: Indicates whether Fingerprint columns can contain duplicate entries (true) or are to contain only non-repeated values (false).
            :param allow_joins_on_columns_with_different_names: Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name (true) or can only be joined on Fingerprint columns of the same name (false).
            :param preserve_nulls: Indicates whether NULL values are to be copied as NULL to encrypted tables (true) or cryptographically processed (false).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                data_encryption_metadata_property = cleanrooms.CfnCollaboration.DataEncryptionMetadataProperty(
                    allow_cleartext=False,
                    allow_duplicates=False,
                    allow_joins_on_columns_with_different_names=False,
                    preserve_nulls=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1d5c25162d0eabd19a06fd0a1ec26adcd8d8a0d12434d6ee8fbec8e27c21965)
                check_type(argname="argument allow_cleartext", value=allow_cleartext, expected_type=type_hints["allow_cleartext"])
                check_type(argname="argument allow_duplicates", value=allow_duplicates, expected_type=type_hints["allow_duplicates"])
                check_type(argname="argument allow_joins_on_columns_with_different_names", value=allow_joins_on_columns_with_different_names, expected_type=type_hints["allow_joins_on_columns_with_different_names"])
                check_type(argname="argument preserve_nulls", value=preserve_nulls, expected_type=type_hints["preserve_nulls"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_cleartext": allow_cleartext,
                "allow_duplicates": allow_duplicates,
                "allow_joins_on_columns_with_different_names": allow_joins_on_columns_with_different_names,
                "preserve_nulls": preserve_nulls,
            }

        @builtins.property
        def allow_cleartext(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether encrypted tables can contain cleartext data (true) or are to cryptographically process every column (false).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowcleartext
            '''
            result = self._values.get("allow_cleartext")
            assert result is not None, "Required property 'allow_cleartext' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def allow_duplicates(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether Fingerprint columns can contain duplicate entries (true) or are to contain only non-repeated values (false).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowduplicates
            '''
            result = self._values.get("allow_duplicates")
            assert result is not None, "Required property 'allow_duplicates' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def allow_joins_on_columns_with_different_names(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name (true) or can only be joined on Fingerprint columns of the same name (false).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowjoinsoncolumnswithdifferentnames
            '''
            result = self._values.get("allow_joins_on_columns_with_different_names")
            assert result is not None, "Required property 'allow_joins_on_columns_with_different_names' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def preserve_nulls(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether NULL values are to be copied as NULL to encrypted tables (true) or cryptographically processed (false).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-preservenulls
            '''
            result = self._values.get("preserve_nulls")
            assert result is not None, "Required property 'preserve_nulls' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataEncryptionMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.MemberSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "display_name": "displayName",
            "member_abilities": "memberAbilities",
        },
    )
    class MemberSpecificationProperty:
        def __init__(
            self,
            *,
            account_id: builtins.str,
            display_name: builtins.str,
            member_abilities: typing.Sequence[builtins.str],
        ) -> None:
            '''Basic metadata used to construct a new member.

            :param account_id: The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
            :param display_name: The member's display name.
            :param member_abilities: The abilities granted to the collaboration member. *Allowed Values* : ``CAN_QUERY`` | ``CAN_RECEIVE_RESULTS``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                member_specification_property = cleanrooms.CfnCollaboration.MemberSpecificationProperty(
                    account_id="accountId",
                    display_name="displayName",
                    member_abilities=["memberAbilities"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c9d415168b79c297b7313d0c42362a70fed420b1dda08e496b99813fbbd3248)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
                check_type(argname="argument member_abilities", value=member_abilities, expected_type=type_hints["member_abilities"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_id": account_id,
                "display_name": display_name,
                "member_abilities": member_abilities,
            }

        @builtins.property
        def account_id(self) -> builtins.str:
            '''The identifier used to reference members of the collaboration.

            Currently only supports AWS account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-accountid
            '''
            result = self._values.get("account_id")
            assert result is not None, "Required property 'account_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def display_name(self) -> builtins.str:
            '''The member's display name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-displayname
            '''
            result = self._values.get("display_name")
            assert result is not None, "Required property 'display_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def member_abilities(self) -> typing.List[builtins.str]:
            '''The abilities granted to the collaboration member.

            *Allowed Values* : ``CAN_QUERY`` | ``CAN_RECEIVE_RESULTS``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-memberabilities
            '''
            result = self._values.get("member_abilities")
            assert result is not None, "Required property 'member_abilities' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaborationProps",
    jsii_struct_bases=[],
    name_mapping={
        "creator_display_name": "creatorDisplayName",
        "creator_member_abilities": "creatorMemberAbilities",
        "description": "description",
        "members": "members",
        "name": "name",
        "query_log_status": "queryLogStatus",
        "data_encryption_metadata": "dataEncryptionMetadata",
        "tags": "tags",
    },
)
class CfnCollaborationProps:
    def __init__(
        self,
        *,
        creator_display_name: builtins.str,
        creator_member_abilities: typing.Sequence[builtins.str],
        description: builtins.str,
        members: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MemberSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        query_log_status: builtins.str,
        data_encryption_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.DataEncryptionMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCollaboration``.

        :param creator_display_name: A display name of the collaboration creator.
        :param creator_member_abilities: The abilities granted to the collaboration creator.
        :param description: A description of the collaboration provided by the collaboration owner.
        :param members: A list of initial members, not including the creator. This list is immutable.
        :param name: A human-readable identifier provided by the collaboration owner. Display names are not unique.
        :param query_log_status: An indicator as to whether query logging has been enabled or disabled for the collaboration.
        :param data_encryption_metadata: The settings for client-side encryption for cryptographic computing.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_collaboration_props = cleanrooms.CfnCollaborationProps(
                creator_display_name="creatorDisplayName",
                creator_member_abilities=["creatorMemberAbilities"],
                description="description",
                members=[cleanrooms.CfnCollaboration.MemberSpecificationProperty(
                    account_id="accountId",
                    display_name="displayName",
                    member_abilities=["memberAbilities"]
                )],
                name="name",
                query_log_status="queryLogStatus",
            
                # the properties below are optional
                data_encryption_metadata=cleanrooms.CfnCollaboration.DataEncryptionMetadataProperty(
                    allow_cleartext=False,
                    allow_duplicates=False,
                    allow_joins_on_columns_with_different_names=False,
                    preserve_nulls=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2049291a9933df94c4258b33838a3aa8100d0214a4519c3d84e6d70ed724c55d)
            check_type(argname="argument creator_display_name", value=creator_display_name, expected_type=type_hints["creator_display_name"])
            check_type(argname="argument creator_member_abilities", value=creator_member_abilities, expected_type=type_hints["creator_member_abilities"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query_log_status", value=query_log_status, expected_type=type_hints["query_log_status"])
            check_type(argname="argument data_encryption_metadata", value=data_encryption_metadata, expected_type=type_hints["data_encryption_metadata"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "creator_display_name": creator_display_name,
            "creator_member_abilities": creator_member_abilities,
            "description": description,
            "members": members,
            "name": name,
            "query_log_status": query_log_status,
        }
        if data_encryption_metadata is not None:
            self._values["data_encryption_metadata"] = data_encryption_metadata
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def creator_display_name(self) -> builtins.str:
        '''A display name of the collaboration creator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-creatordisplayname
        '''
        result = self._values.get("creator_display_name")
        assert result is not None, "Required property 'creator_display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def creator_member_abilities(self) -> typing.List[builtins.str]:
        '''The abilities granted to the collaboration creator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-creatormemberabilities
        '''
        result = self._values.get("creator_member_abilities")
        assert result is not None, "Required property 'creator_member_abilities' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> builtins.str:
        '''A description of the collaboration provided by the collaboration owner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def members(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MemberSpecificationProperty]]]:
        '''A list of initial members, not including the creator.

        This list is immutable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-members
        '''
        result = self._values.get("members")
        assert result is not None, "Required property 'members' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MemberSpecificationProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A human-readable identifier provided by the collaboration owner.

        Display names are not unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_log_status(self) -> builtins.str:
        '''An indicator as to whether query logging has been enabled or disabled for the collaboration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-querylogstatus
        '''
        result = self._values.get("query_log_status")
        assert result is not None, "Required property 'query_log_status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_encryption_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.DataEncryptionMetadataProperty]]:
        '''The settings for client-side encryption for cryptographic computing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-dataencryptionmetadata
        '''
        result = self._values.get("data_encryption_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.DataEncryptionMetadataProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollaborationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConfiguredTable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable",
):
    '''Creates a new configured table resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_configured_table = cleanrooms.CfnConfiguredTable(self, "MyCfnConfiguredTable",
            allowed_columns=["allowedColumns"],
            analysis_method="analysisMethod",
            name="name",
            table_reference=cleanrooms.CfnConfiguredTable.TableReferenceProperty(
                glue=cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty(
                    database_name="databaseName",
                    table_name="tableName"
                )
            ),
        
            # the properties below are optional
            analysis_rules=[cleanrooms.CfnConfiguredTable.AnalysisRuleProperty(
                policy=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty(
                    v1=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                        aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                            aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                                column_names=["columnNames"],
                                function="function"
                            )],
                            dimension_columns=["dimensionColumns"],
                            join_columns=["joinColumns"],
                            output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                                column_name="columnName",
                                minimum=123,
                                type="type"
                            )],
                            scalar_functions=["scalarFunctions"],
        
                            # the properties below are optional
                            allowed_join_operators=["allowedJoinOperators"],
                            join_required="joinRequired"
                        ),
                        list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                            join_columns=["joinColumns"],
                            list_columns=["listColumns"],
        
                            # the properties below are optional
                            allowed_join_operators=["allowedJoinOperators"]
                        )
                    )
                ),
                type="type"
            )],
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
        allowed_columns: typing.Sequence[builtins.str],
        analysis_method: builtins.str,
        name: builtins.str,
        table_reference: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.TableReferenceProperty", typing.Dict[builtins.str, typing.Any]]],
        analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AnalysisRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param allowed_columns: The columns within the underlying AWS Glue table that can be utilized within collaborations.
        :param analysis_method: The analysis method for the configured table. The only valid value is currently ``DIRECT_QUERY``.
        :param name: A name for the configured table.
        :param table_reference: The AWS Glue table that this configured table represents.
        :param analysis_rules: The entire created analysis rule.
        :param description: A description for the configured table.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6da68c3fc7e3c0674ddb5e2082cfb964074dd6f86f1df6dfcede15001d6f1259)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfiguredTableProps(
            allowed_columns=allowed_columns,
            analysis_method=analysis_method,
            name=name,
            table_reference=table_reference,
            analysis_rules=analysis_rules,
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
            type_hints = typing.get_type_hints(_typecheckingstub__fecfad26837cc2fdccacfdfb035a18dcac563292f6d300d8052bc89207ae04fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5c9224380ccb774fe3599e8c47969dd65412118923ba36f2fc0d722c916638e)
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
        '''Returns the Amazon Resource Name (ARN) of the specified configured table.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:configuredtable/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConfiguredTableIdentifier")
    def attr_configured_table_identifier(self) -> builtins.str:
        '''Returns the unique identifier of the specified configured table.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE33333``

        :cloudformationAttribute: ConfiguredTableIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfiguredTableIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="allowedColumns")
    def allowed_columns(self) -> typing.List[builtins.str]:
        '''The columns within the underlying AWS Glue table that can be utilized within collaborations.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedColumns"))

    @allowed_columns.setter
    def allowed_columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e6aec85126d8c2d12db0e5442b4d56c199d90e95cd9b98b1c92b7652d7c7eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedColumns", value)

    @builtins.property
    @jsii.member(jsii_name="analysisMethod")
    def analysis_method(self) -> builtins.str:
        '''The analysis method for the configured table.'''
        return typing.cast(builtins.str, jsii.get(self, "analysisMethod"))

    @analysis_method.setter
    def analysis_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd16c3f5e30018a39bada3627e112c5d99eea9283a9ad2de82b9790911c3169)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analysisMethod", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the configured table.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8743fd9932eb6c0afe523245bfc3bc611bed75b8e179806716cdbd7e1e97f817)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tableReference")
    def table_reference(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.TableReferenceProperty"]:
        '''The AWS Glue table that this configured table represents.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.TableReferenceProperty"], jsii.get(self, "tableReference"))

    @table_reference.setter
    def table_reference(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.TableReferenceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81f7eaa704c6766bfee1be9d2d2b0c8cc4751fd3eb996d6d9902238bdc710232)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableReference", value)

    @builtins.property
    @jsii.member(jsii_name="analysisRules")
    def analysis_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleProperty"]]]]:
        '''The entire created analysis rule.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleProperty"]]]], jsii.get(self, "analysisRules"))

    @analysis_rules.setter
    def analysis_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26267c9443103a44d253b803cbd021f980a5d2b9c34ee95ca6dfc809fab0f1e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analysisRules", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the configured table.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c8634d59e391cfec8341b7e4b408bb2c2335c7e17e4ff15bc5f5d8abc23fd91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3a9395564381a20388411d14ffd2bda7a4d604b2cf7bf643f5e5bd129bdd0f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AggregateColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"column_names": "columnNames", "function": "function"},
    )
    class AggregateColumnProperty:
        def __init__(
            self,
            *,
            column_names: typing.Sequence[builtins.str],
            function: builtins.str,
        ) -> None:
            '''Column in configured table that can be used in aggregate function in query.

            :param column_names: Column names in configured table of aggregate columns.
            :param function: Aggregation function that can be applied to aggregate column in query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                aggregate_column_property = cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                    column_names=["columnNames"],
                    function="function"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa417839f91cf8cc845476ca63e8e1d38ea951bbc307aaa969fdea5be7e16893)
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument function", value=function, expected_type=type_hints["function"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_names": column_names,
                "function": function,
            }

        @builtins.property
        def column_names(self) -> typing.List[builtins.str]:
            '''Column names in configured table of aggregate columns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html#cfn-cleanrooms-configuredtable-aggregatecolumn-columnnames
            '''
            result = self._values.get("column_names")
            assert result is not None, "Required property 'column_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def function(self) -> builtins.str:
            '''Aggregation function that can be applied to aggregate column in query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html#cfn-cleanrooms-configuredtable-aggregatecolumn-function
            '''
            result = self._values.get("function")
            assert result is not None, "Required property 'function' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AggregateColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AggregationConstraintProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_name": "columnName",
            "minimum": "minimum",
            "type": "type",
        },
    )
    class AggregationConstraintProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            minimum: jsii.Number,
            type: builtins.str,
        ) -> None:
            '''Constraint on query output removing output rows that do not meet a minimum number of distinct values of a specified column.

            :param column_name: Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.
            :param minimum: The minimum number of distinct values that an output row must be an aggregation of. Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.
            :param type: The type of aggregation the constraint allows. The only valid value is currently ``COUNT_DISTINCT``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                aggregation_constraint_property = cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                    column_name="columnName",
                    minimum=123,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63f1cc4359753a41914fdd91e80c9746bf76bc8ab990f1c207bf527199e05de5)
                check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
                check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_name": column_name,
                "minimum": minimum,
                "type": type,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def minimum(self) -> jsii.Number:
            '''The minimum number of distinct values that an output row must be an aggregation of.

            Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-minimum
            '''
            result = self._values.get("minimum")
            assert result is not None, "Required property 'minimum' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of aggregation the constraint allows.

            The only valid value is currently ``COUNT_DISTINCT``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AggregationConstraintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregate_columns": "aggregateColumns",
            "dimension_columns": "dimensionColumns",
            "join_columns": "joinColumns",
            "output_constraints": "outputConstraints",
            "scalar_functions": "scalarFunctions",
            "allowed_join_operators": "allowedJoinOperators",
            "join_required": "joinRequired",
        },
    )
    class AnalysisRuleAggregationProperty:
        def __init__(
            self,
            *,
            aggregate_columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AggregateColumnProperty", typing.Dict[builtins.str, typing.Any]]]]],
            dimension_columns: typing.Sequence[builtins.str],
            join_columns: typing.Sequence[builtins.str],
            output_constraints: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AggregationConstraintProperty", typing.Dict[builtins.str, typing.Any]]]]],
            scalar_functions: typing.Sequence[builtins.str],
            allowed_join_operators: typing.Optional[typing.Sequence[builtins.str]] = None,
            join_required: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Enables query structure and specified queries that produce aggregate statistics.

            :param aggregate_columns: The columns that query runners are allowed to use in aggregation queries.
            :param dimension_columns: The columns that query runners are allowed to select, group by, or filter by.
            :param join_columns: Columns in configured table that can be used in join statements and/or as aggregate columns. They can never be outputted directly.
            :param output_constraints: Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.
            :param scalar_functions: Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.
            :param allowed_join_operators: Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is ``AND`` .
            :param join_required: Control that requires member who runs query to do a join with their configured table and/or other configured table in query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_rule_aggregation_property = cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                    aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                        column_names=["columnNames"],
                        function="function"
                    )],
                    dimension_columns=["dimensionColumns"],
                    join_columns=["joinColumns"],
                    output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                        column_name="columnName",
                        minimum=123,
                        type="type"
                    )],
                    scalar_functions=["scalarFunctions"],
                
                    # the properties below are optional
                    allowed_join_operators=["allowedJoinOperators"],
                    join_required="joinRequired"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c88de0a4314f12e0bbceae5eb6edd232a937dc4a6b95c8eb383dabc0231d87e)
                check_type(argname="argument aggregate_columns", value=aggregate_columns, expected_type=type_hints["aggregate_columns"])
                check_type(argname="argument dimension_columns", value=dimension_columns, expected_type=type_hints["dimension_columns"])
                check_type(argname="argument join_columns", value=join_columns, expected_type=type_hints["join_columns"])
                check_type(argname="argument output_constraints", value=output_constraints, expected_type=type_hints["output_constraints"])
                check_type(argname="argument scalar_functions", value=scalar_functions, expected_type=type_hints["scalar_functions"])
                check_type(argname="argument allowed_join_operators", value=allowed_join_operators, expected_type=type_hints["allowed_join_operators"])
                check_type(argname="argument join_required", value=join_required, expected_type=type_hints["join_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aggregate_columns": aggregate_columns,
                "dimension_columns": dimension_columns,
                "join_columns": join_columns,
                "output_constraints": output_constraints,
                "scalar_functions": scalar_functions,
            }
            if allowed_join_operators is not None:
                self._values["allowed_join_operators"] = allowed_join_operators
            if join_required is not None:
                self._values["join_required"] = join_required

        @builtins.property
        def aggregate_columns(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AggregateColumnProperty"]]]:
            '''The columns that query runners are allowed to use in aggregation queries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-aggregatecolumns
            '''
            result = self._values.get("aggregate_columns")
            assert result is not None, "Required property 'aggregate_columns' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AggregateColumnProperty"]]], result)

        @builtins.property
        def dimension_columns(self) -> typing.List[builtins.str]:
            '''The columns that query runners are allowed to select, group by, or filter by.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-dimensioncolumns
            '''
            result = self._values.get("dimension_columns")
            assert result is not None, "Required property 'dimension_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def join_columns(self) -> typing.List[builtins.str]:
            '''Columns in configured table that can be used in join statements and/or as aggregate columns.

            They can never be outputted directly.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-joincolumns
            '''
            result = self._values.get("join_columns")
            assert result is not None, "Required property 'join_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def output_constraints(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AggregationConstraintProperty"]]]:
            '''Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-outputconstraints
            '''
            result = self._values.get("output_constraints")
            assert result is not None, "Required property 'output_constraints' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AggregationConstraintProperty"]]], result)

        @builtins.property
        def scalar_functions(self) -> typing.List[builtins.str]:
            '''Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-scalarfunctions
            '''
            result = self._values.get("scalar_functions")
            assert result is not None, "Required property 'scalar_functions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def allowed_join_operators(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Which logical operators (if any) are to be used in an INNER JOIN match condition.

            Default is ``AND`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-allowedjoinoperators
            '''
            result = self._values.get("allowed_join_operators")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def join_required(self) -> typing.Optional[builtins.str]:
            '''Control that requires member who runs query to do a join with their configured table and/or other configured table in query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-joinrequired
            '''
            result = self._values.get("join_required")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleAggregationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty",
        jsii_struct_bases=[],
        name_mapping={
            "join_columns": "joinColumns",
            "list_columns": "listColumns",
            "allowed_join_operators": "allowedJoinOperators",
        },
    )
    class AnalysisRuleListProperty:
        def __init__(
            self,
            *,
            join_columns: typing.Sequence[builtins.str],
            list_columns: typing.Sequence[builtins.str],
            allowed_join_operators: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A type of analysis rule that enables row-level analysis.

            :param join_columns: Columns that can be used to join a configured table with the table of the member who can query and other members' configured tables.
            :param list_columns: Columns that can be listed in the output.
            :param allowed_join_operators: Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is ``AND`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_rule_list_property = cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                    join_columns=["joinColumns"],
                    list_columns=["listColumns"],
                
                    # the properties below are optional
                    allowed_join_operators=["allowedJoinOperators"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0accd14fb8407350b8ede83ec532b76a492d21ad538a377f14413f98dae0fba)
                check_type(argname="argument join_columns", value=join_columns, expected_type=type_hints["join_columns"])
                check_type(argname="argument list_columns", value=list_columns, expected_type=type_hints["list_columns"])
                check_type(argname="argument allowed_join_operators", value=allowed_join_operators, expected_type=type_hints["allowed_join_operators"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "join_columns": join_columns,
                "list_columns": list_columns,
            }
            if allowed_join_operators is not None:
                self._values["allowed_join_operators"] = allowed_join_operators

        @builtins.property
        def join_columns(self) -> typing.List[builtins.str]:
            '''Columns that can be used to join a configured table with the table of the member who can query and other members' configured tables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-joincolumns
            '''
            result = self._values.get("join_columns")
            assert result is not None, "Required property 'join_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def list_columns(self) -> typing.List[builtins.str]:
            '''Columns that can be listed in the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-listcolumns
            '''
            result = self._values.get("list_columns")
            assert result is not None, "Required property 'list_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def allowed_join_operators(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Which logical operators (if any) are to be used in an INNER JOIN match condition.

            Default is ``AND`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-allowedjoinoperators
            '''
            result = self._values.get("allowed_join_operators")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AnalysisRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"policy": "policy", "type": "type"},
    )
    class AnalysisRuleProperty:
        def __init__(
            self,
            *,
            policy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''A specification about how data from the configured table can be used in a query.

            :param policy: A policy that describes the associated data usage limitations.
            :param type: The type of analysis rule. Valid values are ``AGGREGATION`` and ``LIST``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_rule_property = cleanrooms.CfnConfiguredTable.AnalysisRuleProperty(
                    policy=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty(
                        v1=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                            aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                                aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                                    column_names=["columnNames"],
                                    function="function"
                                )],
                                dimension_columns=["dimensionColumns"],
                                join_columns=["joinColumns"],
                                output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                                    column_name="columnName",
                                    minimum=123,
                                    type="type"
                                )],
                                scalar_functions=["scalarFunctions"],
                
                                # the properties below are optional
                                allowed_join_operators=["allowedJoinOperators"],
                                join_required="joinRequired"
                            ),
                            list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                                join_columns=["joinColumns"],
                                list_columns=["listColumns"],
                
                                # the properties below are optional
                                allowed_join_operators=["allowedJoinOperators"]
                            )
                        )
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__124c3b77588197cdbfdd27c90ac026b586926dd1d223cf478cf9815b95327095)
                check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy": policy,
                "type": type,
            }

        @builtins.property
        def policy(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty"]:
            '''A policy that describes the associated data usage limitations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html#cfn-cleanrooms-configuredtable-analysisrule-policy
            '''
            result = self._values.get("policy")
            assert result is not None, "Required property 'policy' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of analysis rule.

            Valid values are ``AGGREGATION`` and ``LIST``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html#cfn-cleanrooms-configuredtable-analysisrule-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"v1": "v1"},
    )
    class ConfiguredTableAnalysisRulePolicyProperty:
        def __init__(
            self,
            *,
            v1: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Controls on the query specifications that can be run on a configured table.

            :param v1: Controls on the query specifications that can be run on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_analysis_rule_policy_property = cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty(
                    v1=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                        aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                            aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                                column_names=["columnNames"],
                                function="function"
                            )],
                            dimension_columns=["dimensionColumns"],
                            join_columns=["joinColumns"],
                            output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                                column_name="columnName",
                                minimum=123,
                                type="type"
                            )],
                            scalar_functions=["scalarFunctions"],
                
                            # the properties below are optional
                            allowed_join_operators=["allowedJoinOperators"],
                            join_required="joinRequired"
                        ),
                        list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                            join_columns=["joinColumns"],
                            list_columns=["listColumns"],
                
                            # the properties below are optional
                            allowed_join_operators=["allowedJoinOperators"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f1e3e5a795ca7258552d46676801756cc639b2cf39b0a42555fb510dee59fc1)
                check_type(argname="argument v1", value=v1, expected_type=type_hints["v1"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "v1": v1,
            }

        @builtins.property
        def v1(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property"]:
            '''Controls on the query specifications that can be run on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-v1
            '''
            result = self._values.get("v1")
            assert result is not None, "Required property 'v1' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAnalysisRulePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property",
        jsii_struct_bases=[],
        name_mapping={"aggregation": "aggregation", "list": "list"},
    )
    class ConfiguredTableAnalysisRulePolicyV1Property:
        def __init__(
            self,
            *,
            aggregation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AnalysisRuleAggregationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AnalysisRuleListProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Controls on the query specifications that can be run on a configured table.

            :param aggregation: Analysis rule type that enables only aggregation queries on a configured table.
            :param list: Analysis rule type that enables only list queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_analysis_rule_policy_v1_property = cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                    aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                        aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                            column_names=["columnNames"],
                            function="function"
                        )],
                        dimension_columns=["dimensionColumns"],
                        join_columns=["joinColumns"],
                        output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                            column_name="columnName",
                            minimum=123,
                            type="type"
                        )],
                        scalar_functions=["scalarFunctions"],
                
                        # the properties below are optional
                        allowed_join_operators=["allowedJoinOperators"],
                        join_required="joinRequired"
                    ),
                    list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                        join_columns=["joinColumns"],
                        list_columns=["listColumns"],
                
                        # the properties below are optional
                        allowed_join_operators=["allowedJoinOperators"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f3e07fc4df9c2eafb409dd0b417b9236aa995940875e48daa983efee06bd45fc)
                check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
                check_type(argname="argument list", value=list, expected_type=type_hints["list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aggregation is not None:
                self._values["aggregation"] = aggregation
            if list is not None:
                self._values["list"] = list

        @builtins.property
        def aggregation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleAggregationProperty"]]:
            '''Analysis rule type that enables only aggregation queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-aggregation
            '''
            result = self._values.get("aggregation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleAggregationProperty"]], result)

        @builtins.property
        def list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleListProperty"]]:
            '''Analysis rule type that enables only list queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-list
            '''
            result = self._values.get("list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleListProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAnalysisRulePolicyV1Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"database_name": "databaseName", "table_name": "tableName"},
    )
    class GlueTableReferenceProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''A reference to a table within an AWS Glue data catalog.

            :param database_name: The name of the database the AWS Glue table belongs to.
            :param table_name: The name of the AWS Glue table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                glue_table_reference_property = cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty(
                    database_name="databaseName",
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad49810a315ae1c04064504cefbb3e0bc6fec52a1add50545955db56f0db50f9)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
            }

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database the AWS Glue table belongs to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html#cfn-cleanrooms-configuredtable-gluetablereference-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the AWS Glue table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html#cfn-cleanrooms-configuredtable-gluetablereference-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueTableReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.TableReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"glue": "glue"},
    )
    class TableReferenceProperty:
        def __init__(
            self,
            *,
            glue: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.GlueTableReferenceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A pointer to the dataset that underlies this table.

            Currently, this can only be an AWS Glue table.

            :param glue: If present, a reference to the AWS Glue table referred to by this table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                table_reference_property = cleanrooms.CfnConfiguredTable.TableReferenceProperty(
                    glue=cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty(
                        database_name="databaseName",
                        table_name="tableName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48547ee47249030cb21aff2b6c33202b13d80f1552ddf62b21595c3e0bb02374)
                check_type(argname="argument glue", value=glue, expected_type=type_hints["glue"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "glue": glue,
            }

        @builtins.property
        def glue(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.GlueTableReferenceProperty"]:
            '''If present, a reference to the AWS Glue table referred to by this table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html#cfn-cleanrooms-configuredtable-tablereference-glue
            '''
            result = self._values.get("glue")
            assert result is not None, "Required property 'glue' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.GlueTableReferenceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnConfiguredTableAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociation",
):
    '''Creates a configured table association.

    A configured table association links a configured table with a collaboration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_configured_table_association = cleanrooms.CfnConfiguredTableAssociation(self, "MyCfnConfiguredTableAssociation",
            configured_table_identifier="configuredTableIdentifier",
            membership_identifier="membershipIdentifier",
            name="name",
            role_arn="roleArn",
        
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
        configured_table_identifier: builtins.str,
        membership_identifier: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configured_table_identifier: A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.
        :param membership_identifier: The unique ID for the membership this configured table association belongs to.
        :param name: The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.
        :param role_arn: The service will assume this role to access catalog metadata and query the table.
        :param description: A description of the configured table association.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e813cbcc5b9d34191c933a4be199648c57161cd507f73f0659159b5b61777153)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfiguredTableAssociationProps(
            configured_table_identifier=configured_table_identifier,
            membership_identifier=membership_identifier,
            name=name,
            role_arn=role_arn,
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e6d4b82c3edf32301796f14dea9ee962d5b6287982b67f53a6fce4d9e53e702)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b13025a7765c8fcc0096c7e63fe6d35197debf3b5ec554487f0710eeca7c147b)
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
        '''Returns the Amazon Resource Name (ARN) of the specified configured table association.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:configuredtable/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConfiguredTableAssociationIdentifier")
    def attr_configured_table_association_identifier(self) -> builtins.str:
        '''Returns the unique identifier of the specified configured table association.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE33333``

        :cloudformationAttribute: ConfiguredTableAssociationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfiguredTableAssociationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="configuredTableIdentifier")
    def configured_table_identifier(self) -> builtins.str:
        '''A unique identifier for the configured table to be associated to.'''
        return typing.cast(builtins.str, jsii.get(self, "configuredTableIdentifier"))

    @configured_table_identifier.setter
    def configured_table_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9728a7769f77a5cdfb3417c1fc58a389ba8c6ef5730bb294ef56c67c4f965bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuredTableIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="membershipIdentifier")
    def membership_identifier(self) -> builtins.str:
        '''The unique ID for the membership this configured table association belongs to.'''
        return typing.cast(builtins.str, jsii.get(self, "membershipIdentifier"))

    @membership_identifier.setter
    def membership_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0b566414c7844303646de783cb99821d6132816fd82629491db143d70bc328)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membershipIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the configured table association, in lowercase.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bb6d6d8ed4af7ba2289b9a65f55feb240da577eb6c05a2a379ac3aa825876b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The service will assume this role to access catalog metadata and query the table.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ed3a131e342f3d6715894b34f9784b7f6a4bd2257ccd5640eee2873aff3a7bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configured table association.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c12987240d2469d3de49134d97df56891e19e780c69b74115f2054f5a34a614)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab43f7456a874349f59a592b725dc266f2d215b76da6fc373e63e5999b3ce75e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configured_table_identifier": "configuredTableIdentifier",
        "membership_identifier": "membershipIdentifier",
        "name": "name",
        "role_arn": "roleArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnConfiguredTableAssociationProps:
    def __init__(
        self,
        *,
        configured_table_identifier: builtins.str,
        membership_identifier: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguredTableAssociation``.

        :param configured_table_identifier: A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.
        :param membership_identifier: The unique ID for the membership this configured table association belongs to.
        :param name: The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.
        :param role_arn: The service will assume this role to access catalog metadata and query the table.
        :param description: A description of the configured table association.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_configured_table_association_props = cleanrooms.CfnConfiguredTableAssociationProps(
                configured_table_identifier="configuredTableIdentifier",
                membership_identifier="membershipIdentifier",
                name="name",
                role_arn="roleArn",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115dd625c37fad8a84b51d36bcabf9183ae442a7285c6ddd1efddd869faae1dc)
            check_type(argname="argument configured_table_identifier", value=configured_table_identifier, expected_type=type_hints["configured_table_identifier"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configured_table_identifier": configured_table_identifier,
            "membership_identifier": membership_identifier,
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configured_table_identifier(self) -> builtins.str:
        '''A unique identifier for the configured table to be associated to.

        Currently accepts a configured table ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-configuredtableidentifier
        '''
        result = self._values.get("configured_table_identifier")
        assert result is not None, "Required property 'configured_table_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The unique ID for the membership this configured table association belongs to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-membershipidentifier
        '''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the configured table association, in lowercase.

        The table is identified by this name when running protected queries against the underlying data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The service will assume this role to access catalog metadata and query the table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configured table association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfiguredTableAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_columns": "allowedColumns",
        "analysis_method": "analysisMethod",
        "name": "name",
        "table_reference": "tableReference",
        "analysis_rules": "analysisRules",
        "description": "description",
        "tags": "tags",
    },
)
class CfnConfiguredTableProps:
    def __init__(
        self,
        *,
        allowed_columns: typing.Sequence[builtins.str],
        analysis_method: builtins.str,
        name: builtins.str,
        table_reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.TableReferenceProperty, typing.Dict[builtins.str, typing.Any]]],
        analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguredTable``.

        :param allowed_columns: The columns within the underlying AWS Glue table that can be utilized within collaborations.
        :param analysis_method: The analysis method for the configured table. The only valid value is currently ``DIRECT_QUERY``.
        :param name: A name for the configured table.
        :param table_reference: The AWS Glue table that this configured table represents.
        :param analysis_rules: The entire created analysis rule.
        :param description: A description for the configured table.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_configured_table_props = cleanrooms.CfnConfiguredTableProps(
                allowed_columns=["allowedColumns"],
                analysis_method="analysisMethod",
                name="name",
                table_reference=cleanrooms.CfnConfiguredTable.TableReferenceProperty(
                    glue=cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty(
                        database_name="databaseName",
                        table_name="tableName"
                    )
                ),
            
                # the properties below are optional
                analysis_rules=[cleanrooms.CfnConfiguredTable.AnalysisRuleProperty(
                    policy=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty(
                        v1=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                            aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                                aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                                    column_names=["columnNames"],
                                    function="function"
                                )],
                                dimension_columns=["dimensionColumns"],
                                join_columns=["joinColumns"],
                                output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                                    column_name="columnName",
                                    minimum=123,
                                    type="type"
                                )],
                                scalar_functions=["scalarFunctions"],
            
                                # the properties below are optional
                                allowed_join_operators=["allowedJoinOperators"],
                                join_required="joinRequired"
                            ),
                            list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                                join_columns=["joinColumns"],
                                list_columns=["listColumns"],
            
                                # the properties below are optional
                                allowed_join_operators=["allowedJoinOperators"]
                            )
                        )
                    ),
                    type="type"
                )],
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__881d5bc014e7a9ce8400d21437644071526768629f4ac0f4414f60ba95930f3f)
            check_type(argname="argument allowed_columns", value=allowed_columns, expected_type=type_hints["allowed_columns"])
            check_type(argname="argument analysis_method", value=analysis_method, expected_type=type_hints["analysis_method"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument table_reference", value=table_reference, expected_type=type_hints["table_reference"])
            check_type(argname="argument analysis_rules", value=analysis_rules, expected_type=type_hints["analysis_rules"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_columns": allowed_columns,
            "analysis_method": analysis_method,
            "name": name,
            "table_reference": table_reference,
        }
        if analysis_rules is not None:
            self._values["analysis_rules"] = analysis_rules
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def allowed_columns(self) -> typing.List[builtins.str]:
        '''The columns within the underlying AWS Glue table that can be utilized within collaborations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-allowedcolumns
        '''
        result = self._values.get("allowed_columns")
        assert result is not None, "Required property 'allowed_columns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def analysis_method(self) -> builtins.str:
        '''The analysis method for the configured table.

        The only valid value is currently ``DIRECT_QUERY``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-analysismethod
        '''
        result = self._values.get("analysis_method")
        assert result is not None, "Required property 'analysis_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the configured table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_reference(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.TableReferenceProperty]:
        '''The AWS Glue table that this configured table represents.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-tablereference
        '''
        result = self._values.get("table_reference")
        assert result is not None, "Required property 'table_reference' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.TableReferenceProperty], result)

    @builtins.property
    def analysis_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.AnalysisRuleProperty]]]]:
        '''The entire created analysis rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-analysisrules
        '''
        result = self._values.get("analysis_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.AnalysisRuleProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the configured table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfiguredTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMembership(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership",
):
    '''Creates a membership for a specific collaboration identifier and joins the collaboration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_membership = cleanrooms.CfnMembership(self, "MyCfnMembership",
            collaboration_identifier="collaborationIdentifier",
            query_log_status="queryLogStatus",
        
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
        collaboration_identifier: builtins.str,
        query_log_status: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param collaboration_identifier: The unique ID for the associated collaboration.
        :param query_log_status: An indicator as to whether query logging has been enabled or disabled for the collaboration.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74d43efdc8d8359f9de6878ad0f2d25ff79e584d96e5ca863178e6f14312cec1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMembershipProps(
            collaboration_identifier=collaboration_identifier,
            query_log_status=query_log_status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f53a7e47a69cc6ee8550050a85dd5bd1dab4134d650a0e20c9312e56ea80fc60)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78e173bbe42542972b47c21576e57269fe216eab7a86b44fadf695b6653d493d)
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
        '''Returns the Amazon Resource Name (ARN) of the specified membership.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationArn")
    def attr_collaboration_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the specified collaboration.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:collaboration/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: CollaborationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationCreatorAccountId")
    def attr_collaboration_creator_account_id(self) -> builtins.str:
        '''Returns the unique identifier of the specified collaboration creator account.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: CollaborationCreatorAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationCreatorAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipIdentifier")
    def attr_membership_identifier(self) -> builtins.str:
        '''Returns the unique identifier of the specified membership.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE22222``

        :cloudformationAttribute: MembershipIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="collaborationIdentifier")
    def collaboration_identifier(self) -> builtins.str:
        '''The unique ID for the associated collaboration.'''
        return typing.cast(builtins.str, jsii.get(self, "collaborationIdentifier"))

    @collaboration_identifier.setter
    def collaboration_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba2cc6691bad0d4fdbfa43d453737e19bbcc1b63648ed884849a27170f877099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collaborationIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="queryLogStatus")
    def query_log_status(self) -> builtins.str:
        '''An indicator as to whether query logging has been enabled or disabled for the collaboration.'''
        return typing.cast(builtins.str, jsii.get(self, "queryLogStatus"))

    @query_log_status.setter
    def query_log_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee80a156c452c78946d81f28dfee88d47d5702e2d1eeb7a5c7aeb167b25400e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryLogStatus", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efad84033de32d67e94b9ac23a8d3176e7fc904203e000dac066b28793fec68b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "collaboration_identifier": "collaborationIdentifier",
        "query_log_status": "queryLogStatus",
        "tags": "tags",
    },
)
class CfnMembershipProps:
    def __init__(
        self,
        *,
        collaboration_identifier: builtins.str,
        query_log_status: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMembership``.

        :param collaboration_identifier: The unique ID for the associated collaboration.
        :param query_log_status: An indicator as to whether query logging has been enabled or disabled for the collaboration.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_membership_props = cleanrooms.CfnMembershipProps(
                collaboration_identifier="collaborationIdentifier",
                query_log_status="queryLogStatus",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7030966bdb99200cf7aff97662a2ef1e02754d2c014bc030475065ea06e0da)
            check_type(argname="argument collaboration_identifier", value=collaboration_identifier, expected_type=type_hints["collaboration_identifier"])
            check_type(argname="argument query_log_status", value=query_log_status, expected_type=type_hints["query_log_status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collaboration_identifier": collaboration_identifier,
            "query_log_status": query_log_status,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def collaboration_identifier(self) -> builtins.str:
        '''The unique ID for the associated collaboration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-collaborationidentifier
        '''
        result = self._values.get("collaboration_identifier")
        assert result is not None, "Required property 'collaboration_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_log_status(self) -> builtins.str:
        '''An indicator as to whether query logging has been enabled or disabled for the collaboration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-querylogstatus
        '''
        result = self._values.get("query_log_status")
        assert result is not None, "Required property 'query_log_status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMembershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCollaboration",
    "CfnCollaborationProps",
    "CfnConfiguredTable",
    "CfnConfiguredTableAssociation",
    "CfnConfiguredTableAssociationProps",
    "CfnConfiguredTableProps",
    "CfnMembership",
    "CfnMembershipProps",
]

publication.publish()

def _typecheckingstub__a8995527da9ce4212caf3c1fdf601e4947c02ff1e364e92811ac8635be534111(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    creator_display_name: builtins.str,
    creator_member_abilities: typing.Sequence[builtins.str],
    description: builtins.str,
    members: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MemberSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    query_log_status: builtins.str,
    data_encryption_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.DataEncryptionMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b0d208a10b53d5d7bf8e19cff7b1a7be86094960aa43579972861d563de44d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9705b5c9f28f1d364782d5cb996ee4fe0e93dc0fbee1871bc10feeb5a547d9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9f17060755de314c6aea7e9fe1c03f18e31972fafbe5d1edf10b18250f60ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee81f8b64fd681cae1a860e0339dfa0ddeb287c4e709f0b34cc3c8bcf9bc6bd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb5edb6a58e1c0f33620eadb56126089a140277fe87954ea4d3a06146b3559ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e816963af09a7c3bdf0ca05211222f43d66929e9fa8216fe82e8fb6e27493bdc(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MemberSpecificationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585aa64e1eeaa11003c987d7230a1772b0683c9f8866457214d0242ba9d00d4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa852049fd80eee6c2543d7576eb0c8f60a43d90ca97006450c31d8a1ed9df20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86b18a30aac6a5afc1830c4adb282d4f0f3199f7c3d3ce99ffb24dad829a6eb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.DataEncryptionMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06877122efbe5bc41c92999ba727597f48590c383378ee73a94c91fe43305e60(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d5c25162d0eabd19a06fd0a1ec26adcd8d8a0d12434d6ee8fbec8e27c21965(
    *,
    allow_cleartext: typing.Union[builtins.bool, _IResolvable_da3f097b],
    allow_duplicates: typing.Union[builtins.bool, _IResolvable_da3f097b],
    allow_joins_on_columns_with_different_names: typing.Union[builtins.bool, _IResolvable_da3f097b],
    preserve_nulls: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9d415168b79c297b7313d0c42362a70fed420b1dda08e496b99813fbbd3248(
    *,
    account_id: builtins.str,
    display_name: builtins.str,
    member_abilities: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2049291a9933df94c4258b33838a3aa8100d0214a4519c3d84e6d70ed724c55d(
    *,
    creator_display_name: builtins.str,
    creator_member_abilities: typing.Sequence[builtins.str],
    description: builtins.str,
    members: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MemberSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    query_log_status: builtins.str,
    data_encryption_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.DataEncryptionMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6da68c3fc7e3c0674ddb5e2082cfb964074dd6f86f1df6dfcede15001d6f1259(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allowed_columns: typing.Sequence[builtins.str],
    analysis_method: builtins.str,
    name: builtins.str,
    table_reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.TableReferenceProperty, typing.Dict[builtins.str, typing.Any]]],
    analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fecfad26837cc2fdccacfdfb035a18dcac563292f6d300d8052bc89207ae04fe(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c9224380ccb774fe3599e8c47969dd65412118923ba36f2fc0d722c916638e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46e6aec85126d8c2d12db0e5442b4d56c199d90e95cd9b98b1c92b7652d7c7eb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd16c3f5e30018a39bada3627e112c5d99eea9283a9ad2de82b9790911c3169(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8743fd9932eb6c0afe523245bfc3bc611bed75b8e179806716cdbd7e1e97f817(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f7eaa704c6766bfee1be9d2d2b0c8cc4751fd3eb996d6d9902238bdc710232(
    value: typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.TableReferenceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26267c9443103a44d253b803cbd021f980a5d2b9c34ee95ca6dfc809fab0f1e0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.AnalysisRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c8634d59e391cfec8341b7e4b408bb2c2335c7e17e4ff15bc5f5d8abc23fd91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a9395564381a20388411d14ffd2bda7a4d604b2cf7bf643f5e5bd129bdd0f0(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa417839f91cf8cc845476ca63e8e1d38ea951bbc307aaa969fdea5be7e16893(
    *,
    column_names: typing.Sequence[builtins.str],
    function: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f1cc4359753a41914fdd91e80c9746bf76bc8ab990f1c207bf527199e05de5(
    *,
    column_name: builtins.str,
    minimum: jsii.Number,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c88de0a4314f12e0bbceae5eb6edd232a937dc4a6b95c8eb383dabc0231d87e(
    *,
    aggregate_columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AggregateColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
    dimension_columns: typing.Sequence[builtins.str],
    join_columns: typing.Sequence[builtins.str],
    output_constraints: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AggregationConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]],
    scalar_functions: typing.Sequence[builtins.str],
    allowed_join_operators: typing.Optional[typing.Sequence[builtins.str]] = None,
    join_required: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0accd14fb8407350b8ede83ec532b76a492d21ad538a377f14413f98dae0fba(
    *,
    join_columns: typing.Sequence[builtins.str],
    list_columns: typing.Sequence[builtins.str],
    allowed_join_operators: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124c3b77588197cdbfdd27c90ac026b586926dd1d223cf478cf9815b95327095(
    *,
    policy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1e3e5a795ca7258552d46676801756cc639b2cf39b0a42555fb510dee59fc1(
    *,
    v1: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3e07fc4df9c2eafb409dd0b417b9236aa995940875e48daa983efee06bd45fc(
    *,
    aggregation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleAggregationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad49810a315ae1c04064504cefbb3e0bc6fec52a1add50545955db56f0db50f9(
    *,
    database_name: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48547ee47249030cb21aff2b6c33202b13d80f1552ddf62b21595c3e0bb02374(
    *,
    glue: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.GlueTableReferenceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e813cbcc5b9d34191c933a4be199648c57161cd507f73f0659159b5b61777153(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configured_table_identifier: builtins.str,
    membership_identifier: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6d4b82c3edf32301796f14dea9ee962d5b6287982b67f53a6fce4d9e53e702(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b13025a7765c8fcc0096c7e63fe6d35197debf3b5ec554487f0710eeca7c147b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9728a7769f77a5cdfb3417c1fc58a389ba8c6ef5730bb294ef56c67c4f965bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0b566414c7844303646de783cb99821d6132816fd82629491db143d70bc328(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bb6d6d8ed4af7ba2289b9a65f55feb240da577eb6c05a2a379ac3aa825876b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ed3a131e342f3d6715894b34f9784b7f6a4bd2257ccd5640eee2873aff3a7bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c12987240d2469d3de49134d97df56891e19e780c69b74115f2054f5a34a614(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab43f7456a874349f59a592b725dc266f2d215b76da6fc373e63e5999b3ce75e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115dd625c37fad8a84b51d36bcabf9183ae442a7285c6ddd1efddd869faae1dc(
    *,
    configured_table_identifier: builtins.str,
    membership_identifier: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__881d5bc014e7a9ce8400d21437644071526768629f4ac0f4414f60ba95930f3f(
    *,
    allowed_columns: typing.Sequence[builtins.str],
    analysis_method: builtins.str,
    name: builtins.str,
    table_reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.TableReferenceProperty, typing.Dict[builtins.str, typing.Any]]],
    analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74d43efdc8d8359f9de6878ad0f2d25ff79e584d96e5ca863178e6f14312cec1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    collaboration_identifier: builtins.str,
    query_log_status: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53a7e47a69cc6ee8550050a85dd5bd1dab4134d650a0e20c9312e56ea80fc60(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78e173bbe42542972b47c21576e57269fe216eab7a86b44fadf695b6653d493d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba2cc6691bad0d4fdbfa43d453737e19bbcc1b63648ed884849a27170f877099(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee80a156c452c78946d81f28dfee88d47d5702e2d1eeb7a5c7aeb167b25400e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efad84033de32d67e94b9ac23a8d3176e7fc904203e000dac066b28793fec68b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7030966bdb99200cf7aff97662a2ef1e02754d2c014bc030475065ea06e0da(
    *,
    collaboration_identifier: builtins.str,
    query_log_status: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
