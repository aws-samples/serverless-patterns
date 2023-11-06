'''
# AWS::SupportApp Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_supportapp as supportapp
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SupportApp construct libraries](https://constructs.dev/search?q=supportapp)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SupportApp resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SupportApp.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SupportApp](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SupportApp.html).

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
class CfnAccountAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_supportapp.CfnAccountAlias",
):
    '''You can use the ``AWS::SupportApp::AccountAlias`` resource to specify your AWS account when you configure the AWS Support App in Slack.

    Your alias name appears on the AWS Support App page in the Support Center Console and in messages from the AWS Support App. You can use this alias to identify the account you've configured with the AWS Support App .

    For more information, see `AWS Support App in Slack <https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html>`_ in the *AWS Support User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-accountalias.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_supportapp as supportapp
        
        cfn_account_alias = supportapp.CfnAccountAlias(self, "MyCfnAccountAlias",
            account_alias="accountAlias"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account_alias: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account_alias: An alias or short name for an AWS account .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adc663f014a8631377fa42be2ddca3e4697c00856f997592dde64d9a2f62fff8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccountAliasProps(account_alias=account_alias)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3dd85fea57bcb6e9e53f9b8689a087277bd089365db5931813d3993e7bada0a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b34a975b7c3c8e237070c408182a45665ce2b5bb2f7a80177873f4b757f08eea)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountAliasResourceId")
    def attr_account_alias_resource_id(self) -> builtins.str:
        '''The ``AccountAlias`` resource type has an attribute ``AccountAliasResourceId`` . You can use this attribute to identify the resource.

        The ``AccountAliasResourceId`` will be ``AccountAlias_for_accountId`` . In this example, ``AccountAlias_for_`` is the prefix and ``accountId`` is your AWS account number, such as ``AccountAlias_for_123456789012`` .

        :cloudformationAttribute: AccountAliasResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountAliasResourceId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accountAlias")
    def account_alias(self) -> builtins.str:
        '''An alias or short name for an AWS account .'''
        return typing.cast(builtins.str, jsii.get(self, "accountAlias"))

    @account_alias.setter
    def account_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fde9ac7f5be17538e97741bfe840be954079267e66852796867becf705e946c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountAlias", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_supportapp.CfnAccountAliasProps",
    jsii_struct_bases=[],
    name_mapping={"account_alias": "accountAlias"},
)
class CfnAccountAliasProps:
    def __init__(self, *, account_alias: builtins.str) -> None:
        '''Properties for defining a ``CfnAccountAlias``.

        :param account_alias: An alias or short name for an AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-accountalias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_supportapp as supportapp
            
            cfn_account_alias_props = supportapp.CfnAccountAliasProps(
                account_alias="accountAlias"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd7f9fb021f2681b1ee1ddee9d4508a19d0b9c944c0121f242a80ec2227de5e)
            check_type(argname="argument account_alias", value=account_alias, expected_type=type_hints["account_alias"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_alias": account_alias,
        }

    @builtins.property
    def account_alias(self) -> builtins.str:
        '''An alias or short name for an AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-accountalias.html#cfn-supportapp-accountalias-accountalias
        '''
        result = self._values.get("account_alias")
        assert result is not None, "Required property 'account_alias' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccountAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSlackChannelConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_supportapp.CfnSlackChannelConfiguration",
):
    '''You can use the ``AWS::SupportApp::SlackChannelConfiguration`` resource to specify your AWS account when you configure the AWS Support App .

    This resource includes the following information:

    - The Slack channel name and ID
    - The team ID in Slack
    - The Amazon Resource Name (ARN) of the AWS Identity and Access Management ( IAM ) role
    - Whether you want the AWS Support App to notify you when your support cases are created, updated, resolved, or reopened
    - The case severity that you want to get notified for

    For more information, see the following topics in the *AWS Support User Guide* :

    - `AWS Support App in Slack <https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html>`_
    - `Creating AWS Support App in Slack resources with AWS CloudFormation <https://docs.aws.amazon.com/awssupport/latest/user/creating-resources-with-cloudformation.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_supportapp as supportapp
        
        cfn_slack_channel_configuration = supportapp.CfnSlackChannelConfiguration(self, "MyCfnSlackChannelConfiguration",
            channel_id="channelId",
            channel_role_arn="channelRoleArn",
            notify_on_case_severity="notifyOnCaseSeverity",
            team_id="teamId",
        
            # the properties below are optional
            channel_name="channelName",
            notify_on_add_correspondence_to_case=False,
            notify_on_create_or_reopen_case=False,
            notify_on_resolve_case=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        channel_id: builtins.str,
        channel_role_arn: builtins.str,
        notify_on_case_severity: builtins.str,
        team_id: builtins.str,
        channel_name: typing.Optional[builtins.str] = None,
        notify_on_add_correspondence_to_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        notify_on_create_or_reopen_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        notify_on_resolve_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_id: The channel ID in Slack. This ID identifies a channel within a Slack workspace.
        :param channel_role_arn: The Amazon Resource Name (ARN) of the IAM role for this Slack channel configuration. The AWS Support App uses this role to perform AWS Support and Service Quotas actions on your behalf.
        :param notify_on_case_severity: The case severity for your support cases that you want to receive notifications. You can specify ``none`` , ``all`` , or ``high`` .
        :param team_id: The team ID in Slack. This ID uniquely identifies a Slack workspace.
        :param channel_name: The channel name in Slack. This is the channel where you invite the AWS Support App .
        :param notify_on_add_correspondence_to_case: Whether to get notified when a correspondence is added to your support cases.
        :param notify_on_create_or_reopen_case: Whether to get notified when your support cases are created or reopened.
        :param notify_on_resolve_case: Whether to get notified when your support cases are resolved.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e35f22740d18bea5877d00346f0c0dfc0f8a99695f5876d0bb73d3f74836be30)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSlackChannelConfigurationProps(
            channel_id=channel_id,
            channel_role_arn=channel_role_arn,
            notify_on_case_severity=notify_on_case_severity,
            team_id=team_id,
            channel_name=channel_name,
            notify_on_add_correspondence_to_case=notify_on_add_correspondence_to_case,
            notify_on_create_or_reopen_case=notify_on_create_or_reopen_case,
            notify_on_resolve_case=notify_on_resolve_case,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0fcceb2218bf8cf1c54787e7d3ee2882c22cde356972b41b0b399cc8b4363c6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__292f2c17279ab74c21868d9008d2fa26a484eae189ddaec0d6e021f6ef5e2462)
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
    @jsii.member(jsii_name="channelId")
    def channel_id(self) -> builtins.str:
        '''The channel ID in Slack.'''
        return typing.cast(builtins.str, jsii.get(self, "channelId"))

    @channel_id.setter
    def channel_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffe28b2d0eb8b11fbc4a2c27fcd61a83f5a100fe03c0ab639b4c6e4b3e33ad97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelId", value)

    @builtins.property
    @jsii.member(jsii_name="channelRoleArn")
    def channel_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role for this Slack channel configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "channelRoleArn"))

    @channel_role_arn.setter
    def channel_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f715a6c77d680fa338c311c1d85f10785a34855a6418e2e273d0601b721ae55a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="notifyOnCaseSeverity")
    def notify_on_case_severity(self) -> builtins.str:
        '''The case severity for your support cases that you want to receive notifications.'''
        return typing.cast(builtins.str, jsii.get(self, "notifyOnCaseSeverity"))

    @notify_on_case_severity.setter
    def notify_on_case_severity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43889d99461b4eb354d3cda7eac0e70aa64aa695099d6d58aea1b4450edcce73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyOnCaseSeverity", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        '''The team ID in Slack.'''
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0c8b06d535fec4288c5729f7abbd4b628bc6d95a8d237291be707222bb4dfa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''The channel name in Slack.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ee993d7f3cacc21f7ddb4348e334d9d7988e68e53fe09ce2a5c9584d0eece64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value)

    @builtins.property
    @jsii.member(jsii_name="notifyOnAddCorrespondenceToCase")
    def notify_on_add_correspondence_to_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to get notified when a correspondence is added to your support cases.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "notifyOnAddCorrespondenceToCase"))

    @notify_on_add_correspondence_to_case.setter
    def notify_on_add_correspondence_to_case(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8cd4cea2b5fb7897f3ab091e75cdd4a5ca0265e070b473a358a38c910b33c90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyOnAddCorrespondenceToCase", value)

    @builtins.property
    @jsii.member(jsii_name="notifyOnCreateOrReopenCase")
    def notify_on_create_or_reopen_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to get notified when your support cases are created or reopened.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "notifyOnCreateOrReopenCase"))

    @notify_on_create_or_reopen_case.setter
    def notify_on_create_or_reopen_case(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__921399ffc2d54516aa2373e50e1a3e13600afdf675d89510f94d97c081fd7154)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyOnCreateOrReopenCase", value)

    @builtins.property
    @jsii.member(jsii_name="notifyOnResolveCase")
    def notify_on_resolve_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to get notified when your support cases are resolved.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "notifyOnResolveCase"))

    @notify_on_resolve_case.setter
    def notify_on_resolve_case(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdf168cfdf59423abb532004d6218672a01d6693597b0f69fecd68f3be197540)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyOnResolveCase", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_supportapp.CfnSlackChannelConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_id": "channelId",
        "channel_role_arn": "channelRoleArn",
        "notify_on_case_severity": "notifyOnCaseSeverity",
        "team_id": "teamId",
        "channel_name": "channelName",
        "notify_on_add_correspondence_to_case": "notifyOnAddCorrespondenceToCase",
        "notify_on_create_or_reopen_case": "notifyOnCreateOrReopenCase",
        "notify_on_resolve_case": "notifyOnResolveCase",
    },
)
class CfnSlackChannelConfigurationProps:
    def __init__(
        self,
        *,
        channel_id: builtins.str,
        channel_role_arn: builtins.str,
        notify_on_case_severity: builtins.str,
        team_id: builtins.str,
        channel_name: typing.Optional[builtins.str] = None,
        notify_on_add_correspondence_to_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        notify_on_create_or_reopen_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        notify_on_resolve_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSlackChannelConfiguration``.

        :param channel_id: The channel ID in Slack. This ID identifies a channel within a Slack workspace.
        :param channel_role_arn: The Amazon Resource Name (ARN) of the IAM role for this Slack channel configuration. The AWS Support App uses this role to perform AWS Support and Service Quotas actions on your behalf.
        :param notify_on_case_severity: The case severity for your support cases that you want to receive notifications. You can specify ``none`` , ``all`` , or ``high`` .
        :param team_id: The team ID in Slack. This ID uniquely identifies a Slack workspace.
        :param channel_name: The channel name in Slack. This is the channel where you invite the AWS Support App .
        :param notify_on_add_correspondence_to_case: Whether to get notified when a correspondence is added to your support cases.
        :param notify_on_create_or_reopen_case: Whether to get notified when your support cases are created or reopened.
        :param notify_on_resolve_case: Whether to get notified when your support cases are resolved.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_supportapp as supportapp
            
            cfn_slack_channel_configuration_props = supportapp.CfnSlackChannelConfigurationProps(
                channel_id="channelId",
                channel_role_arn="channelRoleArn",
                notify_on_case_severity="notifyOnCaseSeverity",
                team_id="teamId",
            
                # the properties below are optional
                channel_name="channelName",
                notify_on_add_correspondence_to_case=False,
                notify_on_create_or_reopen_case=False,
                notify_on_resolve_case=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1843e7081e108ba747a740558f507bae85fe1c8cfcc3feaeba051b183cee274)
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
            check_type(argname="argument channel_role_arn", value=channel_role_arn, expected_type=type_hints["channel_role_arn"])
            check_type(argname="argument notify_on_case_severity", value=notify_on_case_severity, expected_type=type_hints["notify_on_case_severity"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument notify_on_add_correspondence_to_case", value=notify_on_add_correspondence_to_case, expected_type=type_hints["notify_on_add_correspondence_to_case"])
            check_type(argname="argument notify_on_create_or_reopen_case", value=notify_on_create_or_reopen_case, expected_type=type_hints["notify_on_create_or_reopen_case"])
            check_type(argname="argument notify_on_resolve_case", value=notify_on_resolve_case, expected_type=type_hints["notify_on_resolve_case"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_id": channel_id,
            "channel_role_arn": channel_role_arn,
            "notify_on_case_severity": notify_on_case_severity,
            "team_id": team_id,
        }
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if notify_on_add_correspondence_to_case is not None:
            self._values["notify_on_add_correspondence_to_case"] = notify_on_add_correspondence_to_case
        if notify_on_create_or_reopen_case is not None:
            self._values["notify_on_create_or_reopen_case"] = notify_on_create_or_reopen_case
        if notify_on_resolve_case is not None:
            self._values["notify_on_resolve_case"] = notify_on_resolve_case

    @builtins.property
    def channel_id(self) -> builtins.str:
        '''The channel ID in Slack.

        This ID identifies a channel within a Slack workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-channelid
        '''
        result = self._values.get("channel_id")
        assert result is not None, "Required property 'channel_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role for this Slack channel configuration.

        The AWS Support App uses this role to perform AWS Support and Service Quotas actions on your behalf.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-channelrolearn
        '''
        result = self._values.get("channel_role_arn")
        assert result is not None, "Required property 'channel_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notify_on_case_severity(self) -> builtins.str:
        '''The case severity for your support cases that you want to receive notifications.

        You can specify ``none`` , ``all`` , or ``high`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-notifyoncaseseverity
        '''
        result = self._values.get("notify_on_case_severity")
        assert result is not None, "Required property 'notify_on_case_severity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def team_id(self) -> builtins.str:
        '''The team ID in Slack.

        This ID uniquely identifies a Slack workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-teamid
        '''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''The channel name in Slack.

        This is the channel where you invite the AWS Support App .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-channelname
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notify_on_add_correspondence_to_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to get notified when a correspondence is added to your support cases.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-notifyonaddcorrespondencetocase
        '''
        result = self._values.get("notify_on_add_correspondence_to_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def notify_on_create_or_reopen_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to get notified when your support cases are created or reopened.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-notifyoncreateorreopencase
        '''
        result = self._values.get("notify_on_create_or_reopen_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def notify_on_resolve_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to get notified when your support cases are resolved.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-notifyonresolvecase
        '''
        result = self._values.get("notify_on_resolve_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSlackChannelConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSlackWorkspaceConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_supportapp.CfnSlackWorkspaceConfiguration",
):
    '''You can use the ``AWS::SupportApp::SlackWorkspaceConfiguration`` resource to specify your Slack workspace configuration.

    This resource configures your AWS account so that you can use the specified Slack workspace in the AWS Support App . This resource includes the following information:

    - The team ID for the Slack workspace
    - The version ID of the resource to use with AWS CloudFormation

    For more information, see the following topics in the *AWS Support User Guide* :

    - `AWS Support App in Slack <https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html>`_
    - `Creating AWS Support App in Slack resources with AWS CloudFormation <https://docs.aws.amazon.com/awssupport/latest/user/creating-resources-with-cloudformation.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_supportapp as supportapp
        
        cfn_slack_workspace_configuration = supportapp.CfnSlackWorkspaceConfiguration(self, "MyCfnSlackWorkspaceConfiguration",
            team_id="teamId",
        
            # the properties below are optional
            version_id="versionId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        team_id: builtins.str,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param team_id: The team ID in Slack. This ID uniquely identifies a Slack workspace, such as ``T012ABCDEFG`` .
        :param version_id: An identifier used to update an existing Slack workspace configuration in AWS CloudFormation , such as ``100`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d0583297d2e6c375e6cdb181da90b314f05ff30ac14e4871aee08c02c6e3ba9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSlackWorkspaceConfigurationProps(
            team_id=team_id, version_id=version_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3918e45acd71c83f26b84dca0a2a8bed71a05ca2b72eb939649bb36c55f6b17b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5877cbec75443b7954d3eaadf8db63d435ba5f2aee8512840a994c27f8609ad5)
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
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        '''The team ID in Slack.'''
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96287eac0dcd1b969ed2409312a0160a9263ba631a67ad99c2e8535a2d29da0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> typing.Optional[builtins.str]:
        '''An identifier used to update an existing Slack workspace configuration in AWS CloudFormation , such as ``100`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f10519eb1d45ed1305e842ac3665885bde5d1c65940455981356edc1d9e295e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_supportapp.CfnSlackWorkspaceConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"team_id": "teamId", "version_id": "versionId"},
)
class CfnSlackWorkspaceConfigurationProps:
    def __init__(
        self,
        *,
        team_id: builtins.str,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSlackWorkspaceConfiguration``.

        :param team_id: The team ID in Slack. This ID uniquely identifies a Slack workspace, such as ``T012ABCDEFG`` .
        :param version_id: An identifier used to update an existing Slack workspace configuration in AWS CloudFormation , such as ``100`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_supportapp as supportapp
            
            cfn_slack_workspace_configuration_props = supportapp.CfnSlackWorkspaceConfigurationProps(
                team_id="teamId",
            
                # the properties below are optional
                version_id="versionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b53646f592b68acb6be1739217822ffee1d340b2812e0c7ac946b5c0f163437)
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "team_id": team_id,
        }
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def team_id(self) -> builtins.str:
        '''The team ID in Slack.

        This ID uniquely identifies a Slack workspace, such as ``T012ABCDEFG`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html#cfn-supportapp-slackworkspaceconfiguration-teamid
        '''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''An identifier used to update an existing Slack workspace configuration in AWS CloudFormation , such as ``100`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html#cfn-supportapp-slackworkspaceconfiguration-versionid
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSlackWorkspaceConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccountAlias",
    "CfnAccountAliasProps",
    "CfnSlackChannelConfiguration",
    "CfnSlackChannelConfigurationProps",
    "CfnSlackWorkspaceConfiguration",
    "CfnSlackWorkspaceConfigurationProps",
]

publication.publish()

def _typecheckingstub__adc663f014a8631377fa42be2ddca3e4697c00856f997592dde64d9a2f62fff8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_alias: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3dd85fea57bcb6e9e53f9b8689a087277bd089365db5931813d3993e7bada0a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34a975b7c3c8e237070c408182a45665ce2b5bb2f7a80177873f4b757f08eea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fde9ac7f5be17538e97741bfe840be954079267e66852796867becf705e946c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd7f9fb021f2681b1ee1ddee9d4508a19d0b9c944c0121f242a80ec2227de5e(
    *,
    account_alias: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35f22740d18bea5877d00346f0c0dfc0f8a99695f5876d0bb73d3f74836be30(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_id: builtins.str,
    channel_role_arn: builtins.str,
    notify_on_case_severity: builtins.str,
    team_id: builtins.str,
    channel_name: typing.Optional[builtins.str] = None,
    notify_on_add_correspondence_to_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    notify_on_create_or_reopen_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    notify_on_resolve_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0fcceb2218bf8cf1c54787e7d3ee2882c22cde356972b41b0b399cc8b4363c6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__292f2c17279ab74c21868d9008d2fa26a484eae189ddaec0d6e021f6ef5e2462(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffe28b2d0eb8b11fbc4a2c27fcd61a83f5a100fe03c0ab639b4c6e4b3e33ad97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f715a6c77d680fa338c311c1d85f10785a34855a6418e2e273d0601b721ae55a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43889d99461b4eb354d3cda7eac0e70aa64aa695099d6d58aea1b4450edcce73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c8b06d535fec4288c5729f7abbd4b628bc6d95a8d237291be707222bb4dfa5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee993d7f3cacc21f7ddb4348e334d9d7988e68e53fe09ce2a5c9584d0eece64(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8cd4cea2b5fb7897f3ab091e75cdd4a5ca0265e070b473a358a38c910b33c90(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921399ffc2d54516aa2373e50e1a3e13600afdf675d89510f94d97c081fd7154(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf168cfdf59423abb532004d6218672a01d6693597b0f69fecd68f3be197540(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1843e7081e108ba747a740558f507bae85fe1c8cfcc3feaeba051b183cee274(
    *,
    channel_id: builtins.str,
    channel_role_arn: builtins.str,
    notify_on_case_severity: builtins.str,
    team_id: builtins.str,
    channel_name: typing.Optional[builtins.str] = None,
    notify_on_add_correspondence_to_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    notify_on_create_or_reopen_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    notify_on_resolve_case: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0583297d2e6c375e6cdb181da90b314f05ff30ac14e4871aee08c02c6e3ba9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    team_id: builtins.str,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3918e45acd71c83f26b84dca0a2a8bed71a05ca2b72eb939649bb36c55f6b17b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5877cbec75443b7954d3eaadf8db63d435ba5f2aee8512840a994c27f8609ad5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96287eac0dcd1b969ed2409312a0160a9263ba631a67ad99c2e8535a2d29da0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f10519eb1d45ed1305e842ac3665885bde5d1c65940455981356edc1d9e295e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b53646f592b68acb6be1739217822ffee1d340b2812e0c7ac946b5c0f163437(
    *,
    team_id: builtins.str,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
