'''
# AWS::ResourceExplorer2 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_resourceexplorer2 as resourceexplorer2
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ResourceExplorer2 construct libraries](https://constructs.dev/search?q=resourceexplorer2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ResourceExplorer2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResourceExplorer2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ResourceExplorer2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResourceExplorer2.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDefaultViewAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_resourceexplorer2.CfnDefaultViewAssociation",
):
    '''Sets the specified view as the default for the AWS Region in which you call this operation.

    If a user makes a search query that doesn't explicitly specify the view to use, Resource Explorer chooses this default view automatically for searches performed in this AWS Region .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_resourceexplorer2 as resourceexplorer2
        
        cfn_default_view_association = resourceexplorer2.CfnDefaultViewAssociation(self, "MyCfnDefaultViewAssociation",
            view_arn="viewArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        view_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param view_arn: The ARN of the view to set as the default for the AWS Region and AWS account in which you call this operation. The specified view must already exist in the specified Region.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63112644362183375393f464fd83dd8b1bd993c1724b0718d649f4624fa4242b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDefaultViewAssociationProps(view_arn=view_arn)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cef124cf4de616cdbfaa59c7b45ccb3cf247ebacf5072b55cc719a3b6e6d1499)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd920c7487b699e37154cd1ba3a752af6eb4789ed12a7c8762c530b9f1440b9a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedAwsPrincipal")
    def attr_associated_aws_principal(self) -> builtins.str:
        '''The unique identifier of the principal for which the specified view was made the default for the AWS Region that contains the view.

        For example:

        ``123456789012``

        :cloudformationAttribute: AssociatedAwsPrincipal
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociatedAwsPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="viewArn")
    def view_arn(self) -> builtins.str:
        '''The ARN of the view to set as the default for the AWS Region and AWS account in which you call this operation.'''
        return typing.cast(builtins.str, jsii.get(self, "viewArn"))

    @view_arn.setter
    def view_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d34137c13dccff8aec091fe498d52117edd5707c82c68e72ee608bacd180f14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_resourceexplorer2.CfnDefaultViewAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"view_arn": "viewArn"},
)
class CfnDefaultViewAssociationProps:
    def __init__(self, *, view_arn: builtins.str) -> None:
        '''Properties for defining a ``CfnDefaultViewAssociation``.

        :param view_arn: The ARN of the view to set as the default for the AWS Region and AWS account in which you call this operation. The specified view must already exist in the specified Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_resourceexplorer2 as resourceexplorer2
            
            cfn_default_view_association_props = resourceexplorer2.CfnDefaultViewAssociationProps(
                view_arn="viewArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2ff822be1f978fdc7b240f4ff3072e84a4b31cfb5ccb5f4c3f0c27293713d42)
            check_type(argname="argument view_arn", value=view_arn, expected_type=type_hints["view_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "view_arn": view_arn,
        }

    @builtins.property
    def view_arn(self) -> builtins.str:
        '''The ARN of the view to set as the default for the AWS Region and AWS account in which you call this operation.

        The specified view must already exist in the specified Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.html#cfn-resourceexplorer2-defaultviewassociation-viewarn
        '''
        result = self._values.get("view_arn")
        assert result is not None, "Required property 'view_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultViewAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnIndex(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_resourceexplorer2.CfnIndex",
):
    '''Turns on Resource Explorer in the AWS Region in which you called this operation by creating an index.

    Resource Explorer begins discovering the resources in this Region and stores the details about the resources in the index so that they can be queried by using the `Search <https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html>`_ operation.

    You can create either a local index that returns search results from only the AWS Region in which the index exists, or you can create an aggregator index that returns search results from all AWS Regions in the AWS account .

    For more details about what happens when you turn on Resource Explorer in an AWS Region , see `Turning on Resource Explorer to index your resources in an AWS Region <https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-activate.html>`_ in the *AWS Resource Explorer User Guide.*

    If this is the first AWS Region in which you've created an index for Resource Explorer, this operation also creates a service-linked role in your AWS account that allows Resource Explorer to search for your resources and populate the index.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_resourceexplorer2 as resourceexplorer2
        
        cfn_index = resourceexplorer2.CfnIndex(self, "MyCfnIndex",
            type="type",
        
            # the properties below are optional
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param type: Specifies the type of the index in this Region. For information about the aggregator index and how it differs from a local index, see `Turning on cross-Region search by creating an aggregator index <https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html>`_ in the *AWS Resource Explorer User Guide.* .
        :param tags: The specified tags are attached to only the index created in this AWS Region . The tags don't attach to any of the resources listed in the index.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__accccd442e137b2533911bfe6a9c63d90b98a01337a2c8e9c58697e0848fb88e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIndexProps(type=type, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9868b671e46d1bbfcbe098b2349183185ded8e3b83f1d5b803364752d2cc285a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b638862b412603d6dd583664fa4630195d0701c2ccda99715eb025e6f3466ae)
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
        '''The ARN of the new index for the AWS Region . For example:.

        ``arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIndexState")
    def attr_index_state(self) -> builtins.str:
        '''Indicates the current state of the index. For example:.

        ``CREATING``

        :cloudformationAttribute: IndexState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIndexState"))

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
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Specifies the type of the index in this Region.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee8250a3f3491b042dbc508f663480728f7a2654be50c8b46f65888be7b7086e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The specified tags are attached to only the index created in this AWS Region .'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cf3e59046bbed69cac69bb9d9a3fcb94f8253aa6c2753a213e4e0970930dbf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_resourceexplorer2.CfnIndexProps",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "tags": "tags"},
)
class CfnIndexProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIndex``.

        :param type: Specifies the type of the index in this Region. For information about the aggregator index and how it differs from a local index, see `Turning on cross-Region search by creating an aggregator index <https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html>`_ in the *AWS Resource Explorer User Guide.* .
        :param tags: The specified tags are attached to only the index created in this AWS Region . The tags don't attach to any of the resources listed in the index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_resourceexplorer2 as resourceexplorer2
            
            cfn_index_props = resourceexplorer2.CfnIndexProps(
                type="type",
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07785dc50db019a4bae6a0b2472b82a77afbee3276a6e6212049584d8dce9628)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def type(self) -> builtins.str:
        '''Specifies the type of the index in this Region.

        For information about the aggregator index and how it differs from a local index, see `Turning on cross-Region search by creating an aggregator index <https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html>`_ in the *AWS Resource Explorer User Guide.* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html#cfn-resourceexplorer2-index-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The specified tags are attached to only the index created in this AWS Region .

        The tags don't attach to any of the resources listed in the index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html#cfn-resourceexplorer2-index-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnView(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_resourceexplorer2.CfnView",
):
    '''Creates a view that users can query by using the `Search <https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html>`_ operation. Results from queries that you make using this view include only resources that match the view's ``Filters`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_resourceexplorer2 as resourceexplorer2
        
        cfn_view = resourceexplorer2.CfnView(self, "MyCfnView",
            view_name="viewName",
        
            # the properties below are optional
            filters=resourceexplorer2.CfnView.FiltersProperty(
                filter_string="filterString"
            ),
            included_properties=[resourceexplorer2.CfnView.IncludedPropertyProperty(
                name="name"
            )],
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        view_name: builtins.str,
        filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnView.FiltersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        included_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnView.IncludedPropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param view_name: The name of the new view.
        :param filters: An array of strings that include search keywords, prefixes, and operators that filter the results that are returned for queries made using this view. When you use this view in a `Search <https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html>`_ operation, the filter string is combined with the search's ``QueryString`` parameter using a logical ``AND`` operator. For information about the supported syntax, see `Search query reference for Resource Explorer <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html>`_ in the *AWS Resource Explorer User Guide* . .. epigraph:: This query string in the context of this operation supports only `filter prefixes <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters>`_ with optional `operators <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators>`_ . It doesn't support free-form text. For example, the string ``region:us* service:ec2 -tag:stage=prod`` includes all Amazon EC2 resources in any AWS Region that begin with the letters ``us`` and are *not* tagged with a key ``Stage`` that has the value ``prod`` .
        :param included_properties: A list of fields that provide additional information about the view.
        :param tags: Tag key and value pairs that are attached to the view.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f124943049ede771902c48eecbb29bb165c5c4c2d774e691c255a756964e18a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnViewProps(
            view_name=view_name,
            filters=filters,
            included_properties=included_properties,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f690df80d2c072a8fce4e6d89c310169f5b269e2ad04155ed5955fe3df76fa9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__69c823ae1d0498dc7396a55c7efdfcce450fd73eb89e8abb06b9dddc537607b6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrViewArn")
    def attr_view_arn(self) -> builtins.str:
        '''The ARN of the new view. For example:.

        ``arn:aws:resource-explorer-2:us-east-1:123456789012:view/MyView/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222``

        :cloudformationAttribute: ViewArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrViewArn"))

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
    @jsii.member(jsii_name="viewName")
    def view_name(self) -> builtins.str:
        '''The name of the new view.'''
        return typing.cast(builtins.str, jsii.get(self, "viewName"))

    @view_name.setter
    def view_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34b0928f3062cee9252036904eb9ab259165c1538d4a06b7a8dd389f9c54c008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewName", value)

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnView.FiltersProperty"]]:
        '''An array of strings that include search keywords, prefixes, and operators that filter the results that are returned for queries made using this view.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnView.FiltersProperty"]], jsii.get(self, "filters"))

    @filters.setter
    def filters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnView.FiltersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5fb01321040e194a5b4764d6eb89a25f4149cfd8bf5c274c004d722fdfc3ac9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filters", value)

    @builtins.property
    @jsii.member(jsii_name="includedProperties")
    def included_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnView.IncludedPropertyProperty"]]]]:
        '''A list of fields that provide additional information about the view.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnView.IncludedPropertyProperty"]]]], jsii.get(self, "includedProperties"))

    @included_properties.setter
    def included_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnView.IncludedPropertyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a4f8894d1b066b915e6771816801795e9d3e2fe0de81b028355665ff6ec0bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedProperties", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tag key and value pairs that are attached to the view.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba074542162150148d90cb3cc2f181855f03e4ed820e7ceba4ad32404363e0a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resourceexplorer2.CfnView.FiltersProperty",
        jsii_struct_bases=[],
        name_mapping={"filter_string": "filterString"},
    )
    class FiltersProperty:
        def __init__(self, *, filter_string: builtins.str) -> None:
            '''An object with a ``FilterString`` that specifies which resources to include in the results of queries made using this view.

            :param filter_string: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-filters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resourceexplorer2 as resourceexplorer2
                
                filters_property = resourceexplorer2.CfnView.FiltersProperty(
                    filter_string="filterString"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf41fccad0321607e35d5e689530c4ced25681bfd4c6eead0799e7be5371e21f)
                check_type(argname="argument filter_string", value=filter_string, expected_type=type_hints["filter_string"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filter_string": filter_string,
            }

        @builtins.property
        def filter_string(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-filters.html#cfn-resourceexplorer2-view-filters-filterstring
            '''
            result = self._values.get("filter_string")
            assert result is not None, "Required property 'filter_string' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FiltersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resourceexplorer2.CfnView.IncludedPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class IncludedPropertyProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''Information about an additional property that describes a resource, that you can optionally include in a view.

            :param name: The name of the property that is included in this view.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-includedproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resourceexplorer2 as resourceexplorer2
                
                included_property_property = resourceexplorer2.CfnView.IncludedPropertyProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b2008d74d735dee7e077ba99ee91afcce783365dbdad581b46682239d77c928)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the property that is included in this view.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-includedproperty.html#cfn-resourceexplorer2-view-includedproperty-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IncludedPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_resourceexplorer2.CfnViewProps",
    jsii_struct_bases=[],
    name_mapping={
        "view_name": "viewName",
        "filters": "filters",
        "included_properties": "includedProperties",
        "tags": "tags",
    },
)
class CfnViewProps:
    def __init__(
        self,
        *,
        view_name: builtins.str,
        filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnView.FiltersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        included_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnView.IncludedPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnView``.

        :param view_name: The name of the new view.
        :param filters: An array of strings that include search keywords, prefixes, and operators that filter the results that are returned for queries made using this view. When you use this view in a `Search <https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html>`_ operation, the filter string is combined with the search's ``QueryString`` parameter using a logical ``AND`` operator. For information about the supported syntax, see `Search query reference for Resource Explorer <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html>`_ in the *AWS Resource Explorer User Guide* . .. epigraph:: This query string in the context of this operation supports only `filter prefixes <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters>`_ with optional `operators <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators>`_ . It doesn't support free-form text. For example, the string ``region:us* service:ec2 -tag:stage=prod`` includes all Amazon EC2 resources in any AWS Region that begin with the letters ``us`` and are *not* tagged with a key ``Stage`` that has the value ``prod`` .
        :param included_properties: A list of fields that provide additional information about the view.
        :param tags: Tag key and value pairs that are attached to the view.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_resourceexplorer2 as resourceexplorer2
            
            cfn_view_props = resourceexplorer2.CfnViewProps(
                view_name="viewName",
            
                # the properties below are optional
                filters=resourceexplorer2.CfnView.FiltersProperty(
                    filter_string="filterString"
                ),
                included_properties=[resourceexplorer2.CfnView.IncludedPropertyProperty(
                    name="name"
                )],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d2ab4fc7971aa574280f08b92f4a9047a7bd1d73b33d97e446ef83034b5e8d)
            check_type(argname="argument view_name", value=view_name, expected_type=type_hints["view_name"])
            check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            check_type(argname="argument included_properties", value=included_properties, expected_type=type_hints["included_properties"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "view_name": view_name,
        }
        if filters is not None:
            self._values["filters"] = filters
        if included_properties is not None:
            self._values["included_properties"] = included_properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def view_name(self) -> builtins.str:
        '''The name of the new view.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-viewname
        '''
        result = self._values.get("view_name")
        assert result is not None, "Required property 'view_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnView.FiltersProperty]]:
        '''An array of strings that include search keywords, prefixes, and operators that filter the results that are returned for queries made using this view.

        When you use this view in a `Search <https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html>`_ operation, the filter string is combined with the search's ``QueryString`` parameter using a logical ``AND`` operator.

        For information about the supported syntax, see `Search query reference for Resource Explorer <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html>`_ in the *AWS Resource Explorer User Guide* .
        .. epigraph::

           This query string in the context of this operation supports only `filter prefixes <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters>`_ with optional `operators <https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators>`_ . It doesn't support free-form text. For example, the string ``region:us* service:ec2 -tag:stage=prod`` includes all Amazon EC2 resources in any AWS Region that begin with the letters ``us`` and are *not* tagged with a key ``Stage`` that has the value ``prod`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-filters
        '''
        result = self._values.get("filters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnView.FiltersProperty]], result)

    @builtins.property
    def included_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnView.IncludedPropertyProperty]]]]:
        '''A list of fields that provide additional information about the view.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-includedproperties
        '''
        result = self._values.get("included_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnView.IncludedPropertyProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tag key and value pairs that are attached to the view.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnViewProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDefaultViewAssociation",
    "CfnDefaultViewAssociationProps",
    "CfnIndex",
    "CfnIndexProps",
    "CfnView",
    "CfnViewProps",
]

publication.publish()

def _typecheckingstub__63112644362183375393f464fd83dd8b1bd993c1724b0718d649f4624fa4242b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    view_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cef124cf4de616cdbfaa59c7b45ccb3cf247ebacf5072b55cc719a3b6e6d1499(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd920c7487b699e37154cd1ba3a752af6eb4789ed12a7c8762c530b9f1440b9a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d34137c13dccff8aec091fe498d52117edd5707c82c68e72ee608bacd180f14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2ff822be1f978fdc7b240f4ff3072e84a4b31cfb5ccb5f4c3f0c27293713d42(
    *,
    view_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__accccd442e137b2533911bfe6a9c63d90b98a01337a2c8e9c58697e0848fb88e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    type: builtins.str,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9868b671e46d1bbfcbe098b2349183185ded8e3b83f1d5b803364752d2cc285a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b638862b412603d6dd583664fa4630195d0701c2ccda99715eb025e6f3466ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee8250a3f3491b042dbc508f663480728f7a2654be50c8b46f65888be7b7086e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf3e59046bbed69cac69bb9d9a3fcb94f8253aa6c2753a213e4e0970930dbf4(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07785dc50db019a4bae6a0b2472b82a77afbee3276a6e6212049584d8dce9628(
    *,
    type: builtins.str,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f124943049ede771902c48eecbb29bb165c5c4c2d774e691c255a756964e18a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    view_name: builtins.str,
    filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnView.FiltersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    included_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnView.IncludedPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f690df80d2c072a8fce4e6d89c310169f5b269e2ad04155ed5955fe3df76fa9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c823ae1d0498dc7396a55c7efdfcce450fd73eb89e8abb06b9dddc537607b6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34b0928f3062cee9252036904eb9ab259165c1538d4a06b7a8dd389f9c54c008(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5fb01321040e194a5b4764d6eb89a25f4149cfd8bf5c274c004d722fdfc3ac9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnView.FiltersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a4f8894d1b066b915e6771816801795e9d3e2fe0de81b028355665ff6ec0bf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnView.IncludedPropertyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba074542162150148d90cb3cc2f181855f03e4ed820e7ceba4ad32404363e0a8(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf41fccad0321607e35d5e689530c4ced25681bfd4c6eead0799e7be5371e21f(
    *,
    filter_string: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2008d74d735dee7e077ba99ee91afcce783365dbdad581b46682239d77c928(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d2ab4fc7971aa574280f08b92f4a9047a7bd1d73b33d97e446ef83034b5e8d(
    *,
    view_name: builtins.str,
    filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnView.FiltersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    included_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnView.IncludedPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
