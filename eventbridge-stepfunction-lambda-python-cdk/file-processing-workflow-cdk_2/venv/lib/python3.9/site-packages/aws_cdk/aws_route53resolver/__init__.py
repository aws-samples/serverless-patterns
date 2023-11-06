'''
# Amazon Route53 Resolver Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_route53resolver as route53resolver
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Route53Resolver construct libraries](https://constructs.dev/search?q=route53resolver)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Route53Resolver resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53Resolver.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-route53resolver-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Route53Resolver](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53Resolver.html).

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
class CfnFirewallDomainList(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnFirewallDomainList",
):
    '''High-level information about a list of firewall domains for use in a `AWS::Route53Resolver::FirewallRule <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-rule.html>`_ . This is returned by `GetFirewallDomainList <https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallDomainList.html>`_ .

    To retrieve the domains that are defined for this domain list, call `ListFirewallDomains <https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallDomains.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_firewall_domain_list = route53resolver.CfnFirewallDomainList(self, "MyCfnFirewallDomainList",
            domain_file_url="domainFileUrl",
            domains=["domains"],
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
        domain_file_url: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_file_url: The fully qualified URL or URI of the file stored in Amazon Simple Storage Service (Amazon S3) that contains the list of domains to import. The file must be in an S3 bucket that's in the same Region as your DNS Firewall. The file must be a text file and must contain a single domain per line.
        :param domains: A list of the domain lists that you have defined.
        :param name: The name of the domain list.
        :param tags: A list of the tag keys and values that you want to associate with the domain list.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc007bdf474ff9b47656099203906368c5f49f4d31157c1bdf719174d13ca40)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFirewallDomainListProps(
            domain_file_url=domain_file_url, domains=domains, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2405f17a30b66b6ef7aa547ea3c9aaa5c2a71fbbd629b379f60d5c8bb77b12)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f70bcca1229db1f0e43a5ddacf558806ab81c69674e0c6071a249f5a17277467)
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
        '''The Amazon Resource Name (ARN) of the firewall domain list.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The date and time that the domain list was created, in Unix time format and Coordinated Universal Time (UTC).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatorRequestId")
    def attr_creator_request_id(self) -> builtins.str:
        '''A unique string defined by you to identify the request.

        This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.

        :cloudformationAttribute: CreatorRequestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatorRequestId"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainCount")
    def attr_domain_count(self) -> jsii.Number:
        '''The number of domain names that are specified in the domain list.

        :cloudformationAttribute: DomainCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDomainCount"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the domain list.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrManagedOwnerName")
    def attr_managed_owner_name(self) -> builtins.str:
        '''The owner of the list, used only for lists that are not managed by you.

        For example, the managed domain list ``AWSManagedDomainsMalwareDomainList`` has the managed owner name ``Route 53 Resolver DNS Firewall`` .

        :cloudformationAttribute: ManagedOwnerName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagedOwnerName"))

    @builtins.property
    @jsii.member(jsii_name="attrModificationTime")
    def attr_modification_time(self) -> builtins.str:
        '''The date and time that the domain list was last modified, in Unix time format and Coordinated Universal Time (UTC).

        :cloudformationAttribute: ModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the domain list.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''Additional information about the status of the list, if available.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

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
    @jsii.member(jsii_name="domainFileUrl")
    def domain_file_url(self) -> typing.Optional[builtins.str]:
        '''The fully qualified URL or URI of the file stored in Amazon Simple Storage Service (Amazon S3) that contains the list of domains to import.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainFileUrl"))

    @domain_file_url.setter
    def domain_file_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7accf6059d36236bce36e86dfe63d1ed53f3a65d7ea53742399c9759352e0cae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainFileUrl", value)

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the domain lists that you have defined.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domains"))

    @domains.setter
    def domains(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b87817a90afaf5311ea389ff3c45a6853527be9808e40cce2f6cfc19305941)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domains", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain list.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8645f4358aa1d05bc91526dd122ba90e9cde2f5b7544ed3b380aa0eb87ab69d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of the tag keys and values that you want to associate with the domain list.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f30863ebcd73dd0ef970d69c195c961c38e90666b69b852fe97a3c6de8aa245d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnFirewallDomainListProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_file_url": "domainFileUrl",
        "domains": "domains",
        "name": "name",
        "tags": "tags",
    },
)
class CfnFirewallDomainListProps:
    def __init__(
        self,
        *,
        domain_file_url: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFirewallDomainList``.

        :param domain_file_url: The fully qualified URL or URI of the file stored in Amazon Simple Storage Service (Amazon S3) that contains the list of domains to import. The file must be in an S3 bucket that's in the same Region as your DNS Firewall. The file must be a text file and must contain a single domain per line.
        :param domains: A list of the domain lists that you have defined.
        :param name: The name of the domain list.
        :param tags: A list of the tag keys and values that you want to associate with the domain list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_firewall_domain_list_props = route53resolver.CfnFirewallDomainListProps(
                domain_file_url="domainFileUrl",
                domains=["domains"],
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cf9cc65cbfb33602e70ad9026e1edbeb5f1b4164b0394d3cfdce7740e405780)
            check_type(argname="argument domain_file_url", value=domain_file_url, expected_type=type_hints["domain_file_url"])
            check_type(argname="argument domains", value=domains, expected_type=type_hints["domains"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if domain_file_url is not None:
            self._values["domain_file_url"] = domain_file_url
        if domains is not None:
            self._values["domains"] = domains
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_file_url(self) -> typing.Optional[builtins.str]:
        '''The fully qualified URL or URI of the file stored in Amazon Simple Storage Service (Amazon S3) that contains the list of domains to import.

        The file must be in an S3 bucket that's in the same Region as your DNS Firewall. The file must be a text file and must contain a single domain per line.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domainfileurl
        '''
        result = self._values.get("domain_file_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the domain lists that you have defined.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domains
        '''
        result = self._values.get("domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of the tag keys and values that you want to associate with the domain list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallDomainListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFirewallRuleGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnFirewallRuleGroup",
):
    '''High-level information for a firewall rule group.

    A firewall rule group is a collection of rules that DNS Firewall uses to filter DNS network traffic for a VPC. To retrieve the rules for the rule group, call `ListFirewallRules <https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRules.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_firewall_rule_group = route53resolver.CfnFirewallRuleGroup(self, "MyCfnFirewallRuleGroup",
            firewall_rules=[route53resolver.CfnFirewallRuleGroup.FirewallRuleProperty(
                action="action",
                firewall_domain_list_id="firewallDomainListId",
                priority=123,
        
                # the properties below are optional
                block_override_dns_type="blockOverrideDnsType",
                block_override_domain="blockOverrideDomain",
                block_override_ttl=123,
                block_response="blockResponse"
            )],
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
        firewall_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFirewallRuleGroup.FirewallRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param firewall_rules: A list of the rules that you have defined.
        :param name: The name of the rule group.
        :param tags: A list of the tag keys and values that you want to associate with the rule group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9746be8e0b121eabecb18d7b9ae1bc9af428e5cc8d783e461c9320d06c8fc0e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFirewallRuleGroupProps(
            firewall_rules=firewall_rules, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea942bf9103d2894a7ad703494b0079059be2da97aa2ac442ccd1f4c2637788a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__352836508cb4a234dce9db067a4a6b16892d2992b535ab5789a8b26510d33298)
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
        '''The ARN (Amazon Resource Name) of the rule group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The date and time that the rule group was created, in Unix time format and Coordinated Universal Time (UTC).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatorRequestId")
    def attr_creator_request_id(self) -> builtins.str:
        '''A unique string defined by you to identify the request.

        This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.

        :cloudformationAttribute: CreatorRequestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatorRequestId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the rule group.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrModificationTime")
    def attr_modification_time(self) -> builtins.str:
        '''The date and time that the rule group was last modified, in Unix time format and Coordinated Universal Time (UTC).

        :cloudformationAttribute: ModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''The AWS account ID for the account that created the rule group.

        When a rule group is shared with your account, this is the account that has shared the rule group with you.

        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleCount")
    def attr_rule_count(self) -> jsii.Number:
        '''The number of rules in the rule group.

        :cloudformationAttribute: RuleCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRuleCount"))

    @builtins.property
    @jsii.member(jsii_name="attrShareStatus")
    def attr_share_status(self) -> builtins.str:
        '''Whether the rule group is shared with other AWS accounts , or was shared with the current account by another AWS account .

        Sharing is configured through AWS Resource Access Manager ( AWS RAM ).

        :cloudformationAttribute: ShareStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrShareStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the domain list.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''Additional information about the status of the rule group, if available.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

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
    @jsii.member(jsii_name="firewallRules")
    def firewall_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallRuleGroup.FirewallRuleProperty"]]]]:
        '''A list of the rules that you have defined.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallRuleGroup.FirewallRuleProperty"]]]], jsii.get(self, "firewallRules"))

    @firewall_rules.setter
    def firewall_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFirewallRuleGroup.FirewallRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4982ed4db0c8f64d957d86baded56ef341d967caa88d8b33ffd869caf06121bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallRules", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f12316eeee008a57ff409a2d0928e62d72782a14a490f01a676f1ec1bcbfaec7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of the tag keys and values that you want to associate with the rule group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e88161bfa870a62d2b106ff0d76bb87c2d573da805d7d6852d0dff9534955a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53resolver.CfnFirewallRuleGroup.FirewallRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "firewall_domain_list_id": "firewallDomainListId",
            "priority": "priority",
            "block_override_dns_type": "blockOverrideDnsType",
            "block_override_domain": "blockOverrideDomain",
            "block_override_ttl": "blockOverrideTtl",
            "block_response": "blockResponse",
        },
    )
    class FirewallRuleProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            firewall_domain_list_id: builtins.str,
            priority: jsii.Number,
            block_override_dns_type: typing.Optional[builtins.str] = None,
            block_override_domain: typing.Optional[builtins.str] = None,
            block_override_ttl: typing.Optional[jsii.Number] = None,
            block_response: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A single firewall rule in a rule group.

            :param action: The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list: - ``ALLOW`` - Permit the request to go through. - ``ALERT`` - Permit the request to go through but send an alert to the logs. - ``BLOCK`` - Disallow the request. If this is specified,then ``BlockResponse`` must also be specified. if ``BlockResponse`` is ``OVERRIDE`` , then all of the following ``OVERRIDE`` attributes must be specified: - ``BlockOverrideDnsType`` - ``BlockOverrideDomain`` - ``BlockOverrideTtl``
            :param firewall_domain_list_id: The ID of the domain list that's used in the rule.
            :param priority: The priority of the rule in the rule group. This value must be unique within the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.
            :param block_override_dns_type: The DNS record's type. This determines the format of the record value that you provided in ``BlockOverrideDomain`` . Used for the rule action ``BLOCK`` with a ``BlockResponse`` setting of ``OVERRIDE`` .
            :param block_override_domain: The custom DNS record to send back in response to the query. Used for the rule action ``BLOCK`` with a ``BlockResponse`` setting of ``OVERRIDE`` .
            :param block_override_ttl: The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action ``BLOCK`` with a ``BlockResponse`` setting of ``OVERRIDE`` .
            :param block_response: The way that you want DNS Firewall to block the request. Used for the rule action setting ``BLOCK`` . - ``NODATA`` - Respond indicating that the query was successful, but no response is available for it. - ``NXDOMAIN`` - Respond indicating that the domain name that's in the query doesn't exist. - ``OVERRIDE`` - Provide a custom override in the response. This option requires custom handling details in the rule's ``BlockOverride*`` settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53resolver as route53resolver
                
                firewall_rule_property = route53resolver.CfnFirewallRuleGroup.FirewallRuleProperty(
                    action="action",
                    firewall_domain_list_id="firewallDomainListId",
                    priority=123,
                
                    # the properties below are optional
                    block_override_dns_type="blockOverrideDnsType",
                    block_override_domain="blockOverrideDomain",
                    block_override_ttl=123,
                    block_response="blockResponse"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__61f0f7aa6db62533b4486bd58a4692d76a133c14cd2281a8ea8e083c9d952e92)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument firewall_domain_list_id", value=firewall_domain_list_id, expected_type=type_hints["firewall_domain_list_id"])
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument block_override_dns_type", value=block_override_dns_type, expected_type=type_hints["block_override_dns_type"])
                check_type(argname="argument block_override_domain", value=block_override_domain, expected_type=type_hints["block_override_domain"])
                check_type(argname="argument block_override_ttl", value=block_override_ttl, expected_type=type_hints["block_override_ttl"])
                check_type(argname="argument block_response", value=block_response, expected_type=type_hints["block_response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "firewall_domain_list_id": firewall_domain_list_id,
                "priority": priority,
            }
            if block_override_dns_type is not None:
                self._values["block_override_dns_type"] = block_override_dns_type
            if block_override_domain is not None:
                self._values["block_override_domain"] = block_override_domain
            if block_override_ttl is not None:
                self._values["block_override_ttl"] = block_override_ttl
            if block_response is not None:
                self._values["block_response"] = block_response

        @builtins.property
        def action(self) -> builtins.str:
            '''The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list:  - ``ALLOW`` - Permit the request to go through.

            - ``ALERT`` - Permit the request to go through but send an alert to the logs.
            - ``BLOCK`` - Disallow the request. If this is specified,then ``BlockResponse`` must also be specified.

            if ``BlockResponse`` is ``OVERRIDE`` , then all of the following ``OVERRIDE`` attributes must be specified:

            - ``BlockOverrideDnsType``
            - ``BlockOverrideDomain``
            - ``BlockOverrideTtl``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def firewall_domain_list_id(self) -> builtins.str:
            '''The ID of the domain list that's used in the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainlistid
            '''
            result = self._values.get("firewall_domain_list_id")
            assert result is not None, "Required property 'firewall_domain_list_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def priority(self) -> jsii.Number:
            '''The priority of the rule in the rule group.

            This value must be unique within the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def block_override_dns_type(self) -> typing.Optional[builtins.str]:
            '''The DNS record's type.

            This determines the format of the record value that you provided in ``BlockOverrideDomain`` . Used for the rule action ``BLOCK`` with a ``BlockResponse`` setting of ``OVERRIDE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridednstype
            '''
            result = self._values.get("block_override_dns_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def block_override_domain(self) -> typing.Optional[builtins.str]:
            '''The custom DNS record to send back in response to the query.

            Used for the rule action ``BLOCK`` with a ``BlockResponse`` setting of ``OVERRIDE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridedomain
            '''
            result = self._values.get("block_override_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def block_override_ttl(self) -> typing.Optional[jsii.Number]:
            '''The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record.

            Used for the rule action ``BLOCK`` with a ``BlockResponse`` setting of ``OVERRIDE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridettl
            '''
            result = self._values.get("block_override_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def block_response(self) -> typing.Optional[builtins.str]:
            '''The way that you want DNS Firewall to block the request. Used for the rule action setting ``BLOCK`` .

            - ``NODATA`` - Respond indicating that the query was successful, but no response is available for it.
            - ``NXDOMAIN`` - Respond indicating that the domain name that's in the query doesn't exist.
            - ``OVERRIDE`` - Provide a custom override in the response. This option requires custom handling details in the rule's ``BlockOverride*`` settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockresponse
            '''
            result = self._values.get("block_response")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirewallRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFirewallRuleGroupAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnFirewallRuleGroupAssociation",
):
    '''An association between a firewall rule group and a VPC, which enables DNS filtering for the VPC.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_firewall_rule_group_association = route53resolver.CfnFirewallRuleGroupAssociation(self, "MyCfnFirewallRuleGroupAssociation",
            firewall_rule_group_id="firewallRuleGroupId",
            priority=123,
            vpc_id="vpcId",
        
            # the properties below are optional
            mutation_protection="mutationProtection",
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
        firewall_rule_group_id: builtins.str,
        priority: jsii.Number,
        vpc_id: builtins.str,
        mutation_protection: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param firewall_rule_group_id: The unique identifier of the firewall rule group.
        :param priority: The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 101, 200, and so on. You can change the priority setting for a rule group association after you create it. The allowed values for ``Priority`` are between 100 and 9900 (excluding 100 and 9900).
        :param vpc_id: The unique identifier of the VPC that is associated with the rule group.
        :param mutation_protection: If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.
        :param name: The name of the association.
        :param tags: A list of the tag keys and values that you want to associate with the rule group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c14109c8e9e82ef7977fee407f404276a6ffc4744fe71860c6f744a1417c11)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFirewallRuleGroupAssociationProps(
            firewall_rule_group_id=firewall_rule_group_id,
            priority=priority,
            vpc_id=vpc_id,
            mutation_protection=mutation_protection,
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb2fdbfc384a2329d8566518aa7e6dca0ba449cb6e23695e5da8d2c513888425)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56ea8836437672c68ec57924133e337a27b9fafc2d249f6546208b170785b90d)
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
        '''The Amazon Resource Name (ARN) of the firewall rule group association.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The date and time that the association was created, in Unix time format and Coordinated Universal Time (UTC).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatorRequestId")
    def attr_creator_request_id(self) -> builtins.str:
        '''A unique string defined by you to identify the request.

        This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.

        :cloudformationAttribute: CreatorRequestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatorRequestId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier for the association.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrManagedOwnerName")
    def attr_managed_owner_name(self) -> builtins.str:
        '''The owner of the association, used only for associations that are not managed by you.

        If you use AWS Firewall Manager to manage your firewallls from DNS Firewall, then this reports Firewall Manager as the managed owner.

        :cloudformationAttribute: ManagedOwnerName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagedOwnerName"))

    @builtins.property
    @jsii.member(jsii_name="attrModificationTime")
    def attr_modification_time(self) -> builtins.str:
        '''The date and time that the association was last modified, in Unix time format and Coordinated Universal Time (UTC).

        :cloudformationAttribute: ModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the association.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''Additional information about the status of the response, if available.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

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
    @jsii.member(jsii_name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> builtins.str:
        '''The unique identifier of the firewall rule group.'''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupId"))

    @firewall_rule_group_id.setter
    def firewall_rule_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81cf8ccbce652950199c4dc1d0498a06a405b1ea4f5654eb5b6bb15f011648c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallRuleGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC.'''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df379a1c86479068b208302f1f580ece307474355f5278ac695c719477ae84dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The unique identifier of the VPC that is associated with the rule group.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e2014dd57caa582ea59405600284b7af6255f792c390ea00e77e3491d8b060b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="mutationProtection")
    def mutation_protection(self) -> typing.Optional[builtins.str]:
        '''If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mutationProtection"))

    @mutation_protection.setter
    def mutation_protection(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be4d526713d68289e6792be4e80077d1ba62e05562705b2fdb43ca4018bb78b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutationProtection", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the association.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc1de518cdf5bfd11595ce5f841fb4008cc78e7e77be4df9c607f13a26d4ae6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of the tag keys and values that you want to associate with the rule group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd6a12a52fb303ead4db8087ce88b25dc5647283d9c2521b9c57f027d901a8ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnFirewallRuleGroupAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_rule_group_id": "firewallRuleGroupId",
        "priority": "priority",
        "vpc_id": "vpcId",
        "mutation_protection": "mutationProtection",
        "name": "name",
        "tags": "tags",
    },
)
class CfnFirewallRuleGroupAssociationProps:
    def __init__(
        self,
        *,
        firewall_rule_group_id: builtins.str,
        priority: jsii.Number,
        vpc_id: builtins.str,
        mutation_protection: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFirewallRuleGroupAssociation``.

        :param firewall_rule_group_id: The unique identifier of the firewall rule group.
        :param priority: The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 101, 200, and so on. You can change the priority setting for a rule group association after you create it. The allowed values for ``Priority`` are between 100 and 9900 (excluding 100 and 9900).
        :param vpc_id: The unique identifier of the VPC that is associated with the rule group.
        :param mutation_protection: If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.
        :param name: The name of the association.
        :param tags: A list of the tag keys and values that you want to associate with the rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_firewall_rule_group_association_props = route53resolver.CfnFirewallRuleGroupAssociationProps(
                firewall_rule_group_id="firewallRuleGroupId",
                priority=123,
                vpc_id="vpcId",
            
                # the properties below are optional
                mutation_protection="mutationProtection",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__715b8023408ad9032f9d4e486688e3bb6a5d34ab729223deee30ce0cd75c46e8)
            check_type(argname="argument firewall_rule_group_id", value=firewall_rule_group_id, expected_type=type_hints["firewall_rule_group_id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument mutation_protection", value=mutation_protection, expected_type=type_hints["mutation_protection"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_rule_group_id": firewall_rule_group_id,
            "priority": priority,
            "vpc_id": vpc_id,
        }
        if mutation_protection is not None:
            self._values["mutation_protection"] = mutation_protection
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firewall_rule_group_id(self) -> builtins.str:
        '''The unique identifier of the firewall rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid
        '''
        result = self._values.get("firewall_rule_group_id")
        assert result is not None, "Required property 'firewall_rule_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC.

        DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting.

        You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 101, 200, and so on. You can change the priority setting for a rule group association after you create it.

        The allowed values for ``Priority`` are between 100 and 9900 (excluding 100 and 9900).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The unique identifier of the VPC that is associated with the rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mutation_protection(self) -> typing.Optional[builtins.str]:
        '''If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-mutationprotection
        '''
        result = self._values.get("mutation_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of the tag keys and values that you want to associate with the rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallRuleGroupAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnFirewallRuleGroupProps",
    jsii_struct_bases=[],
    name_mapping={"firewall_rules": "firewallRules", "name": "name", "tags": "tags"},
)
class CfnFirewallRuleGroupProps:
    def __init__(
        self,
        *,
        firewall_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallRuleGroup.FirewallRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFirewallRuleGroup``.

        :param firewall_rules: A list of the rules that you have defined.
        :param name: The name of the rule group.
        :param tags: A list of the tag keys and values that you want to associate with the rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_firewall_rule_group_props = route53resolver.CfnFirewallRuleGroupProps(
                firewall_rules=[route53resolver.CfnFirewallRuleGroup.FirewallRuleProperty(
                    action="action",
                    firewall_domain_list_id="firewallDomainListId",
                    priority=123,
            
                    # the properties below are optional
                    block_override_dns_type="blockOverrideDnsType",
                    block_override_domain="blockOverrideDomain",
                    block_override_ttl=123,
                    block_response="blockResponse"
                )],
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b614b409c77b0163f669e1c5a722bed570fc73bbd7afce583918c9e4ee2b0436)
            check_type(argname="argument firewall_rules", value=firewall_rules, expected_type=type_hints["firewall_rules"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if firewall_rules is not None:
            self._values["firewall_rules"] = firewall_rules
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firewall_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFirewallRuleGroup.FirewallRuleProperty]]]]:
        '''A list of the rules that you have defined.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-firewallrules
        '''
        result = self._values.get("firewall_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFirewallRuleGroup.FirewallRuleProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of the tag keys and values that you want to associate with the rule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallRuleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResolverConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverConfig",
):
    '''A complex type that contains information about a Resolver configuration for a VPC.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_resolver_config = route53resolver.CfnResolverConfig(self, "MyCfnResolverConfig",
            autodefined_reverse_flag="autodefinedReverseFlag",
            resource_id="resourceId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        autodefined_reverse_flag: builtins.str,
        resource_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param autodefined_reverse_flag: Represents the desired status of ``AutodefinedReverse`` . The only supported value on creation is ``DISABLE`` . Deletion of this resource will return ``AutodefinedReverse`` to its default value of ``ENABLED`` .
        :param resource_id: The ID of the Amazon Virtual Private Cloud VPC that you're configuring Resolver for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35122d782a5f80846e3948e7eb0337b124eee2f562394f9f0ac3811b76027fa7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverConfigProps(
            autodefined_reverse_flag=autodefined_reverse_flag, resource_id=resource_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b80f7dd8c3634834446059b6a5647da70f751aee16fc635988309e2b114da8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9245311f34648ea25b101be3ffb5369952910a59e960688b54f2c2258e39669)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAutodefinedReverse")
    def attr_autodefined_reverse(self) -> builtins.str:
        '''The status of whether or not the Route 53 Resolver will create autodefined rules for reverse DNS lookups.

        This is enabled by default.

        :cloudformationAttribute: AutodefinedReverse
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAutodefinedReverse"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''ID for the Route 53 Resolver configuration.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''The owner account ID of the Amazon Virtual Private Cloud VPC.

        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="autodefinedReverseFlag")
    def autodefined_reverse_flag(self) -> builtins.str:
        '''Represents the desired status of ``AutodefinedReverse`` .'''
        return typing.cast(builtins.str, jsii.get(self, "autodefinedReverseFlag"))

    @autodefined_reverse_flag.setter
    def autodefined_reverse_flag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__450443ae6074ab44544f056831d2657be6437d1211323970c28fc56cac885b6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autodefinedReverseFlag", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        '''The ID of the Amazon Virtual Private Cloud VPC that you're configuring Resolver for.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a88dabe1b002091b3f1b20007f475ad636ceff67622ca0df695d865e58b6afee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "autodefined_reverse_flag": "autodefinedReverseFlag",
        "resource_id": "resourceId",
    },
)
class CfnResolverConfigProps:
    def __init__(
        self,
        *,
        autodefined_reverse_flag: builtins.str,
        resource_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnResolverConfig``.

        :param autodefined_reverse_flag: Represents the desired status of ``AutodefinedReverse`` . The only supported value on creation is ``DISABLE`` . Deletion of this resource will return ``AutodefinedReverse`` to its default value of ``ENABLED`` .
        :param resource_id: The ID of the Amazon Virtual Private Cloud VPC that you're configuring Resolver for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_resolver_config_props = route53resolver.CfnResolverConfigProps(
                autodefined_reverse_flag="autodefinedReverseFlag",
                resource_id="resourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e8a6715c54a3032f85efda72259aecef906caa87b4729b8c9bc48010e591ae1)
            check_type(argname="argument autodefined_reverse_flag", value=autodefined_reverse_flag, expected_type=type_hints["autodefined_reverse_flag"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "autodefined_reverse_flag": autodefined_reverse_flag,
            "resource_id": resource_id,
        }

    @builtins.property
    def autodefined_reverse_flag(self) -> builtins.str:
        '''Represents the desired status of ``AutodefinedReverse`` .

        The only supported value on creation is ``DISABLE`` . Deletion of this resource will return ``AutodefinedReverse`` to its default value of ``ENABLED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#cfn-route53resolver-resolverconfig-autodefinedreverseflag
        '''
        result = self._values.get("autodefined_reverse_flag")
        assert result is not None, "Required property 'autodefined_reverse_flag' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The ID of the Amazon Virtual Private Cloud VPC that you're configuring Resolver for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#cfn-route53resolver-resolverconfig-resourceid
        '''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResolverDNSSECConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverDNSSECConfig",
):
    '''The ``AWS::Route53Resolver::ResolverDNSSECConfig`` resource is a complex type that contains information about a configuration for DNSSEC validation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_resolver_dNSSECConfig = route53resolver.CfnResolverDNSSECConfig(self, "MyCfnResolverDNSSECConfig",
            resource_id="resourceId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_id: The ID of the virtual private cloud (VPC) that you're configuring the DNSSEC validation status for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6638caafa1a9c5bdf9ed48d3577b02e4b40b5d79f1097e2f38ee76bd54e1d00)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverDNSSECConfigProps(resource_id=resource_id)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beec86a3f946f8bba21b5baf99d30238ede31cae4cc0235cc599a7acac27a76d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__500914e8a66667918411304e05cdc48d8739533812eafaae6b25a74fff18a0bd)
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
        '''The primary identifier of this ``ResolverDNSSECConfig`` resource.

        For example: ``rdsc-689d45d1ae623bf3`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''The AWS account of the owner.

        For example: ``111122223333`` .

        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property
    @jsii.member(jsii_name="attrValidationStatus")
    def attr_validation_status(self) -> builtins.str:
        '''The current status of this ``ResolverDNSSECConfig`` resource.

        For example: ``Enabled`` .

        :cloudformationAttribute: ValidationStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrValidationStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC) that you're configuring the DNSSEC validation status for.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01500aa55167586426473b83ae123cd92339f7e27e6ca9404fe1a1196a1d0708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverDNSSECConfigProps",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId"},
)
class CfnResolverDNSSECConfigProps:
    def __init__(self, *, resource_id: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``CfnResolverDNSSECConfig``.

        :param resource_id: The ID of the virtual private cloud (VPC) that you're configuring the DNSSEC validation status for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_resolver_dNSSECConfig_props = route53resolver.CfnResolverDNSSECConfigProps(
                resource_id="resourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1d6cb497f316e5311641ff022dde6f5ae37e4e937722cbf4e49800c7dcf748)
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resource_id is not None:
            self._values["resource_id"] = resource_id

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC) that you're configuring the DNSSEC validation status for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#cfn-route53resolver-resolverdnssecconfig-resourceid
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverDNSSECConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnResolverEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverEndpoint",
):
    '''Creates a Resolver endpoint. There are two types of Resolver endpoints, inbound and outbound:.

    - An *inbound Resolver endpoint* forwards DNS queries to the DNS service for a VPC from your network.
    - An *outbound Resolver endpoint* forwards DNS queries from the DNS service for a VPC to your network.

    .. epigraph::

       - You cannot update ``ResolverEndpointType`` and ``IpAddresses`` in the same request.
       - When you update a dual-stack IP address, you must update both IP addresses. You can’t update only an IPv4 or IPv6 and keep an existing IP address.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_resolver_endpoint = route53resolver.CfnResolverEndpoint(self, "MyCfnResolverEndpoint",
            direction="direction",
            ip_addresses=[route53resolver.CfnResolverEndpoint.IpAddressRequestProperty(
                subnet_id="subnetId",
        
                # the properties below are optional
                ip="ip",
                ipv6="ipv6"
            )],
            security_group_ids=["securityGroupIds"],
        
            # the properties below are optional
            name="name",
            outpost_arn="outpostArn",
            preferred_instance_type="preferredInstanceType",
            resolver_endpoint_type="resolverEndpointType",
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
        direction: builtins.str,
        ip_addresses: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResolverEndpoint.IpAddressRequestProperty", typing.Dict[builtins.str, typing.Any]]]]],
        security_group_ids: typing.Sequence[builtins.str],
        name: typing.Optional[builtins.str] = None,
        outpost_arn: typing.Optional[builtins.str] = None,
        preferred_instance_type: typing.Optional[builtins.str] = None,
        resolver_endpoint_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param direction: Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:. - ``INBOUND`` : allows DNS queries to your VPC from your network - ``OUTBOUND`` : allows DNS queries from your VPC to your network
        :param ip_addresses: The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). The subnet ID uniquely identifies a VPC. .. epigraph:: Even though the minimum is 1, Route 53 requires that you create at least two.
        :param security_group_ids: The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound rules (for inbound endpoints) or outbound rules (for outbound endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.
        :param name: A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.
        :param outpost_arn: 
        :param preferred_instance_type: 
        :param resolver_endpoint_type: The Resolver endpoint IP address type.
        :param tags: Route 53 Resolver doesn't support updating tags through CloudFormation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08cda89b08c8f731727f875daf3a8c19a757df0fc3eddf478f27fb0918b6f59b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverEndpointProps(
            direction=direction,
            ip_addresses=ip_addresses,
            security_group_ids=security_group_ids,
            name=name,
            outpost_arn=outpost_arn,
            preferred_instance_type=preferred_instance_type,
            resolver_endpoint_type=resolver_endpoint_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a594f1c4ff5a6e919f865cddbec172bf9c70dad7f119245b693e56904c3e22)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3077592639c4d7a8ad53495b093b110bbe6949ecec62cd24403bddabcd687bea)
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
        '''The Amazon Resource Name (ARN) of the resolver endpoint, such as ``arn:aws:route53resolver:us-east-1:123456789012:resolver-endpoint/resolver-endpoint-a1bzhi`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDirection")
    def attr_direction(self) -> builtins.str:
        '''Indicates whether the resolver endpoint allows inbound or outbound DNS queries.

        :cloudformationAttribute: Direction
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDirection"))

    @builtins.property
    @jsii.member(jsii_name="attrHostVpcId")
    def attr_host_vpc_id(self) -> builtins.str:
        '''The ID of the VPC that you want to create the resolver endpoint in.

        :cloudformationAttribute: HostVPCId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostVpcId"))

    @builtins.property
    @jsii.member(jsii_name="attrIpAddressCount")
    def attr_ip_address_count(self) -> builtins.str:
        '''The number of IP addresses that the resolver endpoint can use for DNS queries.

        :cloudformationAttribute: IpAddressCount
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAddressCount"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name that you assigned to the resolver endpoint when you created the endpoint.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrOutpostArn")
    def attr_outpost_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: OutpostArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOutpostArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPreferredInstanceType")
    def attr_preferred_instance_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: PreferredInstanceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPreferredInstanceType"))

    @builtins.property
    @jsii.member(jsii_name="attrResolverEndpointId")
    def attr_resolver_endpoint_id(self) -> builtins.str:
        '''The ID of the resolver endpoint.

        :cloudformationAttribute: ResolverEndpointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverEndpointId"))

    @builtins.property
    @jsii.member(jsii_name="attrResolverEndpointType")
    def attr_resolver_endpoint_type(self) -> builtins.str:
        '''For the endpoint type you can choose either IPv4, IPv6.

        or dual-stack. A dual-stack endpoint means that it will resolve via both IPv4 and IPv6. If you choose either IPv4 or IPv6, this endpoint type is applied to all IP addresses.

        :cloudformationAttribute: ResolverEndpointType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverEndpointType"))

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
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        '''Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:.'''
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f26ad3d56070bf14ea6a442897c79a8a10930bf839dceba26c9ddfdb495eaf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResolverEndpoint.IpAddressRequestProperty"]]]:
        '''The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints).'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResolverEndpoint.IpAddressRequestProperty"]]], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResolverEndpoint.IpAddressRequestProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff067f29f23ed0518b0bcb12dad7868af652ab264fc7832f5763aa0ed2fb1a1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The ID of one or more security groups that control access to this VPC.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd40fe8701b13449c18839f0320f4f7723ee68f4abc97b40851e451655db5a80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1565ceb760deb938817958de13e27b5c61682731edf6932d20ea1ee2f895ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="outpostArn")
    def outpost_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outpostArn"))

    @outpost_arn.setter
    def outpost_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d31b571c20f15c111682add26863cca7cacc533d03d2dabb2de16fb161cd87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostArn", value)

    @builtins.property
    @jsii.member(jsii_name="preferredInstanceType")
    def preferred_instance_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredInstanceType"))

    @preferred_instance_type.setter
    def preferred_instance_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bfc22635cdaf30309d694026a7044f4f420cfb764c71a1a598838d0e309097b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredInstanceType", value)

    @builtins.property
    @jsii.member(jsii_name="resolverEndpointType")
    def resolver_endpoint_type(self) -> typing.Optional[builtins.str]:
        '''The Resolver endpoint IP address type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolverEndpointType"))

    @resolver_endpoint_type.setter
    def resolver_endpoint_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea12c0007aac9ac64aa33ecafe1e72ea50009a42185b59a7edc01f7f78ca38f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolverEndpointType", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Route 53 Resolver doesn't support updating tags through CloudFormation.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05af99e199269a9c0a481219900f7596a6eba88d314ae22816c89f9f4a219e9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverEndpoint.IpAddressRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_id": "subnetId", "ip": "ip", "ipv6": "ipv6"},
    )
    class IpAddressRequestProperty:
        def __init__(
            self,
            *,
            subnet_id: builtins.str,
            ip: typing.Optional[builtins.str] = None,
            ipv6: typing.Optional[builtins.str] = None,
        ) -> None:
            '''In a `CreateResolverEndpoint <https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html>`_ request, the IP address that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). ``IpAddressRequest`` also includes the ID of the subnet that contains the IP address.

            :param subnet_id: The ID of the subnet that contains the IP address.
            :param ip: The IPv4 address that you want to use for DNS queries.
            :param ipv6: The IPv6 address that you want to use for DNS queries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53resolver as route53resolver
                
                ip_address_request_property = route53resolver.CfnResolverEndpoint.IpAddressRequestProperty(
                    subnet_id="subnetId",
                
                    # the properties below are optional
                    ip="ip",
                    ipv6="ipv6"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d97f321837e470551bf5db7cc56a0a66e6f3735b27f4874ba4123f7e2cfbf7d8)
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
                check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
                check_type(argname="argument ipv6", value=ipv6, expected_type=type_hints["ipv6"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_id": subnet_id,
            }
            if ip is not None:
                self._values["ip"] = ip
            if ipv6 is not None:
                self._values["ipv6"] = ipv6

        @builtins.property
        def subnet_id(self) -> builtins.str:
            '''The ID of the subnet that contains the IP address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid
            '''
            result = self._values.get("subnet_id")
            assert result is not None, "Required property 'subnet_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ip(self) -> typing.Optional[builtins.str]:
            '''The IPv4 address that you want to use for DNS queries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-ip
            '''
            result = self._values.get("ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ipv6(self) -> typing.Optional[builtins.str]:
            '''The IPv6 address that you want to use for DNS queries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-ipv6
            '''
            result = self._values.get("ipv6")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpAddressRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "direction": "direction",
        "ip_addresses": "ipAddresses",
        "security_group_ids": "securityGroupIds",
        "name": "name",
        "outpost_arn": "outpostArn",
        "preferred_instance_type": "preferredInstanceType",
        "resolver_endpoint_type": "resolverEndpointType",
        "tags": "tags",
    },
)
class CfnResolverEndpointProps:
    def __init__(
        self,
        *,
        direction: builtins.str,
        ip_addresses: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolverEndpoint.IpAddressRequestProperty, typing.Dict[builtins.str, typing.Any]]]]],
        security_group_ids: typing.Sequence[builtins.str],
        name: typing.Optional[builtins.str] = None,
        outpost_arn: typing.Optional[builtins.str] = None,
        preferred_instance_type: typing.Optional[builtins.str] = None,
        resolver_endpoint_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResolverEndpoint``.

        :param direction: Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:. - ``INBOUND`` : allows DNS queries to your VPC from your network - ``OUTBOUND`` : allows DNS queries from your VPC to your network
        :param ip_addresses: The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). The subnet ID uniquely identifies a VPC. .. epigraph:: Even though the minimum is 1, Route 53 requires that you create at least two.
        :param security_group_ids: The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound rules (for inbound endpoints) or outbound rules (for outbound endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.
        :param name: A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.
        :param outpost_arn: 
        :param preferred_instance_type: 
        :param resolver_endpoint_type: The Resolver endpoint IP address type.
        :param tags: Route 53 Resolver doesn't support updating tags through CloudFormation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_resolver_endpoint_props = route53resolver.CfnResolverEndpointProps(
                direction="direction",
                ip_addresses=[route53resolver.CfnResolverEndpoint.IpAddressRequestProperty(
                    subnet_id="subnetId",
            
                    # the properties below are optional
                    ip="ip",
                    ipv6="ipv6"
                )],
                security_group_ids=["securityGroupIds"],
            
                # the properties below are optional
                name="name",
                outpost_arn="outpostArn",
                preferred_instance_type="preferredInstanceType",
                resolver_endpoint_type="resolverEndpointType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cc09ce842a854995739f051f3b593bc3ded813d2e97260dcb20f39108e8d889)
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=type_hints["ip_addresses"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument outpost_arn", value=outpost_arn, expected_type=type_hints["outpost_arn"])
            check_type(argname="argument preferred_instance_type", value=preferred_instance_type, expected_type=type_hints["preferred_instance_type"])
            check_type(argname="argument resolver_endpoint_type", value=resolver_endpoint_type, expected_type=type_hints["resolver_endpoint_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "direction": direction,
            "ip_addresses": ip_addresses,
            "security_group_ids": security_group_ids,
        }
        if name is not None:
            self._values["name"] = name
        if outpost_arn is not None:
            self._values["outpost_arn"] = outpost_arn
        if preferred_instance_type is not None:
            self._values["preferred_instance_type"] = preferred_instance_type
        if resolver_endpoint_type is not None:
            self._values["resolver_endpoint_type"] = resolver_endpoint_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def direction(self) -> builtins.str:
        '''Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:.

        - ``INBOUND`` : allows DNS queries to your VPC from your network
        - ``OUTBOUND`` : allows DNS queries from your VPC to your network

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-direction
        '''
        result = self._values.get("direction")
        assert result is not None, "Required property 'direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_addresses(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResolverEndpoint.IpAddressRequestProperty]]]:
        '''The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints).

        The subnet ID uniquely identifies a VPC.
        .. epigraph::

           Even though the minimum is 1, Route 53 requires that you create at least two.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-ipaddresses
        '''
        result = self._values.get("ip_addresses")
        assert result is not None, "Required property 'ip_addresses' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResolverEndpoint.IpAddressRequestProperty]]], result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The ID of one or more security groups that control access to this VPC.

        The security group must include one or more inbound rules (for inbound endpoints) or outbound rules (for outbound endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outpost_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-outpostarn
        '''
        result = self._values.get("outpost_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_instance_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-preferredinstancetype
        '''
        result = self._values.get("preferred_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolver_endpoint_type(self) -> typing.Optional[builtins.str]:
        '''The Resolver endpoint IP address type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-resolverendpointtype
        '''
        result = self._values.get("resolver_endpoint_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Route 53 Resolver doesn't support updating tags through CloudFormation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResolverQueryLoggingConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverQueryLoggingConfig",
):
    '''The AWS::Route53Resolver::ResolverQueryLoggingConfig resource is a complex type that contains settings for one query logging configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_resolver_query_logging_config = route53resolver.CfnResolverQueryLoggingConfig(self, "MyCfnResolverQueryLoggingConfig",
            destination_arn="destinationArn",
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_arn: The ARN of the resource that you want Resolver to send query logs: an Amazon S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
        :param name: The name of the query logging configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24f7f7cd30eb329e550fcb22ab4dcca0511ccbc9db92caea497cb901e8cab5a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverQueryLoggingConfigProps(
            destination_arn=destination_arn, name=name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceae4268e30e5118e3afcbed515bd209f19b85cac9f4879f451843942d065c2c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e64acb85fc2778ad49c6a6597c3bc955a1bd7a2c31643ee85de4e3a9a69a47f0)
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
        '''The Amazon Resource Name (ARN) for the query logging configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationCount")
    def attr_association_count(self) -> jsii.Number:
        '''The number of VPCs that are associated with the query logging configuration.

        :cloudformationAttribute: AssociationCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAssociationCount"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The date and time that the query logging configuration was created, in Unix time format and Coordinated Universal Time (UTC).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatorRequestId")
    def attr_creator_request_id(self) -> builtins.str:
        '''A unique string that identifies the request that created the query logging configuration.

        The ``CreatorRequestId`` allows failed requests to be retried without the risk of running the operation twice.

        :cloudformationAttribute: CreatorRequestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatorRequestId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID for the query logging configuration.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''The AWS account ID for the account that created the query logging configuration.

        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property
    @jsii.member(jsii_name="attrShareStatus")
    def attr_share_status(self) -> builtins.str:
        '''An indication of whether the query logging configuration is shared with other AWS account s, or was shared with the current account by another AWS account .

        Sharing is configured through AWS Resource Access Manager ( AWS RAM ).

        :cloudformationAttribute: ShareStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrShareStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the specified query logging configuration. Valid values include the following:.

        - ``CREATING`` : Resolver is creating the query logging configuration.
        - ``CREATED`` : The query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.
        - ``DELETING`` : Resolver is deleting this query logging configuration.
        - ``FAILED`` : Resolver can't deliver logs to the location that is specified in the query logging configuration. Here are two common causes:
        - The specified destination (for example, an Amazon S3 bucket) was deleted.
        - Permissions don't allow sending logs to the destination.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the resource that you want Resolver to send query logs: an Amazon S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationArn"))

    @destination_arn.setter
    def destination_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__702489df5065cd7f9b56058549807af95a48ea6a2ae2079b66359c556f8a679b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the query logging configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__619bc974053932510090c83ab6e45a2a1bce6285058cdfad4eadcaf81e211df9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.implements(_IInspectable_c2943556)
class CfnResolverQueryLoggingConfigAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverQueryLoggingConfigAssociation",
):
    '''The AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation resource is a configuration for DNS query logging.

    After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_resolver_query_logging_config_association = route53resolver.CfnResolverQueryLoggingConfigAssociation(self, "MyCfnResolverQueryLoggingConfigAssociation",
            resolver_query_log_config_id="resolverQueryLogConfigId",
            resource_id="resourceId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resolver_query_log_config_id: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resolver_query_log_config_id: The ID of the query logging configuration that a VPC is associated with.
        :param resource_id: The ID of the Amazon VPC that is associated with the query logging configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bab4a8e285b8f5bd00ec7784b85dfa36801874e1e16d9ee8e779b0fea8fba0e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverQueryLoggingConfigAssociationProps(
            resolver_query_log_config_id=resolver_query_log_config_id,
            resource_id=resource_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea9e7fa7565de1a958cab659ce5835c5ff96a12b5f22c942f50c1697a6e1bad6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7129edbb9ae2ecd48a6f3cb5630988ab69f9fa2d6b78f2d542e8beb450c91874)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The date and time that the VPC was associated with the query logging configuration, in Unix time format and Coordinated Universal Time (UTC).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrError")
    def attr_error(self) -> builtins.str:
        '''If the value of ``Status`` is ``FAILED`` , the value of ``Error`` indicates the cause:.

        - ``DESTINATION_NOT_FOUND`` : The specified destination (for example, an Amazon S3 bucket) was deleted.
        - ``ACCESS_DENIED`` : Permissions don't allow sending logs to the destination.

        If the value of ``Status`` is a value other than ``FAILED`` , ``Error`` is null.

        :cloudformationAttribute: Error
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrError"))

    @builtins.property
    @jsii.member(jsii_name="attrErrorMessage")
    def attr_error_message(self) -> builtins.str:
        '''Contains additional information about the error.

        If the value or ``Error`` is null, the value of ``ErrorMessage`` is also null.

        :cloudformationAttribute: ErrorMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrErrorMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the query logging association.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the specified query logging association. Valid values include the following:.

        - ``CREATING`` : Resolver is creating an association between an Amazon Virtual Private Cloud (Amazon VPC) and a query logging configuration.
        - ``CREATED`` : The association between an Amazon VPC and a query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.
        - ``DELETING`` : Resolver is deleting this query logging association.
        - ``FAILED`` : Resolver either couldn't create or couldn't delete the query logging association.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the query logging configuration that a VPC is associated with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolverQueryLogConfigId"))

    @resolver_query_log_config_id.setter
    def resolver_query_log_config_id(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1db906ade05cdffe0b91a4fd2853b84b934e5cdf736daf38331df97c1423271)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolverQueryLogConfigId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the Amazon VPC that is associated with the query logging configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b694d8fb6cb8627d77c3255fc71a59f89d38cc7a25fe9cf461f8580674f323d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverQueryLoggingConfigAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "resolver_query_log_config_id": "resolverQueryLogConfigId",
        "resource_id": "resourceId",
    },
)
class CfnResolverQueryLoggingConfigAssociationProps:
    def __init__(
        self,
        *,
        resolver_query_log_config_id: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResolverQueryLoggingConfigAssociation``.

        :param resolver_query_log_config_id: The ID of the query logging configuration that a VPC is associated with.
        :param resource_id: The ID of the Amazon VPC that is associated with the query logging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_resolver_query_logging_config_association_props = route53resolver.CfnResolverQueryLoggingConfigAssociationProps(
                resolver_query_log_config_id="resolverQueryLogConfigId",
                resource_id="resourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9922d645c66dbe12414cb71b48fbdb1d63b9b6ab9822bdc726d40d6b6d7ec6af)
            check_type(argname="argument resolver_query_log_config_id", value=resolver_query_log_config_id, expected_type=type_hints["resolver_query_log_config_id"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resolver_query_log_config_id is not None:
            self._values["resolver_query_log_config_id"] = resolver_query_log_config_id
        if resource_id is not None:
            self._values["resource_id"] = resource_id

    @builtins.property
    def resolver_query_log_config_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the query logging configuration that a VPC is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resolverquerylogconfigid
        '''
        result = self._values.get("resolver_query_log_config_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the Amazon VPC that is associated with the query logging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resourceid
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverQueryLoggingConfigAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverQueryLoggingConfigProps",
    jsii_struct_bases=[],
    name_mapping={"destination_arn": "destinationArn", "name": "name"},
)
class CfnResolverQueryLoggingConfigProps:
    def __init__(
        self,
        *,
        destination_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResolverQueryLoggingConfig``.

        :param destination_arn: The ARN of the resource that you want Resolver to send query logs: an Amazon S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
        :param name: The name of the query logging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_resolver_query_logging_config_props = route53resolver.CfnResolverQueryLoggingConfigProps(
                destination_arn="destinationArn",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee1cbce67551eb150646abe50220d9cf7ebeceb023635a7a5fafd4c05efa335a)
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination_arn is not None:
            self._values["destination_arn"] = destination_arn
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def destination_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the resource that you want Resolver to send query logs: an Amazon S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-destinationarn
        '''
        result = self._values.get("destination_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the query logging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverQueryLoggingConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnResolverRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverRule",
):
    '''For DNS queries that originate in your VPCs, specifies which Resolver endpoint the queries pass through, one domain name that you want to forward to your network, and the IP addresses of the DNS resolvers in your network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_resolver_rule = route53resolver.CfnResolverRule(self, "MyCfnResolverRule",
            domain_name="domainName",
            rule_type="ruleType",
        
            # the properties below are optional
            name="name",
            resolver_endpoint_id="resolverEndpointId",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_ips=[route53resolver.CfnResolverRule.TargetAddressProperty(
                ip="ip",
                ipv6="ipv6",
                port="port"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        rule_type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        resolver_endpoint_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_ips: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResolverRule.TargetAddressProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: DNS queries for this domain name are forwarded to the IP addresses that are specified in ``TargetIps`` . If a query matches multiple Resolver rules (example.com and www.example.com), the query is routed using the Resolver rule that contains the most specific domain name (www.example.com).
        :param rule_type: When you want to forward DNS queries for specified domain name to resolvers on your network, specify ``FORWARD`` . When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify ``SYSTEM`` . For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify ``FORWARD`` for ``RuleType`` . To then have Resolver process queries for apex.example.com, you create a rule and specify ``SYSTEM`` for ``RuleType`` . Currently, only Resolver can create rules that have a value of ``RECURSIVE`` for ``RuleType`` .
        :param name: The name for the Resolver rule, which you specified when you created the Resolver rule.
        :param resolver_endpoint_id: The ID of the endpoint that the rule is associated with.
        :param tags: Tags help organize and categorize your Resolver rules. Each tag consists of a key and an optional value, both of which you define.
        :param target_ips: An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7253810e416357d129df95b3c7aa9aa0f08e68de7d465658e598912cf1656eab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverRuleProps(
            domain_name=domain_name,
            rule_type=rule_type,
            name=name,
            resolver_endpoint_id=resolver_endpoint_id,
            tags=tags,
            target_ips=target_ips,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6027dfe6179ef3a94f1a4d35887422f48613a9a557a99a3bb4e0cf44c4aa48a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__678a826ad1212e0a47c15e7671251c43f8125d6006b97d932cbc2bda67eca2be)
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
        '''The Amazon Resource Name (ARN) of the resolver rule, such as ``arn:aws:route53resolver:us-east-1:123456789012:resolver-rule/resolver-rule-a1bzhi`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps.

        If a query matches multiple resolver rules (example.com and www.example.com), the query is routed using the resolver rule that contains the most specific domain name (www.example.com).

        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrResolverEndpointId")
    def attr_resolver_endpoint_id(self) -> builtins.str:
        '''The ID of the outbound endpoint that the rule is associated with, such as ``rslvr-out-fdc049932dexample`` .

        :cloudformationAttribute: ResolverEndpointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverEndpointId"))

    @builtins.property
    @jsii.member(jsii_name="attrResolverRuleId")
    def attr_resolver_rule_id(self) -> builtins.str:
        '''When the value of ``RuleType`` is ``FORWARD`` , the ID that Resolver assigned to the resolver rule when you created it, such as ``rslvr-rr-5328a0899aexample`` .

        This value isn't applicable when ``RuleType`` is ``SYSTEM`` .

        :cloudformationAttribute: ResolverRuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverRuleId"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetIps")
    def attr_target_ips(self) -> _IResolvable_da3f097b:
        '''When the value of ``RuleType`` is ``FORWARD`` , the IP addresses that the outbound endpoint forwards DNS queries to, typically the IP addresses for DNS resolvers on your network.

        This value isn't applicable when ``RuleType`` is ``SYSTEM`` .

        :cloudformationAttribute: TargetIps
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrTargetIps"))

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
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''DNS queries for this domain name are forwarded to the IP addresses that are specified in ``TargetIps`` .'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e83136a81b10aed2481c602cdca3f63e1c2bcaed82fe69b1ab2413af7c0b7c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="ruleType")
    def rule_type(self) -> builtins.str:
        '''When you want to forward DNS queries for specified domain name to resolvers on your network, specify ``FORWARD`` .'''
        return typing.cast(builtins.str, jsii.get(self, "ruleType"))

    @rule_type.setter
    def rule_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13530a5c4f7ce175ae03b85dc7d4550ae7a3cb68cb2be12c89a167e8db1a5822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the Resolver rule, which you specified when you created the Resolver rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b755d1de5f0792399af99f6519ecfdf572b862a0faeaf3dfb0fe65d57dedbd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resolverEndpointId")
    def resolver_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the endpoint that the rule is associated with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolverEndpointId"))

    @resolver_endpoint_id.setter
    def resolver_endpoint_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c083d92c5db206009067a23539e3835de5a4ffaadb5f9e02ae055cbecd6ae69c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolverEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags help organize and categorize your Resolver rules.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e091d2bae0380988eb82095436cc653b0277ca57b3313d9ab9a9d738a207e94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="targetIps")
    def target_ips(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResolverRule.TargetAddressProperty"]]]]:
        '''An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResolverRule.TargetAddressProperty"]]]], jsii.get(self, "targetIps"))

    @target_ips.setter
    def target_ips(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResolverRule.TargetAddressProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b47bfd58a0e36e9ad214a987222bbde73856ea070da35c19a584767b9de30ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIps", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverRule.TargetAddressProperty",
        jsii_struct_bases=[],
        name_mapping={"ip": "ip", "ipv6": "ipv6", "port": "port"},
    )
    class TargetAddressProperty:
        def __init__(
            self,
            *,
            ip: typing.Optional[builtins.str] = None,
            ipv6: typing.Optional[builtins.str] = None,
            port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''In a `CreateResolverRule <https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html>`_ request, an array of the IPs that you want to forward DNS queries to.

            :param ip: One IPv4 address that you want to forward DNS queries to.
            :param ipv6: One IPv6 address that you want to forward DNS queries to.
            :param port: The port at ``Ip`` that you want to forward DNS queries to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53resolver as route53resolver
                
                target_address_property = route53resolver.CfnResolverRule.TargetAddressProperty(
                    ip="ip",
                    ipv6="ipv6",
                    port="port"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f5d5e066bc7e887c4651fe3eebf6009eace009cdd0d99976dd16327e29a0de7)
                check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
                check_type(argname="argument ipv6", value=ipv6, expected_type=type_hints["ipv6"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ip is not None:
                self._values["ip"] = ip
            if ipv6 is not None:
                self._values["ipv6"] = ipv6
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def ip(self) -> typing.Optional[builtins.str]:
            '''One IPv4 address that you want to forward DNS queries to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-ip
            '''
            result = self._values.get("ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ipv6(self) -> typing.Optional[builtins.str]:
            '''One IPv6 address that you want to forward DNS queries to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-ipv6
            '''
            result = self._values.get("ipv6")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The port at ``Ip`` that you want to forward DNS queries to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetAddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnResolverRuleAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverRuleAssociation",
):
    '''In the response to an `AssociateResolverRule <https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html>`_ , `DisassociateResolverRule <https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverRule.html>`_ , or `ListResolverRuleAssociations <https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html>`_ request, provides information about an association between a resolver rule and a VPC. The association determines which DNS queries that originate in the VPC are forwarded to your network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53resolver as route53resolver
        
        cfn_resolver_rule_association = route53resolver.CfnResolverRuleAssociation(self, "MyCfnResolverRuleAssociation",
            resolver_rule_id="resolverRuleId",
            vpc_id="vpcId",
        
            # the properties below are optional
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resolver_rule_id: builtins.str,
        vpc_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resolver_rule_id: The ID of the Resolver rule that you associated with the VPC that is specified by ``VPCId`` .
        :param vpc_id: The ID of the VPC that you associated the Resolver rule with.
        :param name: The name of an association between a Resolver rule and a VPC.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e372f7e2d960601c8b6496b7cbefaf56be2402644532349feb6b1a788f12a6f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverRuleAssociationProps(
            resolver_rule_id=resolver_rule_id, vpc_id=vpc_id, name=name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd72e2446876b88be1d5f55caa206da94a291e5fb29d78a49f68d43eeddc553)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5141e3b6396432746dcd2839a8073924edaf6eab60fe09dd5216f7bccc1041b7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of an association between a resolver rule and a VPC, such as ``test.example.com in beta VPC`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrResolverRuleAssociationId")
    def attr_resolver_rule_association_id(self) -> builtins.str:
        '''The ID of the resolver rule association that you want to get information about, such as ``rslvr-rrassoc-97242eaf88example`` .

        :cloudformationAttribute: ResolverRuleAssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverRuleAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="attrResolverRuleId")
    def attr_resolver_rule_id(self) -> builtins.str:
        '''The ID of the resolver rule that you associated with the VPC that is specified by ``VPCId`` , such as ``rslvr-rr-5328a0899example`` .

        :cloudformationAttribute: ResolverRuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverRuleId"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcId")
    def attr_vpc_id(self) -> builtins.str:
        '''The ID of the VPC that you associated the resolver rule with, such as ``vpc-03cf94c75cexample`` .

        :cloudformationAttribute: VPCId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resolverRuleId")
    def resolver_rule_id(self) -> builtins.str:
        '''The ID of the Resolver rule that you associated with the VPC that is specified by ``VPCId`` .'''
        return typing.cast(builtins.str, jsii.get(self, "resolverRuleId"))

    @resolver_rule_id.setter
    def resolver_rule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b339255d54086d1a2889af53d18e2ed8f550493f3c975ff59cf0e43dda0b04ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolverRuleId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The ID of the VPC that you associated the Resolver rule with.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3630b9d70d02412653907de27de2ead8c93d153609a25e45e46a1586ddf587e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of an association between a Resolver rule and a VPC.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbb22cd6829772b1f3226c329a7cb57daf6b212b33815f8279e8d64303e66c7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverRuleAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "resolver_rule_id": "resolverRuleId",
        "vpc_id": "vpcId",
        "name": "name",
    },
)
class CfnResolverRuleAssociationProps:
    def __init__(
        self,
        *,
        resolver_rule_id: builtins.str,
        vpc_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResolverRuleAssociation``.

        :param resolver_rule_id: The ID of the Resolver rule that you associated with the VPC that is specified by ``VPCId`` .
        :param vpc_id: The ID of the VPC that you associated the Resolver rule with.
        :param name: The name of an association between a Resolver rule and a VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_resolver_rule_association_props = route53resolver.CfnResolverRuleAssociationProps(
                resolver_rule_id="resolverRuleId",
                vpc_id="vpcId",
            
                # the properties below are optional
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7cd1048ae30851b3480dc04a365c7bd487212f9328f80bc61e1bae1ae0c865)
            check_type(argname="argument resolver_rule_id", value=resolver_rule_id, expected_type=type_hints["resolver_rule_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resolver_rule_id": resolver_rule_id,
            "vpc_id": vpc_id,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def resolver_rule_id(self) -> builtins.str:
        '''The ID of the Resolver rule that you associated with the VPC that is specified by ``VPCId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-resolverruleid
        '''
        result = self._values.get("resolver_rule_id")
        assert result is not None, "Required property 'resolver_rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The ID of the VPC that you associated the Resolver rule with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of an association between a Resolver rule and a VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverRuleAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53resolver.CfnResolverRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "rule_type": "ruleType",
        "name": "name",
        "resolver_endpoint_id": "resolverEndpointId",
        "tags": "tags",
        "target_ips": "targetIps",
    },
)
class CfnResolverRuleProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        rule_type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        resolver_endpoint_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_ips: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolverRule.TargetAddressProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResolverRule``.

        :param domain_name: DNS queries for this domain name are forwarded to the IP addresses that are specified in ``TargetIps`` . If a query matches multiple Resolver rules (example.com and www.example.com), the query is routed using the Resolver rule that contains the most specific domain name (www.example.com).
        :param rule_type: When you want to forward DNS queries for specified domain name to resolvers on your network, specify ``FORWARD`` . When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify ``SYSTEM`` . For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify ``FORWARD`` for ``RuleType`` . To then have Resolver process queries for apex.example.com, you create a rule and specify ``SYSTEM`` for ``RuleType`` . Currently, only Resolver can create rules that have a value of ``RECURSIVE`` for ``RuleType`` .
        :param name: The name for the Resolver rule, which you specified when you created the Resolver rule.
        :param resolver_endpoint_id: The ID of the endpoint that the rule is associated with.
        :param tags: Tags help organize and categorize your Resolver rules. Each tag consists of a key and an optional value, both of which you define.
        :param target_ips: An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53resolver as route53resolver
            
            cfn_resolver_rule_props = route53resolver.CfnResolverRuleProps(
                domain_name="domainName",
                rule_type="ruleType",
            
                # the properties below are optional
                name="name",
                resolver_endpoint_id="resolverEndpointId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_ips=[route53resolver.CfnResolverRule.TargetAddressProperty(
                    ip="ip",
                    ipv6="ipv6",
                    port="port"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdcaea1870aaf2dc13fe56b2d15a89d6adba2ad5884071fc618c9e4bb2c3ddec)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument rule_type", value=rule_type, expected_type=type_hints["rule_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resolver_endpoint_id", value=resolver_endpoint_id, expected_type=type_hints["resolver_endpoint_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_ips", value=target_ips, expected_type=type_hints["target_ips"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "rule_type": rule_type,
        }
        if name is not None:
            self._values["name"] = name
        if resolver_endpoint_id is not None:
            self._values["resolver_endpoint_id"] = resolver_endpoint_id
        if tags is not None:
            self._values["tags"] = tags
        if target_ips is not None:
            self._values["target_ips"] = target_ips

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''DNS queries for this domain name are forwarded to the IP addresses that are specified in ``TargetIps`` .

        If a query matches multiple Resolver rules (example.com and www.example.com), the query is routed using the Resolver rule that contains the most specific domain name (www.example.com).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_type(self) -> builtins.str:
        '''When you want to forward DNS queries for specified domain name to resolvers on your network, specify ``FORWARD`` .

        When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify ``SYSTEM`` .

        For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify ``FORWARD`` for ``RuleType`` . To then have Resolver process queries for apex.example.com, you create a rule and specify ``SYSTEM`` for ``RuleType`` .

        Currently, only Resolver can create rules that have a value of ``RECURSIVE`` for ``RuleType`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-ruletype
        '''
        result = self._values.get("rule_type")
        assert result is not None, "Required property 'rule_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the Resolver rule, which you specified when you created the Resolver rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolver_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the endpoint that the rule is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-resolverendpointid
        '''
        result = self._values.get("resolver_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags help organize and categorize your Resolver rules.

        Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def target_ips(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResolverRule.TargetAddressProperty]]]]:
        '''An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to.

        Typically, these are the IP addresses of DNS resolvers on your network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-targetips
        '''
        result = self._values.get("target_ips")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResolverRule.TargetAddressProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFirewallDomainList",
    "CfnFirewallDomainListProps",
    "CfnFirewallRuleGroup",
    "CfnFirewallRuleGroupAssociation",
    "CfnFirewallRuleGroupAssociationProps",
    "CfnFirewallRuleGroupProps",
    "CfnResolverConfig",
    "CfnResolverConfigProps",
    "CfnResolverDNSSECConfig",
    "CfnResolverDNSSECConfigProps",
    "CfnResolverEndpoint",
    "CfnResolverEndpointProps",
    "CfnResolverQueryLoggingConfig",
    "CfnResolverQueryLoggingConfigAssociation",
    "CfnResolverQueryLoggingConfigAssociationProps",
    "CfnResolverQueryLoggingConfigProps",
    "CfnResolverRule",
    "CfnResolverRuleAssociation",
    "CfnResolverRuleAssociationProps",
    "CfnResolverRuleProps",
]

publication.publish()

def _typecheckingstub__bcc007bdf474ff9b47656099203906368c5f49f4d31157c1bdf719174d13ca40(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_file_url: typing.Optional[builtins.str] = None,
    domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2405f17a30b66b6ef7aa547ea3c9aaa5c2a71fbbd629b379f60d5c8bb77b12(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f70bcca1229db1f0e43a5ddacf558806ab81c69674e0c6071a249f5a17277467(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7accf6059d36236bce36e86dfe63d1ed53f3a65d7ea53742399c9759352e0cae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b87817a90afaf5311ea389ff3c45a6853527be9808e40cce2f6cfc19305941(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8645f4358aa1d05bc91526dd122ba90e9cde2f5b7544ed3b380aa0eb87ab69d4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30863ebcd73dd0ef970d69c195c961c38e90666b69b852fe97a3c6de8aa245d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf9cc65cbfb33602e70ad9026e1edbeb5f1b4164b0394d3cfdce7740e405780(
    *,
    domain_file_url: typing.Optional[builtins.str] = None,
    domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9746be8e0b121eabecb18d7b9ae1bc9af428e5cc8d783e461c9320d06c8fc0e6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    firewall_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallRuleGroup.FirewallRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea942bf9103d2894a7ad703494b0079059be2da97aa2ac442ccd1f4c2637788a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__352836508cb4a234dce9db067a4a6b16892d2992b535ab5789a8b26510d33298(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4982ed4db0c8f64d957d86baded56ef341d967caa88d8b33ffd869caf06121bc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFirewallRuleGroup.FirewallRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f12316eeee008a57ff409a2d0928e62d72782a14a490f01a676f1ec1bcbfaec7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e88161bfa870a62d2b106ff0d76bb87c2d573da805d7d6852d0dff9534955a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61f0f7aa6db62533b4486bd58a4692d76a133c14cd2281a8ea8e083c9d952e92(
    *,
    action: builtins.str,
    firewall_domain_list_id: builtins.str,
    priority: jsii.Number,
    block_override_dns_type: typing.Optional[builtins.str] = None,
    block_override_domain: typing.Optional[builtins.str] = None,
    block_override_ttl: typing.Optional[jsii.Number] = None,
    block_response: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c14109c8e9e82ef7977fee407f404276a6ffc4744fe71860c6f744a1417c11(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    firewall_rule_group_id: builtins.str,
    priority: jsii.Number,
    vpc_id: builtins.str,
    mutation_protection: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb2fdbfc384a2329d8566518aa7e6dca0ba449cb6e23695e5da8d2c513888425(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ea8836437672c68ec57924133e337a27b9fafc2d249f6546208b170785b90d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81cf8ccbce652950199c4dc1d0498a06a405b1ea4f5654eb5b6bb15f011648c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df379a1c86479068b208302f1f580ece307474355f5278ac695c719477ae84dc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e2014dd57caa582ea59405600284b7af6255f792c390ea00e77e3491d8b060b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be4d526713d68289e6792be4e80077d1ba62e05562705b2fdb43ca4018bb78b0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc1de518cdf5bfd11595ce5f841fb4008cc78e7e77be4df9c607f13a26d4ae6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd6a12a52fb303ead4db8087ce88b25dc5647283d9c2521b9c57f027d901a8ef(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__715b8023408ad9032f9d4e486688e3bb6a5d34ab729223deee30ce0cd75c46e8(
    *,
    firewall_rule_group_id: builtins.str,
    priority: jsii.Number,
    vpc_id: builtins.str,
    mutation_protection: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b614b409c77b0163f669e1c5a722bed570fc73bbd7afce583918c9e4ee2b0436(
    *,
    firewall_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFirewallRuleGroup.FirewallRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35122d782a5f80846e3948e7eb0337b124eee2f562394f9f0ac3811b76027fa7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    autodefined_reverse_flag: builtins.str,
    resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b80f7dd8c3634834446059b6a5647da70f751aee16fc635988309e2b114da8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9245311f34648ea25b101be3ffb5369952910a59e960688b54f2c2258e39669(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450443ae6074ab44544f056831d2657be6437d1211323970c28fc56cac885b6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a88dabe1b002091b3f1b20007f475ad636ceff67622ca0df695d865e58b6afee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e8a6715c54a3032f85efda72259aecef906caa87b4729b8c9bc48010e591ae1(
    *,
    autodefined_reverse_flag: builtins.str,
    resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6638caafa1a9c5bdf9ed48d3577b02e4b40b5d79f1097e2f38ee76bd54e1d00(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beec86a3f946f8bba21b5baf99d30238ede31cae4cc0235cc599a7acac27a76d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__500914e8a66667918411304e05cdc48d8739533812eafaae6b25a74fff18a0bd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01500aa55167586426473b83ae123cd92339f7e27e6ca9404fe1a1196a1d0708(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d1d6cb497f316e5311641ff022dde6f5ae37e4e937722cbf4e49800c7dcf748(
    *,
    resource_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08cda89b08c8f731727f875daf3a8c19a757df0fc3eddf478f27fb0918b6f59b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    direction: builtins.str,
    ip_addresses: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolverEndpoint.IpAddressRequestProperty, typing.Dict[builtins.str, typing.Any]]]]],
    security_group_ids: typing.Sequence[builtins.str],
    name: typing.Optional[builtins.str] = None,
    outpost_arn: typing.Optional[builtins.str] = None,
    preferred_instance_type: typing.Optional[builtins.str] = None,
    resolver_endpoint_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a594f1c4ff5a6e919f865cddbec172bf9c70dad7f119245b693e56904c3e22(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3077592639c4d7a8ad53495b093b110bbe6949ecec62cd24403bddabcd687bea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f26ad3d56070bf14ea6a442897c79a8a10930bf839dceba26c9ddfdb495eaf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff067f29f23ed0518b0bcb12dad7868af652ab264fc7832f5763aa0ed2fb1a1c(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResolverEndpoint.IpAddressRequestProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd40fe8701b13449c18839f0320f4f7723ee68f4abc97b40851e451655db5a80(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1565ceb760deb938817958de13e27b5c61682731edf6932d20ea1ee2f895ff1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d31b571c20f15c111682add26863cca7cacc533d03d2dabb2de16fb161cd87(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bfc22635cdaf30309d694026a7044f4f420cfb764c71a1a598838d0e309097b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea12c0007aac9ac64aa33ecafe1e72ea50009a42185b59a7edc01f7f78ca38f4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05af99e199269a9c0a481219900f7596a6eba88d314ae22816c89f9f4a219e9c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d97f321837e470551bf5db7cc56a0a66e6f3735b27f4874ba4123f7e2cfbf7d8(
    *,
    subnet_id: builtins.str,
    ip: typing.Optional[builtins.str] = None,
    ipv6: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc09ce842a854995739f051f3b593bc3ded813d2e97260dcb20f39108e8d889(
    *,
    direction: builtins.str,
    ip_addresses: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolverEndpoint.IpAddressRequestProperty, typing.Dict[builtins.str, typing.Any]]]]],
    security_group_ids: typing.Sequence[builtins.str],
    name: typing.Optional[builtins.str] = None,
    outpost_arn: typing.Optional[builtins.str] = None,
    preferred_instance_type: typing.Optional[builtins.str] = None,
    resolver_endpoint_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24f7f7cd30eb329e550fcb22ab4dcca0511ccbc9db92caea497cb901e8cab5a8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceae4268e30e5118e3afcbed515bd209f19b85cac9f4879f451843942d065c2c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64acb85fc2778ad49c6a6597c3bc955a1bd7a2c31643ee85de4e3a9a69a47f0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702489df5065cd7f9b56058549807af95a48ea6a2ae2079b66359c556f8a679b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619bc974053932510090c83ab6e45a2a1bce6285058cdfad4eadcaf81e211df9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bab4a8e285b8f5bd00ec7784b85dfa36801874e1e16d9ee8e779b0fea8fba0e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resolver_query_log_config_id: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea9e7fa7565de1a958cab659ce5835c5ff96a12b5f22c942f50c1697a6e1bad6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7129edbb9ae2ecd48a6f3cb5630988ab69f9fa2d6b78f2d542e8beb450c91874(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1db906ade05cdffe0b91a4fd2853b84b934e5cdf736daf38331df97c1423271(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b694d8fb6cb8627d77c3255fc71a59f89d38cc7a25fe9cf461f8580674f323d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9922d645c66dbe12414cb71b48fbdb1d63b9b6ab9822bdc726d40d6b6d7ec6af(
    *,
    resolver_query_log_config_id: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee1cbce67551eb150646abe50220d9cf7ebeceb023635a7a5fafd4c05efa335a(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7253810e416357d129df95b3c7aa9aa0f08e68de7d465658e598912cf1656eab(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    rule_type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    resolver_endpoint_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_ips: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolverRule.TargetAddressProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6027dfe6179ef3a94f1a4d35887422f48613a9a557a99a3bb4e0cf44c4aa48a5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678a826ad1212e0a47c15e7671251c43f8125d6006b97d932cbc2bda67eca2be(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e83136a81b10aed2481c602cdca3f63e1c2bcaed82fe69b1ab2413af7c0b7c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13530a5c4f7ce175ae03b85dc7d4550ae7a3cb68cb2be12c89a167e8db1a5822(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b755d1de5f0792399af99f6519ecfdf572b862a0faeaf3dfb0fe65d57dedbd2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c083d92c5db206009067a23539e3835de5a4ffaadb5f9e02ae055cbecd6ae69c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e091d2bae0380988eb82095436cc653b0277ca57b3313d9ab9a9d738a207e94(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b47bfd58a0e36e9ad214a987222bbde73856ea070da35c19a584767b9de30ae(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResolverRule.TargetAddressProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5d5e066bc7e887c4651fe3eebf6009eace009cdd0d99976dd16327e29a0de7(
    *,
    ip: typing.Optional[builtins.str] = None,
    ipv6: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e372f7e2d960601c8b6496b7cbefaf56be2402644532349feb6b1a788f12a6f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resolver_rule_id: builtins.str,
    vpc_id: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd72e2446876b88be1d5f55caa206da94a291e5fb29d78a49f68d43eeddc553(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5141e3b6396432746dcd2839a8073924edaf6eab60fe09dd5216f7bccc1041b7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b339255d54086d1a2889af53d18e2ed8f550493f3c975ff59cf0e43dda0b04ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3630b9d70d02412653907de27de2ead8c93d153609a25e45e46a1586ddf587e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbb22cd6829772b1f3226c329a7cb57daf6b212b33815f8279e8d64303e66c7e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7cd1048ae30851b3480dc04a365c7bd487212f9328f80bc61e1bae1ae0c865(
    *,
    resolver_rule_id: builtins.str,
    vpc_id: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdcaea1870aaf2dc13fe56b2d15a89d6adba2ad5884071fc618c9e4bb2c3ddec(
    *,
    domain_name: builtins.str,
    rule_type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    resolver_endpoint_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_ips: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolverRule.TargetAddressProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
