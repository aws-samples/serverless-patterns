'''
# AWS::APS Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_aps as aps
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for APS construct libraries](https://constructs.dev/search?q=aps)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::APS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_APS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::APS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_APS.html).

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
class CfnRuleGroupsNamespace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnRuleGroupsNamespace",
):
    '''The definition of a rule groups namespace in an Amazon Managed Service for Prometheus workspace.

    A rule groups namespace is associated with exactly one rules file. A workspace can have multiple rule groups namespaces. For more information about rules files, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ , in the *Amazon Managed Service for Prometheus User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html
    :cloudformationResource: AWS::APS::RuleGroupsNamespace
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_rule_groups_namespace = aps.CfnRuleGroupsNamespace(self, "MyCfnRuleGroupsNamespace",
            data="data",
            name="name",
            workspace="workspace",
        
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
        data: builtins.str,
        name: builtins.str,
        workspace: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data: The rules file used in the namespace. For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param name: The name of the rule groups namespace.
        :param workspace: The ID of the workspace to add the rule groups namespace.
        :param tags: The list of tag keys and values that are associated with the rule groups namespace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d681a4d4a1e9d9052c98f45bf8b21257e825ee8185b30ea4b6f887fc7416b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuleGroupsNamespaceProps(
            data=data, name=name, workspace=workspace, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f066376b2a4b15a103f9a01bca66f252615381ddc55bd5508262712fd03eec2d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__501ad912878791d9cc1a45e52a9642fb0747f4ddf4482708286f9bfde7e036de)
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
        '''The ARN of the rule groups namespace.

        For example, ``arn:aws:aps:<region>:123456789012:rulegroupsnamespace/ws-example1-1234-abcd-5678-ef90abcd1234/rulesfile1`` .

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
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        '''The rules file used in the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__327e955bc86deb15923357f0f050e077304b8dbbb2c9baba9d84a13c5d7b695d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the rule groups namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f3851e1fa5b758763dff1a85515e41a8c57e1b4da81b2e677f003890944957f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="workspace")
    def workspace(self) -> builtins.str:
        '''The ID of the workspace to add the rule groups namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "workspace"))

    @workspace.setter
    def workspace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f899db17dfa1e1837e2b90cca5f83f23f67ca015116201811ad84d044e9ebe95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspace", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tag keys and values that are associated with the rule groups namespace.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9af819e60d52c87c9369e4854d0dfc8d4917db97219839fbc11cf2bdad55659)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnRuleGroupsNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "data": "data",
        "name": "name",
        "workspace": "workspace",
        "tags": "tags",
    },
)
class CfnRuleGroupsNamespaceProps:
    def __init__(
        self,
        *,
        data: builtins.str,
        name: builtins.str,
        workspace: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuleGroupsNamespace``.

        :param data: The rules file used in the namespace. For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param name: The name of the rule groups namespace.
        :param workspace: The ID of the workspace to add the rule groups namespace.
        :param tags: The list of tag keys and values that are associated with the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_rule_groups_namespace_props = aps.CfnRuleGroupsNamespaceProps(
                data="data",
                name="name",
                workspace="workspace",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ba9f13df78597d09b62adc5501ac56c5fedca3215c115e02cb7e3be9e440366)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument workspace", value=workspace, expected_type=type_hints["workspace"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data": data,
            "name": name,
            "workspace": workspace,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data(self) -> builtins.str:
        '''The rules file used in the namespace.

        For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-data
        '''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace(self) -> builtins.str:
        '''The ID of the workspace to add the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-workspace
        '''
        result = self._values.get("workspace")
        assert result is not None, "Required property 'workspace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tag keys and values that are associated with the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleGroupsNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnScraper(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnScraper",
):
    '''A scraper is a fully-managed agentless collector that discovers and pulls metrics automatically.

    A scraper pulls metrics from Prometheus-compatible sources within an Amazon EKS cluster, and sends them to your Amazon Managed Service for Prometheus workspace. Scrapers are flexible. You can configure the scraper to control what metrics are collected, the frequency of collection, what transformations are applied to the metrics, and more.

    An IAM role will be created for you that Amazon Managed Service for Prometheus uses to access the metrics in your cluster. You must configure this role with a policy that allows it to scrape metrics from your cluster. For more information, see `Configuring your Amazon EKS cluster <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-eks-setup>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    The ``scrapeConfiguration`` parameter contains the YAML configuration for the scraper.
    .. epigraph::

       For more information about collectors, including what metrics are collected, and how to configure the scraper, see `Using an AWS managed collector <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html
    :cloudformationResource: AWS::APS::Scraper
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_scraper = aps.CfnScraper(self, "MyCfnScraper",
            destination=aps.CfnScraper.DestinationProperty(
                amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                    workspace_arn="workspaceArn"
                )
            ),
            scrape_configuration=aps.CfnScraper.ScrapeConfigurationProperty(
                configuration_blob="configurationBlob"
            ),
            source=aps.CfnScraper.SourceProperty(
                eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                    cluster_arn="clusterArn",
                    subnet_ids=["subnetIds"],
        
                    # the properties below are optional
                    security_group_ids=["securityGroupIds"]
                )
            ),
        
            # the properties below are optional
            alias="alias",
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
        destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.ScrapeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        alias: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination: The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.
        :param scrape_configuration: The configuration in use by the scraper.
        :param source: The Amazon EKS cluster from which the scraper collects metrics.
        :param alias: An optional user-assigned scraper alias.
        :param tags: (Optional) The list of tag keys and values associated with the scraper.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d4cb1653b22b80f73c5fa4972418519c1d58f8ac033d22184f1b74ee25bf2b0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScraperProps(
            destination=destination,
            scrape_configuration=scrape_configuration,
            source=source,
            alias=alias,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ef0eaaf8983b897d546f9e872b3a951993e032cd8b5f5f1725e32854f8d096)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d151b530ba64dde831142e12510e32c75c01b169477c6e43bf92c26ab330e2ae)
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
        '''The Amazon Resource Name (ARN) of the scraper.

        For example, ``arn:aws:aps:<region>:123456798012:scraper/s-example1-1234-abcd-5678-ef9012abcd34`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleArn")
    def attr_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.

        For example, ``arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-12example`` .

        :cloudformationAttribute: RoleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrScraperId")
    def attr_scraper_id(self) -> builtins.str:
        '''The ID of the scraper.

        For example, ``s-example1-1234-abcd-5678-ef9012abcd34`` .

        :cloudformationAttribute: ScraperId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScraperId"))

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
    @jsii.member(jsii_name="destination")
    def destination(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.DestinationProperty"]:
        '''The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.DestinationProperty"], jsii.get(self, "destination"))

    @destination.setter
    def destination(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScraper.DestinationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d835d9e17a3614f6837476fe3d3de37c4e38685abfd4cc8e4e49236802dfc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="scrapeConfiguration")
    def scrape_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.ScrapeConfigurationProperty"]:
        '''The configuration in use by the scraper.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.ScrapeConfigurationProperty"], jsii.get(self, "scrapeConfiguration"))

    @scrape_configuration.setter
    def scrape_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScraper.ScrapeConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a91c6d3e6031af4c2e1ba10ae98234919eb5f1efa54c12c929f7141e223af9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scrapeConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.SourceProperty"]:
        '''The Amazon EKS cluster from which the scraper collects metrics.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.SourceProperty"], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScraper.SourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4baaa2665d7ddf1c8e51575f5139441f25d102954ee91a2fcbf97644019a8c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        '''An optional user-assigned scraper alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b98e11e4ea8701c0469eb24a036fb1452c2573d264405f3d5237c104fd77a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) The list of tag keys and values associated with the scraper.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265ada3fe1d3014c11a5af4d87c8e4b691d29a917e8643b804a82b7c3223573f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.AmpConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"workspace_arn": "workspaceArn"},
    )
    class AmpConfigurationProperty:
        def __init__(self, *, workspace_arn: builtins.str) -> None:
            '''The ``AmpConfiguration`` structure defines the Amazon Managed Service for Prometheus instance a scraper should send metrics to.

            :param workspace_arn: ARN of the Amazon Managed Service for Prometheus workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-ampconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                amp_configuration_property = aps.CfnScraper.AmpConfigurationProperty(
                    workspace_arn="workspaceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__02c8f0a43ed30375a3d1b283c2450f310915b0f0fcff6103d168cb18a16bfc4f)
                check_type(argname="argument workspace_arn", value=workspace_arn, expected_type=type_hints["workspace_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workspace_arn": workspace_arn,
            }

        @builtins.property
        def workspace_arn(self) -> builtins.str:
            '''ARN of the Amazon Managed Service for Prometheus workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-ampconfiguration.html#cfn-aps-scraper-ampconfiguration-workspacearn
            '''
            result = self._values.get("workspace_arn")
            assert result is not None, "Required property 'workspace_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmpConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"amp_configuration": "ampConfiguration"},
    )
    class DestinationProperty:
        def __init__(
            self,
            *,
            amp_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.AmpConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Where to send the metrics from a scraper.

            :param amp_configuration: The Amazon Managed Service for Prometheus workspace to send metrics to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                destination_property = aps.CfnScraper.DestinationProperty(
                    amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                        workspace_arn="workspaceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9dfeb013903b3b566e12e34ac903da7aaad96412ee8622e798d0f4931b78c31)
                check_type(argname="argument amp_configuration", value=amp_configuration, expected_type=type_hints["amp_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "amp_configuration": amp_configuration,
            }

        @builtins.property
        def amp_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.AmpConfigurationProperty"]:
            '''The Amazon Managed Service for Prometheus workspace to send metrics to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-destination.html#cfn-aps-scraper-destination-ampconfiguration
            '''
            result = self._values.get("amp_configuration")
            assert result is not None, "Required property 'amp_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.AmpConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.EksConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_arn": "clusterArn",
            "subnet_ids": "subnetIds",
            "security_group_ids": "securityGroupIds",
        },
    )
    class EksConfigurationProperty:
        def __init__(
            self,
            *,
            cluster_arn: builtins.str,
            subnet_ids: typing.Sequence[builtins.str],
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The ``EksConfiguration`` structure describes the connection to the Amazon EKS cluster from which a scraper collects metrics.

            :param cluster_arn: ARN of the Amazon EKS cluster.
            :param subnet_ids: A list of subnet IDs for the Amazon EKS cluster VPC configuration.
            :param security_group_ids: A list of the security group IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                eks_configuration_property = aps.CfnScraper.EksConfigurationProperty(
                    cluster_arn="clusterArn",
                    subnet_ids=["subnetIds"],
                
                    # the properties below are optional
                    security_group_ids=["securityGroupIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d84c728405d664f762d3c86aae8f989f77a50273eb74e76dce90e3e0305f06a9)
                check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_arn": cluster_arn,
                "subnet_ids": subnet_ids,
            }
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids

        @builtins.property
        def cluster_arn(self) -> builtins.str:
            '''ARN of the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-clusterarn
            '''
            result = self._values.get("cluster_arn")
            assert result is not None, "Required property 'cluster_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''A list of subnet IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the security group IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.ScrapeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"configuration_blob": "configurationBlob"},
    )
    class ScrapeConfigurationProperty:
        def __init__(self, *, configuration_blob: builtins.str) -> None:
            '''A scrape configuration for a scraper, base 64 encoded.

            For more information, see `Scraper configuration <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration>`_ in the *Amazon Managed Service for Prometheus User Guide* .

            :param configuration_blob: The base 64 encoded scrape configuration file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                scrape_configuration_property = aps.CfnScraper.ScrapeConfigurationProperty(
                    configuration_blob="configurationBlob"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__61507a1463486662c27c8fec99a5cb181f22e5f346b7bb6d10823ad9b7102b72)
                check_type(argname="argument configuration_blob", value=configuration_blob, expected_type=type_hints["configuration_blob"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_blob": configuration_blob,
            }

        @builtins.property
        def configuration_blob(self) -> builtins.str:
            '''The base 64 encoded scrape configuration file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapeconfiguration.html#cfn-aps-scraper-scrapeconfiguration-configurationblob
            '''
            result = self._values.get("configuration_blob")
            assert result is not None, "Required property 'configuration_blob' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScrapeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_configuration": "eksConfiguration"},
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            eks_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.EksConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The source of collected metrics for a scraper.

            :param eks_configuration: The Amazon EKS cluster from which a scraper collects metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                source_property = aps.CfnScraper.SourceProperty(
                    eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                        cluster_arn="clusterArn",
                        subnet_ids=["subnetIds"],
                
                        # the properties below are optional
                        security_group_ids=["securityGroupIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__655e83ac40d7d6fcc3362aa2c25fcfadc0beb5744ef393de105d7d152821a330)
                check_type(argname="argument eks_configuration", value=eks_configuration, expected_type=type_hints["eks_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "eks_configuration": eks_configuration,
            }

        @builtins.property
        def eks_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.EksConfigurationProperty"]:
            '''The Amazon EKS cluster from which a scraper collects metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-source.html#cfn-aps-scraper-source-eksconfiguration
            '''
            result = self._values.get("eks_configuration")
            assert result is not None, "Required property 'eks_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.EksConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnScraperProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "scrape_configuration": "scrapeConfiguration",
        "source": "source",
        "alias": "alias",
        "tags": "tags",
    },
)
class CfnScraperProps:
    def __init__(
        self,
        *,
        destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
        scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScrapeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
        alias: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScraper``.

        :param destination: The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.
        :param scrape_configuration: The configuration in use by the scraper.
        :param source: The Amazon EKS cluster from which the scraper collects metrics.
        :param alias: An optional user-assigned scraper alias.
        :param tags: (Optional) The list of tag keys and values associated with the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_scraper_props = aps.CfnScraperProps(
                destination=aps.CfnScraper.DestinationProperty(
                    amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                        workspace_arn="workspaceArn"
                    )
                ),
                scrape_configuration=aps.CfnScraper.ScrapeConfigurationProperty(
                    configuration_blob="configurationBlob"
                ),
                source=aps.CfnScraper.SourceProperty(
                    eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                        cluster_arn="clusterArn",
                        subnet_ids=["subnetIds"],
            
                        # the properties below are optional
                        security_group_ids=["securityGroupIds"]
                    )
                ),
            
                # the properties below are optional
                alias="alias",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f302dfc2aa92636b313e32f5d91a0ccfd79ebde0259b977f6291d4c8329455d7)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument scrape_configuration", value=scrape_configuration, expected_type=type_hints["scrape_configuration"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "scrape_configuration": scrape_configuration,
            "source": source,
        }
        if alias is not None:
            self._values["alias"] = alias
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScraper.DestinationProperty]:
        '''The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-destination
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScraper.DestinationProperty], result)

    @builtins.property
    def scrape_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScraper.ScrapeConfigurationProperty]:
        '''The configuration in use by the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-scrapeconfiguration
        '''
        result = self._values.get("scrape_configuration")
        assert result is not None, "Required property 'scrape_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScraper.ScrapeConfigurationProperty], result)

    @builtins.property
    def source(self) -> typing.Union[_IResolvable_da3f097b, CfnScraper.SourceProperty]:
        '''The Amazon EKS cluster from which the scraper collects metrics.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScraper.SourceProperty], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''An optional user-assigned scraper alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-alias
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) The list of tag keys and values associated with the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScraperProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkspace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace",
):
    '''An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html
    :cloudformationResource: AWS::APS::Workspace
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_workspace = aps.CfnWorkspace(self, "MyCfnWorkspace",
            alert_manager_definition="alertManagerDefinition",
            alias="alias",
            kms_key_arn="kmsKeyArn",
            logging_configuration=aps.CfnWorkspace.LoggingConfigurationProperty(
                log_group_arn="logGroupArn"
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
        alert_manager_definition: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alert_manager_definition: The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace. For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* . The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ). ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``
        :param alias: The alias that is assigned to this workspace to help identify it. It does not need to be unique.
        :param kms_key_arn: (optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param logging_configuration: Contains information about the logging configuration for the workspace.
        :param tags: The list of tag keys and values that are associated with the workspace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d7d4de6c2c3c0a6cc1f746f35f29f98344da5c5d59e48a9d1e788ab80e3ef9b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkspaceProps(
            alert_manager_definition=alert_manager_definition,
            alias=alias,
            kms_key_arn=kms_key_arn,
            logging_configuration=logging_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea1a406920301232e7f737fa791c75b19a41702c2a8761c41de9163390ebcdf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__391b593ff5f1b04fd33a43b56be0c4a7f41dd147af44a0bc665b22d97e9640c8)
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
        '''The ARN of the workspace.

        For example, ``arn:aws:aps:<region>:123456789012:workspace/ws-example1-1234-abcd-5678-ef90abcd1234`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPrometheusEndpoint")
    def attr_prometheus_endpoint(self) -> builtins.str:
        '''The Prometheus endpoint available for this workspace.

        For example, ``https://aps-workspaces.<region>.amazonaws.com/workspaces/ws-example1-1234-abcd-5678-ef90abcd1234/api/v1/`` .

        :cloudformationAttribute: PrometheusEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrometheusEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkspaceId")
    def attr_workspace_id(self) -> builtins.str:
        '''The unique ID for the workspace.

        For example, ``ws-example1-1234-abcd-5678-ef90abcd1234`` .

        :cloudformationAttribute: WorkspaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkspaceId"))

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
    @jsii.member(jsii_name="alertManagerDefinition")
    def alert_manager_definition(self) -> typing.Optional[builtins.str]:
        '''The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertManagerDefinition"))

    @alert_manager_definition.setter
    def alert_manager_definition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c2399f13a196d4fdd83827148d3942b4231e42e722c32b0c66a56f8425f5d1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertManagerDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        '''The alias that is assigned to this workspace to help identify it.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69c703012a200792f370b43791a7b9e6c8ab12b196993de037a82396c6c51b3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''(optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e1bc26d25cdad92f552b6ceb5e8a4ae6d459a5f2737ae032c5a2f069eedf68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingConfigurationProperty"]]:
        '''Contains information about the logging configuration for the workspace.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingConfigurationProperty"]], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab06dccfc037b2ba3e02b4a3154224a63edcfe3fc06381ff9162c2c33a94b712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tag keys and values that are associated with the workspace.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4e1977fb1f7aad47144a42af408e41c9d01794f3569a614a9ed54effb1c1e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the logging configuration for the workspace.

            :param log_group_arn: The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                logging_configuration_property = aps.CfnWorkspace.LoggingConfigurationProperty(
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa0678eca2188c6c3220d708f7d16298acecab165f03de8b400d1fada6a4b9d9)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_arn is not None:
                self._values["log_group_arn"] = log_group_arn

        @builtins.property
        def log_group_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the CloudWatch log group to which the vended log data will be published.

            This log group must exist prior to calling this operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html#cfn-aps-workspace-loggingconfiguration-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnWorkspaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "alert_manager_definition": "alertManagerDefinition",
        "alias": "alias",
        "kms_key_arn": "kmsKeyArn",
        "logging_configuration": "loggingConfiguration",
        "tags": "tags",
    },
)
class CfnWorkspaceProps:
    def __init__(
        self,
        *,
        alert_manager_definition: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkspace``.

        :param alert_manager_definition: The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace. For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* . The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ). ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``
        :param alias: The alias that is assigned to this workspace to help identify it. It does not need to be unique.
        :param kms_key_arn: (optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param logging_configuration: Contains information about the logging configuration for the workspace.
        :param tags: The list of tag keys and values that are associated with the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_workspace_props = aps.CfnWorkspaceProps(
                alert_manager_definition="alertManagerDefinition",
                alias="alias",
                kms_key_arn="kmsKeyArn",
                logging_configuration=aps.CfnWorkspace.LoggingConfigurationProperty(
                    log_group_arn="logGroupArn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e95bd874171795b8c6f6104e5fee9fa1d8f50cb6e1edc6d2cc01a77eb0f50a)
            check_type(argname="argument alert_manager_definition", value=alert_manager_definition, expected_type=type_hints["alert_manager_definition"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alert_manager_definition is not None:
            self._values["alert_manager_definition"] = alert_manager_definition
        if alias is not None:
            self._values["alias"] = alias
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def alert_manager_definition(self) -> typing.Optional[builtins.str]:
        '''The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace.

        For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ).

        ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alertmanagerdefinition
        '''
        result = self._values.get("alert_manager_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''The alias that is assigned to this workspace to help identify it.

        It does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alias
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''(optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace.

        For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.LoggingConfigurationProperty]]:
        '''Contains information about the logging configuration for the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.LoggingConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tag keys and values that are associated with the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRuleGroupsNamespace",
    "CfnRuleGroupsNamespaceProps",
    "CfnScraper",
    "CfnScraperProps",
    "CfnWorkspace",
    "CfnWorkspaceProps",
]

publication.publish()

def _typecheckingstub__02d681a4d4a1e9d9052c98f45bf8b21257e825ee8185b30ea4b6f887fc7416b1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data: builtins.str,
    name: builtins.str,
    workspace: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f066376b2a4b15a103f9a01bca66f252615381ddc55bd5508262712fd03eec2d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501ad912878791d9cc1a45e52a9642fb0747f4ddf4482708286f9bfde7e036de(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__327e955bc86deb15923357f0f050e077304b8dbbb2c9baba9d84a13c5d7b695d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3851e1fa5b758763dff1a85515e41a8c57e1b4da81b2e677f003890944957f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f899db17dfa1e1837e2b90cca5f83f23f67ca015116201811ad84d044e9ebe95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9af819e60d52c87c9369e4854d0dfc8d4917db97219839fbc11cf2bdad55659(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba9f13df78597d09b62adc5501ac56c5fedca3215c115e02cb7e3be9e440366(
    *,
    data: builtins.str,
    name: builtins.str,
    workspace: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4cb1653b22b80f73c5fa4972418519c1d58f8ac033d22184f1b74ee25bf2b0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScrapeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    alias: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ef0eaaf8983b897d546f9e872b3a951993e032cd8b5f5f1725e32854f8d096(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d151b530ba64dde831142e12510e32c75c01b169477c6e43bf92c26ab330e2ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d835d9e17a3614f6837476fe3d3de37c4e38685abfd4cc8e4e49236802dfc0(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.DestinationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a91c6d3e6031af4c2e1ba10ae98234919eb5f1efa54c12c929f7141e223af9(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.ScrapeConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4baaa2665d7ddf1c8e51575f5139441f25d102954ee91a2fcbf97644019a8c48(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.SourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b98e11e4ea8701c0469eb24a036fb1452c2573d264405f3d5237c104fd77a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265ada3fe1d3014c11a5af4d87c8e4b691d29a917e8643b804a82b7c3223573f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02c8f0a43ed30375a3d1b283c2450f310915b0f0fcff6103d168cb18a16bfc4f(
    *,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9dfeb013903b3b566e12e34ac903da7aaad96412ee8622e798d0f4931b78c31(
    *,
    amp_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.AmpConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84c728405d664f762d3c86aae8f989f77a50273eb74e76dce90e3e0305f06a9(
    *,
    cluster_arn: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61507a1463486662c27c8fec99a5cb181f22e5f346b7bb6d10823ad9b7102b72(
    *,
    configuration_blob: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__655e83ac40d7d6fcc3362aa2c25fcfadc0beb5744ef393de105d7d152821a330(
    *,
    eks_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.EksConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f302dfc2aa92636b313e32f5d91a0ccfd79ebde0259b977f6291d4c8329455d7(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScrapeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    alias: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7d4de6c2c3c0a6cc1f746f35f29f98344da5c5d59e48a9d1e788ab80e3ef9b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alert_manager_definition: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea1a406920301232e7f737fa791c75b19a41702c2a8761c41de9163390ebcdf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391b593ff5f1b04fd33a43b56be0c4a7f41dd147af44a0bc665b22d97e9640c8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2399f13a196d4fdd83827148d3942b4231e42e722c32b0c66a56f8425f5d1a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c703012a200792f370b43791a7b9e6c8ab12b196993de037a82396c6c51b3d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e1bc26d25cdad92f552b6ceb5e8a4ae6d459a5f2737ae032c5a2f069eedf68(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab06dccfc037b2ba3e02b4a3154224a63edcfe3fc06381ff9162c2c33a94b712(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.LoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4e1977fb1f7aad47144a42af408e41c9d01794f3569a614a9ed54effb1c1e5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa0678eca2188c6c3220d708f7d16298acecab165f03de8b400d1fada6a4b9d9(
    *,
    log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e95bd874171795b8c6f6104e5fee9fa1d8f50cb6e1edc6d2cc01a77eb0f50a(
    *,
    alert_manager_definition: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
