'''
# AWS::CustomerProfiles Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_customerprofiles as customerprofiles
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CustomerProfiles construct libraries](https://constructs.dev/search?q=customerprofiles)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CustomerProfiles resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CustomerProfiles.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CustomerProfiles](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CustomerProfiles.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnCalculatedAttributeDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition",
):
    '''A calculated attribute definition for Customer Profiles.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_calculated_attribute_definition = customerprofiles.CfnCalculatedAttributeDefinition(self, "MyCfnCalculatedAttributeDefinition",
            attribute_details=customerprofiles.CfnCalculatedAttributeDefinition.AttributeDetailsProperty(
                attributes=[customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty(
                    name="name"
                )],
                expression="expression"
            ),
            calculated_attribute_name="calculatedAttributeName",
            domain_name="domainName",
            statistic="statistic",
        
            # the properties below are optional
            conditions=customerprofiles.CfnCalculatedAttributeDefinition.ConditionsProperty(
                object_count=123,
                range=customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty(
                    unit="unit",
                    value=123
                ),
                threshold=customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty(
                    operator="operator",
                    value="value"
                )
            ),
            description="description",
            display_name="displayName",
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
        attribute_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.AttributeDetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        calculated_attribute_name: builtins.str,
        domain_name: builtins.str,
        statistic: builtins.str,
        conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.ConditionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param attribute_details: Mathematical expression and a list of attribute items specified in that expression.
        :param calculated_attribute_name: The name of an attribute defined in a profile object type.
        :param domain_name: The unique name of the domain.
        :param statistic: The aggregation operation to perform for the calculated attribute.
        :param conditions: The conditions including range, object count, and threshold for the calculated attribute.
        :param description: The description of the calculated attribute.
        :param display_name: The display name of the calculated attribute.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a09ab96caa4db6cfa4ebb0207c025a7f976cac18f814d69b882506cf2971669)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCalculatedAttributeDefinitionProps(
            attribute_details=attribute_details,
            calculated_attribute_name=calculated_attribute_name,
            domain_name=domain_name,
            statistic=statistic,
            conditions=conditions,
            description=description,
            display_name=display_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c355c3b327941e1e80c87b111beedb797243265da934cbe14cb40a04def39b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ff2e7320eba6c67e11b5108c4174e965091aab4bf1ed72835487ea46d7bd228)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the calculated attribute definition was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the calculated attribute definition was most recently edited.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="attributeDetails")
    def attribute_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeDetailsProperty"]:
        '''Mathematical expression and a list of attribute items specified in that expression.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeDetailsProperty"], jsii.get(self, "attributeDetails"))

    @attribute_details.setter
    def attribute_details(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeDetailsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc094b8898d98fbc0a232ed05081d6ffd11e6092cf72d062c7ab6a1a118b2655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeDetails", value)

    @builtins.property
    @jsii.member(jsii_name="calculatedAttributeName")
    def calculated_attribute_name(self) -> builtins.str:
        '''The name of an attribute defined in a profile object type.'''
        return typing.cast(builtins.str, jsii.get(self, "calculatedAttributeName"))

    @calculated_attribute_name.setter
    def calculated_attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1874ab73c6c7fb500a83379a356ae12dde9d52f47b68d1b2dfe7fb7772ae682)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "calculatedAttributeName", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__806572f2b3c6f3d60619dab1026866577ec43486c44775df8e7f00f9ec946cc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        '''The aggregation operation to perform for the calculated attribute.'''
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24137af23c238e226876684e3ad841c56564bd3e9f7c488415d38fbd9560440e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ConditionsProperty"]]:
        '''The conditions including range, object count, and threshold for the calculated attribute.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ConditionsProperty"]], jsii.get(self, "conditions"))

    @conditions.setter
    def conditions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ConditionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d9f165d8e8dde422309619ae01ce8e4f77e67c1d8707134c0f7c2a25fd53ebc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditions", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the calculated attribute.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e94c935ac0604ce2b84a26b87f764d32bfa425eb59416e0935dca9d2a010ce58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the calculated attribute.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64a1f1d0da7758807d6fc0184c03cfdc7c695677f2dd2cfeb300cb009b6e9d69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66b41ae1f61b2d451c01e8a6b3eabc1ef1fe6f0e51c71a264d46a9df8ec0ad14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.AttributeDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "expression": "expression"},
    )
    class AttributeDetailsProperty:
        def __init__(
            self,
            *,
            attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.AttributeItemProperty", typing.Dict[builtins.str, typing.Any]]]]],
            expression: builtins.str,
        ) -> None:
            '''Mathematical expression and a list of attribute items specified in that expression.

            :param attributes: Mathematical expression and a list of attribute items specified in that expression.
            :param expression: Mathematical expression that is performed on attribute items provided in the attribute list. Each element in the expression should follow the structure of "{ObjectTypeName.AttributeName}".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                attribute_details_property = customerprofiles.CfnCalculatedAttributeDefinition.AttributeDetailsProperty(
                    attributes=[customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty(
                        name="name"
                    )],
                    expression="expression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6241b1471123a742a03d1b24e69021bc3c2c3b4a805094f7a6176be6f76da07a)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attributes": attributes,
                "expression": expression,
            }

        @builtins.property
        def attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeItemProperty"]]]:
            '''Mathematical expression and a list of attribute items specified in that expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails-attributes
            '''
            result = self._values.get("attributes")
            assert result is not None, "Required property 'attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeItemProperty"]]], result)

        @builtins.property
        def expression(self) -> builtins.str:
            '''Mathematical expression that is performed on attribute items provided in the attribute list.

            Each element in the expression should follow the structure of "{ObjectTypeName.AttributeName}".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class AttributeItemProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''The details of a single attribute item specified in the mathematical expression.

            :param name: The unique name of the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                attribute_item_property = customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2af823a61c3449f36ffaa48661361e9de02280cffeeefa5a3d5990a5035cd43b)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The unique name of the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html#cfn-customerprofiles-calculatedattributedefinition-attributeitem-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.ConditionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object_count": "objectCount",
            "range": "range",
            "threshold": "threshold",
        },
    )
    class ConditionsProperty:
        def __init__(
            self,
            *,
            object_count: typing.Optional[jsii.Number] = None,
            range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.RangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            threshold: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.ThresholdProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The conditions including range, object count, and threshold for the calculated attribute.

            :param object_count: The number of profile objects used for the calculated attribute.
            :param range: The relative time period over which data is included in the aggregation.
            :param threshold: The threshold for the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                conditions_property = customerprofiles.CfnCalculatedAttributeDefinition.ConditionsProperty(
                    object_count=123,
                    range=customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty(
                        unit="unit",
                        value=123
                    ),
                    threshold=customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty(
                        operator="operator",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5d5606a68f168622e019935c1cfd2eb8821e95f36c66313b2a6f7a38cc4e472)
                check_type(argname="argument object_count", value=object_count, expected_type=type_hints["object_count"])
                check_type(argname="argument range", value=range, expected_type=type_hints["range"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if object_count is not None:
                self._values["object_count"] = object_count
            if range is not None:
                self._values["range"] = range
            if threshold is not None:
                self._values["threshold"] = threshold

        @builtins.property
        def object_count(self) -> typing.Optional[jsii.Number]:
            '''The number of profile objects used for the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-objectcount
            '''
            result = self._values.get("object_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def range(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.RangeProperty"]]:
            '''The relative time period over which data is included in the aggregation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-range
            '''
            result = self._values.get("range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.RangeProperty"]], result)

        @builtins.property
        def threshold(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ThresholdProperty"]]:
            '''The threshold for the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-threshold
            '''
            result = self._values.get("threshold")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ThresholdProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class RangeProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''The relative time period over which data is included in the aggregation.

            :param unit: The unit of time.
            :param value: The amount of time of the specified unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                range_property = customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty(
                    unit="unit",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4567eb83ac5620aa6be36cbd0e38cdba257d259743e1017616dbc2252fc66f9d)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''The unit of time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''The amount of time of the specified unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty",
        jsii_struct_bases=[],
        name_mapping={"operator": "operator", "value": "value"},
    )
    class ThresholdProperty:
        def __init__(self, *, operator: builtins.str, value: builtins.str) -> None:
            '''The threshold for the calculated attribute.

            :param operator: The operator of the threshold.
            :param value: The value of the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                threshold_property = customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty(
                    operator="operator",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dcc19afa2a314e3392b1f8004f5ce5593298e226e89f8bb3424dc57cefbb2646)
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "operator": operator,
                "value": value,
            }

        @builtins.property
        def operator(self) -> builtins.str:
            '''The operator of the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html#cfn-customerprofiles-calculatedattributedefinition-threshold-operator
            '''
            result = self._values.get("operator")
            assert result is not None, "Required property 'operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html#cfn-customerprofiles-calculatedattributedefinition-threshold-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThresholdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_details": "attributeDetails",
        "calculated_attribute_name": "calculatedAttributeName",
        "domain_name": "domainName",
        "statistic": "statistic",
        "conditions": "conditions",
        "description": "description",
        "display_name": "displayName",
        "tags": "tags",
    },
)
class CfnCalculatedAttributeDefinitionProps:
    def __init__(
        self,
        *,
        attribute_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.AttributeDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
        calculated_attribute_name: builtins.str,
        domain_name: builtins.str,
        statistic: builtins.str,
        conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCalculatedAttributeDefinition``.

        :param attribute_details: Mathematical expression and a list of attribute items specified in that expression.
        :param calculated_attribute_name: The name of an attribute defined in a profile object type.
        :param domain_name: The unique name of the domain.
        :param statistic: The aggregation operation to perform for the calculated attribute.
        :param conditions: The conditions including range, object count, and threshold for the calculated attribute.
        :param description: The description of the calculated attribute.
        :param display_name: The display name of the calculated attribute.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_calculated_attribute_definition_props = customerprofiles.CfnCalculatedAttributeDefinitionProps(
                attribute_details=customerprofiles.CfnCalculatedAttributeDefinition.AttributeDetailsProperty(
                    attributes=[customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty(
                        name="name"
                    )],
                    expression="expression"
                ),
                calculated_attribute_name="calculatedAttributeName",
                domain_name="domainName",
                statistic="statistic",
            
                # the properties below are optional
                conditions=customerprofiles.CfnCalculatedAttributeDefinition.ConditionsProperty(
                    object_count=123,
                    range=customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty(
                        unit="unit",
                        value=123
                    ),
                    threshold=customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty(
                        operator="operator",
                        value="value"
                    )
                ),
                description="description",
                display_name="displayName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b490cf412d8b10ddc1ddbf98b6d852a5446deca7e9befe3439df8de5169c37dd)
            check_type(argname="argument attribute_details", value=attribute_details, expected_type=type_hints["attribute_details"])
            check_type(argname="argument calculated_attribute_name", value=calculated_attribute_name, expected_type=type_hints["calculated_attribute_name"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_details": attribute_details,
            "calculated_attribute_name": calculated_attribute_name,
            "domain_name": domain_name,
            "statistic": statistic,
        }
        if conditions is not None:
            self._values["conditions"] = conditions
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def attribute_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.AttributeDetailsProperty]:
        '''Mathematical expression and a list of attribute items specified in that expression.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails
        '''
        result = self._values.get("attribute_details")
        assert result is not None, "Required property 'attribute_details' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.AttributeDetailsProperty], result)

    @builtins.property
    def calculated_attribute_name(self) -> builtins.str:
        '''The name of an attribute defined in a profile object type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-calculatedattributename
        '''
        result = self._values.get("calculated_attribute_name")
        assert result is not None, "Required property 'calculated_attribute_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''The aggregation operation to perform for the calculated attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-statistic
        '''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.ConditionsProperty]]:
        '''The conditions including range, object count, and threshold for the calculated attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-conditions
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.ConditionsProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the calculated attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the calculated attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCalculatedAttributeDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain",
):
    '''Specifies an Amazon Connect Customer Profiles Domain.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_domain = customerprofiles.CfnDomain(self, "MyCfnDomain",
            domain_name="domainName",
        
            # the properties below are optional
            dead_letter_queue_url="deadLetterQueueUrl",
            default_encryption_key="defaultEncryptionKey",
            default_expiration_days=123,
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
        domain_name: builtins.str,
        dead_letter_queue_url: typing.Optional[builtins.str] = None,
        default_encryption_key: typing.Optional[builtins.str] = None,
        default_expiration_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The unique name of the domain.
        :param dead_letter_queue_url: The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue.
        :param default_encryption_key: The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.
        :param default_expiration_days: The default number of days until the data within the domain expires.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cc1e612474254ea8edde86de3e08226c0c50e450782b3a99c92e87c31b99bad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(
            domain_name=domain_name,
            dead_letter_queue_url=dead_letter_queue_url,
            default_encryption_key=default_encryption_key,
            default_expiration_days=default_expiration_days,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd90568f369097b5d7a19088e675226c1257ad9e9ac30f3a478e941435aaaf5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88e553e446de50b16b878a912bc0a5f6f8763a19282b8d9da5099d68ef82e5b6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the domain was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the domain was most recently edited.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

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
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5155d94ec0a92f02d3b08cff5971632f213635d3dd2577433bbe328e9fac1d90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> typing.Optional[builtins.str]:
        '''The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deadLetterQueueUrl"))

    @dead_letter_queue_url.setter
    def dead_letter_queue_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39213ab6c2161d29ce1bafee3ec589effa27e2d24da755fd856339bb486e25a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deadLetterQueueUrl", value)

    @builtins.property
    @jsii.member(jsii_name="defaultEncryptionKey")
    def default_encryption_key(self) -> typing.Optional[builtins.str]:
        '''The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultEncryptionKey"))

    @default_encryption_key.setter
    def default_encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9ea79eb70814ff005e2ba351fe52042bea41d55509db4f24fbbf0d33cfb9a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultEncryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="defaultExpirationDays")
    def default_expiration_days(self) -> typing.Optional[jsii.Number]:
        '''The default number of days until the data within the domain expires.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultExpirationDays"))

    @default_expiration_days.setter
    def default_expiration_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d16654417fe9cbdb9f2b4f0145b59b3328699684a9b2c7ae7f2a3ad9b271e93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultExpirationDays", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc3d01d93fe80a75ec77ac1c37d929543f51e4a47feb47e25ebd0afa5fee06a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "dead_letter_queue_url": "deadLetterQueueUrl",
        "default_encryption_key": "defaultEncryptionKey",
        "default_expiration_days": "defaultExpirationDays",
        "tags": "tags",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        dead_letter_queue_url: typing.Optional[builtins.str] = None,
        default_encryption_key: typing.Optional[builtins.str] = None,
        default_expiration_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param domain_name: The unique name of the domain.
        :param dead_letter_queue_url: The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue.
        :param default_encryption_key: The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.
        :param default_expiration_days: The default number of days until the data within the domain expires.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_domain_props = customerprofiles.CfnDomainProps(
                domain_name="domainName",
            
                # the properties below are optional
                dead_letter_queue_url="deadLetterQueueUrl",
                default_encryption_key="defaultEncryptionKey",
                default_expiration_days=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03a55eb0b8d16e4b2b2589908d65475847a28870949386381667b6572e627f96)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument dead_letter_queue_url", value=dead_letter_queue_url, expected_type=type_hints["dead_letter_queue_url"])
            check_type(argname="argument default_encryption_key", value=default_encryption_key, expected_type=type_hints["default_encryption_key"])
            check_type(argname="argument default_expiration_days", value=default_expiration_days, expected_type=type_hints["default_expiration_days"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if dead_letter_queue_url is not None:
            self._values["dead_letter_queue_url"] = dead_letter_queue_url
        if default_encryption_key is not None:
            self._values["default_encryption_key"] = default_encryption_key
        if default_expiration_days is not None:
            self._values["default_expiration_days"] = default_expiration_days
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dead_letter_queue_url(self) -> typing.Optional[builtins.str]:
        '''The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications.

        You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl
        '''
        result = self._values.get("dead_letter_queue_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_encryption_key(self) -> typing.Optional[builtins.str]:
        '''The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified.

        It is used to encrypt all data before it is placed in permanent or semi-permanent storage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey
        '''
        result = self._values.get("default_encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_expiration_days(self) -> typing.Optional[jsii.Number]:
        '''The default number of days until the data within the domain expires.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays
        '''
        result = self._values.get("default_expiration_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEventStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventStream",
):
    '''An Event Stream resource of Amazon Connect Customer Profiles.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_event_stream = customerprofiles.CfnEventStream(self, "MyCfnEventStream",
            domain_name="domainName",
            event_stream_name="eventStreamName",
            uri="uri",
        
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
        domain_name: builtins.str,
        event_stream_name: builtins.str,
        uri: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The unique name of the domain.
        :param event_stream_name: The name of the event stream.
        :param uri: The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab29d0d747428994b84491cb3989a05a67bcb4cf0b84ebeba8fd19114b7cd61d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventStreamProps(
            domain_name=domain_name,
            event_stream_name=event_stream_name,
            uri=uri,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d37a000675ecf626a3348ff78d7f60db4441f2bb16c208d8dea0d1a4ecbd88f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__897cf1ba007446204846a7b757f800cd045b6bea2153894c6a8efdade633eaca)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the export was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDestinationDetails")
    def attr_destination_details(self) -> _IResolvable_da3f097b:
        '''Details regarding the Kinesis stream.

        :cloudformationAttribute: DestinationDetails
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDestinationDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrDestinationDetailsStatus")
    def attr_destination_details_status(self) -> builtins.str:
        '''The status of enabling the Kinesis stream as a destination for export.

        :cloudformationAttribute: DestinationDetails.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDestinationDetailsStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrDestinationDetailsUri")
    def attr_destination_details_uri(self) -> builtins.str:
        '''The StreamARN of the destination to deliver profile events to.

        For example, arn:aws:kinesis:region:account-id:stream/stream-name.

        :cloudformationAttribute: DestinationDetails.Uri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDestinationDetailsUri"))

    @builtins.property
    @jsii.member(jsii_name="attrEventStreamArn")
    def attr_event_stream_arn(self) -> builtins.str:
        '''A unique identifier for the event stream.

        :cloudformationAttribute: EventStreamArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventStreamArn"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The operational state of destination stream for export.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e40edb2a552aa50e0d65e685a232d9e8b469877491c9fd016aaf025966b9a1b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="eventStreamName")
    def event_stream_name(self) -> builtins.str:
        '''The name of the event stream.'''
        return typing.cast(builtins.str, jsii.get(self, "eventStreamName"))

    @event_stream_name.setter
    def event_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87ecaa8f57744bab81313074352cbc2f82cf8f797e78ce582ff548aa6251c330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        '''The StreamARN of the destination to deliver profile events to.'''
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d80288203f7d0782baca6858266d8c740f3fda90b2d6ef328306f3e966d5ee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dcffaefd3d051ab25e983d551d4abe7f28bcc0ccc2cc0f00dfbe9151cc9bd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventStream.DestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"status": "status", "uri": "uri"},
    )
    class DestinationDetailsProperty:
        def __init__(self, *, status: builtins.str, uri: builtins.str) -> None:
            '''Details regarding the Kinesis stream.

            :param status: The status of enabling the Kinesis stream as a destination for export.
            :param uri: The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                destination_details_property = customerprofiles.CfnEventStream.DestinationDetailsProperty(
                    status="status",
                    uri="uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__14be2a6e46acdc39b98267227ca646cdeba3edce7277e1499527949bda68cd54)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
                "uri": uri,
            }

        @builtins.property
        def status(self) -> builtins.str:
            '''The status of enabling the Kinesis stream as a destination for export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html#cfn-customerprofiles-eventstream-destinationdetails-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def uri(self) -> builtins.str:
            '''The StreamARN of the destination to deliver profile events to.

            For example, arn:aws:kinesis:region:account-id:stream/stream-name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html#cfn-customerprofiles-eventstream-destinationdetails-uri
            '''
            result = self._values.get("uri")
            assert result is not None, "Required property 'uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "event_stream_name": "eventStreamName",
        "uri": "uri",
        "tags": "tags",
    },
)
class CfnEventStreamProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        event_stream_name: builtins.str,
        uri: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventStream``.

        :param domain_name: The unique name of the domain.
        :param event_stream_name: The name of the event stream.
        :param uri: The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_event_stream_props = customerprofiles.CfnEventStreamProps(
                domain_name="domainName",
                event_stream_name="eventStreamName",
                uri="uri",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__813f95ba6287d3dc18d43b5b2ff35fbde17184e556360b280e3386143cfc00f0)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument event_stream_name", value=event_stream_name, expected_type=type_hints["event_stream_name"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "event_stream_name": event_stream_name,
            "uri": uri,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_stream_name(self) -> builtins.str:
        '''The name of the event stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-eventstreamname
        '''
        result = self._values.get("event_stream_name")
        assert result is not None, "Required property 'event_stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''The StreamARN of the destination to deliver profile events to.

        For example, arn:aws:kinesis:region:account-id:stream/stream-name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-uri
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration",
):
    '''Specifies an Amazon Connect Customer Profiles Integration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_integration = customerprofiles.CfnIntegration(self, "MyCfnIntegration",
            domain_name="domainName",
        
            # the properties below are optional
            flow_definition=customerprofiles.CfnIntegration.FlowDefinitionProperty(
                flow_name="flowName",
                kms_arn="kmsArn",
                source_flow_config=customerprofiles.CfnIntegration.SourceFlowConfigProperty(
                    connector_type="connectorType",
                    source_connector_properties=customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                        marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                            object="object"
                        ),
                        s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                            bucket_name="bucketName",
        
                            # the properties below are optional
                            bucket_prefix="bucketPrefix"
                        ),
                        salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                            object="object",
        
                            # the properties below are optional
                            enable_dynamic_field_update=False,
                            include_deleted_records=False
                        ),
                        service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                            object="object"
                        ),
                        zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                            object="object"
                        )
                    ),
        
                    # the properties below are optional
                    connector_profile_name="connectorProfileName",
                    incremental_pull_config=customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                        datetime_type_field_name="datetimeTypeFieldName"
                    )
                ),
                tasks=[customerprofiles.CfnIntegration.TaskProperty(
                    source_fields=["sourceFields"],
                    task_type="taskType",
        
                    # the properties below are optional
                    connector_operator=customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                        marketo="marketo",
                        s3="s3",
                        salesforce="salesforce",
                        service_now="serviceNow",
                        zendesk="zendesk"
                    ),
                    destination_field="destinationField",
                    task_properties=[customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                        operator_property_key="operatorPropertyKey",
                        property="property"
                    )]
                )],
                trigger_config=customerprofiles.CfnIntegration.TriggerConfigProperty(
                    trigger_type="triggerType",
        
                    # the properties below are optional
                    trigger_properties=customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                        scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                            schedule_expression="scheduleExpression",
        
                            # the properties below are optional
                            data_pull_mode="dataPullMode",
                            first_execution_from=123,
                            schedule_end_time=123,
                            schedule_offset=123,
                            schedule_start_time=123,
                            timezone="timezone"
                        )
                    )
                ),
        
                # the properties below are optional
                description="description"
            ),
            object_type_name="objectTypeName",
            object_type_names=[customerprofiles.CfnIntegration.ObjectTypeMappingProperty(
                key="key",
                value="value"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            uri="uri"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        flow_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.FlowDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        object_type_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ObjectTypeMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The unique name of the domain.
        :param flow_definition: The configuration that controls how Customer Profiles retrieves data from the source.
        :param object_type_name: The name of the profile object type mapping to use.
        :param object_type_names: The object type mapping.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param uri: The URI of the S3 bucket or any other type of data source.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8211c08b95eabfe008b27ab5b3b74bab34f671b7bd9761e15cdb090da9d3d95)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIntegrationProps(
            domain_name=domain_name,
            flow_definition=flow_definition,
            object_type_name=object_type_name,
            object_type_names=object_type_names,
            tags=tags,
            uri=uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85eb075da84dc570034fe72854e5f377beb9454784461fb242856b2b0d6db071)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a02b200ac7ef42474d61bef0afc23d2047a43211308a0f0f346c8804318a953d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the integration was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the integration was most recently edited.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

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
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d13bac4a06b95e4fadaf50aaed39e2383120484f2d6e868a652119e3c0741a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="flowDefinition")
    def flow_definition(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.FlowDefinitionProperty"]]:
        '''The configuration that controls how Customer Profiles retrieves data from the source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.FlowDefinitionProperty"]], jsii.get(self, "flowDefinition"))

    @flow_definition.setter
    def flow_definition(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.FlowDefinitionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda84696baed289de5f577073d9697fd7b0969af55567086ad86e6466b533e14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the profile object type mapping to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ac4be2e5060d6806d086adb14efc1af2df364f07423ea56e6af2958c23fc2b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeName", value)

    @builtins.property
    @jsii.member(jsii_name="objectTypeNames")
    def object_type_names(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ObjectTypeMappingProperty"]]]]:
        '''The object type mapping.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ObjectTypeMappingProperty"]]]], jsii.get(self, "objectTypeNames"))

    @object_type_names.setter
    def object_type_names(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ObjectTypeMappingProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d19e3d184d030db553288fb9b5bf060b201c3b429358e9c4818b39453b44a060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeNames", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55efe13391c8b01dcc8a4fc8cdb64b30e0590e3c2de5fbdfaf88656f9ad1a18e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        '''The URI of the S3 bucket or any other type of data source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02e9de6347e213a96d6d3dc4870b6c07c7e7db9b8044cff9f9952e0192a795c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ConnectorOperatorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "marketo": "marketo",
            "s3": "s3",
            "salesforce": "salesforce",
            "service_now": "serviceNow",
            "zendesk": "zendesk",
        },
    )
    class ConnectorOperatorProperty:
        def __init__(
            self,
            *,
            marketo: typing.Optional[builtins.str] = None,
            s3: typing.Optional[builtins.str] = None,
            salesforce: typing.Optional[builtins.str] = None,
            service_now: typing.Optional[builtins.str] = None,
            zendesk: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The operation to be performed on the provided source fields.

            :param marketo: The operation to be performed on the provided Marketo source fields.
            :param s3: The operation to be performed on the provided Amazon S3 source fields.
            :param salesforce: The operation to be performed on the provided Salesforce source fields.
            :param service_now: The operation to be performed on the provided ServiceNow source fields.
            :param zendesk: The operation to be performed on the provided Zendesk source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                connector_operator_property = customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                    marketo="marketo",
                    s3="s3",
                    salesforce="salesforce",
                    service_now="serviceNow",
                    zendesk="zendesk"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8ff575fc6d67c92e33f52c9a2a9924dd1914b3ec97eb67ea19a5f83109dfe09)
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if marketo is not None:
                self._values["marketo"] = marketo
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if service_now is not None:
                self._values["service_now"] = service_now
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def marketo(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Marketo source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Amazon S3 source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def salesforce(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Salesforce source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_now(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided ServiceNow source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zendesk(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Zendesk source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorOperatorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.FlowDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "flow_name": "flowName",
            "kms_arn": "kmsArn",
            "source_flow_config": "sourceFlowConfig",
            "tasks": "tasks",
            "trigger_config": "triggerConfig",
            "description": "description",
        },
    )
    class FlowDefinitionProperty:
        def __init__(
            self,
            *,
            flow_name: builtins.str,
            kms_arn: builtins.str,
            source_flow_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.SourceFlowConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            tasks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TaskProperty", typing.Dict[builtins.str, typing.Any]]]]],
            trigger_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TriggerConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configurations that control how Customer Profiles retrieves data from the source, Amazon AppFlow.

            Customer Profiles uses this information to create an AppFlow flow on behalf of customers.

            :param flow_name: The specified name of the flow. Use underscores (_) or hyphens (-) only. Spaces are not allowed.
            :param kms_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key you provide for encryption.
            :param source_flow_config: The configuration that controls how Customer Profiles retrieves data from the source.
            :param tasks: A list of tasks that Customer Profiles performs while transferring the data in the flow run.
            :param trigger_config: The trigger settings that determine how and when the flow runs.
            :param description: A description of the flow you want to create.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                flow_definition_property = customerprofiles.CfnIntegration.FlowDefinitionProperty(
                    flow_name="flowName",
                    kms_arn="kmsArn",
                    source_flow_config=customerprofiles.CfnIntegration.SourceFlowConfigProperty(
                        connector_type="connectorType",
                        source_connector_properties=customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                            marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                                object="object"
                            ),
                            s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                                bucket_name="bucketName",
                
                                # the properties below are optional
                                bucket_prefix="bucketPrefix"
                            ),
                            salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                                object="object",
                
                                # the properties below are optional
                                enable_dynamic_field_update=False,
                                include_deleted_records=False
                            ),
                            service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                                object="object"
                            ),
                            zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                                object="object"
                            )
                        ),
                
                        # the properties below are optional
                        connector_profile_name="connectorProfileName",
                        incremental_pull_config=customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                            datetime_type_field_name="datetimeTypeFieldName"
                        )
                    ),
                    tasks=[customerprofiles.CfnIntegration.TaskProperty(
                        source_fields=["sourceFields"],
                        task_type="taskType",
                
                        # the properties below are optional
                        connector_operator=customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                            marketo="marketo",
                            s3="s3",
                            salesforce="salesforce",
                            service_now="serviceNow",
                            zendesk="zendesk"
                        ),
                        destination_field="destinationField",
                        task_properties=[customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                            operator_property_key="operatorPropertyKey",
                            property="property"
                        )]
                    )],
                    trigger_config=customerprofiles.CfnIntegration.TriggerConfigProperty(
                        trigger_type="triggerType",
                
                        # the properties below are optional
                        trigger_properties=customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                            scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                                schedule_expression="scheduleExpression",
                
                                # the properties below are optional
                                data_pull_mode="dataPullMode",
                                first_execution_from=123,
                                schedule_end_time=123,
                                schedule_offset=123,
                                schedule_start_time=123,
                                timezone="timezone"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__684e26c18461ba90c60337c4f41ecfe0fff4d6e92e5f5ccc4fca2dbb9cb7fe58)
                check_type(argname="argument flow_name", value=flow_name, expected_type=type_hints["flow_name"])
                check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
                check_type(argname="argument source_flow_config", value=source_flow_config, expected_type=type_hints["source_flow_config"])
                check_type(argname="argument tasks", value=tasks, expected_type=type_hints["tasks"])
                check_type(argname="argument trigger_config", value=trigger_config, expected_type=type_hints["trigger_config"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "flow_name": flow_name,
                "kms_arn": kms_arn,
                "source_flow_config": source_flow_config,
                "tasks": tasks,
                "trigger_config": trigger_config,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def flow_name(self) -> builtins.str:
            '''The specified name of the flow.

            Use underscores (_) or hyphens (-) only. Spaces are not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-flowname
            '''
            result = self._values.get("flow_name")
            assert result is not None, "Required property 'flow_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key you provide for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-kmsarn
            '''
            result = self._values.get("kms_arn")
            assert result is not None, "Required property 'kms_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_flow_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnIntegration.SourceFlowConfigProperty"]:
            '''The configuration that controls how Customer Profiles retrieves data from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-sourceflowconfig
            '''
            result = self._values.get("source_flow_config")
            assert result is not None, "Required property 'source_flow_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIntegration.SourceFlowConfigProperty"], result)

        @builtins.property
        def tasks(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TaskProperty"]]]:
            '''A list of tasks that Customer Profiles performs while transferring the data in the flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-tasks
            '''
            result = self._values.get("tasks")
            assert result is not None, "Required property 'tasks' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TaskProperty"]]], result)

        @builtins.property
        def trigger_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnIntegration.TriggerConfigProperty"]:
            '''The trigger settings that determine how and when the flow runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-triggerconfig
            '''
            result = self._values.get("trigger_config")
            assert result is not None, "Required property 'trigger_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIntegration.TriggerConfigProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the flow you want to create.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.IncrementalPullConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"datetime_type_field_name": "datetimeTypeFieldName"},
    )
    class IncrementalPullConfigProperty:
        def __init__(
            self,
            *,
            datetime_type_field_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration used when importing incremental records from the source.

            :param datetime_type_field_name: A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                incremental_pull_config_property = customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                    datetime_type_field_name="datetimeTypeFieldName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b30373edbc1fc87d87c0305c0d579d9085e768165db2968c37ebc100141fc94c)
                check_type(argname="argument datetime_type_field_name", value=datetime_type_field_name, expected_type=type_hints["datetime_type_field_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if datetime_type_field_name is not None:
                self._values["datetime_type_field_name"] = datetime_type_field_name

        @builtins.property
        def datetime_type_field_name(self) -> typing.Optional[builtins.str]:
            '''A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html#cfn-customerprofiles-integration-incrementalpullconfig-datetimetypefieldname
            '''
            result = self._values.get("datetime_type_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IncrementalPullConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class MarketoSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Marketo is being used as a source.

            :param object: The object specified in the Marketo flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                marketo_source_properties_property = customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a60c86877c43b5afd59790a18d6019039ccc87b2d8b8b5c9299157eda159890)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Marketo flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html#cfn-customerprofiles-integration-marketosourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarketoSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ObjectTypeMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ObjectTypeMappingProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an ``ObjectTypeName`` (template) used to ingest the event.

            :param key: The key.
            :param value: The value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                object_type_mapping_property = customerprofiles.CfnIntegration.ObjectTypeMappingProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d9afb6e6e9868c0b8b44a3a96fec8e43830e8a548405844dbf1d5a8d81ced10d)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html#cfn-customerprofiles-integration-objecttypemapping-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html#cfn-customerprofiles-integration-objecttypemapping-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.S3SourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "bucket_prefix": "bucketPrefix"},
    )
    class S3SourcePropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties that are applied when Amazon S3 is being used as the flow source.

            :param bucket_name: The Amazon S3 bucket name where the source files are stored.
            :param bucket_prefix: The object key for the Amazon S3 bucket in which the source files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                s3_source_properties_property = customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a79daf2a1599613c0d4820e23ade3e1ab729e048f4f33e5e1ca2c56d56a3757b)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The Amazon S3 bucket name where the source files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The object key for the Amazon S3 bucket in which the source files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "enable_dynamic_field_update": "enableDynamicFieldUpdate",
            "include_deleted_records": "includeDeletedRecords",
        },
    )
    class SalesforceSourcePropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_deleted_records: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The properties that are applied when Salesforce is being used as a source.

            :param object: The object specified in the Salesforce flow source.
            :param enable_dynamic_field_update: The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.
            :param include_deleted_records: Indicates whether Amazon AppFlow includes deleted files in the flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                salesforce_source_properties_property = customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                    object="object",
                
                    # the properties below are optional
                    enable_dynamic_field_update=False,
                    include_deleted_records=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48d96167457187d54618dd4839b1f9086125a2307ec481de96e070635baf5c77)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument enable_dynamic_field_update", value=enable_dynamic_field_update, expected_type=type_hints["enable_dynamic_field_update"])
                check_type(argname="argument include_deleted_records", value=include_deleted_records, expected_type=type_hints["include_deleted_records"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }
            if enable_dynamic_field_update is not None:
                self._values["enable_dynamic_field_update"] = enable_dynamic_field_update
            if include_deleted_records is not None:
                self._values["include_deleted_records"] = include_deleted_records

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Salesforce flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enable_dynamic_field_update(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-enabledynamicfieldupdate
            '''
            result = self._values.get("enable_dynamic_field_update")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_deleted_records(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether Amazon AppFlow includes deleted files in the flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-includedeletedrecords
            '''
            result = self._values.get("include_deleted_records")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule_expression": "scheduleExpression",
            "data_pull_mode": "dataPullMode",
            "first_execution_from": "firstExecutionFrom",
            "schedule_end_time": "scheduleEndTime",
            "schedule_offset": "scheduleOffset",
            "schedule_start_time": "scheduleStartTime",
            "timezone": "timezone",
        },
    )
    class ScheduledTriggerPropertiesProperty:
        def __init__(
            self,
            *,
            schedule_expression: builtins.str,
            data_pull_mode: typing.Optional[builtins.str] = None,
            first_execution_from: typing.Optional[jsii.Number] = None,
            schedule_end_time: typing.Optional[jsii.Number] = None,
            schedule_offset: typing.Optional[jsii.Number] = None,
            schedule_start_time: typing.Optional[jsii.Number] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration details of a scheduled-trigger flow that you define.

            Currently, these settings only apply to the scheduled-trigger type.

            :param schedule_expression: The scheduling expression that determines the rate at which the schedule will run, for example rate (5 minutes).
            :param data_pull_mode: Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.
            :param first_execution_from: Specifies the date range for the records to import from the connector in the first flow run.
            :param schedule_end_time: Specifies the scheduled end time for a scheduled-trigger flow.
            :param schedule_offset: Specifies the optional offset that is added to the time interval for a schedule-triggered flow.
            :param schedule_start_time: Specifies the scheduled start time for a scheduled-trigger flow.
            :param timezone: Specifies the time zone used when referring to the date and time of a scheduled-triggered flow, such as America/New_York.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                scheduled_trigger_properties_property = customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                    schedule_expression="scheduleExpression",
                
                    # the properties below are optional
                    data_pull_mode="dataPullMode",
                    first_execution_from=123,
                    schedule_end_time=123,
                    schedule_offset=123,
                    schedule_start_time=123,
                    timezone="timezone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e5944d396eaa65c18b0b184d20b092353bd232b3071af67d1f4668a3a6cb830)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument data_pull_mode", value=data_pull_mode, expected_type=type_hints["data_pull_mode"])
                check_type(argname="argument first_execution_from", value=first_execution_from, expected_type=type_hints["first_execution_from"])
                check_type(argname="argument schedule_end_time", value=schedule_end_time, expected_type=type_hints["schedule_end_time"])
                check_type(argname="argument schedule_offset", value=schedule_offset, expected_type=type_hints["schedule_offset"])
                check_type(argname="argument schedule_start_time", value=schedule_start_time, expected_type=type_hints["schedule_start_time"])
                check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }
            if data_pull_mode is not None:
                self._values["data_pull_mode"] = data_pull_mode
            if first_execution_from is not None:
                self._values["first_execution_from"] = first_execution_from
            if schedule_end_time is not None:
                self._values["schedule_end_time"] = schedule_end_time
            if schedule_offset is not None:
                self._values["schedule_offset"] = schedule_offset
            if schedule_start_time is not None:
                self._values["schedule_start_time"] = schedule_start_time
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''The scheduling expression that determines the rate at which the schedule will run, for example rate (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_pull_mode(self) -> typing.Optional[builtins.str]:
            '''Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode
            '''
            result = self._values.get("data_pull_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_execution_from(self) -> typing.Optional[jsii.Number]:
            '''Specifies the date range for the records to import from the connector in the first flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom
            '''
            result = self._values.get("first_execution_from")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_end_time(self) -> typing.Optional[jsii.Number]:
            '''Specifies the scheduled end time for a scheduled-trigger flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime
            '''
            result = self._values.get("schedule_end_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_offset(self) -> typing.Optional[jsii.Number]:
            '''Specifies the optional offset that is added to the time interval for a schedule-triggered flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset
            '''
            result = self._values.get("schedule_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_start_time(self) -> typing.Optional[jsii.Number]:
            '''Specifies the scheduled start time for a scheduled-trigger flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime
            '''
            result = self._values.get("schedule_start_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''Specifies the time zone used when referring to the date and time of a scheduled-triggered flow, such as America/New_York.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduledTriggerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class ServiceNowSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when ServiceNow is being used as a source.

            :param object: The object specified in the ServiceNow flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                service_now_source_properties_property = customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e39d4ec6bb5656a7c82bcb644c1e71ed86635052e302daedb141f92c9338d5e)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the ServiceNow flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html#cfn-customerprofiles-integration-servicenowsourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "marketo": "marketo",
            "s3": "s3",
            "salesforce": "salesforce",
            "service_now": "serviceNow",
            "zendesk": "zendesk",
        },
    )
    class SourceConnectorPropertiesProperty:
        def __init__(
            self,
            *,
            marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.MarketoSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.S3SourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.SalesforceSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ServiceNowSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ZendeskSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the information that is required to query a particular Amazon AppFlow connector.

            Customer Profiles supports Salesforce, Zendesk, Marketo, ServiceNow and Amazon S3.

            :param marketo: The properties that are applied when Marketo is being used as a source.
            :param s3: The properties that are applied when Amazon S3 is being used as the flow source.
            :param salesforce: The properties that are applied when Salesforce is being used as a source.
            :param service_now: The properties that are applied when ServiceNow is being used as a source.
            :param zendesk: The properties that are applied when using Zendesk as a flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                source_connector_properties_property = customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                    marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                        object="object"
                    ),
                    s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        bucket_prefix="bucketPrefix"
                    ),
                    salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                        object="object",
                
                        # the properties below are optional
                        enable_dynamic_field_update=False,
                        include_deleted_records=False
                    ),
                    service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                        object="object"
                    ),
                    zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                        object="object"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__886a4a6c1d593aa53fe13ccd79b82bf91be008e3952bb987ac48d2b64b7a6ac9)
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if marketo is not None:
                self._values["marketo"] = marketo
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if service_now is not None:
                self._values["service_now"] = service_now
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def marketo(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.MarketoSourcePropertiesProperty"]]:
            '''The properties that are applied when Marketo is being used as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.MarketoSourcePropertiesProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.S3SourcePropertiesProperty"]]:
            '''The properties that are applied when Amazon S3 is being used as the flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.S3SourcePropertiesProperty"]], result)

        @builtins.property
        def salesforce(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.SalesforceSourcePropertiesProperty"]]:
            '''The properties that are applied when Salesforce is being used as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.SalesforceSourcePropertiesProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ServiceNowSourcePropertiesProperty"]]:
            '''The properties that are applied when ServiceNow is being used as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ServiceNowSourcePropertiesProperty"]], result)

        @builtins.property
        def zendesk(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ZendeskSourcePropertiesProperty"]]:
            '''The properties that are applied when using Zendesk as a flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ZendeskSourcePropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConnectorPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.SourceFlowConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_type": "connectorType",
            "source_connector_properties": "sourceConnectorProperties",
            "connector_profile_name": "connectorProfileName",
            "incremental_pull_config": "incrementalPullConfig",
        },
    )
    class SourceFlowConfigProperty:
        def __init__(
            self,
            *,
            connector_type: builtins.str,
            source_connector_properties: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.SourceConnectorPropertiesProperty", typing.Dict[builtins.str, typing.Any]]],
            connector_profile_name: typing.Optional[builtins.str] = None,
            incremental_pull_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.IncrementalPullConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration that controls how Customer Profiles retrieves data from the source.

            :param connector_type: The type of connector, such as Salesforce, Marketo, and so on.
            :param source_connector_properties: Specifies the information that is required to query a particular source connector.
            :param connector_profile_name: The name of the Amazon AppFlow connector profile. This name must be unique for each connector profile in the AWS account .
            :param incremental_pull_config: Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                source_flow_config_property = customerprofiles.CfnIntegration.SourceFlowConfigProperty(
                    connector_type="connectorType",
                    source_connector_properties=customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                        marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                            object="object"
                        ),
                        s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                            bucket_name="bucketName",
                
                            # the properties below are optional
                            bucket_prefix="bucketPrefix"
                        ),
                        salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                            object="object",
                
                            # the properties below are optional
                            enable_dynamic_field_update=False,
                            include_deleted_records=False
                        ),
                        service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                            object="object"
                        ),
                        zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                            object="object"
                        )
                    ),
                
                    # the properties below are optional
                    connector_profile_name="connectorProfileName",
                    incremental_pull_config=customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                        datetime_type_field_name="datetimeTypeFieldName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55d9871f7bd0e95109d517268a1cdd0da37965b7b7acd24cb1bfd91cacda7d2f)
                check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
                check_type(argname="argument source_connector_properties", value=source_connector_properties, expected_type=type_hints["source_connector_properties"])
                check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
                check_type(argname="argument incremental_pull_config", value=incremental_pull_config, expected_type=type_hints["incremental_pull_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connector_type": connector_type,
                "source_connector_properties": source_connector_properties,
            }
            if connector_profile_name is not None:
                self._values["connector_profile_name"] = connector_profile_name
            if incremental_pull_config is not None:
                self._values["incremental_pull_config"] = incremental_pull_config

        @builtins.property
        def connector_type(self) -> builtins.str:
            '''The type of connector, such as Salesforce, Marketo, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectortype
            '''
            result = self._values.get("connector_type")
            assert result is not None, "Required property 'connector_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_connector_properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnIntegration.SourceConnectorPropertiesProperty"]:
            '''Specifies the information that is required to query a particular source connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties
            '''
            result = self._values.get("source_connector_properties")
            assert result is not None, "Required property 'source_connector_properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIntegration.SourceConnectorPropertiesProperty"], result)

        @builtins.property
        def connector_profile_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon AppFlow connector profile.

            This name must be unique for each connector profile in the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename
            '''
            result = self._values.get("connector_profile_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def incremental_pull_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.IncrementalPullConfigProperty"]]:
            '''Defines the configuration for a scheduled incremental data pull.

            If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig
            '''
            result = self._values.get("incremental_pull_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.IncrementalPullConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceFlowConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.TaskPropertiesMapProperty",
        jsii_struct_bases=[],
        name_mapping={
            "operator_property_key": "operatorPropertyKey",
            "property": "property",
        },
    )
    class TaskPropertiesMapProperty:
        def __init__(
            self,
            *,
            operator_property_key: builtins.str,
            property: builtins.str,
        ) -> None:
            '''A map used to store task-related information.

            The execution service looks for particular information based on the ``TaskType`` .

            :param operator_property_key: The task property key.
            :param property: The task property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                task_properties_map_property = customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                    operator_property_key="operatorPropertyKey",
                    property="property"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a8a6d70493dcc8d57205e11e51993268d52dac180561f2ae05a6aa7eba5fab11)
                check_type(argname="argument operator_property_key", value=operator_property_key, expected_type=type_hints["operator_property_key"])
                check_type(argname="argument property", value=property, expected_type=type_hints["property"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "operator_property_key": operator_property_key,
                "property": property,
            }

        @builtins.property
        def operator_property_key(self) -> builtins.str:
            '''The task property key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-operatorpropertykey
            '''
            result = self._values.get("operator_property_key")
            assert result is not None, "Required property 'operator_property_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def property(self) -> builtins.str:
            '''The task property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-property
            '''
            result = self._values.get("property")
            assert result is not None, "Required property 'property' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskPropertiesMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.TaskProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_fields": "sourceFields",
            "task_type": "taskType",
            "connector_operator": "connectorOperator",
            "destination_field": "destinationField",
            "task_properties": "taskProperties",
        },
    )
    class TaskProperty:
        def __init__(
            self,
            *,
            source_fields: typing.Sequence[builtins.str],
            task_type: builtins.str,
            connector_operator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ConnectorOperatorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            destination_field: typing.Optional[builtins.str] = None,
            task_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TaskPropertiesMapProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``Task`` property type specifies the class for modeling different type of tasks.

            Task implementation varies based on the TaskType.

            :param source_fields: The source fields to which a particular task is applied.
            :param task_type: Specifies the particular task implementation that Amazon AppFlow performs.
            :param connector_operator: The operation to be performed on the provided source fields.
            :param destination_field: A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.
            :param task_properties: A map used to store task-related information. The service looks for particular information based on the TaskType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                task_property = customerprofiles.CfnIntegration.TaskProperty(
                    source_fields=["sourceFields"],
                    task_type="taskType",
                
                    # the properties below are optional
                    connector_operator=customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                        marketo="marketo",
                        s3="s3",
                        salesforce="salesforce",
                        service_now="serviceNow",
                        zendesk="zendesk"
                    ),
                    destination_field="destinationField",
                    task_properties=[customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                        operator_property_key="operatorPropertyKey",
                        property="property"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c97356b1cf286df38ebed38c9f4ce8135e5160a1254e87e74e1baaba8f2149f)
                check_type(argname="argument source_fields", value=source_fields, expected_type=type_hints["source_fields"])
                check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
                check_type(argname="argument connector_operator", value=connector_operator, expected_type=type_hints["connector_operator"])
                check_type(argname="argument destination_field", value=destination_field, expected_type=type_hints["destination_field"])
                check_type(argname="argument task_properties", value=task_properties, expected_type=type_hints["task_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_fields": source_fields,
                "task_type": task_type,
            }
            if connector_operator is not None:
                self._values["connector_operator"] = connector_operator
            if destination_field is not None:
                self._values["destination_field"] = destination_field
            if task_properties is not None:
                self._values["task_properties"] = task_properties

        @builtins.property
        def source_fields(self) -> typing.List[builtins.str]:
            '''The source fields to which a particular task is applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-sourcefields
            '''
            result = self._values.get("source_fields")
            assert result is not None, "Required property 'source_fields' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def task_type(self) -> builtins.str:
            '''Specifies the particular task implementation that Amazon AppFlow performs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-tasktype
            '''
            result = self._values.get("task_type")
            assert result is not None, "Required property 'task_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def connector_operator(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ConnectorOperatorProperty"]]:
            '''The operation to be performed on the provided source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-connectoroperator
            '''
            result = self._values.get("connector_operator")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ConnectorOperatorProperty"]], result)

        @builtins.property
        def destination_field(self) -> typing.Optional[builtins.str]:
            '''A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-destinationfield
            '''
            result = self._values.get("destination_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def task_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TaskPropertiesMapProperty"]]]]:
            '''A map used to store task-related information.

            The service looks for particular information based on the TaskType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-taskproperties
            '''
            result = self._values.get("task_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TaskPropertiesMapProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.TriggerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trigger_type": "triggerType",
            "trigger_properties": "triggerProperties",
        },
    )
    class TriggerConfigProperty:
        def __init__(
            self,
            *,
            trigger_type: builtins.str,
            trigger_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TriggerPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The trigger settings that determine how and when Amazon AppFlow runs the specified flow.

            :param trigger_type: Specifies the type of flow trigger. It can be OnDemand, Scheduled, or Event.
            :param trigger_properties: Specifies the configuration details of a schedule-triggered flow that you define. Currently, these settings only apply to the Scheduled trigger type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                trigger_config_property = customerprofiles.CfnIntegration.TriggerConfigProperty(
                    trigger_type="triggerType",
                
                    # the properties below are optional
                    trigger_properties=customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                        scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                            schedule_expression="scheduleExpression",
                
                            # the properties below are optional
                            data_pull_mode="dataPullMode",
                            first_execution_from=123,
                            schedule_end_time=123,
                            schedule_offset=123,
                            schedule_start_time=123,
                            timezone="timezone"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43314febd76ccf4bc3946158640fcdb8e8e2b2e8aa92fe065358b557e5787cdc)
                check_type(argname="argument trigger_type", value=trigger_type, expected_type=type_hints["trigger_type"])
                check_type(argname="argument trigger_properties", value=trigger_properties, expected_type=type_hints["trigger_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "trigger_type": trigger_type,
            }
            if trigger_properties is not None:
                self._values["trigger_properties"] = trigger_properties

        @builtins.property
        def trigger_type(self) -> builtins.str:
            '''Specifies the type of flow trigger.

            It can be OnDemand, Scheduled, or Event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggertype
            '''
            result = self._values.get("trigger_type")
            assert result is not None, "Required property 'trigger_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def trigger_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TriggerPropertiesProperty"]]:
            '''Specifies the configuration details of a schedule-triggered flow that you define.

            Currently, these settings only apply to the Scheduled trigger type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggerproperties
            '''
            result = self._values.get("trigger_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TriggerPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.TriggerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"scheduled": "scheduled"},
    )
    class TriggerPropertiesProperty:
        def __init__(
            self,
            *,
            scheduled: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ScheduledTriggerPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration details that control the trigger for a flow.

            Currently, these settings only apply to the Scheduled trigger type.

            :param scheduled: Specifies the configuration details of a schedule-triggered flow that you define.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                trigger_properties_property = customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                    scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                        schedule_expression="scheduleExpression",
                
                        # the properties below are optional
                        data_pull_mode="dataPullMode",
                        first_execution_from=123,
                        schedule_end_time=123,
                        schedule_offset=123,
                        schedule_start_time=123,
                        timezone="timezone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d95880464ba4d79437e95620f7b099ab48173665d71b3b3e9925b31023ae79a)
                check_type(argname="argument scheduled", value=scheduled, expected_type=type_hints["scheduled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if scheduled is not None:
                self._values["scheduled"] = scheduled

        @builtins.property
        def scheduled(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ScheduledTriggerPropertiesProperty"]]:
            '''Specifies the configuration details of a schedule-triggered flow that you define.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html#cfn-customerprofiles-integration-triggerproperties-scheduled
            '''
            result = self._values.get("scheduled")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ScheduledTriggerPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class ZendeskSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when using Zendesk as a flow source.

            :param object: The object specified in the Zendesk flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                zendesk_source_properties_property = customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6fec16a3ec50ec7d597e7573ae1e24e531163b732505e322d5ef39e9267351db)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Zendesk flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html#cfn-customerprofiles-integration-zendesksourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZendeskSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "flow_definition": "flowDefinition",
        "object_type_name": "objectTypeName",
        "object_type_names": "objectTypeNames",
        "tags": "tags",
        "uri": "uri",
    },
)
class CfnIntegrationProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        flow_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.FlowDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        object_type_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ObjectTypeMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnIntegration``.

        :param domain_name: The unique name of the domain.
        :param flow_definition: The configuration that controls how Customer Profiles retrieves data from the source.
        :param object_type_name: The name of the profile object type mapping to use.
        :param object_type_names: The object type mapping.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param uri: The URI of the S3 bucket or any other type of data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_integration_props = customerprofiles.CfnIntegrationProps(
                domain_name="domainName",
            
                # the properties below are optional
                flow_definition=customerprofiles.CfnIntegration.FlowDefinitionProperty(
                    flow_name="flowName",
                    kms_arn="kmsArn",
                    source_flow_config=customerprofiles.CfnIntegration.SourceFlowConfigProperty(
                        connector_type="connectorType",
                        source_connector_properties=customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                            marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                                object="object"
                            ),
                            s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                                bucket_name="bucketName",
            
                                # the properties below are optional
                                bucket_prefix="bucketPrefix"
                            ),
                            salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                                object="object",
            
                                # the properties below are optional
                                enable_dynamic_field_update=False,
                                include_deleted_records=False
                            ),
                            service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                                object="object"
                            ),
                            zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                                object="object"
                            )
                        ),
            
                        # the properties below are optional
                        connector_profile_name="connectorProfileName",
                        incremental_pull_config=customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                            datetime_type_field_name="datetimeTypeFieldName"
                        )
                    ),
                    tasks=[customerprofiles.CfnIntegration.TaskProperty(
                        source_fields=["sourceFields"],
                        task_type="taskType",
            
                        # the properties below are optional
                        connector_operator=customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                            marketo="marketo",
                            s3="s3",
                            salesforce="salesforce",
                            service_now="serviceNow",
                            zendesk="zendesk"
                        ),
                        destination_field="destinationField",
                        task_properties=[customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                            operator_property_key="operatorPropertyKey",
                            property="property"
                        )]
                    )],
                    trigger_config=customerprofiles.CfnIntegration.TriggerConfigProperty(
                        trigger_type="triggerType",
            
                        # the properties below are optional
                        trigger_properties=customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                            scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                                schedule_expression="scheduleExpression",
            
                                # the properties below are optional
                                data_pull_mode="dataPullMode",
                                first_execution_from=123,
                                schedule_end_time=123,
                                schedule_offset=123,
                                schedule_start_time=123,
                                timezone="timezone"
                            )
                        )
                    ),
            
                    # the properties below are optional
                    description="description"
                ),
                object_type_name="objectTypeName",
                object_type_names=[customerprofiles.CfnIntegration.ObjectTypeMappingProperty(
                    key="key",
                    value="value"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                uri="uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52bfebce0bd12cb9d9ed6354b0627c3f2946899ecf1ba8120aa70c1e1e22428d)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument flow_definition", value=flow_definition, expected_type=type_hints["flow_definition"])
            check_type(argname="argument object_type_name", value=object_type_name, expected_type=type_hints["object_type_name"])
            check_type(argname="argument object_type_names", value=object_type_names, expected_type=type_hints["object_type_names"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if flow_definition is not None:
            self._values["flow_definition"] = flow_definition
        if object_type_name is not None:
            self._values["object_type_name"] = object_type_name
        if object_type_names is not None:
            self._values["object_type_names"] = object_type_names
        if tags is not None:
            self._values["tags"] = tags
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_definition(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.FlowDefinitionProperty]]:
        '''The configuration that controls how Customer Profiles retrieves data from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-flowdefinition
        '''
        result = self._values.get("flow_definition")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.FlowDefinitionProperty]], result)

    @builtins.property
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the profile object type mapping to use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename
        '''
        result = self._values.get("object_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_type_names(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIntegration.ObjectTypeMappingProperty]]]]:
        '''The object type mapping.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypenames
        '''
        result = self._values.get("object_type_names")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIntegration.ObjectTypeMappingProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The URI of the S3 bucket or any other type of data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnObjectType(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType",
):
    '''Specifies an Amazon Connect Customer Profiles Object Type Mapping.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_object_type = customerprofiles.CfnObjectType(self, "MyCfnObjectType",
            domain_name="domainName",
        
            # the properties below are optional
            allow_profile_creation=False,
            description="description",
            encryption_key="encryptionKey",
            expiration_days=123,
            fields=[customerprofiles.CfnObjectType.FieldMapProperty(
                name="name",
                object_type_field=customerprofiles.CfnObjectType.ObjectTypeFieldProperty(
                    content_type="contentType",
                    source="source",
                    target="target"
                )
            )],
            keys=[customerprofiles.CfnObjectType.KeyMapProperty(
                name="name",
                object_type_key_list=[customerprofiles.CfnObjectType.ObjectTypeKeyProperty(
                    field_names=["fieldNames"],
                    standard_identifiers=["standardIdentifiers"]
                )]
            )],
            object_type_name="objectTypeName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            template_id="templateId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        expiration_days: typing.Optional[jsii.Number] = None,
        fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObjectType.FieldMapProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObjectType.KeyMapProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The unique name of the domain.
        :param allow_profile_creation: Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is ``FALSE`` . If the AllowProfileCreation flag is set to ``FALSE`` , then the service tries to fetch a standard profile and associate this object with the profile. If it is set to ``TRUE`` , and if no match is found, then the service creates a new standard profile.
        :param description: The description of the profile object type mapping.
        :param encryption_key: The customer-provided key to encrypt the profile object that will be created in this profile object type mapping. If not specified the system will use the encryption key of the domain.
        :param expiration_days: The number of days until the data of this type expires.
        :param fields: A list of field definitions for the object type mapping.
        :param keys: A list of keys that can be used to map data to the profile or search for the profile.
        :param object_type_name: The name of the profile object type.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param template_id: A unique identifier for the template mapping. This can be used instead of specifying the Keys and Fields properties directly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e58419cb0a7694b5c554275a8721df95dc40489e742a23c76f7830ca5210127a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnObjectTypeProps(
            domain_name=domain_name,
            allow_profile_creation=allow_profile_creation,
            description=description,
            encryption_key=encryption_key,
            expiration_days=expiration_days,
            fields=fields,
            keys=keys,
            object_type_name=object_type_name,
            tags=tags,
            template_id=template_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__091e212a123e3a0cfb8577aebb7068432007378feb06e4af48a00036957ea470)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0769bdf04f2e44acf0d6aa58be6958449e3ed7487344183891e249f5aefe6bea)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the object type was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the object type was most recently edited.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

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
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b24cea9cf31f287c3b3c148ba0586506624f0432fe276fdb1ec08d552833ef32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="allowProfileCreation")
    def allow_profile_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "allowProfileCreation"))

    @allow_profile_creation.setter
    def allow_profile_creation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b0f4dc9c396c634c5fa55ab6032956c1c94c0dec83e089c60d92fb58640061c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowProfileCreation", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the profile object type mapping.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aba990030ebf284cb51fc495ba3f894a3828072faa9f459784674e3467c4e696)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The customer-provided key to encrypt the profile object that will be created in this profile object type mapping.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ca3be4f6e2ca6127ac1ca1adcf9552041402fd0c44217f1d4f13a4e14bf2b40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="expirationDays")
    def expiration_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days until the data of this type expires.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationDays"))

    @expiration_days.setter
    def expiration_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d57ec4a44e9d66c50a3e82cedcef4d73b7c54672341cb6bdc26bb43d5048de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationDays", value)

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.FieldMapProperty"]]]]:
        '''A list of field definitions for the object type mapping.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.FieldMapProperty"]]]], jsii.get(self, "fields"))

    @fields.setter
    def fields(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.FieldMapProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eccf30ab38ee3158514f0243fca4f8f7f38ae86489a3784a2fee01eb15f10f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property
    @jsii.member(jsii_name="keys")
    def keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.KeyMapProperty"]]]]:
        '''A list of keys that can be used to map data to the profile or search for the profile.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.KeyMapProperty"]]]], jsii.get(self, "keys"))

    @keys.setter
    def keys(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.KeyMapProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521c1a4bfa097c3b1f3951ecd6980736e1de35a3bfe50227b262534c59370624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keys", value)

    @builtins.property
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the profile object type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19dbd5a494e7060e32b7c4cc781d4cee2093bd041be3baf6d8b03e5f66d76985)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__034fbef34b9c45ddeef371cddf129b147eb3c6d5cb089d2a874dec871d849617)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateId")
    def template_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the template mapping.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateId"))

    @template_id.setter
    def template_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c3516f296b116ed334a16a7f280bc13da509b7cc1b2d0f53992808db2bf0433)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType.FieldMapProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "object_type_field": "objectTypeField"},
    )
    class FieldMapProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            object_type_field: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObjectType.ObjectTypeFieldProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A map of the name and ObjectType field.

            :param name: Name of the field.
            :param object_type_field: Represents a field in a ProfileObjectType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                field_map_property = customerprofiles.CfnObjectType.FieldMapProperty(
                    name="name",
                    object_type_field=customerprofiles.CfnObjectType.ObjectTypeFieldProperty(
                        content_type="contentType",
                        source="source",
                        target="target"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed4b9fc776f1c6cc0260e8e465d5e13c160ba26b2ed598c73a7b95e98cf61c94)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument object_type_field", value=object_type_field, expected_type=type_hints["object_type_field"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if object_type_field is not None:
                self._values["object_type_field"] = object_type_field

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_type_field(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnObjectType.ObjectTypeFieldProperty"]]:
            '''Represents a field in a ProfileObjectType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-objecttypefield
            '''
            result = self._values.get("object_type_field")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnObjectType.ObjectTypeFieldProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType.KeyMapProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "object_type_key_list": "objectTypeKeyList"},
    )
    class KeyMapProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            object_type_key_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObjectType.ObjectTypeKeyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A unique key map that can be used to map data to the profile.

            :param name: Name of the key.
            :param object_type_key_list: A list of ObjectTypeKey.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                key_map_property = customerprofiles.CfnObjectType.KeyMapProperty(
                    name="name",
                    object_type_key_list=[customerprofiles.CfnObjectType.ObjectTypeKeyProperty(
                        field_names=["fieldNames"],
                        standard_identifiers=["standardIdentifiers"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ea3cec6c8d04e9528d2f478540e3895caf69bc8db4178642b943b32ed3f9261)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument object_type_key_list", value=object_type_key_list, expected_type=type_hints["object_type_key_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if object_type_key_list is not None:
                self._values["object_type_key_list"] = object_type_key_list

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_type_key_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.ObjectTypeKeyProperty"]]]]:
            '''A list of ObjectTypeKey.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-objecttypekeylist
            '''
            result = self._values.get("object_type_key_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.ObjectTypeKeyProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType.ObjectTypeFieldProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content_type": "contentType",
            "source": "source",
            "target": "target",
        },
    )
    class ObjectTypeFieldProperty:
        def __init__(
            self,
            *,
            content_type: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
            target: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a field in a ProfileObjectType.

            :param content_type: The content type of the field. Used for determining equality when searching.
            :param source: A field of a ProfileObject. For example: _source.FirstName, where “_source” is a ProfileObjectType of a Zendesk user and “FirstName” is a field in that ObjectType.
            :param target: The location of the data in the standard ProfileObject model. For example: _profile.Address.PostalCode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                object_type_field_property = customerprofiles.CfnObjectType.ObjectTypeFieldProperty(
                    content_type="contentType",
                    source="source",
                    target="target"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b178f0d9e90930c4a4fd81ab392ed9c808bb1ea28f32cdd69c558694300980b)
                check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content_type is not None:
                self._values["content_type"] = content_type
            if source is not None:
                self._values["source"] = source
            if target is not None:
                self._values["target"] = target

        @builtins.property
        def content_type(self) -> typing.Optional[builtins.str]:
            '''The content type of the field.

            Used for determining equality when searching.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-contenttype
            '''
            result = self._values.get("content_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''A field of a ProfileObject.

            For example: _source.FirstName, where “_source” is a ProfileObjectType of a Zendesk user and “FirstName” is a field in that ObjectType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''The location of the data in the standard ProfileObject model.

            For example: _profile.Address.PostalCode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType.ObjectTypeKeyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_names": "fieldNames",
            "standard_identifiers": "standardIdentifiers",
        },
    )
    class ObjectTypeKeyProperty:
        def __init__(
            self,
            *,
            field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            standard_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''An object that defines the Key element of a ProfileObject.

            A Key is a special element that can be used to search for a customer profile.

            :param field_names: The reference for the key name of the fields map.
            :param standard_identifiers: The types of keys that a ProfileObject can have. Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE means that this key can be used to tie an object to a PROFILE. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                object_type_key_property = customerprofiles.CfnObjectType.ObjectTypeKeyProperty(
                    field_names=["fieldNames"],
                    standard_identifiers=["standardIdentifiers"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7448ca799e207118d55f0019b3c6c35b6416f32804761112746d00e405772897)
                check_type(argname="argument field_names", value=field_names, expected_type=type_hints["field_names"])
                check_type(argname="argument standard_identifiers", value=standard_identifiers, expected_type=type_hints["standard_identifiers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if field_names is not None:
                self._values["field_names"] = field_names
            if standard_identifiers is not None:
                self._values["standard_identifiers"] = standard_identifiers

        @builtins.property
        def field_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The reference for the key name of the fields map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-fieldnames
            '''
            result = self._values.get("field_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def standard_identifiers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The types of keys that a ProfileObject can have.

            Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE means that this key can be used to tie an object to a PROFILE. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers
            '''
            result = self._values.get("standard_identifiers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeKeyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectTypeProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "allow_profile_creation": "allowProfileCreation",
        "description": "description",
        "encryption_key": "encryptionKey",
        "expiration_days": "expirationDays",
        "fields": "fields",
        "keys": "keys",
        "object_type_name": "objectTypeName",
        "tags": "tags",
        "template_id": "templateId",
    },
)
class CfnObjectTypeProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        expiration_days: typing.Optional[jsii.Number] = None,
        fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.FieldMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.KeyMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnObjectType``.

        :param domain_name: The unique name of the domain.
        :param allow_profile_creation: Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is ``FALSE`` . If the AllowProfileCreation flag is set to ``FALSE`` , then the service tries to fetch a standard profile and associate this object with the profile. If it is set to ``TRUE`` , and if no match is found, then the service creates a new standard profile.
        :param description: The description of the profile object type mapping.
        :param encryption_key: The customer-provided key to encrypt the profile object that will be created in this profile object type mapping. If not specified the system will use the encryption key of the domain.
        :param expiration_days: The number of days until the data of this type expires.
        :param fields: A list of field definitions for the object type mapping.
        :param keys: A list of keys that can be used to map data to the profile or search for the profile.
        :param object_type_name: The name of the profile object type.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param template_id: A unique identifier for the template mapping. This can be used instead of specifying the Keys and Fields properties directly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_object_type_props = customerprofiles.CfnObjectTypeProps(
                domain_name="domainName",
            
                # the properties below are optional
                allow_profile_creation=False,
                description="description",
                encryption_key="encryptionKey",
                expiration_days=123,
                fields=[customerprofiles.CfnObjectType.FieldMapProperty(
                    name="name",
                    object_type_field=customerprofiles.CfnObjectType.ObjectTypeFieldProperty(
                        content_type="contentType",
                        source="source",
                        target="target"
                    )
                )],
                keys=[customerprofiles.CfnObjectType.KeyMapProperty(
                    name="name",
                    object_type_key_list=[customerprofiles.CfnObjectType.ObjectTypeKeyProperty(
                        field_names=["fieldNames"],
                        standard_identifiers=["standardIdentifiers"]
                    )]
                )],
                object_type_name="objectTypeName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                template_id="templateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__674aff1f8e16a6059ac0e56bfd831b21c20b3b3358878f53ea82ff2eea85954e)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument allow_profile_creation", value=allow_profile_creation, expected_type=type_hints["allow_profile_creation"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument expiration_days", value=expiration_days, expected_type=type_hints["expiration_days"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
            check_type(argname="argument object_type_name", value=object_type_name, expected_type=type_hints["object_type_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if allow_profile_creation is not None:
            self._values["allow_profile_creation"] = allow_profile_creation
        if description is not None:
            self._values["description"] = description
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if expiration_days is not None:
            self._values["expiration_days"] = expiration_days
        if fields is not None:
            self._values["fields"] = fields
        if keys is not None:
            self._values["keys"] = keys
        if object_type_name is not None:
            self._values["object_type_name"] = object_type_name
        if tags is not None:
            self._values["tags"] = tags
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_profile_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type.

        The default is ``FALSE`` . If the AllowProfileCreation flag is set to ``FALSE`` , then the service tries to fetch a standard profile and associate this object with the profile. If it is set to ``TRUE`` , and if no match is found, then the service creates a new standard profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation
        '''
        result = self._values.get("allow_profile_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the profile object type mapping.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The customer-provided key to encrypt the profile object that will be created in this profile object type mapping.

        If not specified the system will use the encryption key of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days until the data of this type expires.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays
        '''
        result = self._values.get("expiration_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.FieldMapProperty]]]]:
        '''A list of field definitions for the object type mapping.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.FieldMapProperty]]]], result)

    @builtins.property
    def keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.KeyMapProperty]]]]:
        '''A list of keys that can be used to map data to the profile or search for the profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys
        '''
        result = self._values.get("keys")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.KeyMapProperty]]]], result)

    @builtins.property
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the profile object type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename
        '''
        result = self._values.get("object_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the template mapping.

        This can be used instead of specifying the Keys and Fields properties directly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid
        '''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnObjectTypeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCalculatedAttributeDefinition",
    "CfnCalculatedAttributeDefinitionProps",
    "CfnDomain",
    "CfnDomainProps",
    "CfnEventStream",
    "CfnEventStreamProps",
    "CfnIntegration",
    "CfnIntegrationProps",
    "CfnObjectType",
    "CfnObjectTypeProps",
]

publication.publish()

def _typecheckingstub__3a09ab96caa4db6cfa4ebb0207c025a7f976cac18f814d69b882506cf2971669(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    attribute_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.AttributeDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    calculated_attribute_name: builtins.str,
    domain_name: builtins.str,
    statistic: builtins.str,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c355c3b327941e1e80c87b111beedb797243265da934cbe14cb40a04def39b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff2e7320eba6c67e11b5108c4174e965091aab4bf1ed72835487ea46d7bd228(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc094b8898d98fbc0a232ed05081d6ffd11e6092cf72d062c7ab6a1a118b2655(
    value: typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.AttributeDetailsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1874ab73c6c7fb500a83379a356ae12dde9d52f47b68d1b2dfe7fb7772ae682(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__806572f2b3c6f3d60619dab1026866577ec43486c44775df8e7f00f9ec946cc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24137af23c238e226876684e3ad841c56564bd3e9f7c488415d38fbd9560440e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d9f165d8e8dde422309619ae01ce8e4f77e67c1d8707134c0f7c2a25fd53ebc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.ConditionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94c935ac0604ce2b84a26b87f764d32bfa425eb59416e0935dca9d2a010ce58(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64a1f1d0da7758807d6fc0184c03cfdc7c695677f2dd2cfeb300cb009b6e9d69(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66b41ae1f61b2d451c01e8a6b3eabc1ef1fe6f0e51c71a264d46a9df8ec0ad14(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6241b1471123a742a03d1b24e69021bc3c2c3b4a805094f7a6176be6f76da07a(
    *,
    attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.AttributeItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
    expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2af823a61c3449f36ffaa48661361e9de02280cffeeefa5a3d5990a5035cd43b(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d5606a68f168622e019935c1cfd2eb8821e95f36c66313b2a6f7a38cc4e472(
    *,
    object_count: typing.Optional[jsii.Number] = None,
    range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.RangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ThresholdProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4567eb83ac5620aa6be36cbd0e38cdba257d259743e1017616dbc2252fc66f9d(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcc19afa2a314e3392b1f8004f5ce5593298e226e89f8bb3424dc57cefbb2646(
    *,
    operator: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b490cf412d8b10ddc1ddbf98b6d852a5446deca7e9befe3439df8de5169c37dd(
    *,
    attribute_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.AttributeDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    calculated_attribute_name: builtins.str,
    domain_name: builtins.str,
    statistic: builtins.str,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cc1e612474254ea8edde86de3e08226c0c50e450782b3a99c92e87c31b99bad(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    dead_letter_queue_url: typing.Optional[builtins.str] = None,
    default_encryption_key: typing.Optional[builtins.str] = None,
    default_expiration_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd90568f369097b5d7a19088e675226c1257ad9e9ac30f3a478e941435aaaf5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88e553e446de50b16b878a912bc0a5f6f8763a19282b8d9da5099d68ef82e5b6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5155d94ec0a92f02d3b08cff5971632f213635d3dd2577433bbe328e9fac1d90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39213ab6c2161d29ce1bafee3ec589effa27e2d24da755fd856339bb486e25a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9ea79eb70814ff005e2ba351fe52042bea41d55509db4f24fbbf0d33cfb9a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d16654417fe9cbdb9f2b4f0145b59b3328699684a9b2c7ae7f2a3ad9b271e93(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc3d01d93fe80a75ec77ac1c37d929543f51e4a47feb47e25ebd0afa5fee06a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a55eb0b8d16e4b2b2589908d65475847a28870949386381667b6572e627f96(
    *,
    domain_name: builtins.str,
    dead_letter_queue_url: typing.Optional[builtins.str] = None,
    default_encryption_key: typing.Optional[builtins.str] = None,
    default_expiration_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab29d0d747428994b84491cb3989a05a67bcb4cf0b84ebeba8fd19114b7cd61d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    event_stream_name: builtins.str,
    uri: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d37a000675ecf626a3348ff78d7f60db4441f2bb16c208d8dea0d1a4ecbd88f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897cf1ba007446204846a7b757f800cd045b6bea2153894c6a8efdade633eaca(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40edb2a552aa50e0d65e685a232d9e8b469877491c9fd016aaf025966b9a1b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ecaa8f57744bab81313074352cbc2f82cf8f797e78ce582ff548aa6251c330(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d80288203f7d0782baca6858266d8c740f3fda90b2d6ef328306f3e966d5ee4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dcffaefd3d051ab25e983d551d4abe7f28bcc0ccc2cc0f00dfbe9151cc9bd64(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14be2a6e46acdc39b98267227ca646cdeba3edce7277e1499527949bda68cd54(
    *,
    status: builtins.str,
    uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813f95ba6287d3dc18d43b5b2ff35fbde17184e556360b280e3386143cfc00f0(
    *,
    domain_name: builtins.str,
    event_stream_name: builtins.str,
    uri: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8211c08b95eabfe008b27ab5b3b74bab34f671b7bd9761e15cdb090da9d3d95(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    flow_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.FlowDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_type_name: typing.Optional[builtins.str] = None,
    object_type_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ObjectTypeMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85eb075da84dc570034fe72854e5f377beb9454784461fb242856b2b0d6db071(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a02b200ac7ef42474d61bef0afc23d2047a43211308a0f0f346c8804318a953d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d13bac4a06b95e4fadaf50aaed39e2383120484f2d6e868a652119e3c0741a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda84696baed289de5f577073d9697fd7b0969af55567086ad86e6466b533e14(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.FlowDefinitionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ac4be2e5060d6806d086adb14efc1af2df364f07423ea56e6af2958c23fc2b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19e3d184d030db553288fb9b5bf060b201c3b429358e9c4818b39453b44a060(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIntegration.ObjectTypeMappingProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55efe13391c8b01dcc8a4fc8cdb64b30e0590e3c2de5fbdfaf88656f9ad1a18e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e9de6347e213a96d6d3dc4870b6c07c7e7db9b8044cff9f9952e0192a795c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8ff575fc6d67c92e33f52c9a2a9924dd1914b3ec97eb67ea19a5f83109dfe09(
    *,
    marketo: typing.Optional[builtins.str] = None,
    s3: typing.Optional[builtins.str] = None,
    salesforce: typing.Optional[builtins.str] = None,
    service_now: typing.Optional[builtins.str] = None,
    zendesk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__684e26c18461ba90c60337c4f41ecfe0fff4d6e92e5f5ccc4fca2dbb9cb7fe58(
    *,
    flow_name: builtins.str,
    kms_arn: builtins.str,
    source_flow_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.SourceFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    tasks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TaskProperty, typing.Dict[builtins.str, typing.Any]]]]],
    trigger_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TriggerConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30373edbc1fc87d87c0305c0d579d9085e768165db2968c37ebc100141fc94c(
    *,
    datetime_type_field_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a60c86877c43b5afd59790a18d6019039ccc87b2d8b8b5c9299157eda159890(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9afb6e6e9868c0b8b44a3a96fec8e43830e8a548405844dbf1d5a8d81ced10d(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a79daf2a1599613c0d4820e23ade3e1ab729e048f4f33e5e1ca2c56d56a3757b(
    *,
    bucket_name: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d96167457187d54618dd4839b1f9086125a2307ec481de96e070635baf5c77(
    *,
    object: builtins.str,
    enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_deleted_records: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e5944d396eaa65c18b0b184d20b092353bd232b3071af67d1f4668a3a6cb830(
    *,
    schedule_expression: builtins.str,
    data_pull_mode: typing.Optional[builtins.str] = None,
    first_execution_from: typing.Optional[jsii.Number] = None,
    schedule_end_time: typing.Optional[jsii.Number] = None,
    schedule_offset: typing.Optional[jsii.Number] = None,
    schedule_start_time: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e39d4ec6bb5656a7c82bcb644c1e71ed86635052e302daedb141f92c9338d5e(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__886a4a6c1d593aa53fe13ccd79b82bf91be008e3952bb987ac48d2b64b7a6ac9(
    *,
    marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.MarketoSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.S3SourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.SalesforceSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ServiceNowSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ZendeskSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d9871f7bd0e95109d517268a1cdd0da37965b7b7acd24cb1bfd91cacda7d2f(
    *,
    connector_type: builtins.str,
    source_connector_properties: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.SourceConnectorPropertiesProperty, typing.Dict[builtins.str, typing.Any]]],
    connector_profile_name: typing.Optional[builtins.str] = None,
    incremental_pull_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.IncrementalPullConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a6d70493dcc8d57205e11e51993268d52dac180561f2ae05a6aa7eba5fab11(
    *,
    operator_property_key: builtins.str,
    property: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c97356b1cf286df38ebed38c9f4ce8135e5160a1254e87e74e1baaba8f2149f(
    *,
    source_fields: typing.Sequence[builtins.str],
    task_type: builtins.str,
    connector_operator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ConnectorOperatorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    destination_field: typing.Optional[builtins.str] = None,
    task_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TaskPropertiesMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43314febd76ccf4bc3946158640fcdb8e8e2b2e8aa92fe065358b557e5787cdc(
    *,
    trigger_type: builtins.str,
    trigger_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TriggerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d95880464ba4d79437e95620f7b099ab48173665d71b3b3e9925b31023ae79a(
    *,
    scheduled: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ScheduledTriggerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fec16a3ec50ec7d597e7573ae1e24e531163b732505e322d5ef39e9267351db(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52bfebce0bd12cb9d9ed6354b0627c3f2946899ecf1ba8120aa70c1e1e22428d(
    *,
    domain_name: builtins.str,
    flow_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.FlowDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_type_name: typing.Optional[builtins.str] = None,
    object_type_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ObjectTypeMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e58419cb0a7694b5c554275a8721df95dc40489e742a23c76f7830ca5210127a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    expiration_days: typing.Optional[jsii.Number] = None,
    fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.FieldMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.KeyMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    object_type_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__091e212a123e3a0cfb8577aebb7068432007378feb06e4af48a00036957ea470(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0769bdf04f2e44acf0d6aa58be6958449e3ed7487344183891e249f5aefe6bea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b24cea9cf31f287c3b3c148ba0586506624f0432fe276fdb1ec08d552833ef32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b0f4dc9c396c634c5fa55ab6032956c1c94c0dec83e089c60d92fb58640061c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba990030ebf284cb51fc495ba3f894a3828072faa9f459784674e3467c4e696(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ca3be4f6e2ca6127ac1ca1adcf9552041402fd0c44217f1d4f13a4e14bf2b40(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d57ec4a44e9d66c50a3e82cedcef4d73b7c54672341cb6bdc26bb43d5048de(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eccf30ab38ee3158514f0243fca4f8f7f38ae86489a3784a2fee01eb15f10f58(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.FieldMapProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521c1a4bfa097c3b1f3951ecd6980736e1de35a3bfe50227b262534c59370624(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.KeyMapProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19dbd5a494e7060e32b7c4cc781d4cee2093bd041be3baf6d8b03e5f66d76985(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034fbef34b9c45ddeef371cddf129b147eb3c6d5cb089d2a874dec871d849617(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c3516f296b116ed334a16a7f280bc13da509b7cc1b2d0f53992808db2bf0433(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4b9fc776f1c6cc0260e8e465d5e13c160ba26b2ed598c73a7b95e98cf61c94(
    *,
    name: typing.Optional[builtins.str] = None,
    object_type_field: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.ObjectTypeFieldProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea3cec6c8d04e9528d2f478540e3895caf69bc8db4178642b943b32ed3f9261(
    *,
    name: typing.Optional[builtins.str] = None,
    object_type_key_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.ObjectTypeKeyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b178f0d9e90930c4a4fd81ab392ed9c808bb1ea28f32cdd69c558694300980b(
    *,
    content_type: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7448ca799e207118d55f0019b3c6c35b6416f32804761112746d00e405772897(
    *,
    field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    standard_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__674aff1f8e16a6059ac0e56bfd831b21c20b3b3358878f53ea82ff2eea85954e(
    *,
    domain_name: builtins.str,
    allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    expiration_days: typing.Optional[jsii.Number] = None,
    fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.FieldMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.KeyMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    object_type_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
