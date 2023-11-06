'''
# AWS::Route53RecoveryControl Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_route53recoverycontrol as route53recoverycontrol
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Route53RecoveryControl construct libraries](https://constructs.dev/search?q=route53recoverycontrol)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Route53RecoveryControl resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53RecoveryControl.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Route53RecoveryControl](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53RecoveryControl.html).

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
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnCluster",
):
    '''Creates a cluster in Amazon Route 53 Application Recovery Controller.

    A cluster is a set of redundant Regional endpoints that you can run Route 53 ARC API calls against to update or get the state of one or more routing controls.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
        
        cfn_cluster = route53recoverycontrol.CfnCluster(self, "MyCfnCluster",
            name="name",
        
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
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Name of the cluster. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon).
        :param tags: The value for a tag.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a22ce3cb989f0084b0215729b9e32485e8f3c7d8c5b66e19c5d569e7319889ca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1d5d3d9f3a1044ea448e47cbbc2078fcd16eda9541fc5415cf9d029dd4ebb80)
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
            type_hints = typing.get_type_hints(_typecheckingstub__157cd2ce4f13202c3d86071a895cc645d726227e8e629edaa431247ba0c6394e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterArn")
    def attr_cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the cluster.

        :cloudformationAttribute: ClusterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterArn"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterEndpoints")
    def attr_cluster_endpoints(self) -> _IResolvable_da3f097b:
        '''An array of endpoints for the cluster.

        You specify one of these endpoints when you want to set or retrieve a routing control state in the cluster.

        :cloudformationAttribute: ClusterEndpoints
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrClusterEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The deployment status of the cluster.

        Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1256c59e47b758559a89c3e22392b86499c611a6b2d3207ea90be4979bcc55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The value for a tag.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07baed78448e49810892cf249edb0e6836f52fd39d85bd39a03b4d9a5c018f83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnCluster.ClusterEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint": "endpoint", "region": "region"},
    )
    class ClusterEndpointProperty:
        def __init__(
            self,
            *,
            endpoint: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A cluster endpoint.

            You specify one of the five cluster endpoints, which consists of an endpoint URL and an AWS Region, when you want to get or update a routing control state in the cluster.

            For more information, see `Code examples <https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples.html>`_ in the Amazon Route 53 Application Recovery Controller Developer Guide.

            :param endpoint: A cluster endpoint URL for one of the five redundant clusters that you specify to set or retrieve a routing control state.
            :param region: The AWS Region for a cluster endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
                
                cluster_endpoint_property = route53recoverycontrol.CfnCluster.ClusterEndpointProperty(
                    endpoint="endpoint",
                    region="region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__417623fb2e8bf530a95eb326a2e5d219300a55ce5482328b4bf15990d0310e22)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if region is not None:
                self._values["region"] = region

        @builtins.property
        def endpoint(self) -> typing.Optional[builtins.str]:
            '''A cluster endpoint URL for one of the five redundant clusters that you specify to set or retrieve a routing control state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region for a cluster endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param name: Name of the cluster. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon).
        :param tags: The value for a tag.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
            
            cfn_cluster_props = route53recoverycontrol.CfnClusterProps(
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ce2dce26c7c141f1b9e0e5bcda1dc9d1ab67320e0af4676b77cea0c5569d52)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the cluster.

        You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The value for a tag.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnControlPanel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnControlPanel",
):
    '''Creates a new control panel in Amazon Route 53 Application Recovery Controller.

    A control panel represents a group of routing controls that can be changed together in a single transaction. You can use a control panel to centrally view the operational status of applications across your organization, and trigger multi-app failovers in a single transaction, for example, to fail over from one AWS Region (cell) to another.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
        
        cfn_control_panel = route53recoverycontrol.CfnControlPanel(self, "MyCfnControlPanel",
            name="name",
        
            # the properties below are optional
            cluster_arn="clusterArn",
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
        name: builtins.str,
        cluster_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the control panel. You can use any non-white space character in the name.
        :param cluster_arn: The Amazon Resource Name (ARN) of the cluster for the control panel.
        :param tags: The value for a tag.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af4420a741fa687672aaafb49569b8fb25d0ae5baef4ea3a30346b1e29fdeddc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnControlPanelProps(name=name, cluster_arn=cluster_arn, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__906d7ee6c36bc3e1a47d63da18a0ef8f9dfc5b1b853e525b7b6f63b82e861c3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf81ef33259a058090f6fa1cc9339f3649028db55e20370b7278b6b62060dffb)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrControlPanelArn")
    def attr_control_panel_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the control panel.

        :cloudformationAttribute: ControlPanelArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrControlPanelArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDefaultControlPanel")
    def attr_default_control_panel(self) -> _IResolvable_da3f097b:
        '''The boolean flag that is set to true for the default control panel in the cluster.

        :cloudformationAttribute: DefaultControlPanel
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDefaultControlPanel"))

    @builtins.property
    @jsii.member(jsii_name="attrRoutingControlCount")
    def attr_routing_control_count(self) -> jsii.Number:
        '''The number of routing controls in the control panel.

        :cloudformationAttribute: RoutingControlCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRoutingControlCount"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The deployment status of control panel.

        Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the control panel.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff1e4aff586d839998504ce3800e2d90978f6d2f2b4749548b04479b125b5876)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the cluster for the control panel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a03d1b0034ff93cad4c05e7991efc53df68fe3cdd2e75d6b622c9c79bdadb978)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The value for a tag.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e918a49aa511684305e6f0fb7fb172abe97ec14120062a0a7055abb8d3b11df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnControlPanelProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "cluster_arn": "clusterArn", "tags": "tags"},
)
class CfnControlPanelProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        cluster_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnControlPanel``.

        :param name: The name of the control panel. You can use any non-white space character in the name.
        :param cluster_arn: The Amazon Resource Name (ARN) of the cluster for the control panel.
        :param tags: The value for a tag.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
            
            cfn_control_panel_props = route53recoverycontrol.CfnControlPanelProps(
                name="name",
            
                # the properties below are optional
                cluster_arn="clusterArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50e50657a1a484bf705523a13399e8ac229d80e2376b9afeb9094f2552d0e434)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if cluster_arn is not None:
            self._values["cluster_arn"] = cluster_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the control panel.

        You can use any non-white space character in the name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the cluster for the control panel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn
        '''
        result = self._values.get("cluster_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The value for a tag.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnControlPanelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRoutingControl(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnRoutingControl",
):
    '''Creates a routing control in Amazon Route 53 Application Recovery Controller.

    Routing control states are maintained on the highly reliable cluster data plane.

    To get or update the state of the routing control, you must specify a cluster endpoint, which is an endpoint URL and an AWS Region. For more information, see `Code examples <https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples.html>`_ in the Amazon Route 53 Application Recovery Controller Developer Guide.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
        
        cfn_routing_control = route53recoverycontrol.CfnRoutingControl(self, "MyCfnRoutingControl",
            name="name",
        
            # the properties below are optional
            cluster_arn="clusterArn",
            control_panel_arn="controlPanelArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        cluster_arn: typing.Optional[builtins.str] = None,
        control_panel_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the routing control. You can use any non-white space character in the name.
        :param cluster_arn: The Amazon Resource Name (ARN) of the cluster that hosts the routing control.
        :param control_panel_arn: The Amazon Resource Name (ARN) of the control panel that includes the routing control.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8e66a23f93757dc3bc37d83299cb23ab412cab6e96d4afaf3456eb08bbe1384)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRoutingControlProps(
            name=name, cluster_arn=cluster_arn, control_panel_arn=control_panel_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cea52182bae1f52b300778ab2900344293265e4a0e849cdfe61a3dce971c102)
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
            type_hints = typing.get_type_hints(_typecheckingstub__76de149d457b1328783895c028b114f9744b7d58dd013e9640f5e3efd449753e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRoutingControlArn")
    def attr_routing_control_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the routing control.

        :cloudformationAttribute: RoutingControlArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoutingControlArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The deployment status of the routing control.

        Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the routing control.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ffc3a734bfe1d7ef78f014e4a963d3351e1c500ddba76301e057f64865b8d24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the cluster that hosts the routing control.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a18f0809fa84cd7460c3453004605dc29ea8e93f869dcea8d169e007ab9dcc54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="controlPanelArn")
    def control_panel_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the control panel that includes the routing control.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "controlPanelArn"))

    @control_panel_arn.setter
    def control_panel_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc7cd54715a8da344cf718e3f18f4ce00a90691ceb31d93f935d4046fa90a0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "controlPanelArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnRoutingControlProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "cluster_arn": "clusterArn",
        "control_panel_arn": "controlPanelArn",
    },
)
class CfnRoutingControlProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        cluster_arn: typing.Optional[builtins.str] = None,
        control_panel_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnRoutingControl``.

        :param name: The name of the routing control. You can use any non-white space character in the name.
        :param cluster_arn: The Amazon Resource Name (ARN) of the cluster that hosts the routing control.
        :param control_panel_arn: The Amazon Resource Name (ARN) of the control panel that includes the routing control.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
            
            cfn_routing_control_props = route53recoverycontrol.CfnRoutingControlProps(
                name="name",
            
                # the properties below are optional
                cluster_arn="clusterArn",
                control_panel_arn="controlPanelArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be91c55bdc0168798c12f7b90c6849a8a971899532b4c0d715d17dc211090cf9)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument control_panel_arn", value=control_panel_arn, expected_type=type_hints["control_panel_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if cluster_arn is not None:
            self._values["cluster_arn"] = cluster_arn
        if control_panel_arn is not None:
            self._values["control_panel_arn"] = control_panel_arn

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the routing control.

        You can use any non-white space character in the name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the cluster that hosts the routing control.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-clusterarn
        '''
        result = self._values.get("cluster_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def control_panel_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the control panel that includes the routing control.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-controlpanelarn
        '''
        result = self._values.get("control_panel_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRoutingControlProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSafetyRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnSafetyRule",
):
    '''Creates a safety rule in a control panel in Amazon Route 53 Application Recovery Controller.

    Safety rules in Amazon Route 53 Application Recovery Controller let you add safeguards around changing routing control states, and enabling and disabling routing controls, to help prevent unwanted outcomes. Note that the name of a safety rule must be unique within a control panel.

    There are two types of safety rules in Route 53 ARC: assertion rules and gating rules.

    Assertion rule: An assertion rule enforces that, when you change a routing control state, certain criteria are met. For example, the criteria might be that at least one routing control state is ``On`` after the transaction completes so that traffic continues to be directed to at least one cell for the application. This prevents a fail-open scenario.

    Gating rule: A gating rule lets you configure a gating routing control as an overall on-off switch for a group of routing controls. Or, you can configure more complex gating scenarios, for example, by configuring multiple gating routing controls.

    For more information, see `Safety rules <https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.safety-rules.html>`_ in the Amazon Route 53 Application Recovery Controller Developer Guide.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
        
        cfn_safety_rule = route53recoverycontrol.CfnSafetyRule(self, "MyCfnSafetyRule",
            control_panel_arn="controlPanelArn",
            name="name",
            rule_config=route53recoverycontrol.CfnSafetyRule.RuleConfigProperty(
                inverted=False,
                threshold=123,
                type="type"
            ),
        
            # the properties below are optional
            assertion_rule=route53recoverycontrol.CfnSafetyRule.AssertionRuleProperty(
                asserted_controls=["assertedControls"],
                wait_period_ms=123
            ),
            gating_rule=route53recoverycontrol.CfnSafetyRule.GatingRuleProperty(
                gating_controls=["gatingControls"],
                target_controls=["targetControls"],
                wait_period_ms=123
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
        control_panel_arn: builtins.str,
        name: builtins.str,
        rule_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSafetyRule.RuleConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        assertion_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSafetyRule.AssertionRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        gating_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSafetyRule.GatingRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param control_panel_arn: The Amazon Resource Name (ARN) for the control panel.
        :param name: The name of the assertion rule. The name must be unique within a control panel. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon)
        :param rule_config: The criteria that you set for specific assertion controls (routing controls) that designate how many control states must be ``ON`` as the result of a transaction. For example, if you have three assertion controls, you might specify ``ATLEAST 2`` for your rule configuration. This means that at least two assertion controls must be ``ON`` , so that at least two AWS Regions have traffic flowing to them.
        :param assertion_rule: An assertion rule enforces that, when you change a routing control state, that the criteria that you set in the rule configuration is met. Otherwise, the change to the routing control is not accepted. For example, the criteria might be that at least one routing control state is ``On`` after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.
        :param gating_rule: A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete. For example, if you specify one gating routing control and you set the ``Type`` in the rule configuration to ``OR`` , that indicates that you must set the gating routing control to ``On`` for the rule to evaluate as true; that is, for the gating control switch to be On. When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule.
        :param tags: The value for a tag.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada45d21faa78154fe211f8a129efa23cb89aef71314ca3d913f77b7503e67b3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSafetyRuleProps(
            control_panel_arn=control_panel_arn,
            name=name,
            rule_config=rule_config,
            assertion_rule=assertion_rule,
            gating_rule=gating_rule,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc0ff8959fc7098a93ba8121b62c4604117277cfc3c24b5083e009b52708acb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca9d90b4e6e7c5b8904a7f97b5817b9a5a99144110b842ba64d728b8930aad14)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSafetyRuleArn")
    def attr_safety_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the safety rule.

        :cloudformationAttribute: SafetyRuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSafetyRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The deployment status of the safety rule.

        Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="controlPanelArn")
    def control_panel_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the control panel.'''
        return typing.cast(builtins.str, jsii.get(self, "controlPanelArn"))

    @control_panel_arn.setter
    def control_panel_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac7fd6aa767c97d5a44cdfccf8155e0d77251d8c9591d85dcdc48e3400d9a988)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "controlPanelArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the assertion rule.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a87cb89df1aa33fe1c8db7fb822d3e7f34782e740bfb2ca584bafa663cb5807c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ruleConfig")
    def rule_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.RuleConfigProperty"]:
        '''The criteria that you set for specific assertion controls (routing controls) that designate how many control states must be ``ON`` as the result of a transaction.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.RuleConfigProperty"], jsii.get(self, "ruleConfig"))

    @rule_config.setter
    def rule_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.RuleConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7aad314d51748eb191ea9b0e9889d83df03cd198fc13eed992ee56efe980963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleConfig", value)

    @builtins.property
    @jsii.member(jsii_name="assertionRule")
    def assertion_rule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.AssertionRuleProperty"]]:
        '''An assertion rule enforces that, when you change a routing control state, that the criteria that you set in the rule configuration is met.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.AssertionRuleProperty"]], jsii.get(self, "assertionRule"))

    @assertion_rule.setter
    def assertion_rule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.AssertionRuleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19b243601ac621ff529a9f1e0672f5662b990b3a10fa6c3709439314ee34ea4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assertionRule", value)

    @builtins.property
    @jsii.member(jsii_name="gatingRule")
    def gating_rule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.GatingRuleProperty"]]:
        '''A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.GatingRuleProperty"]], jsii.get(self, "gatingRule"))

    @gating_rule.setter
    def gating_rule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSafetyRule.GatingRuleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8620a5842adbe4ff4519c97bca27014d017f98e271369a1d1e6cef3f4026c19a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatingRule", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The value for a tag.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bd1e26d09f647010d0e1f98f3c76cc6cdcae0897c20573ffc9e57371f980308)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnSafetyRule.AssertionRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "asserted_controls": "assertedControls",
            "wait_period_ms": "waitPeriodMs",
        },
    )
    class AssertionRuleProperty:
        def __init__(
            self,
            *,
            asserted_controls: typing.Sequence[builtins.str],
            wait_period_ms: jsii.Number,
        ) -> None:
            '''An assertion rule enforces that, when you change a routing control state, that the criteria that you set in the rule configuration is met.

            Otherwise, the change to the routing control is not accepted. For example, the criteria might be that at least one routing control state is ``On`` after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.

            :param asserted_controls: The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions.
            :param wait_period_ms: An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent flapping of state. The wait period is 5000 ms by default, but you can choose a custom value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
                
                assertion_rule_property = route53recoverycontrol.CfnSafetyRule.AssertionRuleProperty(
                    asserted_controls=["assertedControls"],
                    wait_period_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed41f1b03917d2b555857972db2d17c822ab6a52a6d97abe4bbccf0372d0c1ea)
                check_type(argname="argument asserted_controls", value=asserted_controls, expected_type=type_hints["asserted_controls"])
                check_type(argname="argument wait_period_ms", value=wait_period_ms, expected_type=type_hints["wait_period_ms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "asserted_controls": asserted_controls,
                "wait_period_ms": wait_period_ms,
            }

        @builtins.property
        def asserted_controls(self) -> typing.List[builtins.str]:
            '''The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed.

            For example, you might include three routing controls, one for each of three AWS Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-assertedcontrols
            '''
            result = self._values.get("asserted_controls")
            assert result is not None, "Required property 'asserted_controls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def wait_period_ms(self) -> jsii.Number:
            '''An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail.

            This helps prevent flapping of state. The wait period is 5000 ms by default, but you can choose a custom value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-waitperiodms
            '''
            result = self._values.get("wait_period_ms")
            assert result is not None, "Required property 'wait_period_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssertionRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnSafetyRule.GatingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "gating_controls": "gatingControls",
            "target_controls": "targetControls",
            "wait_period_ms": "waitPeriodMs",
        },
    )
    class GatingRuleProperty:
        def __init__(
            self,
            *,
            gating_controls: typing.Sequence[builtins.str],
            target_controls: typing.Sequence[builtins.str],
            wait_period_ms: jsii.Number,
        ) -> None:
            '''A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete.

            For example, if you specify one gating routing control and you set the ``Type`` in the rule configuration to ``OR`` , that indicates that you must set the gating routing control to ``On`` for the rule to evaluate as true; that is, for the gating control switch to be On. When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule.

            :param gating_controls: An array of gating routing control Amazon Resource Names (ARNs). For a simple on-off switch, specify the ARN for one routing control. The gating routing controls are evaluated by the rule configuration that you specify to determine if the target routing control states can be changed.
            :param target_controls: An array of target routing control Amazon Resource Names (ARNs) for which the states can only be updated if the rule configuration that you specify evaluates to true for the gating routing control. As a simple example, if you have a single gating control, it acts as an overall on-off switch for a set of target routing controls. You can use this to manually override automated failover, for example.
            :param wait_period_ms: An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent flapping of state. The wait period is 5000 ms by default, but you can choose a custom value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
                
                gating_rule_property = route53recoverycontrol.CfnSafetyRule.GatingRuleProperty(
                    gating_controls=["gatingControls"],
                    target_controls=["targetControls"],
                    wait_period_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c5117f2c875821616bc202779e0c96aa6802dceac68d7e79a315ebc7478c010)
                check_type(argname="argument gating_controls", value=gating_controls, expected_type=type_hints["gating_controls"])
                check_type(argname="argument target_controls", value=target_controls, expected_type=type_hints["target_controls"])
                check_type(argname="argument wait_period_ms", value=wait_period_ms, expected_type=type_hints["wait_period_ms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "gating_controls": gating_controls,
                "target_controls": target_controls,
                "wait_period_ms": wait_period_ms,
            }

        @builtins.property
        def gating_controls(self) -> typing.List[builtins.str]:
            '''An array of gating routing control Amazon Resource Names (ARNs).

            For a simple on-off switch, specify the ARN for one routing control. The gating routing controls are evaluated by the rule configuration that you specify to determine if the target routing control states can be changed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-gatingcontrols
            '''
            result = self._values.get("gating_controls")
            assert result is not None, "Required property 'gating_controls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def target_controls(self) -> typing.List[builtins.str]:
            '''An array of target routing control Amazon Resource Names (ARNs) for which the states can only be updated if the rule configuration that you specify evaluates to true for the gating routing control.

            As a simple example, if you have a single gating control, it acts as an overall on-off switch for a set of target routing controls. You can use this to manually override automated failover, for example.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-targetcontrols
            '''
            result = self._values.get("target_controls")
            assert result is not None, "Required property 'target_controls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def wait_period_ms(self) -> jsii.Number:
            '''An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail.

            This helps prevent flapping of state. The wait period is 5000 ms by default, but you can choose a custom value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-waitperiodms
            '''
            result = self._values.get("wait_period_ms")
            assert result is not None, "Required property 'wait_period_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnSafetyRule.RuleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "inverted": "inverted",
            "threshold": "threshold",
            "type": "type",
        },
    )
    class RuleConfigProperty:
        def __init__(
            self,
            *,
            inverted: typing.Union[builtins.bool, _IResolvable_da3f097b],
            threshold: jsii.Number,
            type: builtins.str,
        ) -> None:
            '''The rule configuration for an assertion rule.

            That is, the criteria that you set for specific assertion controls (routing controls) that specify how many controls must be enabled after a transaction completes.

            :param inverted: Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa.
            :param threshold: The value of N, when you specify an ``ATLEAST`` rule type. That is, ``Threshold`` is the number of controls that must be set when you specify an ``ATLEAST`` type.
            :param type: A rule can be one of the following: ``ATLEAST`` , ``AND`` , or ``OR`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
                
                rule_config_property = route53recoverycontrol.CfnSafetyRule.RuleConfigProperty(
                    inverted=False,
                    threshold=123,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e9c7596694f51a191b407b4cf7800cd696d05a6cbbcb4f0a2890c69a7758ace)
                check_type(argname="argument inverted", value=inverted, expected_type=type_hints["inverted"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "inverted": inverted,
                "threshold": threshold,
                "type": type,
            }

        @builtins.property
        def inverted(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Logical negation of the rule.

            If the rule would usually evaluate true, it's evaluated as false, and vice versa.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-inverted
            '''
            result = self._values.get("inverted")
            assert result is not None, "Required property 'inverted' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''The value of N, when you specify an ``ATLEAST`` rule type.

            That is, ``Threshold`` is the number of controls that must be set when you specify an ``ATLEAST`` type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''A rule can be one of the following: ``ATLEAST`` , ``AND`` , or ``OR`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53recoverycontrol.CfnSafetyRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "control_panel_arn": "controlPanelArn",
        "name": "name",
        "rule_config": "ruleConfig",
        "assertion_rule": "assertionRule",
        "gating_rule": "gatingRule",
        "tags": "tags",
    },
)
class CfnSafetyRuleProps:
    def __init__(
        self,
        *,
        control_panel_arn: builtins.str,
        name: builtins.str,
        rule_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.RuleConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        assertion_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.AssertionRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        gating_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.GatingRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSafetyRule``.

        :param control_panel_arn: The Amazon Resource Name (ARN) for the control panel.
        :param name: The name of the assertion rule. The name must be unique within a control panel. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon)
        :param rule_config: The criteria that you set for specific assertion controls (routing controls) that designate how many control states must be ``ON`` as the result of a transaction. For example, if you have three assertion controls, you might specify ``ATLEAST 2`` for your rule configuration. This means that at least two assertion controls must be ``ON`` , so that at least two AWS Regions have traffic flowing to them.
        :param assertion_rule: An assertion rule enforces that, when you change a routing control state, that the criteria that you set in the rule configuration is met. Otherwise, the change to the routing control is not accepted. For example, the criteria might be that at least one routing control state is ``On`` after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.
        :param gating_rule: A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete. For example, if you specify one gating routing control and you set the ``Type`` in the rule configuration to ``OR`` , that indicates that you must set the gating routing control to ``On`` for the rule to evaluate as true; that is, for the gating control switch to be On. When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule.
        :param tags: The value for a tag.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53recoverycontrol as route53recoverycontrol
            
            cfn_safety_rule_props = route53recoverycontrol.CfnSafetyRuleProps(
                control_panel_arn="controlPanelArn",
                name="name",
                rule_config=route53recoverycontrol.CfnSafetyRule.RuleConfigProperty(
                    inverted=False,
                    threshold=123,
                    type="type"
                ),
            
                # the properties below are optional
                assertion_rule=route53recoverycontrol.CfnSafetyRule.AssertionRuleProperty(
                    asserted_controls=["assertedControls"],
                    wait_period_ms=123
                ),
                gating_rule=route53recoverycontrol.CfnSafetyRule.GatingRuleProperty(
                    gating_controls=["gatingControls"],
                    target_controls=["targetControls"],
                    wait_period_ms=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44e00780d2bb00de407ed35a33395166d559891130b782d5658fb973337fbe9)
            check_type(argname="argument control_panel_arn", value=control_panel_arn, expected_type=type_hints["control_panel_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule_config", value=rule_config, expected_type=type_hints["rule_config"])
            check_type(argname="argument assertion_rule", value=assertion_rule, expected_type=type_hints["assertion_rule"])
            check_type(argname="argument gating_rule", value=gating_rule, expected_type=type_hints["gating_rule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "control_panel_arn": control_panel_arn,
            "name": name,
            "rule_config": rule_config,
        }
        if assertion_rule is not None:
            self._values["assertion_rule"] = assertion_rule
        if gating_rule is not None:
            self._values["gating_rule"] = gating_rule
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def control_panel_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the control panel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-controlpanelarn
        '''
        result = self._values.get("control_panel_arn")
        assert result is not None, "Required property 'control_panel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the assertion rule.

        The name must be unique within a control panel. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSafetyRule.RuleConfigProperty]:
        '''The criteria that you set for specific assertion controls (routing controls) that designate how many control states must be ``ON`` as the result of a transaction.

        For example, if you have three assertion controls, you might specify ``ATLEAST 2`` for your rule configuration. This means that at least two assertion controls must be ``ON`` , so that at least two AWS Regions have traffic flowing to them.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-ruleconfig
        '''
        result = self._values.get("rule_config")
        assert result is not None, "Required property 'rule_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSafetyRule.RuleConfigProperty], result)

    @builtins.property
    def assertion_rule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSafetyRule.AssertionRuleProperty]]:
        '''An assertion rule enforces that, when you change a routing control state, that the criteria that you set in the rule configuration is met.

        Otherwise, the change to the routing control is not accepted. For example, the criteria might be that at least one routing control state is ``On`` after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule
        '''
        result = self._values.get("assertion_rule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSafetyRule.AssertionRuleProperty]], result)

    @builtins.property
    def gating_rule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSafetyRule.GatingRuleProperty]]:
        '''A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete.

        For example, if you specify one gating routing control and you set the ``Type`` in the rule configuration to ``OR`` , that indicates that you must set the gating routing control to ``On`` for the rule to evaluate as true; that is, for the gating control switch to be On. When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule
        '''
        result = self._values.get("gating_rule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSafetyRule.GatingRuleProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The value for a tag.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSafetyRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
    "CfnControlPanel",
    "CfnControlPanelProps",
    "CfnRoutingControl",
    "CfnRoutingControlProps",
    "CfnSafetyRule",
    "CfnSafetyRuleProps",
]

publication.publish()

def _typecheckingstub__a22ce3cb989f0084b0215729b9e32485e8f3c7d8c5b66e19c5d569e7319889ca(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1d5d3d9f3a1044ea448e47cbbc2078fcd16eda9541fc5415cf9d029dd4ebb80(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__157cd2ce4f13202c3d86071a895cc645d726227e8e629edaa431247ba0c6394e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1256c59e47b758559a89c3e22392b86499c611a6b2d3207ea90be4979bcc55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07baed78448e49810892cf249edb0e6836f52fd39d85bd39a03b4d9a5c018f83(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417623fb2e8bf530a95eb326a2e5d219300a55ce5482328b4bf15990d0310e22(
    *,
    endpoint: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ce2dce26c7c141f1b9e0e5bcda1dc9d1ab67320e0af4676b77cea0c5569d52(
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af4420a741fa687672aaafb49569b8fb25d0ae5baef4ea3a30346b1e29fdeddc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    cluster_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__906d7ee6c36bc3e1a47d63da18a0ef8f9dfc5b1b853e525b7b6f63b82e861c3b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf81ef33259a058090f6fa1cc9339f3649028db55e20370b7278b6b62060dffb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff1e4aff586d839998504ce3800e2d90978f6d2f2b4749548b04479b125b5876(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a03d1b0034ff93cad4c05e7991efc53df68fe3cdd2e75d6b622c9c79bdadb978(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e918a49aa511684305e6f0fb7fb172abe97ec14120062a0a7055abb8d3b11df(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50e50657a1a484bf705523a13399e8ac229d80e2376b9afeb9094f2552d0e434(
    *,
    name: builtins.str,
    cluster_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8e66a23f93757dc3bc37d83299cb23ab412cab6e96d4afaf3456eb08bbe1384(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    cluster_arn: typing.Optional[builtins.str] = None,
    control_panel_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cea52182bae1f52b300778ab2900344293265e4a0e849cdfe61a3dce971c102(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76de149d457b1328783895c028b114f9744b7d58dd013e9640f5e3efd449753e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffc3a734bfe1d7ef78f014e4a963d3351e1c500ddba76301e057f64865b8d24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18f0809fa84cd7460c3453004605dc29ea8e93f869dcea8d169e007ab9dcc54(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc7cd54715a8da344cf718e3f18f4ce00a90691ceb31d93f935d4046fa90a0a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be91c55bdc0168798c12f7b90c6849a8a971899532b4c0d715d17dc211090cf9(
    *,
    name: builtins.str,
    cluster_arn: typing.Optional[builtins.str] = None,
    control_panel_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada45d21faa78154fe211f8a129efa23cb89aef71314ca3d913f77b7503e67b3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    control_panel_arn: builtins.str,
    name: builtins.str,
    rule_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.RuleConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    assertion_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.AssertionRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gating_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.GatingRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc0ff8959fc7098a93ba8121b62c4604117277cfc3c24b5083e009b52708acb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca9d90b4e6e7c5b8904a7f97b5817b9a5a99144110b842ba64d728b8930aad14(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac7fd6aa767c97d5a44cdfccf8155e0d77251d8c9591d85dcdc48e3400d9a988(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87cb89df1aa33fe1c8db7fb822d3e7f34782e740bfb2ca584bafa663cb5807c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7aad314d51748eb191ea9b0e9889d83df03cd198fc13eed992ee56efe980963(
    value: typing.Union[_IResolvable_da3f097b, CfnSafetyRule.RuleConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b243601ac621ff529a9f1e0672f5662b990b3a10fa6c3709439314ee34ea4d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSafetyRule.AssertionRuleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8620a5842adbe4ff4519c97bca27014d017f98e271369a1d1e6cef3f4026c19a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSafetyRule.GatingRuleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bd1e26d09f647010d0e1f98f3c76cc6cdcae0897c20573ffc9e57371f980308(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed41f1b03917d2b555857972db2d17c822ab6a52a6d97abe4bbccf0372d0c1ea(
    *,
    asserted_controls: typing.Sequence[builtins.str],
    wait_period_ms: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5117f2c875821616bc202779e0c96aa6802dceac68d7e79a315ebc7478c010(
    *,
    gating_controls: typing.Sequence[builtins.str],
    target_controls: typing.Sequence[builtins.str],
    wait_period_ms: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e9c7596694f51a191b407b4cf7800cd696d05a6cbbcb4f0a2890c69a7758ace(
    *,
    inverted: typing.Union[builtins.bool, _IResolvable_da3f097b],
    threshold: jsii.Number,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44e00780d2bb00de407ed35a33395166d559891130b782d5658fb973337fbe9(
    *,
    control_panel_arn: builtins.str,
    name: builtins.str,
    rule_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.RuleConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    assertion_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.AssertionRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gating_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSafetyRule.GatingRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
