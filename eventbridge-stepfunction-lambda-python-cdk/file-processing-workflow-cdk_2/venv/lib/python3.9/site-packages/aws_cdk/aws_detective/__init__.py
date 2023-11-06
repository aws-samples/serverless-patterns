'''
# AWS::Detective Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_detective as detective
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Detective construct libraries](https://constructs.dev/search?q=detective)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Detective resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Detective.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Detective](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Detective.html).

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
class CfnGraph(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_detective.CfnGraph",
):
    '''The ``AWS::Detective::Graph`` resource is an Amazon Detective resource type that creates a Detective behavior graph.

    The requesting account becomes the administrator account for the behavior graph.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_detective as detective
        
        cfn_graph = detective.CfnGraph(self, "MyCfnGraph",
            auto_enable_members=False,
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
        auto_enable_members: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_enable_members: Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph. By default, this property is set to ``false`` . If you want to change the value of this property, you must be the Detective administrator for the organization. For more information on setting a Detective administrator account, see `AWS::Detective::OrganizationAdmin <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html>`_ Default: - false
        :param tags: The tag values to assign to the new behavior graph.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35c13d9bc47be944ae94949da016fdbb9358dcb215abb1da6176d7e3ee53a804)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphProps(auto_enable_members=auto_enable_members, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__759c0a91a60111bc6af09d55e323cbfdd01e2a1beda41d95d78c666e94579275)
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
            type_hints = typing.get_type_hints(_typecheckingstub__46fde5f95e1a0971beb1da64e90595afb005f925e05b021a1b3b807498818ab8)
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
        '''The ARN of the new behavior graph.

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
    @jsii.member(jsii_name="autoEnableMembers")
    def auto_enable_members(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoEnableMembers"))

    @auto_enable_members.setter
    def auto_enable_members(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__017213db557533db476b11d3395ad002c1c77bc8cc9e28bdee567c8e34fc6ae0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoEnableMembers", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tag values to assign to the new behavior graph.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeb800de7e2138cfe98794158b6d6acc2871d2831f80f41887f5118e20ddcba7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_detective.CfnGraphProps",
    jsii_struct_bases=[],
    name_mapping={"auto_enable_members": "autoEnableMembers", "tags": "tags"},
)
class CfnGraphProps:
    def __init__(
        self,
        *,
        auto_enable_members: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraph``.

        :param auto_enable_members: Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph. By default, this property is set to ``false`` . If you want to change the value of this property, you must be the Detective administrator for the organization. For more information on setting a Detective administrator account, see `AWS::Detective::OrganizationAdmin <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html>`_ Default: - false
        :param tags: The tag values to assign to the new behavior graph.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_detective as detective
            
            cfn_graph_props = detective.CfnGraphProps(
                auto_enable_members=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a226decb0450af1162df8b1540b45da7e7669d305d0e8a36b824b4e85332f93)
            check_type(argname="argument auto_enable_members", value=auto_enable_members, expected_type=type_hints["auto_enable_members"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_enable_members is not None:
            self._values["auto_enable_members"] = auto_enable_members
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auto_enable_members(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.

        By default, this property is set to ``false`` . If you want to change the value of this property, you must be the Detective administrator for the organization. For more information on setting a Detective administrator account, see `AWS::Detective::OrganizationAdmin <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html>`_

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html#cfn-detective-graph-autoenablemembers
        '''
        result = self._values.get("auto_enable_members")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tag values to assign to the new behavior graph.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html#cfn-detective-graph-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMemberInvitation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_detective.CfnMemberInvitation",
):
    '''The ``AWS::Detective::MemberInvitation`` resource is an Amazon Detective resource type that creates an invitation to join a Detective behavior graph.

    The administrator account can choose whether to send an email notification of the invitation to the root user email address of the AWS account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_detective as detective
        
        cfn_member_invitation = detective.CfnMemberInvitation(self, "MyCfnMemberInvitation",
            graph_arn="graphArn",
            member_email_address="memberEmailAddress",
            member_id="memberId",
        
            # the properties below are optional
            disable_email_notification=False,
            message="message"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        graph_arn: builtins.str,
        member_email_address: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param graph_arn: The ARN of the behavior graph to invite the account to contribute data to.
        :param member_email_address: The root user email address of the invited account. If the email address provided is not the root user email address for the provided account, the invitation creation fails.
        :param member_id: The AWS account identifier of the invited account.
        :param disable_email_notification: Whether to send an invitation email to the member account. If set to true, the member account does not receive an invitation email. Default: - false
        :param message: Customized text to include in the invitation email message.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e34d274362e0f21d70fec2895986898f3c3ecf0e61cfff18301ece8bbca92937)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMemberInvitationProps(
            graph_arn=graph_arn,
            member_email_address=member_email_address,
            member_id=member_id,
            disable_email_notification=disable_email_notification,
            message=message,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a79276f8311d161ad0c97e0224bf67f13caeb3555f9726d01364e5d8c9221a4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a41a4a8122f98766d433d9f5e7b7fe3cfd79846b79b03e375826f7f0400376c)
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
    @jsii.member(jsii_name="graphArn")
    def graph_arn(self) -> builtins.str:
        '''The ARN of the behavior graph to invite the account to contribute data to.'''
        return typing.cast(builtins.str, jsii.get(self, "graphArn"))

    @graph_arn.setter
    def graph_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b12ee371571562da274cbc7b8f9ea5fcd9b0f00711e7457cdaa512b01dd4d9f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphArn", value)

    @builtins.property
    @jsii.member(jsii_name="memberEmailAddress")
    def member_email_address(self) -> builtins.str:
        '''The root user email address of the invited account.'''
        return typing.cast(builtins.str, jsii.get(self, "memberEmailAddress"))

    @member_email_address.setter
    def member_email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__effa006ed39255027e20425818f01d5bd8d8799e0f0c9bbaa8605773192cb9e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberEmailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> builtins.str:
        '''The AWS account identifier of the invited account.'''
        return typing.cast(builtins.str, jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0493b702981486fe3adacfc3b48927622dac6cb286fac2e11ee81e222b483192)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberId", value)

    @builtins.property
    @jsii.member(jsii_name="disableEmailNotification")
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to send an invitation email to the member account.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "disableEmailNotification"))

    @disable_email_notification.setter
    def disable_email_notification(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__660e62f59a214a78dff16da1b8a2a68e2f58419729f3c700cdee6f7697a65eaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEmailNotification", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Optional[builtins.str]:
        '''Customized text to include in the invitation email message.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "message"))

    @message.setter
    def message(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31ea094d2aaa558144a048004a5a7542d051737344a0807aac03c8ba0e840fc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_detective.CfnMemberInvitationProps",
    jsii_struct_bases=[],
    name_mapping={
        "graph_arn": "graphArn",
        "member_email_address": "memberEmailAddress",
        "member_id": "memberId",
        "disable_email_notification": "disableEmailNotification",
        "message": "message",
    },
)
class CfnMemberInvitationProps:
    def __init__(
        self,
        *,
        graph_arn: builtins.str,
        member_email_address: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMemberInvitation``.

        :param graph_arn: The ARN of the behavior graph to invite the account to contribute data to.
        :param member_email_address: The root user email address of the invited account. If the email address provided is not the root user email address for the provided account, the invitation creation fails.
        :param member_id: The AWS account identifier of the invited account.
        :param disable_email_notification: Whether to send an invitation email to the member account. If set to true, the member account does not receive an invitation email. Default: - false
        :param message: Customized text to include in the invitation email message.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_detective as detective
            
            cfn_member_invitation_props = detective.CfnMemberInvitationProps(
                graph_arn="graphArn",
                member_email_address="memberEmailAddress",
                member_id="memberId",
            
                # the properties below are optional
                disable_email_notification=False,
                message="message"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6168872a1142480c9838dd35aabe4ddc94fa8bd63cd0e251f53d61f6a9924b3a)
            check_type(argname="argument graph_arn", value=graph_arn, expected_type=type_hints["graph_arn"])
            check_type(argname="argument member_email_address", value=member_email_address, expected_type=type_hints["member_email_address"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
            check_type(argname="argument disable_email_notification", value=disable_email_notification, expected_type=type_hints["disable_email_notification"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_arn": graph_arn,
            "member_email_address": member_email_address,
            "member_id": member_id,
        }
        if disable_email_notification is not None:
            self._values["disable_email_notification"] = disable_email_notification
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def graph_arn(self) -> builtins.str:
        '''The ARN of the behavior graph to invite the account to contribute data to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-grapharn
        '''
        result = self._values.get("graph_arn")
        assert result is not None, "Required property 'graph_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_email_address(self) -> builtins.str:
        '''The root user email address of the invited account.

        If the email address provided is not the root user email address for the provided account, the invitation creation fails.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberemailaddress
        '''
        result = self._values.get("member_email_address")
        assert result is not None, "Required property 'member_email_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(self) -> builtins.str:
        '''The AWS account identifier of the invited account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to send an invitation email to the member account.

        If set to true, the member account does not receive an invitation email.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-disableemailnotification
        '''
        result = self._values.get("disable_email_notification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Customized text to include in the invitation email message.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemberInvitationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnOrganizationAdmin(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_detective.CfnOrganizationAdmin",
):
    '''The ``AWS::Detective::OrganizationAdmin`` resource is an Amazon Detective resource type that designates the Detective administrator account for the organization in the current region.

    If the account does not have Detective enabled, then this resource enables Detective for that account and creates a new behavior graph.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_detective as detective
        
        cfn_organization_admin = detective.CfnOrganizationAdmin(self, "MyCfnOrganizationAdmin",
            account_id="accountId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account_id: The AWS account identifier of the account to designate as the Detective administrator account for the organization.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af46c55b142c272aabfd3b293f9ccf1547910145fb8eb3c1a9a019652cd54fa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationAdminProps(account_id=account_id)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9afea3e493aa39786d788e14325de3fed57b80257e73fef9fe6672ef74f94c6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__257f0f051d1ceb0d963fe00a9089a670e5c90961aee260faa726e53bba38b1f7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGraphArn")
    def attr_graph_arn(self) -> builtins.str:
        '''The ARN of the behavior graph to invite the account to contribute data to.

        :cloudformationAttribute: GraphArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGraphArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        '''The AWS account identifier of the account to designate as the Detective administrator account for the organization.'''
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b3ebd6ff4fb0708cfa2cc5ee080b09356c9175b7e842ebce16ec9cba148b7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_detective.CfnOrganizationAdminProps",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class CfnOrganizationAdminProps:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''Properties for defining a ``CfnOrganizationAdmin``.

        :param account_id: The AWS account identifier of the account to designate as the Detective administrator account for the organization.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_detective as detective
            
            cfn_organization_admin_props = detective.CfnOrganizationAdminProps(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__164d4fa1c8c00a35586a49186d85259b687131e38684be0bfa265178bc9896dc)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AWS account identifier of the account to designate as the Detective administrator account for the organization.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html#cfn-detective-organizationadmin-accountid
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationAdminProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGraph",
    "CfnGraphProps",
    "CfnMemberInvitation",
    "CfnMemberInvitationProps",
    "CfnOrganizationAdmin",
    "CfnOrganizationAdminProps",
]

publication.publish()

def _typecheckingstub__35c13d9bc47be944ae94949da016fdbb9358dcb215abb1da6176d7e3ee53a804(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_enable_members: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__759c0a91a60111bc6af09d55e323cbfdd01e2a1beda41d95d78c666e94579275(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46fde5f95e1a0971beb1da64e90595afb005f925e05b021a1b3b807498818ab8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017213db557533db476b11d3395ad002c1c77bc8cc9e28bdee567c8e34fc6ae0(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeb800de7e2138cfe98794158b6d6acc2871d2831f80f41887f5118e20ddcba7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a226decb0450af1162df8b1540b45da7e7669d305d0e8a36b824b4e85332f93(
    *,
    auto_enable_members: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e34d274362e0f21d70fec2895986898f3c3ecf0e61cfff18301ece8bbca92937(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    graph_arn: builtins.str,
    member_email_address: builtins.str,
    member_id: builtins.str,
    disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a79276f8311d161ad0c97e0224bf67f13caeb3555f9726d01364e5d8c9221a4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a41a4a8122f98766d433d9f5e7b7fe3cfd79846b79b03e375826f7f0400376c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12ee371571562da274cbc7b8f9ea5fcd9b0f00711e7457cdaa512b01dd4d9f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__effa006ed39255027e20425818f01d5bd8d8799e0f0c9bbaa8605773192cb9e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0493b702981486fe3adacfc3b48927622dac6cb286fac2e11ee81e222b483192(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660e62f59a214a78dff16da1b8a2a68e2f58419729f3c700cdee6f7697a65eaf(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31ea094d2aaa558144a048004a5a7542d051737344a0807aac03c8ba0e840fc1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6168872a1142480c9838dd35aabe4ddc94fa8bd63cd0e251f53d61f6a9924b3a(
    *,
    graph_arn: builtins.str,
    member_email_address: builtins.str,
    member_id: builtins.str,
    disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af46c55b142c272aabfd3b293f9ccf1547910145fb8eb3c1a9a019652cd54fa(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9afea3e493aa39786d788e14325de3fed57b80257e73fef9fe6672ef74f94c6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257f0f051d1ceb0d963fe00a9089a670e5c90961aee260faa726e53bba38b1f7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b3ebd6ff4fb0708cfa2cc5ee080b09356c9175b7e842ebce16ec9cba148b7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__164d4fa1c8c00a35586a49186d85259b687131e38684be0bfa265178bc9896dc(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
