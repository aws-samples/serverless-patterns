'''
# Amazon Athena Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_athena as athena
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Athena construct libraries](https://constructs.dev/search?q=athena)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Athena resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Athena.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Athena](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Athena.html).

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


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCapacityReservation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_athena.CfnCapacityReservation",
):
    '''Specifies a capacity reservation with the provided name and number of requested data processing units.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html
    :cloudformationResource: AWS::Athena::CapacityReservation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_athena as athena
        
        cfn_capacity_reservation = athena.CfnCapacityReservation(self, "MyCfnCapacityReservation",
            name="name",
            target_dpus=123,
        
            # the properties below are optional
            capacity_assignment_configuration=athena.CfnCapacityReservation.CapacityAssignmentConfigurationProperty(
                capacity_assignments=[athena.CfnCapacityReservation.CapacityAssignmentProperty(
                    workgroup_names=["workgroupNames"]
                )]
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
        name: builtins.str,
        target_dpus: jsii.Number,
        capacity_assignment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapacityReservation.CapacityAssignmentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the capacity reservation.
        :param target_dpus: The number of data processing units requested.
        :param capacity_assignment_configuration: Assigns Athena workgroups (and hence their queries) to capacity reservations. A capacity reservation can have only one capacity assignment configuration, but the capacity assignment configuration can be made up of multiple individual assignments. Each assignment specifies how Athena queries can consume capacity from the capacity reservation that their workgroup is mapped to.
        :param tags: An array of key-value pairs to apply to the capacity reservation. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7458bc9b2513dcdcbd6a0f9a6fcf8ad6ac0dd26405dc0f98526c7739ed69c27c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCapacityReservationProps(
            name=name,
            target_dpus=target_dpus,
            capacity_assignment_configuration=capacity_assignment_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bcae353c3f5a5e1be964ca831d796ba8924d38d98e4da35f1f4249f28af0833)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c53690919665793c02b948caf7c04a9ead8e6a42334d1d9e82cc4e52fcb473d8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAllocatedDpus")
    def attr_allocated_dpus(self) -> jsii.Number:
        '''The number of data processing units currently allocated.

        :cloudformationAttribute: AllocatedDpus
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAllocatedDpus"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the capacity reservation.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time in UTC epoch millis when the capacity reservation was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastSuccessfulAllocationTime")
    def attr_last_successful_allocation_time(self) -> builtins.str:
        '''The time of the most recent capacity allocation that succeeded.

        :cloudformationAttribute: LastSuccessfulAllocationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastSuccessfulAllocationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the capacity reservation.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the capacity reservation.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e52ca03df32f93c24d4644e58482808fd84da5af0a6c8aad6cd35c472aacb8c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="targetDpus")
    def target_dpus(self) -> jsii.Number:
        '''The number of data processing units requested.'''
        return typing.cast(jsii.Number, jsii.get(self, "targetDpus"))

    @target_dpus.setter
    def target_dpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__673e63d688637c639118c4ff9bd95f6fb3efe1b1a0c8e2ca1005cd0aec265b52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDpus", value)

    @builtins.property
    @jsii.member(jsii_name="capacityAssignmentConfiguration")
    def capacity_assignment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCapacityReservation.CapacityAssignmentConfigurationProperty"]]:
        '''Assigns Athena workgroups (and hence their queries) to capacity reservations.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCapacityReservation.CapacityAssignmentConfigurationProperty"]], jsii.get(self, "capacityAssignmentConfiguration"))

    @capacity_assignment_configuration.setter
    def capacity_assignment_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCapacityReservation.CapacityAssignmentConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a48300257a027470aa2568c3011be47c3a12de78febb9a5d2cbc29c8489c9470)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityAssignmentConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the capacity reservation.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2d5ea5f595f96f7b9cd5f389257bb6c2960294d98f1ab6ad6a6c1ab211b6a2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnCapacityReservation.CapacityAssignmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"capacity_assignments": "capacityAssignments"},
    )
    class CapacityAssignmentConfigurationProperty:
        def __init__(
            self,
            *,
            capacity_assignments: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapacityReservation.CapacityAssignmentProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Assigns Athena workgroups (and hence their queries) to capacity reservations.

            A capacity reservation can have only one capacity assignment configuration, but the capacity assignment configuration can be made up of multiple individual assignments. Each assignment specifies how Athena queries can consume capacity from the capacity reservation that their workgroup is mapped to.

            :param capacity_assignments: The list of assignments that make up the capacity assignment configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                capacity_assignment_configuration_property = athena.CfnCapacityReservation.CapacityAssignmentConfigurationProperty(
                    capacity_assignments=[athena.CfnCapacityReservation.CapacityAssignmentProperty(
                        workgroup_names=["workgroupNames"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db76e33e02ec05ffa8974dcc161a2bc5a3765035346802d58d4dfe7853a80348)
                check_type(argname="argument capacity_assignments", value=capacity_assignments, expected_type=type_hints["capacity_assignments"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "capacity_assignments": capacity_assignments,
            }

        @builtins.property
        def capacity_assignments(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCapacityReservation.CapacityAssignmentProperty"]]]:
            '''The list of assignments that make up the capacity assignment configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignmentconfiguration.html#cfn-athena-capacityreservation-capacityassignmentconfiguration-capacityassignments
            '''
            result = self._values.get("capacity_assignments")
            assert result is not None, "Required property 'capacity_assignments' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCapacityReservation.CapacityAssignmentProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityAssignmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnCapacityReservation.CapacityAssignmentProperty",
        jsii_struct_bases=[],
        name_mapping={"workgroup_names": "workgroupNames"},
    )
    class CapacityAssignmentProperty:
        def __init__(self, *, workgroup_names: typing.Sequence[builtins.str]) -> None:
            '''A mapping between one or more workgroups and a capacity reservation.

            :param workgroup_names: The list of workgroup names for the capacity assignment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                capacity_assignment_property = athena.CfnCapacityReservation.CapacityAssignmentProperty(
                    workgroup_names=["workgroupNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e658c20843cc693ef5569c20bee6d431a496b10c7009acb64986e6a31ca21df2)
                check_type(argname="argument workgroup_names", value=workgroup_names, expected_type=type_hints["workgroup_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workgroup_names": workgroup_names,
            }

        @builtins.property
        def workgroup_names(self) -> typing.List[builtins.str]:
            '''The list of workgroup names for the capacity assignment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignment.html#cfn-athena-capacityreservation-capacityassignment-workgroupnames
            '''
            result = self._values.get("workgroup_names")
            assert result is not None, "Required property 'workgroup_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityAssignmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_athena.CfnCapacityReservationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "target_dpus": "targetDpus",
        "capacity_assignment_configuration": "capacityAssignmentConfiguration",
        "tags": "tags",
    },
)
class CfnCapacityReservationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        target_dpus: jsii.Number,
        capacity_assignment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapacityReservation.CapacityAssignmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCapacityReservation``.

        :param name: The name of the capacity reservation.
        :param target_dpus: The number of data processing units requested.
        :param capacity_assignment_configuration: Assigns Athena workgroups (and hence their queries) to capacity reservations. A capacity reservation can have only one capacity assignment configuration, but the capacity assignment configuration can be made up of multiple individual assignments. Each assignment specifies how Athena queries can consume capacity from the capacity reservation that their workgroup is mapped to.
        :param tags: An array of key-value pairs to apply to the capacity reservation. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_athena as athena
            
            cfn_capacity_reservation_props = athena.CfnCapacityReservationProps(
                name="name",
                target_dpus=123,
            
                # the properties below are optional
                capacity_assignment_configuration=athena.CfnCapacityReservation.CapacityAssignmentConfigurationProperty(
                    capacity_assignments=[athena.CfnCapacityReservation.CapacityAssignmentProperty(
                        workgroup_names=["workgroupNames"]
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a214961375f078f4b3bde83f338ac59ad879fce3adfb57a29b21cf15190a97f8)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_dpus", value=target_dpus, expected_type=type_hints["target_dpus"])
            check_type(argname="argument capacity_assignment_configuration", value=capacity_assignment_configuration, expected_type=type_hints["capacity_assignment_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "target_dpus": target_dpus,
        }
        if capacity_assignment_configuration is not None:
            self._values["capacity_assignment_configuration"] = capacity_assignment_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the capacity reservation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html#cfn-athena-capacityreservation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_dpus(self) -> jsii.Number:
        '''The number of data processing units requested.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html#cfn-athena-capacityreservation-targetdpus
        '''
        result = self._values.get("target_dpus")
        assert result is not None, "Required property 'target_dpus' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def capacity_assignment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCapacityReservation.CapacityAssignmentConfigurationProperty]]:
        '''Assigns Athena workgroups (and hence their queries) to capacity reservations.

        A capacity reservation can have only one capacity assignment configuration, but the capacity assignment configuration can be made up of multiple individual assignments. Each assignment specifies how Athena queries can consume capacity from the capacity reservation that their workgroup is mapped to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html#cfn-athena-capacityreservation-capacityassignmentconfiguration
        '''
        result = self._values.get("capacity_assignment_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCapacityReservation.CapacityAssignmentConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the capacity reservation.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html#cfn-athena-capacityreservation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCapacityReservationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDataCatalog(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_athena.CfnDataCatalog",
):
    '''The AWS::Athena::DataCatalog resource specifies an Amazon Athena data catalog, which contains a name, description, type, parameters, and tags.

    For more information, see `DataCatalog <https://docs.aws.amazon.com/athena/latest/APIReference/API_DataCatalog.html>`_ in the *Amazon Athena API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html
    :cloudformationResource: AWS::Athena::DataCatalog
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_athena as athena
        
        cfn_data_catalog = athena.CfnDataCatalog(self, "MyCfnDataCatalog",
            name="name",
            type="type",
        
            # the properties below are optional
            description="description",
            parameters={
                "parameters_key": "parameters"
            },
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
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the data catalog. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters.
        :param type: The type of data catalog: ``LAMBDA`` for a federated catalog, ``GLUE`` for AWS Glue Catalog, or ``HIVE`` for an external hive metastore.
        :param description: A description of the data catalog.
        :param parameters: Specifies the Lambda function or functions to use for the data catalog. The mapping used depends on the catalog type. - The ``HIVE`` data catalog type uses the following syntax. The ``metadata-function`` parameter is required. ``The sdk-version`` parameter is optional and defaults to the currently supported version. ``metadata-function= *lambda_arn* , sdk-version= *version_number*`` - The ``LAMBDA`` data catalog type uses one of the following sets of required parameters, but not both. - When one Lambda function processes metadata and another Lambda function reads data, the following syntax is used. Both parameters are required. ``metadata-function= *lambda_arn* , record-function= *lambda_arn*`` - A composite Lambda function that processes both metadata and data uses the following syntax. ``function= *lambda_arn*`` - The ``GLUE`` type takes a catalog ID parameter and is required. The ``*catalog_id*`` is the account ID of the AWS account to which the Glue catalog belongs. ``catalog-id= *catalog_id*`` - The ``GLUE`` data catalog type also applies to the default ``AwsDataCatalog`` that already exists in your account, of which you can have only one and cannot modify.
        :param tags: The tags (key-value pairs) to associate with this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05023d61a95576869568bc095d9889b971a9d8c061cba5833a71f44231f3b9e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataCatalogProps(
            name=name,
            type=type,
            description=description,
            parameters=parameters,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70484df33f57719ba2197f7ae86dd846651ec89bd9dc9853fbc4fff3bb342b5e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__53b184d971619ad9ceb2925488e914f96ae85a3537cc1bbc7fcec083c3c925b5)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the data catalog.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1608b3146e652acde24c1f4fa9b482be4691d7f18e63abae7294e6d2be79cd57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of data catalog: ``LAMBDA`` for a federated catalog, ``GLUE`` for AWS Glue Catalog, or ``HIVE`` for an external hive metastore.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__648f5f258b71a886cda692ac680360ffcaf9aa72e0b747dc0986bc6a3da0b9c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the data catalog.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da91751e350be071e1bcad20db12b8878ad53b907a7422a55f53fa3951e8f509)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Specifies the Lambda function or functions to use for the data catalog.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c7bec0cee9cc93380a50923dfa0015a801db986ded37e98f7318cd85af887ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags (key-value pairs) to associate with this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__732720a85a91adafa344b33afc56917f285d76d3c81b8851c7f46aee8ac4b31f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_athena.CfnDataCatalogProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "description": "description",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnDataCatalogProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataCatalog``.

        :param name: The name of the data catalog. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters.
        :param type: The type of data catalog: ``LAMBDA`` for a federated catalog, ``GLUE`` for AWS Glue Catalog, or ``HIVE`` for an external hive metastore.
        :param description: A description of the data catalog.
        :param parameters: Specifies the Lambda function or functions to use for the data catalog. The mapping used depends on the catalog type. - The ``HIVE`` data catalog type uses the following syntax. The ``metadata-function`` parameter is required. ``The sdk-version`` parameter is optional and defaults to the currently supported version. ``metadata-function= *lambda_arn* , sdk-version= *version_number*`` - The ``LAMBDA`` data catalog type uses one of the following sets of required parameters, but not both. - When one Lambda function processes metadata and another Lambda function reads data, the following syntax is used. Both parameters are required. ``metadata-function= *lambda_arn* , record-function= *lambda_arn*`` - A composite Lambda function that processes both metadata and data uses the following syntax. ``function= *lambda_arn*`` - The ``GLUE`` type takes a catalog ID parameter and is required. The ``*catalog_id*`` is the account ID of the AWS account to which the Glue catalog belongs. ``catalog-id= *catalog_id*`` - The ``GLUE`` data catalog type also applies to the default ``AwsDataCatalog`` that already exists in your account, of which you can have only one and cannot modify.
        :param tags: The tags (key-value pairs) to associate with this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_athena as athena
            
            cfn_data_catalog_props = athena.CfnDataCatalogProps(
                name="name",
                type="type",
            
                # the properties below are optional
                description="description",
                parameters={
                    "parameters_key": "parameters"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2151d2fd30be9f56cebbd5adb97d92e074856a6590b6970f5a1cb707de68d79)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the data catalog.

        The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of data catalog: ``LAMBDA`` for a federated catalog, ``GLUE`` for AWS Glue Catalog, or ``HIVE`` for an external hive metastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the data catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Specifies the Lambda function or functions to use for the data catalog.

        The mapping used depends on the catalog type.

        - The ``HIVE`` data catalog type uses the following syntax. The ``metadata-function`` parameter is required. ``The sdk-version`` parameter is optional and defaults to the currently supported version.

        ``metadata-function= *lambda_arn* , sdk-version= *version_number*``

        - The ``LAMBDA`` data catalog type uses one of the following sets of required parameters, but not both.
        - When one Lambda function processes metadata and another Lambda function reads data, the following syntax is used. Both parameters are required.

        ``metadata-function= *lambda_arn* , record-function= *lambda_arn*``

        - A composite Lambda function that processes both metadata and data uses the following syntax.

        ``function= *lambda_arn*``

        - The ``GLUE`` type takes a catalog ID parameter and is required. The ``*catalog_id*`` is the account ID of the AWS account to which the Glue catalog belongs.

        ``catalog-id= *catalog_id*``

        - The ``GLUE`` data catalog type also applies to the default ``AwsDataCatalog`` that already exists in your account, of which you can have only one and cannot modify.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags (key-value pairs) to associate with this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataCatalogProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnNamedQuery(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_athena.CfnNamedQuery",
):
    '''The ``AWS::Athena::NamedQuery`` resource specifies an Amazon Athena saved query, where ``QueryString`` contains the SQL query statements that make up the query.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
    :cloudformationResource: AWS::Athena::NamedQuery
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_athena as athena
        
        cfn_named_query = athena.CfnNamedQuery(self, "MyCfnNamedQuery",
            database="database",
            query_string="queryString",
        
            # the properties below are optional
            description="description",
            name="name",
            work_group="workGroup"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        database: builtins.str,
        query_string: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        work_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param database: The database to which the query belongs.
        :param query_string: The SQL statements that make up the query.
        :param description: The query description.
        :param name: The query name.
        :param work_group: The name of the workgroup that contains the named query.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a6acd727802c2fa7a22438ae44b6660590077a4f16a3e6add10721d6e8db0a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNamedQueryProps(
            database=database,
            query_string=query_string,
            description=description,
            name=name,
            work_group=work_group,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddec5e38097efea59697e1d796fb6a6d88b7ddece86ca310e4558dddfdb308b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf59ed9b65b480c5d847ba252258084274a9caf2a33c0d357ec8831f81ecba20)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrNamedQueryId")
    def attr_named_query_id(self) -> builtins.str:
        '''The unique ID of the query.

        :cloudformationAttribute: NamedQueryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamedQueryId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        '''The database to which the query belongs.'''
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__501cd8c10c3d115e2f7cac0d6afe0b38bf2af9f4c2baa50fa99e8e7ba4327165)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        '''The SQL statements that make up the query.'''
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c663852da3bf6abca104187294becf5134a8fc1a2d9f25c6701872f41fde8ba9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The query description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a745e34dd545f8dc388bc187b5819d2ef704db543656d96e0b9de86430379e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The query name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bff191aa3a040eb433f325a55450844fa2a74753c5b7cc84413e2cda83bd7d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="workGroup")
    def work_group(self) -> typing.Optional[builtins.str]:
        '''The name of the workgroup that contains the named query.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workGroup"))

    @work_group.setter
    def work_group(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb682c36871b1c9d1ea3cca54fdda6bd4c9a2175d91b4bcc2aff8385207d037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workGroup", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_athena.CfnNamedQueryProps",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "query_string": "queryString",
        "description": "description",
        "name": "name",
        "work_group": "workGroup",
    },
)
class CfnNamedQueryProps:
    def __init__(
        self,
        *,
        database: builtins.str,
        query_string: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        work_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnNamedQuery``.

        :param database: The database to which the query belongs.
        :param query_string: The SQL statements that make up the query.
        :param description: The query description.
        :param name: The query name.
        :param work_group: The name of the workgroup that contains the named query.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_athena as athena
            
            cfn_named_query_props = athena.CfnNamedQueryProps(
                database="database",
                query_string="queryString",
            
                # the properties below are optional
                description="description",
                name="name",
                work_group="workGroup"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6843e60f95befbeeac102b484bbd44b76e442a562d520fa09f15e78c6028b865)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument work_group", value=work_group, expected_type=type_hints["work_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "query_string": query_string,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if work_group is not None:
            self._values["work_group"] = work_group

    @builtins.property
    def database(self) -> builtins.str:
        '''The database to which the query belongs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_string(self) -> builtins.str:
        '''The SQL statements that make up the query.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring
        '''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The query description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The query name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def work_group(self) -> typing.Optional[builtins.str]:
        '''The name of the workgroup that contains the named query.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-workgroup
        '''
        result = self._values.get("work_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNamedQueryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPreparedStatement(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_athena.CfnPreparedStatement",
):
    '''Specifies a prepared statement for use with SQL queries in Athena.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html
    :cloudformationResource: AWS::Athena::PreparedStatement
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_athena as athena
        
        cfn_prepared_statement = athena.CfnPreparedStatement(self, "MyCfnPreparedStatement",
            query_statement="queryStatement",
            statement_name="statementName",
            work_group="workGroup",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        query_statement: builtins.str,
        statement_name: builtins.str,
        work_group: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param query_statement: The query string for the prepared statement.
        :param statement_name: The name of the prepared statement.
        :param work_group: The workgroup to which the prepared statement belongs.
        :param description: The description of the prepared statement.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c4c8a39ce9fb61cd606b4abe521c05c0c7c27caa382a68b361cf3be632c8c83)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPreparedStatementProps(
            query_statement=query_statement,
            statement_name=statement_name,
            work_group=work_group,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a69017370b966513d7ca221de45e0ee04038dba0f3e2b7a738436d078d1c48c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0b1adefc3ae78288ead2138671ccc59867e63261ac6fa2f2ea32a85d1c2805f)
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
    @jsii.member(jsii_name="queryStatement")
    def query_statement(self) -> builtins.str:
        '''The query string for the prepared statement.'''
        return typing.cast(builtins.str, jsii.get(self, "queryStatement"))

    @query_statement.setter
    def query_statement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18c5e047fd7a10b962ddfc814e209cbca4ff1a422c2293eb18b16d83af0711a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStatement", value)

    @builtins.property
    @jsii.member(jsii_name="statementName")
    def statement_name(self) -> builtins.str:
        '''The name of the prepared statement.'''
        return typing.cast(builtins.str, jsii.get(self, "statementName"))

    @statement_name.setter
    def statement_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dda65d001efb04fb60a14b983d53ba4365b21f672e62245cf7f61199a432872)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementName", value)

    @builtins.property
    @jsii.member(jsii_name="workGroup")
    def work_group(self) -> builtins.str:
        '''The workgroup to which the prepared statement belongs.'''
        return typing.cast(builtins.str, jsii.get(self, "workGroup"))

    @work_group.setter
    def work_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99d939bc99487519bb0415ef8ada649107f8686d2077741c486620ecf3af8996)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workGroup", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the prepared statement.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f39b664043d33c495a721144bc0de55a433122a4024bcbb066c229ec4cf1fe8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_athena.CfnPreparedStatementProps",
    jsii_struct_bases=[],
    name_mapping={
        "query_statement": "queryStatement",
        "statement_name": "statementName",
        "work_group": "workGroup",
        "description": "description",
    },
)
class CfnPreparedStatementProps:
    def __init__(
        self,
        *,
        query_statement: builtins.str,
        statement_name: builtins.str,
        work_group: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPreparedStatement``.

        :param query_statement: The query string for the prepared statement.
        :param statement_name: The name of the prepared statement.
        :param work_group: The workgroup to which the prepared statement belongs.
        :param description: The description of the prepared statement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_athena as athena
            
            cfn_prepared_statement_props = athena.CfnPreparedStatementProps(
                query_statement="queryStatement",
                statement_name="statementName",
                work_group="workGroup",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__709f141308344c291dfca2deddc79eabfe04118b21e11aa37c781298b5454317)
            check_type(argname="argument query_statement", value=query_statement, expected_type=type_hints["query_statement"])
            check_type(argname="argument statement_name", value=statement_name, expected_type=type_hints["statement_name"])
            check_type(argname="argument work_group", value=work_group, expected_type=type_hints["work_group"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_statement": query_statement,
            "statement_name": statement_name,
            "work_group": work_group,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def query_statement(self) -> builtins.str:
        '''The query string for the prepared statement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-querystatement
        '''
        result = self._values.get("query_statement")
        assert result is not None, "Required property 'query_statement' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_name(self) -> builtins.str:
        '''The name of the prepared statement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-statementname
        '''
        result = self._values.get("statement_name")
        assert result is not None, "Required property 'statement_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def work_group(self) -> builtins.str:
        '''The workgroup to which the prepared statement belongs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-workgroup
        '''
        result = self._values.get("work_group")
        assert result is not None, "Required property 'work_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the prepared statement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPreparedStatementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup",
):
    '''The AWS::Athena::WorkGroup resource specifies an Amazon Athena workgroup, which contains a name, description, creation time, state, and other configuration, listed under ``WorkGroupConfiguration`` .

    Each workgroup enables you to isolate queries for you or your group from other queries in the same account. For more information, see `CreateWorkGroup <https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateWorkGroup.html>`_ in the *Amazon Athena API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html
    :cloudformationResource: AWS::Athena::WorkGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_athena as athena
        
        cfn_work_group = athena.CfnWorkGroup(self, "MyCfnWorkGroup",
            name="name",
        
            # the properties below are optional
            description="description",
            recursive_delete_option=False,
            state="state",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            work_group_configuration=athena.CfnWorkGroup.WorkGroupConfigurationProperty(
                additional_configuration="additionalConfiguration",
                bytes_scanned_cutoff_per_query=123,
                customer_content_encryption_configuration=athena.CfnWorkGroup.CustomerContentEncryptionConfigurationProperty(
                    kms_key="kmsKey"
                ),
                enforce_work_group_configuration=False,
                engine_version=athena.CfnWorkGroup.EngineVersionProperty(
                    effective_engine_version="effectiveEngineVersion",
                    selected_engine_version="selectedEngineVersion"
                ),
                execution_role="executionRole",
                publish_cloud_watch_metrics_enabled=False,
                requester_pays_enabled=False,
                result_configuration=athena.CfnWorkGroup.ResultConfigurationProperty(
                    acl_configuration=athena.CfnWorkGroup.AclConfigurationProperty(
                        s3_acl_option="s3AclOption"
                    ),
                    encryption_configuration=athena.CfnWorkGroup.EncryptionConfigurationProperty(
                        encryption_option="encryptionOption",
        
                        # the properties below are optional
                        kms_key="kmsKey"
                    ),
                    expected_bucket_owner="expectedBucketOwner",
                    output_location="outputLocation"
                )
            ),
            work_group_configuration_updates=athena.CfnWorkGroup.WorkGroupConfigurationUpdatesProperty(
                additional_configuration="additionalConfiguration",
                bytes_scanned_cutoff_per_query=123,
                customer_content_encryption_configuration=athena.CfnWorkGroup.CustomerContentEncryptionConfigurationProperty(
                    kms_key="kmsKey"
                ),
                enforce_work_group_configuration=False,
                engine_version=athena.CfnWorkGroup.EngineVersionProperty(
                    effective_engine_version="effectiveEngineVersion",
                    selected_engine_version="selectedEngineVersion"
                ),
                execution_role="executionRole",
                publish_cloud_watch_metrics_enabled=False,
                remove_bytes_scanned_cutoff_per_query=False,
                remove_customer_content_encryption_configuration=False,
                requester_pays_enabled=False,
                result_configuration_updates=athena.CfnWorkGroup.ResultConfigurationUpdatesProperty(
                    acl_configuration=athena.CfnWorkGroup.AclConfigurationProperty(
                        s3_acl_option="s3AclOption"
                    ),
                    encryption_configuration=athena.CfnWorkGroup.EncryptionConfigurationProperty(
                        encryption_option="encryptionOption",
        
                        # the properties below are optional
                        kms_key="kmsKey"
                    ),
                    expected_bucket_owner="expectedBucketOwner",
                    output_location="outputLocation",
                    remove_acl_configuration=False,
                    remove_encryption_configuration=False,
                    remove_expected_bucket_owner=False,
                    remove_output_location=False
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        recursive_delete_option: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        work_group_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.WorkGroupConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        work_group_configuration_updates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.WorkGroupConfigurationUpdatesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The workgroup name.
        :param description: The workgroup description.
        :param recursive_delete_option: The option to delete a workgroup and its contents even if the workgroup contains any named queries. The default is false.
        :param state: The state of the workgroup: ENABLED or DISABLED.
        :param tags: The tags (key-value pairs) to associate with this resource.
        :param work_group_configuration: The configuration of the workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether Amazon CloudWatch Metrics are enabled for the workgroup, and the limit for the amount of bytes scanned (cutoff) per query, if it is specified. The ``EnforceWorkGroupConfiguration`` option determines whether workgroup settings override client-side query settings.
        :param work_group_configuration_updates: (deprecated) The configuration information that will be updated for this workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, whether the workgroup settings override the client-side settings, and the data usage limit for the amount of bytes scanned per query, if it is specified.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be0f7d9e26f77f516ae56dabfd6aae7d4d7e7404767cea86eb51dbe5a20e9fc9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkGroupProps(
            name=name,
            description=description,
            recursive_delete_option=recursive_delete_option,
            state=state,
            tags=tags,
            work_group_configuration=work_group_configuration,
            work_group_configuration_updates=work_group_configuration_updates,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a89351b058fb473aa673ca436e54b399faeed90f862768d495efb059a3875b1c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f1e5526c989991241a139bb91d1d3a69c3857127a6488cbc9d7a52f30e64b6e)
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
        '''The date and time the workgroup was created, as a UNIX timestamp in seconds.

        For example: ``1582761016`` .

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkGroupConfigurationEngineVersionEffectiveEngineVersion")
    def attr_work_group_configuration_engine_version_effective_engine_version(
        self,
    ) -> builtins.str:
        '''Read only.

        The engine version on which the query runs. If the user requests a valid engine version other than Auto, the effective engine version is the same as the engine version that the user requested. If the user requests Auto, the effective engine version is chosen by Athena. When a request to update the engine version is made by a CreateWorkGroup or UpdateWorkGroup operation, the EffectiveEngineVersion field is ignored.

        :cloudformationAttribute: WorkGroupConfiguration.EngineVersion.EffectiveEngineVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkGroupConfigurationEngineVersionEffectiveEngineVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkGroupConfigurationUpdatesEngineVersionEffectiveEngineVersion")
    def attr_work_group_configuration_updates_engine_version_effective_engine_version(
        self,
    ) -> builtins.str:
        '''Read only.

        The engine version on which the query runs. If the user requests a valid engine version other than Auto, the effective engine version is the same as the engine version that the user requested. If the user requests Auto, the effective engine version is chosen by Athena. When a request to update the engine version is made by a ``CreateWorkGroup`` or ``UpdateWorkGroup`` operation, the ``EffectiveEngineVersion`` field is ignored.

        :cloudformationAttribute: WorkGroupConfigurationUpdates.EngineVersion.EffectiveEngineVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkGroupConfigurationUpdatesEngineVersionEffectiveEngineVersion"))

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
        '''The workgroup name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a0aa36fc7c960f3a6b523e94a0875ba081b0757724ca672dc4d58a5da328d86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The workgroup description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c3416008ff859aa8fd00dc773e06bb93607be2c43f4d8dc1962b2bbcf013c1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="recursiveDeleteOption")
    def recursive_delete_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The option to delete a workgroup and its contents even if the workgroup contains any named queries.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "recursiveDeleteOption"))

    @recursive_delete_option.setter
    def recursive_delete_option(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a00e8480ec3a751e59ec61ecdf367b39021a964ca18fdc42e47cc0ae3bf52b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recursiveDeleteOption", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the workgroup: ENABLED or DISABLED.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ca675b7d3278faf35ffe34635716d8704c5407a6628b6ede3bd1119276aef0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags (key-value pairs) to associate with this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6dca743e6f0d274bbeac5f19381d936c9a4ea24a2a2ebe3fbd3e468b43fc16f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workGroupConfiguration")
    def work_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.WorkGroupConfigurationProperty"]]:
        '''The configuration of the workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether Amazon CloudWatch Metrics are enabled for the workgroup, and the limit for the amount of bytes scanned (cutoff) per query, if it is specified.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.WorkGroupConfigurationProperty"]], jsii.get(self, "workGroupConfiguration"))

    @work_group_configuration.setter
    def work_group_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.WorkGroupConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffe180d9d0a40f65f5055211f5690cad94d8268dbb88d2644e371d7e17725ac6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workGroupConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="workGroupConfigurationUpdates")
    def work_group_configuration_updates(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.WorkGroupConfigurationUpdatesProperty"]]:
        '''(deprecated) The configuration information that will be updated for this workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, whether the workgroup settings override the client-side settings, and the data usage limit for the amount of bytes scanned per query, if it is specified.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.WorkGroupConfigurationUpdatesProperty"]], jsii.get(self, "workGroupConfigurationUpdates"))

    @work_group_configuration_updates.setter
    def work_group_configuration_updates(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.WorkGroupConfigurationUpdatesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a488c1ed1dfb72d7cde64a1f15e1f03602827583e7998463eb0cbad4597ab95a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workGroupConfigurationUpdates", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup.AclConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_acl_option": "s3AclOption"},
    )
    class AclConfigurationProperty:
        def __init__(self, *, s3_acl_option: builtins.str) -> None:
            '''Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results.

            When Athena stores query results in Amazon S3, the canned ACL is set with the ``x-amz-acl`` request header. For more information about S3 Object Ownership, see `Object Ownership settings <https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html#object-ownership-overview>`_ in the *Amazon S3 User Guide* .

            :param s3_acl_option: The Amazon S3 canned ACL that Athena should specify when storing query results. Currently the only supported canned ACL is ``BUCKET_OWNER_FULL_CONTROL`` . If a query runs in a workgroup and the workgroup overrides client-side settings, then the Amazon S3 canned ACL specified in the workgroup's settings is used for all queries that run in the workgroup. For more information about Amazon S3 canned ACLs, see `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl>`_ in the *Amazon S3 User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-aclconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                acl_configuration_property = athena.CfnWorkGroup.AclConfigurationProperty(
                    s3_acl_option="s3AclOption"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d08c097512b882cb470dc37bf746c41eaf32d76443ec31f122bf7863c4eb842)
                check_type(argname="argument s3_acl_option", value=s3_acl_option, expected_type=type_hints["s3_acl_option"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_acl_option": s3_acl_option,
            }

        @builtins.property
        def s3_acl_option(self) -> builtins.str:
            '''The Amazon S3 canned ACL that Athena should specify when storing query results.

            Currently the only supported canned ACL is ``BUCKET_OWNER_FULL_CONTROL`` . If a query runs in a workgroup and the workgroup overrides client-side settings, then the Amazon S3 canned ACL specified in the workgroup's settings is used for all queries that run in the workgroup. For more information about Amazon S3 canned ACLs, see `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl>`_ in the *Amazon S3 User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-aclconfiguration.html#cfn-athena-workgroup-aclconfiguration-s3acloption
            '''
            result = self._values.get("s3_acl_option")
            assert result is not None, "Required property 's3_acl_option' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AclConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup.CustomerContentEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key": "kmsKey"},
    )
    class CustomerContentEncryptionConfigurationProperty:
        def __init__(self, *, kms_key: builtins.str) -> None:
            '''Specifies the customer managed KMS key that is used to encrypt the user's data stores in Athena.

            When an AWS managed key is used, this value is null. This setting does not apply to Athena SQL workgroups.

            :param kms_key: The customer managed KMS key that is used to encrypt the user's data stores in Athena.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-customercontentencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                customer_content_encryption_configuration_property = athena.CfnWorkGroup.CustomerContentEncryptionConfigurationProperty(
                    kms_key="kmsKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3480ab9bdaef6bae695825b3df3eae10d42fc973ee85c1e9d372a5012990c61)
                check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kms_key": kms_key,
            }

        @builtins.property
        def kms_key(self) -> builtins.str:
            '''The customer managed KMS key that is used to encrypt the user's data stores in Athena.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-customercontentencryptionconfiguration.html#cfn-athena-workgroup-customercontentencryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
            assert result is not None, "Required property 'kms_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerContentEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_option": "encryptionOption", "kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_option: builtins.str,
            kms_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''If query results are encrypted in Amazon S3, indicates the encryption option used (for example, ``SSE_KMS`` or ``CSE_KMS`` ) and key information.

            :param encryption_option: Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys ( ``SSE_S3`` ), server-side encryption with KMS-managed keys ( ``SSE_KMS`` ), or client-side encryption with KMS-managed keys ( ``CSE_KMS`` ) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
            :param kms_key: For ``SSE_KMS`` and ``CSE_KMS`` , this is the KMS key ARN or ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                encryption_configuration_property = athena.CfnWorkGroup.EncryptionConfigurationProperty(
                    encryption_option="encryptionOption",
                
                    # the properties below are optional
                    kms_key="kmsKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa79fae7a2ac9eacbed710d8ee5a01ad03c3b9f537094d9f71d622a0bac4b6d7)
                check_type(argname="argument encryption_option", value=encryption_option, expected_type=type_hints["encryption_option"])
                check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_option": encryption_option,
            }
            if kms_key is not None:
                self._values["kms_key"] = kms_key

        @builtins.property
        def encryption_option(self) -> builtins.str:
            '''Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys ( ``SSE_S3`` ), server-side encryption with KMS-managed keys ( ``SSE_KMS`` ), or client-side encryption with KMS-managed keys ( ``CSE_KMS`` ) is used.

            If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-encryptionoption
            '''
            result = self._values.get("encryption_option")
            assert result is not None, "Required property 'encryption_option' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key(self) -> typing.Optional[builtins.str]:
            '''For ``SSE_KMS`` and ``CSE_KMS`` , this is the KMS key ARN or ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup.EngineVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "effective_engine_version": "effectiveEngineVersion",
            "selected_engine_version": "selectedEngineVersion",
        },
    )
    class EngineVersionProperty:
        def __init__(
            self,
            *,
            effective_engine_version: typing.Optional[builtins.str] = None,
            selected_engine_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Athena engine version for running queries, or the PySpark engine version for running sessions.

            :param effective_engine_version: Read only. The engine version on which the query runs. If the user requests a valid engine version other than Auto, the effective engine version is the same as the engine version that the user requested. If the user requests Auto, the effective engine version is chosen by Athena. When a request to update the engine version is made by a ``CreateWorkGroup`` or ``UpdateWorkGroup`` operation, the ``EffectiveEngineVersion`` field is ignored.
            :param selected_engine_version: The engine version requested by the user. Possible values are determined by the output of ``ListEngineVersions`` , including AUTO. The default is AUTO.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                engine_version_property = athena.CfnWorkGroup.EngineVersionProperty(
                    effective_engine_version="effectiveEngineVersion",
                    selected_engine_version="selectedEngineVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__89f0b78a82f24ece8384b490252230129c42a711fdb038b4ecd645d321ca82e1)
                check_type(argname="argument effective_engine_version", value=effective_engine_version, expected_type=type_hints["effective_engine_version"])
                check_type(argname="argument selected_engine_version", value=selected_engine_version, expected_type=type_hints["selected_engine_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if effective_engine_version is not None:
                self._values["effective_engine_version"] = effective_engine_version
            if selected_engine_version is not None:
                self._values["selected_engine_version"] = selected_engine_version

        @builtins.property
        def effective_engine_version(self) -> typing.Optional[builtins.str]:
            '''Read only.

            The engine version on which the query runs. If the user requests a valid engine version other than Auto, the effective engine version is the same as the engine version that the user requested. If the user requests Auto, the effective engine version is chosen by Athena. When a request to update the engine version is made by a ``CreateWorkGroup`` or ``UpdateWorkGroup`` operation, the ``EffectiveEngineVersion`` field is ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-effectiveengineversion
            '''
            result = self._values.get("effective_engine_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def selected_engine_version(self) -> typing.Optional[builtins.str]:
            '''The engine version requested by the user.

            Possible values are determined by the output of ``ListEngineVersions`` , including AUTO. The default is AUTO.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-selectedengineversion
            '''
            result = self._values.get("selected_engine_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EngineVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup.ResultConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acl_configuration": "aclConfiguration",
            "encryption_configuration": "encryptionConfiguration",
            "expected_bucket_owner": "expectedBucketOwner",
            "output_location": "outputLocation",
        },
    )
    class ResultConfigurationProperty:
        def __init__(
            self,
            *,
            acl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.AclConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            expected_bucket_owner: typing.Optional[builtins.str] = None,
            output_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query and calculation results.

            These are known as "client-side settings". If workgroup settings override client-side settings, then the query uses the workgroup settings.

            :param acl_configuration: Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results. Currently the only supported canned ACL is ``BUCKET_OWNER_FULL_CONTROL`` . This is a client-side setting. If workgroup settings override client-side settings, then the query uses the ACL configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See ``EnforceWorkGroupConfiguration`` .
            :param encryption_configuration: If query results are encrypted in Amazon S3, indicates the encryption option used (for example, ``SSE_KMS`` or ``CSE_KMS`` ) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See ``EnforceWorkGroupConfiguration`` and `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .
            :param expected_bucket_owner: The account ID that you expect to be the owner of the Amazon S3 bucket specified by ``ResultConfiguration:OutputLocation`` . If set, Athena uses the value for ``ExpectedBucketOwner`` when it makes Amazon S3 calls to your specified output location. If the ``ExpectedBucketOwner`` account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the ``ExpectedBucketOwner`` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See ``EnforceWorkGroupConfiguration`` .
            :param output_location: The location in Amazon S3 where your query results are stored, such as ``s3://path/to/query/bucket/`` . To run a query, you must specify the query results location using either a client-side setting for individual queries or a location specified by the workgroup. If workgroup settings override client-side settings, then the query uses the location specified for the workgroup. If no query location is set, Athena issues an error. For more information, see `Working with Query Results, Output Files, and Query History <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`_ and ``EnforceWorkGroupConfiguration`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                result_configuration_property = athena.CfnWorkGroup.ResultConfigurationProperty(
                    acl_configuration=athena.CfnWorkGroup.AclConfigurationProperty(
                        s3_acl_option="s3AclOption"
                    ),
                    encryption_configuration=athena.CfnWorkGroup.EncryptionConfigurationProperty(
                        encryption_option="encryptionOption",
                
                        # the properties below are optional
                        kms_key="kmsKey"
                    ),
                    expected_bucket_owner="expectedBucketOwner",
                    output_location="outputLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86d94b0afb15160d6ec72666a7574c95b2d16afd21c5ca80a9f352f319f2f46c)
                check_type(argname="argument acl_configuration", value=acl_configuration, expected_type=type_hints["acl_configuration"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
                check_type(argname="argument expected_bucket_owner", value=expected_bucket_owner, expected_type=type_hints["expected_bucket_owner"])
                check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if acl_configuration is not None:
                self._values["acl_configuration"] = acl_configuration
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if expected_bucket_owner is not None:
                self._values["expected_bucket_owner"] = expected_bucket_owner
            if output_location is not None:
                self._values["output_location"] = output_location

        @builtins.property
        def acl_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.AclConfigurationProperty"]]:
            '''Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results.

            Currently the only supported canned ACL is ``BUCKET_OWNER_FULL_CONTROL`` . This is a client-side setting. If workgroup settings override client-side settings, then the query uses the ACL configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See ``EnforceWorkGroupConfiguration`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-aclconfiguration
            '''
            result = self._values.get("acl_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.AclConfigurationProperty"]], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.EncryptionConfigurationProperty"]]:
            '''If query results are encrypted in Amazon S3, indicates the encryption option used (for example, ``SSE_KMS`` or ``CSE_KMS`` ) and key information.

            This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See ``EnforceWorkGroupConfiguration`` and `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def expected_bucket_owner(self) -> typing.Optional[builtins.str]:
            '''The account ID that you expect to be the owner of the Amazon S3 bucket specified by ``ResultConfiguration:OutputLocation`` .

            If set, Athena uses the value for ``ExpectedBucketOwner`` when it makes Amazon S3 calls to your specified output location. If the ``ExpectedBucketOwner`` account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.

            This is a client-side setting. If workgroup settings override client-side settings, then the query uses the ``ExpectedBucketOwner`` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See ``EnforceWorkGroupConfiguration`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-expectedbucketowner
            '''
            result = self._values.get("expected_bucket_owner")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_location(self) -> typing.Optional[builtins.str]:
            '''The location in Amazon S3 where your query results are stored, such as ``s3://path/to/query/bucket/`` .

            To run a query, you must specify the query results location using either a client-side setting for individual queries or a location specified by the workgroup. If workgroup settings override client-side settings, then the query uses the location specified for the workgroup. If no query location is set, Athena issues an error. For more information, see `Working with Query Results, Output Files, and Query History <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`_ and ``EnforceWorkGroupConfiguration`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-outputlocation
            '''
            result = self._values.get("output_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResultConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup.ResultConfigurationUpdatesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acl_configuration": "aclConfiguration",
            "encryption_configuration": "encryptionConfiguration",
            "expected_bucket_owner": "expectedBucketOwner",
            "output_location": "outputLocation",
            "remove_acl_configuration": "removeAclConfiguration",
            "remove_encryption_configuration": "removeEncryptionConfiguration",
            "remove_expected_bucket_owner": "removeExpectedBucketOwner",
            "remove_output_location": "removeOutputLocation",
        },
    )
    class ResultConfigurationUpdatesProperty:
        def __init__(
            self,
            *,
            acl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.AclConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            expected_bucket_owner: typing.Optional[builtins.str] = None,
            output_location: typing.Optional[builtins.str] = None,
            remove_acl_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            remove_encryption_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            remove_expected_bucket_owner: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            remove_output_location: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The information about the updates in the query results, such as output location and encryption configuration for the query results.

            :param acl_configuration: The ACL configuration for the query results.
            :param encryption_configuration: The encryption configuration for the query results.
            :param expected_bucket_owner: The AWS account ID that you expect to be the owner of the Amazon S3 bucket specified by ``ResultConfiguration$OutputLocation`` . If set, Athena uses the value for ``ExpectedBucketOwner`` when it makes Amazon S3 calls to your specified output location. If the ``ExpectedBucketOwner`` AWS account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error. If workgroup settings override client-side settings, then the query uses the ``ExpectedBucketOwner`` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See ``WorkGroupConfiguration$EnforceWorkGroupConfiguration`` and `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .
            :param output_location: The location in Amazon S3 where your query results are stored, such as ``s3://path/to/query/bucket/`` . For more information, see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`_ If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup. The "workgroup settings override" is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See ``EnforceWorkGroupConfiguration`` .
            :param remove_acl_configuration: If set to ``true`` , indicates that the previously-specified ACL configuration for queries in this workgroup should be ignored and set to null. If set to ``false`` or not set, and a value is present in the ``AclConfiguration`` of ``ResultConfigurationUpdates`` , the ``AclConfiguration`` in the workgroup's ``ResultConfiguration`` is updated with the new value. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .
            :param remove_encryption_configuration: If set to "true", indicates that the previously-specified encryption configuration (also known as the client-side setting) for queries in this workgroup should be ignored and set to null. If set to "false" or not set, and a value is present in the EncryptionConfiguration in ResultConfigurationUpdates (the client-side setting), the EncryptionConfiguration in the workgroup's ResultConfiguration will be updated with the new value. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .
            :param remove_expected_bucket_owner: If set to "true", removes the AWS account ID previously specified for ``ResultConfiguration$ExpectedBucketOwner`` . If set to "false" or not set, and a value is present in the ``ExpectedBucketOwner`` in ``ResultConfigurationUpdates`` (the client-side setting), the ``ExpectedBucketOwner`` in the workgroup's ``ResultConfiguration`` is updated with the new value. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .
            :param remove_output_location: If set to "true", indicates that the previously-specified query results location (also known as a client-side setting) for queries in this workgroup should be ignored and set to null. If set to "false" or not set, and a value is present in the OutputLocation in ResultConfigurationUpdates (the client-side setting), the OutputLocation in the workgroup's ResultConfiguration will be updated with the new value. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                result_configuration_updates_property = athena.CfnWorkGroup.ResultConfigurationUpdatesProperty(
                    acl_configuration=athena.CfnWorkGroup.AclConfigurationProperty(
                        s3_acl_option="s3AclOption"
                    ),
                    encryption_configuration=athena.CfnWorkGroup.EncryptionConfigurationProperty(
                        encryption_option="encryptionOption",
                
                        # the properties below are optional
                        kms_key="kmsKey"
                    ),
                    expected_bucket_owner="expectedBucketOwner",
                    output_location="outputLocation",
                    remove_acl_configuration=False,
                    remove_encryption_configuration=False,
                    remove_expected_bucket_owner=False,
                    remove_output_location=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dfde88e9cbba4fc81da00b04c8cc63d678d91113cf67503da9a7475c7688b0c5)
                check_type(argname="argument acl_configuration", value=acl_configuration, expected_type=type_hints["acl_configuration"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
                check_type(argname="argument expected_bucket_owner", value=expected_bucket_owner, expected_type=type_hints["expected_bucket_owner"])
                check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
                check_type(argname="argument remove_acl_configuration", value=remove_acl_configuration, expected_type=type_hints["remove_acl_configuration"])
                check_type(argname="argument remove_encryption_configuration", value=remove_encryption_configuration, expected_type=type_hints["remove_encryption_configuration"])
                check_type(argname="argument remove_expected_bucket_owner", value=remove_expected_bucket_owner, expected_type=type_hints["remove_expected_bucket_owner"])
                check_type(argname="argument remove_output_location", value=remove_output_location, expected_type=type_hints["remove_output_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if acl_configuration is not None:
                self._values["acl_configuration"] = acl_configuration
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if expected_bucket_owner is not None:
                self._values["expected_bucket_owner"] = expected_bucket_owner
            if output_location is not None:
                self._values["output_location"] = output_location
            if remove_acl_configuration is not None:
                self._values["remove_acl_configuration"] = remove_acl_configuration
            if remove_encryption_configuration is not None:
                self._values["remove_encryption_configuration"] = remove_encryption_configuration
            if remove_expected_bucket_owner is not None:
                self._values["remove_expected_bucket_owner"] = remove_expected_bucket_owner
            if remove_output_location is not None:
                self._values["remove_output_location"] = remove_output_location

        @builtins.property
        def acl_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.AclConfigurationProperty"]]:
            '''The ACL configuration for the query results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-aclconfiguration
            '''
            result = self._values.get("acl_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.AclConfigurationProperty"]], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.EncryptionConfigurationProperty"]]:
            '''The encryption configuration for the query results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def expected_bucket_owner(self) -> typing.Optional[builtins.str]:
            '''The AWS account ID that you expect to be the owner of the Amazon S3 bucket specified by ``ResultConfiguration$OutputLocation`` .

            If set, Athena uses the value for ``ExpectedBucketOwner`` when it makes Amazon S3 calls to your specified output location. If the ``ExpectedBucketOwner`` AWS account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.

            If workgroup settings override client-side settings, then the query uses the ``ExpectedBucketOwner`` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See ``WorkGroupConfiguration$EnforceWorkGroupConfiguration`` and `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-expectedbucketowner
            '''
            result = self._values.get("expected_bucket_owner")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_location(self) -> typing.Optional[builtins.str]:
            '''The location in Amazon S3 where your query results are stored, such as ``s3://path/to/query/bucket/`` .

            For more information, see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`_ If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup. The "workgroup settings override" is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See ``EnforceWorkGroupConfiguration`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-outputlocation
            '''
            result = self._values.get("output_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_acl_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to ``true`` , indicates that the previously-specified ACL configuration for queries in this workgroup should be ignored and set to null.

            If set to ``false`` or not set, and a value is present in the ``AclConfiguration`` of ``ResultConfigurationUpdates`` , the ``AclConfiguration`` in the workgroup's ``ResultConfiguration`` is updated with the new value. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeaclconfiguration
            '''
            result = self._values.get("remove_acl_configuration")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def remove_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to "true", indicates that the previously-specified encryption configuration (also known as the client-side setting) for queries in this workgroup should be ignored and set to null.

            If set to "false" or not set, and a value is present in the EncryptionConfiguration in ResultConfigurationUpdates (the client-side setting), the EncryptionConfiguration in the workgroup's ResultConfiguration will be updated with the new value. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeencryptionconfiguration
            '''
            result = self._values.get("remove_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def remove_expected_bucket_owner(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to "true", removes the AWS account ID previously specified for ``ResultConfiguration$ExpectedBucketOwner`` .

            If set to "false" or not set, and a value is present in the ``ExpectedBucketOwner`` in ``ResultConfigurationUpdates`` (the client-side setting), the ``ExpectedBucketOwner`` in the workgroup's ``ResultConfiguration`` is updated with the new value. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeexpectedbucketowner
            '''
            result = self._values.get("remove_expected_bucket_owner")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def remove_output_location(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to "true", indicates that the previously-specified query results location (also known as a client-side setting) for queries in this workgroup should be ignored and set to null.

            If set to "false" or not set, and a value is present in the OutputLocation in ResultConfigurationUpdates (the client-side setting), the OutputLocation in the workgroup's ResultConfiguration will be updated with the new value. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeoutputlocation
            '''
            result = self._values.get("remove_output_location")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResultConfigurationUpdatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup.WorkGroupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_configuration": "additionalConfiguration",
            "bytes_scanned_cutoff_per_query": "bytesScannedCutoffPerQuery",
            "customer_content_encryption_configuration": "customerContentEncryptionConfiguration",
            "enforce_work_group_configuration": "enforceWorkGroupConfiguration",
            "engine_version": "engineVersion",
            "execution_role": "executionRole",
            "publish_cloud_watch_metrics_enabled": "publishCloudWatchMetricsEnabled",
            "requester_pays_enabled": "requesterPaysEnabled",
            "result_configuration": "resultConfiguration",
        },
    )
    class WorkGroupConfigurationProperty:
        def __init__(
            self,
            *,
            additional_configuration: typing.Optional[builtins.str] = None,
            bytes_scanned_cutoff_per_query: typing.Optional[jsii.Number] = None,
            customer_content_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.CustomerContentEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enforce_work_group_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            engine_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.EngineVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            execution_role: typing.Optional[builtins.str] = None,
            publish_cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            requester_pays_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.ResultConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration of the workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether Amazon CloudWatch Metrics are enabled for the workgroup, and the limit for the amount of bytes scanned (cutoff) per query, if it is specified.

            The ``EnforceWorkGroupConfiguration`` option determines whether workgroup settings override client-side query settings.

            :param additional_configuration: Specifies a user defined JSON string that is passed to the session engine.
            :param bytes_scanned_cutoff_per_query: The upper limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. No default is defined. .. epigraph:: This property currently supports integer types. Support for long values is planned.
            :param customer_content_encryption_configuration: Specifies the KMS key that is used to encrypt the user's data stores in Athena. This setting does not apply to Athena SQL workgroups.
            :param enforce_work_group_configuration: If set to "true", the settings for the workgroup override client-side settings. If set to "false", client-side settings are used. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .
            :param engine_version: The engine version that all queries running on the workgroup use.
            :param execution_role: Role used to access user resources in an Athena for Apache Spark session. This property applies only to Spark-enabled workgroups in Athena.
            :param publish_cloud_watch_metrics_enabled: Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.
            :param requester_pays_enabled: If set to ``true`` , allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries. If set to ``false`` , workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is ``false`` . For more information about Requester Pays buckets, see `Requester Pays Buckets <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`_ in the *Amazon Simple Storage Service Developer Guide* .
            :param result_configuration: Specifies the location in Amazon S3 where query results are stored and the encryption option, if any, used for query results. For more information, see `Working with Query Results, Output Files, and Query History <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                work_group_configuration_property = athena.CfnWorkGroup.WorkGroupConfigurationProperty(
                    additional_configuration="additionalConfiguration",
                    bytes_scanned_cutoff_per_query=123,
                    customer_content_encryption_configuration=athena.CfnWorkGroup.CustomerContentEncryptionConfigurationProperty(
                        kms_key="kmsKey"
                    ),
                    enforce_work_group_configuration=False,
                    engine_version=athena.CfnWorkGroup.EngineVersionProperty(
                        effective_engine_version="effectiveEngineVersion",
                        selected_engine_version="selectedEngineVersion"
                    ),
                    execution_role="executionRole",
                    publish_cloud_watch_metrics_enabled=False,
                    requester_pays_enabled=False,
                    result_configuration=athena.CfnWorkGroup.ResultConfigurationProperty(
                        acl_configuration=athena.CfnWorkGroup.AclConfigurationProperty(
                            s3_acl_option="s3AclOption"
                        ),
                        encryption_configuration=athena.CfnWorkGroup.EncryptionConfigurationProperty(
                            encryption_option="encryptionOption",
                
                            # the properties below are optional
                            kms_key="kmsKey"
                        ),
                        expected_bucket_owner="expectedBucketOwner",
                        output_location="outputLocation"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5bc58a8f7fc071c8f6e3cf6044079ec303e9ba8521ef96ca98c62cfdd175a6a8)
                check_type(argname="argument additional_configuration", value=additional_configuration, expected_type=type_hints["additional_configuration"])
                check_type(argname="argument bytes_scanned_cutoff_per_query", value=bytes_scanned_cutoff_per_query, expected_type=type_hints["bytes_scanned_cutoff_per_query"])
                check_type(argname="argument customer_content_encryption_configuration", value=customer_content_encryption_configuration, expected_type=type_hints["customer_content_encryption_configuration"])
                check_type(argname="argument enforce_work_group_configuration", value=enforce_work_group_configuration, expected_type=type_hints["enforce_work_group_configuration"])
                check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
                check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
                check_type(argname="argument publish_cloud_watch_metrics_enabled", value=publish_cloud_watch_metrics_enabled, expected_type=type_hints["publish_cloud_watch_metrics_enabled"])
                check_type(argname="argument requester_pays_enabled", value=requester_pays_enabled, expected_type=type_hints["requester_pays_enabled"])
                check_type(argname="argument result_configuration", value=result_configuration, expected_type=type_hints["result_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if additional_configuration is not None:
                self._values["additional_configuration"] = additional_configuration
            if bytes_scanned_cutoff_per_query is not None:
                self._values["bytes_scanned_cutoff_per_query"] = bytes_scanned_cutoff_per_query
            if customer_content_encryption_configuration is not None:
                self._values["customer_content_encryption_configuration"] = customer_content_encryption_configuration
            if enforce_work_group_configuration is not None:
                self._values["enforce_work_group_configuration"] = enforce_work_group_configuration
            if engine_version is not None:
                self._values["engine_version"] = engine_version
            if execution_role is not None:
                self._values["execution_role"] = execution_role
            if publish_cloud_watch_metrics_enabled is not None:
                self._values["publish_cloud_watch_metrics_enabled"] = publish_cloud_watch_metrics_enabled
            if requester_pays_enabled is not None:
                self._values["requester_pays_enabled"] = requester_pays_enabled
            if result_configuration is not None:
                self._values["result_configuration"] = result_configuration

        @builtins.property
        def additional_configuration(self) -> typing.Optional[builtins.str]:
            '''Specifies a user defined JSON string that is passed to the session engine.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-additionalconfiguration
            '''
            result = self._values.get("additional_configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bytes_scanned_cutoff_per_query(self) -> typing.Optional[jsii.Number]:
            '''The upper limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.

            No default is defined.
            .. epigraph::

               This property currently supports integer types. Support for long values is planned.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-bytesscannedcutoffperquery
            '''
            result = self._values.get("bytes_scanned_cutoff_per_query")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def customer_content_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.CustomerContentEncryptionConfigurationProperty"]]:
            '''Specifies the KMS key that is used to encrypt the user's data stores in Athena.

            This setting does not apply to Athena SQL workgroups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-customercontentencryptionconfiguration
            '''
            result = self._values.get("customer_content_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.CustomerContentEncryptionConfigurationProperty"]], result)

        @builtins.property
        def enforce_work_group_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to "true", the settings for the workgroup override client-side settings.

            If set to "false", client-side settings are used. For more information, see `Workgroup Settings Override Client-Side Settings <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration
            '''
            result = self._values.get("enforce_work_group_configuration")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def engine_version(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.EngineVersionProperty"]]:
            '''The engine version that all queries running on the workgroup use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-engineversion
            '''
            result = self._values.get("engine_version")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.EngineVersionProperty"]], result)

        @builtins.property
        def execution_role(self) -> typing.Optional[builtins.str]:
            '''Role used to access user resources in an Athena for Apache Spark session.

            This property applies only to Spark-enabled workgroups in Athena.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-executionrole
            '''
            result = self._values.get("execution_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def publish_cloud_watch_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-publishcloudwatchmetricsenabled
            '''
            result = self._values.get("publish_cloud_watch_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def requester_pays_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to ``true`` , allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries.

            If set to ``false`` , workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is ``false`` . For more information about Requester Pays buckets, see `Requester Pays Buckets <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`_ in the *Amazon Simple Storage Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-requesterpaysenabled
            '''
            result = self._values.get("requester_pays_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def result_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.ResultConfigurationProperty"]]:
            '''Specifies the location in Amazon S3 where query results are stored and the encryption option, if any, used for query results.

            For more information, see `Working with Query Results, Output Files, and Query History <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-resultconfiguration
            '''
            result = self._values.get("result_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.ResultConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkGroupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroup.WorkGroupConfigurationUpdatesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_configuration": "additionalConfiguration",
            "bytes_scanned_cutoff_per_query": "bytesScannedCutoffPerQuery",
            "customer_content_encryption_configuration": "customerContentEncryptionConfiguration",
            "enforce_work_group_configuration": "enforceWorkGroupConfiguration",
            "engine_version": "engineVersion",
            "execution_role": "executionRole",
            "publish_cloud_watch_metrics_enabled": "publishCloudWatchMetricsEnabled",
            "remove_bytes_scanned_cutoff_per_query": "removeBytesScannedCutoffPerQuery",
            "remove_customer_content_encryption_configuration": "removeCustomerContentEncryptionConfiguration",
            "requester_pays_enabled": "requesterPaysEnabled",
            "result_configuration_updates": "resultConfigurationUpdates",
        },
    )
    class WorkGroupConfigurationUpdatesProperty:
        def __init__(
            self,
            *,
            additional_configuration: typing.Optional[builtins.str] = None,
            bytes_scanned_cutoff_per_query: typing.Optional[jsii.Number] = None,
            customer_content_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.CustomerContentEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enforce_work_group_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            engine_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.EngineVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            execution_role: typing.Optional[builtins.str] = None,
            publish_cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            remove_bytes_scanned_cutoff_per_query: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            remove_customer_content_encryption_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            requester_pays_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            result_configuration_updates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkGroup.ResultConfigurationUpdatesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration information that will be updated for this workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, whether the workgroup settings override the client-side settings, and the data usage limit for the amount of bytes scanned per query, if it is specified.

            :param additional_configuration: Additional Configuration that are passed to Athena Spark Calculations running in this workgroup.
            :param bytes_scanned_cutoff_per_query: The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.
            :param customer_content_encryption_configuration: Indicates the KMS key for encrypting notebook content.
            :param enforce_work_group_configuration: If set to "true", the settings for the workgroup override client-side settings. If set to "false", client-side settings are used
            :param engine_version: The Athena engine version for running queries.
            :param execution_role: Execution Role ARN required to run Athena Spark Calculations.
            :param publish_cloud_watch_metrics_enabled: Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.
            :param remove_bytes_scanned_cutoff_per_query: Indicates that the data usage control limit per query is removed.
            :param remove_customer_content_encryption_configuration: 
            :param requester_pays_enabled: If set to true, allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries. If set to false, workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error.
            :param result_configuration_updates: The result configuration information about the queries in this workgroup that will be updated. Includes the updated results location and an updated option for encrypting query results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_athena as athena
                
                work_group_configuration_updates_property = athena.CfnWorkGroup.WorkGroupConfigurationUpdatesProperty(
                    additional_configuration="additionalConfiguration",
                    bytes_scanned_cutoff_per_query=123,
                    customer_content_encryption_configuration=athena.CfnWorkGroup.CustomerContentEncryptionConfigurationProperty(
                        kms_key="kmsKey"
                    ),
                    enforce_work_group_configuration=False,
                    engine_version=athena.CfnWorkGroup.EngineVersionProperty(
                        effective_engine_version="effectiveEngineVersion",
                        selected_engine_version="selectedEngineVersion"
                    ),
                    execution_role="executionRole",
                    publish_cloud_watch_metrics_enabled=False,
                    remove_bytes_scanned_cutoff_per_query=False,
                    remove_customer_content_encryption_configuration=False,
                    requester_pays_enabled=False,
                    result_configuration_updates=athena.CfnWorkGroup.ResultConfigurationUpdatesProperty(
                        acl_configuration=athena.CfnWorkGroup.AclConfigurationProperty(
                            s3_acl_option="s3AclOption"
                        ),
                        encryption_configuration=athena.CfnWorkGroup.EncryptionConfigurationProperty(
                            encryption_option="encryptionOption",
                
                            # the properties below are optional
                            kms_key="kmsKey"
                        ),
                        expected_bucket_owner="expectedBucketOwner",
                        output_location="outputLocation",
                        remove_acl_configuration=False,
                        remove_encryption_configuration=False,
                        remove_expected_bucket_owner=False,
                        remove_output_location=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d600654f5aa48cb49fd4baf2a677e5f7725dcfa1249836427c1d9f65a0904de)
                check_type(argname="argument additional_configuration", value=additional_configuration, expected_type=type_hints["additional_configuration"])
                check_type(argname="argument bytes_scanned_cutoff_per_query", value=bytes_scanned_cutoff_per_query, expected_type=type_hints["bytes_scanned_cutoff_per_query"])
                check_type(argname="argument customer_content_encryption_configuration", value=customer_content_encryption_configuration, expected_type=type_hints["customer_content_encryption_configuration"])
                check_type(argname="argument enforce_work_group_configuration", value=enforce_work_group_configuration, expected_type=type_hints["enforce_work_group_configuration"])
                check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
                check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
                check_type(argname="argument publish_cloud_watch_metrics_enabled", value=publish_cloud_watch_metrics_enabled, expected_type=type_hints["publish_cloud_watch_metrics_enabled"])
                check_type(argname="argument remove_bytes_scanned_cutoff_per_query", value=remove_bytes_scanned_cutoff_per_query, expected_type=type_hints["remove_bytes_scanned_cutoff_per_query"])
                check_type(argname="argument remove_customer_content_encryption_configuration", value=remove_customer_content_encryption_configuration, expected_type=type_hints["remove_customer_content_encryption_configuration"])
                check_type(argname="argument requester_pays_enabled", value=requester_pays_enabled, expected_type=type_hints["requester_pays_enabled"])
                check_type(argname="argument result_configuration_updates", value=result_configuration_updates, expected_type=type_hints["result_configuration_updates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if additional_configuration is not None:
                self._values["additional_configuration"] = additional_configuration
            if bytes_scanned_cutoff_per_query is not None:
                self._values["bytes_scanned_cutoff_per_query"] = bytes_scanned_cutoff_per_query
            if customer_content_encryption_configuration is not None:
                self._values["customer_content_encryption_configuration"] = customer_content_encryption_configuration
            if enforce_work_group_configuration is not None:
                self._values["enforce_work_group_configuration"] = enforce_work_group_configuration
            if engine_version is not None:
                self._values["engine_version"] = engine_version
            if execution_role is not None:
                self._values["execution_role"] = execution_role
            if publish_cloud_watch_metrics_enabled is not None:
                self._values["publish_cloud_watch_metrics_enabled"] = publish_cloud_watch_metrics_enabled
            if remove_bytes_scanned_cutoff_per_query is not None:
                self._values["remove_bytes_scanned_cutoff_per_query"] = remove_bytes_scanned_cutoff_per_query
            if remove_customer_content_encryption_configuration is not None:
                self._values["remove_customer_content_encryption_configuration"] = remove_customer_content_encryption_configuration
            if requester_pays_enabled is not None:
                self._values["requester_pays_enabled"] = requester_pays_enabled
            if result_configuration_updates is not None:
                self._values["result_configuration_updates"] = result_configuration_updates

        @builtins.property
        def additional_configuration(self) -> typing.Optional[builtins.str]:
            '''Additional Configuration that are passed to Athena Spark Calculations running in this workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-additionalconfiguration
            '''
            result = self._values.get("additional_configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bytes_scanned_cutoff_per_query(self) -> typing.Optional[jsii.Number]:
            '''The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-bytesscannedcutoffperquery
            '''
            result = self._values.get("bytes_scanned_cutoff_per_query")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def customer_content_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.CustomerContentEncryptionConfigurationProperty"]]:
            '''Indicates the KMS key for encrypting notebook content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-customercontentencryptionconfiguration
            '''
            result = self._values.get("customer_content_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.CustomerContentEncryptionConfigurationProperty"]], result)

        @builtins.property
        def enforce_work_group_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to "true", the settings for the workgroup override client-side settings.

            If set to "false", client-side settings are used

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-enforceworkgroupconfiguration
            '''
            result = self._values.get("enforce_work_group_configuration")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def engine_version(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.EngineVersionProperty"]]:
            '''The Athena engine version for running queries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-engineversion
            '''
            result = self._values.get("engine_version")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.EngineVersionProperty"]], result)

        @builtins.property
        def execution_role(self) -> typing.Optional[builtins.str]:
            '''Execution Role ARN required to run Athena Spark Calculations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-executionrole
            '''
            result = self._values.get("execution_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def publish_cloud_watch_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-publishcloudwatchmetricsenabled
            '''
            result = self._values.get("publish_cloud_watch_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def remove_bytes_scanned_cutoff_per_query(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates that the data usage control limit per query is removed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-removebytesscannedcutoffperquery
            '''
            result = self._values.get("remove_bytes_scanned_cutoff_per_query")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def remove_customer_content_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-removecustomercontentencryptionconfiguration
            '''
            result = self._values.get("remove_customer_content_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def requester_pays_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to true, allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries.

            If set to false, workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-requesterpaysenabled
            '''
            result = self._values.get("requester_pays_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def result_configuration_updates(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.ResultConfigurationUpdatesProperty"]]:
            '''The result configuration information about the queries in this workgroup that will be updated.

            Includes the updated results location and an updated option for encrypting query results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-resultconfigurationupdates
            '''
            result = self._values.get("result_configuration_updates")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkGroup.ResultConfigurationUpdatesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkGroupConfigurationUpdatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_athena.CfnWorkGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "recursive_delete_option": "recursiveDeleteOption",
        "state": "state",
        "tags": "tags",
        "work_group_configuration": "workGroupConfiguration",
        "work_group_configuration_updates": "workGroupConfigurationUpdates",
    },
)
class CfnWorkGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        recursive_delete_option: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        work_group_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.WorkGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        work_group_configuration_updates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.WorkGroupConfigurationUpdatesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkGroup``.

        :param name: The workgroup name.
        :param description: The workgroup description.
        :param recursive_delete_option: The option to delete a workgroup and its contents even if the workgroup contains any named queries. The default is false.
        :param state: The state of the workgroup: ENABLED or DISABLED.
        :param tags: The tags (key-value pairs) to associate with this resource.
        :param work_group_configuration: The configuration of the workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether Amazon CloudWatch Metrics are enabled for the workgroup, and the limit for the amount of bytes scanned (cutoff) per query, if it is specified. The ``EnforceWorkGroupConfiguration`` option determines whether workgroup settings override client-side query settings.
        :param work_group_configuration_updates: (deprecated) The configuration information that will be updated for this workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, whether the workgroup settings override the client-side settings, and the data usage limit for the amount of bytes scanned per query, if it is specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_athena as athena
            
            cfn_work_group_props = athena.CfnWorkGroupProps(
                name="name",
            
                # the properties below are optional
                description="description",
                recursive_delete_option=False,
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                work_group_configuration=athena.CfnWorkGroup.WorkGroupConfigurationProperty(
                    additional_configuration="additionalConfiguration",
                    bytes_scanned_cutoff_per_query=123,
                    customer_content_encryption_configuration=athena.CfnWorkGroup.CustomerContentEncryptionConfigurationProperty(
                        kms_key="kmsKey"
                    ),
                    enforce_work_group_configuration=False,
                    engine_version=athena.CfnWorkGroup.EngineVersionProperty(
                        effective_engine_version="effectiveEngineVersion",
                        selected_engine_version="selectedEngineVersion"
                    ),
                    execution_role="executionRole",
                    publish_cloud_watch_metrics_enabled=False,
                    requester_pays_enabled=False,
                    result_configuration=athena.CfnWorkGroup.ResultConfigurationProperty(
                        acl_configuration=athena.CfnWorkGroup.AclConfigurationProperty(
                            s3_acl_option="s3AclOption"
                        ),
                        encryption_configuration=athena.CfnWorkGroup.EncryptionConfigurationProperty(
                            encryption_option="encryptionOption",
            
                            # the properties below are optional
                            kms_key="kmsKey"
                        ),
                        expected_bucket_owner="expectedBucketOwner",
                        output_location="outputLocation"
                    )
                ),
                work_group_configuration_updates=athena.CfnWorkGroup.WorkGroupConfigurationUpdatesProperty(
                    additional_configuration="additionalConfiguration",
                    bytes_scanned_cutoff_per_query=123,
                    customer_content_encryption_configuration=athena.CfnWorkGroup.CustomerContentEncryptionConfigurationProperty(
                        kms_key="kmsKey"
                    ),
                    enforce_work_group_configuration=False,
                    engine_version=athena.CfnWorkGroup.EngineVersionProperty(
                        effective_engine_version="effectiveEngineVersion",
                        selected_engine_version="selectedEngineVersion"
                    ),
                    execution_role="executionRole",
                    publish_cloud_watch_metrics_enabled=False,
                    remove_bytes_scanned_cutoff_per_query=False,
                    remove_customer_content_encryption_configuration=False,
                    requester_pays_enabled=False,
                    result_configuration_updates=athena.CfnWorkGroup.ResultConfigurationUpdatesProperty(
                        acl_configuration=athena.CfnWorkGroup.AclConfigurationProperty(
                            s3_acl_option="s3AclOption"
                        ),
                        encryption_configuration=athena.CfnWorkGroup.EncryptionConfigurationProperty(
                            encryption_option="encryptionOption",
            
                            # the properties below are optional
                            kms_key="kmsKey"
                        ),
                        expected_bucket_owner="expectedBucketOwner",
                        output_location="outputLocation",
                        remove_acl_configuration=False,
                        remove_encryption_configuration=False,
                        remove_expected_bucket_owner=False,
                        remove_output_location=False
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a4bfef13ffe779b4b820a3b9c0da8391485059087230747da25d5f8e5c9c4c3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument recursive_delete_option", value=recursive_delete_option, expected_type=type_hints["recursive_delete_option"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument work_group_configuration", value=work_group_configuration, expected_type=type_hints["work_group_configuration"])
            check_type(argname="argument work_group_configuration_updates", value=work_group_configuration_updates, expected_type=type_hints["work_group_configuration_updates"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if recursive_delete_option is not None:
            self._values["recursive_delete_option"] = recursive_delete_option
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if work_group_configuration is not None:
            self._values["work_group_configuration"] = work_group_configuration
        if work_group_configuration_updates is not None:
            self._values["work_group_configuration_updates"] = work_group_configuration_updates

    @builtins.property
    def name(self) -> builtins.str:
        '''The workgroup name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The workgroup description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recursive_delete_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The option to delete a workgroup and its contents even if the workgroup contains any named queries.

        The default is false.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        '''
        result = self._values.get("recursive_delete_option")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the workgroup: ENABLED or DISABLED.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags (key-value pairs) to associate with this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def work_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkGroup.WorkGroupConfigurationProperty]]:
        '''The configuration of the workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether Amazon CloudWatch Metrics are enabled for the workgroup, and the limit for the amount of bytes scanned (cutoff) per query, if it is specified.

        The ``EnforceWorkGroupConfiguration`` option determines whether workgroup settings override client-side query settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        '''
        result = self._values.get("work_group_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkGroup.WorkGroupConfigurationProperty]], result)

    @builtins.property
    def work_group_configuration_updates(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkGroup.WorkGroupConfigurationUpdatesProperty]]:
        '''(deprecated) The configuration information that will be updated for this workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, whether the workgroup settings override the client-side settings, and the data usage limit for the amount of bytes scanned per query, if it is specified.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        :stability: deprecated
        '''
        result = self._values.get("work_group_configuration_updates")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkGroup.WorkGroupConfigurationUpdatesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCapacityReservation",
    "CfnCapacityReservationProps",
    "CfnDataCatalog",
    "CfnDataCatalogProps",
    "CfnNamedQuery",
    "CfnNamedQueryProps",
    "CfnPreparedStatement",
    "CfnPreparedStatementProps",
    "CfnWorkGroup",
    "CfnWorkGroupProps",
]

publication.publish()

def _typecheckingstub__7458bc9b2513dcdcbd6a0f9a6fcf8ad6ac0dd26405dc0f98526c7739ed69c27c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    target_dpus: jsii.Number,
    capacity_assignment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapacityReservation.CapacityAssignmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bcae353c3f5a5e1be964ca831d796ba8924d38d98e4da35f1f4249f28af0833(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53690919665793c02b948caf7c04a9ead8e6a42334d1d9e82cc4e52fcb473d8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e52ca03df32f93c24d4644e58482808fd84da5af0a6c8aad6cd35c472aacb8c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__673e63d688637c639118c4ff9bd95f6fb3efe1b1a0c8e2ca1005cd0aec265b52(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a48300257a027470aa2568c3011be47c3a12de78febb9a5d2cbc29c8489c9470(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCapacityReservation.CapacityAssignmentConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2d5ea5f595f96f7b9cd5f389257bb6c2960294d98f1ab6ad6a6c1ab211b6a2d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db76e33e02ec05ffa8974dcc161a2bc5a3765035346802d58d4dfe7853a80348(
    *,
    capacity_assignments: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapacityReservation.CapacityAssignmentProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e658c20843cc693ef5569c20bee6d431a496b10c7009acb64986e6a31ca21df2(
    *,
    workgroup_names: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a214961375f078f4b3bde83f338ac59ad879fce3adfb57a29b21cf15190a97f8(
    *,
    name: builtins.str,
    target_dpus: jsii.Number,
    capacity_assignment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapacityReservation.CapacityAssignmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05023d61a95576869568bc095d9889b971a9d8c061cba5833a71f44231f3b9e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70484df33f57719ba2197f7ae86dd846651ec89bd9dc9853fbc4fff3bb342b5e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53b184d971619ad9ceb2925488e914f96ae85a3537cc1bbc7fcec083c3c925b5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1608b3146e652acde24c1f4fa9b482be4691d7f18e63abae7294e6d2be79cd57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648f5f258b71a886cda692ac680360ffcaf9aa72e0b747dc0986bc6a3da0b9c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da91751e350be071e1bcad20db12b8878ad53b907a7422a55f53fa3951e8f509(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7bec0cee9cc93380a50923dfa0015a801db986ded37e98f7318cd85af887ed(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__732720a85a91adafa344b33afc56917f285d76d3c81b8851c7f46aee8ac4b31f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2151d2fd30be9f56cebbd5adb97d92e074856a6590b6970f5a1cb707de68d79(
    *,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a6acd727802c2fa7a22438ae44b6660590077a4f16a3e6add10721d6e8db0a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    database: builtins.str,
    query_string: builtins.str,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    work_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddec5e38097efea59697e1d796fb6a6d88b7ddece86ca310e4558dddfdb308b6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf59ed9b65b480c5d847ba252258084274a9caf2a33c0d357ec8831f81ecba20(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501cd8c10c3d115e2f7cac0d6afe0b38bf2af9f4c2baa50fa99e8e7ba4327165(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c663852da3bf6abca104187294becf5134a8fc1a2d9f25c6701872f41fde8ba9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a745e34dd545f8dc388bc187b5819d2ef704db543656d96e0b9de86430379e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bff191aa3a040eb433f325a55450844fa2a74753c5b7cc84413e2cda83bd7d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb682c36871b1c9d1ea3cca54fdda6bd4c9a2175d91b4bcc2aff8385207d037(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6843e60f95befbeeac102b484bbd44b76e442a562d520fa09f15e78c6028b865(
    *,
    database: builtins.str,
    query_string: builtins.str,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    work_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c4c8a39ce9fb61cd606b4abe521c05c0c7c27caa382a68b361cf3be632c8c83(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    query_statement: builtins.str,
    statement_name: builtins.str,
    work_group: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a69017370b966513d7ca221de45e0ee04038dba0f3e2b7a738436d078d1c48c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0b1adefc3ae78288ead2138671ccc59867e63261ac6fa2f2ea32a85d1c2805f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18c5e047fd7a10b962ddfc814e209cbca4ff1a422c2293eb18b16d83af0711a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dda65d001efb04fb60a14b983d53ba4365b21f672e62245cf7f61199a432872(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99d939bc99487519bb0415ef8ada649107f8686d2077741c486620ecf3af8996(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f39b664043d33c495a721144bc0de55a433122a4024bcbb066c229ec4cf1fe8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709f141308344c291dfca2deddc79eabfe04118b21e11aa37c781298b5454317(
    *,
    query_statement: builtins.str,
    statement_name: builtins.str,
    work_group: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be0f7d9e26f77f516ae56dabfd6aae7d4d7e7404767cea86eb51dbe5a20e9fc9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    recursive_delete_option: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    work_group_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.WorkGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    work_group_configuration_updates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.WorkGroupConfigurationUpdatesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a89351b058fb473aa673ca436e54b399faeed90f862768d495efb059a3875b1c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f1e5526c989991241a139bb91d1d3a69c3857127a6488cbc9d7a52f30e64b6e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a0aa36fc7c960f3a6b523e94a0875ba081b0757724ca672dc4d58a5da328d86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c3416008ff859aa8fd00dc773e06bb93607be2c43f4d8dc1962b2bbcf013c1d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a00e8480ec3a751e59ec61ecdf367b39021a964ca18fdc42e47cc0ae3bf52b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca675b7d3278faf35ffe34635716d8704c5407a6628b6ede3bd1119276aef0b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6dca743e6f0d274bbeac5f19381d936c9a4ea24a2a2ebe3fbd3e468b43fc16f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffe180d9d0a40f65f5055211f5690cad94d8268dbb88d2644e371d7e17725ac6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkGroup.WorkGroupConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a488c1ed1dfb72d7cde64a1f15e1f03602827583e7998463eb0cbad4597ab95a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkGroup.WorkGroupConfigurationUpdatesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d08c097512b882cb470dc37bf746c41eaf32d76443ec31f122bf7863c4eb842(
    *,
    s3_acl_option: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3480ab9bdaef6bae695825b3df3eae10d42fc973ee85c1e9d372a5012990c61(
    *,
    kms_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa79fae7a2ac9eacbed710d8ee5a01ad03c3b9f537094d9f71d622a0bac4b6d7(
    *,
    encryption_option: builtins.str,
    kms_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f0b78a82f24ece8384b490252230129c42a711fdb038b4ecd645d321ca82e1(
    *,
    effective_engine_version: typing.Optional[builtins.str] = None,
    selected_engine_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86d94b0afb15160d6ec72666a7574c95b2d16afd21c5ca80a9f352f319f2f46c(
    *,
    acl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.AclConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    output_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfde88e9cbba4fc81da00b04c8cc63d678d91113cf67503da9a7475c7688b0c5(
    *,
    acl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.AclConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    output_location: typing.Optional[builtins.str] = None,
    remove_acl_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    remove_encryption_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    remove_expected_bucket_owner: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    remove_output_location: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc58a8f7fc071c8f6e3cf6044079ec303e9ba8521ef96ca98c62cfdd175a6a8(
    *,
    additional_configuration: typing.Optional[builtins.str] = None,
    bytes_scanned_cutoff_per_query: typing.Optional[jsii.Number] = None,
    customer_content_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.CustomerContentEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enforce_work_group_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    engine_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.EngineVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    execution_role: typing.Optional[builtins.str] = None,
    publish_cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    requester_pays_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.ResultConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d600654f5aa48cb49fd4baf2a677e5f7725dcfa1249836427c1d9f65a0904de(
    *,
    additional_configuration: typing.Optional[builtins.str] = None,
    bytes_scanned_cutoff_per_query: typing.Optional[jsii.Number] = None,
    customer_content_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.CustomerContentEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enforce_work_group_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    engine_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.EngineVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    execution_role: typing.Optional[builtins.str] = None,
    publish_cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    remove_bytes_scanned_cutoff_per_query: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    remove_customer_content_encryption_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    requester_pays_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    result_configuration_updates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.ResultConfigurationUpdatesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a4bfef13ffe779b4b820a3b9c0da8391485059087230747da25d5f8e5c9c4c3(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    recursive_delete_option: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    work_group_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.WorkGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    work_group_configuration_updates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkGroup.WorkGroupConfigurationUpdatesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
