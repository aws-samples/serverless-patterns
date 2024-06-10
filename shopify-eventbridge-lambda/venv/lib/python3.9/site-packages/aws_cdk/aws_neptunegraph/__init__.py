'''
# AWS::NeptuneGraph Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_neptunegraph as neptunegraph
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NeptuneGraph construct libraries](https://constructs.dev/search?q=neptunegraph)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NeptuneGraph resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NeptuneGraph.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NeptuneGraph](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NeptuneGraph.html).

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
class CfnGraph(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraph",
):
    '''The ``AWS ::NeptuneGraph::Graph`` resource creates an  graph.

    is a memory-optimized graph database engine for analytics. For more information, see ` <https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html>`_ .

    You can use ``AWS ::NeptuneGraph::Graph.DeletionProtection`` to help guard against unintended deletion of your graph.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html
    :cloudformationResource: AWS::NeptuneGraph::Graph
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_neptunegraph as neptunegraph
        
        cfn_graph = neptunegraph.CfnGraph(self, "MyCfnGraph",
            provisioned_memory=123,
        
            # the properties below are optional
            deletion_protection=False,
            graph_name="graphName",
            public_connectivity=False,
            replica_count=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vector_search_configuration=neptunegraph.CfnGraph.VectorSearchConfigurationProperty(
                vector_search_dimension=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        provisioned_memory: jsii.Number,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        graph_name: typing.Optional[builtins.str] = None,
        public_connectivity: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_search_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraph.VectorSearchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param provisioned_memory: The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 128
        :param deletion_protection: A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
        :param graph_name: The graph name. For example: ``my-graph-1`` . The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. If you don't specify a graph name, a unique graph name is generated for you using the prefix ``graph-for`` , followed by a combination of ``Stack Name`` and a ``UUID`` .
        :param public_connectivity: Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. When the graph is publicly available, its domain name system (DNS) endpoint resolves to the public IP address from the internet. When the graph isn't publicly available, you need to create a ``PrivateGraphEndpoint`` in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC. Default: If not specified, the default value is false. .. epigraph:: If enabling public connectivity for the first time, there will be a delay while it is enabled.
        :param replica_count: The number of replicas in other AZs. Default: If not specified, the default value is 1.
        :param tags: Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
        :param vector_search_configuration: Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as ``dimension=`` value. Max = 65,535
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e963857650d4e99964bc9bad7da0b29a5d2d3c66d3452d1e9b4f35e89330e04b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphProps(
            provisioned_memory=provisioned_memory,
            deletion_protection=deletion_protection,
            graph_name=graph_name,
            public_connectivity=public_connectivity,
            replica_count=replica_count,
            tags=tags,
            vector_search_configuration=vector_search_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf52fbc1feb3cff366f97eb4e18219365009dc4166140b56dc094f0ff30060e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a52af3501a45e0012cf5459541c03326347319e68fa62eb909482cdc27da744c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''The connection endpoint for the graph.

        For example: ``g-12a3bcdef4.us-east-1.neptune-graph.amazonaws.com``

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrGraphArn")
    def attr_graph_arn(self) -> builtins.str:
        '''The ARN of the graph.

        For example: ``arn:aws:neptune-graph:us-east-1:111122223333:graph/g-12a3bcdef4``

        :cloudformationAttribute: GraphArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGraphArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGraphId")
    def attr_graph_id(self) -> builtins.str:
        '''The ID of the graph.

        For example: ``g-12a3bcdef4``

        :cloudformationAttribute: GraphId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGraphId"))

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
    @jsii.member(jsii_name="provisionedMemory")
    def provisioned_memory(self) -> jsii.Number:
        '''The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.'''
        return typing.cast(jsii.Number, jsii.get(self, "provisionedMemory"))

    @provisioned_memory.setter
    def provisioned_memory(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be08bf40b529ebc7ced68a048b332cc2239437062acb120b333ae55ee1a28087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionedMemory", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A value that indicates whether the graph has deletion protection enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d4dc803566213a64093ff7c2e80aeb4a54bbf259b51aa0f56875846630453c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="graphName")
    def graph_name(self) -> typing.Optional[builtins.str]:
        '''The graph name.

        For example: ``my-graph-1`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "graphName"))

    @graph_name.setter
    def graph_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e36e1cbffa42257001fdc31d1dd6378f3a98ce8e7f3bcd68a4772b9cb33cbbe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphName", value)

    @builtins.property
    @jsii.member(jsii_name="publicConnectivity")
    def public_connectivity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether or not the graph can be reachable over the internet.

        All access to graphs is IAM authenticated.
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publicConnectivity"))

    @public_connectivity.setter
    def public_connectivity(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9704e1ee452151e117b8f45f27e9257936bf4012fb73bd4445e9f623dce33af6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicConnectivity", value)

    @builtins.property
    @jsii.member(jsii_name="replicaCount")
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''The number of replicas in other AZs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicaCount"))

    @replica_count.setter
    def replica_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f28b1503d0209026da409a25c88bd8a02abf6c3c5ad8dd42afd261c716df1e27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicaCount", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds metadata tags to the new graph.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49f939472207baf1bb12ed3155e6d6c9c7b0a5427a254d271f09e144b617f439)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vectorSearchConfiguration")
    def vector_search_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraph.VectorSearchConfigurationProperty"]]:
        '''Specifies the number of dimensions for vector embeddings that will be loaded into the graph.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraph.VectorSearchConfigurationProperty"]], jsii.get(self, "vectorSearchConfiguration"))

    @vector_search_configuration.setter
    def vector_search_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraph.VectorSearchConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f52f361f4f645382b2e53faccee1b1e685b8665ddcc9f188eae9dec9c26ae9af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vectorSearchConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraph.VectorSearchConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vector_search_dimension": "vectorSearchDimension"},
    )
    class VectorSearchConfigurationProperty:
        def __init__(self, *, vector_search_dimension: jsii.Number) -> None:
            '''The vector-search configuration for the graph, which specifies the vector dimension to use in the vector index, if any.

            :param vector_search_dimension: The number of dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-vectorsearchconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_neptunegraph as neptunegraph
                
                vector_search_configuration_property = neptunegraph.CfnGraph.VectorSearchConfigurationProperty(
                    vector_search_dimension=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a4625f08e1fb2af5a059a020fbbe4f9b64ced8f30cb593a275b3af90d3b579b)
                check_type(argname="argument vector_search_dimension", value=vector_search_dimension, expected_type=type_hints["vector_search_dimension"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "vector_search_dimension": vector_search_dimension,
            }

        @builtins.property
        def vector_search_dimension(self) -> jsii.Number:
            '''The number of dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-vectorsearchconfiguration.html#cfn-neptunegraph-graph-vectorsearchconfiguration-vectorsearchdimension
            '''
            result = self._values.get("vector_search_dimension")
            assert result is not None, "Required property 'vector_search_dimension' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VectorSearchConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraphProps",
    jsii_struct_bases=[],
    name_mapping={
        "provisioned_memory": "provisionedMemory",
        "deletion_protection": "deletionProtection",
        "graph_name": "graphName",
        "public_connectivity": "publicConnectivity",
        "replica_count": "replicaCount",
        "tags": "tags",
        "vector_search_configuration": "vectorSearchConfiguration",
    },
)
class CfnGraphProps:
    def __init__(
        self,
        *,
        provisioned_memory: jsii.Number,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        graph_name: typing.Optional[builtins.str] = None,
        public_connectivity: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_search_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraph.VectorSearchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraph``.

        :param provisioned_memory: The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 128
        :param deletion_protection: A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
        :param graph_name: The graph name. For example: ``my-graph-1`` . The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. If you don't specify a graph name, a unique graph name is generated for you using the prefix ``graph-for`` , followed by a combination of ``Stack Name`` and a ``UUID`` .
        :param public_connectivity: Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. When the graph is publicly available, its domain name system (DNS) endpoint resolves to the public IP address from the internet. When the graph isn't publicly available, you need to create a ``PrivateGraphEndpoint`` in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC. Default: If not specified, the default value is false. .. epigraph:: If enabling public connectivity for the first time, there will be a delay while it is enabled.
        :param replica_count: The number of replicas in other AZs. Default: If not specified, the default value is 1.
        :param tags: Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
        :param vector_search_configuration: Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as ``dimension=`` value. Max = 65,535

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_neptunegraph as neptunegraph
            
            cfn_graph_props = neptunegraph.CfnGraphProps(
                provisioned_memory=123,
            
                # the properties below are optional
                deletion_protection=False,
                graph_name="graphName",
                public_connectivity=False,
                replica_count=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vector_search_configuration=neptunegraph.CfnGraph.VectorSearchConfigurationProperty(
                    vector_search_dimension=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c5873f5b0997b6619747c309d6a4e6c52de08653e961a9abf16f71c41b60b71)
            check_type(argname="argument provisioned_memory", value=provisioned_memory, expected_type=type_hints["provisioned_memory"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument graph_name", value=graph_name, expected_type=type_hints["graph_name"])
            check_type(argname="argument public_connectivity", value=public_connectivity, expected_type=type_hints["public_connectivity"])
            check_type(argname="argument replica_count", value=replica_count, expected_type=type_hints["replica_count"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vector_search_configuration", value=vector_search_configuration, expected_type=type_hints["vector_search_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "provisioned_memory": provisioned_memory,
        }
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if graph_name is not None:
            self._values["graph_name"] = graph_name
        if public_connectivity is not None:
            self._values["public_connectivity"] = public_connectivity
        if replica_count is not None:
            self._values["replica_count"] = replica_count
        if tags is not None:
            self._values["tags"] = tags
        if vector_search_configuration is not None:
            self._values["vector_search_configuration"] = vector_search_configuration

    @builtins.property
    def provisioned_memory(self) -> jsii.Number:
        '''The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.

        Min = 128

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-provisionedmemory
        '''
        result = self._values.get("provisioned_memory")
        assert result is not None, "Required property 'provisioned_memory' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A value that indicates whether the graph has deletion protection enabled.

        The graph can't be deleted when deletion protection is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-deletionprotection
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def graph_name(self) -> typing.Optional[builtins.str]:
        '''The graph name. For example: ``my-graph-1`` .

        The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens.

        If you don't specify a graph name, a unique graph name is generated for you using the prefix ``graph-for`` , followed by a combination of ``Stack Name`` and a ``UUID`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-graphname
        '''
        result = self._values.get("graph_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_connectivity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated.

        When the graph is publicly available, its domain name system (DNS) endpoint resolves to the public IP address from the internet. When the graph isn't publicly available, you need to create a ``PrivateGraphEndpoint`` in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC.

        Default: If not specified, the default value is false.
        .. epigraph::

           If enabling public connectivity for the first time, there will be a delay while it is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-publicconnectivity
        '''
        result = self._values.get("public_connectivity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''The number of replicas in other AZs.

        Default: If not specified, the default value is 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-replicacount
        '''
        result = self._values.get("replica_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds metadata tags to the new graph.

        These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vector_search_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraph.VectorSearchConfigurationProperty]]:
        '''Specifies the number of dimensions for vector embeddings that will be loaded into the graph.

        The value is specified as ``dimension=`` value. Max = 65,535

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-vectorsearchconfiguration
        '''
        result = self._values.get("vector_search_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraph.VectorSearchConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPrivateGraphEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnPrivateGraphEndpoint",
):
    '''Create a private graph endpoint to allow private access from to the graph from within a VPC.

    You can attach security groups to the private graph endpoint.
    .. epigraph::

       VPC endpoint charges apply.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html
    :cloudformationResource: AWS::NeptuneGraph::PrivateGraphEndpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_neptunegraph as neptunegraph
        
        cfn_private_graph_endpoint = neptunegraph.CfnPrivateGraphEndpoint(self, "MyCfnPrivateGraphEndpoint",
            graph_identifier="graphIdentifier",
            vpc_id="vpcId",
        
            # the properties below are optional
            security_group_ids=["securityGroupIds"],
            subnet_ids=["subnetIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        graph_identifier: builtins.str,
        vpc_id: builtins.str,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param graph_identifier: The unique identifier of the Neptune Analytics graph.
        :param vpc_id: The VPC in which the private graph endpoint needs to be created.
        :param security_group_ids: Security groups to be attached to the private graph endpoint..
        :param subnet_ids: Subnets in which private graph endpoint ENIs are created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01fbeae7e1567a93f602c30b996e949980cb85f4a6668a45a57e1fc68b7c6e1c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrivateGraphEndpointProps(
            graph_identifier=graph_identifier,
            vpc_id=vpc_id,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb2f8751fc71246393259a24b1f5b2dbf9fcd4b4b036f2fbc0dd9c938d27ed6b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8799795ac3d65adbbfd8af3b354287148d6f330fe76c184e9d21cc479404fe7c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPrivateGraphEndpointIdentifier")
    def attr_private_graph_endpoint_identifier(self) -> builtins.str:
        '''PrivateGraphEndpoint resource identifier generated by concatenating the associated GraphIdentifier and VpcId with an underscore separator.

        For example, if GraphIdentifier is ``g-12a3bcdef4`` and VpcId is ``vpc-111122223333aabbc`` , the generated PrivateGraphEndpointIdentifier will be ``g-12a3bcdef4_vpc-111122223333aabbc`` .

        :cloudformationAttribute: PrivateGraphEndpointIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateGraphEndpointIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcEndpointId")
    def attr_vpc_endpoint_id(self) -> builtins.str:
        '''VPC endpoint that provides a private connection between the Graph and specified VPC.

        For example: ``vpce-aabbaabbaabbaabba`` .

        :cloudformationAttribute: VpcEndpointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcEndpointId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="graphIdentifier")
    def graph_identifier(self) -> builtins.str:
        '''The unique identifier of the Neptune Analytics graph.'''
        return typing.cast(builtins.str, jsii.get(self, "graphIdentifier"))

    @graph_identifier.setter
    def graph_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c521eedd758be47324602ff294b6442e60a3e36064525b070eda655dce79b56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The VPC in which the private graph endpoint needs to be created.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8cead657efa4cbd411fd2fce0f1d5a3ce1d6da29415a8974e2a94651164cccd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Security groups to be attached to the private graph endpoint..'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__682bcd6c1c60a24355d9121c725518329acfd29ac4c1e75c30476fa597fb3235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Subnets in which private graph endpoint ENIs are created.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4fc8bb9e26efd06ea5bc87d6e7358de98fcb83d1fb96fc3f74ed77165366cd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnPrivateGraphEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "graph_identifier": "graphIdentifier",
        "vpc_id": "vpcId",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
    },
)
class CfnPrivateGraphEndpointProps:
    def __init__(
        self,
        *,
        graph_identifier: builtins.str,
        vpc_id: builtins.str,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrivateGraphEndpoint``.

        :param graph_identifier: The unique identifier of the Neptune Analytics graph.
        :param vpc_id: The VPC in which the private graph endpoint needs to be created.
        :param security_group_ids: Security groups to be attached to the private graph endpoint..
        :param subnet_ids: Subnets in which private graph endpoint ENIs are created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_neptunegraph as neptunegraph
            
            cfn_private_graph_endpoint_props = neptunegraph.CfnPrivateGraphEndpointProps(
                graph_identifier="graphIdentifier",
                vpc_id="vpcId",
            
                # the properties below are optional
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4034e8161715769ce918d492497f1ae3b63217d21450c72a2386f26fb2a4b186)
            check_type(argname="argument graph_identifier", value=graph_identifier, expected_type=type_hints["graph_identifier"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_identifier": graph_identifier,
            "vpc_id": vpc_id,
        }
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def graph_identifier(self) -> builtins.str:
        '''The unique identifier of the Neptune Analytics graph.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html#cfn-neptunegraph-privategraphendpoint-graphidentifier
        '''
        result = self._values.get("graph_identifier")
        assert result is not None, "Required property 'graph_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VPC in which the private graph endpoint needs to be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html#cfn-neptunegraph-privategraphendpoint-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Security groups to be attached to the private graph endpoint..

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html#cfn-neptunegraph-privategraphendpoint-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Subnets in which private graph endpoint ENIs are created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html#cfn-neptunegraph-privategraphendpoint-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrivateGraphEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGraph",
    "CfnGraphProps",
    "CfnPrivateGraphEndpoint",
    "CfnPrivateGraphEndpointProps",
]

publication.publish()

def _typecheckingstub__e963857650d4e99964bc9bad7da0b29a5d2d3c66d3452d1e9b4f35e89330e04b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    provisioned_memory: jsii.Number,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    graph_name: typing.Optional[builtins.str] = None,
    public_connectivity: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_search_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraph.VectorSearchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf52fbc1feb3cff366f97eb4e18219365009dc4166140b56dc094f0ff30060e4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a52af3501a45e0012cf5459541c03326347319e68fa62eb909482cdc27da744c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be08bf40b529ebc7ced68a048b332cc2239437062acb120b333ae55ee1a28087(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4dc803566213a64093ff7c2e80aeb4a54bbf259b51aa0f56875846630453c9(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e36e1cbffa42257001fdc31d1dd6378f3a98ce8e7f3bcd68a4772b9cb33cbbe7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9704e1ee452151e117b8f45f27e9257936bf4012fb73bd4445e9f623dce33af6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28b1503d0209026da409a25c88bd8a02abf6c3c5ad8dd42afd261c716df1e27(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49f939472207baf1bb12ed3155e6d6c9c7b0a5427a254d271f09e144b617f439(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52f361f4f645382b2e53faccee1b1e685b8665ddcc9f188eae9dec9c26ae9af(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraph.VectorSearchConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a4625f08e1fb2af5a059a020fbbe4f9b64ced8f30cb593a275b3af90d3b579b(
    *,
    vector_search_dimension: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c5873f5b0997b6619747c309d6a4e6c52de08653e961a9abf16f71c41b60b71(
    *,
    provisioned_memory: jsii.Number,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    graph_name: typing.Optional[builtins.str] = None,
    public_connectivity: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_search_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraph.VectorSearchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01fbeae7e1567a93f602c30b996e949980cb85f4a6668a45a57e1fc68b7c6e1c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    graph_identifier: builtins.str,
    vpc_id: builtins.str,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb2f8751fc71246393259a24b1f5b2dbf9fcd4b4b036f2fbc0dd9c938d27ed6b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8799795ac3d65adbbfd8af3b354287148d6f330fe76c184e9d21cc479404fe7c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c521eedd758be47324602ff294b6442e60a3e36064525b070eda655dce79b56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8cead657efa4cbd411fd2fce0f1d5a3ce1d6da29415a8974e2a94651164cccd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682bcd6c1c60a24355d9121c725518329acfd29ac4c1e75c30476fa597fb3235(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4fc8bb9e26efd06ea5bc87d6e7358de98fcb83d1fb96fc3f74ed77165366cd5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4034e8161715769ce918d492497f1ae3b63217d21450c72a2386f26fb2a4b186(
    *,
    graph_identifier: builtins.str,
    vpc_id: builtins.str,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
