'''
# AWS::KendraRanking Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_kendraranking as kendraranking
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for KendraRanking construct libraries](https://constructs.dev/search?q=kendraranking)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::KendraRanking resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KendraRanking.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::KendraRanking](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KendraRanking.html).

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
class CfnExecutionPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kendraranking.CfnExecutionPlan",
):
    '''Creates a rescore execution plan.

    A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the ``Rescore`` API. You set the number of capacity units that you require for Amazon Kendra Intelligent Ranking to rescore or re-rank a search service's results.

    For an example of using the ``CreateRescoreExecutionPlan`` API, including using the Python and Java SDKs, see `Semantically ranking a search service's results <https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendraranking-executionplan.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kendraranking as kendraranking
        
        cfn_execution_plan = kendraranking.CfnExecutionPlan(self, "MyCfnExecutionPlan",
            name="name",
        
            # the properties below are optional
            capacity_units=kendraranking.CfnExecutionPlan.CapacityUnitsConfigurationProperty(
                rescore_capacity_units=123
            ),
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
        name: builtins.str,
        capacity_units: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnExecutionPlan.CapacityUnitsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the rescore execution plan.
        :param capacity_units: You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see `Adjusting capacity <https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html>`_ .
        :param description: A description for the rescore execution plan.
        :param tags: A list of key-value pairs that identify or categorize your rescore execution plan. You can also use tags to help control access to the rescore execution plan. Tag keys and values can consist of Unicode letters, digits, white space. They can also consist of underscore, period, colon, equal, plus, and asperand.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ad8ffee997e60c547397dcad2b6175d967468b936a768fcba47720363d43bd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnExecutionPlanProps(
            name=name,
            capacity_units=capacity_units,
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0ca4271c359a22f0adcff780309b5d6d29fe57d367ba67e1cdd09e261476207)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9dd8de73c1eedf442e860206645ff7a5453a42f7ee156ff1d3cb6c0084a8f80)
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
        '''The Amazon Resource Name (ARN) of the rescore execution plan.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the rescore execution plan.

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the rescore execution plan.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0db3b98973e564e5a4b30f991391bb1b49f61fcdec383f174a6613c8158e4ea0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="capacityUnits")
    def capacity_units(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnExecutionPlan.CapacityUnitsConfigurationProperty"]]:
        '''You can set additional capacity units to meet the needs of your rescore execution plan.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnExecutionPlan.CapacityUnitsConfigurationProperty"]], jsii.get(self, "capacityUnits"))

    @capacity_units.setter
    def capacity_units(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnExecutionPlan.CapacityUnitsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf82105f97a1c94ff72a8269c751d540ea7e092450fdb48e2bbdbb2d8314735d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the rescore execution plan.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1db9cba35f7e629b2c9a36f1f2a30a3b2958a4fc872e860756137af869eb2062)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize your rescore execution plan.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55d68c9f299d528d643242539117e67cdcb6d318233fbecc0794963d32a7dd69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendraranking.CfnExecutionPlan.CapacityUnitsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"rescore_capacity_units": "rescoreCapacityUnits"},
    )
    class CapacityUnitsConfigurationProperty:
        def __init__(self, *, rescore_capacity_units: jsii.Number) -> None:
            '''Sets additional capacity units configured for your rescore execution plan.

            A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the ``Rescore`` API. You can add and remove capacity units to fit your usage requirements.

            :param rescore_capacity_units: The amount of extra capacity for your rescore execution plan. A single extra capacity unit for a rescore execution plan provides 0.01 rescore requests per second. You can add up to 1000 extra capacity units.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendraranking-executionplan-capacityunitsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendraranking as kendraranking
                
                capacity_units_configuration_property = kendraranking.CfnExecutionPlan.CapacityUnitsConfigurationProperty(
                    rescore_capacity_units=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a681fa857411b5b813fd3ea51ba3c2278b7c1fb3b2c743dbcaf4c754eb37600)
                check_type(argname="argument rescore_capacity_units", value=rescore_capacity_units, expected_type=type_hints["rescore_capacity_units"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rescore_capacity_units": rescore_capacity_units,
            }

        @builtins.property
        def rescore_capacity_units(self) -> jsii.Number:
            '''The amount of extra capacity for your rescore execution plan.

            A single extra capacity unit for a rescore execution plan provides 0.01 rescore requests per second. You can add up to 1000 extra capacity units.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendraranking-executionplan-capacityunitsconfiguration.html#cfn-kendraranking-executionplan-capacityunitsconfiguration-rescorecapacityunits
            '''
            result = self._values.get("rescore_capacity_units")
            assert result is not None, "Required property 'rescore_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityUnitsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kendraranking.CfnExecutionPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "capacity_units": "capacityUnits",
        "description": "description",
        "tags": "tags",
    },
)
class CfnExecutionPlanProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        capacity_units: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExecutionPlan.CapacityUnitsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnExecutionPlan``.

        :param name: A name for the rescore execution plan.
        :param capacity_units: You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see `Adjusting capacity <https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html>`_ .
        :param description: A description for the rescore execution plan.
        :param tags: A list of key-value pairs that identify or categorize your rescore execution plan. You can also use tags to help control access to the rescore execution plan. Tag keys and values can consist of Unicode letters, digits, white space. They can also consist of underscore, period, colon, equal, plus, and asperand.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendraranking-executionplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kendraranking as kendraranking
            
            cfn_execution_plan_props = kendraranking.CfnExecutionPlanProps(
                name="name",
            
                # the properties below are optional
                capacity_units=kendraranking.CfnExecutionPlan.CapacityUnitsConfigurationProperty(
                    rescore_capacity_units=123
                ),
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6824e9d616fc4857909be0579f7bafbf44cfdbe1f17d09ace318ad6214947d0c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument capacity_units", value=capacity_units, expected_type=type_hints["capacity_units"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if capacity_units is not None:
            self._values["capacity_units"] = capacity_units
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the rescore execution plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendraranking-executionplan.html#cfn-kendraranking-executionplan-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_units(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnExecutionPlan.CapacityUnitsConfigurationProperty]]:
        '''You can set additional capacity units to meet the needs of your rescore execution plan.

        You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see `Adjusting capacity <https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendraranking-executionplan.html#cfn-kendraranking-executionplan-capacityunits
        '''
        result = self._values.get("capacity_units")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnExecutionPlan.CapacityUnitsConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the rescore execution plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendraranking-executionplan.html#cfn-kendraranking-executionplan-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize your rescore execution plan.

        You can also use tags to help control access to the rescore execution plan. Tag keys and values can consist of Unicode letters, digits, white space. They can also consist of underscore, period, colon, equal, plus, and asperand.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendraranking-executionplan.html#cfn-kendraranking-executionplan-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExecutionPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnExecutionPlan",
    "CfnExecutionPlanProps",
]

publication.publish()

def _typecheckingstub__10ad8ffee997e60c547397dcad2b6175d967468b936a768fcba47720363d43bd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    capacity_units: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExecutionPlan.CapacityUnitsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ca4271c359a22f0adcff780309b5d6d29fe57d367ba67e1cdd09e261476207(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9dd8de73c1eedf442e860206645ff7a5453a42f7ee156ff1d3cb6c0084a8f80(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0db3b98973e564e5a4b30f991391bb1b49f61fcdec383f174a6613c8158e4ea0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf82105f97a1c94ff72a8269c751d540ea7e092450fdb48e2bbdbb2d8314735d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnExecutionPlan.CapacityUnitsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1db9cba35f7e629b2c9a36f1f2a30a3b2958a4fc872e860756137af869eb2062(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d68c9f299d528d643242539117e67cdcb6d318233fbecc0794963d32a7dd69(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a681fa857411b5b813fd3ea51ba3c2278b7c1fb3b2c743dbcaf4c754eb37600(
    *,
    rescore_capacity_units: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6824e9d616fc4857909be0579f7bafbf44cfdbe1f17d09ace318ad6214947d0c(
    *,
    name: builtins.str,
    capacity_units: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExecutionPlan.CapacityUnitsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
