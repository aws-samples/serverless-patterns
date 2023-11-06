'''
# AWS::Route53RecoveryReadiness Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_route53recoveryreadiness as route53recoveryreadiness
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Route53RecoveryReadiness construct libraries](https://constructs.dev/search?q=route53recoveryreadiness)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Route53RecoveryReadiness resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53RecoveryReadiness.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Route53RecoveryReadiness](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53RecoveryReadiness.html).

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
class CfnCell(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnCell",
):
    '''Creates a cell in recovery group in Amazon Route 53 Application Recovery Controller.

    A cell in Route 53 ARC represents replicas or independent units of failover in your application. It groups within it all the AWS resources that are necessary for your application to run independently. Typically, you would have define one set of resources in a primary cell and another set in a standby cell in your recovery group.

    After you set up the cells for your application, you can create readiness checks in Route 53 ARC to continually audit readiness for AWS resource quotas, capacity, network routing policies, and other predefined rules.

    You can set up notifications about changes that would affect your ability to fail over to a replica and recover. However, you should make decisions about whether to fail away from or to a replica based on your monitoring and health check systems. You should consider readiness checks as a complementary service to those systems.

    Route 53 ARC Readiness supports us-east-1 and us-west-2 AWS Regions only.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
        
        cfn_cell = route53recoveryreadiness.CfnCell(self, "MyCfnCell",
            cell_name="cellName",
            cells=["cells"],
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
        cell_name: typing.Optional[builtins.str] = None,
        cells: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cell_name: The name of the cell to create.
        :param cells: A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific AWS Regions .
        :param tags: A collection of tags associated with a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13c868895ca08bff854c8fe7678338e1867e993f867d49908046cd6a17629e31)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCellProps(cell_name=cell_name, cells=cells, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26df4eeedb5a0c616a1f3dad8c75f078f50e698da7a0e84e3a5d5735d6c00031)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d601dfd1114a47f09e8e4cc5e2fc61a0bc1bf8d65d07fa8a618424b7fe19fba)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCellArn")
    def attr_cell_arn(self) -> builtins.str:
        '''The ARN of the cell.

        :cloudformationAttribute: CellArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCellArn"))

    @builtins.property
    @jsii.member(jsii_name="attrParentReadinessScopes")
    def attr_parent_readiness_scopes(self) -> typing.List[builtins.str]:
        '''The readiness scope for the cell, which can be the Amazon Resource Name (ARN) of a cell or the ARN of a recovery group.

        Although this is a list, it can currently have only one element.

        :cloudformationAttribute: ParentReadinessScopes
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrParentReadinessScopes"))

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
    @jsii.member(jsii_name="cellName")
    def cell_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cell to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cellName"))

    @cell_name.setter
    def cell_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63cf36126d8dd3b5e19180b0442de9842488ed8e561e44cde76e6ed852c19ad8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cellName", value)

    @builtins.property
    @jsii.member(jsii_name="cells")
    def cells(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cells"))

    @cells.setter
    def cells(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e9f11291a25b5e6f4ae9c7ac92db4cdc610f3d4102f4a96a81ba897fa1d87a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cells", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62f10011bc9a0c74b1e4ea8cc9c9bbf3a0a134a424b6f640abf9c44879051377)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnCellProps",
    jsii_struct_bases=[],
    name_mapping={"cell_name": "cellName", "cells": "cells", "tags": "tags"},
)
class CfnCellProps:
    def __init__(
        self,
        *,
        cell_name: typing.Optional[builtins.str] = None,
        cells: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCell``.

        :param cell_name: The name of the cell to create.
        :param cells: A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific AWS Regions .
        :param tags: A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
            
            cfn_cell_props = route53recoveryreadiness.CfnCellProps(
                cell_name="cellName",
                cells=["cells"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__073034bd9956a2710068070b5d811ab42b3869de8e1a5c263d9e23a04df0cdfe)
            check_type(argname="argument cell_name", value=cell_name, expected_type=type_hints["cell_name"])
            check_type(argname="argument cells", value=cells, expected_type=type_hints["cells"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cell_name is not None:
            self._values["cell_name"] = cell_name
        if cells is not None:
            self._values["cells"] = cells
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cell_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cell to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cellname
        '''
        result = self._values.get("cell_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cells(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells.

        For example, Availability Zones within specific AWS Regions .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cells
        '''
        result = self._values.get("cells")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCellProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnReadinessCheck(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnReadinessCheck",
):
    '''Creates a readiness check in Amazon Route 53 Application Recovery Controller.

    A readiness check continually monitors a resource set in your application, such as a set of Amazon Aurora instances, that Route 53 ARC is auditing recovery readiness for. The audits run once every minute on every resource that's associated with a readiness check.

    Every resource type has a set of rules associated with it that Route 53 ARC uses to audit resources for readiness. For more information, see `Readiness rules descriptions <https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.rules-resources.html>`_ in the Amazon Route 53 Application Recovery Controller Developer Guide.

    Route 53 ARC Readiness supports us-east-1 and us-west-2 AWS Regions only.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
        
        cfn_readiness_check = route53recoveryreadiness.CfnReadinessCheck(self, "MyCfnReadinessCheck",
            readiness_check_name="readinessCheckName",
            resource_set_name="resourceSetName",
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
        readiness_check_name: typing.Optional[builtins.str] = None,
        resource_set_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param readiness_check_name: The name of the readiness check to create.
        :param resource_set_name: The name of the resource set to check.
        :param tags: A collection of tags associated with a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bfbc5fa46ba2840c24892c634f80e8275ce2c76eb60922ee3c04a4b324e5b29)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReadinessCheckProps(
            readiness_check_name=readiness_check_name,
            resource_set_name=resource_set_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc7ffe6a29dd5f6e715a9726b09f80833380e0fbe980f5834be46b1ccd41b66)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6e1cff4db070736f87d566522f4b3545a4ad286947133e85c7ced4c96cedc81)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrReadinessCheckArn")
    def attr_readiness_check_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the readiness check.

        :cloudformationAttribute: ReadinessCheckArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReadinessCheckArn"))

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
    @jsii.member(jsii_name="readinessCheckName")
    def readiness_check_name(self) -> typing.Optional[builtins.str]:
        '''The name of the readiness check to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readinessCheckName"))

    @readiness_check_name.setter
    def readiness_check_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f3539c459e090a80aab3f1856cae71bbd8d5f0f2c8667cf9e39d7014435f965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readinessCheckName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceSetName")
    def resource_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the resource set to check.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceSetName"))

    @resource_set_name.setter
    def resource_set_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44d71b9a26b0dfffda11f6844c9805bb334cdaf3e1a1e32bcd05e04e31050f43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceSetName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e79dc3aec0a3b3131b20694a730ecd7706f552f333a9b6a0ddcd951311d439c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnReadinessCheckProps",
    jsii_struct_bases=[],
    name_mapping={
        "readiness_check_name": "readinessCheckName",
        "resource_set_name": "resourceSetName",
        "tags": "tags",
    },
)
class CfnReadinessCheckProps:
    def __init__(
        self,
        *,
        readiness_check_name: typing.Optional[builtins.str] = None,
        resource_set_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReadinessCheck``.

        :param readiness_check_name: The name of the readiness check to create.
        :param resource_set_name: The name of the resource set to check.
        :param tags: A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
            
            cfn_readiness_check_props = route53recoveryreadiness.CfnReadinessCheckProps(
                readiness_check_name="readinessCheckName",
                resource_set_name="resourceSetName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3c438502ee1a60d4adaea3215d352734901afcdf6cd40ef143a801e67d7e601)
            check_type(argname="argument readiness_check_name", value=readiness_check_name, expected_type=type_hints["readiness_check_name"])
            check_type(argname="argument resource_set_name", value=resource_set_name, expected_type=type_hints["resource_set_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if readiness_check_name is not None:
            self._values["readiness_check_name"] = readiness_check_name
        if resource_set_name is not None:
            self._values["resource_set_name"] = resource_set_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def readiness_check_name(self) -> typing.Optional[builtins.str]:
        '''The name of the readiness check to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname
        '''
        result = self._values.get("readiness_check_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the resource set to check.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname
        '''
        result = self._values.get("resource_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReadinessCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRecoveryGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnRecoveryGroup",
):
    '''Creates a recovery group in Amazon Route 53 Application Recovery Controller.

    A recovery group represents your application. It typically consists of two or more cells that are replicas of each other in terms of resources and functionality, so that you can fail over from one to the other, for example, from one Region to another. You create recovery groups so you can use readiness checks to audit resources in your application.

    For more information, see `Readiness checks, resource sets, and readiness scopes <https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.readiness-scope.html>`_ in the Amazon Route 53 Application Recovery Controller Developer Guide.

    Route 53 ARC Readiness supports us-east-1 and us-west-2 AWS Regions only.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
        
        cfn_recovery_group = route53recoveryreadiness.CfnRecoveryGroup(self, "MyCfnRecoveryGroup",
            cells=["cells"],
            recovery_group_name="recoveryGroupName",
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
        cells: typing.Optional[typing.Sequence[builtins.str]] = None,
        recovery_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cells: A list of the cell Amazon Resource Names (ARNs) in the recovery group.
        :param recovery_group_name: The name of the recovery group to create.
        :param tags: A collection of tags associated with a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99277ba24eed449052f2cdf23737421f1433215fdc3cfd730a4385c704b3d713)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRecoveryGroupProps(
            cells=cells, recovery_group_name=recovery_group_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db42d74a58f7864ec5ade4f46151f65d1fa1d6ce64c6818e481b49190794f1ef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f57608369ed24b503beb8852606ac5b02696eec54ae288e3e1b88defdd9c7816)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRecoveryGroupArn")
    def attr_recovery_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the recovery group.

        :cloudformationAttribute: RecoveryGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRecoveryGroupArn"))

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
    @jsii.member(jsii_name="cells")
    def cells(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the cell Amazon Resource Names (ARNs) in the recovery group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cells"))

    @cells.setter
    def cells(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5560294538ccfc7bb97ce8e2648a8ee6987e7a11a8852c027f1ae32197b5ced6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cells", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryGroupName")
    def recovery_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the recovery group to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryGroupName"))

    @recovery_group_name.setter
    def recovery_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e7b96d2a45ee2f819b9208f20855952769d9f0b63ad222e9e8c5279db457c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5466e3c5b9c14b878f6f4476a3156bdb5bc5565b79e490b847655152995e7ee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnRecoveryGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "cells": "cells",
        "recovery_group_name": "recoveryGroupName",
        "tags": "tags",
    },
)
class CfnRecoveryGroupProps:
    def __init__(
        self,
        *,
        cells: typing.Optional[typing.Sequence[builtins.str]] = None,
        recovery_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRecoveryGroup``.

        :param cells: A list of the cell Amazon Resource Names (ARNs) in the recovery group.
        :param recovery_group_name: The name of the recovery group to create.
        :param tags: A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
            
            cfn_recovery_group_props = route53recoveryreadiness.CfnRecoveryGroupProps(
                cells=["cells"],
                recovery_group_name="recoveryGroupName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d342dcd3563435baa37fbbe16fdf0ff7b67201aa0844f5e1cf9d141d0bf9cd7)
            check_type(argname="argument cells", value=cells, expected_type=type_hints["cells"])
            check_type(argname="argument recovery_group_name", value=recovery_group_name, expected_type=type_hints["recovery_group_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cells is not None:
            self._values["cells"] = cells
        if recovery_group_name is not None:
            self._values["recovery_group_name"] = recovery_group_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cells(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the cell Amazon Resource Names (ARNs) in the recovery group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-cells
        '''
        result = self._values.get("cells")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def recovery_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the recovery group to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-recoverygroupname
        '''
        result = self._values.get("recovery_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A collection of tags associated with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecoveryGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnResourceSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnResourceSet",
):
    '''Creates a resource set in Amazon Route 53 Application Recovery Controller.

    A resource set is a set of resources of one type, such as Network Load Balancers, that span multiple cells. You can associate a resource set with a readiness check to have Route 53 ARC continually monitor the resources in the set for failover readiness.

    You typically create a resource set and a readiness check for each supported type of AWS resource in your application.

    For more information, see `Readiness checks, resource sets, and readiness scopes <https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.readiness-scope.html>`_ in the Amazon Route 53 Application Recovery Controller Developer Guide.

    Route 53 ARC Readiness supports us-east-1 and us-west-2 AWS Regions only.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
        
        cfn_resource_set = route53recoveryreadiness.CfnResourceSet(self, "MyCfnResourceSet",
            resources=[route53recoveryreadiness.CfnResourceSet.ResourceProperty(
                component_id="componentId",
                dns_target_resource=route53recoveryreadiness.CfnResourceSet.DNSTargetResourceProperty(
                    domain_name="domainName",
                    hosted_zone_arn="hostedZoneArn",
                    record_set_id="recordSetId",
                    record_type="recordType",
                    target_resource=route53recoveryreadiness.CfnResourceSet.TargetResourceProperty(
                        nlb_resource=route53recoveryreadiness.CfnResourceSet.NLBResourceProperty(
                            arn="arn"
                        ),
                        r53_resource=route53recoveryreadiness.CfnResourceSet.R53ResourceRecordProperty(
                            domain_name="domainName",
                            record_set_id="recordSetId"
                        )
                    )
                ),
                readiness_scopes=["readinessScopes"],
                resource_arn="resourceArn"
            )],
            resource_set_type="resourceSetType",
        
            # the properties below are optional
            resource_set_name="resourceSetName",
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
        resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceSet.ResourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        resource_set_type: builtins.str,
        resource_set_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resources: A list of resource objects in the resource set.
        :param resource_set_type: The resource type of the resources in the resource set. Enter one of the following values for resource type:. AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource. Note that AWS::Route53RecoveryReadiness::DNSTargetResource is only used for this setting. It isn't an actual AWS CloudFormation resource type.
        :param resource_set_name: The name of the resource set to create.
        :param tags: A tag to associate with the parameters for a resource set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf6ebc0a9f935f88e0a23244138eb8cafe24b7630a5d785402d2354855596ebf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceSetProps(
            resources=resources,
            resource_set_type=resource_set_type,
            resource_set_name=resource_set_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fef85644281cf421ef43660e50fdbdb7916d6d66f698ce5050c537f21b4acc67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d1ced2fffee0146aab77f129ff62ca87caa55cd5db0cbf2406e2baa2d316e27)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceSetArn")
    def attr_resource_set_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource set.

        :cloudformationAttribute: ResourceSetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceSetArn"))

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
    @jsii.member(jsii_name="resources")
    def resources(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.ResourceProperty"]]]:
        '''A list of resource objects in the resource set.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.ResourceProperty"]]], jsii.get(self, "resources"))

    @resources.setter
    def resources(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.ResourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4df7976fde8840dbbd29fd87b41d6fde568c4d3f43e84abd295e34dc123b85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="resourceSetType")
    def resource_set_type(self) -> builtins.str:
        '''The resource type of the resources in the resource set.

        Enter one of the following values for resource type:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceSetType"))

    @resource_set_type.setter
    def resource_set_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16cdb7ef88bcfa5e79a6b24f5a7afa77f90bc848a7011c10d11293035c9283fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceSetType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceSetName")
    def resource_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the resource set to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceSetName"))

    @resource_set_name.setter
    def resource_set_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d8323a736d4d8bc880e1dd4c2787e873cd4353286043e264ff9457c074a93d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceSetName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A tag to associate with the parameters for a resource set.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8ce7b0dd37445da5365919573096496787ce1ddd7ea67b054df32684fa0cb5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnResourceSet.DNSTargetResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "domain_name": "domainName",
            "hosted_zone_arn": "hostedZoneArn",
            "record_set_id": "recordSetId",
            "record_type": "recordType",
            "target_resource": "targetResource",
        },
    )
    class DNSTargetResourceProperty:
        def __init__(
            self,
            *,
            domain_name: typing.Optional[builtins.str] = None,
            hosted_zone_arn: typing.Optional[builtins.str] = None,
            record_set_id: typing.Optional[builtins.str] = None,
            record_type: typing.Optional[builtins.str] = None,
            target_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceSet.TargetResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A component for DNS/routing control readiness checks and architecture checks.

            :param domain_name: The domain name that acts as an ingress point to a portion of the customer application.
            :param hosted_zone_arn: The hosted zone Amazon Resource Name (ARN) that contains the DNS record with the provided name of the target resource.
            :param record_set_id: The Amazon Route 53 record set ID that uniquely identifies a DNS record, given a name and a type.
            :param record_type: The type of DNS record of the target resource.
            :param target_resource: The target resource that the Route 53 record points to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
                
                d_nSTarget_resource_property = route53recoveryreadiness.CfnResourceSet.DNSTargetResourceProperty(
                    domain_name="domainName",
                    hosted_zone_arn="hostedZoneArn",
                    record_set_id="recordSetId",
                    record_type="recordType",
                    target_resource=route53recoveryreadiness.CfnResourceSet.TargetResourceProperty(
                        nlb_resource=route53recoveryreadiness.CfnResourceSet.NLBResourceProperty(
                            arn="arn"
                        ),
                        r53_resource=route53recoveryreadiness.CfnResourceSet.R53ResourceRecordProperty(
                            domain_name="domainName",
                            record_set_id="recordSetId"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__32358efbe7c385e7d76edfec00d6be4356e94128de2d64a8d0ace0fa96702e2c)
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument hosted_zone_arn", value=hosted_zone_arn, expected_type=type_hints["hosted_zone_arn"])
                check_type(argname="argument record_set_id", value=record_set_id, expected_type=type_hints["record_set_id"])
                check_type(argname="argument record_type", value=record_type, expected_type=type_hints["record_type"])
                check_type(argname="argument target_resource", value=target_resource, expected_type=type_hints["target_resource"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if domain_name is not None:
                self._values["domain_name"] = domain_name
            if hosted_zone_arn is not None:
                self._values["hosted_zone_arn"] = hosted_zone_arn
            if record_set_id is not None:
                self._values["record_set_id"] = record_set_id
            if record_type is not None:
                self._values["record_type"] = record_type
            if target_resource is not None:
                self._values["target_resource"] = target_resource

        @builtins.property
        def domain_name(self) -> typing.Optional[builtins.str]:
            '''The domain name that acts as an ingress point to a portion of the customer application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-domainname
            '''
            result = self._values.get("domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hosted_zone_arn(self) -> typing.Optional[builtins.str]:
            '''The hosted zone Amazon Resource Name (ARN) that contains the DNS record with the provided name of the target resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-hostedzonearn
            '''
            result = self._values.get("hosted_zone_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_set_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon Route 53 record set ID that uniquely identifies a DNS record, given a name and a type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordsetid
            '''
            result = self._values.get("record_set_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_type(self) -> typing.Optional[builtins.str]:
            '''The type of DNS record of the target resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordtype
            '''
            result = self._values.get("record_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.TargetResourceProperty"]]:
            '''The target resource that the Route 53 record points to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-targetresource
            '''
            result = self._values.get("target_resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.TargetResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DNSTargetResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnResourceSet.NLBResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class NLBResourceProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''The Network Load Balancer resource that a DNS target resource points to.

            :param arn: The Network Load Balancer resource Amazon Resource Name (ARN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
                
                n_lBResource_property = route53recoveryreadiness.CfnResourceSet.NLBResourceProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__600815406b2a1e95c6a05550df4fc06db9418b487fd1d28b01318205286ef457)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The Network Load Balancer resource Amazon Resource Name (ARN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html#cfn-route53recoveryreadiness-resourceset-nlbresource-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NLBResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnResourceSet.R53ResourceRecordProperty",
        jsii_struct_bases=[],
        name_mapping={"domain_name": "domainName", "record_set_id": "recordSetId"},
    )
    class R53ResourceRecordProperty:
        def __init__(
            self,
            *,
            domain_name: typing.Optional[builtins.str] = None,
            record_set_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Amazon Route 53 resource that a DNS target resource record points to.

            :param domain_name: The DNS target domain name.
            :param record_set_id: The Amazon Route 53 Resource Record Set ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
                
                r53_resource_record_property = route53recoveryreadiness.CfnResourceSet.R53ResourceRecordProperty(
                    domain_name="domainName",
                    record_set_id="recordSetId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05047634c6d70b5f1c983a80d886ef2a301a0fc1ef82f3a4aa86d4063f4d0a68)
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument record_set_id", value=record_set_id, expected_type=type_hints["record_set_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if domain_name is not None:
                self._values["domain_name"] = domain_name
            if record_set_id is not None:
                self._values["record_set_id"] = record_set_id

        @builtins.property
        def domain_name(self) -> typing.Optional[builtins.str]:
            '''The DNS target domain name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-domainname
            '''
            result = self._values.get("domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_set_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon Route 53 Resource Record Set ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-recordsetid
            '''
            result = self._values.get("record_set_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "R53ResourceRecordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnResourceSet.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_id": "componentId",
            "dns_target_resource": "dnsTargetResource",
            "readiness_scopes": "readinessScopes",
            "resource_arn": "resourceArn",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            component_id: typing.Optional[builtins.str] = None,
            dns_target_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceSet.DNSTargetResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            readiness_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The resource element of a resource set.

            :param component_id: The component identifier of the resource, generated when DNS target resource is used.
            :param dns_target_resource: A component for DNS/routing control readiness checks. This is a required setting when ``ResourceSet`` ``ResourceSetType`` is set to ``AWS::Route53RecoveryReadiness::DNSTargetResource`` . Do not set it for any other ``ResourceSetType`` setting.
            :param readiness_scopes: The recovery group Amazon Resource Name (ARN) or the cell ARN that the readiness checks for this resource set are scoped to.
            :param resource_arn: The Amazon Resource Name (ARN) of the AWS resource. This is a required setting for all ``ResourceSet`` ``ResourceSetType`` settings except ``AWS::Route53RecoveryReadiness::DNSTargetResource`` . Do not set this when ``ResourceSetType`` is set to ``AWS::Route53RecoveryReadiness::DNSTargetResource`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
                
                resource_property = route53recoveryreadiness.CfnResourceSet.ResourceProperty(
                    component_id="componentId",
                    dns_target_resource=route53recoveryreadiness.CfnResourceSet.DNSTargetResourceProperty(
                        domain_name="domainName",
                        hosted_zone_arn="hostedZoneArn",
                        record_set_id="recordSetId",
                        record_type="recordType",
                        target_resource=route53recoveryreadiness.CfnResourceSet.TargetResourceProperty(
                            nlb_resource=route53recoveryreadiness.CfnResourceSet.NLBResourceProperty(
                                arn="arn"
                            ),
                            r53_resource=route53recoveryreadiness.CfnResourceSet.R53ResourceRecordProperty(
                                domain_name="domainName",
                                record_set_id="recordSetId"
                            )
                        )
                    ),
                    readiness_scopes=["readinessScopes"],
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__afec2888efa0ee04a661bcde195c3a04b092b5644744184d2c35c93c03801d07)
                check_type(argname="argument component_id", value=component_id, expected_type=type_hints["component_id"])
                check_type(argname="argument dns_target_resource", value=dns_target_resource, expected_type=type_hints["dns_target_resource"])
                check_type(argname="argument readiness_scopes", value=readiness_scopes, expected_type=type_hints["readiness_scopes"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_id is not None:
                self._values["component_id"] = component_id
            if dns_target_resource is not None:
                self._values["dns_target_resource"] = dns_target_resource
            if readiness_scopes is not None:
                self._values["readiness_scopes"] = readiness_scopes
            if resource_arn is not None:
                self._values["resource_arn"] = resource_arn

        @builtins.property
        def component_id(self) -> typing.Optional[builtins.str]:
            '''The component identifier of the resource, generated when DNS target resource is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-componentid
            '''
            result = self._values.get("component_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dns_target_resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.DNSTargetResourceProperty"]]:
            '''A component for DNS/routing control readiness checks.

            This is a required setting when ``ResourceSet`` ``ResourceSetType`` is set to ``AWS::Route53RecoveryReadiness::DNSTargetResource`` . Do not set it for any other ``ResourceSetType`` setting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-dnstargetresource
            '''
            result = self._values.get("dns_target_resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.DNSTargetResourceProperty"]], result)

        @builtins.property
        def readiness_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The recovery group Amazon Resource Name (ARN) or the cell ARN that the readiness checks for this resource set are scoped to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-readinessscopes
            '''
            result = self._values.get("readiness_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the AWS resource.

            This is a required setting for all ``ResourceSet`` ``ResourceSetType`` settings except ``AWS::Route53RecoveryReadiness::DNSTargetResource`` . Do not set this when ``ResourceSetType`` is set to ``AWS::Route53RecoveryReadiness::DNSTargetResource`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-resourcearn
            '''
            result = self._values.get("resource_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnResourceSet.TargetResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"nlb_resource": "nlbResource", "r53_resource": "r53Resource"},
    )
    class TargetResourceProperty:
        def __init__(
            self,
            *,
            nlb_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceSet.NLBResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            r53_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceSet.R53ResourceRecordProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The target resource that the Route 53 record points to.

            :param nlb_resource: The Network Load Balancer resource that a DNS target resource points to.
            :param r53_resource: The Route 53 resource that a DNS target resource record points to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
                
                target_resource_property = route53recoveryreadiness.CfnResourceSet.TargetResourceProperty(
                    nlb_resource=route53recoveryreadiness.CfnResourceSet.NLBResourceProperty(
                        arn="arn"
                    ),
                    r53_resource=route53recoveryreadiness.CfnResourceSet.R53ResourceRecordProperty(
                        domain_name="domainName",
                        record_set_id="recordSetId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16ba16f97722031f82a55ec2c9c68e5635ae95c709411fdf3cc1a49625a8b6da)
                check_type(argname="argument nlb_resource", value=nlb_resource, expected_type=type_hints["nlb_resource"])
                check_type(argname="argument r53_resource", value=r53_resource, expected_type=type_hints["r53_resource"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if nlb_resource is not None:
                self._values["nlb_resource"] = nlb_resource
            if r53_resource is not None:
                self._values["r53_resource"] = r53_resource

        @builtins.property
        def nlb_resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.NLBResourceProperty"]]:
            '''The Network Load Balancer resource that a DNS target resource points to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-nlbresource
            '''
            result = self._values.get("nlb_resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.NLBResourceProperty"]], result)

        @builtins.property
        def r53_resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.R53ResourceRecordProperty"]]:
            '''The Route 53 resource that a DNS target resource record points to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-r53resource
            '''
            result = self._values.get("r53_resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceSet.R53ResourceRecordProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53recoveryreadiness.CfnResourceSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "resources": "resources",
        "resource_set_type": "resourceSetType",
        "resource_set_name": "resourceSetName",
        "tags": "tags",
    },
)
class CfnResourceSetProps:
    def __init__(
        self,
        *,
        resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceSet.ResourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
        resource_set_type: builtins.str,
        resource_set_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceSet``.

        :param resources: A list of resource objects in the resource set.
        :param resource_set_type: The resource type of the resources in the resource set. Enter one of the following values for resource type:. AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource. Note that AWS::Route53RecoveryReadiness::DNSTargetResource is only used for this setting. It isn't an actual AWS CloudFormation resource type.
        :param resource_set_name: The name of the resource set to create.
        :param tags: A tag to associate with the parameters for a resource set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53recoveryreadiness as route53recoveryreadiness
            
            cfn_resource_set_props = route53recoveryreadiness.CfnResourceSetProps(
                resources=[route53recoveryreadiness.CfnResourceSet.ResourceProperty(
                    component_id="componentId",
                    dns_target_resource=route53recoveryreadiness.CfnResourceSet.DNSTargetResourceProperty(
                        domain_name="domainName",
                        hosted_zone_arn="hostedZoneArn",
                        record_set_id="recordSetId",
                        record_type="recordType",
                        target_resource=route53recoveryreadiness.CfnResourceSet.TargetResourceProperty(
                            nlb_resource=route53recoveryreadiness.CfnResourceSet.NLBResourceProperty(
                                arn="arn"
                            ),
                            r53_resource=route53recoveryreadiness.CfnResourceSet.R53ResourceRecordProperty(
                                domain_name="domainName",
                                record_set_id="recordSetId"
                            )
                        )
                    ),
                    readiness_scopes=["readinessScopes"],
                    resource_arn="resourceArn"
                )],
                resource_set_type="resourceSetType",
            
                # the properties below are optional
                resource_set_name="resourceSetName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06d1c28c31b64001c9f66d444600c6ed3d54876f5b918f83e00293963c674ba4)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument resource_set_type", value=resource_set_type, expected_type=type_hints["resource_set_type"])
            check_type(argname="argument resource_set_name", value=resource_set_name, expected_type=type_hints["resource_set_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resources": resources,
            "resource_set_type": resource_set_type,
        }
        if resource_set_name is not None:
            self._values["resource_set_name"] = resource_set_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def resources(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResourceSet.ResourceProperty]]]:
        '''A list of resource objects in the resource set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resources
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResourceSet.ResourceProperty]]], result)

    @builtins.property
    def resource_set_type(self) -> builtins.str:
        '''The resource type of the resources in the resource set. Enter one of the following values for resource type:.

        AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource.

        Note that AWS::Route53RecoveryReadiness::DNSTargetResource is only used for this setting. It isn't an actual AWS CloudFormation resource type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesettype
        '''
        result = self._values.get("resource_set_type")
        assert result is not None, "Required property 'resource_set_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the resource set to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesetname
        '''
        result = self._values.get("resource_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A tag to associate with the parameters for a resource set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCell",
    "CfnCellProps",
    "CfnReadinessCheck",
    "CfnReadinessCheckProps",
    "CfnRecoveryGroup",
    "CfnRecoveryGroupProps",
    "CfnResourceSet",
    "CfnResourceSetProps",
]

publication.publish()

def _typecheckingstub__13c868895ca08bff854c8fe7678338e1867e993f867d49908046cd6a17629e31(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cell_name: typing.Optional[builtins.str] = None,
    cells: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26df4eeedb5a0c616a1f3dad8c75f078f50e698da7a0e84e3a5d5735d6c00031(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d601dfd1114a47f09e8e4cc5e2fc61a0bc1bf8d65d07fa8a618424b7fe19fba(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63cf36126d8dd3b5e19180b0442de9842488ed8e561e44cde76e6ed852c19ad8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e9f11291a25b5e6f4ae9c7ac92db4cdc610f3d4102f4a96a81ba897fa1d87a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62f10011bc9a0c74b1e4ea8cc9c9bbf3a0a134a424b6f640abf9c44879051377(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__073034bd9956a2710068070b5d811ab42b3869de8e1a5c263d9e23a04df0cdfe(
    *,
    cell_name: typing.Optional[builtins.str] = None,
    cells: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bfbc5fa46ba2840c24892c634f80e8275ce2c76eb60922ee3c04a4b324e5b29(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    readiness_check_name: typing.Optional[builtins.str] = None,
    resource_set_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc7ffe6a29dd5f6e715a9726b09f80833380e0fbe980f5834be46b1ccd41b66(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6e1cff4db070736f87d566522f4b3545a4ad286947133e85c7ced4c96cedc81(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f3539c459e090a80aab3f1856cae71bbd8d5f0f2c8667cf9e39d7014435f965(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44d71b9a26b0dfffda11f6844c9805bb334cdaf3e1a1e32bcd05e04e31050f43(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79dc3aec0a3b3131b20694a730ecd7706f552f333a9b6a0ddcd951311d439c3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3c438502ee1a60d4adaea3215d352734901afcdf6cd40ef143a801e67d7e601(
    *,
    readiness_check_name: typing.Optional[builtins.str] = None,
    resource_set_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99277ba24eed449052f2cdf23737421f1433215fdc3cfd730a4385c704b3d713(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cells: typing.Optional[typing.Sequence[builtins.str]] = None,
    recovery_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db42d74a58f7864ec5ade4f46151f65d1fa1d6ce64c6818e481b49190794f1ef(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f57608369ed24b503beb8852606ac5b02696eec54ae288e3e1b88defdd9c7816(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5560294538ccfc7bb97ce8e2648a8ee6987e7a11a8852c027f1ae32197b5ced6(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e7b96d2a45ee2f819b9208f20855952769d9f0b63ad222e9e8c5279db457c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5466e3c5b9c14b878f6f4476a3156bdb5bc5565b79e490b847655152995e7ee0(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d342dcd3563435baa37fbbe16fdf0ff7b67201aa0844f5e1cf9d141d0bf9cd7(
    *,
    cells: typing.Optional[typing.Sequence[builtins.str]] = None,
    recovery_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6ebc0a9f935f88e0a23244138eb8cafe24b7630a5d785402d2354855596ebf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceSet.ResourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resource_set_type: builtins.str,
    resource_set_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fef85644281cf421ef43660e50fdbdb7916d6d66f698ce5050c537f21b4acc67(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1ced2fffee0146aab77f129ff62ca87caa55cd5db0cbf2406e2baa2d316e27(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4df7976fde8840dbbd29fd87b41d6fde568c4d3f43e84abd295e34dc123b85(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResourceSet.ResourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16cdb7ef88bcfa5e79a6b24f5a7afa77f90bc848a7011c10d11293035c9283fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d8323a736d4d8bc880e1dd4c2787e873cd4353286043e264ff9457c074a93d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8ce7b0dd37445da5365919573096496787ce1ddd7ea67b054df32684fa0cb5f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32358efbe7c385e7d76edfec00d6be4356e94128de2d64a8d0ace0fa96702e2c(
    *,
    domain_name: typing.Optional[builtins.str] = None,
    hosted_zone_arn: typing.Optional[builtins.str] = None,
    record_set_id: typing.Optional[builtins.str] = None,
    record_type: typing.Optional[builtins.str] = None,
    target_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceSet.TargetResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600815406b2a1e95c6a05550df4fc06db9418b487fd1d28b01318205286ef457(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05047634c6d70b5f1c983a80d886ef2a301a0fc1ef82f3a4aa86d4063f4d0a68(
    *,
    domain_name: typing.Optional[builtins.str] = None,
    record_set_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afec2888efa0ee04a661bcde195c3a04b092b5644744184d2c35c93c03801d07(
    *,
    component_id: typing.Optional[builtins.str] = None,
    dns_target_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceSet.DNSTargetResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    readiness_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16ba16f97722031f82a55ec2c9c68e5635ae95c709411fdf3cc1a49625a8b6da(
    *,
    nlb_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceSet.NLBResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    r53_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceSet.R53ResourceRecordProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d1c28c31b64001c9f66d444600c6ed3d54876f5b918f83e00293963c674ba4(
    *,
    resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceSet.ResourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resource_set_type: builtins.str,
    resource_set_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
