'''
# AWS::XRay Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_xray as xray
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for XRay construct libraries](https://constructs.dev/search?q=xray)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::XRay resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_XRay.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::XRay](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_XRay.html).

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
class CfnGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_xray.CfnGroup",
):
    '''Use the ``AWS::XRay::Group`` resource to specify a group with a name and a filter expression.

    Groups enable the collection of traces that match the filter expression, can be used to filter service graphs and traces, and to supply Amazon CloudWatch metrics.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html
    :cloudformationResource: AWS::XRay::Group
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_xray as xray
        
        cfn_group = xray.CfnGroup(self, "MyCfnGroup",
            group_name="groupName",
        
            # the properties below are optional
            filter_expression="filterExpression",
            insights_configuration=xray.CfnGroup.InsightsConfigurationProperty(
                insights_enabled=False,
                notifications_enabled=False
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
        group_name: builtins.str,
        filter_expression: typing.Optional[builtins.str] = None,
        insights_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGroup.InsightsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param group_name: The unique case-sensitive name of the group.
        :param filter_expression: The filter expression defining the parameters to include traces.
        :param insights_configuration: The structure containing configurations related to insights. - The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group. - The NotificationsEnabled boolean can be set to true to enable insights notifications through Amazon EventBridge for the group.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79279e4db6118afe6e4c5be4499d44b2aa6c4ddc5a7ee32f6146b2501493c9d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(
            group_name=group_name,
            filter_expression=filter_expression,
            insights_configuration=insights_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7abca464ae2f7a114f4dd93f3dc1ecbe0792d2bac93a95ac3ac82b16aef5c2e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19f1367ce30e9341420e3d92b8bdc2f9f5a51af03be62558e9ed01e0acc7087d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGroupArn")
    def attr_group_arn(self) -> builtins.str:
        '''The group ARN that was created or updated.

        :cloudformationAttribute: GroupARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGroupArn"))

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
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        '''The unique case-sensitive name of the group.'''
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bac310f0b8e51bb58affed34cf73d91ae569d63e09e4952ee0c2065aabcc9b8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="filterExpression")
    def filter_expression(self) -> typing.Optional[builtins.str]:
        '''The filter expression defining the parameters to include traces.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterExpression"))

    @filter_expression.setter
    def filter_expression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6391d6ff4cc2d0f1149fedb9145d535d8ea36eb3d9204e8c571103f428afbddf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterExpression", value)

    @builtins.property
    @jsii.member(jsii_name="insightsConfiguration")
    def insights_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGroup.InsightsConfigurationProperty"]]:
        '''The structure containing configurations related to insights.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGroup.InsightsConfigurationProperty"]], jsii.get(self, "insightsConfiguration"))

    @insights_configuration.setter
    def insights_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGroup.InsightsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__957f91a4405ce2712333b79726f8bfb8286eec4818a624c669571438f6448b5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a071fb02f9af41678c1aa140934cb53cbcce1dbe74b1a64a172499cda1df59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_xray.CfnGroup.InsightsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "insights_enabled": "insightsEnabled",
            "notifications_enabled": "notificationsEnabled",
        },
    )
    class InsightsConfigurationProperty:
        def __init__(
            self,
            *,
            insights_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            notifications_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The structure containing configurations related to insights.

            :param insights_enabled: Set the InsightsEnabled value to true to enable insights or false to disable insights.
            :param notifications_enabled: Set the NotificationsEnabled value to true to enable insights notifications. Notifications can only be enabled on a group with InsightsEnabled set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_xray as xray
                
                insights_configuration_property = xray.CfnGroup.InsightsConfigurationProperty(
                    insights_enabled=False,
                    notifications_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41527dec5fb77f3f618c6e88ead67e5135576189dbd8c58d81dde45b968915c1)
                check_type(argname="argument insights_enabled", value=insights_enabled, expected_type=type_hints["insights_enabled"])
                check_type(argname="argument notifications_enabled", value=notifications_enabled, expected_type=type_hints["notifications_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if insights_enabled is not None:
                self._values["insights_enabled"] = insights_enabled
            if notifications_enabled is not None:
                self._values["notifications_enabled"] = notifications_enabled

        @builtins.property
        def insights_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set the InsightsEnabled value to true to enable insights or false to disable insights.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html#cfn-xray-group-insightsconfiguration-insightsenabled
            '''
            result = self._values.get("insights_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def notifications_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set the NotificationsEnabled value to true to enable insights notifications.

            Notifications can only be enabled on a group with InsightsEnabled set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html#cfn-xray-group-insightsconfiguration-notificationsenabled
            '''
            result = self._values.get("notifications_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InsightsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_xray.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "filter_expression": "filterExpression",
        "insights_configuration": "insightsConfiguration",
        "tags": "tags",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        group_name: builtins.str,
        filter_expression: typing.Optional[builtins.str] = None,
        insights_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.InsightsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroup``.

        :param group_name: The unique case-sensitive name of the group.
        :param filter_expression: The filter expression defining the parameters to include traces.
        :param insights_configuration: The structure containing configurations related to insights. - The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group. - The NotificationsEnabled boolean can be set to true to enable insights notifications through Amazon EventBridge for the group.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_xray as xray
            
            cfn_group_props = xray.CfnGroupProps(
                group_name="groupName",
            
                # the properties below are optional
                filter_expression="filterExpression",
                insights_configuration=xray.CfnGroup.InsightsConfigurationProperty(
                    insights_enabled=False,
                    notifications_enabled=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df933d0182acdb6109d741b7f8c8d1c6c70bf0511060fb40cc94126c9706fea2)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument filter_expression", value=filter_expression, expected_type=type_hints["filter_expression"])
            check_type(argname="argument insights_configuration", value=insights_configuration, expected_type=type_hints["insights_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
        }
        if filter_expression is not None:
            self._values["filter_expression"] = filter_expression
        if insights_configuration is not None:
            self._values["insights_configuration"] = insights_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The unique case-sensitive name of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-groupname
        '''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_expression(self) -> typing.Optional[builtins.str]:
        '''The filter expression defining the parameters to include traces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-filterexpression
        '''
        result = self._values.get("filter_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insights_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGroup.InsightsConfigurationProperty]]:
        '''The structure containing configurations related to insights.

        - The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group.
        - The NotificationsEnabled boolean can be set to true to enable insights notifications through Amazon EventBridge for the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-insightsconfiguration
        '''
        result = self._values.get("insights_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGroup.InsightsConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_xray.CfnResourcePolicy",
):
    '''Use ``AWS::XRay::ResourcePolicy`` to specify an X-Ray resource-based policy, which grants one or more AWS services and accounts permissions to access X-Ray .

    Each resource-based policy is associated with a specific AWS account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html
    :cloudformationResource: AWS::XRay::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_xray as xray
        
        cfn_resource_policy = xray.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            policy_document="policyDocument",
            policy_name="policyName",
        
            # the properties below are optional
            bypass_policy_lockout_check=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
        bypass_policy_lockout_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: The resource-based policy document, which can be up to 5kb in size.
        :param policy_name: The name of the resource-based policy. Must be unique within a specific AWS account.
        :param bypass_policy_lockout_check: A flag to indicate whether to bypass the resource-based policy lockout safety check.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09bf223d757229b3cb8cbe48721f48c0cbd4a7746b05a01764790f36345573a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(
            policy_document=policy_document,
            policy_name=policy_name,
            bypass_policy_lockout_check=bypass_policy_lockout_check,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913a1daf900403c93bbf0005d03a8be81102dd3bc83cdb8518d2dd1d15b63433)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13b6101ae5cc715d1f79bcacfa86b9fa86e826692e042cfe03258d53519d67fd)
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
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> builtins.str:
        '''The resource-based policy document, which can be up to 5kb in size.'''
        return typing.cast(builtins.str, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af55d3faaae74acf53b854b6a92270baa6db03739fe44ce6145a162d44902a06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the resource-based policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__209c64342e8a5a0263f0a86bbf3fa917b289c6deeccd681fb92a6eb2e88a0c63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="bypassPolicyLockoutCheck")
    def bypass_policy_lockout_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag to indicate whether to bypass the resource-based policy lockout safety check.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "bypassPolicyLockoutCheck"))

    @bypass_policy_lockout_check.setter
    def bypass_policy_lockout_check(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7bdbf1a6df4fd529d3e30429951840ab05b0592694020851839a8a2b9e3e104)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypassPolicyLockoutCheck", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_xray.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_document": "policyDocument",
        "policy_name": "policyName",
        "bypass_policy_lockout_check": "bypassPolicyLockoutCheck",
    },
)
class CfnResourcePolicyProps:
    def __init__(
        self,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
        bypass_policy_lockout_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param policy_document: The resource-based policy document, which can be up to 5kb in size.
        :param policy_name: The name of the resource-based policy. Must be unique within a specific AWS account.
        :param bypass_policy_lockout_check: A flag to indicate whether to bypass the resource-based policy lockout safety check.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_xray as xray
            
            cfn_resource_policy_props = xray.CfnResourcePolicyProps(
                policy_document="policyDocument",
                policy_name="policyName",
            
                # the properties below are optional
                bypass_policy_lockout_check=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bf01f8c2bafe7edbe5e11b45f610f28582a393f64724e6ed0ed222de4072781)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument bypass_policy_lockout_check", value=bypass_policy_lockout_check, expected_type=type_hints["bypass_policy_lockout_check"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "policy_name": policy_name,
        }
        if bypass_policy_lockout_check is not None:
            self._values["bypass_policy_lockout_check"] = bypass_policy_lockout_check

    @builtins.property
    def policy_document(self) -> builtins.str:
        '''The resource-based policy document, which can be up to 5kb in size.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html#cfn-xray-resourcepolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the resource-based policy.

        Must be unique within a specific AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html#cfn-xray-resourcepolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bypass_policy_lockout_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag to indicate whether to bypass the resource-based policy lockout safety check.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html#cfn-xray-resourcepolicy-bypasspolicylockoutcheck
        '''
        result = self._values.get("bypass_policy_lockout_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnSamplingRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_xray.CfnSamplingRule",
):
    '''Use the ``AWS::XRay::SamplingRule`` resource to specify a sampling rule, which controls sampling behavior for instrumented applications.

    Include a ``SamplingRule`` entity to create or update a sampling rule.
    .. epigraph::

       ``SamplingRule.Version`` can only be set when creating a sampling rule. Updating the version will cause the update to fail.

    Services retrieve rules with `GetSamplingRules <https://docs.aws.amazon.com//xray/latest/api/API_GetSamplingRules.html>`_ , and evaluate each rule in ascending order of *priority* for each request. If a rule matches, the service records a trace, borrowing it from the reservoir size. After 10 seconds, the service reports back to X-Ray with `GetSamplingTargets <https://docs.aws.amazon.com//xray/latest/api/API_GetSamplingTargets.html>`_ to get updated versions of each in-use rule. The updated rule contains a trace quota that the service can use instead of borrowing from the reservoir.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html
    :cloudformationResource: AWS::XRay::SamplingRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_xray as xray
        
        cfn_sampling_rule = xray.CfnSamplingRule(self, "MyCfnSamplingRule",
            rule_name="ruleName",
            sampling_rule=xray.CfnSamplingRule.SamplingRuleProperty(
                fixed_rate=123,
                host="host",
                http_method="httpMethod",
                priority=123,
                reservoir_size=123,
                resource_arn="resourceArn",
                service_name="serviceName",
                service_type="serviceType",
                url_path="urlPath",
        
                # the properties below are optional
                attributes={
                    "attributes_key": "attributes"
                },
                rule_arn="ruleArn",
                rule_name="ruleName",
                version=123
            ),
            sampling_rule_record=xray.CfnSamplingRule.SamplingRuleRecordProperty(
                created_at="createdAt",
                modified_at="modifiedAt",
                sampling_rule=xray.CfnSamplingRule.SamplingRuleProperty(
                    fixed_rate=123,
                    host="host",
                    http_method="httpMethod",
                    priority=123,
                    reservoir_size=123,
                    resource_arn="resourceArn",
                    service_name="serviceName",
                    service_type="serviceType",
                    url_path="urlPath",
        
                    # the properties below are optional
                    attributes={
                        "attributes_key": "attributes"
                    },
                    rule_arn="ruleArn",
                    rule_name="ruleName",
                    version=123
                )
            ),
            sampling_rule_update=xray.CfnSamplingRule.SamplingRuleUpdateProperty(
                attributes={
                    "attributes_key": "attributes"
                },
                fixed_rate=123,
                host="host",
                http_method="httpMethod",
                priority=123,
                reservoir_size=123,
                resource_arn="resourceArn",
                rule_arn="ruleArn",
                rule_name="ruleName",
                service_name="serviceName",
                service_type="serviceType",
                url_path="urlPath"
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
        rule_name: typing.Optional[builtins.str] = None,
        sampling_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSamplingRule.SamplingRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sampling_rule_record: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSamplingRule.SamplingRuleRecordProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sampling_rule_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSamplingRule.SamplingRuleUpdateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule_name: (deprecated) The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.
        :param sampling_rule: The sampling rule to be created or updated.
        :param sampling_rule_record: 
        :param sampling_rule_update: 
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb4d975473491dccd407df9690e6fceb6dbcc5ac1f4ba127279d9ee30a29c5d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSamplingRuleProps(
            rule_name=rule_name,
            sampling_rule=sampling_rule,
            sampling_rule_record=sampling_rule_record,
            sampling_rule_update=sampling_rule_update,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__624ab47ce33649518bc24568b8b2583dc957da28537df41f403aeb3ea0680d2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57ea08ad6e6e5bc7db937ef2c2a6789c68855af241a0ba52c0b54453fbb49767)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The sampling rule ARN that was created or updated.

        :cloudformationAttribute: RuleARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The ARN of the sampling rule.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd8d7287c18525ced0edbe0ae13ca6a5a4bb0e697194a6eb3b2bfb5b316ea97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value)

    @builtins.property
    @jsii.member(jsii_name="samplingRule")
    def sampling_rule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleProperty"]]:
        '''The sampling rule to be created or updated.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleProperty"]], jsii.get(self, "samplingRule"))

    @sampling_rule.setter
    def sampling_rule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a965682ad75df2200e58494d853db775e098c0c90dd947b9961224b54bc67ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingRule", value)

    @builtins.property
    @jsii.member(jsii_name="samplingRuleRecord")
    def sampling_rule_record(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleRecordProperty"]]:
        '''
        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleRecordProperty"]], jsii.get(self, "samplingRuleRecord"))

    @sampling_rule_record.setter
    def sampling_rule_record(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleRecordProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ffb44db5e7ce42ca30db4f800cb827f451fb16f3c954b4861aa26a37724c329)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingRuleRecord", value)

    @builtins.property
    @jsii.member(jsii_name="samplingRuleUpdate")
    def sampling_rule_update(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleUpdateProperty"]]:
        '''
        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleUpdateProperty"]], jsii.get(self, "samplingRuleUpdate"))

    @sampling_rule_update.setter
    def sampling_rule_update(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleUpdateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e1134e68ff20f7571a3a6e6eac44897d1f5ed5ab595b9d98fd5cbd23398519e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingRuleUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a1929852408087d2571046ee7f325eff12f76e0d9beeee0f8058531688f32fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_xray.CfnSamplingRule.SamplingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fixed_rate": "fixedRate",
            "host": "host",
            "http_method": "httpMethod",
            "priority": "priority",
            "reservoir_size": "reservoirSize",
            "resource_arn": "resourceArn",
            "service_name": "serviceName",
            "service_type": "serviceType",
            "url_path": "urlPath",
            "attributes": "attributes",
            "rule_arn": "ruleArn",
            "rule_name": "ruleName",
            "version": "version",
        },
    )
    class SamplingRuleProperty:
        def __init__(
            self,
            *,
            fixed_rate: jsii.Number,
            host: builtins.str,
            http_method: builtins.str,
            priority: jsii.Number,
            reservoir_size: jsii.Number,
            resource_arn: builtins.str,
            service_name: builtins.str,
            service_type: builtins.str,
            url_path: builtins.str,
            attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            rule_arn: typing.Optional[builtins.str] = None,
            rule_name: typing.Optional[builtins.str] = None,
            version: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A sampling rule that services use to decide whether to instrument a request.

            Rule fields can match properties of the service, or properties of a request. The service can ignore rules that don't match its properties.

            :param fixed_rate: The percentage of matching requests to instrument, after the reservoir is exhausted.
            :param host: Matches the hostname from a request URL.
            :param http_method: Matches the HTTP method of a request.
            :param priority: The priority of the sampling rule.
            :param reservoir_size: A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
            :param resource_arn: Matches the ARN of the AWS resource on which the service runs.
            :param service_name: Matches the ``name`` that the service uses to identify itself in segments.
            :param service_type: Matches the ``origin`` that the service uses to identify its type in segments.
            :param url_path: Matches the path from a request URL.
            :param attributes: Matches attributes derived from the request. *Map Entries:* Maximum number of 5 items. *Key Length Constraints:* Minimum length of 1. Maximum length of 32. *Value Length Constraints:* Minimum length of 1. Maximum length of 32.
            :param rule_arn: The ARN of the sampling rule. Specify a rule by either name or ARN, but not both. .. epigraph:: Specifying a sampling rule by name is recommended, as specifying by ARN will be deprecated in future.
            :param rule_name: The name of the sampling rule. Specify a rule by either name or ARN, but not both.
            :param version: The version of the sampling rule. ``Version`` can only be set when creating a new sampling rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_xray as xray
                
                sampling_rule_property = xray.CfnSamplingRule.SamplingRuleProperty(
                    fixed_rate=123,
                    host="host",
                    http_method="httpMethod",
                    priority=123,
                    reservoir_size=123,
                    resource_arn="resourceArn",
                    service_name="serviceName",
                    service_type="serviceType",
                    url_path="urlPath",
                
                    # the properties below are optional
                    attributes={
                        "attributes_key": "attributes"
                    },
                    rule_arn="ruleArn",
                    rule_name="ruleName",
                    version=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43bc9b1caf3053b699ff280f7b010b90f9d18aa1854cf7169b6066bf2887c3d9)
                check_type(argname="argument fixed_rate", value=fixed_rate, expected_type=type_hints["fixed_rate"])
                check_type(argname="argument host", value=host, expected_type=type_hints["host"])
                check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument reservoir_size", value=reservoir_size, expected_type=type_hints["reservoir_size"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
                check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
                check_type(argname="argument url_path", value=url_path, expected_type=type_hints["url_path"])
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fixed_rate": fixed_rate,
                "host": host,
                "http_method": http_method,
                "priority": priority,
                "reservoir_size": reservoir_size,
                "resource_arn": resource_arn,
                "service_name": service_name,
                "service_type": service_type,
                "url_path": url_path,
            }
            if attributes is not None:
                self._values["attributes"] = attributes
            if rule_arn is not None:
                self._values["rule_arn"] = rule_arn
            if rule_name is not None:
                self._values["rule_name"] = rule_name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def fixed_rate(self) -> jsii.Number:
            '''The percentage of matching requests to instrument, after the reservoir is exhausted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-fixedrate
            '''
            result = self._values.get("fixed_rate")
            assert result is not None, "Required property 'fixed_rate' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''Matches the hostname from a request URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def http_method(self) -> builtins.str:
            '''Matches the HTTP method of a request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-httpmethod
            '''
            result = self._values.get("http_method")
            assert result is not None, "Required property 'http_method' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def priority(self) -> jsii.Number:
            '''The priority of the sampling rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def reservoir_size(self) -> jsii.Number:
            '''A fixed number of matching requests to instrument per second, prior to applying the fixed rate.

            The reservoir is not used directly by services, but applies to all services using the rule collectively.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-reservoirsize
            '''
            result = self._values.get("reservoir_size")
            assert result is not None, "Required property 'reservoir_size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''Matches the ARN of the AWS resource on which the service runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_name(self) -> builtins.str:
            '''Matches the ``name`` that the service uses to identify itself in segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-servicename
            '''
            result = self._values.get("service_name")
            assert result is not None, "Required property 'service_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_type(self) -> builtins.str:
            '''Matches the ``origin`` that the service uses to identify its type in segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-servicetype
            '''
            result = self._values.get("service_type")
            assert result is not None, "Required property 'service_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def url_path(self) -> builtins.str:
            '''Matches the path from a request URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-urlpath
            '''
            result = self._values.get("url_path")
            assert result is not None, "Required property 'url_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Matches attributes derived from the request.

            *Map Entries:* Maximum number of 5 items.

            *Key Length Constraints:* Minimum length of 1. Maximum length of 32.

            *Value Length Constraints:* Minimum length of 1. Maximum length of 32.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def rule_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

            .. epigraph::

               Specifying a sampling rule by name is recommended, as specifying by ARN will be deprecated in future.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-rulearn
            '''
            result = self._values.get("rule_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_name(self) -> typing.Optional[builtins.str]:
            '''The name of the sampling rule.

            Specify a rule by either name or ARN, but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-rulename
            '''
            result = self._values.get("rule_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[jsii.Number]:
            '''The version of the sampling rule.

            ``Version`` can only be set when creating a new sampling rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamplingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_xray.CfnSamplingRule.SamplingRuleRecordProperty",
        jsii_struct_bases=[],
        name_mapping={
            "created_at": "createdAt",
            "modified_at": "modifiedAt",
            "sampling_rule": "samplingRule",
        },
    )
    class SamplingRuleRecordProperty:
        def __init__(
            self,
            *,
            created_at: typing.Optional[builtins.str] = None,
            modified_at: typing.Optional[builtins.str] = None,
            sampling_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSamplingRule.SamplingRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param created_at: When the rule was created, in Unix time seconds.
            :param modified_at: When the rule was modified, in Unix time seconds.
            :param sampling_rule: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_xray as xray
                
                sampling_rule_record_property = xray.CfnSamplingRule.SamplingRuleRecordProperty(
                    created_at="createdAt",
                    modified_at="modifiedAt",
                    sampling_rule=xray.CfnSamplingRule.SamplingRuleProperty(
                        fixed_rate=123,
                        host="host",
                        http_method="httpMethod",
                        priority=123,
                        reservoir_size=123,
                        resource_arn="resourceArn",
                        service_name="serviceName",
                        service_type="serviceType",
                        url_path="urlPath",
                
                        # the properties below are optional
                        attributes={
                            "attributes_key": "attributes"
                        },
                        rule_arn="ruleArn",
                        rule_name="ruleName",
                        version=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b82d1dc50d432c980a6858f43473d293909235617d21487fdf7d00127b61312d)
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument modified_at", value=modified_at, expected_type=type_hints["modified_at"])
                check_type(argname="argument sampling_rule", value=sampling_rule, expected_type=type_hints["sampling_rule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if created_at is not None:
                self._values["created_at"] = created_at
            if modified_at is not None:
                self._values["modified_at"] = modified_at
            if sampling_rule is not None:
                self._values["sampling_rule"] = sampling_rule

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''When the rule was created, in Unix time seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html#cfn-xray-samplingrule-samplingrulerecord-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def modified_at(self) -> typing.Optional[builtins.str]:
            '''When the rule was modified, in Unix time seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html#cfn-xray-samplingrule-samplingrulerecord-modifiedat
            '''
            result = self._values.get("modified_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sampling_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html#cfn-xray-samplingrule-samplingrulerecord-samplingrule
            '''
            result = self._values.get("sampling_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSamplingRule.SamplingRuleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamplingRuleRecordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_xray.CfnSamplingRule.SamplingRuleUpdateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attributes": "attributes",
            "fixed_rate": "fixedRate",
            "host": "host",
            "http_method": "httpMethod",
            "priority": "priority",
            "reservoir_size": "reservoirSize",
            "resource_arn": "resourceArn",
            "rule_arn": "ruleArn",
            "rule_name": "ruleName",
            "service_name": "serviceName",
            "service_type": "serviceType",
            "url_path": "urlPath",
        },
    )
    class SamplingRuleUpdateProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            fixed_rate: typing.Optional[jsii.Number] = None,
            host: typing.Optional[builtins.str] = None,
            http_method: typing.Optional[builtins.str] = None,
            priority: typing.Optional[jsii.Number] = None,
            reservoir_size: typing.Optional[jsii.Number] = None,
            resource_arn: typing.Optional[builtins.str] = None,
            rule_arn: typing.Optional[builtins.str] = None,
            rule_name: typing.Optional[builtins.str] = None,
            service_name: typing.Optional[builtins.str] = None,
            service_type: typing.Optional[builtins.str] = None,
            url_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attributes: Matches attributes derived from the request.
            :param fixed_rate: The percentage of matching requests to instrument, after the reservoir is exhausted.
            :param host: Matches the hostname from a request URL.
            :param http_method: Matches the HTTP method from a request URL.
            :param priority: The priority of the sampling rule.
            :param reservoir_size: A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
            :param resource_arn: Matches the ARN of the AWS resource on which the service runs.
            :param rule_arn: The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.
            :param rule_name: The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.
            :param service_name: Matches the name that the service uses to identify itself in segments.
            :param service_type: Matches the origin that the service uses to identify its type in segments.
            :param url_path: Matches the path from a request URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_xray as xray
                
                sampling_rule_update_property = xray.CfnSamplingRule.SamplingRuleUpdateProperty(
                    attributes={
                        "attributes_key": "attributes"
                    },
                    fixed_rate=123,
                    host="host",
                    http_method="httpMethod",
                    priority=123,
                    reservoir_size=123,
                    resource_arn="resourceArn",
                    rule_arn="ruleArn",
                    rule_name="ruleName",
                    service_name="serviceName",
                    service_type="serviceType",
                    url_path="urlPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__75a672db5b7c76b4aaf3fd52ee6a4e3a911cc745d1728fa77059a1fcaae2f173)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument fixed_rate", value=fixed_rate, expected_type=type_hints["fixed_rate"])
                check_type(argname="argument host", value=host, expected_type=type_hints["host"])
                check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument reservoir_size", value=reservoir_size, expected_type=type_hints["reservoir_size"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
                check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
                check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
                check_type(argname="argument url_path", value=url_path, expected_type=type_hints["url_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if fixed_rate is not None:
                self._values["fixed_rate"] = fixed_rate
            if host is not None:
                self._values["host"] = host
            if http_method is not None:
                self._values["http_method"] = http_method
            if priority is not None:
                self._values["priority"] = priority
            if reservoir_size is not None:
                self._values["reservoir_size"] = reservoir_size
            if resource_arn is not None:
                self._values["resource_arn"] = resource_arn
            if rule_arn is not None:
                self._values["rule_arn"] = rule_arn
            if rule_name is not None:
                self._values["rule_name"] = rule_name
            if service_name is not None:
                self._values["service_name"] = service_name
            if service_type is not None:
                self._values["service_type"] = service_type
            if url_path is not None:
                self._values["url_path"] = url_path

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Matches attributes derived from the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def fixed_rate(self) -> typing.Optional[jsii.Number]:
            '''The percentage of matching requests to instrument, after the reservoir is exhausted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-fixedrate
            '''
            result = self._values.get("fixed_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def host(self) -> typing.Optional[builtins.str]:
            '''Matches the hostname from a request URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-host
            '''
            result = self._values.get("host")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def http_method(self) -> typing.Optional[builtins.str]:
            '''Matches the HTTP method from a request URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-httpmethod
            '''
            result = self._values.get("http_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            '''The priority of the sampling rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-priority
            '''
            result = self._values.get("priority")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def reservoir_size(self) -> typing.Optional[jsii.Number]:
            '''A fixed number of matching requests to instrument per second, prior to applying the fixed rate.

            The reservoir is not used directly by services, but applies to all services using the rule collectively.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-reservoirsize
            '''
            result = self._values.get("reservoir_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def resource_arn(self) -> typing.Optional[builtins.str]:
            '''Matches the ARN of the AWS resource on which the service runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-resourcearn
            '''
            result = self._values.get("resource_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the sampling rule.

            Specify a rule by either name or ARN, but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-rulearn
            '''
            result = self._values.get("rule_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_name(self) -> typing.Optional[builtins.str]:
            '''The ARN of the sampling rule.

            Specify a rule by either name or ARN, but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-rulename
            '''
            result = self._values.get("rule_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            '''Matches the name that the service uses to identify itself in segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-servicename
            '''
            result = self._values.get("service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_type(self) -> typing.Optional[builtins.str]:
            '''Matches the origin that the service uses to identify its type in segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-servicetype
            '''
            result = self._values.get("service_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url_path(self) -> typing.Optional[builtins.str]:
            '''Matches the path from a request URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-urlpath
            '''
            result = self._values.get("url_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamplingRuleUpdateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_xray.CfnSamplingRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "rule_name": "ruleName",
        "sampling_rule": "samplingRule",
        "sampling_rule_record": "samplingRuleRecord",
        "sampling_rule_update": "samplingRuleUpdate",
        "tags": "tags",
    },
)
class CfnSamplingRuleProps:
    def __init__(
        self,
        *,
        rule_name: typing.Optional[builtins.str] = None,
        sampling_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sampling_rule_record: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleRecordProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sampling_rule_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleUpdateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSamplingRule``.

        :param rule_name: (deprecated) The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.
        :param sampling_rule: The sampling rule to be created or updated.
        :param sampling_rule_record: 
        :param sampling_rule_update: 
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_xray as xray
            
            cfn_sampling_rule_props = xray.CfnSamplingRuleProps(
                rule_name="ruleName",
                sampling_rule=xray.CfnSamplingRule.SamplingRuleProperty(
                    fixed_rate=123,
                    host="host",
                    http_method="httpMethod",
                    priority=123,
                    reservoir_size=123,
                    resource_arn="resourceArn",
                    service_name="serviceName",
                    service_type="serviceType",
                    url_path="urlPath",
            
                    # the properties below are optional
                    attributes={
                        "attributes_key": "attributes"
                    },
                    rule_arn="ruleArn",
                    rule_name="ruleName",
                    version=123
                ),
                sampling_rule_record=xray.CfnSamplingRule.SamplingRuleRecordProperty(
                    created_at="createdAt",
                    modified_at="modifiedAt",
                    sampling_rule=xray.CfnSamplingRule.SamplingRuleProperty(
                        fixed_rate=123,
                        host="host",
                        http_method="httpMethod",
                        priority=123,
                        reservoir_size=123,
                        resource_arn="resourceArn",
                        service_name="serviceName",
                        service_type="serviceType",
                        url_path="urlPath",
            
                        # the properties below are optional
                        attributes={
                            "attributes_key": "attributes"
                        },
                        rule_arn="ruleArn",
                        rule_name="ruleName",
                        version=123
                    )
                ),
                sampling_rule_update=xray.CfnSamplingRule.SamplingRuleUpdateProperty(
                    attributes={
                        "attributes_key": "attributes"
                    },
                    fixed_rate=123,
                    host="host",
                    http_method="httpMethod",
                    priority=123,
                    reservoir_size=123,
                    resource_arn="resourceArn",
                    rule_arn="ruleArn",
                    rule_name="ruleName",
                    service_name="serviceName",
                    service_type="serviceType",
                    url_path="urlPath"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6728191ed28a57c9130311eb26a506218d6fceeade2816c46cf035cf422c06a2)
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument sampling_rule", value=sampling_rule, expected_type=type_hints["sampling_rule"])
            check_type(argname="argument sampling_rule_record", value=sampling_rule_record, expected_type=type_hints["sampling_rule_record"])
            check_type(argname="argument sampling_rule_update", value=sampling_rule_update, expected_type=type_hints["sampling_rule_update"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if sampling_rule is not None:
            self._values["sampling_rule"] = sampling_rule
        if sampling_rule_record is not None:
            self._values["sampling_rule_record"] = sampling_rule_record
        if sampling_rule_update is not None:
            self._values["sampling_rule_update"] = sampling_rule_update
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The ARN of the sampling rule.

        Specify a rule by either name or ARN, but not both.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-rulename
        :stability: deprecated
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sampling_rule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleProperty]]:
        '''The sampling rule to be created or updated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingrule
        '''
        result = self._values.get("sampling_rule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleProperty]], result)

    @builtins.property
    def sampling_rule_record(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleRecordProperty]]:
        '''
        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingrulerecord
        :stability: deprecated
        '''
        result = self._values.get("sampling_rule_record")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleRecordProperty]], result)

    @builtins.property
    def sampling_rule_update(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleUpdateProperty]]:
        '''
        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingruleupdate
        :stability: deprecated
        '''
        result = self._values.get("sampling_rule_update")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleUpdateProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSamplingRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGroup",
    "CfnGroupProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CfnSamplingRule",
    "CfnSamplingRuleProps",
]

publication.publish()

def _typecheckingstub__79279e4db6118afe6e4c5be4499d44b2aa6c4ddc5a7ee32f6146b2501493c9d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_name: builtins.str,
    filter_expression: typing.Optional[builtins.str] = None,
    insights_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.InsightsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7abca464ae2f7a114f4dd93f3dc1ecbe0792d2bac93a95ac3ac82b16aef5c2e2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f1367ce30e9341420e3d92b8bdc2f9f5a51af03be62558e9ed01e0acc7087d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac310f0b8e51bb58affed34cf73d91ae569d63e09e4952ee0c2065aabcc9b8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6391d6ff4cc2d0f1149fedb9145d535d8ea36eb3d9204e8c571103f428afbddf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__957f91a4405ce2712333b79726f8bfb8286eec4818a624c669571438f6448b5d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGroup.InsightsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a071fb02f9af41678c1aa140934cb53cbcce1dbe74b1a64a172499cda1df59(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41527dec5fb77f3f618c6e88ead67e5135576189dbd8c58d81dde45b968915c1(
    *,
    insights_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    notifications_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df933d0182acdb6109d741b7f8c8d1c6c70bf0511060fb40cc94126c9706fea2(
    *,
    group_name: builtins.str,
    filter_expression: typing.Optional[builtins.str] = None,
    insights_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.InsightsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09bf223d757229b3cb8cbe48721f48c0cbd4a7746b05a01764790f36345573a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
    bypass_policy_lockout_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913a1daf900403c93bbf0005d03a8be81102dd3bc83cdb8518d2dd1d15b63433(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13b6101ae5cc715d1f79bcacfa86b9fa86e826692e042cfe03258d53519d67fd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af55d3faaae74acf53b854b6a92270baa6db03739fe44ce6145a162d44902a06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209c64342e8a5a0263f0a86bbf3fa917b289c6deeccd681fb92a6eb2e88a0c63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7bdbf1a6df4fd529d3e30429951840ab05b0592694020851839a8a2b9e3e104(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf01f8c2bafe7edbe5e11b45f610f28582a393f64724e6ed0ed222de4072781(
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
    bypass_policy_lockout_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb4d975473491dccd407df9690e6fceb6dbcc5ac1f4ba127279d9ee30a29c5d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule_name: typing.Optional[builtins.str] = None,
    sampling_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sampling_rule_record: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleRecordProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sampling_rule_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleUpdateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__624ab47ce33649518bc24568b8b2583dc957da28537df41f403aeb3ea0680d2a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ea08ad6e6e5bc7db937ef2c2a6789c68855af241a0ba52c0b54453fbb49767(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd8d7287c18525ced0edbe0ae13ca6a5a4bb0e697194a6eb3b2bfb5b316ea97(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a965682ad75df2200e58494d853db775e098c0c90dd947b9961224b54bc67ef(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ffb44db5e7ce42ca30db4f800cb827f451fb16f3c954b4861aa26a37724c329(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleRecordProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1134e68ff20f7571a3a6e6eac44897d1f5ed5ab595b9d98fd5cbd23398519e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSamplingRule.SamplingRuleUpdateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a1929852408087d2571046ee7f325eff12f76e0d9beeee0f8058531688f32fa(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43bc9b1caf3053b699ff280f7b010b90f9d18aa1854cf7169b6066bf2887c3d9(
    *,
    fixed_rate: jsii.Number,
    host: builtins.str,
    http_method: builtins.str,
    priority: jsii.Number,
    reservoir_size: jsii.Number,
    resource_arn: builtins.str,
    service_name: builtins.str,
    service_type: builtins.str,
    url_path: builtins.str,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    rule_arn: typing.Optional[builtins.str] = None,
    rule_name: typing.Optional[builtins.str] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b82d1dc50d432c980a6858f43473d293909235617d21487fdf7d00127b61312d(
    *,
    created_at: typing.Optional[builtins.str] = None,
    modified_at: typing.Optional[builtins.str] = None,
    sampling_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a672db5b7c76b4aaf3fd52ee6a4e3a911cc745d1728fa77059a1fcaae2f173(
    *,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    fixed_rate: typing.Optional[jsii.Number] = None,
    host: typing.Optional[builtins.str] = None,
    http_method: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    reservoir_size: typing.Optional[jsii.Number] = None,
    resource_arn: typing.Optional[builtins.str] = None,
    rule_arn: typing.Optional[builtins.str] = None,
    rule_name: typing.Optional[builtins.str] = None,
    service_name: typing.Optional[builtins.str] = None,
    service_type: typing.Optional[builtins.str] = None,
    url_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6728191ed28a57c9130311eb26a506218d6fceeade2816c46cf035cf422c06a2(
    *,
    rule_name: typing.Optional[builtins.str] = None,
    sampling_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sampling_rule_record: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleRecordProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sampling_rule_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSamplingRule.SamplingRuleUpdateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
