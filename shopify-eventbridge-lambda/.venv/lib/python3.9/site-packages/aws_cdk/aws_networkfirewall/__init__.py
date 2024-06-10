'''
# AWS::NetworkFirewall Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_networkfirewall as networkfirewall
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NetworkFirewall construct libraries](https://constructs.dev/search?q=networkfirewall)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NetworkFirewall resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkFirewall.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NetworkFirewall](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkFirewall.html).

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
class CfnFirewall(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewall",
):
    '''Use the ``Firewall`` to provide stateful, managed, network firewall and intrusion detection and prevention filtering for your VPCs in Amazon VPC .

    The firewall defines the configuration settings for an AWS Network Firewall firewall. The settings include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall AWS resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html
    :cloudformationResource: AWS::NetworkFirewall::Firewall
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkfirewall as networkfirewall
        
        cfn_firewall = networkfirewall.CfnFirewall(self, "MyCfnFirewall",
            firewall_name="firewallName",
            firewall_policy_arn="firewallPolicyArn",
            subnet_mappings=[networkfirewall.CfnFirewall.SubnetMappingProperty(
                subnet_id="subnetId",
        
                # the properties below are optional
                ip_address_type="ipAddressType"
            )],
            vpc_id="vpcId",
        
            # the properties below are optional
            delete_protection=False,
            description="description",
            firewall_policy_change_protection=False,
            subnet_change_protection=False,
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
        firewall_name: builtins.str,
        firewall_policy_arn: builtins.str,
        subnet_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewall.SubnetMappingProperty", typing.Dict[builtins.str, typing.Any]]]]],
        vpc_id: builtins.str,
        delete_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        firewall_policy_change_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        subnet_change_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param firewall_name: The descriptive name of the firewall. You can't change the name of a firewall after you create it.
        :param firewall_policy_arn: The Amazon Resource Name (ARN) of the firewall policy. The relationship of firewall to firewall policy is many to one. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls.
        :param subnet_mappings: The public subnets that Network Firewall is using for the firewall. Each subnet must belong to a different Availability Zone.
        :param vpc_id: The unique identifier of the VPC where the firewall is in use. You can't change the VPC of a firewall after you create the firewall.
        :param delete_protection: A flag indicating whether it is possible to delete the firewall. A setting of ``TRUE`` indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to ``TRUE`` .
        :param description: A description of the firewall.
        :param firewall_policy_change_protection: A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to ``TRUE`` .
        :param subnet_change_protection: A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to ``TRUE`` .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8735e4ce7e79159823190ad059af802b7721b71930c6b4b8805c4676b38d4d56)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFirewallProps(
            firewall_name=firewall_name,
            firewall_policy_arn=firewall_policy_arn,
            subnet_mappings=subnet_mappings,
            vpc_id=vpc_id,
            delete_protection=delete_protection,
            description=description,
            firewall_policy_change_protection=firewall_policy_change_protection,
            subnet_change_protection=subnet_change_protection,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c4e2793da1cf8bea450c2122d2557d378fad5e129ebb26f114a36cfc6506a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__46677a58d997dd59fd033c9a9ee94e3689cafff9e028d3e2d162ddfeee718547)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointIds")
    def attr_endpoint_ids(self) -> typing.List[builtins.str]:
        '''The unique IDs of the firewall endpoints for all of the subnets that you attached to the firewall.

        The subnets are not listed in any particular order. For example: ``["us-west-2c:vpce-111122223333", "us-west-2a:vpce-987654321098", "us-west-2b:vpce-012345678901"]`` .

        :cloudformationAttribute: EndpointIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrEndpointIds"))

    @builtins.property
    @jsii.member(jsii_name="attrFirewallArn")
    def attr_firewall_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ``Firewall`` .

        :cloudformationAttribute: FirewallArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFirewallId")
    def attr_firewall_id(self) -> builtins.str:
        '''The name of the ``Firewall`` resource.

        :cloudformationAttribute: FirewallId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallId"))

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
    @jsii.member(jsii_name="firewallName")
    def firewall_name(self) -> builtins.str:
        '''The descriptive name of the firewall.'''
        return typing.cast(builtins.str, jsii.get(self, "firewallName"))

    @firewall_name.setter
    def firewall_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdb28f607bba18f9f1db46f554b41c7ddfaaf01fe3c74c5f99726bd72458a115)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallName", value)

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyArn")
    def firewall_policy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the firewall policy.'''
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyArn"))

    @firewall_policy_arn.setter
    def firewall_policy_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c711ef7af7567ab69b12f083b26c4033f7cdf1593bf27227f989d7c73e8c9fc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicyArn", value)

    @builtins.property
    @jsii.member(jsii_name="subnetMappings")
    def subnet_mappings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewall.SubnetMappingProperty"]]]:
        '''The public subnets that Network Firewall is using for the firewall.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewall.SubnetMappingProperty"]]], jsii.get(self, "subnetMappings"))

    @subnet_mappings.setter
    def subnet_mappings(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewall.SubnetMappingProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2f1e41c3294b6f9ed43f3936b8feb28ed4bd73021f059aae4743db717241ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetMappings", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The unique identifier of the VPC where the firewall is in use.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba092b3d0c9ca8819ad31fd4320cebdee3150a45603af80de70f2c0bbb9e04b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="deleteProtection")
    def delete_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag indicating whether it is possible to delete the firewall.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deleteProtection"))

    @delete_protection.setter
    def delete_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d69795554b50f9f4f46a0470d9cf06e4d826d030dcab9f0adfc3a3d566c8b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteProtection", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the firewall.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea0349bbbe56acfbf8d2e11ce10cdd2221eb418df0a6df3602174f8015ca4f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyChangeProtection")
    def firewall_policy_change_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A setting indicating whether the firewall is protected against a change to the firewall policy association.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "firewallPolicyChangeProtection"))

    @firewall_policy_change_protection.setter
    def firewall_policy_change_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee50239d13ab311a798770d372dccb418872f67c3e07c873f5d87e11df129a35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicyChangeProtection", value)

    @builtins.property
    @jsii.member(jsii_name="subnetChangeProtection")
    def subnet_change_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A setting indicating whether the firewall is protected against changes to the subnet associations.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "subnetChangeProtection"))

    @subnet_change_protection.setter
    def subnet_change_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3edeae6cf81be7cb1d87c21080d7c060fb1fdbd872b4292af576701d514ade47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetChangeProtection", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1b2b141c4b9a04d63365f9d8a2a5636d417c4a087ebfbfd40be7336d4d258da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewall.SubnetMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_id": "subnetId", "ip_address_type": "ipAddressType"},
    )
    class SubnetMappingProperty:
        def __init__(
            self,
            *,
            subnet_id: builtins.str,
            ip_address_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ID for a subnet that you want to associate with the firewall.

            AWS Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnet's Availability Zone.

            :param subnet_id: The unique identifier for the subnet.
            :param ip_address_type: The subnet's IP address type. You can't change the IP address type after you create the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                subnet_mapping_property = networkfirewall.CfnFirewall.SubnetMappingProperty(
                    subnet_id="subnetId",
                
                    # the properties below are optional
                    ip_address_type="ipAddressType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf86d50b8eec902ee512afbe0dfd3b1ee2bc8f0b9f4fb9acb4ac637ae3662fc0)
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
                check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_id": subnet_id,
            }
            if ip_address_type is not None:
                self._values["ip_address_type"] = ip_address_type

        @builtins.property
        def subnet_id(self) -> builtins.str:
            '''The unique identifier for the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html#cfn-networkfirewall-firewall-subnetmapping-subnetid
            '''
            result = self._values.get("subnet_id")
            assert result is not None, "Required property 'subnet_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ip_address_type(self) -> typing.Optional[builtins.str]:
            '''The subnet's IP address type.

            You can't change the IP address type after you create the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html#cfn-networkfirewall-firewall-subnetmapping-ipaddresstype
            '''
            result = self._values.get("ip_address_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubnetMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFirewallPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy",
):
    '''Use the ``FirewallPolicy`` to define the stateless and stateful network traffic filtering behavior for your ``Firewall`` .

    You can use one firewall policy for multiple firewalls.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html
    :cloudformationResource: AWS::NetworkFirewall::FirewallPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkfirewall as networkfirewall
        
        cfn_firewall_policy = networkfirewall.CfnFirewallPolicy(self, "MyCfnFirewallPolicy",
            firewall_policy=networkfirewall.CfnFirewallPolicy.FirewallPolicyProperty(
                stateless_default_actions=["statelessDefaultActions"],
                stateless_fragment_default_actions=["statelessFragmentDefaultActions"],
        
                # the properties below are optional
                policy_variables=networkfirewall.CfnFirewallPolicy.PolicyVariablesProperty(
                    rule_variables={
                        "rule_variables_key": {
                            "definition": ["definition"]
                        }
                    }
                ),
                stateful_default_actions=["statefulDefaultActions"],
                stateful_engine_options=networkfirewall.CfnFirewallPolicy.StatefulEngineOptionsProperty(
                    rule_order="ruleOrder",
                    stream_exception_policy="streamExceptionPolicy"
                ),
                stateful_rule_group_references=[networkfirewall.CfnFirewallPolicy.StatefulRuleGroupReferenceProperty(
                    resource_arn="resourceArn",
        
                    # the properties below are optional
                    override=networkfirewall.CfnFirewallPolicy.StatefulRuleGroupOverrideProperty(
                        action="action"
                    ),
                    priority=123
                )],
                stateless_custom_actions=[networkfirewall.CfnFirewallPolicy.CustomActionProperty(
                    action_definition=networkfirewall.CfnFirewallPolicy.ActionDefinitionProperty(
                        publish_metric_action=networkfirewall.CfnFirewallPolicy.PublishMetricActionProperty(
                            dimensions=[networkfirewall.CfnFirewallPolicy.DimensionProperty(
                                value="value"
                            )]
                        )
                    ),
                    action_name="actionName"
                )],
                stateless_rule_group_references=[networkfirewall.CfnFirewallPolicy.StatelessRuleGroupReferenceProperty(
                    priority=123,
                    resource_arn="resourceArn"
                )],
                tls_inspection_configuration_arn="tlsInspectionConfigurationArn"
            ),
            firewall_policy_name="firewallPolicyName",
        
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
        firewall_policy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.FirewallPolicyProperty", typing.Dict[builtins.str, typing.Any]]],
        firewall_policy_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param firewall_policy: The traffic filtering behavior of a firewall policy, defined in a collection of stateless and stateful rule groups and other settings.
        :param firewall_policy_name: The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.
        :param description: A description of the firewall policy.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d88babb6ad6946bc506d4761908231f5bd58eca8a4b6bc16dfccccad329a61ca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFirewallPolicyProps(
            firewall_policy=firewall_policy,
            firewall_policy_name=firewall_policy_name,
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d5c5132a5b6e646e64fbde7a0f144884b26ad6646fb61ce294ea7f055ebdea9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56698f8e6b1c138a730626856a3d169be448aa17fd1614293c276d6b465f45a2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrFirewallPolicyArn")
    def attr_firewall_policy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ``FirewallPolicy`` .

        :cloudformationAttribute: FirewallPolicyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallPolicyArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFirewallPolicyId")
    def attr_firewall_policy_id(self) -> builtins.str:
        '''The unique ID of the ``FirewallPolicy`` resource.

        :cloudformationAttribute: FirewallPolicyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallPolicyId"))

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
    @jsii.member(jsii_name="firewallPolicy")
    def firewall_policy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.FirewallPolicyProperty"]:
        '''The traffic filtering behavior of a firewall policy, defined in a collection of stateless and stateful rule groups and other settings.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.FirewallPolicyProperty"], jsii.get(self, "firewallPolicy"))

    @firewall_policy.setter
    def firewall_policy(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.FirewallPolicyProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__706340078bfabf1ab4df2417fc17af1521f1718330cb1fc0087bd9afbac6b09e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyName")
    def firewall_policy_name(self) -> builtins.str:
        '''The descriptive name of the firewall policy.'''
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyName"))

    @firewall_policy_name.setter
    def firewall_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c7e3a8041e7e54afea999d4d0ef02ac9ae2b07dcdf0a03eae03b540da1897f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the firewall policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17c32ed9aaa9f9ee7c0bc9d17e141d75109032a7a60deaf6aed2663b8c4728a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c11c99d52a27fc2ece4bf3400c4dd843466996564051d6963ae198097626d76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.ActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"publish_metric_action": "publishMetricAction"},
    )
    class ActionDefinitionProperty:
        def __init__(
            self,
            *,
            publish_metric_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.PublishMetricActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A custom action to use in stateless rule actions settings.

            :param publish_metric_action: Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet. This setting defines a CloudWatch dimension value to be published. You can pair this custom action with any of the standard stateless rule actions. For example, you could pair this in a rule action with the standard action that forwards the packet for stateful inspection. Then, when a packet matches the rule, Network Firewall publishes metrics for the packet and forwards it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                action_definition_property = networkfirewall.CfnFirewallPolicy.ActionDefinitionProperty(
                    publish_metric_action=networkfirewall.CfnFirewallPolicy.PublishMetricActionProperty(
                        dimensions=[networkfirewall.CfnFirewallPolicy.DimensionProperty(
                            value="value"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__85467f041a9b94df26a26630991c0c22b625a860b01ccf1dafa4f6c431ca3d2f)
                check_type(argname="argument publish_metric_action", value=publish_metric_action, expected_type=type_hints["publish_metric_action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if publish_metric_action is not None:
                self._values["publish_metric_action"] = publish_metric_action

        @builtins.property
        def publish_metric_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.PublishMetricActionProperty"]]:
            '''Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet.

            This setting defines a CloudWatch dimension value to be published.

            You can pair this custom action with any of the standard stateless rule actions. For example, you could pair this in a rule action with the standard action that forwards the packet for stateful inspection. Then, when a packet matches the rule, Network Firewall publishes metrics for the packet and forwards it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html#cfn-networkfirewall-firewallpolicy-actiondefinition-publishmetricaction
            '''
            result = self._values.get("publish_metric_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.PublishMetricActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.CustomActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_definition": "actionDefinition",
            "action_name": "actionName",
        },
    )
    class CustomActionProperty:
        def __init__(
            self,
            *,
            action_definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.ActionDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
            action_name: builtins.str,
        ) -> None:
            '''An optional, non-standard action to use for stateless packet handling.

            You can define this in addition to the standard action that you must specify.

            You define and name the custom actions that you want to be able to use, and then you reference them by name in your actions settings.

            You can use custom actions in the following places:

            - In an ``RuleGroup.StatelessRulesAndCustomActions`` . The custom actions are available for use by name inside the ``StatelessRulesAndCustomActions`` where you define them. You can use them for your stateless rule actions to specify what to do with a packet that matches the rule's match attributes.
            - In an ``FirewallPolicy`` specification, in ``StatelessCustomActions`` . The custom actions are available for use inside the policy where you define them. You can use them for the policy's default stateless actions settings to specify what to do with packets that don't match any of the policy's stateless rules.

            :param action_definition: The custom action associated with the action name.
            :param action_name: The descriptive name of the custom action. You can't change the name of a custom action after you create it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                custom_action_property = networkfirewall.CfnFirewallPolicy.CustomActionProperty(
                    action_definition=networkfirewall.CfnFirewallPolicy.ActionDefinitionProperty(
                        publish_metric_action=networkfirewall.CfnFirewallPolicy.PublishMetricActionProperty(
                            dimensions=[networkfirewall.CfnFirewallPolicy.DimensionProperty(
                                value="value"
                            )]
                        )
                    ),
                    action_name="actionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1aea5034d17a5ca042ab3479dcb09b74cc8b32425872aa94df5c552a5d6c7fa1)
                check_type(argname="argument action_definition", value=action_definition, expected_type=type_hints["action_definition"])
                check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action_definition": action_definition,
                "action_name": action_name,
            }

        @builtins.property
        def action_definition(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.ActionDefinitionProperty"]:
            '''The custom action associated with the action name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actiondefinition
            '''
            result = self._values.get("action_definition")
            assert result is not None, "Required property 'action_definition' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.ActionDefinitionProperty"], result)

        @builtins.property
        def action_name(self) -> builtins.str:
            '''The descriptive name of the custom action.

            You can't change the name of a custom action after you create it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actionname
            '''
            result = self._values.get("action_name")
            assert result is not None, "Required property 'action_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''The value to use in an Amazon CloudWatch custom metric dimension.

            This is used in the ``PublishMetrics`` custom action. A CloudWatch custom metric dimension is a name/value pair that's part of the identity of a metric.

            AWS Network Firewall sets the dimension name to ``CustomAction`` and you provide the dimension value.

            For more information about CloudWatch custom metric dimensions, see `Publishing Custom Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#usingDimensions>`_ in the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>`_ .

            :param value: The value to use in the custom metric dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                dimension_property = networkfirewall.CfnFirewallPolicy.DimensionProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__774d6b3d9a237f7aee33cd708631d88ea8bd3d72e6ab927132f715b75e77c5a8)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''The value to use in the custom metric dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html#cfn-networkfirewall-firewallpolicy-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.FirewallPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "stateless_default_actions": "statelessDefaultActions",
            "stateless_fragment_default_actions": "statelessFragmentDefaultActions",
            "policy_variables": "policyVariables",
            "stateful_default_actions": "statefulDefaultActions",
            "stateful_engine_options": "statefulEngineOptions",
            "stateful_rule_group_references": "statefulRuleGroupReferences",
            "stateless_custom_actions": "statelessCustomActions",
            "stateless_rule_group_references": "statelessRuleGroupReferences",
            "tls_inspection_configuration_arn": "tlsInspectionConfigurationArn",
        },
    )
    class FirewallPolicyProperty:
        def __init__(
            self,
            *,
            stateless_default_actions: typing.Sequence[builtins.str],
            stateless_fragment_default_actions: typing.Sequence[builtins.str],
            policy_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.PolicyVariablesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            stateful_default_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
            stateful_engine_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.StatefulEngineOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            stateful_rule_group_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.StatefulRuleGroupReferenceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            stateless_custom_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.CustomActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            stateless_rule_group_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.StatelessRuleGroupReferenceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tls_inspection_configuration_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The traffic filtering behavior of a firewall policy, defined in a collection of stateless and stateful rule groups and other settings.

            :param stateless_default_actions: The actions to take on a packet if it doesn't match any of the stateless rules in the policy. If you want non-matching packets to be forwarded for stateful inspection, specify ``aws:forward_to_sfe`` . You must specify one of the standard actions: ``aws:pass`` , ``aws:drop`` , or ``aws:forward_to_sfe`` . In addition, you can specify custom actions that are compatible with your standard section choice. For example, you could specify ``["aws:pass"]`` or you could specify ``["aws:pass", “customActionName”]`` . For information about compatibility, see the custom action descriptions.
            :param stateless_fragment_default_actions: The actions to take on a fragmented packet if it doesn't match any of the stateless rules in the policy. If you want non-matching fragmented packets to be forwarded for stateful inspection, specify ``aws:forward_to_sfe`` . You must specify one of the standard actions: ``aws:pass`` , ``aws:drop`` , or ``aws:forward_to_sfe`` . In addition, you can specify custom actions that are compatible with your standard section choice. For example, you could specify ``["aws:pass"]`` or you could specify ``["aws:pass", “customActionName”]`` . For information about compatibility, see the custom action descriptions.
            :param policy_variables: Contains variables that you can use to override default Suricata settings in your firewall policy.
            :param stateful_default_actions: The default actions to take on a packet that doesn't match any stateful rules. The stateful default action is optional, and is only valid when using the strict rule order. Valid values of the stateful default action: - aws:drop_strict - aws:drop_established - aws:alert_strict - aws:alert_established For more information, see `Strict evaluation order <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html#suricata-strict-rule-evaluation-order.html>`_ in the *AWS Network Firewall Developer Guide* .
            :param stateful_engine_options: Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.
            :param stateful_rule_group_references: References to the stateful rule groups that are used in the policy. These define the inspection criteria in stateful rules.
            :param stateless_custom_actions: The custom action definitions that are available for use in the firewall policy's ``StatelessDefaultActions`` setting. You name each custom action that you define, and then you can use it by name in your default actions specifications.
            :param stateless_rule_group_references: References to the stateless rule groups that are used in the policy. These define the matching criteria in stateless rules.
            :param tls_inspection_configuration_arn: The Amazon Resource Name (ARN) of the TLS inspection configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                firewall_policy_property = networkfirewall.CfnFirewallPolicy.FirewallPolicyProperty(
                    stateless_default_actions=["statelessDefaultActions"],
                    stateless_fragment_default_actions=["statelessFragmentDefaultActions"],
                
                    # the properties below are optional
                    policy_variables=networkfirewall.CfnFirewallPolicy.PolicyVariablesProperty(
                        rule_variables={
                            "rule_variables_key": {
                                "definition": ["definition"]
                            }
                        }
                    ),
                    stateful_default_actions=["statefulDefaultActions"],
                    stateful_engine_options=networkfirewall.CfnFirewallPolicy.StatefulEngineOptionsProperty(
                        rule_order="ruleOrder",
                        stream_exception_policy="streamExceptionPolicy"
                    ),
                    stateful_rule_group_references=[networkfirewall.CfnFirewallPolicy.StatefulRuleGroupReferenceProperty(
                        resource_arn="resourceArn",
                
                        # the properties below are optional
                        override=networkfirewall.CfnFirewallPolicy.StatefulRuleGroupOverrideProperty(
                            action="action"
                        ),
                        priority=123
                    )],
                    stateless_custom_actions=[networkfirewall.CfnFirewallPolicy.CustomActionProperty(
                        action_definition=networkfirewall.CfnFirewallPolicy.ActionDefinitionProperty(
                            publish_metric_action=networkfirewall.CfnFirewallPolicy.PublishMetricActionProperty(
                                dimensions=[networkfirewall.CfnFirewallPolicy.DimensionProperty(
                                    value="value"
                                )]
                            )
                        ),
                        action_name="actionName"
                    )],
                    stateless_rule_group_references=[networkfirewall.CfnFirewallPolicy.StatelessRuleGroupReferenceProperty(
                        priority=123,
                        resource_arn="resourceArn"
                    )],
                    tls_inspection_configuration_arn="tlsInspectionConfigurationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b6a6014864b81482e4c4a383921c58673d84e8e882dc4fb7cea71a2db29fc18)
                check_type(argname="argument stateless_default_actions", value=stateless_default_actions, expected_type=type_hints["stateless_default_actions"])
                check_type(argname="argument stateless_fragment_default_actions", value=stateless_fragment_default_actions, expected_type=type_hints["stateless_fragment_default_actions"])
                check_type(argname="argument policy_variables", value=policy_variables, expected_type=type_hints["policy_variables"])
                check_type(argname="argument stateful_default_actions", value=stateful_default_actions, expected_type=type_hints["stateful_default_actions"])
                check_type(argname="argument stateful_engine_options", value=stateful_engine_options, expected_type=type_hints["stateful_engine_options"])
                check_type(argname="argument stateful_rule_group_references", value=stateful_rule_group_references, expected_type=type_hints["stateful_rule_group_references"])
                check_type(argname="argument stateless_custom_actions", value=stateless_custom_actions, expected_type=type_hints["stateless_custom_actions"])
                check_type(argname="argument stateless_rule_group_references", value=stateless_rule_group_references, expected_type=type_hints["stateless_rule_group_references"])
                check_type(argname="argument tls_inspection_configuration_arn", value=tls_inspection_configuration_arn, expected_type=type_hints["tls_inspection_configuration_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "stateless_default_actions": stateless_default_actions,
                "stateless_fragment_default_actions": stateless_fragment_default_actions,
            }
            if policy_variables is not None:
                self._values["policy_variables"] = policy_variables
            if stateful_default_actions is not None:
                self._values["stateful_default_actions"] = stateful_default_actions
            if stateful_engine_options is not None:
                self._values["stateful_engine_options"] = stateful_engine_options
            if stateful_rule_group_references is not None:
                self._values["stateful_rule_group_references"] = stateful_rule_group_references
            if stateless_custom_actions is not None:
                self._values["stateless_custom_actions"] = stateless_custom_actions
            if stateless_rule_group_references is not None:
                self._values["stateless_rule_group_references"] = stateless_rule_group_references
            if tls_inspection_configuration_arn is not None:
                self._values["tls_inspection_configuration_arn"] = tls_inspection_configuration_arn

        @builtins.property
        def stateless_default_actions(self) -> typing.List[builtins.str]:
            '''The actions to take on a packet if it doesn't match any of the stateless rules in the policy.

            If you want non-matching packets to be forwarded for stateful inspection, specify ``aws:forward_to_sfe`` .

            You must specify one of the standard actions: ``aws:pass`` , ``aws:drop`` , or ``aws:forward_to_sfe`` . In addition, you can specify custom actions that are compatible with your standard section choice.

            For example, you could specify ``["aws:pass"]`` or you could specify ``["aws:pass", “customActionName”]`` . For information about compatibility, see the custom action descriptions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessdefaultactions
            '''
            result = self._values.get("stateless_default_actions")
            assert result is not None, "Required property 'stateless_default_actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def stateless_fragment_default_actions(self) -> typing.List[builtins.str]:
            '''The actions to take on a fragmented packet if it doesn't match any of the stateless rules in the policy.

            If you want non-matching fragmented packets to be forwarded for stateful inspection, specify ``aws:forward_to_sfe`` .

            You must specify one of the standard actions: ``aws:pass`` , ``aws:drop`` , or ``aws:forward_to_sfe`` . In addition, you can specify custom actions that are compatible with your standard section choice.

            For example, you could specify ``["aws:pass"]`` or you could specify ``["aws:pass", “customActionName”]`` . For information about compatibility, see the custom action descriptions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessfragmentdefaultactions
            '''
            result = self._values.get("stateless_fragment_default_actions")
            assert result is not None, "Required property 'stateless_fragment_default_actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def policy_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.PolicyVariablesProperty"]]:
            '''Contains variables that you can use to override default Suricata settings in your firewall policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-policyvariables
            '''
            result = self._values.get("policy_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.PolicyVariablesProperty"]], result)

        @builtins.property
        def stateful_default_actions(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The default actions to take on a packet that doesn't match any stateful rules.

            The stateful default action is optional, and is only valid when using the strict rule order.

            Valid values of the stateful default action:

            - aws:drop_strict
            - aws:drop_established
            - aws:alert_strict
            - aws:alert_established

            For more information, see `Strict evaluation order <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html#suricata-strict-rule-evaluation-order.html>`_ in the *AWS Network Firewall Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefuldefaultactions
            '''
            result = self._values.get("stateful_default_actions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def stateful_engine_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.StatefulEngineOptionsProperty"]]:
            '''Additional options governing how Network Firewall handles stateful rules.

            The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulengineoptions
            '''
            result = self._values.get("stateful_engine_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.StatefulEngineOptionsProperty"]], result)

        @builtins.property
        def stateful_rule_group_references(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.StatefulRuleGroupReferenceProperty"]]]]:
            '''References to the stateful rule groups that are used in the policy.

            These define the inspection criteria in stateful rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulrulegroupreferences
            '''
            result = self._values.get("stateful_rule_group_references")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.StatefulRuleGroupReferenceProperty"]]]], result)

        @builtins.property
        def stateless_custom_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.CustomActionProperty"]]]]:
            '''The custom action definitions that are available for use in the firewall policy's ``StatelessDefaultActions`` setting.

            You name each custom action that you define, and then you can use it by name in your default actions specifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelesscustomactions
            '''
            result = self._values.get("stateless_custom_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.CustomActionProperty"]]]], result)

        @builtins.property
        def stateless_rule_group_references(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.StatelessRuleGroupReferenceProperty"]]]]:
            '''References to the stateless rule groups that are used in the policy.

            These define the matching criteria in stateless rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessrulegroupreferences
            '''
            result = self._values.get("stateless_rule_group_references")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.StatelessRuleGroupReferenceProperty"]]]], result)

        @builtins.property
        def tls_inspection_configuration_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the TLS inspection configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-tlsinspectionconfigurationarn
            '''
            result = self._values.get("tls_inspection_configuration_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirewallPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.IPSetProperty",
        jsii_struct_bases=[],
        name_mapping={"definition": "definition"},
    )
    class IPSetProperty:
        def __init__(
            self,
            *,
            definition: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A list of IP addresses and address ranges, in CIDR notation.

            This is part of a ``RuleVariables`` .

            :param definition: The list of IP addresses and address ranges, in CIDR notation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-ipset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                i_pSet_property = {
                    "definition": ["definition"]
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d067b828f689f1f983a48f9f4eb8d06f4dfe2f2e6a20585837d5fe154bfc4ae8)
                check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if definition is not None:
                self._values["definition"] = definition

        @builtins.property
        def definition(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of IP addresses and address ranges, in CIDR notation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-ipset.html#cfn-networkfirewall-firewallpolicy-ipset-definition
            '''
            result = self._values.get("definition")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IPSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.PolicyVariablesProperty",
        jsii_struct_bases=[],
        name_mapping={"rule_variables": "ruleVariables"},
    )
    class PolicyVariablesProperty:
        def __init__(
            self,
            *,
            rule_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.IPSetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains variables that you can use to override default Suricata settings in your firewall policy.

            :param rule_variables: The IPv4 or IPv6 addresses in CIDR notation to use for the Suricata ``HOME_NET`` variable. If your firewall uses an inspection VPC, you might want to override the ``HOME_NET`` variable with the CIDRs of your home networks. If you don't override ``HOME_NET`` with your own CIDRs, Network Firewall by default uses the CIDR of your inspection VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-policyvariables.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                policy_variables_property = networkfirewall.CfnFirewallPolicy.PolicyVariablesProperty(
                    rule_variables={
                        "rule_variables_key": {
                            "definition": ["definition"]
                        }
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e866a0377e767391b6cb1e114ddc7eed91f1e04c8ab4203b0af3b09a8befd47)
                check_type(argname="argument rule_variables", value=rule_variables, expected_type=type_hints["rule_variables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rule_variables is not None:
                self._values["rule_variables"] = rule_variables

        @builtins.property
        def rule_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.IPSetProperty"]]]]:
            '''The IPv4 or IPv6 addresses in CIDR notation to use for the Suricata ``HOME_NET`` variable.

            If your firewall uses an inspection VPC, you might want to override the ``HOME_NET`` variable with the CIDRs of your home networks. If you don't override ``HOME_NET`` with your own CIDRs, Network Firewall by default uses the CIDR of your inspection VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-policyvariables.html#cfn-networkfirewall-firewallpolicy-policyvariables-rulevariables
            '''
            result = self._values.get("rule_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.IPSetProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyVariablesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.PublishMetricActionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimensions": "dimensions"},
    )
    class PublishMetricActionProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet.

            This setting defines a CloudWatch dimension value to be published.

            :param dimensions: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                publish_metric_action_property = networkfirewall.CfnFirewallPolicy.PublishMetricActionProperty(
                    dimensions=[networkfirewall.CfnFirewallPolicy.DimensionProperty(
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eab9540ab80b4dd980d8dda17b30755d1e15a920591be54fdd8184a0a4e4eb42)
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimensions": dimensions,
            }

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.DimensionProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html#cfn-networkfirewall-firewallpolicy-publishmetricaction-dimensions
            '''
            result = self._values.get("dimensions")
            assert result is not None, "Required property 'dimensions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.DimensionProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublishMetricActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.StatefulEngineOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_order": "ruleOrder",
            "stream_exception_policy": "streamExceptionPolicy",
        },
    )
    class StatefulEngineOptionsProperty:
        def __init__(
            self,
            *,
            rule_order: typing.Optional[builtins.str] = None,
            stream_exception_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration settings for the handling of the stateful rule groups in a firewall policy.

            :param rule_order: Indicates how to manage the order of stateful rule evaluation for the policy. ``DEFAULT_ACTION_ORDER`` is the default behavior. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see `Evaluation order for stateful rules <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html>`_ in the *AWS Network Firewall Developer Guide* .
            :param stream_exception_policy: Configures how Network Firewall processes traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself. - ``DROP`` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. This is the default behavior. - ``CONTINUE`` - Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to ``drop http`` traffic, Network Firewall won't match the traffic for this rule because the service won't have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependent—a TCP-layer rule using a ``flow:stateless`` rule would still match, as would the ``aws:drop_strict`` default action. - ``REJECT`` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall will have context about the new session and will apply rules to the subsequent traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                stateful_engine_options_property = networkfirewall.CfnFirewallPolicy.StatefulEngineOptionsProperty(
                    rule_order="ruleOrder",
                    stream_exception_policy="streamExceptionPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69e95338d370bfb1bbb954499358a8d8914836eb171006f958c9fa4debca2e09)
                check_type(argname="argument rule_order", value=rule_order, expected_type=type_hints["rule_order"])
                check_type(argname="argument stream_exception_policy", value=stream_exception_policy, expected_type=type_hints["stream_exception_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rule_order is not None:
                self._values["rule_order"] = rule_order
            if stream_exception_policy is not None:
                self._values["stream_exception_policy"] = stream_exception_policy

        @builtins.property
        def rule_order(self) -> typing.Optional[builtins.str]:
            '''Indicates how to manage the order of stateful rule evaluation for the policy.

            ``DEFAULT_ACTION_ORDER`` is the default behavior. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see `Evaluation order for stateful rules <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html>`_ in the *AWS Network Firewall Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html#cfn-networkfirewall-firewallpolicy-statefulengineoptions-ruleorder
            '''
            result = self._values.get("rule_order")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_exception_policy(self) -> typing.Optional[builtins.str]:
            '''Configures how Network Firewall processes traffic when a network connection breaks midstream.

            Network connections can break due to disruptions in external networks or within the firewall itself.

            - ``DROP`` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. This is the default behavior.
            - ``CONTINUE`` - Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to ``drop http`` traffic, Network Firewall won't match the traffic for this rule because the service won't have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependent—a TCP-layer rule using a ``flow:stateless`` rule would still match, as would the ``aws:drop_strict`` default action.
            - ``REJECT`` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall will have context about the new session and will apply rules to the subsequent traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html#cfn-networkfirewall-firewallpolicy-statefulengineoptions-streamexceptionpolicy
            '''
            result = self._values.get("stream_exception_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatefulEngineOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.StatefulRuleGroupOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action"},
    )
    class StatefulRuleGroupOverrideProperty:
        def __init__(self, *, action: typing.Optional[builtins.str] = None) -> None:
            '''The setting that allows the policy owner to change the behavior of the rule group within a policy.

            :param action: The action that changes the rule group from ``DROP`` to ``ALERT`` . This only applies to managed rule groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                stateful_rule_group_override_property = networkfirewall.CfnFirewallPolicy.StatefulRuleGroupOverrideProperty(
                    action="action"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__62be7baa7c0ae22655f34e1d3316236c114457fe368caf2a958ba1fd9578c7f4)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The action that changes the rule group from ``DROP`` to ``ALERT`` .

            This only applies to managed rule groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupoverride-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatefulRuleGroupOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.StatefulRuleGroupReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_arn": "resourceArn",
            "override": "override",
            "priority": "priority",
        },
    )
    class StatefulRuleGroupReferenceProperty:
        def __init__(
            self,
            *,
            resource_arn: builtins.str,
            override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallPolicy.StatefulRuleGroupOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            priority: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Identifier for a single stateful rule group, used in a firewall policy to refer to a rule group.

            :param resource_arn: The Amazon Resource Name (ARN) of the stateful rule group.
            :param override: The action that allows the policy owner to override the behavior of the rule group within a policy.
            :param priority: An integer setting that indicates the order in which to run the stateful rule groups in a single ``FirewallPolicy`` . This setting only applies to firewall policies that specify the ``STRICT_ORDER`` rule order in the stateful engine options settings. Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy. You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so there's a wide range in between, for example use 100, 200, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                stateful_rule_group_reference_property = networkfirewall.CfnFirewallPolicy.StatefulRuleGroupReferenceProperty(
                    resource_arn="resourceArn",
                
                    # the properties below are optional
                    override=networkfirewall.CfnFirewallPolicy.StatefulRuleGroupOverrideProperty(
                        action="action"
                    ),
                    priority=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b35f780a3045f4df1ecbf5bb69deb711659429dcfd9f87d388080942e7b17ef8)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument override", value=override, expected_type=type_hints["override"])
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }
            if override is not None:
                self._values["override"] = override
            if priority is not None:
                self._values["priority"] = priority

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the stateful rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def override(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.StatefulRuleGroupOverrideProperty"]]:
            '''The action that allows the policy owner to override the behavior of the rule group within a policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-override
            '''
            result = self._values.get("override")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFirewallPolicy.StatefulRuleGroupOverrideProperty"]], result)

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            '''An integer setting that indicates the order in which to run the stateful rule groups in a single ``FirewallPolicy`` .

            This setting only applies to firewall policies that specify the ``STRICT_ORDER`` rule order in the stateful engine options settings.

            Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.

            You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so there's a wide range in between, for example use 100, 200, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-priority
            '''
            result = self._values.get("priority")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatefulRuleGroupReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicy.StatelessRuleGroupReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"priority": "priority", "resource_arn": "resourceArn"},
    )
    class StatelessRuleGroupReferenceProperty:
        def __init__(
            self,
            *,
            priority: jsii.Number,
            resource_arn: builtins.str,
        ) -> None:
            '''Identifier for a single stateless rule group, used in a firewall policy to refer to the rule group.

            :param priority: An integer setting that indicates the order in which to run the stateless rule groups in a single ``FirewallPolicy`` . Network Firewall applies each stateless rule group to a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.
            :param resource_arn: The Amazon Resource Name (ARN) of the stateless rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                stateless_rule_group_reference_property = networkfirewall.CfnFirewallPolicy.StatelessRuleGroupReferenceProperty(
                    priority=123,
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4abfbbd63f3454ea4b5597e2099b8d101919bc21b3cc73051aad275b321347ca)
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "priority": priority,
                "resource_arn": resource_arn,
            }

        @builtins.property
        def priority(self) -> jsii.Number:
            '''An integer setting that indicates the order in which to run the stateless rule groups in a single ``FirewallPolicy`` .

            Network Firewall applies each stateless rule group to a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the stateless rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatelessRuleGroupReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_policy": "firewallPolicy",
        "firewall_policy_name": "firewallPolicyName",
        "description": "description",
        "tags": "tags",
    },
)
class CfnFirewallPolicyProps:
    def __init__(
        self,
        *,
        firewall_policy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.FirewallPolicyProperty, typing.Dict[builtins.str, typing.Any]]],
        firewall_policy_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFirewallPolicy``.

        :param firewall_policy: The traffic filtering behavior of a firewall policy, defined in a collection of stateless and stateful rule groups and other settings.
        :param firewall_policy_name: The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.
        :param description: A description of the firewall policy.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkfirewall as networkfirewall
            
            cfn_firewall_policy_props = networkfirewall.CfnFirewallPolicyProps(
                firewall_policy=networkfirewall.CfnFirewallPolicy.FirewallPolicyProperty(
                    stateless_default_actions=["statelessDefaultActions"],
                    stateless_fragment_default_actions=["statelessFragmentDefaultActions"],
            
                    # the properties below are optional
                    policy_variables=networkfirewall.CfnFirewallPolicy.PolicyVariablesProperty(
                        rule_variables={
                            "rule_variables_key": {
                                "definition": ["definition"]
                            }
                        }
                    ),
                    stateful_default_actions=["statefulDefaultActions"],
                    stateful_engine_options=networkfirewall.CfnFirewallPolicy.StatefulEngineOptionsProperty(
                        rule_order="ruleOrder",
                        stream_exception_policy="streamExceptionPolicy"
                    ),
                    stateful_rule_group_references=[networkfirewall.CfnFirewallPolicy.StatefulRuleGroupReferenceProperty(
                        resource_arn="resourceArn",
            
                        # the properties below are optional
                        override=networkfirewall.CfnFirewallPolicy.StatefulRuleGroupOverrideProperty(
                            action="action"
                        ),
                        priority=123
                    )],
                    stateless_custom_actions=[networkfirewall.CfnFirewallPolicy.CustomActionProperty(
                        action_definition=networkfirewall.CfnFirewallPolicy.ActionDefinitionProperty(
                            publish_metric_action=networkfirewall.CfnFirewallPolicy.PublishMetricActionProperty(
                                dimensions=[networkfirewall.CfnFirewallPolicy.DimensionProperty(
                                    value="value"
                                )]
                            )
                        ),
                        action_name="actionName"
                    )],
                    stateless_rule_group_references=[networkfirewall.CfnFirewallPolicy.StatelessRuleGroupReferenceProperty(
                        priority=123,
                        resource_arn="resourceArn"
                    )],
                    tls_inspection_configuration_arn="tlsInspectionConfigurationArn"
                ),
                firewall_policy_name="firewallPolicyName",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2c62703239bb4479e4595613edad2d44e170db98c687d725b8c824f819e362)
            check_type(argname="argument firewall_policy", value=firewall_policy, expected_type=type_hints["firewall_policy"])
            check_type(argname="argument firewall_policy_name", value=firewall_policy_name, expected_type=type_hints["firewall_policy_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_policy": firewall_policy,
            "firewall_policy_name": firewall_policy_name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firewall_policy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnFirewallPolicy.FirewallPolicyProperty]:
        '''The traffic filtering behavior of a firewall policy, defined in a collection of stateless and stateful rule groups and other settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy
        '''
        result = self._values.get("firewall_policy")
        assert result is not None, "Required property 'firewall_policy' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFirewallPolicy.FirewallPolicyProperty], result)

    @builtins.property
    def firewall_policy_name(self) -> builtins.str:
        '''The descriptive name of the firewall policy.

        You can't change the name of a firewall policy after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicyname
        '''
        result = self._values.get("firewall_policy_name")
        assert result is not None, "Required property 'firewall_policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the firewall policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnFirewallProps",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_name": "firewallName",
        "firewall_policy_arn": "firewallPolicyArn",
        "subnet_mappings": "subnetMappings",
        "vpc_id": "vpcId",
        "delete_protection": "deleteProtection",
        "description": "description",
        "firewall_policy_change_protection": "firewallPolicyChangeProtection",
        "subnet_change_protection": "subnetChangeProtection",
        "tags": "tags",
    },
)
class CfnFirewallProps:
    def __init__(
        self,
        *,
        firewall_name: builtins.str,
        firewall_policy_arn: builtins.str,
        subnet_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewall.SubnetMappingProperty, typing.Dict[builtins.str, typing.Any]]]]],
        vpc_id: builtins.str,
        delete_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        firewall_policy_change_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        subnet_change_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFirewall``.

        :param firewall_name: The descriptive name of the firewall. You can't change the name of a firewall after you create it.
        :param firewall_policy_arn: The Amazon Resource Name (ARN) of the firewall policy. The relationship of firewall to firewall policy is many to one. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls.
        :param subnet_mappings: The public subnets that Network Firewall is using for the firewall. Each subnet must belong to a different Availability Zone.
        :param vpc_id: The unique identifier of the VPC where the firewall is in use. You can't change the VPC of a firewall after you create the firewall.
        :param delete_protection: A flag indicating whether it is possible to delete the firewall. A setting of ``TRUE`` indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to ``TRUE`` .
        :param description: A description of the firewall.
        :param firewall_policy_change_protection: A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to ``TRUE`` .
        :param subnet_change_protection: A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to ``TRUE`` .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkfirewall as networkfirewall
            
            cfn_firewall_props = networkfirewall.CfnFirewallProps(
                firewall_name="firewallName",
                firewall_policy_arn="firewallPolicyArn",
                subnet_mappings=[networkfirewall.CfnFirewall.SubnetMappingProperty(
                    subnet_id="subnetId",
            
                    # the properties below are optional
                    ip_address_type="ipAddressType"
                )],
                vpc_id="vpcId",
            
                # the properties below are optional
                delete_protection=False,
                description="description",
                firewall_policy_change_protection=False,
                subnet_change_protection=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d4108d5c35b1608da0d36c8bb60f52501d3b0634ca4324342a71c57bc238e99)
            check_type(argname="argument firewall_name", value=firewall_name, expected_type=type_hints["firewall_name"])
            check_type(argname="argument firewall_policy_arn", value=firewall_policy_arn, expected_type=type_hints["firewall_policy_arn"])
            check_type(argname="argument subnet_mappings", value=subnet_mappings, expected_type=type_hints["subnet_mappings"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument delete_protection", value=delete_protection, expected_type=type_hints["delete_protection"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument firewall_policy_change_protection", value=firewall_policy_change_protection, expected_type=type_hints["firewall_policy_change_protection"])
            check_type(argname="argument subnet_change_protection", value=subnet_change_protection, expected_type=type_hints["subnet_change_protection"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_name": firewall_name,
            "firewall_policy_arn": firewall_policy_arn,
            "subnet_mappings": subnet_mappings,
            "vpc_id": vpc_id,
        }
        if delete_protection is not None:
            self._values["delete_protection"] = delete_protection
        if description is not None:
            self._values["description"] = description
        if firewall_policy_change_protection is not None:
            self._values["firewall_policy_change_protection"] = firewall_policy_change_protection
        if subnet_change_protection is not None:
            self._values["subnet_change_protection"] = subnet_change_protection
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firewall_name(self) -> builtins.str:
        '''The descriptive name of the firewall.

        You can't change the name of a firewall after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname
        '''
        result = self._values.get("firewall_name")
        assert result is not None, "Required property 'firewall_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_policy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the firewall policy.

        The relationship of firewall to firewall policy is many to one. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn
        '''
        result = self._values.get("firewall_policy_arn")
        assert result is not None, "Required property 'firewall_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_mappings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFirewall.SubnetMappingProperty]]]:
        '''The public subnets that Network Firewall is using for the firewall.

        Each subnet must belong to a different Availability Zone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings
        '''
        result = self._values.get("subnet_mappings")
        assert result is not None, "Required property 'subnet_mappings' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFirewall.SubnetMappingProperty]]], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The unique identifier of the VPC where the firewall is in use.

        You can't change the VPC of a firewall after you create the firewall.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag indicating whether it is possible to delete the firewall.

        A setting of ``TRUE`` indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to ``TRUE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection
        '''
        result = self._values.get("delete_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the firewall.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firewall_policy_change_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A setting indicating whether the firewall is protected against a change to the firewall policy association.

        Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to ``TRUE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection
        '''
        result = self._values.get("firewall_policy_change_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def subnet_change_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A setting indicating whether the firewall is protected against changes to the subnet associations.

        Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to ``TRUE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection
        '''
        result = self._values.get("subnet_change_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLoggingConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnLoggingConfiguration",
):
    '''Use the ``LoggingConfiguration`` to define the destinations and logging options for an ``Firewall`` .

    You must change the logging configuration by changing one ``LogDestinationConfig`` setting at a time in your ``LogDestinationConfigs`` .

    You can make only one of the following changes to your ``LoggingConfiguration`` resource:

    - Create a new log destination object by adding a single ``LogDestinationConfig`` array element to ``LogDestinationConfigs`` .
    - Delete a log destination object by removing a single ``LogDestinationConfig`` array element from ``LogDestinationConfigs`` .
    - Change the ``LogDestination`` setting in a single ``LogDestinationConfig`` array element.

    You can't change the ``LogDestinationType`` or ``LogType`` in a ``LogDestinationConfig`` . To change these settings, delete the existing ``LogDestinationConfig`` object and create a new one, in two separate modifications.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html
    :cloudformationResource: AWS::NetworkFirewall::LoggingConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkfirewall as networkfirewall
        
        cfn_logging_configuration = networkfirewall.CfnLoggingConfiguration(self, "MyCfnLoggingConfiguration",
            firewall_arn="firewallArn",
            logging_configuration=networkfirewall.CfnLoggingConfiguration.LoggingConfigurationProperty(
                log_destination_configs=[networkfirewall.CfnLoggingConfiguration.LogDestinationConfigProperty(
                    log_destination={
                        "log_destination_key": "logDestination"
                    },
                    log_destination_type="logDestinationType",
                    log_type="logType"
                )]
            ),
        
            # the properties below are optional
            firewall_name="firewallName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        firewall_arn: builtins.str,
        logging_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggingConfiguration.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        firewall_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param firewall_arn: The Amazon Resource Name (ARN) of the ``Firewall`` that the logging configuration is associated with. You can't change the firewall specification after you create the logging configuration.
        :param logging_configuration: Defines how AWS Network Firewall performs logging for a ``Firewall`` .
        :param firewall_name: The name of the firewall that the logging configuration is associated with. You can't change the firewall specification after you create the logging configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71487a7865ce1877156cecd1cb83afa7ffd5f6428fa2611a7537c9ccf8667afe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoggingConfigurationProps(
            firewall_arn=firewall_arn,
            logging_configuration=logging_configuration,
            firewall_name=firewall_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf1d8af41633c95dd577d7d2736c4bc7e5071ece1527fb65bc7392f72a7a43b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b51b1357cb88ac7feaa787c6f1526ec7769461fd859c5b55b6f8e5caf4cf1264)
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
    @jsii.member(jsii_name="firewallArn")
    def firewall_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ``Firewall`` that the logging configuration is associated with.'''
        return typing.cast(builtins.str, jsii.get(self, "firewallArn"))

    @firewall_arn.setter
    def firewall_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d71125ddf5ba2d377facff407ef5a2fcdbd3c618a7499d3633c68130f56adcee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallArn", value)

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.LoggingConfigurationProperty"]:
        '''Defines how AWS Network Firewall performs logging for a ``Firewall`` .'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.LoggingConfigurationProperty"], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.LoggingConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6379a583f20adcddf04ea938455ca9e96ed6e0a2293ffa4b83968515494d8120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="firewallName")
    def firewall_name(self) -> typing.Optional[builtins.str]:
        '''The name of the firewall that the logging configuration is associated with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallName"))

    @firewall_name.setter
    def firewall_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e3640e7313e33945bc2b7c00caa777b47e14239e160ded6a349405aeb0b47da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnLoggingConfiguration.LogDestinationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_destination": "logDestination",
            "log_destination_type": "logDestinationType",
            "log_type": "logType",
        },
    )
    class LogDestinationConfigProperty:
        def __init__(
            self,
            *,
            log_destination: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
            log_destination_type: builtins.str,
            log_type: builtins.str,
        ) -> None:
            '''Defines where AWS Network Firewall sends logs for the firewall for one log type.

            This is used in ``LoggingConfiguration`` . You can send each type of log to an Amazon S3 bucket, a CloudWatch log group, or a Kinesis Data Firehose delivery stream.

            Network Firewall generates logs for stateful rule groups. You can save alert and flow log types. The stateful rules engine records flow logs for all network traffic that it receives. It records alert logs for traffic that matches stateful rules that have the rule action set to ``DROP`` or ``ALERT`` .

            :param log_destination: The named location for the logs, provided in a key:value mapping that is specific to the chosen destination type. - For an Amazon S3 bucket, provide the name of the bucket, with key ``bucketName`` , and optionally provide a prefix, with key ``prefix`` . The following example specifies an Amazon S3 bucket named ``DOC-EXAMPLE-BUCKET`` and the prefix ``alerts`` : ``"LogDestination": { "bucketName": "DOC-EXAMPLE-BUCKET", "prefix": "alerts" }`` - For a CloudWatch log group, provide the name of the CloudWatch log group, with key ``logGroup`` . The following example specifies a log group named ``alert-log-group`` : ``"LogDestination": { "logGroup": "alert-log-group" }`` - For a Firehose delivery stream, provide the name of the delivery stream, with key ``deliveryStream`` . The following example specifies a delivery stream named ``alert-delivery-stream`` : ``"LogDestination": { "deliveryStream": "alert-delivery-stream" }``
            :param log_destination_type: The type of storage destination to send these logs to. You can send logs to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.
            :param log_type: The type of log to send. Alert logs report traffic that matches a stateful rule with an action setting that sends an alert log message. Flow logs are standard network traffic flow logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                log_destination_config_property = networkfirewall.CfnLoggingConfiguration.LogDestinationConfigProperty(
                    log_destination={
                        "log_destination_key": "logDestination"
                    },
                    log_destination_type="logDestinationType",
                    log_type="logType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71b2e62cece09027ed51c224134098d51d2c868274bd4da88e455b472e9c005d)
                check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
                check_type(argname="argument log_destination_type", value=log_destination_type, expected_type=type_hints["log_destination_type"])
                check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_destination": log_destination,
                "log_destination_type": log_destination_type,
                "log_type": log_type,
            }

        @builtins.property
        def log_destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
            '''The named location for the logs, provided in a key:value mapping that is specific to the chosen destination type.

            - For an Amazon S3 bucket, provide the name of the bucket, with key ``bucketName`` , and optionally provide a prefix, with key ``prefix`` . The following example specifies an Amazon S3 bucket named ``DOC-EXAMPLE-BUCKET`` and the prefix ``alerts`` :

            ``"LogDestination": { "bucketName": "DOC-EXAMPLE-BUCKET", "prefix": "alerts" }``

            - For a CloudWatch log group, provide the name of the CloudWatch log group, with key ``logGroup`` . The following example specifies a log group named ``alert-log-group`` :

            ``"LogDestination": { "logGroup": "alert-log-group" }``

            - For a Firehose delivery stream, provide the name of the delivery stream, with key ``deliveryStream`` . The following example specifies a delivery stream named ``alert-delivery-stream`` :

            ``"LogDestination": { "deliveryStream": "alert-delivery-stream" }``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestination
            '''
            result = self._values.get("log_destination")
            assert result is not None, "Required property 'log_destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], result)

        @builtins.property
        def log_destination_type(self) -> builtins.str:
            '''The type of storage destination to send these logs to.

            You can send logs to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestinationtype
            '''
            result = self._values.get("log_destination_type")
            assert result is not None, "Required property 'log_destination_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_type(self) -> builtins.str:
            '''The type of log to send.

            Alert logs report traffic that matches a stateful rule with an action setting that sends an alert log message. Flow logs are standard network traffic flow logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logtype
            '''
            result = self._values.get("log_type")
            assert result is not None, "Required property 'log_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDestinationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnLoggingConfiguration.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_destination_configs": "logDestinationConfigs"},
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            log_destination_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggingConfiguration.LogDestinationConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Defines how AWS Network Firewall performs logging for a ``Firewall`` .

            :param log_destination_configs: Defines the logging destinations for the logs for a firewall. Network Firewall generates logs for stateful rule groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                logging_configuration_property = networkfirewall.CfnLoggingConfiguration.LoggingConfigurationProperty(
                    log_destination_configs=[networkfirewall.CfnLoggingConfiguration.LogDestinationConfigProperty(
                        log_destination={
                            "log_destination_key": "logDestination"
                        },
                        log_destination_type="logDestinationType",
                        log_type="logType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7694cf2d5082b8064a259b791a222ad012a1f7bcab308d321c9d4c780c634c13)
                check_type(argname="argument log_destination_configs", value=log_destination_configs, expected_type=type_hints["log_destination_configs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_destination_configs": log_destination_configs,
            }

        @builtins.property
        def log_destination_configs(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.LogDestinationConfigProperty"]]]:
            '''Defines the logging destinations for the logs for a firewall.

            Network Firewall generates logs for stateful rule groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration-logdestinationconfigs
            '''
            result = self._values.get("log_destination_configs")
            assert result is not None, "Required property 'log_destination_configs' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.LogDestinationConfigProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnLoggingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_arn": "firewallArn",
        "logging_configuration": "loggingConfiguration",
        "firewall_name": "firewallName",
    },
)
class CfnLoggingConfigurationProps:
    def __init__(
        self,
        *,
        firewall_arn: builtins.str,
        logging_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        firewall_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLoggingConfiguration``.

        :param firewall_arn: The Amazon Resource Name (ARN) of the ``Firewall`` that the logging configuration is associated with. You can't change the firewall specification after you create the logging configuration.
        :param logging_configuration: Defines how AWS Network Firewall performs logging for a ``Firewall`` .
        :param firewall_name: The name of the firewall that the logging configuration is associated with. You can't change the firewall specification after you create the logging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkfirewall as networkfirewall
            
            cfn_logging_configuration_props = networkfirewall.CfnLoggingConfigurationProps(
                firewall_arn="firewallArn",
                logging_configuration=networkfirewall.CfnLoggingConfiguration.LoggingConfigurationProperty(
                    log_destination_configs=[networkfirewall.CfnLoggingConfiguration.LogDestinationConfigProperty(
                        log_destination={
                            "log_destination_key": "logDestination"
                        },
                        log_destination_type="logDestinationType",
                        log_type="logType"
                    )]
                ),
            
                # the properties below are optional
                firewall_name="firewallName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dab36772798ea19c1d2e2f1e86d2099a88806994c157c7bd4e0d62178ab9369)
            check_type(argname="argument firewall_arn", value=firewall_arn, expected_type=type_hints["firewall_arn"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument firewall_name", value=firewall_name, expected_type=type_hints["firewall_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_arn": firewall_arn,
            "logging_configuration": logging_configuration,
        }
        if firewall_name is not None:
            self._values["firewall_name"] = firewall_name

    @builtins.property
    def firewall_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ``Firewall`` that the logging configuration is associated with.

        You can't change the firewall specification after you create the logging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallarn
        '''
        result = self._values.get("firewall_arn")
        assert result is not None, "Required property 'firewall_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLoggingConfiguration.LoggingConfigurationProperty]:
        '''Defines how AWS Network Firewall performs logging for a ``Firewall`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        assert result is not None, "Required property 'logging_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLoggingConfiguration.LoggingConfigurationProperty], result)

    @builtins.property
    def firewall_name(self) -> typing.Optional[builtins.str]:
        '''The name of the firewall that the logging configuration is associated with.

        You can't change the firewall specification after you create the logging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallname
        '''
        result = self._values.get("firewall_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoggingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRuleGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup",
):
    '''Use the ``RuleGroup`` to define a reusable collection of stateless or stateful network traffic filtering rules.

    You use rule groups in an ``FirewallPolicy`` to specify the filtering behavior of an ``Firewall`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html
    :cloudformationResource: AWS::NetworkFirewall::RuleGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkfirewall as networkfirewall
        
        cfn_rule_group = networkfirewall.CfnRuleGroup(self, "MyCfnRuleGroup",
            capacity=123,
            rule_group_name="ruleGroupName",
            type="type",
        
            # the properties below are optional
            description="description",
            rule_group=networkfirewall.CfnRuleGroup.RuleGroupProperty(
                rules_source=networkfirewall.CfnRuleGroup.RulesSourceProperty(
                    rules_source_list=networkfirewall.CfnRuleGroup.RulesSourceListProperty(
                        generated_rules_type="generatedRulesType",
                        targets=["targets"],
                        target_types=["targetTypes"]
                    ),
                    rules_string="rulesString",
                    stateful_rules=[networkfirewall.CfnRuleGroup.StatefulRuleProperty(
                        action="action",
                        header=networkfirewall.CfnRuleGroup.HeaderProperty(
                            destination="destination",
                            destination_port="destinationPort",
                            direction="direction",
                            protocol="protocol",
                            source="source",
                            source_port="sourcePort"
                        ),
                        rule_options=[networkfirewall.CfnRuleGroup.RuleOptionProperty(
                            keyword="keyword",
        
                            # the properties below are optional
                            settings=["settings"]
                        )]
                    )],
                    stateless_rules_and_custom_actions=networkfirewall.CfnRuleGroup.StatelessRulesAndCustomActionsProperty(
                        stateless_rules=[networkfirewall.CfnRuleGroup.StatelessRuleProperty(
                            priority=123,
                            rule_definition=networkfirewall.CfnRuleGroup.RuleDefinitionProperty(
                                actions=["actions"],
                                match_attributes=networkfirewall.CfnRuleGroup.MatchAttributesProperty(
                                    destination_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                        from_port=123,
                                        to_port=123
                                    )],
                                    destinations=[networkfirewall.CfnRuleGroup.AddressProperty(
                                        address_definition="addressDefinition"
                                    )],
                                    protocols=[123],
                                    source_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                        from_port=123,
                                        to_port=123
                                    )],
                                    sources=[networkfirewall.CfnRuleGroup.AddressProperty(
                                        address_definition="addressDefinition"
                                    )],
                                    tcp_flags=[networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                                        flags=["flags"],
        
                                        # the properties below are optional
                                        masks=["masks"]
                                    )]
                                )
                            )
                        )],
        
                        # the properties below are optional
                        custom_actions=[networkfirewall.CfnRuleGroup.CustomActionProperty(
                            action_definition=networkfirewall.CfnRuleGroup.ActionDefinitionProperty(
                                publish_metric_action=networkfirewall.CfnRuleGroup.PublishMetricActionProperty(
                                    dimensions=[networkfirewall.CfnRuleGroup.DimensionProperty(
                                        value="value"
                                    )]
                                )
                            ),
                            action_name="actionName"
                        )]
                    )
                ),
        
                # the properties below are optional
                reference_sets=networkfirewall.CfnRuleGroup.ReferenceSetsProperty(
                    ip_set_references={
                        "ip_set_references_key": {
                            "reference_arn": "referenceArn"
                        }
                    }
                ),
                rule_variables=networkfirewall.CfnRuleGroup.RuleVariablesProperty(
                    ip_sets={
                        "ip_sets_key": {
                            "definition": ["definition"]
                        }
                    },
                    port_sets={
                        "port_sets_key": networkfirewall.CfnRuleGroup.PortSetProperty(
                            definition=["definition"]
                        )
                    }
                ),
                stateful_rule_options=networkfirewall.CfnRuleGroup.StatefulRuleOptionsProperty(
                    rule_order="ruleOrder"
                )
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
        capacity: jsii.Number,
        rule_group_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rule_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.RuleGroupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param capacity: The maximum operating resources that this rule group can use. You can't change a rule group's capacity setting after you create the rule group. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group.
        :param rule_group_name: The descriptive name of the rule group. You can't change the name of a rule group after you create it.
        :param type: Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.
        :param description: A description of the rule group.
        :param rule_group: An object that defines the rule group rules.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f1d19cebb2e7dfe2bb3a674253e22bfdb540bd48dc9cd243370420d8cec9b9e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuleGroupProps(
            capacity=capacity,
            rule_group_name=rule_group_name,
            type=type,
            description=description,
            rule_group=rule_group,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8ef477504489cc901fa58c5454b1728231c047d069191745b232cb839f0b97)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af5174ab9f3bed2fb8464156fa8d27c8cbbb570726e4667c2ed7634ad777c961)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleGroupArn")
    def attr_rule_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ``RuleGroup`` .

        :cloudformationAttribute: RuleGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleGroupId")
    def attr_rule_group_id(self) -> builtins.str:
        '''The unique ID of the ``RuleGroup`` resource.

        :cloudformationAttribute: RuleGroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleGroupId"))

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
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        '''The maximum operating resources that this rule group can use.'''
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51c7651794925713a49400586d47fdec281f3586c00b18d62055515fd2ef2791)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="ruleGroupName")
    def rule_group_name(self) -> builtins.str:
        '''The descriptive name of the rule group.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleGroupName"))

    @rule_group_name.setter
    def rule_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23a7df76066fa7162c289f359c412bcb9765e3d5b573e0d06d7daf300d391ff3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Indicates whether the rule group is stateless or stateful.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87ac4c425ad11cc87f637d21e3373819fe72741deca8ec3a39ab57b97c38a2e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the rule group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0c85f5fc86d4cd20434a5458984123db8b76ff5d649d26af8be38c56af6a7b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="ruleGroup")
    def rule_group(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleGroupProperty"]]:
        '''An object that defines the rule group rules.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleGroupProperty"]], jsii.get(self, "ruleGroup"))

    @rule_group.setter
    def rule_group(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleGroupProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ed6ac96ae6360b92bfdf6614d9832ba1cad5080dce3a3257a75537c93626bb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleGroup", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5969fe74fc1a24641d71678e96d3133e152f5f87c43e5f7d72af22aa055d7db5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.ActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"publish_metric_action": "publishMetricAction"},
    )
    class ActionDefinitionProperty:
        def __init__(
            self,
            *,
            publish_metric_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.PublishMetricActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A custom action to use in stateless rule actions settings.

            :param publish_metric_action: Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet. This setting defines a CloudWatch dimension value to be published. You can pair this custom action with any of the standard stateless rule actions. For example, you could pair this in a rule action with the standard action that forwards the packet for stateful inspection. Then, when a packet matches the rule, Network Firewall publishes metrics for the packet and forwards it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                action_definition_property = networkfirewall.CfnRuleGroup.ActionDefinitionProperty(
                    publish_metric_action=networkfirewall.CfnRuleGroup.PublishMetricActionProperty(
                        dimensions=[networkfirewall.CfnRuleGroup.DimensionProperty(
                            value="value"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ffeb7b0f0ffdb417d3ac37fe775fea2d6c40814070d270c03323517593b547b9)
                check_type(argname="argument publish_metric_action", value=publish_metric_action, expected_type=type_hints["publish_metric_action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if publish_metric_action is not None:
                self._values["publish_metric_action"] = publish_metric_action

        @builtins.property
        def publish_metric_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.PublishMetricActionProperty"]]:
            '''Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet.

            This setting defines a CloudWatch dimension value to be published.

            You can pair this custom action with any of the standard stateless rule actions. For example, you could pair this in a rule action with the standard action that forwards the packet for stateful inspection. Then, when a packet matches the rule, Network Firewall publishes metrics for the packet and forwards it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html#cfn-networkfirewall-rulegroup-actiondefinition-publishmetricaction
            '''
            result = self._values.get("publish_metric_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.PublishMetricActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.AddressProperty",
        jsii_struct_bases=[],
        name_mapping={"address_definition": "addressDefinition"},
    )
    class AddressProperty:
        def __init__(self, *, address_definition: builtins.str) -> None:
            '''A single IP address specification.

            This is used in the ``RuleGroup.MatchAttributes`` source and destination specifications.

            :param address_definition: Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6. Examples: - To configure Network Firewall to inspect for the IP address 192.0.2.44, specify ``192.0.2.44/32`` . - To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` . - To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` . - To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` . For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                address_property = networkfirewall.CfnRuleGroup.AddressProperty(
                    address_definition="addressDefinition"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d6067c4ca12beed4ffa424b8e13cd23b4810ac4eca1ff16680ad9a71e7289c5)
                check_type(argname="argument address_definition", value=address_definition, expected_type=type_hints["address_definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address_definition": address_definition,
            }

        @builtins.property
        def address_definition(self) -> builtins.str:
            '''Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation.

            Network Firewall supports all address ranges for IPv4 and IPv6.

            Examples:

            - To configure Network Firewall to inspect for the IP address 192.0.2.44, specify ``192.0.2.44/32`` .
            - To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .
            - To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .
            - To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .

            For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html#cfn-networkfirewall-rulegroup-address-addressdefinition
            '''
            result = self._values.get("address_definition")
            assert result is not None, "Required property 'address_definition' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.CustomActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_definition": "actionDefinition",
            "action_name": "actionName",
        },
    )
    class CustomActionProperty:
        def __init__(
            self,
            *,
            action_definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.ActionDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
            action_name: builtins.str,
        ) -> None:
            '''An optional, non-standard action to use for stateless packet handling.

            You can define this in addition to the standard action that you must specify.

            You define and name the custom actions that you want to be able to use, and then you reference them by name in your actions settings.

            You can use custom actions in the following places:

            - In an ``RuleGroup.StatelessRulesAndCustomActions`` . The custom actions are available for use by name inside the ``StatelessRulesAndCustomActions`` where you define them. You can use them for your stateless rule actions to specify what to do with a packet that matches the rule's match attributes.
            - In an ``FirewallPolicy`` specification, in ``StatelessCustomActions`` . The custom actions are available for use inside the policy where you define them. You can use them for the policy's default stateless actions settings to specify what to do with packets that don't match any of the policy's stateless rules.

            :param action_definition: The custom action associated with the action name.
            :param action_name: The descriptive name of the custom action. You can't change the name of a custom action after you create it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                custom_action_property = networkfirewall.CfnRuleGroup.CustomActionProperty(
                    action_definition=networkfirewall.CfnRuleGroup.ActionDefinitionProperty(
                        publish_metric_action=networkfirewall.CfnRuleGroup.PublishMetricActionProperty(
                            dimensions=[networkfirewall.CfnRuleGroup.DimensionProperty(
                                value="value"
                            )]
                        )
                    ),
                    action_name="actionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__776dc4a2267643558107c479367987cde061715c1a5e677dc3d8ad57e6bb07f7)
                check_type(argname="argument action_definition", value=action_definition, expected_type=type_hints["action_definition"])
                check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action_definition": action_definition,
                "action_name": action_name,
            }

        @builtins.property
        def action_definition(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.ActionDefinitionProperty"]:
            '''The custom action associated with the action name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actiondefinition
            '''
            result = self._values.get("action_definition")
            assert result is not None, "Required property 'action_definition' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.ActionDefinitionProperty"], result)

        @builtins.property
        def action_name(self) -> builtins.str:
            '''The descriptive name of the custom action.

            You can't change the name of a custom action after you create it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actionname
            '''
            result = self._values.get("action_name")
            assert result is not None, "Required property 'action_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''The value to use in an Amazon CloudWatch custom metric dimension.

            This is used in the ``PublishMetrics`` custom action. A CloudWatch custom metric dimension is a name/value pair that's part of the identity of a metric.

            AWS Network Firewall sets the dimension name to ``CustomAction`` and you provide the dimension value.

            For more information about CloudWatch custom metric dimensions, see `Publishing Custom Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#usingDimensions>`_ in the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>`_ .

            :param value: The value to use in the custom metric dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                dimension_property = networkfirewall.CfnRuleGroup.DimensionProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__84c1411257e0aebed042d1b8352d41d7cf5b9215102a041f342d81c1abe064f3)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''The value to use in the custom metric dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html#cfn-networkfirewall-rulegroup-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.HeaderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "destination_port": "destinationPort",
            "direction": "direction",
            "protocol": "protocol",
            "source": "source",
            "source_port": "sourcePort",
        },
    )
    class HeaderProperty:
        def __init__(
            self,
            *,
            destination: builtins.str,
            destination_port: builtins.str,
            direction: builtins.str,
            protocol: builtins.str,
            source: builtins.str,
            source_port: builtins.str,
        ) -> None:
            '''The 5-tuple criteria for AWS Network Firewall to use to inspect packet headers in stateful traffic flow inspection.

            Traffic flows that match the criteria are a match for the corresponding stateful rule.

            :param destination: The destination IP address or address range to inspect for, in CIDR notation. To match with any address, specify ``ANY`` . Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6. Examples: - To configure Network Firewall to inspect for the IP address 192.0.2.44, specify ``192.0.2.44/32`` . - To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` . - To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` . - To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` . For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .
            :param destination_port: The destination port to inspect for. You can specify an individual port, for example ``1994`` and you can specify a port range, for example ``1990:1994`` . To match with any port, specify ``ANY`` .
            :param direction: The direction of traffic flow to inspect. If set to ``ANY`` , the inspection matches bidirectional traffic, both from the source to the destination and from the destination to the source. If set to ``FORWARD`` , the inspection only matches traffic going from the source to the destination.
            :param protocol: The protocol to inspect for. To specify all, you can use ``IP`` , because all traffic on AWS and on the internet is IP.
            :param source: The source IP address or address range to inspect for, in CIDR notation. To match with any address, specify ``ANY`` . Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6. Examples: - To configure Network Firewall to inspect for the IP address 192.0.2.44, specify ``192.0.2.44/32`` . - To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` . - To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` . - To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` . For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .
            :param source_port: The source port to inspect for. You can specify an individual port, for example ``1994`` and you can specify a port range, for example ``1990:1994`` . To match with any port, specify ``ANY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                header_property = networkfirewall.CfnRuleGroup.HeaderProperty(
                    destination="destination",
                    destination_port="destinationPort",
                    direction="direction",
                    protocol="protocol",
                    source="source",
                    source_port="sourcePort"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b333909d939962666b3db75451a84fc0fc672a45693aca0c6339237e2a577318)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument destination_port", value=destination_port, expected_type=type_hints["destination_port"])
                check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument source_port", value=source_port, expected_type=type_hints["source_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "destination_port": destination_port,
                "direction": direction,
                "protocol": protocol,
                "source": source,
                "source_port": source_port,
            }

        @builtins.property
        def destination(self) -> builtins.str:
            '''The destination IP address or address range to inspect for, in CIDR notation.

            To match with any address, specify ``ANY`` .

            Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.

            Examples:

            - To configure Network Firewall to inspect for the IP address 192.0.2.44, specify ``192.0.2.44/32`` .
            - To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .
            - To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .
            - To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .

            For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_port(self) -> builtins.str:
            '''The destination port to inspect for.

            You can specify an individual port, for example ``1994`` and you can specify a port range, for example ``1990:1994`` . To match with any port, specify ``ANY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destinationport
            '''
            result = self._values.get("destination_port")
            assert result is not None, "Required property 'destination_port' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def direction(self) -> builtins.str:
            '''The direction of traffic flow to inspect.

            If set to ``ANY`` , the inspection matches bidirectional traffic, both from the source to the destination and from the destination to the source. If set to ``FORWARD`` , the inspection only matches traffic going from the source to the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-direction
            '''
            result = self._values.get("direction")
            assert result is not None, "Required property 'direction' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The protocol to inspect for.

            To specify all, you can use ``IP`` , because all traffic on AWS and on the internet is IP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''The source IP address or address range to inspect for, in CIDR notation.

            To match with any address, specify ``ANY`` .

            Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.

            Examples:

            - To configure Network Firewall to inspect for the IP address 192.0.2.44, specify ``192.0.2.44/32`` .
            - To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .
            - To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .
            - To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .

            For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_port(self) -> builtins.str:
            '''The source port to inspect for.

            You can specify an individual port, for example ``1994`` and you can specify a port range, for example ``1990:1994`` . To match with any port, specify ``ANY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-sourceport
            '''
            result = self._values.get("source_port")
            assert result is not None, "Required property 'source_port' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.IPSetProperty",
        jsii_struct_bases=[],
        name_mapping={"definition": "definition"},
    )
    class IPSetProperty:
        def __init__(
            self,
            *,
            definition: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A list of IP addresses and address ranges, in CIDR notation.

            This is part of a ``RuleGroup.RuleVariables`` .

            :param definition: The list of IP addresses and address ranges, in CIDR notation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                i_pSet_property = {
                    "definition": ["definition"]
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ca53e469af4e88c4294a2b49d50c102b6e9e059bfbfa928cfefb0c899aeca0b6)
                check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if definition is not None:
                self._values["definition"] = definition

        @builtins.property
        def definition(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of IP addresses and address ranges, in CIDR notation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html#cfn-networkfirewall-rulegroup-ipset-definition
            '''
            result = self._values.get("definition")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IPSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.IPSetReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"reference_arn": "referenceArn"},
    )
    class IPSetReferenceProperty:
        def __init__(
            self,
            *,
            reference_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configures one or more ``IPSetReferences`` for a Suricata-compatible rule group.

            An IP set reference is a rule variable that references a resource that you create and manage in another AWS service, such as an Amazon VPC prefix list. Network Firewall IP set references enable you to dynamically update the contents of your rules. When you create, update, or delete the IP set you are referencing in your rule, Network Firewall automatically updates the rule's content with the changes. For more information about IP set references in Network Firewall , see `Using IP set references <https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references.html>`_ in the *Network Firewall Developer Guide* .

            :param reference_arn: The Amazon Resource Name (ARN) of the resource to include in the ``RuleGroup.IPSetReference`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipsetreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                i_pSet_reference_property = {
                    "reference_arn": "referenceArn"
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4c62ac9d27c6484f4a2b9da61680388d72bf1968a69f8864fca9a5dc2c1d420)
                check_type(argname="argument reference_arn", value=reference_arn, expected_type=type_hints["reference_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if reference_arn is not None:
                self._values["reference_arn"] = reference_arn

        @builtins.property
        def reference_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the resource to include in the ``RuleGroup.IPSetReference`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipsetreference.html#cfn-networkfirewall-rulegroup-ipsetreference-referencearn
            '''
            result = self._values.get("reference_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IPSetReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.MatchAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_ports": "destinationPorts",
            "destinations": "destinations",
            "protocols": "protocols",
            "source_ports": "sourcePorts",
            "sources": "sources",
            "tcp_flags": "tcpFlags",
        },
    )
    class MatchAttributesProperty:
        def __init__(
            self,
            *,
            destination_ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.PortRangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.AddressProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            protocols: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            source_ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.PortRangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.AddressProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tcp_flags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.TCPFlagFieldProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Criteria for Network Firewall to use to inspect an individual packet in stateless rule inspection.

            Each match attributes set can include one or more items such as IP address, CIDR range, port number, protocol, and TCP flags.

            :param destination_ports: The destination ports to inspect for. If not specified, this matches with any destination port. This setting is only used for protocols 6 (TCP) and 17 (UDP). You can specify individual ports, for example ``1994`` and you can specify port ranges, for example ``1990:1994`` .
            :param destinations: The destination IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any destination address.
            :param protocols: The protocols to inspect for, specified using each protocol's assigned internet protocol number (IANA). If not specified, this matches with any protocol.
            :param source_ports: The source ports to inspect for. If not specified, this matches with any source port. This setting is only used for protocols 6 (TCP) and 17 (UDP). You can specify individual ports, for example ``1994`` and you can specify port ranges, for example ``1990:1994`` .
            :param sources: The source IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any source address.
            :param tcp_flags: The TCP flags and masks to inspect for. If not specified, this matches with any settings. This setting is only used for protocol 6 (TCP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                match_attributes_property = networkfirewall.CfnRuleGroup.MatchAttributesProperty(
                    destination_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                        from_port=123,
                        to_port=123
                    )],
                    destinations=[networkfirewall.CfnRuleGroup.AddressProperty(
                        address_definition="addressDefinition"
                    )],
                    protocols=[123],
                    source_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                        from_port=123,
                        to_port=123
                    )],
                    sources=[networkfirewall.CfnRuleGroup.AddressProperty(
                        address_definition="addressDefinition"
                    )],
                    tcp_flags=[networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                        flags=["flags"],
                
                        # the properties below are optional
                        masks=["masks"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__90ce1a312793001f5c059c69ea601ba7bc963a51d06ab080c64c4cb1eae7671a)
                check_type(argname="argument destination_ports", value=destination_ports, expected_type=type_hints["destination_ports"])
                check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
                check_type(argname="argument protocols", value=protocols, expected_type=type_hints["protocols"])
                check_type(argname="argument source_ports", value=source_ports, expected_type=type_hints["source_ports"])
                check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
                check_type(argname="argument tcp_flags", value=tcp_flags, expected_type=type_hints["tcp_flags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_ports is not None:
                self._values["destination_ports"] = destination_ports
            if destinations is not None:
                self._values["destinations"] = destinations
            if protocols is not None:
                self._values["protocols"] = protocols
            if source_ports is not None:
                self._values["source_ports"] = source_ports
            if sources is not None:
                self._values["sources"] = sources
            if tcp_flags is not None:
                self._values["tcp_flags"] = tcp_flags

        @builtins.property
        def destination_ports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.PortRangeProperty"]]]]:
            '''The destination ports to inspect for.

            If not specified, this matches with any destination port. This setting is only used for protocols 6 (TCP) and 17 (UDP).

            You can specify individual ports, for example ``1994`` and you can specify port ranges, for example ``1990:1994`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinationports
            '''
            result = self._values.get("destination_ports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.PortRangeProperty"]]]], result)

        @builtins.property
        def destinations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.AddressProperty"]]]]:
            '''The destination IP addresses and address ranges to inspect for, in CIDR notation.

            If not specified, this matches with any destination address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinations
            '''
            result = self._values.get("destinations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.AddressProperty"]]]], result)

        @builtins.property
        def protocols(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''The protocols to inspect for, specified using each protocol's assigned internet protocol number (IANA).

            If not specified, this matches with any protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-protocols
            '''
            result = self._values.get("protocols")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def source_ports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.PortRangeProperty"]]]]:
            '''The source ports to inspect for.

            If not specified, this matches with any source port. This setting is only used for protocols 6 (TCP) and 17 (UDP).

            You can specify individual ports, for example ``1994`` and you can specify port ranges, for example ``1990:1994`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sourceports
            '''
            result = self._values.get("source_ports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.PortRangeProperty"]]]], result)

        @builtins.property
        def sources(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.AddressProperty"]]]]:
            '''The source IP addresses and address ranges to inspect for, in CIDR notation.

            If not specified, this matches with any source address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sources
            '''
            result = self._values.get("sources")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.AddressProperty"]]]], result)

        @builtins.property
        def tcp_flags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.TCPFlagFieldProperty"]]]]:
            '''The TCP flags and masks to inspect for.

            If not specified, this matches with any settings. This setting is only used for protocol 6 (TCP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-tcpflags
            '''
            result = self._values.get("tcp_flags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.TCPFlagFieldProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MatchAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.PortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"from_port": "fromPort", "to_port": "toPort"},
    )
    class PortRangeProperty:
        def __init__(self, *, from_port: jsii.Number, to_port: jsii.Number) -> None:
            '''A single port range specification.

            This is used for source and destination port ranges in the stateless ``RuleGroup.MatchAttributes`` .

            :param from_port: The lower limit of the port range. This must be less than or equal to the ``ToPort`` specification.
            :param to_port: The upper limit of the port range. This must be greater than or equal to the ``FromPort`` specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                port_range_property = networkfirewall.CfnRuleGroup.PortRangeProperty(
                    from_port=123,
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ebd1af803bf4604f5fe65a635655413d3719cd3b737baab39db33daf95c1ac6b)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''The lower limit of the port range.

            This must be less than or equal to the ``ToPort`` specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''The upper limit of the port range.

            This must be greater than or equal to the ``FromPort`` specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.PortSetProperty",
        jsii_struct_bases=[],
        name_mapping={"definition": "definition"},
    )
    class PortSetProperty:
        def __init__(
            self,
            *,
            definition: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A set of port ranges for use in the rules in a rule group.

            :param definition: The set of port ranges.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                port_set_property = networkfirewall.CfnRuleGroup.PortSetProperty(
                    definition=["definition"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d18f51e9866b56513a07e5af9f75eea271b0da41a1c90b0f0eb235ccaeaf6fd8)
                check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if definition is not None:
                self._values["definition"] = definition

        @builtins.property
        def definition(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The set of port ranges.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html#cfn-networkfirewall-rulegroup-portset-definition
            '''
            result = self._values.get("definition")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.PublishMetricActionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimensions": "dimensions"},
    )
    class PublishMetricActionProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet.

            This setting defines a CloudWatch dimension value to be published.

            :param dimensions: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                publish_metric_action_property = networkfirewall.CfnRuleGroup.PublishMetricActionProperty(
                    dimensions=[networkfirewall.CfnRuleGroup.DimensionProperty(
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41a6f7b234552866dbb2f70b78c6c9311fef5d507c07747593b0b90e4a163d46)
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimensions": dimensions,
            }

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.DimensionProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html#cfn-networkfirewall-rulegroup-publishmetricaction-dimensions
            '''
            result = self._values.get("dimensions")
            assert result is not None, "Required property 'dimensions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.DimensionProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublishMetricActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.ReferenceSetsProperty",
        jsii_struct_bases=[],
        name_mapping={"ip_set_references": "ipSetReferences"},
    )
    class ReferenceSetsProperty:
        def __init__(
            self,
            *,
            ip_set_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.IPSetReferenceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configures the ``ReferenceSets`` for a stateful rule group.

            For more information, see the `Using IP set references in Suricata compatible rule groups <https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references.html>`_ in the *Network Firewall User Guide* .

            :param ip_set_references: The IP set references to use in the stateful rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-referencesets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                reference_sets_property = networkfirewall.CfnRuleGroup.ReferenceSetsProperty(
                    ip_set_references={
                        "ip_set_references_key": {
                            "reference_arn": "referenceArn"
                        }
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3955e12e3465fd3060b82c41bb430af9d8272b881b8347a0df73c8b0293b8b00)
                check_type(argname="argument ip_set_references", value=ip_set_references, expected_type=type_hints["ip_set_references"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ip_set_references is not None:
                self._values["ip_set_references"] = ip_set_references

        @builtins.property
        def ip_set_references(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.IPSetReferenceProperty"]]]]:
            '''The IP set references to use in the stateful rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-referencesets.html#cfn-networkfirewall-rulegroup-referencesets-ipsetreferences
            '''
            result = self._values.get("ip_set_references")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.IPSetReferenceProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceSetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.RuleDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "match_attributes": "matchAttributes"},
    )
    class RuleDefinitionProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            match_attributes: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.MatchAttributesProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The inspection criteria and action for a single stateless rule.

            AWS Network Firewall inspects each packet for the specified matching criteria. When a packet matches the criteria, Network Firewall performs the rule's actions on the packet.

            :param actions: The actions to take on a packet that matches one of the stateless rule definition's match attributes. You must specify a standard action and you can add custom actions. .. epigraph:: Network Firewall only forwards a packet for stateful rule inspection if you specify ``aws:forward_to_sfe`` for a rule that the packet matches, or if the packet doesn't match any stateless rule and you specify ``aws:forward_to_sfe`` for the ``StatelessDefaultActions`` setting for the ``FirewallPolicy`` . For every rule, you must specify exactly one of the following standard actions. - *aws:pass* - Discontinues all inspection of the packet and permits it to go to its intended destination. - *aws:drop* - Discontinues all inspection of the packet and blocks it from going to its intended destination. - *aws:forward_to_sfe* - Discontinues stateless inspection of the packet and forwards it to the stateful rule engine for inspection. Additionally, you can specify a custom action. To do this, you define a custom action by name and type, then provide the name you've assigned to the action in this ``Actions`` setting. To provide more than one action in this setting, separate the settings with a comma. For example, if you have a publish metrics custom action that you've named ``MyMetricsAction`` , then you could specify the standard action ``aws:pass`` combined with the custom action using ``[“aws:pass”, “MyMetricsAction”]`` .
            :param match_attributes: Criteria for Network Firewall to use to inspect an individual packet in stateless rule inspection. Each match attributes set can include one or more items such as IP address, CIDR range, port number, protocol, and TCP flags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                rule_definition_property = networkfirewall.CfnRuleGroup.RuleDefinitionProperty(
                    actions=["actions"],
                    match_attributes=networkfirewall.CfnRuleGroup.MatchAttributesProperty(
                        destination_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                            from_port=123,
                            to_port=123
                        )],
                        destinations=[networkfirewall.CfnRuleGroup.AddressProperty(
                            address_definition="addressDefinition"
                        )],
                        protocols=[123],
                        source_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                            from_port=123,
                            to_port=123
                        )],
                        sources=[networkfirewall.CfnRuleGroup.AddressProperty(
                            address_definition="addressDefinition"
                        )],
                        tcp_flags=[networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                            flags=["flags"],
                
                            # the properties below are optional
                            masks=["masks"]
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6a4539cb428b880e373a3db5923e9d0f2d2f91e07045af9358db4aa1f7b47b7)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument match_attributes", value=match_attributes, expected_type=type_hints["match_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "actions": actions,
                "match_attributes": match_attributes,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''The actions to take on a packet that matches one of the stateless rule definition's match attributes.

            You must specify a standard action and you can add custom actions.
            .. epigraph::

               Network Firewall only forwards a packet for stateful rule inspection if you specify ``aws:forward_to_sfe`` for a rule that the packet matches, or if the packet doesn't match any stateless rule and you specify ``aws:forward_to_sfe`` for the ``StatelessDefaultActions`` setting for the ``FirewallPolicy`` .

            For every rule, you must specify exactly one of the following standard actions.

            - *aws:pass* - Discontinues all inspection of the packet and permits it to go to its intended destination.
            - *aws:drop* - Discontinues all inspection of the packet and blocks it from going to its intended destination.
            - *aws:forward_to_sfe* - Discontinues stateless inspection of the packet and forwards it to the stateful rule engine for inspection.

            Additionally, you can specify a custom action. To do this, you define a custom action by name and type, then provide the name you've assigned to the action in this ``Actions`` setting.

            To provide more than one action in this setting, separate the settings with a comma. For example, if you have a publish metrics custom action that you've named ``MyMetricsAction`` , then you could specify the standard action ``aws:pass`` combined with the custom action using ``[“aws:pass”, “MyMetricsAction”]`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def match_attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.MatchAttributesProperty"]:
            '''Criteria for Network Firewall to use to inspect an individual packet in stateless rule inspection.

            Each match attributes set can include one or more items such as IP address, CIDR range, port number, protocol, and TCP flags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-matchattributes
            '''
            result = self._values.get("match_attributes")
            assert result is not None, "Required property 'match_attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.MatchAttributesProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.RuleGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rules_source": "rulesSource",
            "reference_sets": "referenceSets",
            "rule_variables": "ruleVariables",
            "stateful_rule_options": "statefulRuleOptions",
        },
    )
    class RuleGroupProperty:
        def __init__(
            self,
            *,
            rules_source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.RulesSourceProperty", typing.Dict[builtins.str, typing.Any]]],
            reference_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.ReferenceSetsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rule_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.RuleVariablesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            stateful_rule_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.StatefulRuleOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The object that defines the rules in a rule group.

            AWS Network Firewall uses a rule group to inspect and control network traffic. You define stateless rule groups to inspect individual packets and you define stateful rule groups to inspect packets in the context of their traffic flow.

            To use a rule group, you include it by reference in an Network Firewall firewall policy, then you use the policy in a firewall. You can reference a rule group from more than one firewall policy, and you can use a firewall policy in more than one firewall.

            :param rules_source: The stateful rules or stateless rules for the rule group.
            :param reference_sets: The reference sets for the stateful rule group.
            :param rule_variables: Settings that are available for use in the rules in the rule group. You can only use these for stateful rule groups.
            :param stateful_rule_options: Additional options governing how Network Firewall handles stateful rules. The policies where you use your stateful rule group must have stateful rule options settings that are compatible with these settings. Some limitations apply; for more information, see `Strict evaluation order <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-limitations-caveats.html>`_ in the *AWS Network Firewall Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                rule_group_property = networkfirewall.CfnRuleGroup.RuleGroupProperty(
                    rules_source=networkfirewall.CfnRuleGroup.RulesSourceProperty(
                        rules_source_list=networkfirewall.CfnRuleGroup.RulesSourceListProperty(
                            generated_rules_type="generatedRulesType",
                            targets=["targets"],
                            target_types=["targetTypes"]
                        ),
                        rules_string="rulesString",
                        stateful_rules=[networkfirewall.CfnRuleGroup.StatefulRuleProperty(
                            action="action",
                            header=networkfirewall.CfnRuleGroup.HeaderProperty(
                                destination="destination",
                                destination_port="destinationPort",
                                direction="direction",
                                protocol="protocol",
                                source="source",
                                source_port="sourcePort"
                            ),
                            rule_options=[networkfirewall.CfnRuleGroup.RuleOptionProperty(
                                keyword="keyword",
                
                                # the properties below are optional
                                settings=["settings"]
                            )]
                        )],
                        stateless_rules_and_custom_actions=networkfirewall.CfnRuleGroup.StatelessRulesAndCustomActionsProperty(
                            stateless_rules=[networkfirewall.CfnRuleGroup.StatelessRuleProperty(
                                priority=123,
                                rule_definition=networkfirewall.CfnRuleGroup.RuleDefinitionProperty(
                                    actions=["actions"],
                                    match_attributes=networkfirewall.CfnRuleGroup.MatchAttributesProperty(
                                        destination_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                            from_port=123,
                                            to_port=123
                                        )],
                                        destinations=[networkfirewall.CfnRuleGroup.AddressProperty(
                                            address_definition="addressDefinition"
                                        )],
                                        protocols=[123],
                                        source_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                            from_port=123,
                                            to_port=123
                                        )],
                                        sources=[networkfirewall.CfnRuleGroup.AddressProperty(
                                            address_definition="addressDefinition"
                                        )],
                                        tcp_flags=[networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                                            flags=["flags"],
                
                                            # the properties below are optional
                                            masks=["masks"]
                                        )]
                                    )
                                )
                            )],
                
                            # the properties below are optional
                            custom_actions=[networkfirewall.CfnRuleGroup.CustomActionProperty(
                                action_definition=networkfirewall.CfnRuleGroup.ActionDefinitionProperty(
                                    publish_metric_action=networkfirewall.CfnRuleGroup.PublishMetricActionProperty(
                                        dimensions=[networkfirewall.CfnRuleGroup.DimensionProperty(
                                            value="value"
                                        )]
                                    )
                                ),
                                action_name="actionName"
                            )]
                        )
                    ),
                
                    # the properties below are optional
                    reference_sets=networkfirewall.CfnRuleGroup.ReferenceSetsProperty(
                        ip_set_references={
                            "ip_set_references_key": {
                                "reference_arn": "referenceArn"
                            }
                        }
                    ),
                    rule_variables=networkfirewall.CfnRuleGroup.RuleVariablesProperty(
                        ip_sets={
                            "ip_sets_key": {
                                "definition": ["definition"]
                            }
                        },
                        port_sets={
                            "port_sets_key": networkfirewall.CfnRuleGroup.PortSetProperty(
                                definition=["definition"]
                            )
                        }
                    ),
                    stateful_rule_options=networkfirewall.CfnRuleGroup.StatefulRuleOptionsProperty(
                        rule_order="ruleOrder"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6031839dccab8578d6df945e603f857681f1ba43a8750c6823a4956903ee6b0a)
                check_type(argname="argument rules_source", value=rules_source, expected_type=type_hints["rules_source"])
                check_type(argname="argument reference_sets", value=reference_sets, expected_type=type_hints["reference_sets"])
                check_type(argname="argument rule_variables", value=rule_variables, expected_type=type_hints["rule_variables"])
                check_type(argname="argument stateful_rule_options", value=stateful_rule_options, expected_type=type_hints["stateful_rule_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rules_source": rules_source,
            }
            if reference_sets is not None:
                self._values["reference_sets"] = reference_sets
            if rule_variables is not None:
                self._values["rule_variables"] = rule_variables
            if stateful_rule_options is not None:
                self._values["stateful_rule_options"] = stateful_rule_options

        @builtins.property
        def rules_source(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RulesSourceProperty"]:
            '''The stateful rules or stateless rules for the rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulessource
            '''
            result = self._values.get("rules_source")
            assert result is not None, "Required property 'rules_source' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RulesSourceProperty"], result)

        @builtins.property
        def reference_sets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.ReferenceSetsProperty"]]:
            '''The reference sets for the stateful rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-referencesets
            '''
            result = self._values.get("reference_sets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.ReferenceSetsProperty"]], result)

        @builtins.property
        def rule_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleVariablesProperty"]]:
            '''Settings that are available for use in the rules in the rule group.

            You can only use these for stateful rule groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulevariables
            '''
            result = self._values.get("rule_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleVariablesProperty"]], result)

        @builtins.property
        def stateful_rule_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.StatefulRuleOptionsProperty"]]:
            '''Additional options governing how Network Firewall handles stateful rules.

            The policies where you use your stateful rule group must have stateful rule options settings that are compatible with these settings. Some limitations apply; for more information, see `Strict evaluation order <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-limitations-caveats.html>`_ in the *AWS Network Firewall Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-statefulruleoptions
            '''
            result = self._values.get("stateful_rule_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.StatefulRuleOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.RuleOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"keyword": "keyword", "settings": "settings"},
    )
    class RuleOptionProperty:
        def __init__(
            self,
            *,
            keyword: builtins.str,
            settings: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Additional settings for a stateful rule.

            :param keyword: The Suricata rule option keywords. For Network Firewall , the keyword signature ID (sid) is required in the format ``sid:112233`` . The sid must be unique within the rule group. For information about Suricata rule option keywords, see `Rule options <https://docs.aws.amazon.com/https://suricata.readthedocs.io/en/suricata-6.0.9/rules/intro.html#rule-options>`_ .
            :param settings: The Suricata rule option settings. Settings have zero or more values, and the number of possible settings and required settings depends on the keyword. The format for Settings is ``number`` . For information about Suricata rule option settings, see `Rule options <https://docs.aws.amazon.com/https://suricata.readthedocs.io/en/suricata-6.0.9/rules/intro.html#rule-options>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                rule_option_property = networkfirewall.CfnRuleGroup.RuleOptionProperty(
                    keyword="keyword",
                
                    # the properties below are optional
                    settings=["settings"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__82f117785b5345a4a7fbef540dfb4ab49e1476bb3ee3f5b32f4bf8bdde04fa35)
                check_type(argname="argument keyword", value=keyword, expected_type=type_hints["keyword"])
                check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "keyword": keyword,
            }
            if settings is not None:
                self._values["settings"] = settings

        @builtins.property
        def keyword(self) -> builtins.str:
            '''The Suricata rule option keywords.

            For Network Firewall , the keyword signature ID (sid) is required in the format ``sid:112233`` . The sid must be unique within the rule group. For information about Suricata rule option keywords, see `Rule options <https://docs.aws.amazon.com/https://suricata.readthedocs.io/en/suricata-6.0.9/rules/intro.html#rule-options>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-keyword
            '''
            result = self._values.get("keyword")
            assert result is not None, "Required property 'keyword' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def settings(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Suricata rule option settings.

            Settings have zero or more values, and the number of possible settings and required settings depends on the keyword. The format for Settings is ``number`` . For information about Suricata rule option settings, see `Rule options <https://docs.aws.amazon.com/https://suricata.readthedocs.io/en/suricata-6.0.9/rules/intro.html#rule-options>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-settings
            '''
            result = self._values.get("settings")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.RuleVariablesProperty",
        jsii_struct_bases=[],
        name_mapping={"ip_sets": "ipSets", "port_sets": "portSets"},
    )
    class RuleVariablesProperty:
        def __init__(
            self,
            *,
            ip_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.IPSetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            port_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.PortSetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Settings that are available for use in the rules in the ``RuleGroup`` where this is defined.

            :param ip_sets: A list of IP addresses and address ranges, in CIDR notation.
            :param port_sets: A list of port ranges.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                rule_variables_property = networkfirewall.CfnRuleGroup.RuleVariablesProperty(
                    ip_sets={
                        "ip_sets_key": {
                            "definition": ["definition"]
                        }
                    },
                    port_sets={
                        "port_sets_key": networkfirewall.CfnRuleGroup.PortSetProperty(
                            definition=["definition"]
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a07f3723113c8b16a34bf34741ea1461bc25f6ab3b0720f6a8aa564d1272e4ca)
                check_type(argname="argument ip_sets", value=ip_sets, expected_type=type_hints["ip_sets"])
                check_type(argname="argument port_sets", value=port_sets, expected_type=type_hints["port_sets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ip_sets is not None:
                self._values["ip_sets"] = ip_sets
            if port_sets is not None:
                self._values["port_sets"] = port_sets

        @builtins.property
        def ip_sets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.IPSetProperty"]]]]:
            '''A list of IP addresses and address ranges, in CIDR notation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-ipsets
            '''
            result = self._values.get("ip_sets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.IPSetProperty"]]]], result)

        @builtins.property
        def port_sets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.PortSetProperty"]]]]:
            '''A list of port ranges.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-portsets
            '''
            result = self._values.get("port_sets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.PortSetProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleVariablesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.RulesSourceListProperty",
        jsii_struct_bases=[],
        name_mapping={
            "generated_rules_type": "generatedRulesType",
            "targets": "targets",
            "target_types": "targetTypes",
        },
    )
    class RulesSourceListProperty:
        def __init__(
            self,
            *,
            generated_rules_type: builtins.str,
            targets: typing.Sequence[builtins.str],
            target_types: typing.Sequence[builtins.str],
        ) -> None:
            '''Stateful inspection criteria for a domain list rule group.

            For HTTPS traffic, domain filtering is SNI-based. It uses the server name indicator extension of the TLS handshake.

            By default, Network Firewall domain list inspection only includes traffic coming from the VPC where you deploy the firewall. To inspect traffic from IP addresses outside of the deployment VPC, you set the ``HOME_NET`` rule variable to include the CIDR range of the deployment VPC plus the other CIDR ranges. For more information, see ``RuleGroup.RuleVariables`` in this guide and `Stateful domain list rule groups in AWS Network Firewall <https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html>`_ in the *Network Firewall Developer Guide*

            :param generated_rules_type: Whether you want to allow or deny access to the domains in your target list.
            :param targets: The domains that you want to inspect for in your traffic flows. Valid domain specifications are the following:. - Explicit names. For example, ``abc.example.com`` matches only the domain ``abc.example.com`` . - Names that use a domain wildcard, which you indicate with an initial ' ``.`` '. For example, ``.example.com`` matches ``example.com`` and matches all subdomains of ``example.com`` , such as ``abc.example.com`` and ``www.example.com`` .
            :param target_types: The types of targets to inspect for. Valid values are ``TLS_SNI`` and ``HTTP_HOST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                rules_source_list_property = networkfirewall.CfnRuleGroup.RulesSourceListProperty(
                    generated_rules_type="generatedRulesType",
                    targets=["targets"],
                    target_types=["targetTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f9a485e00c504005fdc6e395458d012eb99f789685105dcedf2228712fff5a91)
                check_type(argname="argument generated_rules_type", value=generated_rules_type, expected_type=type_hints["generated_rules_type"])
                check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
                check_type(argname="argument target_types", value=target_types, expected_type=type_hints["target_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "generated_rules_type": generated_rules_type,
                "targets": targets,
                "target_types": target_types,
            }

        @builtins.property
        def generated_rules_type(self) -> builtins.str:
            '''Whether you want to allow or deny access to the domains in your target list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-generatedrulestype
            '''
            result = self._values.get("generated_rules_type")
            assert result is not None, "Required property 'generated_rules_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def targets(self) -> typing.List[builtins.str]:
            '''The domains that you want to inspect for in your traffic flows. Valid domain specifications are the following:.

            - Explicit names. For example, ``abc.example.com`` matches only the domain ``abc.example.com`` .
            - Names that use a domain wildcard, which you indicate with an initial ' ``.`` '. For example, ``.example.com`` matches ``example.com`` and matches all subdomains of ``example.com`` , such as ``abc.example.com`` and ``www.example.com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targets
            '''
            result = self._values.get("targets")
            assert result is not None, "Required property 'targets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def target_types(self) -> typing.List[builtins.str]:
            '''The types of targets to inspect for.

            Valid values are ``TLS_SNI`` and ``HTTP_HOST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targettypes
            '''
            result = self._values.get("target_types")
            assert result is not None, "Required property 'target_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RulesSourceListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.RulesSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rules_source_list": "rulesSourceList",
            "rules_string": "rulesString",
            "stateful_rules": "statefulRules",
            "stateless_rules_and_custom_actions": "statelessRulesAndCustomActions",
        },
    )
    class RulesSourceProperty:
        def __init__(
            self,
            *,
            rules_source_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.RulesSourceListProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rules_string: typing.Optional[builtins.str] = None,
            stateful_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.StatefulRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            stateless_rules_and_custom_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.StatelessRulesAndCustomActionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The stateless or stateful rules definitions for use in a single rule group.

            Each rule group requires a single ``RulesSource`` . You can use an instance of this for either stateless rules or stateful rules.

            :param rules_source_list: Stateful inspection criteria for a domain list rule group.
            :param rules_string: Stateful inspection criteria, provided in Suricata compatible rules. Suricata is an open-source threat detection framework that includes a standard rule-based language for network traffic inspection. These rules contain the inspection criteria and the action to take for traffic that matches the criteria, so this type of rule group doesn't have a separate action setting. .. epigraph:: You can't use the ``priority`` keyword if the ``RuleOrder`` option in ``StatefulRuleOptions`` is set to ``STRICT_ORDER`` .
            :param stateful_rules: An array of individual stateful rules inspection criteria to be used together in a stateful rule group. Use this option to specify simple Suricata rules with protocol, source and destination, ports, direction, and rule options. For information about the Suricata ``Rules`` format, see `Rules Format <https://docs.aws.amazon.com/https://suricata.readthedocs.io/en/suricata-6.0.9/rules/intro.html>`_ .
            :param stateless_rules_and_custom_actions: Stateless inspection criteria to be used in a stateless rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                rules_source_property = networkfirewall.CfnRuleGroup.RulesSourceProperty(
                    rules_source_list=networkfirewall.CfnRuleGroup.RulesSourceListProperty(
                        generated_rules_type="generatedRulesType",
                        targets=["targets"],
                        target_types=["targetTypes"]
                    ),
                    rules_string="rulesString",
                    stateful_rules=[networkfirewall.CfnRuleGroup.StatefulRuleProperty(
                        action="action",
                        header=networkfirewall.CfnRuleGroup.HeaderProperty(
                            destination="destination",
                            destination_port="destinationPort",
                            direction="direction",
                            protocol="protocol",
                            source="source",
                            source_port="sourcePort"
                        ),
                        rule_options=[networkfirewall.CfnRuleGroup.RuleOptionProperty(
                            keyword="keyword",
                
                            # the properties below are optional
                            settings=["settings"]
                        )]
                    )],
                    stateless_rules_and_custom_actions=networkfirewall.CfnRuleGroup.StatelessRulesAndCustomActionsProperty(
                        stateless_rules=[networkfirewall.CfnRuleGroup.StatelessRuleProperty(
                            priority=123,
                            rule_definition=networkfirewall.CfnRuleGroup.RuleDefinitionProperty(
                                actions=["actions"],
                                match_attributes=networkfirewall.CfnRuleGroup.MatchAttributesProperty(
                                    destination_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                        from_port=123,
                                        to_port=123
                                    )],
                                    destinations=[networkfirewall.CfnRuleGroup.AddressProperty(
                                        address_definition="addressDefinition"
                                    )],
                                    protocols=[123],
                                    source_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                        from_port=123,
                                        to_port=123
                                    )],
                                    sources=[networkfirewall.CfnRuleGroup.AddressProperty(
                                        address_definition="addressDefinition"
                                    )],
                                    tcp_flags=[networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                                        flags=["flags"],
                
                                        # the properties below are optional
                                        masks=["masks"]
                                    )]
                                )
                            )
                        )],
                
                        # the properties below are optional
                        custom_actions=[networkfirewall.CfnRuleGroup.CustomActionProperty(
                            action_definition=networkfirewall.CfnRuleGroup.ActionDefinitionProperty(
                                publish_metric_action=networkfirewall.CfnRuleGroup.PublishMetricActionProperty(
                                    dimensions=[networkfirewall.CfnRuleGroup.DimensionProperty(
                                        value="value"
                                    )]
                                )
                            ),
                            action_name="actionName"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__37c2f6cfa9ab89c36a10e214087cb83419a7c8be9fa0d97cb6ff5c156ec1ed2b)
                check_type(argname="argument rules_source_list", value=rules_source_list, expected_type=type_hints["rules_source_list"])
                check_type(argname="argument rules_string", value=rules_string, expected_type=type_hints["rules_string"])
                check_type(argname="argument stateful_rules", value=stateful_rules, expected_type=type_hints["stateful_rules"])
                check_type(argname="argument stateless_rules_and_custom_actions", value=stateless_rules_and_custom_actions, expected_type=type_hints["stateless_rules_and_custom_actions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rules_source_list is not None:
                self._values["rules_source_list"] = rules_source_list
            if rules_string is not None:
                self._values["rules_string"] = rules_string
            if stateful_rules is not None:
                self._values["stateful_rules"] = stateful_rules
            if stateless_rules_and_custom_actions is not None:
                self._values["stateless_rules_and_custom_actions"] = stateless_rules_and_custom_actions

        @builtins.property
        def rules_source_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RulesSourceListProperty"]]:
            '''Stateful inspection criteria for a domain list rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulessourcelist
            '''
            result = self._values.get("rules_source_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RulesSourceListProperty"]], result)

        @builtins.property
        def rules_string(self) -> typing.Optional[builtins.str]:
            '''Stateful inspection criteria, provided in Suricata compatible rules.

            Suricata is an open-source threat detection framework that includes a standard rule-based language for network traffic inspection.

            These rules contain the inspection criteria and the action to take for traffic that matches the criteria, so this type of rule group doesn't have a separate action setting.
            .. epigraph::

               You can't use the ``priority`` keyword if the ``RuleOrder`` option in ``StatefulRuleOptions`` is set to ``STRICT_ORDER`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulesstring
            '''
            result = self._values.get("rules_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stateful_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.StatefulRuleProperty"]]]]:
            '''An array of individual stateful rules inspection criteria to be used together in a stateful rule group.

            Use this option to specify simple Suricata rules with protocol, source and destination, ports, direction, and rule options. For information about the Suricata ``Rules`` format, see `Rules Format <https://docs.aws.amazon.com/https://suricata.readthedocs.io/en/suricata-6.0.9/rules/intro.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statefulrules
            '''
            result = self._values.get("stateful_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.StatefulRuleProperty"]]]], result)

        @builtins.property
        def stateless_rules_and_custom_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.StatelessRulesAndCustomActionsProperty"]]:
            '''Stateless inspection criteria to be used in a stateless rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statelessrulesandcustomactions
            '''
            result = self._values.get("stateless_rules_and_custom_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.StatelessRulesAndCustomActionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RulesSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.StatefulRuleOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"rule_order": "ruleOrder"},
    )
    class StatefulRuleOptionsProperty:
        def __init__(self, *, rule_order: typing.Optional[builtins.str] = None) -> None:
            '''Additional options governing how Network Firewall handles the rule group.

            You can only use these for stateful rule groups.

            :param rule_order: Indicates how to manage the order of the rule evaluation for the rule group. ``DEFAULT_ACTION_ORDER`` is the default behavior. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see `Evaluation order for stateful rules <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html>`_ in the *AWS Network Firewall Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                stateful_rule_options_property = networkfirewall.CfnRuleGroup.StatefulRuleOptionsProperty(
                    rule_order="ruleOrder"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__059685e154b150834c61bccd6793a66e1d0e92258779eb937ca1fa3a1670f3c2)
                check_type(argname="argument rule_order", value=rule_order, expected_type=type_hints["rule_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rule_order is not None:
                self._values["rule_order"] = rule_order

        @builtins.property
        def rule_order(self) -> typing.Optional[builtins.str]:
            '''Indicates how to manage the order of the rule evaluation for the rule group.

            ``DEFAULT_ACTION_ORDER`` is the default behavior. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see `Evaluation order for stateful rules <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html>`_ in the *AWS Network Firewall Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html#cfn-networkfirewall-rulegroup-statefulruleoptions-ruleorder
            '''
            result = self._values.get("rule_order")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatefulRuleOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.StatefulRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "header": "header",
            "rule_options": "ruleOptions",
        },
    )
    class StatefulRuleProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            header: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.HeaderProperty", typing.Dict[builtins.str, typing.Any]]],
            rule_options: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.RuleOptionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A single Suricata rules specification, for use in a stateful rule group.

            Use this option to specify a simple Suricata rule with protocol, source and destination, ports, direction, and rule options. For information about the Suricata ``Rules`` format, see `Rules Format <https://docs.aws.amazon.com/https://suricata.readthedocs.io/en/suricata-6.0.9/rules/intro.html>`_ .

            :param action: Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria. For all actions, Network Firewall performs the specified action and discontinues stateful inspection of the traffic flow. The actions for a stateful rule are defined as follows: - *PASS* - Permits the packets to go to the intended destination. - *DROP* - Blocks the packets from going to the intended destination and sends an alert log message, if alert logging is configured in the ``Firewall`` ``LoggingConfiguration`` . - *REJECT* - Drops traffic that matches the conditions of the stateful rule and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and a ``RST`` bit contained in the TCP header flags. ``REJECT`` is available only for TCP traffic. - *ALERT* - Permits the packets to go to the intended destination and sends an alert log message, if alert logging is configured in the ``Firewall`` ``LoggingConfiguration`` . You can use this action to test a rule that you intend to use to drop traffic. You can enable the rule with ``ALERT`` action, verify in the logs that the rule is filtering as you want, then change the action to ``DROP`` . - *REJECT* - Drops TCP traffic that matches the conditions of the stateful rule, and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and a ``RST`` bit contained in the TCP header flags. Also sends an alert log mesage if alert logging is configured in the ``Firewall`` ``LoggingConfiguration`` . ``REJECT`` isn't currently available for use with IMAP and FTP protocols.
            :param header: The stateful inspection criteria for this rule, used to inspect traffic flows.
            :param rule_options: Additional settings for a stateful rule, provided as keywords and settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                stateful_rule_property = networkfirewall.CfnRuleGroup.StatefulRuleProperty(
                    action="action",
                    header=networkfirewall.CfnRuleGroup.HeaderProperty(
                        destination="destination",
                        destination_port="destinationPort",
                        direction="direction",
                        protocol="protocol",
                        source="source",
                        source_port="sourcePort"
                    ),
                    rule_options=[networkfirewall.CfnRuleGroup.RuleOptionProperty(
                        keyword="keyword",
                
                        # the properties below are optional
                        settings=["settings"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5bb56af25d6c8c99d593795131e22b214fd8722c9ab610ce9e26db6f72cae04)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument header", value=header, expected_type=type_hints["header"])
                check_type(argname="argument rule_options", value=rule_options, expected_type=type_hints["rule_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "header": header,
                "rule_options": rule_options,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria.

            For all actions, Network Firewall performs the specified action and discontinues stateful inspection of the traffic flow.

            The actions for a stateful rule are defined as follows:

            - *PASS* - Permits the packets to go to the intended destination.
            - *DROP* - Blocks the packets from going to the intended destination and sends an alert log message, if alert logging is configured in the ``Firewall`` ``LoggingConfiguration`` .
            - *REJECT* - Drops traffic that matches the conditions of the stateful rule and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and a ``RST`` bit contained in the TCP header flags. ``REJECT`` is available only for TCP traffic.
            - *ALERT* - Permits the packets to go to the intended destination and sends an alert log message, if alert logging is configured in the ``Firewall`` ``LoggingConfiguration`` .

            You can use this action to test a rule that you intend to use to drop traffic. You can enable the rule with ``ALERT`` action, verify in the logs that the rule is filtering as you want, then change the action to ``DROP`` .

            - *REJECT* - Drops TCP traffic that matches the conditions of the stateful rule, and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and a ``RST`` bit contained in the TCP header flags. Also sends an alert log mesage if alert logging is configured in the ``Firewall`` ``LoggingConfiguration`` .

            ``REJECT`` isn't currently available for use with IMAP and FTP protocols.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def header(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.HeaderProperty"]:
            '''The stateful inspection criteria for this rule, used to inspect traffic flows.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-header
            '''
            result = self._values.get("header")
            assert result is not None, "Required property 'header' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.HeaderProperty"], result)

        @builtins.property
        def rule_options(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleOptionProperty"]]]:
            '''Additional settings for a stateful rule, provided as keywords and settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-ruleoptions
            '''
            result = self._values.get("rule_options")
            assert result is not None, "Required property 'rule_options' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleOptionProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatefulRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.StatelessRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"priority": "priority", "rule_definition": "ruleDefinition"},
    )
    class StatelessRuleProperty:
        def __init__(
            self,
            *,
            priority: jsii.Number,
            rule_definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.RuleDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A single stateless rule.

            This is used in ``RuleGroup.StatelessRulesAndCustomActions`` .

            :param priority: Indicates the order in which to run this rule relative to all of the rules that are defined for a stateless rule group. Network Firewall evaluates the rules in a rule group starting with the lowest priority setting. You must ensure that the priority settings are unique for the rule group. Each stateless rule group uses exactly one ``StatelessRulesAndCustomActions`` object, and each ``StatelessRulesAndCustomActions`` contains exactly one ``StatelessRules`` object. To ensure unique priority settings for your rule groups, set unique priorities for the stateless rules that you define inside any single ``StatelessRules`` object. You can change the priority settings of your rules at any time. To make it easier to insert rules later, number them so there's a wide range in between, for example use 100, 200, and so on.
            :param rule_definition: Defines the stateless 5-tuple packet inspection criteria and the action to take on a packet that matches the criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                stateless_rule_property = networkfirewall.CfnRuleGroup.StatelessRuleProperty(
                    priority=123,
                    rule_definition=networkfirewall.CfnRuleGroup.RuleDefinitionProperty(
                        actions=["actions"],
                        match_attributes=networkfirewall.CfnRuleGroup.MatchAttributesProperty(
                            destination_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                from_port=123,
                                to_port=123
                            )],
                            destinations=[networkfirewall.CfnRuleGroup.AddressProperty(
                                address_definition="addressDefinition"
                            )],
                            protocols=[123],
                            source_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                from_port=123,
                                to_port=123
                            )],
                            sources=[networkfirewall.CfnRuleGroup.AddressProperty(
                                address_definition="addressDefinition"
                            )],
                            tcp_flags=[networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                                flags=["flags"],
                
                                # the properties below are optional
                                masks=["masks"]
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8abd713c2522cea4720da70b4aa087d7eb1f6a9257d6d3a5b76148f6102fb22d)
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument rule_definition", value=rule_definition, expected_type=type_hints["rule_definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "priority": priority,
                "rule_definition": rule_definition,
            }

        @builtins.property
        def priority(self) -> jsii.Number:
            '''Indicates the order in which to run this rule relative to all of the rules that are defined for a stateless rule group.

            Network Firewall evaluates the rules in a rule group starting with the lowest priority setting. You must ensure that the priority settings are unique for the rule group.

            Each stateless rule group uses exactly one ``StatelessRulesAndCustomActions`` object, and each ``StatelessRulesAndCustomActions`` contains exactly one ``StatelessRules`` object. To ensure unique priority settings for your rule groups, set unique priorities for the stateless rules that you define inside any single ``StatelessRules`` object.

            You can change the priority settings of your rules at any time. To make it easier to insert rules later, number them so there's a wide range in between, for example use 100, 200, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rule_definition(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleDefinitionProperty"]:
            '''Defines the stateless 5-tuple packet inspection criteria and the action to take on a packet that matches the criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-ruledefinition
            '''
            result = self._values.get("rule_definition")
            assert result is not None, "Required property 'rule_definition' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.RuleDefinitionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatelessRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.StatelessRulesAndCustomActionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "stateless_rules": "statelessRules",
            "custom_actions": "customActions",
        },
    )
    class StatelessRulesAndCustomActionsProperty:
        def __init__(
            self,
            *,
            stateless_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.StatelessRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
            custom_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuleGroup.CustomActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Stateless inspection criteria.

            Each stateless rule group uses exactly one of these data types to define its stateless rules.

            :param stateless_rules: Defines the set of stateless rules for use in a stateless rule group.
            :param custom_actions: Defines an array of individual custom action definitions that are available for use by the stateless rules in this ``StatelessRulesAndCustomActions`` specification. You name each custom action that you define, and then you can use it by name in your stateless rule ``RuleGroup.RuleDefinition`` ``Actions`` specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                stateless_rules_and_custom_actions_property = networkfirewall.CfnRuleGroup.StatelessRulesAndCustomActionsProperty(
                    stateless_rules=[networkfirewall.CfnRuleGroup.StatelessRuleProperty(
                        priority=123,
                        rule_definition=networkfirewall.CfnRuleGroup.RuleDefinitionProperty(
                            actions=["actions"],
                            match_attributes=networkfirewall.CfnRuleGroup.MatchAttributesProperty(
                                destination_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                    from_port=123,
                                    to_port=123
                                )],
                                destinations=[networkfirewall.CfnRuleGroup.AddressProperty(
                                    address_definition="addressDefinition"
                                )],
                                protocols=[123],
                                source_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                    from_port=123,
                                    to_port=123
                                )],
                                sources=[networkfirewall.CfnRuleGroup.AddressProperty(
                                    address_definition="addressDefinition"
                                )],
                                tcp_flags=[networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                                    flags=["flags"],
                
                                    # the properties below are optional
                                    masks=["masks"]
                                )]
                            )
                        )
                    )],
                
                    # the properties below are optional
                    custom_actions=[networkfirewall.CfnRuleGroup.CustomActionProperty(
                        action_definition=networkfirewall.CfnRuleGroup.ActionDefinitionProperty(
                            publish_metric_action=networkfirewall.CfnRuleGroup.PublishMetricActionProperty(
                                dimensions=[networkfirewall.CfnRuleGroup.DimensionProperty(
                                    value="value"
                                )]
                            )
                        ),
                        action_name="actionName"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71d7a12c23bdb40d0d25319bf80720d55c4205129c386e8de5676df43ea5e61b)
                check_type(argname="argument stateless_rules", value=stateless_rules, expected_type=type_hints["stateless_rules"])
                check_type(argname="argument custom_actions", value=custom_actions, expected_type=type_hints["custom_actions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "stateless_rules": stateless_rules,
            }
            if custom_actions is not None:
                self._values["custom_actions"] = custom_actions

        @builtins.property
        def stateless_rules(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.StatelessRuleProperty"]]]:
            '''Defines the set of stateless rules for use in a stateless rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-statelessrules
            '''
            result = self._values.get("stateless_rules")
            assert result is not None, "Required property 'stateless_rules' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.StatelessRuleProperty"]]], result)

        @builtins.property
        def custom_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.CustomActionProperty"]]]]:
            '''Defines an array of individual custom action definitions that are available for use by the stateless rules in this ``StatelessRulesAndCustomActions`` specification.

            You name each custom action that you define, and then you can use it by name in your stateless rule ``RuleGroup.RuleDefinition`` ``Actions`` specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-customactions
            '''
            result = self._values.get("custom_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRuleGroup.CustomActionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatelessRulesAndCustomActionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroup.TCPFlagFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"flags": "flags", "masks": "masks"},
    )
    class TCPFlagFieldProperty:
        def __init__(
            self,
            *,
            flags: typing.Sequence[builtins.str],
            masks: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''TCP flags and masks to inspect packets for. This is used in the ``RuleGroup.MatchAttributes`` specification.

            For example:

            ``"TCPFlags": [ { "Flags": [ "ECE", "SYN" ], "Masks": [ "SYN", "ECE" ] } ]``

            :param flags: Used in conjunction with the ``Masks`` setting to define the flags that must be set and flags that must not be set in order for the packet to match. This setting can only specify values that are also specified in the ``Masks`` setting. For the flags that are specified in the masks setting, the following must be true for the packet to match: - The ones that are set in this flags setting must be set in the packet. - The ones that are not set in this flags setting must also not be set in the packet.
            :param masks: The set of flags to consider in the inspection. To inspect all flags in the valid values list, leave this with no setting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                t_cPFlag_field_property = networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                    flags=["flags"],
                
                    # the properties below are optional
                    masks=["masks"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__775fa1817d39168a6b1883b9e449352da902edc72fb398c55cda18aa8ead3039)
                check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
                check_type(argname="argument masks", value=masks, expected_type=type_hints["masks"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "flags": flags,
            }
            if masks is not None:
                self._values["masks"] = masks

        @builtins.property
        def flags(self) -> typing.List[builtins.str]:
            '''Used in conjunction with the ``Masks`` setting to define the flags that must be set and flags that must not be set in order for the packet to match.

            This setting can only specify values that are also specified in the ``Masks`` setting.

            For the flags that are specified in the masks setting, the following must be true for the packet to match:

            - The ones that are set in this flags setting must be set in the packet.
            - The ones that are not set in this flags setting must also not be set in the packet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-flags
            '''
            result = self._values.get("flags")
            assert result is not None, "Required property 'flags' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def masks(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The set of flags to consider in the inspection.

            To inspect all flags in the valid values list, leave this with no setting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-masks
            '''
            result = self._values.get("masks")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TCPFlagFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnRuleGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "rule_group_name": "ruleGroupName",
        "type": "type",
        "description": "description",
        "rule_group": "ruleGroup",
        "tags": "tags",
    },
)
class CfnRuleGroupProps:
    def __init__(
        self,
        *,
        capacity: jsii.Number,
        rule_group_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rule_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.RuleGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuleGroup``.

        :param capacity: The maximum operating resources that this rule group can use. You can't change a rule group's capacity setting after you create the rule group. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group.
        :param rule_group_name: The descriptive name of the rule group. You can't change the name of a rule group after you create it.
        :param type: Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.
        :param description: A description of the rule group.
        :param rule_group: An object that defines the rule group rules.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkfirewall as networkfirewall
            
            cfn_rule_group_props = networkfirewall.CfnRuleGroupProps(
                capacity=123,
                rule_group_name="ruleGroupName",
                type="type",
            
                # the properties below are optional
                description="description",
                rule_group=networkfirewall.CfnRuleGroup.RuleGroupProperty(
                    rules_source=networkfirewall.CfnRuleGroup.RulesSourceProperty(
                        rules_source_list=networkfirewall.CfnRuleGroup.RulesSourceListProperty(
                            generated_rules_type="generatedRulesType",
                            targets=["targets"],
                            target_types=["targetTypes"]
                        ),
                        rules_string="rulesString",
                        stateful_rules=[networkfirewall.CfnRuleGroup.StatefulRuleProperty(
                            action="action",
                            header=networkfirewall.CfnRuleGroup.HeaderProperty(
                                destination="destination",
                                destination_port="destinationPort",
                                direction="direction",
                                protocol="protocol",
                                source="source",
                                source_port="sourcePort"
                            ),
                            rule_options=[networkfirewall.CfnRuleGroup.RuleOptionProperty(
                                keyword="keyword",
            
                                # the properties below are optional
                                settings=["settings"]
                            )]
                        )],
                        stateless_rules_and_custom_actions=networkfirewall.CfnRuleGroup.StatelessRulesAndCustomActionsProperty(
                            stateless_rules=[networkfirewall.CfnRuleGroup.StatelessRuleProperty(
                                priority=123,
                                rule_definition=networkfirewall.CfnRuleGroup.RuleDefinitionProperty(
                                    actions=["actions"],
                                    match_attributes=networkfirewall.CfnRuleGroup.MatchAttributesProperty(
                                        destination_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                            from_port=123,
                                            to_port=123
                                        )],
                                        destinations=[networkfirewall.CfnRuleGroup.AddressProperty(
                                            address_definition="addressDefinition"
                                        )],
                                        protocols=[123],
                                        source_ports=[networkfirewall.CfnRuleGroup.PortRangeProperty(
                                            from_port=123,
                                            to_port=123
                                        )],
                                        sources=[networkfirewall.CfnRuleGroup.AddressProperty(
                                            address_definition="addressDefinition"
                                        )],
                                        tcp_flags=[networkfirewall.CfnRuleGroup.TCPFlagFieldProperty(
                                            flags=["flags"],
            
                                            # the properties below are optional
                                            masks=["masks"]
                                        )]
                                    )
                                )
                            )],
            
                            # the properties below are optional
                            custom_actions=[networkfirewall.CfnRuleGroup.CustomActionProperty(
                                action_definition=networkfirewall.CfnRuleGroup.ActionDefinitionProperty(
                                    publish_metric_action=networkfirewall.CfnRuleGroup.PublishMetricActionProperty(
                                        dimensions=[networkfirewall.CfnRuleGroup.DimensionProperty(
                                            value="value"
                                        )]
                                    )
                                ),
                                action_name="actionName"
                            )]
                        )
                    ),
            
                    # the properties below are optional
                    reference_sets=networkfirewall.CfnRuleGroup.ReferenceSetsProperty(
                        ip_set_references={
                            "ip_set_references_key": {
                                "reference_arn": "referenceArn"
                            }
                        }
                    ),
                    rule_variables=networkfirewall.CfnRuleGroup.RuleVariablesProperty(
                        ip_sets={
                            "ip_sets_key": {
                                "definition": ["definition"]
                            }
                        },
                        port_sets={
                            "port_sets_key": networkfirewall.CfnRuleGroup.PortSetProperty(
                                definition=["definition"]
                            )
                        }
                    ),
                    stateful_rule_options=networkfirewall.CfnRuleGroup.StatefulRuleOptionsProperty(
                        rule_order="ruleOrder"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__775b93be404fbe10bf6b023b8192636307852f30e49da9892d7e20aa443ecbd0)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument rule_group_name", value=rule_group_name, expected_type=type_hints["rule_group_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument rule_group", value=rule_group, expected_type=type_hints["rule_group"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity": capacity,
            "rule_group_name": rule_group_name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if rule_group is not None:
            self._values["rule_group"] = rule_group
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def capacity(self) -> jsii.Number:
        '''The maximum operating resources that this rule group can use.

        You can't change a rule group's capacity setting after you create the rule group. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-capacity
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule_group_name(self) -> builtins.str:
        '''The descriptive name of the rule group.

        You can't change the name of a rule group after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroupname
        '''
        result = self._values.get("rule_group_name")
        assert result is not None, "Required property 'rule_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Indicates whether the rule group is stateless or stateful.

        If the rule group is stateless, it contains
        stateless rules. If it is stateful, it contains stateful rules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_group(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRuleGroup.RuleGroupProperty]]:
        '''An object that defines the rule group rules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup
        '''
        result = self._values.get("rule_group")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRuleGroup.RuleGroupProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTLSInspectionConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfiguration",
):
    '''The object that defines a TLS inspection configuration.

    AWS Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.

    To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see `Inspecting SSL/TLS traffic with TLS inspection configurations <https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html>`_ in the *AWS Network Firewall Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html
    :cloudformationResource: AWS::NetworkFirewall::TLSInspectionConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkfirewall as networkfirewall
        
        cfn_tLSInspection_configuration = networkfirewall.CfnTLSInspectionConfiguration(self, "MyCfnTLSInspectionConfiguration",
            tls_inspection_configuration=networkfirewall.CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty(
                server_certificate_configurations=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty(
                    certificate_authority_arn="certificateAuthorityArn",
                    check_certificate_revocation_status=networkfirewall.CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty(
                        revoked_status_action="revokedStatusAction",
                        unknown_status_action="unknownStatusAction"
                    ),
                    scopes=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateScopeProperty(
                        destination_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                            from_port=123,
                            to_port=123
                        )],
                        destinations=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                            address_definition="addressDefinition"
                        )],
                        protocols=[123],
                        source_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                            from_port=123,
                            to_port=123
                        )],
                        sources=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                            address_definition="addressDefinition"
                        )]
                    )],
                    server_certificates=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateProperty(
                        resource_arn="resourceArn"
                    )]
                )]
            ),
            tls_inspection_configuration_name="tlsInspectionConfigurationName",
        
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
        tls_inspection_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        tls_inspection_configuration_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param tls_inspection_configuration: The object that defines a TLS inspection configuration. AWS Network Firewall uses TLS inspection configurations to decrypt your firewall's inbound and outbound SSL/TLS traffic. After decryption, AWS Network Firewall inspects the traffic according to your firewall policy's stateful rules, and then re-encrypts it before sending it to its destination. You can enable inspection of your firewall's inbound traffic, outbound traffic, or both. To use TLS inspection with your firewall, you must first import or provision certificates using AWS Certificate Manager , create a TLS inspection configuration, add that configuration to a new firewall policy, and then associate that policy with your firewall. For more information about using TLS inspection configurations, see `Inspecting SSL/TLS traffic with TLS inspection configurations <https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html>`_ in the *AWS Network Firewall Developer Guide* .
        :param tls_inspection_configuration_name: The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.
        :param description: A description of the TLS inspection configuration.
        :param tags: The key:value pairs to associate with the resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec764b679fc98c8fe3aa11d807ebebdd11b5c6a99f92f8eb7c03b663e2ff6773)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTLSInspectionConfigurationProps(
            tls_inspection_configuration=tls_inspection_configuration,
            tls_inspection_configuration_name=tls_inspection_configuration_name,
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fffc8d2cddb56be0caa1d022a327faef26e9d6137d82bda779515250e3fcff9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fba06f46a5cea5a67cd0374f887b8225a08a147db2a073ffe9bc73c588b4887)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTlsInspectionConfigurationArn")
    def attr_tls_inspection_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the TLS inspection configuration.

        :cloudformationAttribute: TLSInspectionConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTlsInspectionConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTlsInspectionConfigurationId")
    def attr_tls_inspection_configuration_id(self) -> builtins.str:
        '''A unique identifier for the TLS inspection configuration.

        This ID is returned in the responses to create and list commands. You provide it to operations such as update and delete.

        :cloudformationAttribute: TLSInspectionConfigurationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTlsInspectionConfigurationId"))

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
    @jsii.member(jsii_name="tlsInspectionConfiguration")
    def tls_inspection_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty"]:
        '''The object that defines a TLS inspection configuration.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty"], jsii.get(self, "tlsInspectionConfiguration"))

    @tls_inspection_configuration.setter
    def tls_inspection_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0caa3698092eac04f0f3cb6ef31ee8a37b5620e7b43e83135c822e030a956e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsInspectionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tlsInspectionConfigurationName")
    def tls_inspection_configuration_name(self) -> builtins.str:
        '''The descriptive name of the TLS inspection configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "tlsInspectionConfigurationName"))

    @tls_inspection_configuration_name.setter
    def tls_inspection_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc056f1763c9b07511c09bccb7850663b8f285be14ee1f3cb521a402d621782f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsInspectionConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the TLS inspection configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a315bf64b464c871474cdb7416d97974a1f1ecea9dca5b529ccb217aa9b8bdbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The key:value pairs to associate with the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1705dcb0cd17e874ce96cef7a6499dffda595fe61408ae3b8537babc4ea07e7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfiguration.AddressProperty",
        jsii_struct_bases=[],
        name_mapping={"address_definition": "addressDefinition"},
    )
    class AddressProperty:
        def __init__(self, *, address_definition: builtins.str) -> None:
            '''A single IP address specification.

            This is used in the `MatchAttributes <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html>`_ source and destination settings.

            :param address_definition: Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6. Examples: - To configure Network Firewall to inspect for the IP address 192.0.2.44, specify ``192.0.2.44/32`` . - To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` . - To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` . - To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` . For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-address.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                address_property = networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                    address_definition="addressDefinition"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d082db2e4a682d2415b7a09e26862470d9c413df2a8e84b76f381e13039916b)
                check_type(argname="argument address_definition", value=address_definition, expected_type=type_hints["address_definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address_definition": address_definition,
            }

        @builtins.property
        def address_definition(self) -> builtins.str:
            '''Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation.

            Network Firewall supports all address ranges for IPv4 and IPv6.

            Examples:

            - To configure Network Firewall to inspect for the IP address 192.0.2.44, specify ``192.0.2.44/32`` .
            - To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .
            - To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .
            - To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .

            For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-address.html#cfn-networkfirewall-tlsinspectionconfiguration-address-addressdefinition
            '''
            result = self._values.get("address_definition")
            assert result is not None, "Required property 'address_definition' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty",
        jsii_struct_bases=[],
        name_mapping={
            "revoked_status_action": "revokedStatusAction",
            "unknown_status_action": "unknownStatusAction",
        },
    )
    class CheckCertificateRevocationStatusProperty:
        def __init__(
            self,
            *,
            revoked_status_action: typing.Optional[builtins.str] = None,
            unknown_status_action: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When enabled, Network Firewall checks if the server certificate presented by the server in the SSL/TLS connection has a revoked or unkown status.

            If the certificate has an unknown or revoked status, you must specify the actions that Network Firewall takes on outbound traffic. To check the certificate revocation status, you must also specify a ``CertificateAuthorityArn`` in `ServerCertificateConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-servercertificateconfiguration.html>`_ .

            :param revoked_status_action: Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has a revoked status. - *PASS* - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection. - *DROP* - Network Firewall closes the connection and drops subsequent packets for that connection. - *REJECT* - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. ``REJECT`` is available only for TCP traffic.
            :param unknown_status_action: Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has an unknown status, or a status that cannot be determined for any other reason, including when the service is unable to connect to the OCSP and CRL endpoints for the certificate. - *PASS* - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection. - *DROP* - Network Firewall closes the connection and drops subsequent packets for that connection. - *REJECT* - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. ``REJECT`` is available only for TCP traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                check_certificate_revocation_status_property = networkfirewall.CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty(
                    revoked_status_action="revokedStatusAction",
                    unknown_status_action="unknownStatusAction"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1916be67886f4be6d0d11a69d9af9613d73f21c4fc6c61a438fed4e7fe9f5ffb)
                check_type(argname="argument revoked_status_action", value=revoked_status_action, expected_type=type_hints["revoked_status_action"])
                check_type(argname="argument unknown_status_action", value=unknown_status_action, expected_type=type_hints["unknown_status_action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if revoked_status_action is not None:
                self._values["revoked_status_action"] = revoked_status_action
            if unknown_status_action is not None:
                self._values["unknown_status_action"] = unknown_status_action

        @builtins.property
        def revoked_status_action(self) -> typing.Optional[builtins.str]:
            '''Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has a revoked status.

            - *PASS* - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.
            - *DROP* - Network Firewall closes the connection and drops subsequent packets for that connection.
            - *REJECT* - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. ``REJECT`` is available only for TCP traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus.html#cfn-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-revokedstatusaction
            '''
            result = self._values.get("revoked_status_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unknown_status_action(self) -> typing.Optional[builtins.str]:
            '''Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has an unknown status, or a status that cannot be determined for any other reason, including when the service is unable to connect to the OCSP and CRL endpoints for the certificate.

            - *PASS* - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.
            - *DROP* - Network Firewall closes the connection and drops subsequent packets for that connection.
            - *REJECT* - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. ``REJECT`` is available only for TCP traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus.html#cfn-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-unknownstatusaction
            '''
            result = self._values.get("unknown_status_action")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CheckCertificateRevocationStatusProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"from_port": "fromPort", "to_port": "toPort"},
    )
    class PortRangeProperty:
        def __init__(self, *, from_port: jsii.Number, to_port: jsii.Number) -> None:
            '''A single port range specification.

            This is used for source and destination port ranges in the stateless rule `MatchAttributes <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html>`_ , ``SourcePorts`` , and ``DestinationPorts`` settings.

            :param from_port: The lower limit of the port range. This must be less than or equal to the ``ToPort`` specification.
            :param to_port: The upper limit of the port range. This must be greater than or equal to the ``FromPort`` specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-portrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                port_range_property = networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                    from_port=123,
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e52a2ce05e8338187aa2dadcb1c9262256663ce3216a2ec64fc97360f74bd260)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''The lower limit of the port range.

            This must be less than or equal to the ``ToPort`` specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-portrange.html#cfn-networkfirewall-tlsinspectionconfiguration-portrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''The upper limit of the port range.

            This must be greater than or equal to the ``FromPort`` specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-portrange.html#cfn-networkfirewall-tlsinspectionconfiguration-portrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_authority_arn": "certificateAuthorityArn",
            "check_certificate_revocation_status": "checkCertificateRevocationStatus",
            "scopes": "scopes",
            "server_certificates": "serverCertificates",
        },
    )
    class ServerCertificateConfigurationProperty:
        def __init__(
            self,
            *,
            certificate_authority_arn: typing.Optional[builtins.str] = None,
            check_certificate_revocation_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scopes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.ServerCertificateScopeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            server_certificates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.ServerCertificateProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configures the AWS Certificate Manager certificates and scope that Network Firewall uses to decrypt and re-encrypt traffic using a `TLSInspectionConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html>`_ . You can configure ``ServerCertificates`` for inbound SSL/TLS inspection, a ``CertificateAuthorityArn`` for outbound SSL/TLS inspection, or both. For information about working with certificates for TLS inspection, see `Using SSL/TLS server certficiates with TLS inspection configurations <https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html>`_ in the *AWS Network Firewall Developer Guide* .

            .. epigraph::

               If a server certificate that's associated with your `TLSInspectionConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html>`_ is revoked, deleted, or expired it can result in client-side TLS errors.

            :param certificate_authority_arn: The Amazon Resource Name (ARN) of the imported certificate authority (CA) certificate within AWS Certificate Manager (ACM) to use for outbound SSL/TLS inspection. The following limitations apply: - You can use CA certificates that you imported into ACM, but you can't generate CA certificates with ACM. - You can't use certificates issued by AWS Private Certificate Authority . For more information about configuring certificates for outbound inspection, see `Using SSL/TLS certificates with certificates with TLS inspection configurations <https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html>`_ in the *AWS Network Firewall Developer Guide* . For information about working with certificates in ACM, see `Importing certificates <https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`_ in the *AWS Certificate Manager User Guide* .
            :param check_certificate_revocation_status: When enabled, Network Firewall checks if the server certificate presented by the server in the SSL/TLS connection has a revoked or unkown status. If the certificate has an unknown or revoked status, you must specify the actions that Network Firewall takes on outbound traffic. To check the certificate revocation status, you must also specify a ``CertificateAuthorityArn`` in `ServerCertificateConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-servercertificateconfiguration.html>`_ .
            :param scopes: A list of scopes.
            :param server_certificates: The list of server certificates to use for inbound SSL/TLS inspection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                server_certificate_configuration_property = networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty(
                    certificate_authority_arn="certificateAuthorityArn",
                    check_certificate_revocation_status=networkfirewall.CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty(
                        revoked_status_action="revokedStatusAction",
                        unknown_status_action="unknownStatusAction"
                    ),
                    scopes=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateScopeProperty(
                        destination_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                            from_port=123,
                            to_port=123
                        )],
                        destinations=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                            address_definition="addressDefinition"
                        )],
                        protocols=[123],
                        source_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                            from_port=123,
                            to_port=123
                        )],
                        sources=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                            address_definition="addressDefinition"
                        )]
                    )],
                    server_certificates=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateProperty(
                        resource_arn="resourceArn"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce24f66a34f9353756eb260c3b8a624c61eebacf13d607b9d31ec38666c435d0)
                check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
                check_type(argname="argument check_certificate_revocation_status", value=check_certificate_revocation_status, expected_type=type_hints["check_certificate_revocation_status"])
                check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
                check_type(argname="argument server_certificates", value=server_certificates, expected_type=type_hints["server_certificates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_authority_arn is not None:
                self._values["certificate_authority_arn"] = certificate_authority_arn
            if check_certificate_revocation_status is not None:
                self._values["check_certificate_revocation_status"] = check_certificate_revocation_status
            if scopes is not None:
                self._values["scopes"] = scopes
            if server_certificates is not None:
                self._values["server_certificates"] = server_certificates

        @builtins.property
        def certificate_authority_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the imported certificate authority (CA) certificate within AWS Certificate Manager (ACM) to use for outbound SSL/TLS inspection.

            The following limitations apply:

            - You can use CA certificates that you imported into ACM, but you can't generate CA certificates with ACM.
            - You can't use certificates issued by AWS Private Certificate Authority .

            For more information about configuring certificates for outbound inspection, see `Using SSL/TLS certificates with certificates with TLS inspection configurations <https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html>`_ in the *AWS Network Firewall Developer Guide* .

            For information about working with certificates in ACM, see `Importing certificates <https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`_ in the *AWS Certificate Manager User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-certificateauthorityarn
            '''
            result = self._values.get("certificate_authority_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def check_certificate_revocation_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty"]]:
            '''When enabled, Network Firewall checks if the server certificate presented by the server in the SSL/TLS connection has a revoked or unkown status.

            If the certificate has an unknown or revoked status, you must specify the actions that Network Firewall takes on outbound traffic. To check the certificate revocation status, you must also specify a ``CertificateAuthorityArn`` in `ServerCertificateConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-servercertificateconfiguration.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-checkcertificaterevocationstatus
            '''
            result = self._values.get("check_certificate_revocation_status")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty"]], result)

        @builtins.property
        def scopes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.ServerCertificateScopeProperty"]]]]:
            '''A list of scopes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-scopes
            '''
            result = self._values.get("scopes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.ServerCertificateScopeProperty"]]]], result)

        @builtins.property
        def server_certificates(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.ServerCertificateProperty"]]]]:
            '''The list of server certificates to use for inbound SSL/TLS inspection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-servercertificates
            '''
            result = self._values.get("server_certificates")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.ServerCertificateProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerCertificateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class ServerCertificateProperty:
        def __init__(
            self,
            *,
            resource_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Any AWS Certificate Manager (ACM) Secure Sockets Layer/Transport Layer Security (SSL/TLS) server certificate that's associated with a `ServerCertificateConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html>`_ . Used in a `TLSInspectionConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html>`_ for inspection of inbound traffic to your firewall. You must request or import a SSL/TLS certificate into ACM for each domain Network Firewall needs to decrypt and inspect. AWS Network Firewall uses the SSL/TLS certificates to decrypt specified inbound SSL/TLS traffic going to your firewall. For information about working with certificates in AWS Certificate Manager , see `Request a public certificate <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html>`_ or `Importing certificates <https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`_ in the *AWS Certificate Manager User Guide* .

            :param resource_arn: The Amazon Resource Name (ARN) of the AWS Certificate Manager SSL/TLS server certificate that's used for inbound SSL/TLS inspection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                server_certificate_property = networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1736b147376470701ba360dfaa711c9d5e294d7332704eac60cd65918d448064)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if resource_arn is not None:
                self._values["resource_arn"] = resource_arn

        @builtins.property
        def resource_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the AWS Certificate Manager SSL/TLS server certificate that's used for inbound SSL/TLS inspection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificate-resourcearn
            '''
            result = self._values.get("resource_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateScopeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_ports": "destinationPorts",
            "destinations": "destinations",
            "protocols": "protocols",
            "source_ports": "sourcePorts",
            "sources": "sources",
        },
    )
    class ServerCertificateScopeProperty:
        def __init__(
            self,
            *,
            destination_ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.PortRangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.AddressProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            protocols: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            source_ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.PortRangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.AddressProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Settings that define the Secure Sockets Layer/Transport Layer Security (SSL/TLS) traffic that Network Firewall should decrypt for inspection by the stateful rule engine.

            :param destination_ports: The destination ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any destination port. You can specify individual ports, for example ``1994`` , and you can specify port ranges, such as ``1990:1994`` .
            :param destinations: The destination IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any destination address.
            :param protocols: The protocols to decrypt for inspection, specified using each protocol's assigned internet protocol number (IANA). Network Firewall currently supports only TCP.
            :param source_ports: The source ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any source port. You can specify individual ports, for example ``1994`` , and you can specify port ranges, such as ``1990:1994`` .
            :param sources: The source IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any source address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                server_certificate_scope_property = networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateScopeProperty(
                    destination_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                        from_port=123,
                        to_port=123
                    )],
                    destinations=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                        address_definition="addressDefinition"
                    )],
                    protocols=[123],
                    source_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                        from_port=123,
                        to_port=123
                    )],
                    sources=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                        address_definition="addressDefinition"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b5b8bcea69a86e77bb55889c9fc36d4e4fe07b98f5188185a383349870221ac)
                check_type(argname="argument destination_ports", value=destination_ports, expected_type=type_hints["destination_ports"])
                check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
                check_type(argname="argument protocols", value=protocols, expected_type=type_hints["protocols"])
                check_type(argname="argument source_ports", value=source_ports, expected_type=type_hints["source_ports"])
                check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_ports is not None:
                self._values["destination_ports"] = destination_ports
            if destinations is not None:
                self._values["destinations"] = destinations
            if protocols is not None:
                self._values["protocols"] = protocols
            if source_ports is not None:
                self._values["source_ports"] = source_ports
            if sources is not None:
                self._values["sources"] = sources

        @builtins.property
        def destination_ports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.PortRangeProperty"]]]]:
            '''The destination ports to decrypt for inspection, in Transmission Control Protocol (TCP) format.

            If not specified, this matches with any destination port.

            You can specify individual ports, for example ``1994`` , and you can specify port ranges, such as ``1990:1994`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-destinationports
            '''
            result = self._values.get("destination_ports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.PortRangeProperty"]]]], result)

        @builtins.property
        def destinations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.AddressProperty"]]]]:
            '''The destination IP addresses and address ranges to decrypt for inspection, in CIDR notation.

            If not specified, this
            matches with any destination address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-destinations
            '''
            result = self._values.get("destinations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.AddressProperty"]]]], result)

        @builtins.property
        def protocols(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''The protocols to decrypt for inspection, specified using each protocol's assigned internet protocol number (IANA).

            Network Firewall currently supports only TCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-protocols
            '''
            result = self._values.get("protocols")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def source_ports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.PortRangeProperty"]]]]:
            '''The source ports to decrypt for inspection, in Transmission Control Protocol (TCP) format.

            If not specified, this matches with any source port.

            You can specify individual ports, for example ``1994`` , and you can specify port ranges, such as ``1990:1994`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-sourceports
            '''
            result = self._values.get("source_ports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.PortRangeProperty"]]]], result)

        @builtins.property
        def sources(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.AddressProperty"]]]]:
            '''The source IP addresses and address ranges to decrypt for inspection, in CIDR notation.

            If not specified, this
            matches with any source address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.html#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-sources
            '''
            result = self._values.get("sources")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.AddressProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerCertificateScopeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "server_certificate_configurations": "serverCertificateConfigurations",
        },
    )
    class TLSInspectionConfigurationProperty:
        def __init__(
            self,
            *,
            server_certificate_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The object that defines a TLS inspection configuration. This defines the TLS inspection configuration.

            AWS Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.

            To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see `Inspecting SSL/TLS traffic with TLS inspection configurations <https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html>`_ in the *AWS Network Firewall Developer Guide* .

            :param server_certificate_configurations: Lists the server certificate configurations that are associated with the TLS configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkfirewall as networkfirewall
                
                t_lSInspection_configuration_property = networkfirewall.CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty(
                    server_certificate_configurations=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty(
                        certificate_authority_arn="certificateAuthorityArn",
                        check_certificate_revocation_status=networkfirewall.CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty(
                            revoked_status_action="revokedStatusAction",
                            unknown_status_action="unknownStatusAction"
                        ),
                        scopes=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateScopeProperty(
                            destination_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                                from_port=123,
                                to_port=123
                            )],
                            destinations=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                                address_definition="addressDefinition"
                            )],
                            protocols=[123],
                            source_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                                from_port=123,
                                to_port=123
                            )],
                            sources=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                                address_definition="addressDefinition"
                            )]
                        )],
                        server_certificates=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateProperty(
                            resource_arn="resourceArn"
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4461b2c6b1b6ac70b96136818f20b2e6fc825894b0c6c6164a3b54b575e735fd)
                check_type(argname="argument server_certificate_configurations", value=server_certificate_configurations, expected_type=type_hints["server_certificate_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if server_certificate_configurations is not None:
                self._values["server_certificate_configurations"] = server_certificate_configurations

        @builtins.property
        def server_certificate_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty"]]]]:
            '''Lists the server certificate configurations that are associated with the TLS configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration-servercertificateconfigurations
            '''
            result = self._values.get("server_certificate_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TLSInspectionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkfirewall.CfnTLSInspectionConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "tls_inspection_configuration": "tlsInspectionConfiguration",
        "tls_inspection_configuration_name": "tlsInspectionConfigurationName",
        "description": "description",
        "tags": "tags",
    },
)
class CfnTLSInspectionConfigurationProps:
    def __init__(
        self,
        *,
        tls_inspection_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        tls_inspection_configuration_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTLSInspectionConfiguration``.

        :param tls_inspection_configuration: The object that defines a TLS inspection configuration. AWS Network Firewall uses TLS inspection configurations to decrypt your firewall's inbound and outbound SSL/TLS traffic. After decryption, AWS Network Firewall inspects the traffic according to your firewall policy's stateful rules, and then re-encrypts it before sending it to its destination. You can enable inspection of your firewall's inbound traffic, outbound traffic, or both. To use TLS inspection with your firewall, you must first import or provision certificates using AWS Certificate Manager , create a TLS inspection configuration, add that configuration to a new firewall policy, and then associate that policy with your firewall. For more information about using TLS inspection configurations, see `Inspecting SSL/TLS traffic with TLS inspection configurations <https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html>`_ in the *AWS Network Firewall Developer Guide* .
        :param tls_inspection_configuration_name: The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.
        :param description: A description of the TLS inspection configuration.
        :param tags: The key:value pairs to associate with the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkfirewall as networkfirewall
            
            cfn_tLSInspection_configuration_props = networkfirewall.CfnTLSInspectionConfigurationProps(
                tls_inspection_configuration=networkfirewall.CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty(
                    server_certificate_configurations=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty(
                        certificate_authority_arn="certificateAuthorityArn",
                        check_certificate_revocation_status=networkfirewall.CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty(
                            revoked_status_action="revokedStatusAction",
                            unknown_status_action="unknownStatusAction"
                        ),
                        scopes=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateScopeProperty(
                            destination_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                                from_port=123,
                                to_port=123
                            )],
                            destinations=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                                address_definition="addressDefinition"
                            )],
                            protocols=[123],
                            source_ports=[networkfirewall.CfnTLSInspectionConfiguration.PortRangeProperty(
                                from_port=123,
                                to_port=123
                            )],
                            sources=[networkfirewall.CfnTLSInspectionConfiguration.AddressProperty(
                                address_definition="addressDefinition"
                            )]
                        )],
                        server_certificates=[networkfirewall.CfnTLSInspectionConfiguration.ServerCertificateProperty(
                            resource_arn="resourceArn"
                        )]
                    )]
                ),
                tls_inspection_configuration_name="tlsInspectionConfigurationName",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f05137012f831af07bffb09e4ece1302036a8c7c23718d26dcb08f4bfdfd66e9)
            check_type(argname="argument tls_inspection_configuration", value=tls_inspection_configuration, expected_type=type_hints["tls_inspection_configuration"])
            check_type(argname="argument tls_inspection_configuration_name", value=tls_inspection_configuration_name, expected_type=type_hints["tls_inspection_configuration_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tls_inspection_configuration": tls_inspection_configuration,
            "tls_inspection_configuration_name": tls_inspection_configuration_name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def tls_inspection_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty]:
        '''The object that defines a TLS inspection configuration.

        AWS Network Firewall uses TLS inspection configurations to decrypt your firewall's inbound and outbound SSL/TLS traffic. After decryption, AWS Network Firewall inspects the traffic according to your firewall policy's stateful rules, and then re-encrypts it before sending it to its destination. You can enable inspection of your firewall's inbound traffic, outbound traffic, or both. To use TLS inspection with your firewall, you must first import or provision certificates using AWS Certificate Manager , create a TLS inspection configuration, add that configuration to a new firewall policy, and then associate that policy with your firewall. For more information about using TLS inspection configurations, see `Inspecting SSL/TLS traffic with TLS inspection configurations <https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html>`_ in the *AWS Network Firewall Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration
        '''
        result = self._values.get("tls_inspection_configuration")
        assert result is not None, "Required property 'tls_inspection_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty], result)

    @builtins.property
    def tls_inspection_configuration_name(self) -> builtins.str:
        '''The descriptive name of the TLS inspection configuration.

        You can't change the name of a TLS inspection configuration after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfigurationname
        '''
        result = self._values.get("tls_inspection_configuration_name")
        assert result is not None, "Required property 'tls_inspection_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the TLS inspection configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The key:value pairs to associate with the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html#cfn-networkfirewall-tlsinspectionconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTLSInspectionConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFirewall",
    "CfnFirewallPolicy",
    "CfnFirewallPolicyProps",
    "CfnFirewallProps",
    "CfnLoggingConfiguration",
    "CfnLoggingConfigurationProps",
    "CfnRuleGroup",
    "CfnRuleGroupProps",
    "CfnTLSInspectionConfiguration",
    "CfnTLSInspectionConfigurationProps",
]

publication.publish()

def _typecheckingstub__8735e4ce7e79159823190ad059af802b7721b71930c6b4b8805c4676b38d4d56(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    firewall_name: builtins.str,
    firewall_policy_arn: builtins.str,
    subnet_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewall.SubnetMappingProperty, typing.Dict[builtins.str, typing.Any]]]]],
    vpc_id: builtins.str,
    delete_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    firewall_policy_change_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    subnet_change_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c4e2793da1cf8bea450c2122d2557d378fad5e129ebb26f114a36cfc6506a2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46677a58d997dd59fd033c9a9ee94e3689cafff9e028d3e2d162ddfeee718547(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdb28f607bba18f9f1db46f554b41c7ddfaaf01fe3c74c5f99726bd72458a115(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c711ef7af7567ab69b12f083b26c4033f7cdf1593bf27227f989d7c73e8c9fc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2f1e41c3294b6f9ed43f3936b8feb28ed4bd73021f059aae4743db717241ab(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFirewall.SubnetMappingProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba092b3d0c9ca8819ad31fd4320cebdee3150a45603af80de70f2c0bbb9e04b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d69795554b50f9f4f46a0470d9cf06e4d826d030dcab9f0adfc3a3d566c8b3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea0349bbbe56acfbf8d2e11ce10cdd2221eb418df0a6df3602174f8015ca4f6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee50239d13ab311a798770d372dccb418872f67c3e07c873f5d87e11df129a35(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3edeae6cf81be7cb1d87c21080d7c060fb1fdbd872b4292af576701d514ade47(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1b2b141c4b9a04d63365f9d8a2a5636d417c4a087ebfbfd40be7336d4d258da(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf86d50b8eec902ee512afbe0dfd3b1ee2bc8f0b9f4fb9acb4ac637ae3662fc0(
    *,
    subnet_id: builtins.str,
    ip_address_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88babb6ad6946bc506d4761908231f5bd58eca8a4b6bc16dfccccad329a61ca(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    firewall_policy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.FirewallPolicyProperty, typing.Dict[builtins.str, typing.Any]]],
    firewall_policy_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5c5132a5b6e646e64fbde7a0f144884b26ad6646fb61ce294ea7f055ebdea9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56698f8e6b1c138a730626856a3d169be448aa17fd1614293c276d6b465f45a2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__706340078bfabf1ab4df2417fc17af1521f1718330cb1fc0087bd9afbac6b09e(
    value: typing.Union[_IResolvable_da3f097b, CfnFirewallPolicy.FirewallPolicyProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c7e3a8041e7e54afea999d4d0ef02ac9ae2b07dcdf0a03eae03b540da1897f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17c32ed9aaa9f9ee7c0bc9d17e141d75109032a7a60deaf6aed2663b8c4728a3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c11c99d52a27fc2ece4bf3400c4dd843466996564051d6963ae198097626d76(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85467f041a9b94df26a26630991c0c22b625a860b01ccf1dafa4f6c431ca3d2f(
    *,
    publish_metric_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.PublishMetricActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aea5034d17a5ca042ab3479dcb09b74cc8b32425872aa94df5c552a5d6c7fa1(
    *,
    action_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.ActionDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    action_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__774d6b3d9a237f7aee33cd708631d88ea8bd3d72e6ab927132f715b75e77c5a8(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6a6014864b81482e4c4a383921c58673d84e8e882dc4fb7cea71a2db29fc18(
    *,
    stateless_default_actions: typing.Sequence[builtins.str],
    stateless_fragment_default_actions: typing.Sequence[builtins.str],
    policy_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.PolicyVariablesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stateful_default_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    stateful_engine_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.StatefulEngineOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stateful_rule_group_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.StatefulRuleGroupReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    stateless_custom_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.CustomActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    stateless_rule_group_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.StatelessRuleGroupReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tls_inspection_configuration_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d067b828f689f1f983a48f9f4eb8d06f4dfe2f2e6a20585837d5fe154bfc4ae8(
    *,
    definition: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e866a0377e767391b6cb1e114ddc7eed91f1e04c8ab4203b0af3b09a8befd47(
    *,
    rule_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.IPSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eab9540ab80b4dd980d8dda17b30755d1e15a920591be54fdd8184a0a4e4eb42(
    *,
    dimensions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69e95338d370bfb1bbb954499358a8d8914836eb171006f958c9fa4debca2e09(
    *,
    rule_order: typing.Optional[builtins.str] = None,
    stream_exception_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62be7baa7c0ae22655f34e1d3316236c114457fe368caf2a958ba1fd9578c7f4(
    *,
    action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b35f780a3045f4df1ecbf5bb69deb711659429dcfd9f87d388080942e7b17ef8(
    *,
    resource_arn: builtins.str,
    override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.StatefulRuleGroupOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    priority: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4abfbbd63f3454ea4b5597e2099b8d101919bc21b3cc73051aad275b321347ca(
    *,
    priority: jsii.Number,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2c62703239bb4479e4595613edad2d44e170db98c687d725b8c824f819e362(
    *,
    firewall_policy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallPolicy.FirewallPolicyProperty, typing.Dict[builtins.str, typing.Any]]],
    firewall_policy_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4108d5c35b1608da0d36c8bb60f52501d3b0634ca4324342a71c57bc238e99(
    *,
    firewall_name: builtins.str,
    firewall_policy_arn: builtins.str,
    subnet_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewall.SubnetMappingProperty, typing.Dict[builtins.str, typing.Any]]]]],
    vpc_id: builtins.str,
    delete_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    firewall_policy_change_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    subnet_change_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71487a7865ce1877156cecd1cb83afa7ffd5f6428fa2611a7537c9ccf8667afe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    firewall_arn: builtins.str,
    logging_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    firewall_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf1d8af41633c95dd577d7d2736c4bc7e5071ece1527fb65bc7392f72a7a43b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51b1357cb88ac7feaa787c6f1526ec7769461fd859c5b55b6f8e5caf4cf1264(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d71125ddf5ba2d377facff407ef5a2fcdbd3c618a7499d3633c68130f56adcee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6379a583f20adcddf04ea938455ca9e96ed6e0a2293ffa4b83968515494d8120(
    value: typing.Union[_IResolvable_da3f097b, CfnLoggingConfiguration.LoggingConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e3640e7313e33945bc2b7c00caa777b47e14239e160ded6a349405aeb0b47da(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b2e62cece09027ed51c224134098d51d2c868274bd4da88e455b472e9c005d(
    *,
    log_destination: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    log_destination_type: builtins.str,
    log_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7694cf2d5082b8064a259b791a222ad012a1f7bcab308d321c9d4c780c634c13(
    *,
    log_destination_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.LogDestinationConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dab36772798ea19c1d2e2f1e86d2099a88806994c157c7bd4e0d62178ab9369(
    *,
    firewall_arn: builtins.str,
    logging_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    firewall_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f1d19cebb2e7dfe2bb3a674253e22bfdb540bd48dc9cd243370420d8cec9b9e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    capacity: jsii.Number,
    rule_group_name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    rule_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.RuleGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8ef477504489cc901fa58c5454b1728231c047d069191745b232cb839f0b97(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5174ab9f3bed2fb8464156fa8d27c8cbbb570726e4667c2ed7634ad777c961(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51c7651794925713a49400586d47fdec281f3586c00b18d62055515fd2ef2791(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23a7df76066fa7162c289f359c412bcb9765e3d5b573e0d06d7daf300d391ff3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ac4c425ad11cc87f637d21e3373819fe72741deca8ec3a39ab57b97c38a2e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c85f5fc86d4cd20434a5458984123db8b76ff5d649d26af8be38c56af6a7b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ed6ac96ae6360b92bfdf6614d9832ba1cad5080dce3a3257a75537c93626bb1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRuleGroup.RuleGroupProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5969fe74fc1a24641d71678e96d3133e152f5f87c43e5f7d72af22aa055d7db5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffeb7b0f0ffdb417d3ac37fe775fea2d6c40814070d270c03323517593b547b9(
    *,
    publish_metric_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.PublishMetricActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6067c4ca12beed4ffa424b8e13cd23b4810ac4eca1ff16680ad9a71e7289c5(
    *,
    address_definition: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__776dc4a2267643558107c479367987cde061715c1a5e677dc3d8ad57e6bb07f7(
    *,
    action_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.ActionDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    action_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84c1411257e0aebed042d1b8352d41d7cf5b9215102a041f342d81c1abe064f3(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b333909d939962666b3db75451a84fc0fc672a45693aca0c6339237e2a577318(
    *,
    destination: builtins.str,
    destination_port: builtins.str,
    direction: builtins.str,
    protocol: builtins.str,
    source: builtins.str,
    source_port: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca53e469af4e88c4294a2b49d50c102b6e9e059bfbfa928cfefb0c899aeca0b6(
    *,
    definition: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c62ac9d27c6484f4a2b9da61680388d72bf1968a69f8864fca9a5dc2c1d420(
    *,
    reference_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90ce1a312793001f5c059c69ea601ba7bc963a51d06ab080c64c4cb1eae7671a(
    *,
    destination_ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.PortRangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.AddressProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    protocols: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
    source_ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.PortRangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.AddressProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tcp_flags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.TCPFlagFieldProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd1af803bf4604f5fe65a635655413d3719cd3b737baab39db33daf95c1ac6b(
    *,
    from_port: jsii.Number,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18f51e9866b56513a07e5af9f75eea271b0da41a1c90b0f0eb235ccaeaf6fd8(
    *,
    definition: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41a6f7b234552866dbb2f70b78c6c9311fef5d507c07747593b0b90e4a163d46(
    *,
    dimensions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3955e12e3465fd3060b82c41bb430af9d8272b881b8347a0df73c8b0293b8b00(
    *,
    ip_set_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.IPSetReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a4539cb428b880e373a3db5923e9d0f2d2f91e07045af9358db4aa1f7b47b7(
    *,
    actions: typing.Sequence[builtins.str],
    match_attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.MatchAttributesProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6031839dccab8578d6df945e603f857681f1ba43a8750c6823a4956903ee6b0a(
    *,
    rules_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.RulesSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    reference_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.ReferenceSetsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rule_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.RuleVariablesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stateful_rule_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.StatefulRuleOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f117785b5345a4a7fbef540dfb4ab49e1476bb3ee3f5b32f4bf8bdde04fa35(
    *,
    keyword: builtins.str,
    settings: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a07f3723113c8b16a34bf34741ea1461bc25f6ab3b0720f6a8aa564d1272e4ca(
    *,
    ip_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.IPSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    port_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.PortSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a485e00c504005fdc6e395458d012eb99f789685105dcedf2228712fff5a91(
    *,
    generated_rules_type: builtins.str,
    targets: typing.Sequence[builtins.str],
    target_types: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37c2f6cfa9ab89c36a10e214087cb83419a7c8be9fa0d97cb6ff5c156ec1ed2b(
    *,
    rules_source_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.RulesSourceListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rules_string: typing.Optional[builtins.str] = None,
    stateful_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.StatefulRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    stateless_rules_and_custom_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.StatelessRulesAndCustomActionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__059685e154b150834c61bccd6793a66e1d0e92258779eb937ca1fa3a1670f3c2(
    *,
    rule_order: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5bb56af25d6c8c99d593795131e22b214fd8722c9ab610ce9e26db6f72cae04(
    *,
    action: builtins.str,
    header: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.HeaderProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_options: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.RuleOptionProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8abd713c2522cea4720da70b4aa087d7eb1f6a9257d6d3a5b76148f6102fb22d(
    *,
    priority: jsii.Number,
    rule_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.RuleDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71d7a12c23bdb40d0d25319bf80720d55c4205129c386e8de5676df43ea5e61b(
    *,
    stateless_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.StatelessRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    custom_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.CustomActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__775fa1817d39168a6b1883b9e449352da902edc72fb398c55cda18aa8ead3039(
    *,
    flags: typing.Sequence[builtins.str],
    masks: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__775b93be404fbe10bf6b023b8192636307852f30e49da9892d7e20aa443ecbd0(
    *,
    capacity: jsii.Number,
    rule_group_name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    rule_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuleGroup.RuleGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec764b679fc98c8fe3aa11d807ebebdd11b5c6a99f92f8eb7c03b663e2ff6773(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    tls_inspection_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    tls_inspection_configuration_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fffc8d2cddb56be0caa1d022a327faef26e9d6137d82bda779515250e3fcff9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fba06f46a5cea5a67cd0374f887b8225a08a147db2a073ffe9bc73c588b4887(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0caa3698092eac04f0f3cb6ef31ee8a37b5620e7b43e83135c822e030a956e5(
    value: typing.Union[_IResolvable_da3f097b, CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc056f1763c9b07511c09bccb7850663b8f285be14ee1f3cb521a402d621782f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a315bf64b464c871474cdb7416d97974a1f1ecea9dca5b529ccb217aa9b8bdbc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1705dcb0cd17e874ce96cef7a6499dffda595fe61408ae3b8537babc4ea07e7d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d082db2e4a682d2415b7a09e26862470d9c413df2a8e84b76f381e13039916b(
    *,
    address_definition: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1916be67886f4be6d0d11a69d9af9613d73f21c4fc6c61a438fed4e7fe9f5ffb(
    *,
    revoked_status_action: typing.Optional[builtins.str] = None,
    unknown_status_action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e52a2ce05e8338187aa2dadcb1c9262256663ce3216a2ec64fc97360f74bd260(
    *,
    from_port: jsii.Number,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce24f66a34f9353756eb260c3b8a624c61eebacf13d607b9d31ec38666c435d0(
    *,
    certificate_authority_arn: typing.Optional[builtins.str] = None,
    check_certificate_revocation_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.CheckCertificateRevocationStatusProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scopes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.ServerCertificateScopeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    server_certificates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.ServerCertificateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1736b147376470701ba360dfaa711c9d5e294d7332704eac60cd65918d448064(
    *,
    resource_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5b8bcea69a86e77bb55889c9fc36d4e4fe07b98f5188185a383349870221ac(
    *,
    destination_ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.PortRangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.AddressProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    protocols: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
    source_ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.PortRangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.AddressProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4461b2c6b1b6ac70b96136818f20b2e6fc825894b0c6c6164a3b54b575e735fd(
    *,
    server_certificate_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.ServerCertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f05137012f831af07bffb09e4ece1302036a8c7c23718d26dcb08f4bfdfd66e9(
    *,
    tls_inspection_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTLSInspectionConfiguration.TLSInspectionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    tls_inspection_configuration_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
