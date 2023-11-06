'''
# AWS::IdentityStore Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_identitystore as identitystore
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IdentityStore construct libraries](https://constructs.dev/search?q=identitystore)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IdentityStore resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IdentityStore.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IdentityStore](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IdentityStore.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_identitystore.CfnGroup",
):
    '''A group object, which contains a specified group’s metadata and attributes.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_identitystore as identitystore
        
        cfn_group = identitystore.CfnGroup(self, "MyCfnGroup",
            display_name="displayName",
            identity_store_id="identityStoreId",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        identity_store_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param display_name: A string containing the name of the group. This value is commonly displayed when the group is referenced.
        :param identity_store_id: The globally unique identifier for the identity store.
        :param description: A string containing the description of the group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37e27ff46dfa4082cad1981cc4ade1e2a9ce445cf9aad4a8eb75e162b9b429f1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(
            display_name=display_name,
            identity_store_id=identity_store_id,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd30cf433d0f11c47c01b425898b3b3494dae8561dd252ec97cb62a6f3ea01c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__181a3492db49132403d11a30d4f4ede267eaa3675413217fae9f2a57427d93a5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGroupId")
    def attr_group_id(self) -> builtins.str:
        '''The identifier of the newly created group in the identity store.

        :cloudformationAttribute: GroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGroupId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''A string containing the name of the group.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2f0d1e640344318d6ca1684bf877149c58a04ff3b658cc26437fd42577ae42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.'''
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ec5af9bcaa29b5bd7b1489efc7cb2d8be21651e7c0abc6581d713983f718c75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A string containing the description of the group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adb1a463b108d61759d25cd969fb5fed9a681bdbfadbf09cefe6655715c026df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.implements(_IInspectable_c2943556)
class CfnGroupMembership(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_identitystore.CfnGroupMembership",
):
    '''Contains the identifiers for a group, a group member, and a ``GroupMembership`` object in the identity store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_identitystore as identitystore
        
        cfn_group_membership = identitystore.CfnGroupMembership(self, "MyCfnGroupMembership",
            group_id="groupId",
            identity_store_id="identityStoreId",
            member_id=identitystore.CfnGroupMembership.MemberIdProperty(
                user_id="userId"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_id: builtins.str,
        identity_store_id: builtins.str,
        member_id: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGroupMembership.MemberIdProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param group_id: The unique identifier for a group in the identity store.
        :param identity_store_id: The globally unique identifier for the identity store.
        :param member_id: An object containing the identifier of a group member. Setting ``MemberId`` 's ``UserId`` field to a specific User's ID indicates we should consider that User as a group member.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d55a804ce565c6f3a413944bff86b3236786318808951cf53ad4eff71316db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupMembershipProps(
            group_id=group_id, identity_store_id=identity_store_id, member_id=member_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bbe599298882f9cb39ad950a183df2f00325817213542a0979da08b15e837de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8c6b11b08fd290fc0948df25fb4993347b63ee62d6cc093b9fdb1639f9be8e9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipId")
    def attr_membership_id(self) -> builtins.str:
        '''The identifier for a ``GroupMembership`` in the identity store.

        :cloudformationAttribute: MembershipId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        '''The unique identifier for a group in the identity store.'''
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84854d3f76ffaf3fcbc3f65a33c1661f74f5b69424e248ef1e8272d270ac7f78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.'''
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbe6d44611bf93ff14a416179e20aded09542ea5eeadef3315ca4e2b9610a458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value)

    @builtins.property
    @jsii.member(jsii_name="memberId")
    def member_id(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnGroupMembership.MemberIdProperty"]:
        '''An object containing the identifier of a group member.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGroupMembership.MemberIdProperty"], jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnGroupMembership.MemberIdProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cf491e3e3c3bfc7f52caab31db7140718db94dfca804458b592c7195b7552ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_identitystore.CfnGroupMembership.MemberIdProperty",
        jsii_struct_bases=[],
        name_mapping={"user_id": "userId"},
    )
    class MemberIdProperty:
        def __init__(self, *, user_id: builtins.str) -> None:
            '''An object that contains the identifier of a group member.

            Setting the ``UserID`` field to the specific identifier for a user indicates that the user is a member of the group.

            :param user_id: The identifier for a user in the identity store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-groupmembership-memberid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_identitystore as identitystore
                
                member_id_property = identitystore.CfnGroupMembership.MemberIdProperty(
                    user_id="userId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa85e069965fcc2401129e3357a969b039233bb2ccffdd9a02afd5dde1c53e25)
                check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "user_id": user_id,
            }

        @builtins.property
        def user_id(self) -> builtins.str:
            '''The identifier for a user in the identity store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-groupmembership-memberid.html#cfn-identitystore-groupmembership-memberid-userid
            '''
            result = self._values.get("user_id")
            assert result is not None, "Required property 'user_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_identitystore.CfnGroupMembershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_id": "groupId",
        "identity_store_id": "identityStoreId",
        "member_id": "memberId",
    },
)
class CfnGroupMembershipProps:
    def __init__(
        self,
        *,
        group_id: builtins.str,
        identity_store_id: builtins.str,
        member_id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroupMembership.MemberIdProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnGroupMembership``.

        :param group_id: The unique identifier for a group in the identity store.
        :param identity_store_id: The globally unique identifier for the identity store.
        :param member_id: An object containing the identifier of a group member. Setting ``MemberId`` 's ``UserId`` field to a specific User's ID indicates we should consider that User as a group member.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_identitystore as identitystore
            
            cfn_group_membership_props = identitystore.CfnGroupMembershipProps(
                group_id="groupId",
                identity_store_id="identityStoreId",
                member_id=identitystore.CfnGroupMembership.MemberIdProperty(
                    user_id="userId"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44a916716d7f3a98b073b5f0337cf90a6d86bd04dc851e6b431e842d7c7184b8)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
            "identity_store_id": identity_store_id,
            "member_id": member_id,
        }

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The unique identifier for a group in the identity store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-groupid
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-identitystoreid
        '''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnGroupMembership.MemberIdProperty]:
        '''An object containing the identifier of a group member.

        Setting ``MemberId`` 's ``UserId`` field to a specific User's ID indicates we should consider that User as a group member.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnGroupMembership.MemberIdProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupMembershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_identitystore.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "identity_store_id": "identityStoreId",
        "description": "description",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        identity_store_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroup``.

        :param display_name: A string containing the name of the group. This value is commonly displayed when the group is referenced.
        :param identity_store_id: The globally unique identifier for the identity store.
        :param description: A string containing the description of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_identitystore as identitystore
            
            cfn_group_props = identitystore.CfnGroupProps(
                display_name="displayName",
                identity_store_id="identityStoreId",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84bf79ae8bc719d02791d6f72a1b629f44562f761a2049ee295009880b02ea18)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
            "identity_store_id": identity_store_id,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def display_name(self) -> builtins.str:
        '''A string containing the name of the group.

        This value is commonly displayed when the group is referenced.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-identitystoreid
        '''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A string containing the description of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGroup",
    "CfnGroupMembership",
    "CfnGroupMembershipProps",
    "CfnGroupProps",
]

publication.publish()

def _typecheckingstub__37e27ff46dfa4082cad1981cc4ade1e2a9ce445cf9aad4a8eb75e162b9b429f1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    display_name: builtins.str,
    identity_store_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd30cf433d0f11c47c01b425898b3b3494dae8561dd252ec97cb62a6f3ea01c0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__181a3492db49132403d11a30d4f4ede267eaa3675413217fae9f2a57427d93a5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2f0d1e640344318d6ca1684bf877149c58a04ff3b658cc26437fd42577ae42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ec5af9bcaa29b5bd7b1489efc7cb2d8be21651e7c0abc6581d713983f718c75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb1a463b108d61759d25cd969fb5fed9a681bdbfadbf09cefe6655715c026df(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d55a804ce565c6f3a413944bff86b3236786318808951cf53ad4eff71316db(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_id: builtins.str,
    identity_store_id: builtins.str,
    member_id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroupMembership.MemberIdProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bbe599298882f9cb39ad950a183df2f00325817213542a0979da08b15e837de(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c6b11b08fd290fc0948df25fb4993347b63ee62d6cc093b9fdb1639f9be8e9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84854d3f76ffaf3fcbc3f65a33c1661f74f5b69424e248ef1e8272d270ac7f78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe6d44611bf93ff14a416179e20aded09542ea5eeadef3315ca4e2b9610a458(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cf491e3e3c3bfc7f52caab31db7140718db94dfca804458b592c7195b7552ec(
    value: typing.Union[_IResolvable_da3f097b, CfnGroupMembership.MemberIdProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa85e069965fcc2401129e3357a969b039233bb2ccffdd9a02afd5dde1c53e25(
    *,
    user_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a916716d7f3a98b073b5f0337cf90a6d86bd04dc851e6b431e842d7c7184b8(
    *,
    group_id: builtins.str,
    identity_store_id: builtins.str,
    member_id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroupMembership.MemberIdProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84bf79ae8bc719d02791d6f72a1b629f44562f761a2049ee295009880b02ea18(
    *,
    display_name: builtins.str,
    identity_store_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
