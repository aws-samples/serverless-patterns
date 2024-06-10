'''
# AWS::Deadline Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_deadline as deadline
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Deadline construct libraries](https://constructs.dev/search?q=deadline)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Deadline resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Deadline.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Deadline](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Deadline.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnFarm(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_deadline.CfnFarm",
):
    '''Creates a farm to allow space for queues and fleets.

    Farms are the space where the components of your renders gather and are pieced together in the cloud. Farms contain budgets and allow you to enforce permissions. Deadline Cloud farms are a useful container for large projects.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-farm.html
    :cloudformationResource: AWS::Deadline::Farm
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_deadline as deadline
        
        cfn_farm = deadline.CfnFarm(self, "MyCfnFarm",
            display_name="displayName",
        
            # the properties below are optional
            description="description",
            kms_key_arn="kmsKeyArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param display_name: The display name of the farm.
        :param description: A description of the farm that helps identify what the farm is used for. Default: - ""
        :param kms_key_arn: The ARN for the KMS key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8cfafb7690986cd3ddb4ba2de814f300f2faab0827e01a86f2f528af27544d1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFarmProps(
            display_name=display_name, description=description, kms_key_arn=kms_key_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6b1d970d70d840fd22a69886b9553ac48f2e83d63e421ea979261b3bddf1d0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__46eb3e8dead939804597fc70dfb9f5b385b7dfeedc4caf4b49813000440c7a7e)
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
        '''The Amazon Resource Name (ARN) assigned to the farm.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFarmId")
    def attr_farm_id(self) -> builtins.str:
        '''The farm ID.

        :cloudformationAttribute: FarmId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFarmId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The display name of the farm.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e3487107fca3fbd8f0f2e3e65063da63a41a523cd6d5ffd0aef63e8ec4c680c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the farm that helps identify what the farm is used for.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225609e046f467aa1cff6857451a01a60bf944d05094eaea191c40155a7b5ee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the KMS key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd09d08fc701cc061b023ad6a5d72db4516ff09e295b470365e390436475464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_deadline.CfnFarmProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "description": "description",
        "kms_key_arn": "kmsKeyArn",
    },
)
class CfnFarmProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFarm``.

        :param display_name: The display name of the farm.
        :param description: A description of the farm that helps identify what the farm is used for. Default: - ""
        :param kms_key_arn: The ARN for the KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-farm.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_deadline as deadline
            
            cfn_farm_props = deadline.CfnFarmProps(
                display_name="displayName",
            
                # the properties below are optional
                description="description",
                kms_key_arn="kmsKeyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85eb8ab8e233d51550c535a34f621e657ea5dfc47e9b977b5a9b73c3be4b9b4f)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The display name of the farm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-farm.html#cfn-deadline-farm-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the farm that helps identify what the farm is used for.

        :default: - ""

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-farm.html#cfn-deadline-farm-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-farm.html#cfn-deadline-farm-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_deadline.CfnFleet",
):
    '''Creates a fleet.

    Fleets gather information relating to compute, or capacity, for renders within your farms. You can choose to manage your own capacity or opt to have fleets fully managed by Deadline Cloud.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html
    :cloudformationResource: AWS::Deadline::Fleet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_deadline as deadline
        
        cfn_fleet = deadline.CfnFleet(self, "MyCfnFleet",
            configuration=deadline.CfnFleet.FleetConfigurationProperty(
                customer_managed=deadline.CfnFleet.CustomerManagedFleetConfigurationProperty(
                    mode="mode",
                    worker_capabilities=deadline.CfnFleet.CustomerManagedWorkerCapabilitiesProperty(
                        cpu_architecture_type="cpuArchitectureType",
                        memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                            min=123,
        
                            # the properties below are optional
                            max=123
                        ),
                        os_family="osFamily",
                        v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                            min=123,
        
                            # the properties below are optional
                            max=123
                        ),
        
                        # the properties below are optional
                        accelerator_count=deadline.CfnFleet.AcceleratorCountRangeProperty(
                            min=123,
        
                            # the properties below are optional
                            max=123
                        ),
                        accelerator_total_memory_mi_b=deadline.CfnFleet.AcceleratorTotalMemoryMiBRangeProperty(
                            min=123,
        
                            # the properties below are optional
                            max=123
                        ),
                        accelerator_types=["acceleratorTypes"],
                        custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                            min=123,
                            name="name",
        
                            # the properties below are optional
                            max=123
                        )],
                        custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                            name="name",
                            values=["values"]
                        )]
                    ),
        
                    # the properties below are optional
                    storage_profile_id="storageProfileId"
                ),
                service_managed_ec2=deadline.CfnFleet.ServiceManagedEc2FleetConfigurationProperty(
                    instance_capabilities=deadline.CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty(
                        cpu_architecture_type="cpuArchitectureType",
                        memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                            min=123,
        
                            # the properties below are optional
                            max=123
                        ),
                        os_family="osFamily",
                        v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                            min=123,
        
                            # the properties below are optional
                            max=123
                        ),
        
                        # the properties below are optional
                        allowed_instance_types=["allowedInstanceTypes"],
                        custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                            min=123,
                            name="name",
        
                            # the properties below are optional
                            max=123
                        )],
                        custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                            name="name",
                            values=["values"]
                        )],
                        excluded_instance_types=["excludedInstanceTypes"],
                        root_ebs_volume=deadline.CfnFleet.Ec2EbsVolumeProperty(
                            iops=123,
                            size_gi_b=123,
                            throughput_mi_b=123
                        )
                    ),
                    instance_market_options=deadline.CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty(
                        type="type"
                    )
                )
            ),
            display_name="displayName",
            max_worker_count=123,
            role_arn="roleArn",
        
            # the properties below are optional
            description="description",
            farm_id="farmId",
            min_worker_count=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.FleetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        display_name: builtins.str,
        max_worker_count: jsii.Number,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        farm_id: typing.Optional[builtins.str] = None,
        min_worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: The configuration details for the fleet.
        :param display_name: The display name of the fleet summary to update.
        :param max_worker_count: The maximum number of workers specified in the fleet.
        :param role_arn: The IAM role that workers in the fleet use when processing jobs.
        :param description: A description that helps identify what the fleet is used for. Default: - ""
        :param farm_id: The farm ID.
        :param min_worker_count: The minimum number of workers in the fleet. Default: - 0
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b982dfa2ac88548efd13c63c65f7144bf79a74dd670eebe5a13537f1fa38090a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFleetProps(
            configuration=configuration,
            display_name=display_name,
            max_worker_count=max_worker_count,
            role_arn=role_arn,
            description=description,
            farm_id=farm_id,
            min_worker_count=min_worker_count,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c7467a1be46332c11edfbc2f2073b67842b79e2b6dc68d7fa0312c8a5b8c595)
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
            type_hints = typing.get_type_hints(_typecheckingstub__624f83add0edac45b93d9318e64f5196dd2045c50f094e69787beb05aa8c11d7)
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
        '''The Amazon Resource Name (ARN) assigned to the fleet.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCapabilities")
    def attr_capabilities(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Capabilities
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrCapabilities"))

    @builtins.property
    @jsii.member(jsii_name="attrFleetId")
    def attr_fleet_id(self) -> builtins.str:
        '''The fleet ID.

        :cloudformationAttribute: FleetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFleetId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the fleet.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkerCount")
    def attr_worker_count(self) -> jsii.Number:
        '''The number of workers in the fleet summary.

        :cloudformationAttribute: WorkerCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrWorkerCount"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetConfigurationProperty"]:
        '''The configuration details for the fleet.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e2fe844317b39494e7f7a1851d6e5842bc0627b2cc937a6709042cb43a27a3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The display name of the fleet summary to update.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d501705678e5cc3f1a305c922a22f7ba207d560bdb5761b3ce0e042852101fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="maxWorkerCount")
    def max_worker_count(self) -> jsii.Number:
        '''The maximum number of workers specified in the fleet.'''
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkerCount"))

    @max_worker_count.setter
    def max_worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__435144cf5095e3c8ecf5073fcb2ee802817fde90c7c30f2fa7b579407c82a89a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkerCount", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The IAM role that workers in the fleet use when processing jobs.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__471ed3a4e000dd618e2be0578e42aa2e8288223309b77395023cba44dff3a738)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description that helps identify what the fleet is used for.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__084da5a242d843b332de24a8c53af7e8830cd00d0dca22235f0c3d665732570b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="farmId")
    def farm_id(self) -> typing.Optional[builtins.str]:
        '''The farm ID.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "farmId"))

    @farm_id.setter
    def farm_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30ce1167517d9e9a39c50fdbd55b565e28d3f5dca61d4b795926951043d1cc2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "farmId", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkerCount")
    def min_worker_count(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of workers in the fleet.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkerCount"))

    @min_worker_count.setter
    def min_worker_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e98aa63695c4cd93c0aae20c0cd7e90226c1100540a8732e0be19b9d6cc5e094)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkerCount", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.AcceleratorCountRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"min": "min", "max": "max"},
    )
    class AcceleratorCountRangeProperty:
        def __init__(
            self,
            *,
            min: jsii.Number,
            max: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The range for the GPU fleet acceleration.

            :param min: The minimum GPU for the accelerator.
            :param max: The maximum GPU for the accelerator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratorcountrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                accelerator_count_range_property = deadline.CfnFleet.AcceleratorCountRangeProperty(
                    min=123,
                
                    # the properties below are optional
                    max=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f4d7e76219e8cce8e44e215b08cd1fef54b62ca3d48dbbc0bc8b3e6040db253e)
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "min": min,
            }
            if max is not None:
                self._values["max"] = max

        @builtins.property
        def min(self) -> jsii.Number:
            '''The minimum GPU for the accelerator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratorcountrange.html#cfn-deadline-fleet-acceleratorcountrange-min
            '''
            result = self._values.get("min")
            assert result is not None, "Required property 'min' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''The maximum GPU for the accelerator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratorcountrange.html#cfn-deadline-fleet-acceleratorcountrange-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AcceleratorCountRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.AcceleratorTotalMemoryMiBRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"min": "min", "max": "max"},
    )
    class AcceleratorTotalMemoryMiBRangeProperty:
        def __init__(
            self,
            *,
            min: jsii.Number,
            max: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The range for memory, in MiB, to use for the accelerator.

            :param min: The minimum amount of memory to use for the accelerator, measured in MiB.
            :param max: The maximum amount of memory to use for the accelerator, measured in MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratortotalmemorymibrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                accelerator_total_memory_mi_bRange_property = deadline.CfnFleet.AcceleratorTotalMemoryMiBRangeProperty(
                    min=123,
                
                    # the properties below are optional
                    max=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e87ae0b2cf7001539dfe803c414d6da11bd37d8db4fe33e1b4847d22cccfd0e)
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "min": min,
            }
            if max is not None:
                self._values["max"] = max

        @builtins.property
        def min(self) -> jsii.Number:
            '''The minimum amount of memory to use for the accelerator, measured in MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratortotalmemorymibrange.html#cfn-deadline-fleet-acceleratortotalmemorymibrange-min
            '''
            result = self._values.get("min")
            assert result is not None, "Required property 'min' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of memory to use for the accelerator, measured in MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratortotalmemorymibrange.html#cfn-deadline-fleet-acceleratortotalmemorymibrange-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AcceleratorTotalMemoryMiBRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.CustomerManagedFleetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mode": "mode",
            "worker_capabilities": "workerCapabilities",
            "storage_profile_id": "storageProfileId",
        },
    )
    class CustomerManagedFleetConfigurationProperty:
        def __init__(
            self,
            *,
            mode: builtins.str,
            worker_capabilities: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.CustomerManagedWorkerCapabilitiesProperty", typing.Dict[builtins.str, typing.Any]]],
            storage_profile_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of a customer managed fleet configuration.

            :param mode: The AWS Auto Scaling mode for the customer managed fleet configuration.
            :param worker_capabilities: The worker capabilities for a customer managed fleet configuration.
            :param storage_profile_id: The storage profile ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedfleetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                customer_managed_fleet_configuration_property = deadline.CfnFleet.CustomerManagedFleetConfigurationProperty(
                    mode="mode",
                    worker_capabilities=deadline.CfnFleet.CustomerManagedWorkerCapabilitiesProperty(
                        cpu_architecture_type="cpuArchitectureType",
                        memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                            min=123,
                
                            # the properties below are optional
                            max=123
                        ),
                        os_family="osFamily",
                        v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                            min=123,
                
                            # the properties below are optional
                            max=123
                        ),
                
                        # the properties below are optional
                        accelerator_count=deadline.CfnFleet.AcceleratorCountRangeProperty(
                            min=123,
                
                            # the properties below are optional
                            max=123
                        ),
                        accelerator_total_memory_mi_b=deadline.CfnFleet.AcceleratorTotalMemoryMiBRangeProperty(
                            min=123,
                
                            # the properties below are optional
                            max=123
                        ),
                        accelerator_types=["acceleratorTypes"],
                        custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                            min=123,
                            name="name",
                
                            # the properties below are optional
                            max=123
                        )],
                        custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                            name="name",
                            values=["values"]
                        )]
                    ),
                
                    # the properties below are optional
                    storage_profile_id="storageProfileId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1e0d0744c60a31b3157ef03f930266f6c000eafa44c6050607897ea5b3e3881d)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument worker_capabilities", value=worker_capabilities, expected_type=type_hints["worker_capabilities"])
                check_type(argname="argument storage_profile_id", value=storage_profile_id, expected_type=type_hints["storage_profile_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
                "worker_capabilities": worker_capabilities,
            }
            if storage_profile_id is not None:
                self._values["storage_profile_id"] = storage_profile_id

        @builtins.property
        def mode(self) -> builtins.str:
            '''The AWS Auto Scaling mode for the customer managed fleet configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedfleetconfiguration.html#cfn-deadline-fleet-customermanagedfleetconfiguration-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def worker_capabilities(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.CustomerManagedWorkerCapabilitiesProperty"]:
            '''The worker capabilities for a customer managed fleet configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedfleetconfiguration.html#cfn-deadline-fleet-customermanagedfleetconfiguration-workercapabilities
            '''
            result = self._values.get("worker_capabilities")
            assert result is not None, "Required property 'worker_capabilities' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.CustomerManagedWorkerCapabilitiesProperty"], result)

        @builtins.property
        def storage_profile_id(self) -> typing.Optional[builtins.str]:
            '''The storage profile ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedfleetconfiguration.html#cfn-deadline-fleet-customermanagedfleetconfiguration-storageprofileid
            '''
            result = self._values.get("storage_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedFleetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.CustomerManagedWorkerCapabilitiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu_architecture_type": "cpuArchitectureType",
            "memory_mib": "memoryMiB",
            "os_family": "osFamily",
            "v_cpu_count": "vCpuCount",
            "accelerator_count": "acceleratorCount",
            "accelerator_total_memory_mib": "acceleratorTotalMemoryMiB",
            "accelerator_types": "acceleratorTypes",
            "custom_amounts": "customAmounts",
            "custom_attributes": "customAttributes",
        },
    )
    class CustomerManagedWorkerCapabilitiesProperty:
        def __init__(
            self,
            *,
            cpu_architecture_type: builtins.str,
            memory_mib: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.MemoryMiBRangeProperty", typing.Dict[builtins.str, typing.Any]]],
            os_family: builtins.str,
            v_cpu_count: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.VCpuCountRangeProperty", typing.Dict[builtins.str, typing.Any]]],
            accelerator_count: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.AcceleratorCountRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            accelerator_total_memory_mib: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.AcceleratorTotalMemoryMiBRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            custom_amounts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.FleetAmountCapabilityProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            custom_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.FleetAttributeCapabilityProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The worker capabilities for a customer managed workflow.

            :param cpu_architecture_type: The CPU architecture type for the customer managed worker capabilities.
            :param memory_mib: The memory (MiB).
            :param os_family: The operating system (OS) family.
            :param v_cpu_count: The vCPU count for the customer manged worker capabilities.
            :param accelerator_count: The range of the accelerator.
            :param accelerator_total_memory_mib: The total memory (MiB) for the customer managed worker capabilities.
            :param accelerator_types: The accelerator types for the customer managed worker capabilities.
            :param custom_amounts: Custom requirement ranges for customer managed worker capabilities.
            :param custom_attributes: Custom attributes for the customer manged worker capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                customer_managed_worker_capabilities_property = deadline.CfnFleet.CustomerManagedWorkerCapabilitiesProperty(
                    cpu_architecture_type="cpuArchitectureType",
                    memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                        min=123,
                
                        # the properties below are optional
                        max=123
                    ),
                    os_family="osFamily",
                    v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                        min=123,
                
                        # the properties below are optional
                        max=123
                    ),
                
                    # the properties below are optional
                    accelerator_count=deadline.CfnFleet.AcceleratorCountRangeProperty(
                        min=123,
                
                        # the properties below are optional
                        max=123
                    ),
                    accelerator_total_memory_mi_b=deadline.CfnFleet.AcceleratorTotalMemoryMiBRangeProperty(
                        min=123,
                
                        # the properties below are optional
                        max=123
                    ),
                    accelerator_types=["acceleratorTypes"],
                    custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                        min=123,
                        name="name",
                
                        # the properties below are optional
                        max=123
                    )],
                    custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                        name="name",
                        values=["values"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bbfd53a4095156c6675556d0bc3d17d02d807749147c8ab86039c9614cf19652)
                check_type(argname="argument cpu_architecture_type", value=cpu_architecture_type, expected_type=type_hints["cpu_architecture_type"])
                check_type(argname="argument memory_mib", value=memory_mib, expected_type=type_hints["memory_mib"])
                check_type(argname="argument os_family", value=os_family, expected_type=type_hints["os_family"])
                check_type(argname="argument v_cpu_count", value=v_cpu_count, expected_type=type_hints["v_cpu_count"])
                check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
                check_type(argname="argument accelerator_total_memory_mib", value=accelerator_total_memory_mib, expected_type=type_hints["accelerator_total_memory_mib"])
                check_type(argname="argument accelerator_types", value=accelerator_types, expected_type=type_hints["accelerator_types"])
                check_type(argname="argument custom_amounts", value=custom_amounts, expected_type=type_hints["custom_amounts"])
                check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cpu_architecture_type": cpu_architecture_type,
                "memory_mib": memory_mib,
                "os_family": os_family,
                "v_cpu_count": v_cpu_count,
            }
            if accelerator_count is not None:
                self._values["accelerator_count"] = accelerator_count
            if accelerator_total_memory_mib is not None:
                self._values["accelerator_total_memory_mib"] = accelerator_total_memory_mib
            if accelerator_types is not None:
                self._values["accelerator_types"] = accelerator_types
            if custom_amounts is not None:
                self._values["custom_amounts"] = custom_amounts
            if custom_attributes is not None:
                self._values["custom_attributes"] = custom_attributes

        @builtins.property
        def cpu_architecture_type(self) -> builtins.str:
            '''The CPU architecture type for the customer managed worker capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-cpuarchitecturetype
            '''
            result = self._values.get("cpu_architecture_type")
            assert result is not None, "Required property 'cpu_architecture_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def memory_mib(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.MemoryMiBRangeProperty"]:
            '''The memory (MiB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-memorymib
            '''
            result = self._values.get("memory_mib")
            assert result is not None, "Required property 'memory_mib' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.MemoryMiBRangeProperty"], result)

        @builtins.property
        def os_family(self) -> builtins.str:
            '''The operating system (OS) family.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-osfamily
            '''
            result = self._values.get("os_family")
            assert result is not None, "Required property 'os_family' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def v_cpu_count(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.VCpuCountRangeProperty"]:
            '''The vCPU count for the customer manged worker capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-vcpucount
            '''
            result = self._values.get("v_cpu_count")
            assert result is not None, "Required property 'v_cpu_count' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.VCpuCountRangeProperty"], result)

        @builtins.property
        def accelerator_count(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AcceleratorCountRangeProperty"]]:
            '''The range of the accelerator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratorcount
            '''
            result = self._values.get("accelerator_count")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AcceleratorCountRangeProperty"]], result)

        @builtins.property
        def accelerator_total_memory_mib(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AcceleratorTotalMemoryMiBRangeProperty"]]:
            '''The total memory (MiB) for the customer managed worker capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratortotalmemorymib
            '''
            result = self._values.get("accelerator_total_memory_mib")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AcceleratorTotalMemoryMiBRangeProperty"]], result)

        @builtins.property
        def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The accelerator types for the customer managed worker capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratortypes
            '''
            result = self._values.get("accelerator_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def custom_amounts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAmountCapabilityProperty"]]]]:
            '''Custom requirement ranges for customer managed worker capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-customamounts
            '''
            result = self._values.get("custom_amounts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAmountCapabilityProperty"]]]], result)

        @builtins.property
        def custom_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAttributeCapabilityProperty"]]]]:
            '''Custom attributes for the customer manged worker capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html#cfn-deadline-fleet-customermanagedworkercapabilities-customattributes
            '''
            result = self._values.get("custom_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAttributeCapabilityProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedWorkerCapabilitiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.Ec2EbsVolumeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iops": "iops",
            "size_gib": "sizeGiB",
            "throughput_mib": "throughputMiB",
        },
    )
    class Ec2EbsVolumeProperty:
        def __init__(
            self,
            *,
            iops: typing.Optional[jsii.Number] = None,
            size_gib: typing.Optional[jsii.Number] = None,
            throughput_mib: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the EBS volume.

            :param iops: The IOPS per volume. Default: - 3000
            :param size_gib: The EBS volume size in GiB. Default: - 250
            :param throughput_mib: The throughput per volume in MiB. Default: - 125

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-ec2ebsvolume.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                ec2_ebs_volume_property = deadline.CfnFleet.Ec2EbsVolumeProperty(
                    iops=123,
                    size_gi_b=123,
                    throughput_mi_b=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6b6ee298f17f76c41b442fe1d743f9b23991d0b29f18a1db1e7c2c2c5cd63be)
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument size_gib", value=size_gib, expected_type=type_hints["size_gib"])
                check_type(argname="argument throughput_mib", value=throughput_mib, expected_type=type_hints["throughput_mib"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iops is not None:
                self._values["iops"] = iops
            if size_gib is not None:
                self._values["size_gib"] = size_gib
            if throughput_mib is not None:
                self._values["throughput_mib"] = throughput_mib

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The IOPS per volume.

            :default: - 3000

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-ec2ebsvolume.html#cfn-deadline-fleet-ec2ebsvolume-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_gib(self) -> typing.Optional[jsii.Number]:
            '''The EBS volume size in GiB.

            :default: - 250

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-ec2ebsvolume.html#cfn-deadline-fleet-ec2ebsvolume-sizegib
            '''
            result = self._values.get("size_gib")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throughput_mib(self) -> typing.Optional[jsii.Number]:
            '''The throughput per volume in MiB.

            :default: - 125

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-ec2ebsvolume.html#cfn-deadline-fleet-ec2ebsvolume-throughputmib
            '''
            result = self._values.get("throughput_mib")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ec2EbsVolumeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.FleetAmountCapabilityProperty",
        jsii_struct_bases=[],
        name_mapping={"min": "min", "name": "name", "max": "max"},
    )
    class FleetAmountCapabilityProperty:
        def __init__(
            self,
            *,
            min: jsii.Number,
            name: builtins.str,
            max: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The fleet amount and attribute capabilities.

            :param min: The minimum amount of fleet worker capability.
            :param name: The name of the fleet capability.
            :param max: The maximum amount of the fleet worker capability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetamountcapability.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                fleet_amount_capability_property = deadline.CfnFleet.FleetAmountCapabilityProperty(
                    min=123,
                    name="name",
                
                    # the properties below are optional
                    max=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0e16e93d244596337be30bf6e8c34bdd5a05f8101356c781ea0ee01c9288890)
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "min": min,
                "name": name,
            }
            if max is not None:
                self._values["max"] = max

        @builtins.property
        def min(self) -> jsii.Number:
            '''The minimum amount of fleet worker capability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetamountcapability.html#cfn-deadline-fleet-fleetamountcapability-min
            '''
            result = self._values.get("min")
            assert result is not None, "Required property 'min' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the fleet capability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetamountcapability.html#cfn-deadline-fleet-fleetamountcapability-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of the fleet worker capability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetamountcapability.html#cfn-deadline-fleet-fleetamountcapability-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FleetAmountCapabilityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.FleetAttributeCapabilityProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class FleetAttributeCapabilityProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''Defines the fleet's capability name, minimum, and maximum.

            :param name: The name of the fleet attribute capability for the worker.
            :param values: The number of fleet attribute capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetattributecapability.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                fleet_attribute_capability_property = deadline.CfnFleet.FleetAttributeCapabilityProperty(
                    name="name",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3aecc2f9273876f0a639b5d6f1630dcfd8aca136d3caeaeb82918997f059f3e4)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the fleet attribute capability for the worker.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetattributecapability.html#cfn-deadline-fleet-fleetattributecapability-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The number of fleet attribute capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetattributecapability.html#cfn-deadline-fleet-fleetattributecapability-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FleetAttributeCapabilityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.FleetCapabilitiesProperty",
        jsii_struct_bases=[],
        name_mapping={"amounts": "amounts", "attributes": "attributes"},
    )
    class FleetCapabilitiesProperty:
        def __init__(
            self,
            *,
            amounts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.FleetAmountCapabilityProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.FleetAttributeCapabilityProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The amounts and attributes of fleets.

            :param amounts: Amount capabilities of the fleet.
            :param attributes: Attribute capabilities of the fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetcapabilities.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                fleet_capabilities_property = deadline.CfnFleet.FleetCapabilitiesProperty(
                    amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                        min=123,
                        name="name",
                
                        # the properties below are optional
                        max=123
                    )],
                    attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                        name="name",
                        values=["values"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__740fdb4badd1a242b2d3b374ef6944877551e5f0eb2de2239a830f3c2028b7b1)
                check_type(argname="argument amounts", value=amounts, expected_type=type_hints["amounts"])
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amounts is not None:
                self._values["amounts"] = amounts
            if attributes is not None:
                self._values["attributes"] = attributes

        @builtins.property
        def amounts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAmountCapabilityProperty"]]]]:
            '''Amount capabilities of the fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetcapabilities.html#cfn-deadline-fleet-fleetcapabilities-amounts
            '''
            result = self._values.get("amounts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAmountCapabilityProperty"]]]], result)

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAttributeCapabilityProperty"]]]]:
            '''Attribute capabilities of the fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetcapabilities.html#cfn-deadline-fleet-fleetcapabilities-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAttributeCapabilityProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FleetCapabilitiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.FleetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_managed": "customerManaged",
            "service_managed_ec2": "serviceManagedEc2",
        },
    )
    class FleetConfigurationProperty:
        def __init__(
            self,
            *,
            customer_managed: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.CustomerManagedFleetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_managed_ec2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ServiceManagedEc2FleetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Fleet configuration details.

            :param customer_managed: The customer managed fleets within a fleet configuration.
            :param service_managed_ec2: The service managed Amazon EC2 instances for a fleet configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                fleet_configuration_property = deadline.CfnFleet.FleetConfigurationProperty(
                    customer_managed=deadline.CfnFleet.CustomerManagedFleetConfigurationProperty(
                        mode="mode",
                        worker_capabilities=deadline.CfnFleet.CustomerManagedWorkerCapabilitiesProperty(
                            cpu_architecture_type="cpuArchitectureType",
                            memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                                min=123,
                
                                # the properties below are optional
                                max=123
                            ),
                            os_family="osFamily",
                            v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                                min=123,
                
                                # the properties below are optional
                                max=123
                            ),
                
                            # the properties below are optional
                            accelerator_count=deadline.CfnFleet.AcceleratorCountRangeProperty(
                                min=123,
                
                                # the properties below are optional
                                max=123
                            ),
                            accelerator_total_memory_mi_b=deadline.CfnFleet.AcceleratorTotalMemoryMiBRangeProperty(
                                min=123,
                
                                # the properties below are optional
                                max=123
                            ),
                            accelerator_types=["acceleratorTypes"],
                            custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                                min=123,
                                name="name",
                
                                # the properties below are optional
                                max=123
                            )],
                            custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                                name="name",
                                values=["values"]
                            )]
                        ),
                
                        # the properties below are optional
                        storage_profile_id="storageProfileId"
                    ),
                    service_managed_ec2=deadline.CfnFleet.ServiceManagedEc2FleetConfigurationProperty(
                        instance_capabilities=deadline.CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty(
                            cpu_architecture_type="cpuArchitectureType",
                            memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                                min=123,
                
                                # the properties below are optional
                                max=123
                            ),
                            os_family="osFamily",
                            v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                                min=123,
                
                                # the properties below are optional
                                max=123
                            ),
                
                            # the properties below are optional
                            allowed_instance_types=["allowedInstanceTypes"],
                            custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                                min=123,
                                name="name",
                
                                # the properties below are optional
                                max=123
                            )],
                            custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                                name="name",
                                values=["values"]
                            )],
                            excluded_instance_types=["excludedInstanceTypes"],
                            root_ebs_volume=deadline.CfnFleet.Ec2EbsVolumeProperty(
                                iops=123,
                                size_gi_b=123,
                                throughput_mi_b=123
                            )
                        ),
                        instance_market_options=deadline.CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty(
                            type="type"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ef3ed1850d4005d38d3a6c912a28b59698026461815dad08ff096a4c327a89c)
                check_type(argname="argument customer_managed", value=customer_managed, expected_type=type_hints["customer_managed"])
                check_type(argname="argument service_managed_ec2", value=service_managed_ec2, expected_type=type_hints["service_managed_ec2"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_managed is not None:
                self._values["customer_managed"] = customer_managed
            if service_managed_ec2 is not None:
                self._values["service_managed_ec2"] = service_managed_ec2

        @builtins.property
        def customer_managed(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.CustomerManagedFleetConfigurationProperty"]]:
            '''The customer managed fleets within a fleet configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetconfiguration.html#cfn-deadline-fleet-fleetconfiguration-customermanaged
            '''
            result = self._values.get("customer_managed")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.CustomerManagedFleetConfigurationProperty"]], result)

        @builtins.property
        def service_managed_ec2(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ServiceManagedEc2FleetConfigurationProperty"]]:
            '''The service managed Amazon EC2 instances for a fleet configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetconfiguration.html#cfn-deadline-fleet-fleetconfiguration-servicemanagedec2
            '''
            result = self._values.get("service_managed_ec2")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ServiceManagedEc2FleetConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FleetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.MemoryMiBRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"min": "min", "max": "max"},
    )
    class MemoryMiBRangeProperty:
        def __init__(
            self,
            *,
            min: jsii.Number,
            max: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The range of memory in MiB.

            :param min: The minimum amount of memory (in MiB).
            :param max: The maximum amount of memory (in MiB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-memorymibrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                memory_mi_bRange_property = deadline.CfnFleet.MemoryMiBRangeProperty(
                    min=123,
                
                    # the properties below are optional
                    max=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0c49c5364d9d5abab3267eb2a6afca69f203020da3e42493624297dd2a5bf0f)
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "min": min,
            }
            if max is not None:
                self._values["max"] = max

        @builtins.property
        def min(self) -> jsii.Number:
            '''The minimum amount of memory (in MiB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-memorymibrange.html#cfn-deadline-fleet-memorymibrange-min
            '''
            result = self._values.get("min")
            assert result is not None, "Required property 'min' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of memory (in MiB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-memorymibrange.html#cfn-deadline-fleet-memorymibrange-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemoryMiBRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.ServiceManagedEc2FleetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_capabilities": "instanceCapabilities",
            "instance_market_options": "instanceMarketOptions",
        },
    )
    class ServiceManagedEc2FleetConfigurationProperty:
        def __init__(
            self,
            *,
            instance_capabilities: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty", typing.Dict[builtins.str, typing.Any]]],
            instance_market_options: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The configuration details for a service managed Amazon EC2 fleet.

            :param instance_capabilities: The Amazon EC2 instance capabilities.
            :param instance_market_options: The Amazon EC2 market type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                service_managed_ec2_fleet_configuration_property = deadline.CfnFleet.ServiceManagedEc2FleetConfigurationProperty(
                    instance_capabilities=deadline.CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty(
                        cpu_architecture_type="cpuArchitectureType",
                        memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                            min=123,
                
                            # the properties below are optional
                            max=123
                        ),
                        os_family="osFamily",
                        v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                            min=123,
                
                            # the properties below are optional
                            max=123
                        ),
                
                        # the properties below are optional
                        allowed_instance_types=["allowedInstanceTypes"],
                        custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                            min=123,
                            name="name",
                
                            # the properties below are optional
                            max=123
                        )],
                        custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                            name="name",
                            values=["values"]
                        )],
                        excluded_instance_types=["excludedInstanceTypes"],
                        root_ebs_volume=deadline.CfnFleet.Ec2EbsVolumeProperty(
                            iops=123,
                            size_gi_b=123,
                            throughput_mi_b=123
                        )
                    ),
                    instance_market_options=deadline.CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty(
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a24a660b503191048581077a517891d27502b69620643c509073603283a2cb39)
                check_type(argname="argument instance_capabilities", value=instance_capabilities, expected_type=type_hints["instance_capabilities"])
                check_type(argname="argument instance_market_options", value=instance_market_options, expected_type=type_hints["instance_market_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_capabilities": instance_capabilities,
                "instance_market_options": instance_market_options,
            }

        @builtins.property
        def instance_capabilities(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty"]:
            '''The Amazon EC2 instance capabilities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration.html#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-instancecapabilities
            '''
            result = self._values.get("instance_capabilities")
            assert result is not None, "Required property 'instance_capabilities' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty"], result)

        @builtins.property
        def instance_market_options(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty"]:
            '''The Amazon EC2 market type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration.html#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-instancemarketoptions
            '''
            result = self._values.get("instance_market_options")
            assert result is not None, "Required property 'instance_market_options' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceManagedEc2FleetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu_architecture_type": "cpuArchitectureType",
            "memory_mib": "memoryMiB",
            "os_family": "osFamily",
            "v_cpu_count": "vCpuCount",
            "allowed_instance_types": "allowedInstanceTypes",
            "custom_amounts": "customAmounts",
            "custom_attributes": "customAttributes",
            "excluded_instance_types": "excludedInstanceTypes",
            "root_ebs_volume": "rootEbsVolume",
        },
    )
    class ServiceManagedEc2InstanceCapabilitiesProperty:
        def __init__(
            self,
            *,
            cpu_architecture_type: builtins.str,
            memory_mib: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.MemoryMiBRangeProperty", typing.Dict[builtins.str, typing.Any]]],
            os_family: builtins.str,
            v_cpu_count: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.VCpuCountRangeProperty", typing.Dict[builtins.str, typing.Any]]],
            allowed_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            custom_amounts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.FleetAmountCapabilityProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            custom_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.FleetAttributeCapabilityProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            root_ebs_volume: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.Ec2EbsVolumeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The Amazon EC2 instance capabilities.

            :param cpu_architecture_type: The CPU architecture type.
            :param memory_mib: The memory, as MiB, for the Amazon EC2 instance type.
            :param os_family: The operating system (OS) family.
            :param v_cpu_count: The amount of vCPU to require for instances in this fleet.
            :param allowed_instance_types: The allowable Amazon EC2 instance types.
            :param custom_amounts: The custom capability amounts to require for instances in this fleet.
            :param custom_attributes: The custom capability attributes to require for instances in this fleet.
            :param excluded_instance_types: The instance types to exclude from the fleet.
            :param root_ebs_volume: The root EBS volume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                service_managed_ec2_instance_capabilities_property = deadline.CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty(
                    cpu_architecture_type="cpuArchitectureType",
                    memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                        min=123,
                
                        # the properties below are optional
                        max=123
                    ),
                    os_family="osFamily",
                    v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                        min=123,
                
                        # the properties below are optional
                        max=123
                    ),
                
                    # the properties below are optional
                    allowed_instance_types=["allowedInstanceTypes"],
                    custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                        min=123,
                        name="name",
                
                        # the properties below are optional
                        max=123
                    )],
                    custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                        name="name",
                        values=["values"]
                    )],
                    excluded_instance_types=["excludedInstanceTypes"],
                    root_ebs_volume=deadline.CfnFleet.Ec2EbsVolumeProperty(
                        iops=123,
                        size_gi_b=123,
                        throughput_mi_b=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6bce0a6fe3858a9b9eaa850b95b27731a62d9ef26b45c40b5684d6586ed6996)
                check_type(argname="argument cpu_architecture_type", value=cpu_architecture_type, expected_type=type_hints["cpu_architecture_type"])
                check_type(argname="argument memory_mib", value=memory_mib, expected_type=type_hints["memory_mib"])
                check_type(argname="argument os_family", value=os_family, expected_type=type_hints["os_family"])
                check_type(argname="argument v_cpu_count", value=v_cpu_count, expected_type=type_hints["v_cpu_count"])
                check_type(argname="argument allowed_instance_types", value=allowed_instance_types, expected_type=type_hints["allowed_instance_types"])
                check_type(argname="argument custom_amounts", value=custom_amounts, expected_type=type_hints["custom_amounts"])
                check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
                check_type(argname="argument excluded_instance_types", value=excluded_instance_types, expected_type=type_hints["excluded_instance_types"])
                check_type(argname="argument root_ebs_volume", value=root_ebs_volume, expected_type=type_hints["root_ebs_volume"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cpu_architecture_type": cpu_architecture_type,
                "memory_mib": memory_mib,
                "os_family": os_family,
                "v_cpu_count": v_cpu_count,
            }
            if allowed_instance_types is not None:
                self._values["allowed_instance_types"] = allowed_instance_types
            if custom_amounts is not None:
                self._values["custom_amounts"] = custom_amounts
            if custom_attributes is not None:
                self._values["custom_attributes"] = custom_attributes
            if excluded_instance_types is not None:
                self._values["excluded_instance_types"] = excluded_instance_types
            if root_ebs_volume is not None:
                self._values["root_ebs_volume"] = root_ebs_volume

        @builtins.property
        def cpu_architecture_type(self) -> builtins.str:
            '''The CPU architecture type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-cpuarchitecturetype
            '''
            result = self._values.get("cpu_architecture_type")
            assert result is not None, "Required property 'cpu_architecture_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def memory_mib(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.MemoryMiBRangeProperty"]:
            '''The memory, as MiB, for the Amazon EC2 instance type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-memorymib
            '''
            result = self._values.get("memory_mib")
            assert result is not None, "Required property 'memory_mib' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.MemoryMiBRangeProperty"], result)

        @builtins.property
        def os_family(self) -> builtins.str:
            '''The operating system (OS) family.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-osfamily
            '''
            result = self._values.get("os_family")
            assert result is not None, "Required property 'os_family' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def v_cpu_count(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.VCpuCountRangeProperty"]:
            '''The amount of vCPU to require for instances in this fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-vcpucount
            '''
            result = self._values.get("v_cpu_count")
            assert result is not None, "Required property 'v_cpu_count' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.VCpuCountRangeProperty"], result)

        @builtins.property
        def allowed_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The allowable Amazon EC2 instance types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-allowedinstancetypes
            '''
            result = self._values.get("allowed_instance_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def custom_amounts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAmountCapabilityProperty"]]]]:
            '''The custom capability amounts to require for instances in this fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-customamounts
            '''
            result = self._values.get("custom_amounts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAmountCapabilityProperty"]]]], result)

        @builtins.property
        def custom_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAttributeCapabilityProperty"]]]]:
            '''The custom capability attributes to require for instances in this fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-customattributes
            '''
            result = self._values.get("custom_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.FleetAttributeCapabilityProperty"]]]], result)

        @builtins.property
        def excluded_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The instance types to exclude from the fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-excludedinstancetypes
            '''
            result = self._values.get("excluded_instance_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def root_ebs_volume(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.Ec2EbsVolumeProperty"]]:
            '''The root EBS volume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html#cfn-deadline-fleet-servicemanagedec2instancecapabilities-rootebsvolume
            '''
            result = self._values.get("root_ebs_volume")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.Ec2EbsVolumeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceManagedEc2InstanceCapabilitiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class ServiceManagedEc2InstanceMarketOptionsProperty:
        def __init__(self, *, type: builtins.str) -> None:
            '''The details of the Amazon EC2 instance market options for a service managed fleet.

            :param type: The Amazon EC2 instance type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                service_managed_ec2_instance_market_options_property = deadline.CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty(
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a8d3a0c18616b5264bff8fa8db0009f71df98b828f0e17e83fea3cc24b4a9443)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The Amazon EC2 instance type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions.html#cfn-deadline-fleet-servicemanagedec2instancemarketoptions-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceManagedEc2InstanceMarketOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnFleet.VCpuCountRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"min": "min", "max": "max"},
    )
    class VCpuCountRangeProperty:
        def __init__(
            self,
            *,
            min: jsii.Number,
            max: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The allowable range of vCPU processing power for the fleet.

            :param min: The minimum amount of vCPU.
            :param max: The maximum amount of vCPU.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-vcpucountrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                v_cpu_count_range_property = deadline.CfnFleet.VCpuCountRangeProperty(
                    min=123,
                
                    # the properties below are optional
                    max=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fcd8ae2a83778ec7a6d7445fcea241d1ce2694a66c1ccc07c23cdd1c8d829c4d)
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "min": min,
            }
            if max is not None:
                self._values["max"] = max

        @builtins.property
        def min(self) -> jsii.Number:
            '''The minimum amount of vCPU.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-vcpucountrange.html#cfn-deadline-fleet-vcpucountrange-min
            '''
            result = self._values.get("min")
            assert result is not None, "Required property 'min' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of vCPU.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-vcpucountrange.html#cfn-deadline-fleet-vcpucountrange-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VCpuCountRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_deadline.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "display_name": "displayName",
        "max_worker_count": "maxWorkerCount",
        "role_arn": "roleArn",
        "description": "description",
        "farm_id": "farmId",
        "min_worker_count": "minWorkerCount",
    },
)
class CfnFleetProps:
    def __init__(
        self,
        *,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        display_name: builtins.str,
        max_worker_count: jsii.Number,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        farm_id: typing.Optional[builtins.str] = None,
        min_worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param configuration: The configuration details for the fleet.
        :param display_name: The display name of the fleet summary to update.
        :param max_worker_count: The maximum number of workers specified in the fleet.
        :param role_arn: The IAM role that workers in the fleet use when processing jobs.
        :param description: A description that helps identify what the fleet is used for. Default: - ""
        :param farm_id: The farm ID.
        :param min_worker_count: The minimum number of workers in the fleet. Default: - 0

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_deadline as deadline
            
            cfn_fleet_props = deadline.CfnFleetProps(
                configuration=deadline.CfnFleet.FleetConfigurationProperty(
                    customer_managed=deadline.CfnFleet.CustomerManagedFleetConfigurationProperty(
                        mode="mode",
                        worker_capabilities=deadline.CfnFleet.CustomerManagedWorkerCapabilitiesProperty(
                            cpu_architecture_type="cpuArchitectureType",
                            memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                                min=123,
            
                                # the properties below are optional
                                max=123
                            ),
                            os_family="osFamily",
                            v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                                min=123,
            
                                # the properties below are optional
                                max=123
                            ),
            
                            # the properties below are optional
                            accelerator_count=deadline.CfnFleet.AcceleratorCountRangeProperty(
                                min=123,
            
                                # the properties below are optional
                                max=123
                            ),
                            accelerator_total_memory_mi_b=deadline.CfnFleet.AcceleratorTotalMemoryMiBRangeProperty(
                                min=123,
            
                                # the properties below are optional
                                max=123
                            ),
                            accelerator_types=["acceleratorTypes"],
                            custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                                min=123,
                                name="name",
            
                                # the properties below are optional
                                max=123
                            )],
                            custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                                name="name",
                                values=["values"]
                            )]
                        ),
            
                        # the properties below are optional
                        storage_profile_id="storageProfileId"
                    ),
                    service_managed_ec2=deadline.CfnFleet.ServiceManagedEc2FleetConfigurationProperty(
                        instance_capabilities=deadline.CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty(
                            cpu_architecture_type="cpuArchitectureType",
                            memory_mi_b=deadline.CfnFleet.MemoryMiBRangeProperty(
                                min=123,
            
                                # the properties below are optional
                                max=123
                            ),
                            os_family="osFamily",
                            v_cpu_count=deadline.CfnFleet.VCpuCountRangeProperty(
                                min=123,
            
                                # the properties below are optional
                                max=123
                            ),
            
                            # the properties below are optional
                            allowed_instance_types=["allowedInstanceTypes"],
                            custom_amounts=[deadline.CfnFleet.FleetAmountCapabilityProperty(
                                min=123,
                                name="name",
            
                                # the properties below are optional
                                max=123
                            )],
                            custom_attributes=[deadline.CfnFleet.FleetAttributeCapabilityProperty(
                                name="name",
                                values=["values"]
                            )],
                            excluded_instance_types=["excludedInstanceTypes"],
                            root_ebs_volume=deadline.CfnFleet.Ec2EbsVolumeProperty(
                                iops=123,
                                size_gi_b=123,
                                throughput_mi_b=123
                            )
                        ),
                        instance_market_options=deadline.CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty(
                            type="type"
                        )
                    )
                ),
                display_name="displayName",
                max_worker_count=123,
                role_arn="roleArn",
            
                # the properties below are optional
                description="description",
                farm_id="farmId",
                min_worker_count=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1472efddb89af74b2ae4dc1156d30448332099bec47f03ae56886a44d2d7c7a)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument max_worker_count", value=max_worker_count, expected_type=type_hints["max_worker_count"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument min_worker_count", value=min_worker_count, expected_type=type_hints["min_worker_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "display_name": display_name,
            "max_worker_count": max_worker_count,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if farm_id is not None:
            self._values["farm_id"] = farm_id
        if min_worker_count is not None:
            self._values["min_worker_count"] = min_worker_count

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnFleet.FleetConfigurationProperty]:
        '''The configuration details for the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html#cfn-deadline-fleet-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFleet.FleetConfigurationProperty], result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The display name of the fleet summary to update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html#cfn-deadline-fleet-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_worker_count(self) -> jsii.Number:
        '''The maximum number of workers specified in the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html#cfn-deadline-fleet-maxworkercount
        '''
        result = self._values.get("max_worker_count")
        assert result is not None, "Required property 'max_worker_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The IAM role that workers in the fleet use when processing jobs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html#cfn-deadline-fleet-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description that helps identify what the fleet is used for.

        :default: - ""

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html#cfn-deadline-fleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def farm_id(self) -> typing.Optional[builtins.str]:
        '''The farm ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html#cfn-deadline-fleet-farmid
        '''
        result = self._values.get("farm_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_worker_count(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of workers in the fleet.

        :default: - 0

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html#cfn-deadline-fleet-minworkercount
        '''
        result = self._values.get("min_worker_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLicenseEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_deadline.CfnLicenseEndpoint",
):
    '''Creates a license endpoint to integrate your various licensed software used for rendering on Deadline Cloud.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-licenseendpoint.html
    :cloudformationResource: AWS::Deadline::LicenseEndpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_deadline as deadline
        
        cfn_license_endpoint = deadline.CfnLicenseEndpoint(self, "MyCfnLicenseEndpoint",
            security_group_ids=["securityGroupIds"],
            subnet_ids=["subnetIds"],
            vpc_id="vpcId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_group_ids: The identifier of the Amazon EC2 security group that controls access to the license endpoint.
        :param subnet_ids: Identifies the VPC subnets that can connect to a license endpoint.
        :param vpc_id: The VCP(virtual private cloud) ID associated with the license endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2263281bf0506f61e2d06a34042a34c3aa49572fcab3143d4b6c4bc81a62b9a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLicenseEndpointProps(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids, vpc_id=vpc_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9aa87cad0472c90e08c8aa1a9c72cc53c01e0cf980555f0f3b357ef4148f041)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de6d4dde55dbb1dabd0b1e8734965495af6d2632c3444c0d7c5478f9682cd4a4)
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
        '''The Amazon Resource Name (ARN) of the license endpoint.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsName")
    def attr_dns_name(self) -> builtins.str:
        '''The DNS name of the license server endpoint.

        :cloudformationAttribute: DnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsName"))

    @builtins.property
    @jsii.member(jsii_name="attrLicenseEndpointId")
    def attr_license_endpoint_id(self) -> builtins.str:
        '''The license endpoint ID.

        :cloudformationAttribute: LicenseEndpointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLicenseEndpointId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the license endpoint.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''The status message of the license endpoint.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The identifier of the Amazon EC2 security group that controls access to the license endpoint.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b00e03274c83f79c32752b72b984299a4efe64919097bbbdec40f67b386b22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Identifies the VPC subnets that can connect to a license endpoint.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e81d93007bb20eb36480796e83aad3e6a0742393a78a71a87a71f081d070227a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The VCP(virtual private cloud) ID associated with the license endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fe095c981d830b60af0a60f921ac267a1eba38300aa520b18fa3678230ddaf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_deadline.CfnLicenseEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
    },
)
class CfnLicenseEndpointProps:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnLicenseEndpoint``.

        :param security_group_ids: The identifier of the Amazon EC2 security group that controls access to the license endpoint.
        :param subnet_ids: Identifies the VPC subnets that can connect to a license endpoint.
        :param vpc_id: The VCP(virtual private cloud) ID associated with the license endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-licenseendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_deadline as deadline
            
            cfn_license_endpoint_props = deadline.CfnLicenseEndpointProps(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a9c98d4186629e7162fde16ad1be09ade6a940c8cf979c87af77955e3a39f02)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The identifier of the Amazon EC2 security group that controls access to the license endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-licenseendpoint.html#cfn-deadline-licenseendpoint-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Identifies the VPC subnets that can connect to a license endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-licenseendpoint.html#cfn-deadline-licenseendpoint-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VCP(virtual private cloud) ID associated with the license endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-licenseendpoint.html#cfn-deadline-licenseendpoint-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLicenseEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMeteredProduct(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_deadline.CfnMeteredProduct",
):
    '''Adds a metered product.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-meteredproduct.html
    :cloudformationResource: AWS::Deadline::MeteredProduct
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_deadline as deadline
        
        cfn_metered_product = deadline.CfnMeteredProduct(self, "MyCfnMeteredProduct",
            family="family",
            license_endpoint_id="licenseEndpointId",
            port=123,
            product_id="productId",
            vendor="vendor"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        family: typing.Optional[builtins.str] = None,
        license_endpoint_id: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        product_id: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param family: The family to which the metered product belongs.
        :param license_endpoint_id: The Amazon EC2 identifier of the license endpoint.
        :param port: The port on which the metered product should run.
        :param product_id: The product ID.
        :param vendor: The vendor.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1349660e6447c1e6551d1ce7cde2c5dc6adbf1fb1fdceb9f214b066a5a6b4ebe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMeteredProductProps(
            family=family,
            license_endpoint_id=license_endpoint_id,
            port=port,
            product_id=product_id,
            vendor=vendor,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d2d01a238f229eb758201d336be8ca9e707d08020ad2910986c804ac3c7809)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ed6d8167aeed2952e867a5d1c33ef70cf0763f5978f31bbc292859ff9bb97a0)
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
        '''The Amazon Resource Name (ARN) of the metered product.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> typing.Optional[builtins.str]:
        '''The family to which the metered product belongs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "family"))

    @family.setter
    def family(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748584b3e13e6b6b100e3e825e6d4334d2e0c93a3397f0df55aae36a0abdc733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="licenseEndpointId")
    def license_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 identifier of the license endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseEndpointId"))

    @license_endpoint_id.setter
    def license_endpoint_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2392ecb737206631d7a319a666b254d855fea916d5e5430c1cb1bbe9c43d20de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port on which the metered product should run.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__866a9b65a442c0e4da725c11f8f3210a936a0cf69a370c376e7d42450692f1c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> typing.Optional[builtins.str]:
        '''The product ID.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7b3217dc50a692aa63ba3c945affcba562e3dca3ad6c9440d62b98f397be2ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> typing.Optional[builtins.str]:
        '''The vendor.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b31f8edad3d25c952475ac2363b0c1e60099e4c875dc5b54b5e01e1c9a364a59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendor", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_deadline.CfnMeteredProductProps",
    jsii_struct_bases=[],
    name_mapping={
        "family": "family",
        "license_endpoint_id": "licenseEndpointId",
        "port": "port",
        "product_id": "productId",
        "vendor": "vendor",
    },
)
class CfnMeteredProductProps:
    def __init__(
        self,
        *,
        family: typing.Optional[builtins.str] = None,
        license_endpoint_id: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        product_id: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMeteredProduct``.

        :param family: The family to which the metered product belongs.
        :param license_endpoint_id: The Amazon EC2 identifier of the license endpoint.
        :param port: The port on which the metered product should run.
        :param product_id: The product ID.
        :param vendor: The vendor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-meteredproduct.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_deadline as deadline
            
            cfn_metered_product_props = deadline.CfnMeteredProductProps(
                family="family",
                license_endpoint_id="licenseEndpointId",
                port=123,
                product_id="productId",
                vendor="vendor"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64de1639a953ff86a7b38c87a1ecf80a18f6b715e19b894e265cf51c1b6d4920)
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument license_endpoint_id", value=license_endpoint_id, expected_type=type_hints["license_endpoint_id"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument vendor", value=vendor, expected_type=type_hints["vendor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if family is not None:
            self._values["family"] = family
        if license_endpoint_id is not None:
            self._values["license_endpoint_id"] = license_endpoint_id
        if port is not None:
            self._values["port"] = port
        if product_id is not None:
            self._values["product_id"] = product_id
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def family(self) -> typing.Optional[builtins.str]:
        '''The family to which the metered product belongs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-meteredproduct.html#cfn-deadline-meteredproduct-family
        '''
        result = self._values.get("family")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 identifier of the license endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-meteredproduct.html#cfn-deadline-meteredproduct-licenseendpointid
        '''
        result = self._values.get("license_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port on which the metered product should run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-meteredproduct.html#cfn-deadline-meteredproduct-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def product_id(self) -> typing.Optional[builtins.str]:
        '''The product ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-meteredproduct.html#cfn-deadline-meteredproduct-productid
        '''
        result = self._values.get("product_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        '''The vendor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-meteredproduct.html#cfn-deadline-meteredproduct-vendor
        '''
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMeteredProductProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnQueue(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_deadline.CfnQueue",
):
    '''Creates a queue to coordinate the order in which jobs run on a farm.

    A queue can also specify where to pull resources and indicate where to output completed jobs.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html
    :cloudformationResource: AWS::Deadline::Queue
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_deadline as deadline
        
        cfn_queue = deadline.CfnQueue(self, "MyCfnQueue",
            display_name="displayName",
        
            # the properties below are optional
            allowed_storage_profile_ids=["allowedStorageProfileIds"],
            default_budget_action="defaultBudgetAction",
            description="description",
            farm_id="farmId",
            job_attachment_settings=deadline.CfnQueue.JobAttachmentSettingsProperty(
                root_prefix="rootPrefix",
                s3_bucket_name="s3BucketName"
            ),
            job_run_as_user=deadline.CfnQueue.JobRunAsUserProperty(
                run_as="runAs",
        
                # the properties below are optional
                posix=deadline.CfnQueue.PosixUserProperty(
                    group="group",
                    user="user"
                ),
                windows=deadline.CfnQueue.WindowsUserProperty(
                    password_arn="passwordArn",
                    user="user"
                )
            ),
            required_file_system_location_names=["requiredFileSystemLocationNames"],
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        allowed_storage_profile_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_budget_action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        farm_id: typing.Optional[builtins.str] = None,
        job_attachment_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQueue.JobAttachmentSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        job_run_as_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQueue.JobRunAsUserProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_file_system_location_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param display_name: The display name of the queue summary to update.
        :param allowed_storage_profile_ids: The identifiers of the storage profiles that this queue can use to share assets between workers using different operating systems.
        :param default_budget_action: The default action taken on a queue summary if a budget wasn't configured. Default: - "NONE"
        :param description: A description of the queue that helps identify what the queue is used for. Default: - ""
        :param farm_id: The farm ID.
        :param job_attachment_settings: The job attachment settings. These are the Amazon S3 bucket name and the Amazon S3 prefix.
        :param job_run_as_user: Identifies the user for a job.
        :param required_file_system_location_names: The file system location that the queue uses.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that workers use when running jobs in this queue.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8ed104ef6a730c7b90ba82ab4ab0b37d213e5444e12df63d7d60b1e23323e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQueueProps(
            display_name=display_name,
            allowed_storage_profile_ids=allowed_storage_profile_ids,
            default_budget_action=default_budget_action,
            description=description,
            farm_id=farm_id,
            job_attachment_settings=job_attachment_settings,
            job_run_as_user=job_run_as_user,
            required_file_system_location_names=required_file_system_location_names,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50a951ea75684c1a0e1477adfe4d54001bbe626c602cd5380b6445649ddc198e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__12f2ec2b01e12cf5d244b5ae5c7b25018631c87603b7819e99ad82f931094696)
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
        '''The Amazon Resource Name (ARN) of the queue.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrQueueId")
    def attr_queue_id(self) -> builtins.str:
        '''The queue ID.

        :cloudformationAttribute: QueueId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueueId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The display name of the queue summary to update.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abb08cf6c0a4af9928a3c56fba912abab7cd2c3c4760117e91af2d94f15d5f6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="allowedStorageProfileIds")
    def allowed_storage_profile_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identifiers of the storage profiles that this queue can use to share assets between workers using different operating systems.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedStorageProfileIds"))

    @allowed_storage_profile_ids.setter
    def allowed_storage_profile_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__261c15a318630458194b6ce3058afe2cbf9e193004fd4e7287059f40d08582f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedStorageProfileIds", value)

    @builtins.property
    @jsii.member(jsii_name="defaultBudgetAction")
    def default_budget_action(self) -> typing.Optional[builtins.str]:
        '''The default action taken on a queue summary if a budget wasn't configured.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultBudgetAction"))

    @default_budget_action.setter
    def default_budget_action(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ed3fcb26efc70612b9ed8cbcccb35da23ffe53b337b83ec742c863a4da84b6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBudgetAction", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the queue that helps identify what the queue is used for.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2559bfc8e75a5a3fe6743bfc64664fbf4a6fc6cb24717a6669ce9a31c288f44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="farmId")
    def farm_id(self) -> typing.Optional[builtins.str]:
        '''The farm ID.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "farmId"))

    @farm_id.setter
    def farm_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fef4d1848bd17d1a655bb4cb1236551eab481ebefcdbbd4e5ae7acc710720145)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "farmId", value)

    @builtins.property
    @jsii.member(jsii_name="jobAttachmentSettings")
    def job_attachment_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.JobAttachmentSettingsProperty"]]:
        '''The job attachment settings.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.JobAttachmentSettingsProperty"]], jsii.get(self, "jobAttachmentSettings"))

    @job_attachment_settings.setter
    def job_attachment_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.JobAttachmentSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358c548fac5f624a3c1d72ec9252063f4d1a9bd3c0342b2e54358d53c0204b5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobAttachmentSettings", value)

    @builtins.property
    @jsii.member(jsii_name="jobRunAsUser")
    def job_run_as_user(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.JobRunAsUserProperty"]]:
        '''Identifies the user for a job.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.JobRunAsUserProperty"]], jsii.get(self, "jobRunAsUser"))

    @job_run_as_user.setter
    def job_run_as_user(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.JobRunAsUserProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b1f44b18bbd9cd34d33d3fe1de23e5f60be6648dd1ee50efa7531459cd7ae65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobRunAsUser", value)

    @builtins.property
    @jsii.member(jsii_name="requiredFileSystemLocationNames")
    def required_file_system_location_names(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The file system location that the queue uses.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requiredFileSystemLocationNames"))

    @required_file_system_location_names.setter
    def required_file_system_location_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d9c178caaac7844afec201e90468fdd98d393162443d88987d2fd5342fb2025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredFileSystemLocationNames", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role that workers use when running jobs in this queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb5bb7ca40abe81d0cb9afaa09246c4bbb7553021c1125ddbc8a2f83d0da3db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnQueue.JobAttachmentSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"root_prefix": "rootPrefix", "s3_bucket_name": "s3BucketName"},
    )
    class JobAttachmentSettingsProperty:
        def __init__(
            self,
            *,
            root_prefix: builtins.str,
            s3_bucket_name: builtins.str,
        ) -> None:
            '''The job attachment settings.

            These are the Amazon S3 bucket name and the Amazon S3 prefix.

            :param root_prefix: The root prefix.
            :param s3_bucket_name: The Amazon S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobattachmentsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                job_attachment_settings_property = deadline.CfnQueue.JobAttachmentSettingsProperty(
                    root_prefix="rootPrefix",
                    s3_bucket_name="s3BucketName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a91b9031e7181044273ba1904b3e19809ee9a8ab762fe24c5dbe20fcf400ff60)
                check_type(argname="argument root_prefix", value=root_prefix, expected_type=type_hints["root_prefix"])
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "root_prefix": root_prefix,
                "s3_bucket_name": s3_bucket_name,
            }

        @builtins.property
        def root_prefix(self) -> builtins.str:
            '''The root prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobattachmentsettings.html#cfn-deadline-queue-jobattachmentsettings-rootprefix
            '''
            result = self._values.get("root_prefix")
            assert result is not None, "Required property 'root_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket_name(self) -> builtins.str:
            '''The Amazon S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobattachmentsettings.html#cfn-deadline-queue-jobattachmentsettings-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            assert result is not None, "Required property 's3_bucket_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobAttachmentSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnQueue.JobRunAsUserProperty",
        jsii_struct_bases=[],
        name_mapping={"run_as": "runAs", "posix": "posix", "windows": "windows"},
    )
    class JobRunAsUserProperty:
        def __init__(
            self,
            *,
            run_as: builtins.str,
            posix: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQueue.PosixUserProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            windows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQueue.WindowsUserProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Identifies the user for a job.

            :param run_as: Specifies whether the job should run using the queue's system user or if the job should run using the worker agent system user.
            :param posix: The user and group that the jobs in the queue run as.
            :param windows: Identifies a Microsoft Windows user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobrunasuser.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                job_run_as_user_property = deadline.CfnQueue.JobRunAsUserProperty(
                    run_as="runAs",
                
                    # the properties below are optional
                    posix=deadline.CfnQueue.PosixUserProperty(
                        group="group",
                        user="user"
                    ),
                    windows=deadline.CfnQueue.WindowsUserProperty(
                        password_arn="passwordArn",
                        user="user"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__06247d11c191e79686284edad9440c4d5c7e8038f712251f72b1a60140fbcd14)
                check_type(argname="argument run_as", value=run_as, expected_type=type_hints["run_as"])
                check_type(argname="argument posix", value=posix, expected_type=type_hints["posix"])
                check_type(argname="argument windows", value=windows, expected_type=type_hints["windows"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "run_as": run_as,
            }
            if posix is not None:
                self._values["posix"] = posix
            if windows is not None:
                self._values["windows"] = windows

        @builtins.property
        def run_as(self) -> builtins.str:
            '''Specifies whether the job should run using the queue's system user or if the job should run using the worker agent system user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobrunasuser.html#cfn-deadline-queue-jobrunasuser-runas
            '''
            result = self._values.get("run_as")
            assert result is not None, "Required property 'run_as' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def posix(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.PosixUserProperty"]]:
            '''The user and group that the jobs in the queue run as.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobrunasuser.html#cfn-deadline-queue-jobrunasuser-posix
            '''
            result = self._values.get("posix")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.PosixUserProperty"]], result)

        @builtins.property
        def windows(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.WindowsUserProperty"]]:
            '''Identifies a Microsoft Windows user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobrunasuser.html#cfn-deadline-queue-jobrunasuser-windows
            '''
            result = self._values.get("windows")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.WindowsUserProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobRunAsUserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnQueue.PosixUserProperty",
        jsii_struct_bases=[],
        name_mapping={"group": "group", "user": "user"},
    )
    class PosixUserProperty:
        def __init__(self, *, group: builtins.str, user: builtins.str) -> None:
            '''The POSIX user.

            :param group: The name of the POSIX user's group.
            :param user: The name of the POSIX user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-posixuser.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                posix_user_property = deadline.CfnQueue.PosixUserProperty(
                    group="group",
                    user="user"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e675ce01c62a0076a355385ac17aeacd32612beedb164bb4511f338c9a841594)
                check_type(argname="argument group", value=group, expected_type=type_hints["group"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "group": group,
                "user": user,
            }

        @builtins.property
        def group(self) -> builtins.str:
            '''The name of the POSIX user's group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-posixuser.html#cfn-deadline-queue-posixuser-group
            '''
            result = self._values.get("group")
            assert result is not None, "Required property 'group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user(self) -> builtins.str:
            '''The name of the POSIX user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-posixuser.html#cfn-deadline-queue-posixuser-user
            '''
            result = self._values.get("user")
            assert result is not None, "Required property 'user' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PosixUserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnQueue.WindowsUserProperty",
        jsii_struct_bases=[],
        name_mapping={"password_arn": "passwordArn", "user": "user"},
    )
    class WindowsUserProperty:
        def __init__(self, *, password_arn: builtins.str, user: builtins.str) -> None:
            '''The Windows user details.

            :param password_arn: The password ARN for the Windows user.
            :param user: The user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-windowsuser.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                windows_user_property = deadline.CfnQueue.WindowsUserProperty(
                    password_arn="passwordArn",
                    user="user"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e21f3cd393d77359583c8744ba670e4eb05b1b53d4bba3a35461caec2a91fc9c)
                check_type(argname="argument password_arn", value=password_arn, expected_type=type_hints["password_arn"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password_arn": password_arn,
                "user": user,
            }

        @builtins.property
        def password_arn(self) -> builtins.str:
            '''The password ARN for the Windows user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-windowsuser.html#cfn-deadline-queue-windowsuser-passwordarn
            '''
            result = self._values.get("password_arn")
            assert result is not None, "Required property 'password_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user(self) -> builtins.str:
            '''The user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-windowsuser.html#cfn-deadline-queue-windowsuser-user
            '''
            result = self._values.get("user")
            assert result is not None, "Required property 'user' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WindowsUserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnQueueEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_deadline.CfnQueueEnvironment",
):
    '''Creates an environment for a queue that defines how jobs in the queue run.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html
    :cloudformationResource: AWS::Deadline::QueueEnvironment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_deadline as deadline
        
        cfn_queue_environment = deadline.CfnQueueEnvironment(self, "MyCfnQueueEnvironment",
            farm_id="farmId",
            priority=123,
            queue_id="queueId",
            template="template",
            template_type="templateType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        farm_id: builtins.str,
        priority: jsii.Number,
        queue_id: builtins.str,
        template: builtins.str,
        template_type: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param farm_id: The identifier assigned to the farm that contains the queue.
        :param priority: The queue environment's priority.
        :param queue_id: The unique identifier of the queue that contains the environment.
        :param template: A JSON or YAML template the describes the processing environment for the queue.
        :param template_type: Specifies whether the template for the queue environment is JSON or YAML.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cf2ef79ee46780c7590cdcaf16949904d0291a2627b57555ffa860cb355319b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQueueEnvironmentProps(
            farm_id=farm_id,
            priority=priority,
            queue_id=queue_id,
            template=template,
            template_type=template_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a6465894d7e168ae6fe30f0f0519094a5d10b4a0db099eaf9e05619574ec819)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4234e955a996a24390a16b9a75175a9e7766aa94cc035cd920a37d37e152197)
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
        '''The name of the queue environment.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrQueueEnvironmentId")
    def attr_queue_environment_id(self) -> builtins.str:
        '''The queue environment ID.

        :cloudformationAttribute: QueueEnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueueEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="farmId")
    def farm_id(self) -> builtins.str:
        '''The identifier assigned to the farm that contains the queue.'''
        return typing.cast(builtins.str, jsii.get(self, "farmId"))

    @farm_id.setter
    def farm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee0a8ebb761f1a339ba695cf1c4453345e0569d6f01c23d4df36dd86031814e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "farmId", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''The queue environment's priority.'''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__462f62b321d72f5a88f323c76e44d85eaa3374e0f6adb3f512104435274114c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="queueId")
    def queue_id(self) -> builtins.str:
        '''The unique identifier of the queue that contains the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "queueId"))

    @queue_id.setter
    def queue_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e636e4de083154e3080b3a798c660c93a0d0503ff898703d5f4337707ee40a26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueId", value)

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> builtins.str:
        '''A JSON or YAML template the describes the processing environment for the queue.'''
        return typing.cast(builtins.str, jsii.get(self, "template"))

    @template.setter
    def template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bebb6c72d0cd02e4f9a11ae2664110700bb277dc5fc328e6a9679f00fe106638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @builtins.property
    @jsii.member(jsii_name="templateType")
    def template_type(self) -> builtins.str:
        '''Specifies whether the template for the queue environment is JSON or YAML.'''
        return typing.cast(builtins.str, jsii.get(self, "templateType"))

    @template_type.setter
    def template_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4192f38c45d04e5d9283902f89bf09ebe24569bc7c096f6e34e9a156c7f2896)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_deadline.CfnQueueEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "farm_id": "farmId",
        "priority": "priority",
        "queue_id": "queueId",
        "template": "template",
        "template_type": "templateType",
    },
)
class CfnQueueEnvironmentProps:
    def __init__(
        self,
        *,
        farm_id: builtins.str,
        priority: jsii.Number,
        queue_id: builtins.str,
        template: builtins.str,
        template_type: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnQueueEnvironment``.

        :param farm_id: The identifier assigned to the farm that contains the queue.
        :param priority: The queue environment's priority.
        :param queue_id: The unique identifier of the queue that contains the environment.
        :param template: A JSON or YAML template the describes the processing environment for the queue.
        :param template_type: Specifies whether the template for the queue environment is JSON or YAML.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_deadline as deadline
            
            cfn_queue_environment_props = deadline.CfnQueueEnvironmentProps(
                farm_id="farmId",
                priority=123,
                queue_id="queueId",
                template="template",
                template_type="templateType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea67e4e193bb92e88985247d97314b7feb5f0208ac9f9998cecd35054915fe67)
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument queue_id", value=queue_id, expected_type=type_hints["queue_id"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument template_type", value=template_type, expected_type=type_hints["template_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "farm_id": farm_id,
            "priority": priority,
            "queue_id": queue_id,
            "template": template,
            "template_type": template_type,
        }

    @builtins.property
    def farm_id(self) -> builtins.str:
        '''The identifier assigned to the farm that contains the queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html#cfn-deadline-queueenvironment-farmid
        '''
        result = self._values.get("farm_id")
        assert result is not None, "Required property 'farm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The queue environment's priority.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html#cfn-deadline-queueenvironment-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def queue_id(self) -> builtins.str:
        '''The unique identifier of the queue that contains the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html#cfn-deadline-queueenvironment-queueid
        '''
        result = self._values.get("queue_id")
        assert result is not None, "Required property 'queue_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template(self) -> builtins.str:
        '''A JSON or YAML template the describes the processing environment for the queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html#cfn-deadline-queueenvironment-template
        '''
        result = self._values.get("template")
        assert result is not None, "Required property 'template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_type(self) -> builtins.str:
        '''Specifies whether the template for the queue environment is JSON or YAML.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html#cfn-deadline-queueenvironment-templatetype
        '''
        result = self._values.get("template_type")
        assert result is not None, "Required property 'template_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueueEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnQueueFleetAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_deadline.CfnQueueFleetAssociation",
):
    '''Creates an association between a queue and a fleet.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queuefleetassociation.html
    :cloudformationResource: AWS::Deadline::QueueFleetAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_deadline as deadline
        
        cfn_queue_fleet_association = deadline.CfnQueueFleetAssociation(self, "MyCfnQueueFleetAssociation",
            farm_id="farmId",
            fleet_id="fleetId",
            queue_id="queueId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        farm_id: builtins.str,
        fleet_id: builtins.str,
        queue_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param farm_id: The identifier of the farm that contains the queue and the fleet.
        :param fleet_id: The fleet ID.
        :param queue_id: The queue ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf5f16a9974daab9dba069dab2d83de0ff5b4a6e417026bc9f4c775d17511e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQueueFleetAssociationProps(
            farm_id=farm_id, fleet_id=fleet_id, queue_id=queue_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ff12ea5f9a70d8e7142807e0c6f13883ba906fa01e1e7887b8de68261b1db16)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e31fddcabe78ead7dcb1221739b2cf550282943452143253d1aba9300c17652)
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
    @jsii.member(jsii_name="farmId")
    def farm_id(self) -> builtins.str:
        '''The identifier of the farm that contains the queue and the fleet.'''
        return typing.cast(builtins.str, jsii.get(self, "farmId"))

    @farm_id.setter
    def farm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e19729f1c6fb8ec0c8b6f6c31e0865e9725dd22fc08c9ec2197711d95f5baa21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "farmId", value)

    @builtins.property
    @jsii.member(jsii_name="fleetId")
    def fleet_id(self) -> builtins.str:
        '''The fleet ID.'''
        return typing.cast(builtins.str, jsii.get(self, "fleetId"))

    @fleet_id.setter
    def fleet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf8c906b58e9214a10c2d83a1b139049a42f93254fc8ec57da660c71ab58bb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetId", value)

    @builtins.property
    @jsii.member(jsii_name="queueId")
    def queue_id(self) -> builtins.str:
        '''The queue ID.'''
        return typing.cast(builtins.str, jsii.get(self, "queueId"))

    @queue_id.setter
    def queue_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad97a4082938a418ac03725615af17abfdffa0f3dcb8f92815671754e0657141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_deadline.CfnQueueFleetAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"farm_id": "farmId", "fleet_id": "fleetId", "queue_id": "queueId"},
)
class CfnQueueFleetAssociationProps:
    def __init__(
        self,
        *,
        farm_id: builtins.str,
        fleet_id: builtins.str,
        queue_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnQueueFleetAssociation``.

        :param farm_id: The identifier of the farm that contains the queue and the fleet.
        :param fleet_id: The fleet ID.
        :param queue_id: The queue ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queuefleetassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_deadline as deadline
            
            cfn_queue_fleet_association_props = deadline.CfnQueueFleetAssociationProps(
                farm_id="farmId",
                fleet_id="fleetId",
                queue_id="queueId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5457199586ad5b5517f14765c4203a9a198d98c68deaf06933477e9fcccc9ffb)
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
            check_type(argname="argument queue_id", value=queue_id, expected_type=type_hints["queue_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "queue_id": queue_id,
        }

    @builtins.property
    def farm_id(self) -> builtins.str:
        '''The identifier of the farm that contains the queue and the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queuefleetassociation.html#cfn-deadline-queuefleetassociation-farmid
        '''
        result = self._values.get("farm_id")
        assert result is not None, "Required property 'farm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fleet_id(self) -> builtins.str:
        '''The fleet ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queuefleetassociation.html#cfn-deadline-queuefleetassociation-fleetid
        '''
        result = self._values.get("fleet_id")
        assert result is not None, "Required property 'fleet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_id(self) -> builtins.str:
        '''The queue ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queuefleetassociation.html#cfn-deadline-queuefleetassociation-queueid
        '''
        result = self._values.get("queue_id")
        assert result is not None, "Required property 'queue_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueueFleetAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_deadline.CfnQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "allowed_storage_profile_ids": "allowedStorageProfileIds",
        "default_budget_action": "defaultBudgetAction",
        "description": "description",
        "farm_id": "farmId",
        "job_attachment_settings": "jobAttachmentSettings",
        "job_run_as_user": "jobRunAsUser",
        "required_file_system_location_names": "requiredFileSystemLocationNames",
        "role_arn": "roleArn",
    },
)
class CfnQueueProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        allowed_storage_profile_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_budget_action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        farm_id: typing.Optional[builtins.str] = None,
        job_attachment_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.JobAttachmentSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        job_run_as_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.JobRunAsUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        required_file_system_location_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnQueue``.

        :param display_name: The display name of the queue summary to update.
        :param allowed_storage_profile_ids: The identifiers of the storage profiles that this queue can use to share assets between workers using different operating systems.
        :param default_budget_action: The default action taken on a queue summary if a budget wasn't configured. Default: - "NONE"
        :param description: A description of the queue that helps identify what the queue is used for. Default: - ""
        :param farm_id: The farm ID.
        :param job_attachment_settings: The job attachment settings. These are the Amazon S3 bucket name and the Amazon S3 prefix.
        :param job_run_as_user: Identifies the user for a job.
        :param required_file_system_location_names: The file system location that the queue uses.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that workers use when running jobs in this queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_deadline as deadline
            
            cfn_queue_props = deadline.CfnQueueProps(
                display_name="displayName",
            
                # the properties below are optional
                allowed_storage_profile_ids=["allowedStorageProfileIds"],
                default_budget_action="defaultBudgetAction",
                description="description",
                farm_id="farmId",
                job_attachment_settings=deadline.CfnQueue.JobAttachmentSettingsProperty(
                    root_prefix="rootPrefix",
                    s3_bucket_name="s3BucketName"
                ),
                job_run_as_user=deadline.CfnQueue.JobRunAsUserProperty(
                    run_as="runAs",
            
                    # the properties below are optional
                    posix=deadline.CfnQueue.PosixUserProperty(
                        group="group",
                        user="user"
                    ),
                    windows=deadline.CfnQueue.WindowsUserProperty(
                        password_arn="passwordArn",
                        user="user"
                    )
                ),
                required_file_system_location_names=["requiredFileSystemLocationNames"],
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a92d64f51023fd5b945aa0d9e2b696749e02f9df358265737e05dd4a730fd30d)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument allowed_storage_profile_ids", value=allowed_storage_profile_ids, expected_type=type_hints["allowed_storage_profile_ids"])
            check_type(argname="argument default_budget_action", value=default_budget_action, expected_type=type_hints["default_budget_action"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument job_attachment_settings", value=job_attachment_settings, expected_type=type_hints["job_attachment_settings"])
            check_type(argname="argument job_run_as_user", value=job_run_as_user, expected_type=type_hints["job_run_as_user"])
            check_type(argname="argument required_file_system_location_names", value=required_file_system_location_names, expected_type=type_hints["required_file_system_location_names"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
        }
        if allowed_storage_profile_ids is not None:
            self._values["allowed_storage_profile_ids"] = allowed_storage_profile_ids
        if default_budget_action is not None:
            self._values["default_budget_action"] = default_budget_action
        if description is not None:
            self._values["description"] = description
        if farm_id is not None:
            self._values["farm_id"] = farm_id
        if job_attachment_settings is not None:
            self._values["job_attachment_settings"] = job_attachment_settings
        if job_run_as_user is not None:
            self._values["job_run_as_user"] = job_run_as_user
        if required_file_system_location_names is not None:
            self._values["required_file_system_location_names"] = required_file_system_location_names
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The display name of the queue summary to update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_storage_profile_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identifiers of the storage profiles that this queue can use to share assets between workers using different operating systems.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-allowedstorageprofileids
        '''
        result = self._values.get("allowed_storage_profile_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_budget_action(self) -> typing.Optional[builtins.str]:
        '''The default action taken on a queue summary if a budget wasn't configured.

        :default: - "NONE"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-defaultbudgetaction
        '''
        result = self._values.get("default_budget_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the queue that helps identify what the queue is used for.

        :default: - ""

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def farm_id(self) -> typing.Optional[builtins.str]:
        '''The farm ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-farmid
        '''
        result = self._values.get("farm_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_attachment_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.JobAttachmentSettingsProperty]]:
        '''The job attachment settings.

        These are the Amazon S3 bucket name and the Amazon S3 prefix.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-jobattachmentsettings
        '''
        result = self._values.get("job_attachment_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.JobAttachmentSettingsProperty]], result)

    @builtins.property
    def job_run_as_user(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.JobRunAsUserProperty]]:
        '''Identifies the user for a job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-jobrunasuser
        '''
        result = self._values.get("job_run_as_user")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.JobRunAsUserProperty]], result)

    @builtins.property
    def required_file_system_location_names(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The file system location that the queue uses.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-requiredfilesystemlocationnames
        '''
        result = self._values.get("required_file_system_location_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role that workers use when running jobs in this queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html#cfn-deadline-queue-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStorageProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_deadline.CfnStorageProfile",
):
    '''Creates a storage profile that specifies the operating system, file type, and file location of resources used on a farm.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html
    :cloudformationResource: AWS::Deadline::StorageProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_deadline as deadline
        
        cfn_storage_profile = deadline.CfnStorageProfile(self, "MyCfnStorageProfile",
            display_name="displayName",
            os_family="osFamily",
        
            # the properties below are optional
            farm_id="farmId",
            file_system_locations=[deadline.CfnStorageProfile.FileSystemLocationProperty(
                name="name",
                path="path",
                type="type"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        os_family: builtins.str,
        farm_id: typing.Optional[builtins.str] = None,
        file_system_locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStorageProfile.FileSystemLocationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param display_name: The display name of the storage profile summary to update.
        :param os_family: The operating system (OS) family.
        :param farm_id: The unique identifier of the farm that contains the storage profile.
        :param file_system_locations: Operating system specific file system path to the storage location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bb4938fbe160a975ec7626f79799d48d7603f2cc166cf513bf1920de8659cb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStorageProfileProps(
            display_name=display_name,
            os_family=os_family,
            farm_id=farm_id,
            file_system_locations=file_system_locations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f2c21ddee6a44d7c3543d169f12db3f66484a191cb97771d03130be960a1dde)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9daf383d7a7e24cea3229e3fe4ee60cad6d86ebd3ae060051973527e9544b1a5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageProfileId")
    def attr_storage_profile_id(self) -> builtins.str:
        '''The storage profile ID.

        :cloudformationAttribute: StorageProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageProfileId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The display name of the storage profile summary to update.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f20c6213a2c65defbfbde8129f9b8c1e7681d519ea98354db0d5bbcf5e03e8d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="osFamily")
    def os_family(self) -> builtins.str:
        '''The operating system (OS) family.'''
        return typing.cast(builtins.str, jsii.get(self, "osFamily"))

    @os_family.setter
    def os_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff32f8bb060d0ada4a6522805c78bae216b6b86ab15b16b64b07a49ae94df357)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osFamily", value)

    @builtins.property
    @jsii.member(jsii_name="farmId")
    def farm_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the farm that contains the storage profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "farmId"))

    @farm_id.setter
    def farm_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f736eedcb6c466af3ef1210e274e369c621b42de8f8102b78a138c4d5cc04f9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "farmId", value)

    @builtins.property
    @jsii.member(jsii_name="fileSystemLocations")
    def file_system_locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStorageProfile.FileSystemLocationProperty"]]]]:
        '''Operating system specific file system path to the storage location.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStorageProfile.FileSystemLocationProperty"]]]], jsii.get(self, "fileSystemLocations"))

    @file_system_locations.setter
    def file_system_locations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStorageProfile.FileSystemLocationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41022fa9902dd4229e3676de8f74c666e01c3237936ce7470d2c1ab45b6055ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemLocations", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_deadline.CfnStorageProfile.FileSystemLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "path": "path", "type": "type"},
    )
    class FileSystemLocationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            path: builtins.str,
            type: builtins.str,
        ) -> None:
            '''The details of the file system location for the resource.

            :param name: The location name.
            :param path: The file path.
            :param type: The type of file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-storageprofile-filesystemlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_deadline as deadline
                
                file_system_location_property = deadline.CfnStorageProfile.FileSystemLocationProperty(
                    name="name",
                    path="path",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30accc33e266fd187349c32faa815a79744e919f16060567a73b75c87e43a574)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "path": path,
                "type": type,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The location name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-storageprofile-filesystemlocation.html#cfn-deadline-storageprofile-filesystemlocation-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> builtins.str:
            '''The file path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-storageprofile-filesystemlocation.html#cfn-deadline-storageprofile-filesystemlocation-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-storageprofile-filesystemlocation.html#cfn-deadline-storageprofile-filesystemlocation-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileSystemLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_deadline.CfnStorageProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "os_family": "osFamily",
        "farm_id": "farmId",
        "file_system_locations": "fileSystemLocations",
    },
)
class CfnStorageProfileProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        os_family: builtins.str,
        farm_id: typing.Optional[builtins.str] = None,
        file_system_locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageProfile.FileSystemLocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStorageProfile``.

        :param display_name: The display name of the storage profile summary to update.
        :param os_family: The operating system (OS) family.
        :param farm_id: The unique identifier of the farm that contains the storage profile.
        :param file_system_locations: Operating system specific file system path to the storage location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_deadline as deadline
            
            cfn_storage_profile_props = deadline.CfnStorageProfileProps(
                display_name="displayName",
                os_family="osFamily",
            
                # the properties below are optional
                farm_id="farmId",
                file_system_locations=[deadline.CfnStorageProfile.FileSystemLocationProperty(
                    name="name",
                    path="path",
                    type="type"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d873ae2006c75776847d16361d1b495d51e00d618e49d32a001db4fe2f72991)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument os_family", value=os_family, expected_type=type_hints["os_family"])
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument file_system_locations", value=file_system_locations, expected_type=type_hints["file_system_locations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
            "os_family": os_family,
        }
        if farm_id is not None:
            self._values["farm_id"] = farm_id
        if file_system_locations is not None:
            self._values["file_system_locations"] = file_system_locations

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The display name of the storage profile summary to update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html#cfn-deadline-storageprofile-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def os_family(self) -> builtins.str:
        '''The operating system (OS) family.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html#cfn-deadline-storageprofile-osfamily
        '''
        result = self._values.get("os_family")
        assert result is not None, "Required property 'os_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def farm_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the farm that contains the storage profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html#cfn-deadline-storageprofile-farmid
        '''
        result = self._values.get("farm_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system_locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStorageProfile.FileSystemLocationProperty]]]]:
        '''Operating system specific file system path to the storage location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html#cfn-deadline-storageprofile-filesystemlocations
        '''
        result = self._values.get("file_system_locations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStorageProfile.FileSystemLocationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStorageProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFarm",
    "CfnFarmProps",
    "CfnFleet",
    "CfnFleetProps",
    "CfnLicenseEndpoint",
    "CfnLicenseEndpointProps",
    "CfnMeteredProduct",
    "CfnMeteredProductProps",
    "CfnQueue",
    "CfnQueueEnvironment",
    "CfnQueueEnvironmentProps",
    "CfnQueueFleetAssociation",
    "CfnQueueFleetAssociationProps",
    "CfnQueueProps",
    "CfnStorageProfile",
    "CfnStorageProfileProps",
]

publication.publish()

def _typecheckingstub__c8cfafb7690986cd3ddb4ba2de814f300f2faab0827e01a86f2f528af27544d1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    display_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6b1d970d70d840fd22a69886b9553ac48f2e83d63e421ea979261b3bddf1d0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46eb3e8dead939804597fc70dfb9f5b385b7dfeedc4caf4b49813000440c7a7e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3487107fca3fbd8f0f2e3e65063da63a41a523cd6d5ffd0aef63e8ec4c680c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225609e046f467aa1cff6857451a01a60bf944d05094eaea191c40155a7b5ee4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd09d08fc701cc061b023ad6a5d72db4516ff09e295b470365e390436475464(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85eb8ab8e233d51550c535a34f621e657ea5dfc47e9b977b5a9b73c3be4b9b4f(
    *,
    display_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b982dfa2ac88548efd13c63c65f7144bf79a74dd670eebe5a13537f1fa38090a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    display_name: builtins.str,
    max_worker_count: jsii.Number,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    farm_id: typing.Optional[builtins.str] = None,
    min_worker_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c7467a1be46332c11edfbc2f2073b67842b79e2b6dc68d7fa0312c8a5b8c595(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__624f83add0edac45b93d9318e64f5196dd2045c50f094e69787beb05aa8c11d7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e2fe844317b39494e7f7a1851d6e5842bc0627b2cc937a6709042cb43a27a3f(
    value: typing.Union[_IResolvable_da3f097b, CfnFleet.FleetConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d501705678e5cc3f1a305c922a22f7ba207d560bdb5761b3ce0e042852101fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435144cf5095e3c8ecf5073fcb2ee802817fde90c7c30f2fa7b579407c82a89a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__471ed3a4e000dd618e2be0578e42aa2e8288223309b77395023cba44dff3a738(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__084da5a242d843b332de24a8c53af7e8830cd00d0dca22235f0c3d665732570b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ce1167517d9e9a39c50fdbd55b565e28d3f5dca61d4b795926951043d1cc2d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e98aa63695c4cd93c0aae20c0cd7e90226c1100540a8732e0be19b9d6cc5e094(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4d7e76219e8cce8e44e215b08cd1fef54b62ca3d48dbbc0bc8b3e6040db253e(
    *,
    min: jsii.Number,
    max: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e87ae0b2cf7001539dfe803c414d6da11bd37d8db4fe33e1b4847d22cccfd0e(
    *,
    min: jsii.Number,
    max: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e0d0744c60a31b3157ef03f930266f6c000eafa44c6050607897ea5b3e3881d(
    *,
    mode: builtins.str,
    worker_capabilities: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CustomerManagedWorkerCapabilitiesProperty, typing.Dict[builtins.str, typing.Any]]],
    storage_profile_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbfd53a4095156c6675556d0bc3d17d02d807749147c8ab86039c9614cf19652(
    *,
    cpu_architecture_type: builtins.str,
    memory_mib: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.MemoryMiBRangeProperty, typing.Dict[builtins.str, typing.Any]]],
    os_family: builtins.str,
    v_cpu_count: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.VCpuCountRangeProperty, typing.Dict[builtins.str, typing.Any]]],
    accelerator_count: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AcceleratorCountRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    accelerator_total_memory_mib: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AcceleratorTotalMemoryMiBRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_amounts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetAmountCapabilityProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetAttributeCapabilityProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6b6ee298f17f76c41b442fe1d743f9b23991d0b29f18a1db1e7c2c2c5cd63be(
    *,
    iops: typing.Optional[jsii.Number] = None,
    size_gib: typing.Optional[jsii.Number] = None,
    throughput_mib: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e16e93d244596337be30bf6e8c34bdd5a05f8101356c781ea0ee01c9288890(
    *,
    min: jsii.Number,
    name: builtins.str,
    max: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aecc2f9273876f0a639b5d6f1630dcfd8aca136d3caeaeb82918997f059f3e4(
    *,
    name: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740fdb4badd1a242b2d3b374ef6944877551e5f0eb2de2239a830f3c2028b7b1(
    *,
    amounts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetAmountCapabilityProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetAttributeCapabilityProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ef3ed1850d4005d38d3a6c912a28b59698026461815dad08ff096a4c327a89c(
    *,
    customer_managed: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CustomerManagedFleetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_managed_ec2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ServiceManagedEc2FleetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c49c5364d9d5abab3267eb2a6afca69f203020da3e42493624297dd2a5bf0f(
    *,
    min: jsii.Number,
    max: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24a660b503191048581077a517891d27502b69620643c509073603283a2cb39(
    *,
    instance_capabilities: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ServiceManagedEc2InstanceCapabilitiesProperty, typing.Dict[builtins.str, typing.Any]]],
    instance_market_options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ServiceManagedEc2InstanceMarketOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6bce0a6fe3858a9b9eaa850b95b27731a62d9ef26b45c40b5684d6586ed6996(
    *,
    cpu_architecture_type: builtins.str,
    memory_mib: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.MemoryMiBRangeProperty, typing.Dict[builtins.str, typing.Any]]],
    os_family: builtins.str,
    v_cpu_count: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.VCpuCountRangeProperty, typing.Dict[builtins.str, typing.Any]]],
    allowed_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_amounts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetAmountCapabilityProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetAttributeCapabilityProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    root_ebs_volume: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.Ec2EbsVolumeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8d3a0c18616b5264bff8fa8db0009f71df98b828f0e17e83fea3cc24b4a9443(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcd8ae2a83778ec7a6d7445fcea241d1ce2694a66c1ccc07c23cdd1c8d829c4d(
    *,
    min: jsii.Number,
    max: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1472efddb89af74b2ae4dc1156d30448332099bec47f03ae56886a44d2d7c7a(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.FleetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    display_name: builtins.str,
    max_worker_count: jsii.Number,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    farm_id: typing.Optional[builtins.str] = None,
    min_worker_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2263281bf0506f61e2d06a34042a34c3aa49572fcab3143d4b6c4bc81a62b9a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9aa87cad0472c90e08c8aa1a9c72cc53c01e0cf980555f0f3b357ef4148f041(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6d4dde55dbb1dabd0b1e8734965495af6d2632c3444c0d7c5478f9682cd4a4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b00e03274c83f79c32752b72b984299a4efe64919097bbbdec40f67b386b22(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81d93007bb20eb36480796e83aad3e6a0742393a78a71a87a71f081d070227a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fe095c981d830b60af0a60f921ac267a1eba38300aa520b18fa3678230ddaf7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a9c98d4186629e7162fde16ad1be09ade6a940c8cf979c87af77955e3a39f02(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1349660e6447c1e6551d1ce7cde2c5dc6adbf1fb1fdceb9f214b066a5a6b4ebe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    family: typing.Optional[builtins.str] = None,
    license_endpoint_id: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    product_id: typing.Optional[builtins.str] = None,
    vendor: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d2d01a238f229eb758201d336be8ca9e707d08020ad2910986c804ac3c7809(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed6d8167aeed2952e867a5d1c33ef70cf0763f5978f31bbc292859ff9bb97a0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748584b3e13e6b6b100e3e825e6d4334d2e0c93a3397f0df55aae36a0abdc733(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2392ecb737206631d7a319a666b254d855fea916d5e5430c1cb1bbe9c43d20de(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__866a9b65a442c0e4da725c11f8f3210a936a0cf69a370c376e7d42450692f1c6(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7b3217dc50a692aa63ba3c945affcba562e3dca3ad6c9440d62b98f397be2ac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b31f8edad3d25c952475ac2363b0c1e60099e4c875dc5b54b5e01e1c9a364a59(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64de1639a953ff86a7b38c87a1ecf80a18f6b715e19b894e265cf51c1b6d4920(
    *,
    family: typing.Optional[builtins.str] = None,
    license_endpoint_id: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    product_id: typing.Optional[builtins.str] = None,
    vendor: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8ed104ef6a730c7b90ba82ab4ab0b37d213e5444e12df63d7d60b1e23323e6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    display_name: builtins.str,
    allowed_storage_profile_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_budget_action: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    farm_id: typing.Optional[builtins.str] = None,
    job_attachment_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.JobAttachmentSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_run_as_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.JobRunAsUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_file_system_location_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a951ea75684c1a0e1477adfe4d54001bbe626c602cd5380b6445649ddc198e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12f2ec2b01e12cf5d244b5ae5c7b25018631c87603b7819e99ad82f931094696(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abb08cf6c0a4af9928a3c56fba912abab7cd2c3c4760117e91af2d94f15d5f6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__261c15a318630458194b6ce3058afe2cbf9e193004fd4e7287059f40d08582f2(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ed3fcb26efc70612b9ed8cbcccb35da23ffe53b337b83ec742c863a4da84b6d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2559bfc8e75a5a3fe6743bfc64664fbf4a6fc6cb24717a6669ce9a31c288f44(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fef4d1848bd17d1a655bb4cb1236551eab481ebefcdbbd4e5ae7acc710720145(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358c548fac5f624a3c1d72ec9252063f4d1a9bd3c0342b2e54358d53c0204b5c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.JobAttachmentSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b1f44b18bbd9cd34d33d3fe1de23e5f60be6648dd1ee50efa7531459cd7ae65(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.JobRunAsUserProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d9c178caaac7844afec201e90468fdd98d393162443d88987d2fd5342fb2025(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb5bb7ca40abe81d0cb9afaa09246c4bbb7553021c1125ddbc8a2f83d0da3db(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a91b9031e7181044273ba1904b3e19809ee9a8ab762fe24c5dbe20fcf400ff60(
    *,
    root_prefix: builtins.str,
    s3_bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06247d11c191e79686284edad9440c4d5c7e8038f712251f72b1a60140fbcd14(
    *,
    run_as: builtins.str,
    posix: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.PosixUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    windows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.WindowsUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e675ce01c62a0076a355385ac17aeacd32612beedb164bb4511f338c9a841594(
    *,
    group: builtins.str,
    user: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21f3cd393d77359583c8744ba670e4eb05b1b53d4bba3a35461caec2a91fc9c(
    *,
    password_arn: builtins.str,
    user: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf2ef79ee46780c7590cdcaf16949904d0291a2627b57555ffa860cb355319b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    farm_id: builtins.str,
    priority: jsii.Number,
    queue_id: builtins.str,
    template: builtins.str,
    template_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a6465894d7e168ae6fe30f0f0519094a5d10b4a0db099eaf9e05619574ec819(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4234e955a996a24390a16b9a75175a9e7766aa94cc035cd920a37d37e152197(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee0a8ebb761f1a339ba695cf1c4453345e0569d6f01c23d4df36dd86031814e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462f62b321d72f5a88f323c76e44d85eaa3374e0f6adb3f512104435274114c0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e636e4de083154e3080b3a798c660c93a0d0503ff898703d5f4337707ee40a26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bebb6c72d0cd02e4f9a11ae2664110700bb277dc5fc328e6a9679f00fe106638(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4192f38c45d04e5d9283902f89bf09ebe24569bc7c096f6e34e9a156c7f2896(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea67e4e193bb92e88985247d97314b7feb5f0208ac9f9998cecd35054915fe67(
    *,
    farm_id: builtins.str,
    priority: jsii.Number,
    queue_id: builtins.str,
    template: builtins.str,
    template_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf5f16a9974daab9dba069dab2d83de0ff5b4a6e417026bc9f4c775d17511e6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    farm_id: builtins.str,
    fleet_id: builtins.str,
    queue_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff12ea5f9a70d8e7142807e0c6f13883ba906fa01e1e7887b8de68261b1db16(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e31fddcabe78ead7dcb1221739b2cf550282943452143253d1aba9300c17652(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e19729f1c6fb8ec0c8b6f6c31e0865e9725dd22fc08c9ec2197711d95f5baa21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf8c906b58e9214a10c2d83a1b139049a42f93254fc8ec57da660c71ab58bb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad97a4082938a418ac03725615af17abfdffa0f3dcb8f92815671754e0657141(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5457199586ad5b5517f14765c4203a9a198d98c68deaf06933477e9fcccc9ffb(
    *,
    farm_id: builtins.str,
    fleet_id: builtins.str,
    queue_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a92d64f51023fd5b945aa0d9e2b696749e02f9df358265737e05dd4a730fd30d(
    *,
    display_name: builtins.str,
    allowed_storage_profile_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_budget_action: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    farm_id: typing.Optional[builtins.str] = None,
    job_attachment_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.JobAttachmentSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_run_as_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.JobRunAsUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_file_system_location_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bb4938fbe160a975ec7626f79799d48d7603f2cc166cf513bf1920de8659cb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    display_name: builtins.str,
    os_family: builtins.str,
    farm_id: typing.Optional[builtins.str] = None,
    file_system_locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageProfile.FileSystemLocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2c21ddee6a44d7c3543d169f12db3f66484a191cb97771d03130be960a1dde(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9daf383d7a7e24cea3229e3fe4ee60cad6d86ebd3ae060051973527e9544b1a5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f20c6213a2c65defbfbde8129f9b8c1e7681d519ea98354db0d5bbcf5e03e8d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff32f8bb060d0ada4a6522805c78bae216b6b86ab15b16b64b07a49ae94df357(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f736eedcb6c466af3ef1210e274e369c621b42de8f8102b78a138c4d5cc04f9c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41022fa9902dd4229e3676de8f74c666e01c3237936ce7470d2c1ab45b6055ea(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStorageProfile.FileSystemLocationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30accc33e266fd187349c32faa815a79744e919f16060567a73b75c87e43a574(
    *,
    name: builtins.str,
    path: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d873ae2006c75776847d16361d1b495d51e00d618e49d32a001db4fe2f72991(
    *,
    display_name: builtins.str,
    os_family: builtins.str,
    farm_id: typing.Optional[builtins.str] = None,
    file_system_locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageProfile.FileSystemLocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
