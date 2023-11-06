'''
# AWS::EMRContainers Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_emrcontainers as emrcontainers
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EMRContainers construct libraries](https://constructs.dev/search?q=emrcontainers)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EMRContainers resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRContainers.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EMRContainers](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRContainers.html).

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
class CfnVirtualCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster",
):
    '''The ``AWS::EMRContainers::VirtualCluster`` resource specifies a virtual cluster.

    A virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list, and delete virtual clusters. They do not consume any additional resources in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrcontainers as emrcontainers
        
        cfn_virtual_cluster = emrcontainers.CfnVirtualCluster(self, "MyCfnVirtualCluster",
            container_provider=emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                id="id",
                info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                        namespace="namespace"
                    )
                ),
                type="type"
            ),
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
        container_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnVirtualCluster.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param container_provider: The container provider of the virtual cluster.
        :param name: The name of the virtual cluster.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a06dc2760ceb0de7a449a23941f15987094157d1a540c30fa67c9e49a3e06101)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVirtualClusterProps(
            container_provider=container_provider, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__802f118bbdec329d651201f6f69836e8e9523c47d32a262a55c4813747ccf78c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3035614e8641a59d4a7600ad906f142054401a42e6c1ca14df8b5d57d08f0823)
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
        '''The Amazon Resource Name (ARN) of the project, such as ``arn:aws:emr-containers:us-east-1:123456789012:/virtualclusters/ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the virtual cluster, such as ``ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="containerProvider")
    def container_provider(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnVirtualCluster.ContainerProviderProperty"]:
        '''The container provider of the virtual cluster.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnVirtualCluster.ContainerProviderProperty"], jsii.get(self, "containerProvider"))

    @container_provider.setter
    def container_provider(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnVirtualCluster.ContainerProviderProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__617f2c6bc289034f068a4b514139fc0bee8f6455f589c3e2de7ee7fb7a3a92e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerProvider", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the virtual cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aea4d0052a5a6cb82d57b5655349988466e02d75bbcc22aec370e6810b4c382d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3436f23ae2ca4313aacb96519980906e71e5bc37e7a466a53353480f948e674)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.ContainerInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_info": "eksInfo"},
    )
    class ContainerInfoProperty:
        def __init__(
            self,
            *,
            eks_info: typing.Union[_IResolvable_da3f097b, typing.Union["CfnVirtualCluster.EksInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The information about the container used for a job run or a managed endpoint.

            :param eks_info: The information about the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_info_property = emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                        namespace="namespace"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e5baf7a38335e2eb8733f2aa2d96a9593d774d095fb8a05dcf1d8bd22323050)
                check_type(argname="argument eks_info", value=eks_info, expected_type=type_hints["eks_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "eks_info": eks_info,
            }

        @builtins.property
        def eks_info(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnVirtualCluster.EksInfoProperty"]:
            '''The information about the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html#cfn-emrcontainers-virtualcluster-containerinfo-eksinfo
            '''
            result = self._values.get("eks_info")
            assert result is not None, "Required property 'eks_info' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnVirtualCluster.EksInfoProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.ContainerProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "info": "info", "type": "type"},
    )
    class ContainerProviderProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            info: typing.Union[_IResolvable_da3f097b, typing.Union["CfnVirtualCluster.ContainerInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''The information about the container provider.

            :param id: The ID of the container cluster. *Minimum* : 1 *Maximum* : 100 *Pattern* : ``^[0-9A-Za-z][A-Za-z0-9\\-_]*``
            :param info: The information about the container cluster.
            :param type: The type of the container provider. Amazon EKS is the only supported type as of now.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_provider_property = emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                    id="id",
                    info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                            namespace="namespace"
                        )
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__19801d68aea5b7c69bfd60c7d9c690e62c4643fe80fcda956e884f367b8b1dcf)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument info", value=info, expected_type=type_hints["info"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "info": info,
                "type": type,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The ID of the container cluster.

            *Minimum* : 1

            *Maximum* : 100

            *Pattern* : ``^[0-9A-Za-z][A-Za-z0-9\\-_]*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def info(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnVirtualCluster.ContainerInfoProperty"]:
            '''The information about the container cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-info
            '''
            result = self._values.get("info")
            assert result is not None, "Required property 'info' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnVirtualCluster.ContainerInfoProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the container provider.

            Amazon EKS is the only supported type as of now.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.EksInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace"},
    )
    class EksInfoProperty:
        def __init__(self, *, namespace: builtins.str) -> None:
            '''The information about the Amazon EKS cluster.

            :param namespace: The namespaces of the EKS cluster. *Minimum* : 1 *Maximum* : 63 *Pattern* : ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                eks_info_property = emrcontainers.CfnVirtualCluster.EksInfoProperty(
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__26be72236c14a8878e3d92d7b17397aa49c8a844f85e9e98c958600dd7a08c8f)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "namespace": namespace,
            }

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespaces of the EKS cluster.

            *Minimum* : 1

            *Maximum* : 63

            *Pattern* : ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html#cfn-emrcontainers-virtualcluster-eksinfo-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_provider": "containerProvider",
        "name": "name",
        "tags": "tags",
    },
)
class CfnVirtualClusterProps:
    def __init__(
        self,
        *,
        container_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVirtualCluster``.

        :param container_provider: The container provider of the virtual cluster.
        :param name: The name of the virtual cluster.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrcontainers as emrcontainers
            
            cfn_virtual_cluster_props = emrcontainers.CfnVirtualClusterProps(
                container_provider=emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                    id="id",
                    info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                            namespace="namespace"
                        )
                    ),
                    type="type"
                ),
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f93ead2a436b8c5a2fc364fff5d9da849a851543aa1433cd7ab649d79d55f9)
            check_type(argname="argument container_provider", value=container_provider, expected_type=type_hints["container_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_provider": container_provider,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def container_provider(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnVirtualCluster.ContainerProviderProperty]:
        '''The container provider of the virtual cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-containerprovider
        '''
        result = self._values.get("container_provider")
        assert result is not None, "Required property 'container_provider' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnVirtualCluster.ContainerProviderProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the virtual cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnVirtualCluster",
    "CfnVirtualClusterProps",
]

publication.publish()

def _typecheckingstub__a06dc2760ceb0de7a449a23941f15987094157d1a540c30fa67c9e49a3e06101(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    container_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802f118bbdec329d651201f6f69836e8e9523c47d32a262a55c4813747ccf78c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3035614e8641a59d4a7600ad906f142054401a42e6c1ca14df8b5d57d08f0823(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__617f2c6bc289034f068a4b514139fc0bee8f6455f589c3e2de7ee7fb7a3a92e3(
    value: typing.Union[_IResolvable_da3f097b, CfnVirtualCluster.ContainerProviderProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea4d0052a5a6cb82d57b5655349988466e02d75bbcc22aec370e6810b4c382d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3436f23ae2ca4313aacb96519980906e71e5bc37e7a466a53353480f948e674(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5baf7a38335e2eb8733f2aa2d96a9593d774d095fb8a05dcf1d8bd22323050(
    *,
    eks_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.EksInfoProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19801d68aea5b7c69bfd60c7d9c690e62c4643fe80fcda956e884f367b8b1dcf(
    *,
    id: builtins.str,
    info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.ContainerInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26be72236c14a8878e3d92d7b17397aa49c8a844f85e9e98c958600dd7a08c8f(
    *,
    namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f93ead2a436b8c5a2fc364fff5d9da849a851543aa1433cd7ab649d79d55f9(
    *,
    container_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
