'''
# AWS::IoTWireless Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotwireless as iotwireless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTWireless construct libraries](https://constructs.dev/search?q=iotwireless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTWireless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTWireless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTWireless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTWireless.html).

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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDestination(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnDestination",
):
    '''Creates a new destination that maps a device message to an AWS IoT rule.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
    :cloudformationResource: AWS::IoTWireless::Destination
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_destination = iotwireless.CfnDestination(self, "MyCfnDestination",
            expression="expression",
            expression_type="expressionType",
            name="name",
        
            # the properties below are optional
            description="description",
            role_arn="roleArn",
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
        expression: builtins.str,
        expression_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param expression: The rule name to send messages to.
        :param expression_type: The type of value in ``Expression`` .
        :param name: The name of the new resource.
        :param description: The description of the new resource. Maximum length is 2048 characters.
        :param role_arn: The ARN of the IAM Role that authorizes the destination.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f61ecfaf93e3a5ee3c176667153d7633c25d7bc246a1af5b6801966503ffc10e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDestinationProps(
            expression=expression,
            expression_type=expression_type,
            name=name,
            description=description,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abcdef1ef5b37ae8d863fbd6e43535b7b8fb98b01e8f63d2e11a2ac69ae40d2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__daceed9db31617342b2ad6da1a597d489d32ddd44aa99d40185846a28691e1a6)
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
        '''The ARN of the destination created.

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
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        '''The rule name to send messages to.'''
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0635097b142a55f017574117ff21a283060521e721f605e4ff6e5a9ed13e63d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="expressionType")
    def expression_type(self) -> builtins.str:
        '''The type of value in ``Expression`` .'''
        return typing.cast(builtins.str, jsii.get(self, "expressionType"))

    @expression_type.setter
    def expression_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c52fb059cb57908dccbf654243c0e24547fefae3afcee7f9441366e93f7368f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expressionType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the new resource.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4a7e2be1c3626a0831a317f8384bfaac10f081d96e1d52fdf7e7d168b531e14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54343b07a7027d746812e326d1dd346e2f583fb1042ea98ffa3720e14655d56f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM Role that authorizes the destination.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b60aa4ef5f47c4662f7208269db494d81166701afac30be03ebe87711d08ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28773e7cb2f78fe606bd46c478d428f25a9d6768b2384a0d5eabc8886d06f5d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "expression_type": "expressionType",
        "name": "name",
        "description": "description",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnDestinationProps:
    def __init__(
        self,
        *,
        expression: builtins.str,
        expression_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDestination``.

        :param expression: The rule name to send messages to.
        :param expression_type: The type of value in ``Expression`` .
        :param name: The name of the new resource.
        :param description: The description of the new resource. Maximum length is 2048 characters.
        :param role_arn: The ARN of the IAM Role that authorizes the destination.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_destination_props = iotwireless.CfnDestinationProps(
                expression="expression",
                expression_type="expressionType",
                name="name",
            
                # the properties below are optional
                description="description",
                role_arn="roleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7257e0c4b674f84972a8cd47754e3ce09588804469529ea8a4efd68a9ae0aae)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument expression_type", value=expression_type, expected_type=type_hints["expression_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
            "expression_type": expression_type,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def expression(self) -> builtins.str:
        '''The rule name to send messages to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression_type(self) -> builtins.str:
        '''The type of value in ``Expression`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype
        '''
        result = self._values.get("expression_type")
        assert result is not None, "Required property 'expression_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the new resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        Maximum length is 2048 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM Role that authorizes the destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDeviceProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnDeviceProfile",
):
    '''Creates a new device profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
    :cloudformationResource: AWS::IoTWireless::DeviceProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_device_profile = iotwireless.CfnDeviceProfile(self, "MyCfnDeviceProfile",
            lo_ra_wan=iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty(
                class_bTimeout=123,
                class_cTimeout=123,
                factory_preset_freqs_list=[123],
                mac_version="macVersion",
                max_duty_cycle=123,
                max_eirp=123,
                ping_slot_dr=123,
                ping_slot_freq=123,
                ping_slot_period=123,
                reg_params_revision="regParamsRevision",
                rf_region="rfRegion",
                rx_data_rate2=123,
                rx_delay1=123,
                rx_dr_offset1=123,
                rx_freq2=123,
                supports32_bit_fCnt=False,
                supports_class_b=False,
                supports_class_c=False,
                supports_join=False
            ),
            name="name",
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
        lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param lo_ra_wan: LoRaWAN device profile object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8067f9295f2cbc045aef3949460556f66763c80bd130293a84c601e6d1cc0b67)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeviceProfileProps(lo_ra_wan=lo_ra_wan, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e5a8081b4b2646cf2e301e2afffc795ab7e32d6a6b52b07e5de54e172bbe245)
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
            type_hints = typing.get_type_hints(_typecheckingstub__23fa48b9862be61ca24ddc5be9d3d852c088e91af603908b772a0f6b98d3bb60)
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
        '''The ARN of the device profile created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the device profile created.

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
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeviceProfile.LoRaWANDeviceProfileProperty"]]:
        '''LoRaWAN device profile object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeviceProfile.LoRaWANDeviceProfileProperty"]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeviceProfile.LoRaWANDeviceProfileProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37bc58d63a4729db23e942a768b31134889d07403a53d90d57a88c269501d5fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25caee2a3bcdb77269d5e10d73ce9e629c40f7a63107b51012a8ae652ea849bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4afbd69995e29e676f14b8919081a76892c1a3dd232747696d84a67dd728424a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "class_b_timeout": "classBTimeout",
            "class_c_timeout": "classCTimeout",
            "factory_preset_freqs_list": "factoryPresetFreqsList",
            "mac_version": "macVersion",
            "max_duty_cycle": "maxDutyCycle",
            "max_eirp": "maxEirp",
            "ping_slot_dr": "pingSlotDr",
            "ping_slot_freq": "pingSlotFreq",
            "ping_slot_period": "pingSlotPeriod",
            "reg_params_revision": "regParamsRevision",
            "rf_region": "rfRegion",
            "rx_data_rate2": "rxDataRate2",
            "rx_delay1": "rxDelay1",
            "rx_dr_offset1": "rxDrOffset1",
            "rx_freq2": "rxFreq2",
            "supports32_bit_f_cnt": "supports32BitFCnt",
            "supports_class_b": "supportsClassB",
            "supports_class_c": "supportsClassC",
            "supports_join": "supportsJoin",
        },
    )
    class LoRaWANDeviceProfileProperty:
        def __init__(
            self,
            *,
            class_b_timeout: typing.Optional[jsii.Number] = None,
            class_c_timeout: typing.Optional[jsii.Number] = None,
            factory_preset_freqs_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            mac_version: typing.Optional[builtins.str] = None,
            max_duty_cycle: typing.Optional[jsii.Number] = None,
            max_eirp: typing.Optional[jsii.Number] = None,
            ping_slot_dr: typing.Optional[jsii.Number] = None,
            ping_slot_freq: typing.Optional[jsii.Number] = None,
            ping_slot_period: typing.Optional[jsii.Number] = None,
            reg_params_revision: typing.Optional[builtins.str] = None,
            rf_region: typing.Optional[builtins.str] = None,
            rx_data_rate2: typing.Optional[jsii.Number] = None,
            rx_delay1: typing.Optional[jsii.Number] = None,
            rx_dr_offset1: typing.Optional[jsii.Number] = None,
            rx_freq2: typing.Optional[jsii.Number] = None,
            supports32_bit_f_cnt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            supports_class_b: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            supports_class_c: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            supports_join: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''LoRaWAN device profile object.

            :param class_b_timeout: The ClassBTimeout value.
            :param class_c_timeout: The ClassCTimeout value.
            :param factory_preset_freqs_list: The list of values that make up the FactoryPresetFreqs value. Valid range of values include a minimum value of 1000000 and a maximum value of 16700000.
            :param mac_version: The MAC version (such as OTAA 1.1 or OTAA 1.0.3) to use with this device profile.
            :param max_duty_cycle: The MaxDutyCycle value.
            :param max_eirp: The MaxEIRP value.
            :param ping_slot_dr: The PingSlotDR value.
            :param ping_slot_freq: The PingSlotFreq value.
            :param ping_slot_period: The PingSlotPeriod value.
            :param reg_params_revision: The version of regional parameters.
            :param rf_region: The frequency band (RFRegion) value.
            :param rx_data_rate2: The RXDataRate2 value.
            :param rx_delay1: The RXDelay1 value.
            :param rx_dr_offset1: The RXDROffset1 value.
            :param rx_freq2: The RXFreq2 value.
            :param supports32_bit_f_cnt: The Supports32BitFCnt value.
            :param supports_class_b: The SupportsClassB value.
            :param supports_class_c: The SupportsClassC value.
            :param supports_join: The SupportsJoin value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANDevice_profile_property = iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty(
                    class_bTimeout=123,
                    class_cTimeout=123,
                    factory_preset_freqs_list=[123],
                    mac_version="macVersion",
                    max_duty_cycle=123,
                    max_eirp=123,
                    ping_slot_dr=123,
                    ping_slot_freq=123,
                    ping_slot_period=123,
                    reg_params_revision="regParamsRevision",
                    rf_region="rfRegion",
                    rx_data_rate2=123,
                    rx_delay1=123,
                    rx_dr_offset1=123,
                    rx_freq2=123,
                    supports32_bit_fCnt=False,
                    supports_class_b=False,
                    supports_class_c=False,
                    supports_join=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0558c6321ef1b0db79fd3fb29f490ef770458d60ef008b53201feac226735893)
                check_type(argname="argument class_b_timeout", value=class_b_timeout, expected_type=type_hints["class_b_timeout"])
                check_type(argname="argument class_c_timeout", value=class_c_timeout, expected_type=type_hints["class_c_timeout"])
                check_type(argname="argument factory_preset_freqs_list", value=factory_preset_freqs_list, expected_type=type_hints["factory_preset_freqs_list"])
                check_type(argname="argument mac_version", value=mac_version, expected_type=type_hints["mac_version"])
                check_type(argname="argument max_duty_cycle", value=max_duty_cycle, expected_type=type_hints["max_duty_cycle"])
                check_type(argname="argument max_eirp", value=max_eirp, expected_type=type_hints["max_eirp"])
                check_type(argname="argument ping_slot_dr", value=ping_slot_dr, expected_type=type_hints["ping_slot_dr"])
                check_type(argname="argument ping_slot_freq", value=ping_slot_freq, expected_type=type_hints["ping_slot_freq"])
                check_type(argname="argument ping_slot_period", value=ping_slot_period, expected_type=type_hints["ping_slot_period"])
                check_type(argname="argument reg_params_revision", value=reg_params_revision, expected_type=type_hints["reg_params_revision"])
                check_type(argname="argument rf_region", value=rf_region, expected_type=type_hints["rf_region"])
                check_type(argname="argument rx_data_rate2", value=rx_data_rate2, expected_type=type_hints["rx_data_rate2"])
                check_type(argname="argument rx_delay1", value=rx_delay1, expected_type=type_hints["rx_delay1"])
                check_type(argname="argument rx_dr_offset1", value=rx_dr_offset1, expected_type=type_hints["rx_dr_offset1"])
                check_type(argname="argument rx_freq2", value=rx_freq2, expected_type=type_hints["rx_freq2"])
                check_type(argname="argument supports32_bit_f_cnt", value=supports32_bit_f_cnt, expected_type=type_hints["supports32_bit_f_cnt"])
                check_type(argname="argument supports_class_b", value=supports_class_b, expected_type=type_hints["supports_class_b"])
                check_type(argname="argument supports_class_c", value=supports_class_c, expected_type=type_hints["supports_class_c"])
                check_type(argname="argument supports_join", value=supports_join, expected_type=type_hints["supports_join"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if class_b_timeout is not None:
                self._values["class_b_timeout"] = class_b_timeout
            if class_c_timeout is not None:
                self._values["class_c_timeout"] = class_c_timeout
            if factory_preset_freqs_list is not None:
                self._values["factory_preset_freqs_list"] = factory_preset_freqs_list
            if mac_version is not None:
                self._values["mac_version"] = mac_version
            if max_duty_cycle is not None:
                self._values["max_duty_cycle"] = max_duty_cycle
            if max_eirp is not None:
                self._values["max_eirp"] = max_eirp
            if ping_slot_dr is not None:
                self._values["ping_slot_dr"] = ping_slot_dr
            if ping_slot_freq is not None:
                self._values["ping_slot_freq"] = ping_slot_freq
            if ping_slot_period is not None:
                self._values["ping_slot_period"] = ping_slot_period
            if reg_params_revision is not None:
                self._values["reg_params_revision"] = reg_params_revision
            if rf_region is not None:
                self._values["rf_region"] = rf_region
            if rx_data_rate2 is not None:
                self._values["rx_data_rate2"] = rx_data_rate2
            if rx_delay1 is not None:
                self._values["rx_delay1"] = rx_delay1
            if rx_dr_offset1 is not None:
                self._values["rx_dr_offset1"] = rx_dr_offset1
            if rx_freq2 is not None:
                self._values["rx_freq2"] = rx_freq2
            if supports32_bit_f_cnt is not None:
                self._values["supports32_bit_f_cnt"] = supports32_bit_f_cnt
            if supports_class_b is not None:
                self._values["supports_class_b"] = supports_class_b
            if supports_class_c is not None:
                self._values["supports_class_c"] = supports_class_c
            if supports_join is not None:
                self._values["supports_join"] = supports_join

        @builtins.property
        def class_b_timeout(self) -> typing.Optional[jsii.Number]:
            '''The ClassBTimeout value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout
            '''
            result = self._values.get("class_b_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def class_c_timeout(self) -> typing.Optional[jsii.Number]:
            '''The ClassCTimeout value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout
            '''
            result = self._values.get("class_c_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def factory_preset_freqs_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''The list of values that make up the FactoryPresetFreqs value.

            Valid range of values include a minimum value of 1000000 and a maximum value of 16700000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-factorypresetfreqslist
            '''
            result = self._values.get("factory_preset_freqs_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def mac_version(self) -> typing.Optional[builtins.str]:
            '''The MAC version (such as OTAA 1.1 or OTAA 1.0.3) to use with this device profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion
            '''
            result = self._values.get("mac_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_duty_cycle(self) -> typing.Optional[jsii.Number]:
            '''The MaxDutyCycle value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle
            '''
            result = self._values.get("max_duty_cycle")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_eirp(self) -> typing.Optional[jsii.Number]:
            '''The MaxEIRP value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp
            '''
            result = self._values.get("max_eirp")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_dr(self) -> typing.Optional[jsii.Number]:
            '''The PingSlotDR value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr
            '''
            result = self._values.get("ping_slot_dr")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_freq(self) -> typing.Optional[jsii.Number]:
            '''The PingSlotFreq value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq
            '''
            result = self._values.get("ping_slot_freq")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_period(self) -> typing.Optional[jsii.Number]:
            '''The PingSlotPeriod value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod
            '''
            result = self._values.get("ping_slot_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def reg_params_revision(self) -> typing.Optional[builtins.str]:
            '''The version of regional parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision
            '''
            result = self._values.get("reg_params_revision")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rf_region(self) -> typing.Optional[builtins.str]:
            '''The frequency band (RFRegion) value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion
            '''
            result = self._values.get("rf_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rx_data_rate2(self) -> typing.Optional[jsii.Number]:
            '''The RXDataRate2 value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdatarate2
            '''
            result = self._values.get("rx_data_rate2")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rx_delay1(self) -> typing.Optional[jsii.Number]:
            '''The RXDelay1 value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdelay1
            '''
            result = self._values.get("rx_delay1")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rx_dr_offset1(self) -> typing.Optional[jsii.Number]:
            '''The RXDROffset1 value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdroffset1
            '''
            result = self._values.get("rx_dr_offset1")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rx_freq2(self) -> typing.Optional[jsii.Number]:
            '''The RXFreq2 value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxfreq2
            '''
            result = self._values.get("rx_freq2")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def supports32_bit_f_cnt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The Supports32BitFCnt value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt
            '''
            result = self._values.get("supports32_bit_f_cnt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def supports_class_b(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The SupportsClassB value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb
            '''
            result = self._values.get("supports_class_b")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def supports_class_c(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The SupportsClassC value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc
            '''
            result = self._values.get("supports_class_c")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def supports_join(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The SupportsJoin value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin
            '''
            result = self._values.get("supports_join")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANDeviceProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnDeviceProfileProps",
    jsii_struct_bases=[],
    name_mapping={"lo_ra_wan": "loRaWan", "name": "name", "tags": "tags"},
)
class CfnDeviceProfileProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeviceProfile``.

        :param lo_ra_wan: LoRaWAN device profile object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_device_profile_props = iotwireless.CfnDeviceProfileProps(
                lo_ra_wan=iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty(
                    class_bTimeout=123,
                    class_cTimeout=123,
                    factory_preset_freqs_list=[123],
                    mac_version="macVersion",
                    max_duty_cycle=123,
                    max_eirp=123,
                    ping_slot_dr=123,
                    ping_slot_freq=123,
                    ping_slot_period=123,
                    reg_params_revision="regParamsRevision",
                    rf_region="rfRegion",
                    rx_data_rate2=123,
                    rx_delay1=123,
                    rx_dr_offset1=123,
                    rx_freq2=123,
                    supports32_bit_fCnt=False,
                    supports_class_b=False,
                    supports_class_c=False,
                    supports_join=False
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5943b1bf4799db06aae66d299d5e86b23f1003e16376a69594302b4e4054ee8)
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeviceProfile.LoRaWANDeviceProfileProperty]]:
        '''LoRaWAN device profile object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeviceProfile.LoRaWANDeviceProfileProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFuotaTask(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnFuotaTask",
):
    '''A FUOTA task.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html
    :cloudformationResource: AWS::IoTWireless::FuotaTask
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_fuota_task = iotwireless.CfnFuotaTask(self, "MyCfnFuotaTask",
            firmware_update_image="firmwareUpdateImage",
            firmware_update_role="firmwareUpdateRole",
            lo_ra_wan=iotwireless.CfnFuotaTask.LoRaWANProperty(
                rf_region="rfRegion",
        
                # the properties below are optional
                start_time="startTime"
            ),
        
            # the properties below are optional
            associate_multicast_group="associateMulticastGroup",
            associate_wireless_device="associateWirelessDevice",
            description="description",
            disassociate_multicast_group="disassociateMulticastGroup",
            disassociate_wireless_device="disassociateWirelessDevice",
            name="name",
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
        firmware_update_image: builtins.str,
        firmware_update_role: builtins.str,
        lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFuotaTask.LoRaWANProperty", typing.Dict[builtins.str, typing.Any]]],
        associate_multicast_group: typing.Optional[builtins.str] = None,
        associate_wireless_device: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disassociate_multicast_group: typing.Optional[builtins.str] = None,
        disassociate_wireless_device: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param firmware_update_image: The S3 URI points to a firmware update image that is to be used with a FUOTA task.
        :param firmware_update_role: The firmware update role that is to be used with a FUOTA task.
        :param lo_ra_wan: The LoRaWAN information used with a FUOTA task.
        :param associate_multicast_group: The ID of the multicast group to associate with a FUOTA task.
        :param associate_wireless_device: The ID of the wireless device to associate with a multicast group.
        :param description: The description of the new resource.
        :param disassociate_multicast_group: The ID of the multicast group to disassociate from a FUOTA task.
        :param disassociate_wireless_device: The ID of the wireless device to disassociate from a FUOTA task.
        :param name: The name of a FUOTA task.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dc14d9e108784569e33639b9546be6bf6547039fdbf1476a6e6dc24a391c8ec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFuotaTaskProps(
            firmware_update_image=firmware_update_image,
            firmware_update_role=firmware_update_role,
            lo_ra_wan=lo_ra_wan,
            associate_multicast_group=associate_multicast_group,
            associate_wireless_device=associate_wireless_device,
            description=description,
            disassociate_multicast_group=disassociate_multicast_group,
            disassociate_wireless_device=disassociate_wireless_device,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b980d91ff24dc028c16177ae311632139802ed07c63559bc60b6b0a7017f8724)
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
            type_hints = typing.get_type_hints(_typecheckingstub__35e7b39665fb6873e720d392fdd079f7eb20ed523e0aa7f027788b71f4f36fa0)
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
        '''The ARN of a FUOTA task.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFuotaTaskStatus")
    def attr_fuota_task_status(self) -> builtins.str:
        '''The status of a FUOTA task.

        :cloudformationAttribute: FuotaTaskStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFuotaTaskStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of a FUOTA task.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanStartTime")
    def attr_lo_ra_wan_start_time(self) -> builtins.str:
        '''Start time of a FUOTA task.

        :cloudformationAttribute: LoRaWAN.StartTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanStartTime"))

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
    @jsii.member(jsii_name="firmwareUpdateImage")
    def firmware_update_image(self) -> builtins.str:
        '''The S3 URI points to a firmware update image that is to be used with a FUOTA task.'''
        return typing.cast(builtins.str, jsii.get(self, "firmwareUpdateImage"))

    @firmware_update_image.setter
    def firmware_update_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c1e683ef261ca9a0e323098857bde336b7b232a1debbe4ce45dedb26ca8745)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firmwareUpdateImage", value)

    @builtins.property
    @jsii.member(jsii_name="firmwareUpdateRole")
    def firmware_update_role(self) -> builtins.str:
        '''The firmware update role that is to be used with a FUOTA task.'''
        return typing.cast(builtins.str, jsii.get(self, "firmwareUpdateRole"))

    @firmware_update_role.setter
    def firmware_update_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__461c299fc6e5ef170d9d68ec3a0d4fd23e292ad17e487e422fa0ced5654b660c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firmwareUpdateRole", value)

    @builtins.property
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnFuotaTask.LoRaWANProperty"]:
        '''The LoRaWAN information used with a FUOTA task.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFuotaTask.LoRaWANProperty"], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFuotaTask.LoRaWANProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ced8500df8e27b1785fe0afc435e424754dde0dc634914ed9fd44ab5b30ce8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="associateMulticastGroup")
    def associate_multicast_group(self) -> typing.Optional[builtins.str]:
        '''The ID of the multicast group to associate with a FUOTA task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associateMulticastGroup"))

    @associate_multicast_group.setter
    def associate_multicast_group(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d57cfccba3878e495806e2629c1b347cbfd7e7defe8b5465dd6bb995d141ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateMulticastGroup", value)

    @builtins.property
    @jsii.member(jsii_name="associateWirelessDevice")
    def associate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to associate with a multicast group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associateWirelessDevice"))

    @associate_wireless_device.setter
    def associate_wireless_device(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__379374179bd98cbed6826061ba79e2ccdcb8f9d331dfad677cfb8ed97f739ee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateWirelessDevice", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd259b9067a68c41327baaabf15d262b9fb84d09030f1cf4a7f0dd8e202ee92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disassociateMulticastGroup")
    def disassociate_multicast_group(self) -> typing.Optional[builtins.str]:
        '''The ID of the multicast group to disassociate from a FUOTA task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disassociateMulticastGroup"))

    @disassociate_multicast_group.setter
    def disassociate_multicast_group(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c01c498cd349d14eb10d07e4f5e44c09c897b78b93d259561e5a16ba5e042381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disassociateMulticastGroup", value)

    @builtins.property
    @jsii.member(jsii_name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to disassociate from a FUOTA task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disassociateWirelessDevice"))

    @disassociate_wireless_device.setter
    def disassociate_wireless_device(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9cb4e1ac40f6c4cb8557e33d35c0e1b17c7dca5a1e5af474d269743b81f4c32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disassociateWirelessDevice", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of a FUOTA task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eacacaf44fc0b79b61f7bfe0ff15f515d32d411b03d265dc1950da37d4e1df4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af87398fea4c8098bb165637d1ed67059206096bfeaa74f0f7e4bc4f155438a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnFuotaTask.LoRaWANProperty",
        jsii_struct_bases=[],
        name_mapping={"rf_region": "rfRegion", "start_time": "startTime"},
    )
    class LoRaWANProperty:
        def __init__(
            self,
            *,
            rf_region: builtins.str,
            start_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The LoRaWAN information used with a FUOTA task.

            :param rf_region: The frequency band (RFRegion) value.
            :param start_time: Start time of a FUOTA task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANProperty = iotwireless.CfnFuotaTask.LoRaWANProperty(
                    rf_region="rfRegion",
                
                    # the properties below are optional
                    start_time="startTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a94393e5e1d51d161120515f2e9774caa190b7efe4ebfe8fa4779de1b04a5107)
                check_type(argname="argument rf_region", value=rf_region, expected_type=type_hints["rf_region"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rf_region": rf_region,
            }
            if start_time is not None:
                self._values["start_time"] = start_time

        @builtins.property
        def rf_region(self) -> builtins.str:
            '''The frequency band (RFRegion) value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-rfregion
            '''
            result = self._values.get("rf_region")
            assert result is not None, "Required property 'rf_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(self) -> typing.Optional[builtins.str]:
            '''Start time of a FUOTA task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnFuotaTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "firmware_update_image": "firmwareUpdateImage",
        "firmware_update_role": "firmwareUpdateRole",
        "lo_ra_wan": "loRaWan",
        "associate_multicast_group": "associateMulticastGroup",
        "associate_wireless_device": "associateWirelessDevice",
        "description": "description",
        "disassociate_multicast_group": "disassociateMulticastGroup",
        "disassociate_wireless_device": "disassociateWirelessDevice",
        "name": "name",
        "tags": "tags",
    },
)
class CfnFuotaTaskProps:
    def __init__(
        self,
        *,
        firmware_update_image: builtins.str,
        firmware_update_role: builtins.str,
        lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFuotaTask.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
        associate_multicast_group: typing.Optional[builtins.str] = None,
        associate_wireless_device: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disassociate_multicast_group: typing.Optional[builtins.str] = None,
        disassociate_wireless_device: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFuotaTask``.

        :param firmware_update_image: The S3 URI points to a firmware update image that is to be used with a FUOTA task.
        :param firmware_update_role: The firmware update role that is to be used with a FUOTA task.
        :param lo_ra_wan: The LoRaWAN information used with a FUOTA task.
        :param associate_multicast_group: The ID of the multicast group to associate with a FUOTA task.
        :param associate_wireless_device: The ID of the wireless device to associate with a multicast group.
        :param description: The description of the new resource.
        :param disassociate_multicast_group: The ID of the multicast group to disassociate from a FUOTA task.
        :param disassociate_wireless_device: The ID of the wireless device to disassociate from a FUOTA task.
        :param name: The name of a FUOTA task.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_fuota_task_props = iotwireless.CfnFuotaTaskProps(
                firmware_update_image="firmwareUpdateImage",
                firmware_update_role="firmwareUpdateRole",
                lo_ra_wan=iotwireless.CfnFuotaTask.LoRaWANProperty(
                    rf_region="rfRegion",
            
                    # the properties below are optional
                    start_time="startTime"
                ),
            
                # the properties below are optional
                associate_multicast_group="associateMulticastGroup",
                associate_wireless_device="associateWirelessDevice",
                description="description",
                disassociate_multicast_group="disassociateMulticastGroup",
                disassociate_wireless_device="disassociateWirelessDevice",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1c3e107aa1ac02161284f43f789dead141c5600532a3e5692ad63f38b6fe334)
            check_type(argname="argument firmware_update_image", value=firmware_update_image, expected_type=type_hints["firmware_update_image"])
            check_type(argname="argument firmware_update_role", value=firmware_update_role, expected_type=type_hints["firmware_update_role"])
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument associate_multicast_group", value=associate_multicast_group, expected_type=type_hints["associate_multicast_group"])
            check_type(argname="argument associate_wireless_device", value=associate_wireless_device, expected_type=type_hints["associate_wireless_device"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disassociate_multicast_group", value=disassociate_multicast_group, expected_type=type_hints["disassociate_multicast_group"])
            check_type(argname="argument disassociate_wireless_device", value=disassociate_wireless_device, expected_type=type_hints["disassociate_wireless_device"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firmware_update_image": firmware_update_image,
            "firmware_update_role": firmware_update_role,
            "lo_ra_wan": lo_ra_wan,
        }
        if associate_multicast_group is not None:
            self._values["associate_multicast_group"] = associate_multicast_group
        if associate_wireless_device is not None:
            self._values["associate_wireless_device"] = associate_wireless_device
        if description is not None:
            self._values["description"] = description
        if disassociate_multicast_group is not None:
            self._values["disassociate_multicast_group"] = disassociate_multicast_group
        if disassociate_wireless_device is not None:
            self._values["disassociate_wireless_device"] = disassociate_wireless_device
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firmware_update_image(self) -> builtins.str:
        '''The S3 URI points to a firmware update image that is to be used with a FUOTA task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdateimage
        '''
        result = self._values.get("firmware_update_image")
        assert result is not None, "Required property 'firmware_update_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firmware_update_role(self) -> builtins.str:
        '''The firmware update role that is to be used with a FUOTA task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdaterole
        '''
        result = self._values.get("firmware_update_role")
        assert result is not None, "Required property 'firmware_update_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnFuotaTask.LoRaWANProperty]:
        '''The LoRaWAN information used with a FUOTA task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        assert result is not None, "Required property 'lo_ra_wan' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFuotaTask.LoRaWANProperty], result)

    @builtins.property
    def associate_multicast_group(self) -> typing.Optional[builtins.str]:
        '''The ID of the multicast group to associate with a FUOTA task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatemulticastgroup
        '''
        result = self._values.get("associate_multicast_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def associate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to associate with a multicast group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatewirelessdevice
        '''
        result = self._values.get("associate_wireless_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disassociate_multicast_group(self) -> typing.Optional[builtins.str]:
        '''The ID of the multicast group to disassociate from a FUOTA task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatemulticastgroup
        '''
        result = self._values.get("disassociate_multicast_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disassociate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to disassociate from a FUOTA task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatewirelessdevice
        '''
        result = self._values.get("disassociate_wireless_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of a FUOTA task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFuotaTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMulticastGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnMulticastGroup",
):
    '''A multicast group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html
    :cloudformationResource: AWS::IoTWireless::MulticastGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_multicast_group = iotwireless.CfnMulticastGroup(self, "MyCfnMulticastGroup",
            lo_ra_wan=iotwireless.CfnMulticastGroup.LoRaWANProperty(
                dl_class="dlClass",
                rf_region="rfRegion",
        
                # the properties below are optional
                number_of_devices_in_group=123,
                number_of_devices_requested=123
            ),
        
            # the properties below are optional
            associate_wireless_device="associateWirelessDevice",
            description="description",
            disassociate_wireless_device="disassociateWirelessDevice",
            name="name",
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
        lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMulticastGroup.LoRaWANProperty", typing.Dict[builtins.str, typing.Any]]],
        associate_wireless_device: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disassociate_wireless_device: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param lo_ra_wan: The LoRaWAN information that is to be used with the multicast group.
        :param associate_wireless_device: The ID of the wireless device to associate with a multicast group.
        :param description: The description of the multicast group.
        :param disassociate_wireless_device: The ID of the wireless device to disassociate from a multicast group.
        :param name: The name of the multicast group.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6fc3915d7fdc89e5cd965ebe2f8ae8013d87d86fae4860debc0123a0b130f24)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMulticastGroupProps(
            lo_ra_wan=lo_ra_wan,
            associate_wireless_device=associate_wireless_device,
            description=description,
            disassociate_wireless_device=disassociate_wireless_device,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ea85117dcaae87f7c258e9db5b97562bfa9d3134ac4257066b0b99c150b670a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fcd2888d21219d187de015a688eab431ac6138768b481256a7336154497d286)
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
        '''The ARN of the multicast group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the multicast group.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanNumberOfDevicesInGroup")
    def attr_lo_ra_wan_number_of_devices_in_group(self) -> jsii.Number:
        '''The number of devices that are associated to the multicast group.

        :cloudformationAttribute: LoRaWAN.NumberOfDevicesInGroup
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanNumberOfDevicesInGroup"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanNumberOfDevicesRequested")
    def attr_lo_ra_wan_number_of_devices_requested(self) -> jsii.Number:
        '''The number of devices that are requested to be associated with the multicast group.

        :cloudformationAttribute: LoRaWAN.NumberOfDevicesRequested
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanNumberOfDevicesRequested"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of a multicast group.

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
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnMulticastGroup.LoRaWANProperty"]:
        '''The LoRaWAN information that is to be used with the multicast group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMulticastGroup.LoRaWANProperty"], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnMulticastGroup.LoRaWANProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c294e487d95b07e085a91c7f8a13feb7802783382655634e559a8b45c99c8ed1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="associateWirelessDevice")
    def associate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to associate with a multicast group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associateWirelessDevice"))

    @associate_wireless_device.setter
    def associate_wireless_device(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae2c095360e3b3956ec27a5a0391c8b9c6a1066c9419e78b18a128b1dce39cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateWirelessDevice", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the multicast group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8546711d1c48df42c3459de0d74a8bd074a39920589e487cf369cb45db970959)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to disassociate from a multicast group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disassociateWirelessDevice"))

    @disassociate_wireless_device.setter
    def disassociate_wireless_device(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c14cccbedbde81f7eab76271cf8904f266f0740eeae3b16d6d56f4c841f9bf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disassociateWirelessDevice", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the multicast group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9827482ae6bbc3367a4ad1ad70db1f6720ac74a9a8bff8d777c1b9974f2a0c22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27a605465487f3c8166eed5c794a991aa0323a4e726e6135514d21538a40f38a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnMulticastGroup.LoRaWANProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dl_class": "dlClass",
            "rf_region": "rfRegion",
            "number_of_devices_in_group": "numberOfDevicesInGroup",
            "number_of_devices_requested": "numberOfDevicesRequested",
        },
    )
    class LoRaWANProperty:
        def __init__(
            self,
            *,
            dl_class: builtins.str,
            rf_region: builtins.str,
            number_of_devices_in_group: typing.Optional[jsii.Number] = None,
            number_of_devices_requested: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The LoRaWAN information that is to be used with the multicast group.

            :param dl_class: DlClass for LoRaWAN. Valid values are ClassB and ClassC.
            :param rf_region: The frequency band (RFRegion) value.
            :param number_of_devices_in_group: Number of devices that are associated to the multicast group.
            :param number_of_devices_requested: Number of devices that are requested to be associated with the multicast group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANProperty = iotwireless.CfnMulticastGroup.LoRaWANProperty(
                    dl_class="dlClass",
                    rf_region="rfRegion",
                
                    # the properties below are optional
                    number_of_devices_in_group=123,
                    number_of_devices_requested=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a226fea2e98276efaf2b644d1722fe1463b41172c734829c58e4752c3acd34f5)
                check_type(argname="argument dl_class", value=dl_class, expected_type=type_hints["dl_class"])
                check_type(argname="argument rf_region", value=rf_region, expected_type=type_hints["rf_region"])
                check_type(argname="argument number_of_devices_in_group", value=number_of_devices_in_group, expected_type=type_hints["number_of_devices_in_group"])
                check_type(argname="argument number_of_devices_requested", value=number_of_devices_requested, expected_type=type_hints["number_of_devices_requested"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dl_class": dl_class,
                "rf_region": rf_region,
            }
            if number_of_devices_in_group is not None:
                self._values["number_of_devices_in_group"] = number_of_devices_in_group
            if number_of_devices_requested is not None:
                self._values["number_of_devices_requested"] = number_of_devices_requested

        @builtins.property
        def dl_class(self) -> builtins.str:
            '''DlClass for LoRaWAN.

            Valid values are ClassB and ClassC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-dlclass
            '''
            result = self._values.get("dl_class")
            assert result is not None, "Required property 'dl_class' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rf_region(self) -> builtins.str:
            '''The frequency band (RFRegion) value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-rfregion
            '''
            result = self._values.get("rf_region")
            assert result is not None, "Required property 'rf_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def number_of_devices_in_group(self) -> typing.Optional[jsii.Number]:
            '''Number of devices that are associated to the multicast group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesingroup
            '''
            result = self._values.get("number_of_devices_in_group")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def number_of_devices_requested(self) -> typing.Optional[jsii.Number]:
            '''Number of devices that are requested to be associated with the multicast group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesrequested
            '''
            result = self._values.get("number_of_devices_requested")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnMulticastGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "lo_ra_wan": "loRaWan",
        "associate_wireless_device": "associateWirelessDevice",
        "description": "description",
        "disassociate_wireless_device": "disassociateWirelessDevice",
        "name": "name",
        "tags": "tags",
    },
)
class CfnMulticastGroupProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMulticastGroup.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
        associate_wireless_device: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disassociate_wireless_device: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMulticastGroup``.

        :param lo_ra_wan: The LoRaWAN information that is to be used with the multicast group.
        :param associate_wireless_device: The ID of the wireless device to associate with a multicast group.
        :param description: The description of the multicast group.
        :param disassociate_wireless_device: The ID of the wireless device to disassociate from a multicast group.
        :param name: The name of the multicast group.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_multicast_group_props = iotwireless.CfnMulticastGroupProps(
                lo_ra_wan=iotwireless.CfnMulticastGroup.LoRaWANProperty(
                    dl_class="dlClass",
                    rf_region="rfRegion",
            
                    # the properties below are optional
                    number_of_devices_in_group=123,
                    number_of_devices_requested=123
                ),
            
                # the properties below are optional
                associate_wireless_device="associateWirelessDevice",
                description="description",
                disassociate_wireless_device="disassociateWirelessDevice",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c4e6fa1a2a0807dcecf7101bb34c083b7ea47e91b475851efefdc2219a41c6d)
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument associate_wireless_device", value=associate_wireless_device, expected_type=type_hints["associate_wireless_device"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disassociate_wireless_device", value=disassociate_wireless_device, expected_type=type_hints["disassociate_wireless_device"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lo_ra_wan": lo_ra_wan,
        }
        if associate_wireless_device is not None:
            self._values["associate_wireless_device"] = associate_wireless_device
        if description is not None:
            self._values["description"] = description
        if disassociate_wireless_device is not None:
            self._values["disassociate_wireless_device"] = disassociate_wireless_device
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnMulticastGroup.LoRaWANProperty]:
        '''The LoRaWAN information that is to be used with the multicast group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        assert result is not None, "Required property 'lo_ra_wan' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnMulticastGroup.LoRaWANProperty], result)

    @builtins.property
    def associate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to associate with a multicast group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-associatewirelessdevice
        '''
        result = self._values.get("associate_wireless_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the multicast group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disassociate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to disassociate from a multicast group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-disassociatewirelessdevice
        '''
        result = self._values.get("disassociate_wireless_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the multicast group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMulticastGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnNetworkAnalyzerConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnNetworkAnalyzerConfiguration",
):
    '''Network analyzer configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html
    :cloudformationResource: AWS::IoTWireless::NetworkAnalyzerConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        # trace_content: Any
        
        cfn_network_analyzer_configuration = iotwireless.CfnNetworkAnalyzerConfiguration(self, "MyCfnNetworkAnalyzerConfiguration",
            name="name",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trace_content=trace_content,
            wireless_devices=["wirelessDevices"],
            wireless_gateways=["wirelessGateways"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trace_content: typing.Any = None,
        wireless_devices: typing.Optional[typing.Sequence[builtins.str]] = None,
        wireless_gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Name of the network analyzer configuration.
        :param description: The description of the resource.
        :param tags: The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.
        :param trace_content: Trace content for your wireless gateway and wireless device resources.
        :param wireless_devices: Wireless device resources to add to the network analyzer configuration. Provide the ``WirelessDeviceId`` of the resource to add in the input array.
        :param wireless_gateways: Wireless gateway resources to add to the network analyzer configuration. Provide the ``WirelessGatewayId`` of the resource to add in the input array.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef76e8561696d18827326b858a29c7a5bd71d6c55e2e8bf310bff5db6a892786)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNetworkAnalyzerConfigurationProps(
            name=name,
            description=description,
            tags=tags,
            trace_content=trace_content,
            wireless_devices=wireless_devices,
            wireless_gateways=wireless_gateways,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb735453542fc1eee5534899adaa88277e0a12f532d40466da5d9007b540f43c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89d3ff277ab1c23aa596a504d2383a5cf86d5bc2401250de37145267f78d0739)
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
        '''The Amazon Resource Name (ARN) of the resource.

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the network analyzer configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c86a3d802557338c300cca0ece6752eb71025ac87c6ef07829166d2ff477df9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93e1a9911115880ebf27f7267ad38fa5bce7c66abe33ebbe75b2bf22eabf9156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b46f409840f000384f5933335a3a3f6ca1fc64ffa82bf977e2ecf1eab8bb21e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="traceContent")
    def trace_content(self) -> typing.Any:
        '''Trace content for your wireless gateway and wireless device resources.'''
        return typing.cast(typing.Any, jsii.get(self, "traceContent"))

    @trace_content.setter
    def trace_content(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec63757a5145f99a0f5ef3d5b25bbe5becfee81e77d099ee2f39369f195858f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "traceContent", value)

    @builtins.property
    @jsii.member(jsii_name="wirelessDevices")
    def wireless_devices(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Wireless device resources to add to the network analyzer configuration.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "wirelessDevices"))

    @wireless_devices.setter
    def wireless_devices(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__345530c2c6feaa99816a9ee99013b64ff606afb8afa94b821fff9b5acdaf603b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wirelessDevices", value)

    @builtins.property
    @jsii.member(jsii_name="wirelessGateways")
    def wireless_gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Wireless gateway resources to add to the network analyzer configuration.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "wirelessGateways"))

    @wireless_gateways.setter
    def wireless_gateways(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a89da82bb29c60f2cbd481009d94f8a49db119e080583ebad6fe6b40308f21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wirelessGateways", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnNetworkAnalyzerConfiguration.TraceContentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_level": "logLevel",
            "wireless_device_frame_info": "wirelessDeviceFrameInfo",
        },
    )
    class TraceContentProperty:
        def __init__(
            self,
            *,
            log_level: typing.Optional[builtins.str] = None,
            wireless_device_frame_info: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Trace content for your wireless gateway and wireless device resources.

            :param log_level: The log level for a log message. The log levels can be disabled, or set to ``ERROR`` to display less verbose logs containing only error information, or to ``INFO`` for more detailed logs
            :param wireless_device_frame_info: ``FrameInfo`` of your wireless device resources for the trace content. Use FrameInfo to debug the communication between your LoRaWAN end devices and the network server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                trace_content_property = iotwireless.CfnNetworkAnalyzerConfiguration.TraceContentProperty(
                    log_level="logLevel",
                    wireless_device_frame_info="wirelessDeviceFrameInfo"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__45bcacb642e8b830d381b062a8db3fed1fc9995b8d0083e17def729766ceaa1f)
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
                check_type(argname="argument wireless_device_frame_info", value=wireless_device_frame_info, expected_type=type_hints["wireless_device_frame_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_level is not None:
                self._values["log_level"] = log_level
            if wireless_device_frame_info is not None:
                self._values["wireless_device_frame_info"] = wireless_device_frame_info

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''The log level for a log message.

            The log levels can be disabled, or set to ``ERROR`` to display less verbose logs containing only error information, or to ``INFO`` for more detailed logs

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def wireless_device_frame_info(self) -> typing.Optional[builtins.str]:
            '''``FrameInfo`` of your wireless device resources for the trace content.

            Use FrameInfo to debug the communication between your LoRaWAN end devices and the network server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-wirelessdeviceframeinfo
            '''
            result = self._values.get("wireless_device_frame_info")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TraceContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnNetworkAnalyzerConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "tags": "tags",
        "trace_content": "traceContent",
        "wireless_devices": "wirelessDevices",
        "wireless_gateways": "wirelessGateways",
    },
)
class CfnNetworkAnalyzerConfigurationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trace_content: typing.Any = None,
        wireless_devices: typing.Optional[typing.Sequence[builtins.str]] = None,
        wireless_gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnNetworkAnalyzerConfiguration``.

        :param name: Name of the network analyzer configuration.
        :param description: The description of the resource.
        :param tags: The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.
        :param trace_content: Trace content for your wireless gateway and wireless device resources.
        :param wireless_devices: Wireless device resources to add to the network analyzer configuration. Provide the ``WirelessDeviceId`` of the resource to add in the input array.
        :param wireless_gateways: Wireless gateway resources to add to the network analyzer configuration. Provide the ``WirelessGatewayId`` of the resource to add in the input array.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            # trace_content: Any
            
            cfn_network_analyzer_configuration_props = iotwireless.CfnNetworkAnalyzerConfigurationProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trace_content=trace_content,
                wireless_devices=["wirelessDevices"],
                wireless_gateways=["wirelessGateways"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de35d2504c45d0e78e2b671e6fad33a1e14e8aa548b7e508caaa7a23bf523bd5)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trace_content", value=trace_content, expected_type=type_hints["trace_content"])
            check_type(argname="argument wireless_devices", value=wireless_devices, expected_type=type_hints["wireless_devices"])
            check_type(argname="argument wireless_gateways", value=wireless_gateways, expected_type=type_hints["wireless_gateways"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if trace_content is not None:
            self._values["trace_content"] = trace_content
        if wireless_devices is not None:
            self._values["wireless_devices"] = wireless_devices
        if wireless_gateways is not None:
            self._values["wireless_gateways"] = wireless_gateways

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the network analyzer configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the specified resource.

        Tags are metadata that you can use to manage a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def trace_content(self) -> typing.Any:
        '''Trace content for your wireless gateway and wireless device resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent
        '''
        result = self._values.get("trace_content")
        return typing.cast(typing.Any, result)

    @builtins.property
    def wireless_devices(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Wireless device resources to add to the network analyzer configuration.

        Provide the ``WirelessDeviceId`` of the resource to add in the input array.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-wirelessdevices
        '''
        result = self._values.get("wireless_devices")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wireless_gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Wireless gateway resources to add to the network analyzer configuration.

        Provide the ``WirelessGatewayId`` of the resource to add in the input array.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-wirelessgateways
        '''
        result = self._values.get("wireless_gateways")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkAnalyzerConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPartnerAccount(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnPartnerAccount",
):
    '''A partner account.

    If ``PartnerAccountId`` and ``PartnerType`` are ``null`` , returns all partner accounts.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html
    :cloudformationResource: AWS::IoTWireless::PartnerAccount
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_partner_account = iotwireless.CfnPartnerAccount(self, "MyCfnPartnerAccount",
            account_linked=False,
            partner_account_id="partnerAccountId",
            partner_type="partnerType",
            sidewalk=iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty(
                app_server_private_key="appServerPrivateKey"
            ),
            sidewalk_response=iotwireless.CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty(
                amazon_id="amazonId",
                arn="arn",
                fingerprint="fingerprint"
            ),
            sidewalk_update=iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty(
                app_server_private_key="appServerPrivateKey"
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
        account_linked: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        partner_account_id: typing.Optional[builtins.str] = None,
        partner_type: typing.Optional[builtins.str] = None,
        sidewalk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnerAccount.SidewalkAccountInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sidewalk_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sidewalk_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnerAccount.SidewalkUpdateAccountProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account_linked: Whether the partner account is linked to the AWS account.
        :param partner_account_id: The ID of the partner account to update.
        :param partner_type: The partner type.
        :param sidewalk: The Sidewalk account credentials.
        :param sidewalk_response: Information about a Sidewalk account.
        :param sidewalk_update: Sidewalk update.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23050117a6e6495f26306a5fff82479bd5fc0476b02f8ebd675aaba8825caf23)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPartnerAccountProps(
            account_linked=account_linked,
            partner_account_id=partner_account_id,
            partner_type=partner_type,
            sidewalk=sidewalk,
            sidewalk_response=sidewalk_response,
            sidewalk_update=sidewalk_update,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__614820e59436cd5cb89f1931fa964da150fbdf2e6b823323674e6cef8ab4bb79)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7087c5f1c74d1220271f38d1f9ff76843a565709c5a8c4011156d03dc8163b3a)
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
        '''The Amazon Resource Name (ARN) of the resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFingerprint")
    def attr_fingerprint(self) -> builtins.str:
        '''The fingerprint of the Sidewalk application server private key.

        :cloudformationAttribute: Fingerprint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFingerprint"))

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
    @jsii.member(jsii_name="accountLinked")
    def account_linked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the partner account is linked to the AWS account.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "accountLinked"))

    @account_linked.setter
    def account_linked(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aaf826ad1c2a370b17963e90c6207f7bb7314d3e7dc5cae931ff248746ba3fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountLinked", value)

    @builtins.property
    @jsii.member(jsii_name="partnerAccountId")
    def partner_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the partner account to update.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerAccountId"))

    @partner_account_id.setter
    def partner_account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3e0bac11a48ea18aaab6b58e90043f92d7be541f658cdee62741f6c3c496ad6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partnerAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="partnerType")
    def partner_type(self) -> typing.Optional[builtins.str]:
        '''The partner type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerType"))

    @partner_type.setter
    def partner_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b67a184faefbbc21a96bb714ed21601a9e1f59ee99b131697db7927e94ab59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partnerType", value)

    @builtins.property
    @jsii.member(jsii_name="sidewalk")
    def sidewalk(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkAccountInfoProperty"]]:
        '''The Sidewalk account credentials.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkAccountInfoProperty"]], jsii.get(self, "sidewalk"))

    @sidewalk.setter
    def sidewalk(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkAccountInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dfc9914aae89e0f8eb197d8ffe2bc096aa60a82245d8f1a8724edd051f7d100)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sidewalk", value)

    @builtins.property
    @jsii.member(jsii_name="sidewalkResponse")
    def sidewalk_response(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty"]]:
        '''Information about a Sidewalk account.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty"]], jsii.get(self, "sidewalkResponse"))

    @sidewalk_response.setter
    def sidewalk_response(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe1611d5cb899b19b3746136128a84710ec89f4b9d8628afa53281d1714b6abb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sidewalkResponse", value)

    @builtins.property
    @jsii.member(jsii_name="sidewalkUpdate")
    def sidewalk_update(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]]:
        '''Sidewalk update.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]], jsii.get(self, "sidewalkUpdate"))

    @sidewalk_update.setter
    def sidewalk_update(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e0971bf93851f4e3f9a7278252a08cda6e44ea93a8e7a0b793f3aa5bc028fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sidewalkUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5c265354d811dc09b785b9e46927998e11bca13038834b76f0874d18d38cfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"app_server_private_key": "appServerPrivateKey"},
    )
    class SidewalkAccountInfoProperty:
        def __init__(self, *, app_server_private_key: builtins.str) -> None:
            '''Information about a Sidewalk account.

            :param app_server_private_key: The Sidewalk application server private key. The application server private key is a secret key, which you should handle in a similar way as you would an application password. You can protect the application server private key by storing the value in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                sidewalk_account_info_property = iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty(
                    app_server_private_key="appServerPrivateKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2026302496a7f825e68ebe0f409dc67f03e56d91b85c6e9620df1d14531c2cd8)
                check_type(argname="argument app_server_private_key", value=app_server_private_key, expected_type=type_hints["app_server_private_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_server_private_key": app_server_private_key,
            }

        @builtins.property
        def app_server_private_key(self) -> builtins.str:
            '''The Sidewalk application server private key.

            The application server private key is a secret key, which you should handle in a similar way as you would an application password. You can protect the application server private key by storing the value in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html#cfn-iotwireless-partneraccount-sidewalkaccountinfo-appserverprivatekey
            '''
            result = self._values.get("app_server_private_key")
            assert result is not None, "Required property 'app_server_private_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkAccountInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty",
        jsii_struct_bases=[],
        name_mapping={
            "amazon_id": "amazonId",
            "arn": "arn",
            "fingerprint": "fingerprint",
        },
    )
    class SidewalkAccountInfoWithFingerprintProperty:
        def __init__(
            self,
            *,
            amazon_id: typing.Optional[builtins.str] = None,
            arn: typing.Optional[builtins.str] = None,
            fingerprint: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a Sidewalk account.

            :param amazon_id: The Sidewalk Amazon ID.
            :param arn: The Amazon Resource Name (ARN) of the resource.
            :param fingerprint: The fingerprint of the Sidewalk application server private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                sidewalk_account_info_with_fingerprint_property = iotwireless.CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty(
                    amazon_id="amazonId",
                    arn="arn",
                    fingerprint="fingerprint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ad67c351551efbad19725dfc18b31f0e8ac440e2de3a4b1505f542c76cb7dd5)
                check_type(argname="argument amazon_id", value=amazon_id, expected_type=type_hints["amazon_id"])
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument fingerprint", value=fingerprint, expected_type=type_hints["fingerprint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amazon_id is not None:
                self._values["amazon_id"] = amazon_id
            if arn is not None:
                self._values["arn"] = arn
            if fingerprint is not None:
                self._values["fingerprint"] = fingerprint

        @builtins.property
        def amazon_id(self) -> typing.Optional[builtins.str]:
            '''The Sidewalk Amazon ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-amazonid
            '''
            result = self._values.get("amazon_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fingerprint(self) -> typing.Optional[builtins.str]:
            '''The fingerprint of the Sidewalk application server private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-fingerprint
            '''
            result = self._values.get("fingerprint")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkAccountInfoWithFingerprintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty",
        jsii_struct_bases=[],
        name_mapping={"app_server_private_key": "appServerPrivateKey"},
    )
    class SidewalkUpdateAccountProperty:
        def __init__(
            self,
            *,
            app_server_private_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sidewalk update.

            :param app_server_private_key: The new Sidewalk application server private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                sidewalk_update_account_property = iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty(
                    app_server_private_key="appServerPrivateKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__419d83ee7d8c9559933db42ce308a1fff6731f91c044b636c9b8c0111ed95630)
                check_type(argname="argument app_server_private_key", value=app_server_private_key, expected_type=type_hints["app_server_private_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_server_private_key is not None:
                self._values["app_server_private_key"] = app_server_private_key

        @builtins.property
        def app_server_private_key(self) -> typing.Optional[builtins.str]:
            '''The new Sidewalk application server private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html#cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey
            '''
            result = self._values.get("app_server_private_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkUpdateAccountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnPartnerAccountProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_linked": "accountLinked",
        "partner_account_id": "partnerAccountId",
        "partner_type": "partnerType",
        "sidewalk": "sidewalk",
        "sidewalk_response": "sidewalkResponse",
        "sidewalk_update": "sidewalkUpdate",
        "tags": "tags",
    },
)
class CfnPartnerAccountProps:
    def __init__(
        self,
        *,
        account_linked: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        partner_account_id: typing.Optional[builtins.str] = None,
        partner_type: typing.Optional[builtins.str] = None,
        sidewalk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkAccountInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sidewalk_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sidewalk_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkUpdateAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPartnerAccount``.

        :param account_linked: Whether the partner account is linked to the AWS account.
        :param partner_account_id: The ID of the partner account to update.
        :param partner_type: The partner type.
        :param sidewalk: The Sidewalk account credentials.
        :param sidewalk_response: Information about a Sidewalk account.
        :param sidewalk_update: Sidewalk update.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_partner_account_props = iotwireless.CfnPartnerAccountProps(
                account_linked=False,
                partner_account_id="partnerAccountId",
                partner_type="partnerType",
                sidewalk=iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty(
                    app_server_private_key="appServerPrivateKey"
                ),
                sidewalk_response=iotwireless.CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty(
                    amazon_id="amazonId",
                    arn="arn",
                    fingerprint="fingerprint"
                ),
                sidewalk_update=iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty(
                    app_server_private_key="appServerPrivateKey"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c81ac7b24f2d30b6f882858ea510845d9241758d5fd74e60160c9d089bc1de6)
            check_type(argname="argument account_linked", value=account_linked, expected_type=type_hints["account_linked"])
            check_type(argname="argument partner_account_id", value=partner_account_id, expected_type=type_hints["partner_account_id"])
            check_type(argname="argument partner_type", value=partner_type, expected_type=type_hints["partner_type"])
            check_type(argname="argument sidewalk", value=sidewalk, expected_type=type_hints["sidewalk"])
            check_type(argname="argument sidewalk_response", value=sidewalk_response, expected_type=type_hints["sidewalk_response"])
            check_type(argname="argument sidewalk_update", value=sidewalk_update, expected_type=type_hints["sidewalk_update"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_linked is not None:
            self._values["account_linked"] = account_linked
        if partner_account_id is not None:
            self._values["partner_account_id"] = partner_account_id
        if partner_type is not None:
            self._values["partner_type"] = partner_type
        if sidewalk is not None:
            self._values["sidewalk"] = sidewalk
        if sidewalk_response is not None:
            self._values["sidewalk_response"] = sidewalk_response
        if sidewalk_update is not None:
            self._values["sidewalk_update"] = sidewalk_update
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_linked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the partner account is linked to the AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-accountlinked
        '''
        result = self._values.get("account_linked")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def partner_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the partner account to update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partneraccountid
        '''
        result = self._values.get("partner_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partner_type(self) -> typing.Optional[builtins.str]:
        '''The partner type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partnertype
        '''
        result = self._values.get("partner_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sidewalk(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkAccountInfoProperty]]:
        '''The Sidewalk account credentials.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalk
        '''
        result = self._values.get("sidewalk")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkAccountInfoProperty]], result)

    @builtins.property
    def sidewalk_response(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty]]:
        '''Information about a Sidewalk account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkresponse
        '''
        result = self._values.get("sidewalk_response")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty]], result)

    @builtins.property
    def sidewalk_update(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkUpdateAccountProperty]]:
        '''Sidewalk update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkupdate
        '''
        result = self._values.get("sidewalk_update")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkUpdateAccountProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPartnerAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnServiceProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnServiceProfile",
):
    '''Creates a new service profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
    :cloudformationResource: AWS::IoTWireless::ServiceProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_service_profile = iotwireless.CfnServiceProfile(self, "MyCfnServiceProfile",
            lo_ra_wan=iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty(
                add_gw_metadata=False,
                channel_mask="channelMask",
                dev_status_req_freq=123,
                dl_bucket_size=123,
                dl_rate=123,
                dl_rate_policy="dlRatePolicy",
                dr_max=123,
                dr_min=123,
                hr_allowed=False,
                min_gw_diversity=123,
                nwk_geo_loc=False,
                pr_allowed=False,
                ra_allowed=False,
                report_dev_status_battery=False,
                report_dev_status_margin=False,
                target_per=123,
                ul_bucket_size=123,
                ul_rate=123,
                ul_rate_policy="ulRatePolicy"
            ),
            name="name",
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
        lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceProfile.LoRaWANServiceProfileProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param lo_ra_wan: LoRaWAN service profile object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca074f221eda320f2c5d116c9446f9cd7110e09a78394cec71fb5ba026bbf22d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProfileProps(lo_ra_wan=lo_ra_wan, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__315dce048c406077b559684777c77b5922185f7618f6e7f04028b47d32b7baf3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3507ca4e4302d93d3394415217c34a0e9785c7d2280e3ed5952192a94d1fe9eb)
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
        '''The ARN of the service profile created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the service profile created.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanChannelMask")
    def attr_lo_ra_wan_channel_mask(self) -> builtins.str:
        '''The ChannelMask value.

        :cloudformationAttribute: LoRaWAN.ChannelMask
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanChannelMask"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDevStatusReqFreq")
    def attr_lo_ra_wan_dev_status_req_freq(self) -> jsii.Number:
        '''The DevStatusReqFreq value.

        :cloudformationAttribute: LoRaWAN.DevStatusReqFreq
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDevStatusReqFreq"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDlBucketSize")
    def attr_lo_ra_wan_dl_bucket_size(self) -> jsii.Number:
        '''The DLBucketSize value.

        :cloudformationAttribute: LoRaWAN.DlBucketSize
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDlBucketSize"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDlRate")
    def attr_lo_ra_wan_dl_rate(self) -> jsii.Number:
        '''The DLRate value.

        :cloudformationAttribute: LoRaWAN.DlRate
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDlRate"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDlRatePolicy")
    def attr_lo_ra_wan_dl_rate_policy(self) -> builtins.str:
        '''The DLRatePolicy value.

        :cloudformationAttribute: LoRaWAN.DlRatePolicy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanDlRatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDrMax")
    def attr_lo_ra_wan_dr_max(self) -> jsii.Number:
        '''The DRMax value.

        :cloudformationAttribute: LoRaWAN.DrMax
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDrMax"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDrMin")
    def attr_lo_ra_wan_dr_min(self) -> jsii.Number:
        '''The DRMin value.

        :cloudformationAttribute: LoRaWAN.DrMin
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDrMin"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanHrAllowed")
    def attr_lo_ra_wan_hr_allowed(self) -> _IResolvable_da3f097b:
        '''The HRAllowed value that describes whether handover roaming is allowed.

        :cloudformationAttribute: LoRaWAN.HrAllowed
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLoRaWanHrAllowed"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanMinGwDiversity")
    def attr_lo_ra_wan_min_gw_diversity(self) -> jsii.Number:
        '''The MinGwDiversity value.

        :cloudformationAttribute: LoRaWAN.MinGwDiversity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanMinGwDiversity"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanNwkGeoLoc")
    def attr_lo_ra_wan_nwk_geo_loc(self) -> _IResolvable_da3f097b:
        '''The NwkGeoLoc value.

        :cloudformationAttribute: LoRaWAN.NwkGeoLoc
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLoRaWanNwkGeoLoc"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanReportDevStatusBattery")
    def attr_lo_ra_wan_report_dev_status_battery(self) -> _IResolvable_da3f097b:
        '''The ReportDevStatusBattery value.

        :cloudformationAttribute: LoRaWAN.ReportDevStatusBattery
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLoRaWanReportDevStatusBattery"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanReportDevStatusMargin")
    def attr_lo_ra_wan_report_dev_status_margin(self) -> _IResolvable_da3f097b:
        '''The ReportDevStatusMargin value.

        :cloudformationAttribute: LoRaWAN.ReportDevStatusMargin
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLoRaWanReportDevStatusMargin"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanResponse")
    def attr_lo_ra_wan_response(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: LoRaWANResponse
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLoRaWanResponse"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanTargetPer")
    def attr_lo_ra_wan_target_per(self) -> jsii.Number:
        '''The TargetPer value.

        :cloudformationAttribute: LoRaWAN.TargetPer
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanTargetPer"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanUlBucketSize")
    def attr_lo_ra_wan_ul_bucket_size(self) -> jsii.Number:
        '''The UlBucketSize value.

        :cloudformationAttribute: LoRaWAN.UlBucketSize
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanUlBucketSize"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanUlRate")
    def attr_lo_ra_wan_ul_rate(self) -> jsii.Number:
        '''The ULRate value.

        :cloudformationAttribute: LoRaWAN.UlRate
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanUlRate"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanUlRatePolicy")
    def attr_lo_ra_wan_ul_rate_policy(self) -> builtins.str:
        '''The ULRatePolicy value.

        :cloudformationAttribute: LoRaWAN.UlRatePolicy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanUlRatePolicy"))

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
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceProfile.LoRaWANServiceProfileProperty"]]:
        '''LoRaWAN service profile object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceProfile.LoRaWANServiceProfileProperty"]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceProfile.LoRaWANServiceProfileProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d12a1731df94a26c15c2c629e69f05069e78147796ed92c827d35da4720ce385)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__495ecf85f557b8fb320530fa172728080da4333c5d1daf49554895e2ede03448)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e06c705f6bfd3ea15e35dda8a1e29b0c43e6f15d22947389e98e820e46ad578)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_gw_metadata": "addGwMetadata",
            "channel_mask": "channelMask",
            "dev_status_req_freq": "devStatusReqFreq",
            "dl_bucket_size": "dlBucketSize",
            "dl_rate": "dlRate",
            "dl_rate_policy": "dlRatePolicy",
            "dr_max": "drMax",
            "dr_min": "drMin",
            "hr_allowed": "hrAllowed",
            "min_gw_diversity": "minGwDiversity",
            "nwk_geo_loc": "nwkGeoLoc",
            "pr_allowed": "prAllowed",
            "ra_allowed": "raAllowed",
            "report_dev_status_battery": "reportDevStatusBattery",
            "report_dev_status_margin": "reportDevStatusMargin",
            "target_per": "targetPer",
            "ul_bucket_size": "ulBucketSize",
            "ul_rate": "ulRate",
            "ul_rate_policy": "ulRatePolicy",
        },
    )
    class LoRaWANServiceProfileProperty:
        def __init__(
            self,
            *,
            add_gw_metadata: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            channel_mask: typing.Optional[builtins.str] = None,
            dev_status_req_freq: typing.Optional[jsii.Number] = None,
            dl_bucket_size: typing.Optional[jsii.Number] = None,
            dl_rate: typing.Optional[jsii.Number] = None,
            dl_rate_policy: typing.Optional[builtins.str] = None,
            dr_max: typing.Optional[jsii.Number] = None,
            dr_min: typing.Optional[jsii.Number] = None,
            hr_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            min_gw_diversity: typing.Optional[jsii.Number] = None,
            nwk_geo_loc: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            pr_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ra_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            report_dev_status_battery: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            report_dev_status_margin: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            target_per: typing.Optional[jsii.Number] = None,
            ul_bucket_size: typing.Optional[jsii.Number] = None,
            ul_rate: typing.Optional[jsii.Number] = None,
            ul_rate_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''LoRaWANServiceProfile object.

            :param add_gw_metadata: The AddGWMetaData value.
            :param channel_mask: The ChannelMask value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dev_status_req_freq: The DevStatusReqFreq value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dl_bucket_size: The DLBucketSize value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dl_rate: The DLRate value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dl_rate_policy: The DLRatePolicy value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dr_max: The DRMax value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dr_min: The DRMin value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param hr_allowed: The HRAllowed value that describes whether handover roaming is allowed. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param min_gw_diversity: The MinGwDiversity value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param nwk_geo_loc: The NwkGeoLoc value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param pr_allowed: The PRAllowed value that describes whether passive roaming is allowed. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param ra_allowed: The RAAllowed value that describes whether roaming activation is allowed.
            :param report_dev_status_battery: The ReportDevStatusBattery value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param report_dev_status_margin: The ReportDevStatusMargin value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param target_per: The TargetPer value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param ul_bucket_size: The UlBucketSize value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param ul_rate: The ULRate value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param ul_rate_policy: The ULRatePolicy value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANService_profile_property = iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty(
                    add_gw_metadata=False,
                    channel_mask="channelMask",
                    dev_status_req_freq=123,
                    dl_bucket_size=123,
                    dl_rate=123,
                    dl_rate_policy="dlRatePolicy",
                    dr_max=123,
                    dr_min=123,
                    hr_allowed=False,
                    min_gw_diversity=123,
                    nwk_geo_loc=False,
                    pr_allowed=False,
                    ra_allowed=False,
                    report_dev_status_battery=False,
                    report_dev_status_margin=False,
                    target_per=123,
                    ul_bucket_size=123,
                    ul_rate=123,
                    ul_rate_policy="ulRatePolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80e153375dd84b74afa9419878247da802f9f8a8a199383f8d5fd7a83461c9d9)
                check_type(argname="argument add_gw_metadata", value=add_gw_metadata, expected_type=type_hints["add_gw_metadata"])
                check_type(argname="argument channel_mask", value=channel_mask, expected_type=type_hints["channel_mask"])
                check_type(argname="argument dev_status_req_freq", value=dev_status_req_freq, expected_type=type_hints["dev_status_req_freq"])
                check_type(argname="argument dl_bucket_size", value=dl_bucket_size, expected_type=type_hints["dl_bucket_size"])
                check_type(argname="argument dl_rate", value=dl_rate, expected_type=type_hints["dl_rate"])
                check_type(argname="argument dl_rate_policy", value=dl_rate_policy, expected_type=type_hints["dl_rate_policy"])
                check_type(argname="argument dr_max", value=dr_max, expected_type=type_hints["dr_max"])
                check_type(argname="argument dr_min", value=dr_min, expected_type=type_hints["dr_min"])
                check_type(argname="argument hr_allowed", value=hr_allowed, expected_type=type_hints["hr_allowed"])
                check_type(argname="argument min_gw_diversity", value=min_gw_diversity, expected_type=type_hints["min_gw_diversity"])
                check_type(argname="argument nwk_geo_loc", value=nwk_geo_loc, expected_type=type_hints["nwk_geo_loc"])
                check_type(argname="argument pr_allowed", value=pr_allowed, expected_type=type_hints["pr_allowed"])
                check_type(argname="argument ra_allowed", value=ra_allowed, expected_type=type_hints["ra_allowed"])
                check_type(argname="argument report_dev_status_battery", value=report_dev_status_battery, expected_type=type_hints["report_dev_status_battery"])
                check_type(argname="argument report_dev_status_margin", value=report_dev_status_margin, expected_type=type_hints["report_dev_status_margin"])
                check_type(argname="argument target_per", value=target_per, expected_type=type_hints["target_per"])
                check_type(argname="argument ul_bucket_size", value=ul_bucket_size, expected_type=type_hints["ul_bucket_size"])
                check_type(argname="argument ul_rate", value=ul_rate, expected_type=type_hints["ul_rate"])
                check_type(argname="argument ul_rate_policy", value=ul_rate_policy, expected_type=type_hints["ul_rate_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_gw_metadata is not None:
                self._values["add_gw_metadata"] = add_gw_metadata
            if channel_mask is not None:
                self._values["channel_mask"] = channel_mask
            if dev_status_req_freq is not None:
                self._values["dev_status_req_freq"] = dev_status_req_freq
            if dl_bucket_size is not None:
                self._values["dl_bucket_size"] = dl_bucket_size
            if dl_rate is not None:
                self._values["dl_rate"] = dl_rate
            if dl_rate_policy is not None:
                self._values["dl_rate_policy"] = dl_rate_policy
            if dr_max is not None:
                self._values["dr_max"] = dr_max
            if dr_min is not None:
                self._values["dr_min"] = dr_min
            if hr_allowed is not None:
                self._values["hr_allowed"] = hr_allowed
            if min_gw_diversity is not None:
                self._values["min_gw_diversity"] = min_gw_diversity
            if nwk_geo_loc is not None:
                self._values["nwk_geo_loc"] = nwk_geo_loc
            if pr_allowed is not None:
                self._values["pr_allowed"] = pr_allowed
            if ra_allowed is not None:
                self._values["ra_allowed"] = ra_allowed
            if report_dev_status_battery is not None:
                self._values["report_dev_status_battery"] = report_dev_status_battery
            if report_dev_status_margin is not None:
                self._values["report_dev_status_margin"] = report_dev_status_margin
            if target_per is not None:
                self._values["target_per"] = target_per
            if ul_bucket_size is not None:
                self._values["ul_bucket_size"] = ul_bucket_size
            if ul_rate is not None:
                self._values["ul_rate"] = ul_rate
            if ul_rate_policy is not None:
                self._values["ul_rate_policy"] = ul_rate_policy

        @builtins.property
        def add_gw_metadata(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The AddGWMetaData value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata
            '''
            result = self._values.get("add_gw_metadata")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def channel_mask(self) -> typing.Optional[builtins.str]:
            '''The ChannelMask value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask
            '''
            result = self._values.get("channel_mask")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dev_status_req_freq(self) -> typing.Optional[jsii.Number]:
            '''The DevStatusReqFreq value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq
            '''
            result = self._values.get("dev_status_req_freq")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_bucket_size(self) -> typing.Optional[jsii.Number]:
            '''The DLBucketSize value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize
            '''
            result = self._values.get("dl_bucket_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_rate(self) -> typing.Optional[jsii.Number]:
            '''The DLRate value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate
            '''
            result = self._values.get("dl_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_rate_policy(self) -> typing.Optional[builtins.str]:
            '''The DLRatePolicy value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy
            '''
            result = self._values.get("dl_rate_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dr_max(self) -> typing.Optional[jsii.Number]:
            '''The DRMax value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax
            '''
            result = self._values.get("dr_max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dr_min(self) -> typing.Optional[jsii.Number]:
            '''The DRMin value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin
            '''
            result = self._values.get("dr_min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def hr_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The HRAllowed value that describes whether handover roaming is allowed.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed
            '''
            result = self._values.get("hr_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def min_gw_diversity(self) -> typing.Optional[jsii.Number]:
            '''The MinGwDiversity value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity
            '''
            result = self._values.get("min_gw_diversity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def nwk_geo_loc(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The NwkGeoLoc value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc
            '''
            result = self._values.get("nwk_geo_loc")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def pr_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The PRAllowed value that describes whether passive roaming is allowed.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed
            '''
            result = self._values.get("pr_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ra_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The RAAllowed value that describes whether roaming activation is allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed
            '''
            result = self._values.get("ra_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def report_dev_status_battery(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The ReportDevStatusBattery value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery
            '''
            result = self._values.get("report_dev_status_battery")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def report_dev_status_margin(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The ReportDevStatusMargin value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin
            '''
            result = self._values.get("report_dev_status_margin")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def target_per(self) -> typing.Optional[jsii.Number]:
            '''The TargetPer value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper
            '''
            result = self._values.get("target_per")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_bucket_size(self) -> typing.Optional[jsii.Number]:
            '''The UlBucketSize value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize
            '''
            result = self._values.get("ul_bucket_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_rate(self) -> typing.Optional[jsii.Number]:
            '''The ULRate value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate
            '''
            result = self._values.get("ul_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_rate_policy(self) -> typing.Optional[builtins.str]:
            '''The ULRatePolicy value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy
            '''
            result = self._values.get("ul_rate_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANServiceProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnServiceProfileProps",
    jsii_struct_bases=[],
    name_mapping={"lo_ra_wan": "loRaWan", "name": "name", "tags": "tags"},
)
class CfnServiceProfileProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceProfile.LoRaWANServiceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceProfile``.

        :param lo_ra_wan: LoRaWAN service profile object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_service_profile_props = iotwireless.CfnServiceProfileProps(
                lo_ra_wan=iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty(
                    add_gw_metadata=False,
                    channel_mask="channelMask",
                    dev_status_req_freq=123,
                    dl_bucket_size=123,
                    dl_rate=123,
                    dl_rate_policy="dlRatePolicy",
                    dr_max=123,
                    dr_min=123,
                    hr_allowed=False,
                    min_gw_diversity=123,
                    nwk_geo_loc=False,
                    pr_allowed=False,
                    ra_allowed=False,
                    report_dev_status_battery=False,
                    report_dev_status_margin=False,
                    target_per=123,
                    ul_bucket_size=123,
                    ul_rate=123,
                    ul_rate_policy="ulRatePolicy"
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c50b2c760a33d8243522ebcd46655f17e5c27bf15d6038dbf0c68cf36232ecb)
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceProfile.LoRaWANServiceProfileProperty]]:
        '''LoRaWAN service profile object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceProfile.LoRaWANServiceProfileProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTaskDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnTaskDefinition",
):
    '''Creates a gateway task definition.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html
    :cloudformationResource: AWS::IoTWireless::TaskDefinition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_task_definition = iotwireless.CfnTaskDefinition(self, "MyCfnTaskDefinition",
            auto_create_tasks=False,
        
            # the properties below are optional
            lo_ra_wan_update_gateway_task_entry=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty(
                current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                    model="model",
                    package_version="packageVersion",
                    station="station"
                ),
                update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                    model="model",
                    package_version="packageVersion",
                    station="station"
                )
            ),
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            task_definition_type="taskDefinitionType",
            update=iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty(
                lo_ra_wan=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty(
                    current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    ),
                    sig_key_crc=123,
                    update_signature="updateSignature",
                    update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    )
                ),
                update_data_role="updateDataRole",
                update_data_source="updateDataSource"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        auto_create_tasks: typing.Union[builtins.bool, _IResolvable_da3f097b],
        lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_definition_type: typing.Optional[builtins.str] = None,
        update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_create_tasks: Whether to automatically create tasks using this task definition for all gateways with the specified current version. If ``false`` , the task must be created by calling ``CreateWirelessGatewayTask`` .
        :param lo_ra_wan_update_gateway_task_entry: LoRaWANUpdateGatewayTaskEntry object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param task_definition_type: A filter to list only the wireless gateway task definitions that use this task definition type.
        :param update: Information about the gateways to update.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d10e64d4deea928b0f793f0894101d94fa8dbafc82f1f64d5fabc09fe26aca6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTaskDefinitionProps(
            auto_create_tasks=auto_create_tasks,
            lo_ra_wan_update_gateway_task_entry=lo_ra_wan_update_gateway_task_entry,
            name=name,
            tags=tags,
            task_definition_type=task_definition_type,
            update=update,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9de16cdf43d0eedc9a4ca88788b721ffd3a0f35e0585fe70fc2a8d9d2f698aaa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce022de682a811bfe3b20f7d040c6f58cab74a9722d6b628e9086aee7a863dc8)
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
        '''The Amazon Resource Name of the resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the new wireless gateway task definition.

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
    @jsii.member(jsii_name="autoCreateTasks")
    def auto_create_tasks(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether to automatically create tasks using this task definition for all gateways with the specified current version.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "autoCreateTasks"))

    @auto_create_tasks.setter
    def auto_create_tasks(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2140f6dd2fd5b773e37d8f7300ca14605b82d89631076e6aa400f13c633cc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoCreateTasks", value)

    @builtins.property
    @jsii.member(jsii_name="loRaWanUpdateGatewayTaskEntry")
    def lo_ra_wan_update_gateway_task_entry(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]]:
        '''LoRaWANUpdateGatewayTaskEntry object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]], jsii.get(self, "loRaWanUpdateGatewayTaskEntry"))

    @lo_ra_wan_update_gateway_task_entry.setter
    def lo_ra_wan_update_gateway_task_entry(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba999a41533710976a33b0a1023c1222f1541c811f550a29499fa6d5675bf40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWanUpdateGatewayTaskEntry", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb88f2db89785cd3e23338b9b79cdcdfeb8e47dcfc703bccb73087cc7c530dac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__302c9856183cfc94540db93d88e4bc1e952c85bd9598afb0ef7bed2bc6a84411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionType")
    def task_definition_type(self) -> typing.Optional[builtins.str]:
        '''A filter to list only the wireless gateway task definitions that use this task definition type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionType"))

    @task_definition_type.setter
    def task_definition_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fd5d538e8d4ed460e65c9ddac2d1d68fd4345c4afe7e403b77fa77f80136dee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinitionType", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]]:
        '''Information about the gateways to update.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]], jsii.get(self, "update"))

    @update.setter
    def update(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7873ddd4c5f9c059a1c30910bb0374ee468e180657a2870e1598db17895e714b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "model": "model",
            "package_version": "packageVersion",
            "station": "station",
        },
    )
    class LoRaWANGatewayVersionProperty:
        def __init__(
            self,
            *,
            model: typing.Optional[builtins.str] = None,
            package_version: typing.Optional[builtins.str] = None,
            station: typing.Optional[builtins.str] = None,
        ) -> None:
            '''LoRaWANGatewayVersion object.

            :param model: The model number of the wireless gateway.
            :param package_version: The version of the wireless gateway firmware.
            :param station: The basic station version of the wireless gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANGateway_version_property = iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                    model="model",
                    package_version="packageVersion",
                    station="station"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9eead759e83004a38194e11d8a25d0f709bff70ca8565202c9519e20c74bbb29)
                check_type(argname="argument model", value=model, expected_type=type_hints["model"])
                check_type(argname="argument package_version", value=package_version, expected_type=type_hints["package_version"])
                check_type(argname="argument station", value=station, expected_type=type_hints["station"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if model is not None:
                self._values["model"] = model
            if package_version is not None:
                self._values["package_version"] = package_version
            if station is not None:
                self._values["station"] = station

        @builtins.property
        def model(self) -> typing.Optional[builtins.str]:
            '''The model number of the wireless gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-model
            '''
            result = self._values.get("model")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def package_version(self) -> typing.Optional[builtins.str]:
            '''The version of the wireless gateway firmware.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-packageversion
            '''
            result = self._values.get("package_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def station(self) -> typing.Optional[builtins.str]:
            '''The basic station version of the wireless gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-station
            '''
            result = self._values.get("station")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANGatewayVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "current_version": "currentVersion",
            "sig_key_crc": "sigKeyCrc",
            "update_signature": "updateSignature",
            "update_version": "updateVersion",
        },
    )
    class LoRaWANUpdateGatewayTaskCreateProperty:
        def __init__(
            self,
            *,
            current_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskDefinition.LoRaWANGatewayVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sig_key_crc: typing.Optional[jsii.Number] = None,
            update_signature: typing.Optional[builtins.str] = None,
            update_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskDefinition.LoRaWANGatewayVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The signature used to verify the update firmware.

            :param current_version: The version of the gateways that should receive the update.
            :param sig_key_crc: The CRC of the signature private key to check.
            :param update_signature: The signature used to verify the update firmware.
            :param update_version: The firmware version to update the gateway to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANUpdate_gateway_task_create_property = iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty(
                    current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    ),
                    sig_key_crc=123,
                    update_signature="updateSignature",
                    update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__afc21f41ee9ebd8dda0283e11946044bf70b6c27b33a3abce3ff415c7ff703f6)
                check_type(argname="argument current_version", value=current_version, expected_type=type_hints["current_version"])
                check_type(argname="argument sig_key_crc", value=sig_key_crc, expected_type=type_hints["sig_key_crc"])
                check_type(argname="argument update_signature", value=update_signature, expected_type=type_hints["update_signature"])
                check_type(argname="argument update_version", value=update_version, expected_type=type_hints["update_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if current_version is not None:
                self._values["current_version"] = current_version
            if sig_key_crc is not None:
                self._values["sig_key_crc"] = sig_key_crc
            if update_signature is not None:
                self._values["update_signature"] = update_signature
            if update_version is not None:
                self._values["update_version"] = update_version

        @builtins.property
        def current_version(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''The version of the gateways that should receive the update.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-currentversion
            '''
            result = self._values.get("current_version")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        @builtins.property
        def sig_key_crc(self) -> typing.Optional[jsii.Number]:
            '''The CRC of the signature private key to check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-sigkeycrc
            '''
            result = self._values.get("sig_key_crc")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def update_signature(self) -> typing.Optional[builtins.str]:
            '''The signature used to verify the update firmware.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updatesignature
            '''
            result = self._values.get("update_signature")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def update_version(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''The firmware version to update the gateway to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updateversion
            '''
            result = self._values.get("update_version")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANUpdateGatewayTaskCreateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "current_version": "currentVersion",
            "update_version": "updateVersion",
        },
    )
    class LoRaWANUpdateGatewayTaskEntryProperty:
        def __init__(
            self,
            *,
            current_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskDefinition.LoRaWANGatewayVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            update_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskDefinition.LoRaWANGatewayVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''LoRaWANUpdateGatewayTaskEntry object.

            :param current_version: The version of the gateways that should receive the update.
            :param update_version: The firmware version to update the gateway to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANUpdate_gateway_task_entry_property = iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty(
                    current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    ),
                    update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d6341594bc267055b9e38191ae8ee71808f7e74d40bfa33ef01f6c1710119fe9)
                check_type(argname="argument current_version", value=current_version, expected_type=type_hints["current_version"])
                check_type(argname="argument update_version", value=update_version, expected_type=type_hints["update_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if current_version is not None:
                self._values["current_version"] = current_version
            if update_version is not None:
                self._values["update_version"] = update_version

        @builtins.property
        def current_version(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''The version of the gateways that should receive the update.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion
            '''
            result = self._values.get("current_version")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        @builtins.property
        def update_version(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''The firmware version to update the gateway to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion
            '''
            result = self._values.get("update_version")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANUpdateGatewayTaskEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lo_ra_wan": "loRaWan",
            "update_data_role": "updateDataRole",
            "update_data_source": "updateDataSource",
        },
    )
    class UpdateWirelessGatewayTaskCreateProperty:
        def __init__(
            self,
            *,
            lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            update_data_role: typing.Optional[builtins.str] = None,
            update_data_source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''UpdateWirelessGatewayTaskCreate object.

            :param lo_ra_wan: The properties that relate to the LoRaWAN wireless gateway.
            :param update_data_role: The IAM role used to read data from the S3 bucket.
            :param update_data_source: The link to the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                update_wireless_gateway_task_create_property = iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty(
                    lo_ra_wan=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty(
                        current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                            model="model",
                            package_version="packageVersion",
                            station="station"
                        ),
                        sig_key_crc=123,
                        update_signature="updateSignature",
                        update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                            model="model",
                            package_version="packageVersion",
                            station="station"
                        )
                    ),
                    update_data_role="updateDataRole",
                    update_data_source="updateDataSource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2395a28ee7e4fa7cb268ed190fa8f9e55566832b4de59e0f97aadf1c082f3ac7)
                check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
                check_type(argname="argument update_data_role", value=update_data_role, expected_type=type_hints["update_data_role"])
                check_type(argname="argument update_data_source", value=update_data_source, expected_type=type_hints["update_data_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lo_ra_wan is not None:
                self._values["lo_ra_wan"] = lo_ra_wan
            if update_data_role is not None:
                self._values["update_data_role"] = update_data_role
            if update_data_source is not None:
                self._values["update_data_source"] = update_data_source

        @builtins.property
        def lo_ra_wan(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty"]]:
            '''The properties that relate to the LoRaWAN wireless gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan
            '''
            result = self._values.get("lo_ra_wan")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty"]], result)

        @builtins.property
        def update_data_role(self) -> typing.Optional[builtins.str]:
            '''The IAM role used to read data from the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole
            '''
            result = self._values.get("update_data_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def update_data_source(self) -> typing.Optional[builtins.str]:
            '''The link to the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource
            '''
            result = self._values.get("update_data_source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateWirelessGatewayTaskCreateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnTaskDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_create_tasks": "autoCreateTasks",
        "lo_ra_wan_update_gateway_task_entry": "loRaWanUpdateGatewayTaskEntry",
        "name": "name",
        "tags": "tags",
        "task_definition_type": "taskDefinitionType",
        "update": "update",
    },
)
class CfnTaskDefinitionProps:
    def __init__(
        self,
        *,
        auto_create_tasks: typing.Union[builtins.bool, _IResolvable_da3f097b],
        lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_definition_type: typing.Optional[builtins.str] = None,
        update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTaskDefinition``.

        :param auto_create_tasks: Whether to automatically create tasks using this task definition for all gateways with the specified current version. If ``false`` , the task must be created by calling ``CreateWirelessGatewayTask`` .
        :param lo_ra_wan_update_gateway_task_entry: LoRaWANUpdateGatewayTaskEntry object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param task_definition_type: A filter to list only the wireless gateway task definitions that use this task definition type.
        :param update: Information about the gateways to update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_task_definition_props = iotwireless.CfnTaskDefinitionProps(
                auto_create_tasks=False,
            
                # the properties below are optional
                lo_ra_wan_update_gateway_task_entry=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty(
                    current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    ),
                    update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    )
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                task_definition_type="taskDefinitionType",
                update=iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty(
                    lo_ra_wan=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty(
                        current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                            model="model",
                            package_version="packageVersion",
                            station="station"
                        ),
                        sig_key_crc=123,
                        update_signature="updateSignature",
                        update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                            model="model",
                            package_version="packageVersion",
                            station="station"
                        )
                    ),
                    update_data_role="updateDataRole",
                    update_data_source="updateDataSource"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__375ac4d1ecfc288b9e4e324b136b3fca6fc5ce7a227ca417eea320f867d83eaa)
            check_type(argname="argument auto_create_tasks", value=auto_create_tasks, expected_type=type_hints["auto_create_tasks"])
            check_type(argname="argument lo_ra_wan_update_gateway_task_entry", value=lo_ra_wan_update_gateway_task_entry, expected_type=type_hints["lo_ra_wan_update_gateway_task_entry"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_definition_type", value=task_definition_type, expected_type=type_hints["task_definition_type"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_create_tasks": auto_create_tasks,
        }
        if lo_ra_wan_update_gateway_task_entry is not None:
            self._values["lo_ra_wan_update_gateway_task_entry"] = lo_ra_wan_update_gateway_task_entry
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if task_definition_type is not None:
            self._values["task_definition_type"] = task_definition_type
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def auto_create_tasks(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether to automatically create tasks using this task definition for all gateways with the specified current version.

        If ``false`` , the task must be created by calling ``CreateWirelessGatewayTask`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-autocreatetasks
        '''
        result = self._values.get("auto_create_tasks")
        assert result is not None, "Required property 'auto_create_tasks' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def lo_ra_wan_update_gateway_task_entry(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]]:
        '''LoRaWANUpdateGatewayTaskEntry object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry
        '''
        result = self._values.get("lo_ra_wan_update_gateway_task_entry")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def task_definition_type(self) -> typing.Optional[builtins.str]:
        '''A filter to list only the wireless gateway task definitions that use this task definition type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-taskdefinitiontype
        '''
        result = self._values.get("task_definition_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]]:
        '''Information about the gateways to update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-update
        '''
        result = self._values.get("update")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTaskDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWirelessDevice(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDevice",
):
    '''Provisions a wireless device.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
    :cloudformationResource: AWS::IoTWireless::WirelessDevice
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_wireless_device = iotwireless.CfnWirelessDevice(self, "MyCfnWirelessDevice",
            destination_name="destinationName",
            type="type",
        
            # the properties below are optional
            description="description",
            last_uplink_received_at="lastUplinkReceivedAt",
            lo_ra_wan=iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty(
                abp_v10_x=iotwireless.CfnWirelessDevice.AbpV10xProperty(
                    dev_addr="devAddr",
                    session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                        app_sKey="appSKey",
                        nwk_sKey="nwkSKey"
                    )
                ),
                abp_v11=iotwireless.CfnWirelessDevice.AbpV11Property(
                    dev_addr="devAddr",
                    session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                        app_sKey="appSKey",
                        f_nwk_sInt_key="fNwkSIntKey",
                        nwk_sEnc_key="nwkSEncKey",
                        s_nwk_sInt_key="sNwkSIntKey"
                    )
                ),
                dev_eui="devEui",
                device_profile_id="deviceProfileId",
                otaa_v10_x=iotwireless.CfnWirelessDevice.OtaaV10xProperty(
                    app_eui="appEui",
                    app_key="appKey"
                ),
                otaa_v11=iotwireless.CfnWirelessDevice.OtaaV11Property(
                    app_key="appKey",
                    join_eui="joinEui",
                    nwk_key="nwkKey"
                ),
                service_profile_id="serviceProfileId"
            ),
            name="name",
            positioning="positioning",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            thing_arn="thingArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessDevice.LoRaWANDeviceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        positioning: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_name: The name of the destination to assign to the new wireless device. Can have only have alphanumeric, - (hyphen) and _ (underscore) characters and it can't have any spaces.
        :param type: The wireless device type.
        :param description: The description of the new resource. Maximum length is 2048.
        :param last_uplink_received_at: The date and time when the most recent uplink was received.
        :param lo_ra_wan: The device configuration information to use to create the wireless device. Must be at least one of OtaaV10x, OtaaV11, AbpV11, or AbpV10x.
        :param name: The name of the new resource.
        :param positioning: FPort values for the GNSS, Stream, and ClockSync functions of the positioning information.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param thing_arn: The ARN of the thing to associate with the wireless device.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a785469cac62290b28ca4347d5562cd8f4e0d3d2543a08bb415fcdfcda69c6e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWirelessDeviceProps(
            destination_name=destination_name,
            type=type,
            description=description,
            last_uplink_received_at=last_uplink_received_at,
            lo_ra_wan=lo_ra_wan,
            name=name,
            positioning=positioning,
            tags=tags,
            thing_arn=thing_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c3f9623871804482a281e90ea9c41a1af250f5169c286db6bc7ab0e057fb788)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cac17e63441404903d9dae8730314dcfb4bdedf123d43ee74bc1d52bf06f9c24)
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
        '''The ARN of the wireless device created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the wireless device created.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrThingName")
    def attr_thing_name(self) -> builtins.str:
        '''The name of the thing associated with the wireless device.

        The value is empty if a thing isn't associated with the device.

        :cloudformationAttribute: ThingName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrThingName"))

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
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        '''The name of the destination to assign to the new wireless device.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationName"))

    @destination_name.setter
    def destination_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8061cf48768d2d28b9433ea6b1db3222bac9893ee1a0c96bcdb98226cc2f3d03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The wireless device type.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b70c988e1950493c52e44208f809dafc1d545d18b89e9e2227674650c390bc4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fc0b1687f73dd9eca4c02d192704c2293c20941495c350b0e122eea76052901)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="lastUplinkReceivedAt")
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''The date and time when the most recent uplink was received.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastUplinkReceivedAt"))

    @last_uplink_received_at.setter
    def last_uplink_received_at(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6eb1d5a6add55c4de31d6a02d93e5a6c7b8f13ebd8c3e95893448a2464af2a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastUplinkReceivedAt", value)

    @builtins.property
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.LoRaWANDeviceProperty"]]:
        '''The device configuration information to use to create the wireless device.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.LoRaWANDeviceProperty"]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.LoRaWANDeviceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a9387fe5c912c19442cf1a22d4b80b3bfec7bfaeaeedfde3a48464707ac5e94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79b8e8d3143dce00df934e2b0287a3a53fc9839551772e6cc273d592d0bc262f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="positioning")
    def positioning(self) -> typing.Optional[builtins.str]:
        '''FPort values for the GNSS, Stream, and ClockSync functions of the positioning information.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "positioning"))

    @positioning.setter
    def positioning(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c7b7fcf5ba7730b0ce3b8c924fe1fe208985f6c0d4fd68b55353bbe9d05b61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "positioning", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de98087af9f5a2df8b9078aef4604fb7a5d9b8ce62eab7c135763cdcf4911075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="thingArn")
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the thing to associate with the wireless device.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingArn"))

    @thing_arn.setter
    def thing_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1062e2a4111f3f10850a14272256ebd97067e00cf02bb987304ac070474dc47f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDevice.AbpV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"dev_addr": "devAddr", "session_keys": "sessionKeys"},
    )
    class AbpV10xProperty:
        def __init__(
            self,
            *,
            dev_addr: builtins.str,
            session_keys: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessDevice.SessionKeysAbpV10xProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''ABP device object for LoRaWAN specification v1.0.x.

            :param dev_addr: The DevAddr value.
            :param session_keys: Session keys for ABP v1.0.x.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                abp_v10x_property = iotwireless.CfnWirelessDevice.AbpV10xProperty(
                    dev_addr="devAddr",
                    session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                        app_sKey="appSKey",
                        nwk_sKey="nwkSKey"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f3c7c33ac394ea769fdff09d74d18df5199694a0b192de0112bc6fc8bad01ac)
                check_type(argname="argument dev_addr", value=dev_addr, expected_type=type_hints["dev_addr"])
                check_type(argname="argument session_keys", value=session_keys, expected_type=type_hints["session_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dev_addr": dev_addr,
                "session_keys": session_keys,
            }

        @builtins.property
        def dev_addr(self) -> builtins.str:
            '''The DevAddr value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-devaddr
            '''
            result = self._values.get("dev_addr")
            assert result is not None, "Required property 'dev_addr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def session_keys(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.SessionKeysAbpV10xProperty"]:
            '''Session keys for ABP v1.0.x.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-sessionkeys
            '''
            result = self._values.get("session_keys")
            assert result is not None, "Required property 'session_keys' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.SessionKeysAbpV10xProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbpV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDevice.AbpV11Property",
        jsii_struct_bases=[],
        name_mapping={"dev_addr": "devAddr", "session_keys": "sessionKeys"},
    )
    class AbpV11Property:
        def __init__(
            self,
            *,
            dev_addr: builtins.str,
            session_keys: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessDevice.SessionKeysAbpV11Property", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''ABP device object for create APIs for v1.1.

            :param dev_addr: The DevAddr value.
            :param session_keys: Session keys for ABP v1.1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                abp_v11_property = iotwireless.CfnWirelessDevice.AbpV11Property(
                    dev_addr="devAddr",
                    session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                        app_sKey="appSKey",
                        f_nwk_sInt_key="fNwkSIntKey",
                        nwk_sEnc_key="nwkSEncKey",
                        s_nwk_sInt_key="sNwkSIntKey"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__60d86251ec9e15886b39ab32d3b20d4a624d17a6f00dd271dfc743f0d050ca1e)
                check_type(argname="argument dev_addr", value=dev_addr, expected_type=type_hints["dev_addr"])
                check_type(argname="argument session_keys", value=session_keys, expected_type=type_hints["session_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dev_addr": dev_addr,
                "session_keys": session_keys,
            }

        @builtins.property
        def dev_addr(self) -> builtins.str:
            '''The DevAddr value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-devaddr
            '''
            result = self._values.get("dev_addr")
            assert result is not None, "Required property 'dev_addr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def session_keys(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.SessionKeysAbpV11Property"]:
            '''Session keys for ABP v1.1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys
            '''
            result = self._values.get("session_keys")
            assert result is not None, "Required property 'session_keys' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.SessionKeysAbpV11Property"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbpV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "abp_v10_x": "abpV10X",
            "abp_v11": "abpV11",
            "dev_eui": "devEui",
            "device_profile_id": "deviceProfileId",
            "otaa_v10_x": "otaaV10X",
            "otaa_v11": "otaaV11",
            "service_profile_id": "serviceProfileId",
        },
    )
    class LoRaWANDeviceProperty:
        def __init__(
            self,
            *,
            abp_v10_x: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessDevice.AbpV10xProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            abp_v11: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessDevice.AbpV11Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            dev_eui: typing.Optional[builtins.str] = None,
            device_profile_id: typing.Optional[builtins.str] = None,
            otaa_v10_x: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessDevice.OtaaV10xProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            otaa_v11: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessDevice.OtaaV11Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_profile_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''LoRaWAN object for create functions.

            :param abp_v10_x: ABP device object for LoRaWAN specification v1.0.x.
            :param abp_v11: ABP device object for create APIs for v1.1.
            :param dev_eui: The DevEUI value.
            :param device_profile_id: The ID of the device profile for the new wireless device.
            :param otaa_v10_x: OTAA device object for create APIs for v1.0.x.
            :param otaa_v11: OTAA device object for v1.1 for create APIs.
            :param service_profile_id: The ID of the service profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANDevice_property = iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty(
                    abp_v10_x=iotwireless.CfnWirelessDevice.AbpV10xProperty(
                        dev_addr="devAddr",
                        session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                            app_sKey="appSKey",
                            nwk_sKey="nwkSKey"
                        )
                    ),
                    abp_v11=iotwireless.CfnWirelessDevice.AbpV11Property(
                        dev_addr="devAddr",
                        session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                            app_sKey="appSKey",
                            f_nwk_sInt_key="fNwkSIntKey",
                            nwk_sEnc_key="nwkSEncKey",
                            s_nwk_sInt_key="sNwkSIntKey"
                        )
                    ),
                    dev_eui="devEui",
                    device_profile_id="deviceProfileId",
                    otaa_v10_x=iotwireless.CfnWirelessDevice.OtaaV10xProperty(
                        app_eui="appEui",
                        app_key="appKey"
                    ),
                    otaa_v11=iotwireless.CfnWirelessDevice.OtaaV11Property(
                        app_key="appKey",
                        join_eui="joinEui",
                        nwk_key="nwkKey"
                    ),
                    service_profile_id="serviceProfileId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__79b613fcb6e4bec4dd04e0ec3aefb63244dbaff286fed6d7327bebfa7aed6cba)
                check_type(argname="argument abp_v10_x", value=abp_v10_x, expected_type=type_hints["abp_v10_x"])
                check_type(argname="argument abp_v11", value=abp_v11, expected_type=type_hints["abp_v11"])
                check_type(argname="argument dev_eui", value=dev_eui, expected_type=type_hints["dev_eui"])
                check_type(argname="argument device_profile_id", value=device_profile_id, expected_type=type_hints["device_profile_id"])
                check_type(argname="argument otaa_v10_x", value=otaa_v10_x, expected_type=type_hints["otaa_v10_x"])
                check_type(argname="argument otaa_v11", value=otaa_v11, expected_type=type_hints["otaa_v11"])
                check_type(argname="argument service_profile_id", value=service_profile_id, expected_type=type_hints["service_profile_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if abp_v10_x is not None:
                self._values["abp_v10_x"] = abp_v10_x
            if abp_v11 is not None:
                self._values["abp_v11"] = abp_v11
            if dev_eui is not None:
                self._values["dev_eui"] = dev_eui
            if device_profile_id is not None:
                self._values["device_profile_id"] = device_profile_id
            if otaa_v10_x is not None:
                self._values["otaa_v10_x"] = otaa_v10_x
            if otaa_v11 is not None:
                self._values["otaa_v11"] = otaa_v11
            if service_profile_id is not None:
                self._values["service_profile_id"] = service_profile_id

        @builtins.property
        def abp_v10_x(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.AbpV10xProperty"]]:
            '''ABP device object for LoRaWAN specification v1.0.x.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x
            '''
            result = self._values.get("abp_v10_x")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.AbpV10xProperty"]], result)

        @builtins.property
        def abp_v11(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.AbpV11Property"]]:
            '''ABP device object for create APIs for v1.1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11
            '''
            result = self._values.get("abp_v11")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.AbpV11Property"]], result)

        @builtins.property
        def dev_eui(self) -> typing.Optional[builtins.str]:
            '''The DevEUI value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deveui
            '''
            result = self._values.get("dev_eui")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_profile_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the device profile for the new wireless device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid
            '''
            result = self._values.get("device_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def otaa_v10_x(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.OtaaV10xProperty"]]:
            '''OTAA device object for create APIs for v1.0.x.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x
            '''
            result = self._values.get("otaa_v10_x")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.OtaaV10xProperty"]], result)

        @builtins.property
        def otaa_v11(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.OtaaV11Property"]]:
            '''OTAA device object for v1.1 for create APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11
            '''
            result = self._values.get("otaa_v11")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWirelessDevice.OtaaV11Property"]], result)

        @builtins.property
        def service_profile_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the service profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid
            '''
            result = self._values.get("service_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANDeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDevice.OtaaV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"app_eui": "appEui", "app_key": "appKey"},
    )
    class OtaaV10xProperty:
        def __init__(self, *, app_eui: builtins.str, app_key: builtins.str) -> None:
            '''
            :param app_eui: The AppEUI value. You specify this value when using LoRaWAN versions v1.0.2 or v1.0.3.
            :param app_key: The AppKey value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                otaa_v10x_property = iotwireless.CfnWirelessDevice.OtaaV10xProperty(
                    app_eui="appEui",
                    app_key="appKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c6f728528b682776f461be6bf8de1ecea138fb90d8be311ecd7db6e21a872a5)
                check_type(argname="argument app_eui", value=app_eui, expected_type=type_hints["app_eui"])
                check_type(argname="argument app_key", value=app_key, expected_type=type_hints["app_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_eui": app_eui,
                "app_key": app_key,
            }

        @builtins.property
        def app_eui(self) -> builtins.str:
            '''The AppEUI value.

            You specify this value when using LoRaWAN versions v1.0.2 or v1.0.3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appeui
            '''
            result = self._values.get("app_eui")
            assert result is not None, "Required property 'app_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def app_key(self) -> builtins.str:
            '''The AppKey value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appkey
            '''
            result = self._values.get("app_key")
            assert result is not None, "Required property 'app_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtaaV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDevice.OtaaV11Property",
        jsii_struct_bases=[],
        name_mapping={"app_key": "appKey", "join_eui": "joinEui", "nwk_key": "nwkKey"},
    )
    class OtaaV11Property:
        def __init__(
            self,
            *,
            app_key: builtins.str,
            join_eui: builtins.str,
            nwk_key: builtins.str,
        ) -> None:
            '''OTAA device object for v1.1 for create APIs.

            :param app_key: The AppKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the AppKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param join_eui: The JoinEUI value.
            :param nwk_key: The NwkKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the NwkKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                otaa_v11_property = iotwireless.CfnWirelessDevice.OtaaV11Property(
                    app_key="appKey",
                    join_eui="joinEui",
                    nwk_key="nwkKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f6d8664fed104b7d07bc47a661096fbb46189f806c5b81cf0e8fb36eed4eb05)
                check_type(argname="argument app_key", value=app_key, expected_type=type_hints["app_key"])
                check_type(argname="argument join_eui", value=join_eui, expected_type=type_hints["join_eui"])
                check_type(argname="argument nwk_key", value=nwk_key, expected_type=type_hints["nwk_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_key": app_key,
                "join_eui": join_eui,
                "nwk_key": nwk_key,
            }

        @builtins.property
        def app_key(self) -> builtins.str:
            '''The AppKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the AppKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-appkey
            '''
            result = self._values.get("app_key")
            assert result is not None, "Required property 'app_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def join_eui(self) -> builtins.str:
            '''The JoinEUI value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-joineui
            '''
            result = self._values.get("join_eui")
            assert result is not None, "Required property 'join_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_key(self) -> builtins.str:
            '''The NwkKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the NwkKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-nwkkey
            '''
            result = self._values.get("nwk_key")
            assert result is not None, "Required property 'nwk_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtaaV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"app_s_key": "appSKey", "nwk_s_key": "nwkSKey"},
    )
    class SessionKeysAbpV10xProperty:
        def __init__(self, *, app_s_key: builtins.str, nwk_s_key: builtins.str) -> None:
            '''Session keys for ABP v1.0.x.

            :param app_s_key: The AppSKey value.
            :param nwk_s_key: The NwkKey value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                session_keys_abp_v10x_property = iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                    app_sKey="appSKey",
                    nwk_sKey="nwkSKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dedcdca7a2f761fdd916265e3946276cbb099297d1b724f7bb420d585d30380a)
                check_type(argname="argument app_s_key", value=app_s_key, expected_type=type_hints["app_s_key"])
                check_type(argname="argument nwk_s_key", value=nwk_s_key, expected_type=type_hints["nwk_s_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_s_key": app_s_key,
                "nwk_s_key": nwk_s_key,
            }

        @builtins.property
        def app_s_key(self) -> builtins.str:
            '''The AppSKey value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey
            '''
            result = self._values.get("app_s_key")
            assert result is not None, "Required property 'app_s_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_s_key(self) -> builtins.str:
            '''The NwkKey value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey
            '''
            result = self._values.get("nwk_s_key")
            assert result is not None, "Required property 'nwk_s_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionKeysAbpV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property",
        jsii_struct_bases=[],
        name_mapping={
            "app_s_key": "appSKey",
            "f_nwk_s_int_key": "fNwkSIntKey",
            "nwk_s_enc_key": "nwkSEncKey",
            "s_nwk_s_int_key": "sNwkSIntKey",
        },
    )
    class SessionKeysAbpV11Property:
        def __init__(
            self,
            *,
            app_s_key: builtins.str,
            f_nwk_s_int_key: builtins.str,
            nwk_s_enc_key: builtins.str,
            s_nwk_s_int_key: builtins.str,
        ) -> None:
            '''Session keys for ABP v1.1.

            :param app_s_key: The AppSKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the AppSKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param f_nwk_s_int_key: The FNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the FNwkSIntKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param nwk_s_enc_key: The NwkSEncKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the NwkSEncKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param s_nwk_s_int_key: The SNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the SNwkSIntKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                session_keys_abp_v11_property = iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                    app_sKey="appSKey",
                    f_nwk_sInt_key="fNwkSIntKey",
                    nwk_sEnc_key="nwkSEncKey",
                    s_nwk_sInt_key="sNwkSIntKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ddc0e655d9778b4919d40faf860f91332e540a826df9ed46a21a69dcbb3396e1)
                check_type(argname="argument app_s_key", value=app_s_key, expected_type=type_hints["app_s_key"])
                check_type(argname="argument f_nwk_s_int_key", value=f_nwk_s_int_key, expected_type=type_hints["f_nwk_s_int_key"])
                check_type(argname="argument nwk_s_enc_key", value=nwk_s_enc_key, expected_type=type_hints["nwk_s_enc_key"])
                check_type(argname="argument s_nwk_s_int_key", value=s_nwk_s_int_key, expected_type=type_hints["s_nwk_s_int_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_s_key": app_s_key,
                "f_nwk_s_int_key": f_nwk_s_int_key,
                "nwk_s_enc_key": nwk_s_enc_key,
                "s_nwk_s_int_key": s_nwk_s_int_key,
            }

        @builtins.property
        def app_s_key(self) -> builtins.str:
            '''The AppSKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the AppSKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey
            '''
            result = self._values.get("app_s_key")
            assert result is not None, "Required property 'app_s_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def f_nwk_s_int_key(self) -> builtins.str:
            '''The FNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the FNwkSIntKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey
            '''
            result = self._values.get("f_nwk_s_int_key")
            assert result is not None, "Required property 'f_nwk_s_int_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_s_enc_key(self) -> builtins.str:
            '''The NwkSEncKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the NwkSEncKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey
            '''
            result = self._values.get("nwk_s_enc_key")
            assert result is not None, "Required property 'nwk_s_enc_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s_nwk_s_int_key(self) -> builtins.str:
            '''The SNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the SNwkSIntKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey
            '''
            result = self._values.get("s_nwk_s_int_key")
            assert result is not None, "Required property 's_nwk_s_int_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionKeysAbpV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWirelessDeviceImportTask(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDeviceImportTask",
):
    '''Information about an import task for wireless devices.

    When creating the resource, either create a single wireless device import task using the Sidewalk manufacturing serial number (SMSN) of the wireless device, or create an import task for multiple devices by specifying both the ``DeviceCreationFile`` and the ``Role`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html
    :cloudformationResource: AWS::IoTWireless::WirelessDeviceImportTask
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_wireless_device_import_task = iotwireless.CfnWirelessDeviceImportTask(self, "MyCfnWirelessDeviceImportTask",
            destination_name="destinationName",
            sidewalk=iotwireless.CfnWirelessDeviceImportTask.SidewalkProperty(
                device_creation_file="deviceCreationFile",
                device_creation_file_list=["deviceCreationFileList"],
                role="role",
                sidewalk_manufacturing_sn="sidewalkManufacturingSn"
            ),
        
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
        destination_name: builtins.str,
        sidewalk: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessDeviceImportTask.SidewalkProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_name: The name of the destination that describes the IoT rule to route messages from the Sidewalk devices in the import task to other applications.
        :param sidewalk: The Sidewalk-related information of the wireless device import task.
        :param tags: Adds to or modifies the tags of the given resource. Tags are metadata that you can use to manage a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b81904b6ea4a40be4179e391a0bb52c165600b850295d5a6b580ad76ede92d3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWirelessDeviceImportTaskProps(
            destination_name=destination_name, sidewalk=sidewalk, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198856489aba15c5acfb8dfab7e2b4a71dc22d665121a8744c5ee52b5a33b0d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31463d1c87fa93be4bb6828c4ea87fb1b208830b87cc7a58cb158e2b3a492e7e)
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
        '''The ARN (Amazon Resource Name) of the import task.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The date and time at which the wireless device import task was created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrFailedImportedDevicesCount")
    def attr_failed_imported_devices_count(self) -> jsii.Number:
        '''The summary information of count of wireless devices that failed to onboard to the import task.

        :cloudformationAttribute: FailedImportedDevicesCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrFailedImportedDevicesCount"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The import task ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrInitializedImportedDevicesCount")
    def attr_initialized_imported_devices_count(self) -> jsii.Number:
        '''The summary information of count of wireless devices that are waiting for the control log to be added to an import task.

        :cloudformationAttribute: InitializedImportedDevicesCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrInitializedImportedDevicesCount"))

    @builtins.property
    @jsii.member(jsii_name="attrOnboardedImportedDevicesCount")
    def attr_onboarded_imported_devices_count(self) -> jsii.Number:
        '''The summary information of count of wireless devices that have been onboarded to the import task.

        :cloudformationAttribute: OnboardedImportedDevicesCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrOnboardedImportedDevicesCount"))

    @builtins.property
    @jsii.member(jsii_name="attrPendingImportedDevicesCount")
    def attr_pending_imported_devices_count(self) -> jsii.Number:
        '''The summary information of count of wireless devices that are waiting in the queue to be onboarded to the import task.

        :cloudformationAttribute: PendingImportedDevicesCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrPendingImportedDevicesCount"))

    @builtins.property
    @jsii.member(jsii_name="attrSidewalkDeviceCreationFileList")
    def attr_sidewalk_device_creation_file_list(self) -> typing.List[builtins.str]:
        '''List of Sidewalk devices that are added to the import task.

        :cloudformationAttribute: Sidewalk.DeviceCreationFileList
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSidewalkDeviceCreationFileList"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of a wireless device import task.

        The status can be ``INITIALIZING`` , ``INITIALIZED`` , ``PENDING`` , ``COMPLETE`` , ``FAILED`` , or ``DELETING`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''The reason that provides additional information about the import task status.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

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
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        '''The name of the destination that describes the IoT rule to route messages from the Sidewalk devices in the import task to other applications.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationName"))

    @destination_name.setter
    def destination_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ededfdd755af77ac21339c21b25ba1960365538a55f8efb323ccb407643c330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationName", value)

    @builtins.property
    @jsii.member(jsii_name="sidewalk")
    def sidewalk(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnWirelessDeviceImportTask.SidewalkProperty"]:
        '''The Sidewalk-related information of the wireless device import task.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWirelessDeviceImportTask.SidewalkProperty"], jsii.get(self, "sidewalk"))

    @sidewalk.setter
    def sidewalk(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnWirelessDeviceImportTask.SidewalkProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b94dcee288462d05aefdffb188ba06832b12dcea7d955f135c110c087bb3874)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sidewalk", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds to or modifies the tags of the given resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37f67b5df03fc789e404057fa4c7dc3cb0bf29a0dd71d20ccd91e499b959af24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDeviceImportTask.SidewalkProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_creation_file": "deviceCreationFile",
            "device_creation_file_list": "deviceCreationFileList",
            "role": "role",
            "sidewalk_manufacturing_sn": "sidewalkManufacturingSn",
        },
    )
    class SidewalkProperty:
        def __init__(
            self,
            *,
            device_creation_file: typing.Optional[builtins.str] = None,
            device_creation_file_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            role: typing.Optional[builtins.str] = None,
            sidewalk_manufacturing_sn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sidewalk-related information about a wireless device import task.

            :param device_creation_file: The CSV file contained in an S3 bucket that's used for adding devices to an import task.
            :param device_creation_file_list: List of Sidewalk devices that are added to the import task.
            :param role: The IAM role that allows AWS IoT Wireless to access the CSV file in the S3 bucket.
            :param sidewalk_manufacturing_sn: The Sidewalk manufacturing serial number (SMSN) of the Sidewalk device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                sidewalk_property = iotwireless.CfnWirelessDeviceImportTask.SidewalkProperty(
                    device_creation_file="deviceCreationFile",
                    device_creation_file_list=["deviceCreationFileList"],
                    role="role",
                    sidewalk_manufacturing_sn="sidewalkManufacturingSn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7674cfa92498ab342f9eac20d079b4999526cab4026edf48f0397de16cd53bd)
                check_type(argname="argument device_creation_file", value=device_creation_file, expected_type=type_hints["device_creation_file"])
                check_type(argname="argument device_creation_file_list", value=device_creation_file_list, expected_type=type_hints["device_creation_file_list"])
                check_type(argname="argument role", value=role, expected_type=type_hints["role"])
                check_type(argname="argument sidewalk_manufacturing_sn", value=sidewalk_manufacturing_sn, expected_type=type_hints["sidewalk_manufacturing_sn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if device_creation_file is not None:
                self._values["device_creation_file"] = device_creation_file
            if device_creation_file_list is not None:
                self._values["device_creation_file_list"] = device_creation_file_list
            if role is not None:
                self._values["role"] = role
            if sidewalk_manufacturing_sn is not None:
                self._values["sidewalk_manufacturing_sn"] = sidewalk_manufacturing_sn

        @builtins.property
        def device_creation_file(self) -> typing.Optional[builtins.str]:
            '''The CSV file contained in an S3 bucket that's used for adding devices to an import task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk-devicecreationfile
            '''
            result = self._values.get("device_creation_file")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_creation_file_list(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''List of Sidewalk devices that are added to the import task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk-devicecreationfilelist
            '''
            result = self._values.get("device_creation_file_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def role(self) -> typing.Optional[builtins.str]:
            '''The IAM role that allows AWS IoT Wireless to access the CSV file in the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk-role
            '''
            result = self._values.get("role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sidewalk_manufacturing_sn(self) -> typing.Optional[builtins.str]:
            '''The Sidewalk manufacturing serial number (SMSN) of the Sidewalk device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk-sidewalkmanufacturingsn
            '''
            result = self._values.get("sidewalk_manufacturing_sn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDeviceImportTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_name": "destinationName",
        "sidewalk": "sidewalk",
        "tags": "tags",
    },
)
class CfnWirelessDeviceImportTaskProps:
    def __init__(
        self,
        *,
        destination_name: builtins.str,
        sidewalk: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDeviceImportTask.SidewalkProperty, typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWirelessDeviceImportTask``.

        :param destination_name: The name of the destination that describes the IoT rule to route messages from the Sidewalk devices in the import task to other applications.
        :param sidewalk: The Sidewalk-related information of the wireless device import task.
        :param tags: Adds to or modifies the tags of the given resource. Tags are metadata that you can use to manage a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_wireless_device_import_task_props = iotwireless.CfnWirelessDeviceImportTaskProps(
                destination_name="destinationName",
                sidewalk=iotwireless.CfnWirelessDeviceImportTask.SidewalkProperty(
                    device_creation_file="deviceCreationFile",
                    device_creation_file_list=["deviceCreationFileList"],
                    role="role",
                    sidewalk_manufacturing_sn="sidewalkManufacturingSn"
                ),
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6e4053bc6cd657f874e13d1418635c416bc4ffa544969dd87a3e3f37282189)
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
            check_type(argname="argument sidewalk", value=sidewalk, expected_type=type_hints["sidewalk"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_name": destination_name,
            "sidewalk": sidewalk,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination_name(self) -> builtins.str:
        '''The name of the destination that describes the IoT rule to route messages from the Sidewalk devices in the import task to other applications.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html#cfn-iotwireless-wirelessdeviceimporttask-destinationname
        '''
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sidewalk(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnWirelessDeviceImportTask.SidewalkProperty]:
        '''The Sidewalk-related information of the wireless device import task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk
        '''
        result = self._values.get("sidewalk")
        assert result is not None, "Required property 'sidewalk' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnWirelessDeviceImportTask.SidewalkProperty], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds to or modifies the tags of the given resource.

        Tags are metadata that you can use to manage a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html#cfn-iotwireless-wirelessdeviceimporttask-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessDeviceImportTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_name": "destinationName",
        "type": "type",
        "description": "description",
        "last_uplink_received_at": "lastUplinkReceivedAt",
        "lo_ra_wan": "loRaWan",
        "name": "name",
        "positioning": "positioning",
        "tags": "tags",
        "thing_arn": "thingArn",
    },
)
class CfnWirelessDeviceProps:
    def __init__(
        self,
        *,
        destination_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.LoRaWANDeviceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        positioning: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWirelessDevice``.

        :param destination_name: The name of the destination to assign to the new wireless device. Can have only have alphanumeric, - (hyphen) and _ (underscore) characters and it can't have any spaces.
        :param type: The wireless device type.
        :param description: The description of the new resource. Maximum length is 2048.
        :param last_uplink_received_at: The date and time when the most recent uplink was received.
        :param lo_ra_wan: The device configuration information to use to create the wireless device. Must be at least one of OtaaV10x, OtaaV11, AbpV11, or AbpV10x.
        :param name: The name of the new resource.
        :param positioning: FPort values for the GNSS, Stream, and ClockSync functions of the positioning information.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param thing_arn: The ARN of the thing to associate with the wireless device.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_wireless_device_props = iotwireless.CfnWirelessDeviceProps(
                destination_name="destinationName",
                type="type",
            
                # the properties below are optional
                description="description",
                last_uplink_received_at="lastUplinkReceivedAt",
                lo_ra_wan=iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty(
                    abp_v10_x=iotwireless.CfnWirelessDevice.AbpV10xProperty(
                        dev_addr="devAddr",
                        session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                            app_sKey="appSKey",
                            nwk_sKey="nwkSKey"
                        )
                    ),
                    abp_v11=iotwireless.CfnWirelessDevice.AbpV11Property(
                        dev_addr="devAddr",
                        session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                            app_sKey="appSKey",
                            f_nwk_sInt_key="fNwkSIntKey",
                            nwk_sEnc_key="nwkSEncKey",
                            s_nwk_sInt_key="sNwkSIntKey"
                        )
                    ),
                    dev_eui="devEui",
                    device_profile_id="deviceProfileId",
                    otaa_v10_x=iotwireless.CfnWirelessDevice.OtaaV10xProperty(
                        app_eui="appEui",
                        app_key="appKey"
                    ),
                    otaa_v11=iotwireless.CfnWirelessDevice.OtaaV11Property(
                        app_key="appKey",
                        join_eui="joinEui",
                        nwk_key="nwkKey"
                    ),
                    service_profile_id="serviceProfileId"
                ),
                name="name",
                positioning="positioning",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                thing_arn="thingArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c132064eaadc8906efb4c94784760c71f0e1de304300dc1e66377c449d5892ee)
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument last_uplink_received_at", value=last_uplink_received_at, expected_type=type_hints["last_uplink_received_at"])
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument positioning", value=positioning, expected_type=type_hints["positioning"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_name": destination_name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if last_uplink_received_at is not None:
            self._values["last_uplink_received_at"] = last_uplink_received_at
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if positioning is not None:
            self._values["positioning"] = positioning
        if tags is not None:
            self._values["tags"] = tags
        if thing_arn is not None:
            self._values["thing_arn"] = thing_arn

    @builtins.property
    def destination_name(self) -> builtins.str:
        '''The name of the destination to assign to the new wireless device.

        Can have only have alphanumeric, - (hyphen) and _ (underscore) characters and it can't have any spaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname
        '''
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The wireless device type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        Maximum length is 2048.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''The date and time when the most recent uplink was received.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lastuplinkreceivedat
        '''
        result = self._values.get("last_uplink_received_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWirelessDevice.LoRaWANDeviceProperty]]:
        '''The device configuration information to use to create the wireless device.

        Must be at least one of OtaaV10x, OtaaV11, AbpV11, or AbpV10x.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWirelessDevice.LoRaWANDeviceProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def positioning(self) -> typing.Optional[builtins.str]:
        '''FPort values for the GNSS, Stream, and ClockSync functions of the positioning information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-positioning
        '''
        result = self._values.get("positioning")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the thing to associate with the wireless device.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-thingarn
        '''
        result = self._values.get("thing_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWirelessGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessGateway",
):
    '''Provisions a wireless gateway.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
    :cloudformationResource: AWS::IoTWireless::WirelessGateway
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotwireless as iotwireless
        
        cfn_wireless_gateway = iotwireless.CfnWirelessGateway(self, "MyCfnWirelessGateway",
            lo_ra_wan=iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty(
                gateway_eui="gatewayEui",
                rf_region="rfRegion"
            ),
        
            # the properties below are optional
            description="description",
            last_uplink_received_at="lastUplinkReceivedAt",
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            thing_arn="thingArn",
            thing_name="thingName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWirelessGateway.LoRaWANGatewayProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param lo_ra_wan: The gateway configuration information to use to create the wireless gateway.
        :param description: The description of the new resource. The maximum length is 2048 characters.
        :param last_uplink_received_at: The date and time when the most recent uplink was received.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param thing_arn: The ARN of the thing to associate with the wireless gateway.
        :param thing_name: The name of the thing associated with the wireless gateway. The value is empty if a thing isn't associated with the gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83cf451292782ed7cf2ebb2ff51643f50a0853d30208d953201e94c64036e0de)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWirelessGatewayProps(
            lo_ra_wan=lo_ra_wan,
            description=description,
            last_uplink_received_at=last_uplink_received_at,
            name=name,
            tags=tags,
            thing_arn=thing_arn,
            thing_name=thing_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69dede8ca1182ed73a8de2fda4268a2b26721b01a1dca9ad4762a6b85fc46a7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__25b4ec1cc0c08824c4c5350c2f1641929aa02b1e3dc040cd37dc55da56700ac0)
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
        '''The ARN of the wireless gateway created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the wireless gateway created.

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
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnWirelessGateway.LoRaWANGatewayProperty"]:
        '''The gateway configuration information to use to create the wireless gateway.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWirelessGateway.LoRaWANGatewayProperty"], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnWirelessGateway.LoRaWANGatewayProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbc33250d661f7557837e50ada87180167d8574118707d139d2eb4fa49602882)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eca333f4fa126f8730b33bcbb64820d18aa68f08be068891c6a435cd321aa4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="lastUplinkReceivedAt")
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''The date and time when the most recent uplink was received.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastUplinkReceivedAt"))

    @last_uplink_received_at.setter
    def last_uplink_received_at(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__900eeac2e5cfdb156d0e28f493a73b729234aa361c7336134d543a0a22f3b460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastUplinkReceivedAt", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc344d26426421b59939c05527ffa4450645002aaa7008eec620471cb3665ac8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__493d37495ffc45845617d2e1ba953b01719cb48c69682d0a6e27d0773456852b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="thingArn")
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the thing to associate with the wireless gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingArn"))

    @thing_arn.setter
    def thing_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff85efe4d13e96f495f18cda698b13ce262995db3a45e1f87de3a4d37d73aff8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingArn", value)

    @builtins.property
    @jsii.member(jsii_name="thingName")
    def thing_name(self) -> typing.Optional[builtins.str]:
        '''The name of the thing associated with the wireless gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingName"))

    @thing_name.setter
    def thing_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3306c2dcc0fb9f5711e347f7795bc7c414ed553dac4e7c1a4de936a98fb073ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty",
        jsii_struct_bases=[],
        name_mapping={"gateway_eui": "gatewayEui", "rf_region": "rfRegion"},
    )
    class LoRaWANGatewayProperty:
        def __init__(
            self,
            *,
            gateway_eui: builtins.str,
            rf_region: builtins.str,
        ) -> None:
            '''LoRaWAN wireless gateway object.

            :param gateway_eui: The gateway's EUI value.
            :param rf_region: The frequency band (RFRegion) value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotwireless as iotwireless
                
                lo_ra_wANGateway_property = iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty(
                    gateway_eui="gatewayEui",
                    rf_region="rfRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ddc162c67799ffa5b9f0b75305d65763275f726ca096abf2be6e97d8d5507d8a)
                check_type(argname="argument gateway_eui", value=gateway_eui, expected_type=type_hints["gateway_eui"])
                check_type(argname="argument rf_region", value=rf_region, expected_type=type_hints["rf_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "gateway_eui": gateway_eui,
                "rf_region": rf_region,
            }

        @builtins.property
        def gateway_eui(self) -> builtins.str:
            '''The gateway's EUI value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui
            '''
            result = self._values.get("gateway_eui")
            assert result is not None, "Required property 'gateway_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rf_region(self) -> builtins.str:
            '''The frequency band (RFRegion) value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion
            '''
            result = self._values.get("rf_region")
            assert result is not None, "Required property 'rf_region' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANGatewayProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotwireless.CfnWirelessGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "lo_ra_wan": "loRaWan",
        "description": "description",
        "last_uplink_received_at": "lastUplinkReceivedAt",
        "name": "name",
        "tags": "tags",
        "thing_arn": "thingArn",
        "thing_name": "thingName",
    },
)
class CfnWirelessGatewayProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessGateway.LoRaWANGatewayProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWirelessGateway``.

        :param lo_ra_wan: The gateway configuration information to use to create the wireless gateway.
        :param description: The description of the new resource. The maximum length is 2048 characters.
        :param last_uplink_received_at: The date and time when the most recent uplink was received.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param thing_arn: The ARN of the thing to associate with the wireless gateway.
        :param thing_name: The name of the thing associated with the wireless gateway. The value is empty if a thing isn't associated with the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotwireless as iotwireless
            
            cfn_wireless_gateway_props = iotwireless.CfnWirelessGatewayProps(
                lo_ra_wan=iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty(
                    gateway_eui="gatewayEui",
                    rf_region="rfRegion"
                ),
            
                # the properties below are optional
                description="description",
                last_uplink_received_at="lastUplinkReceivedAt",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                thing_arn="thingArn",
                thing_name="thingName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c638b98661b74de194655d6ea9f1ffd6ff2285ebce875290921403545f2fde80)
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument last_uplink_received_at", value=last_uplink_received_at, expected_type=type_hints["last_uplink_received_at"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
            check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lo_ra_wan": lo_ra_wan,
        }
        if description is not None:
            self._values["description"] = description
        if last_uplink_received_at is not None:
            self._values["last_uplink_received_at"] = last_uplink_received_at
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if thing_arn is not None:
            self._values["thing_arn"] = thing_arn
        if thing_name is not None:
            self._values["thing_name"] = thing_name

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnWirelessGateway.LoRaWANGatewayProperty]:
        '''The gateway configuration information to use to create the wireless gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        assert result is not None, "Required property 'lo_ra_wan' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnWirelessGateway.LoRaWANGatewayProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        The maximum length is 2048 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''The date and time when the most recent uplink was received.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lastuplinkreceivedat
        '''
        result = self._values.get("last_uplink_received_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the thing to associate with the wireless gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingarn
        '''
        result = self._values.get("thing_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thing_name(self) -> typing.Optional[builtins.str]:
        '''The name of the thing associated with the wireless gateway.

        The value is empty if a thing isn't associated with the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingname
        '''
        result = self._values.get("thing_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDestination",
    "CfnDestinationProps",
    "CfnDeviceProfile",
    "CfnDeviceProfileProps",
    "CfnFuotaTask",
    "CfnFuotaTaskProps",
    "CfnMulticastGroup",
    "CfnMulticastGroupProps",
    "CfnNetworkAnalyzerConfiguration",
    "CfnNetworkAnalyzerConfigurationProps",
    "CfnPartnerAccount",
    "CfnPartnerAccountProps",
    "CfnServiceProfile",
    "CfnServiceProfileProps",
    "CfnTaskDefinition",
    "CfnTaskDefinitionProps",
    "CfnWirelessDevice",
    "CfnWirelessDeviceImportTask",
    "CfnWirelessDeviceImportTaskProps",
    "CfnWirelessDeviceProps",
    "CfnWirelessGateway",
    "CfnWirelessGatewayProps",
]

publication.publish()

def _typecheckingstub__f61ecfaf93e3a5ee3c176667153d7633c25d7bc246a1af5b6801966503ffc10e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    expression: builtins.str,
    expression_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abcdef1ef5b37ae8d863fbd6e43535b7b8fb98b01e8f63d2e11a2ac69ae40d2b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daceed9db31617342b2ad6da1a597d489d32ddd44aa99d40185846a28691e1a6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0635097b142a55f017574117ff21a283060521e721f605e4ff6e5a9ed13e63d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52fb059cb57908dccbf654243c0e24547fefae3afcee7f9441366e93f7368f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4a7e2be1c3626a0831a317f8384bfaac10f081d96e1d52fdf7e7d168b531e14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54343b07a7027d746812e326d1dd346e2f583fb1042ea98ffa3720e14655d56f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b60aa4ef5f47c4662f7208269db494d81166701afac30be03ebe87711d08ef4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28773e7cb2f78fe606bd46c478d428f25a9d6768b2384a0d5eabc8886d06f5d4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7257e0c4b674f84972a8cd47754e3ce09588804469529ea8a4efd68a9ae0aae(
    *,
    expression: builtins.str,
    expression_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8067f9295f2cbc045aef3949460556f66763c80bd130293a84c601e6d1cc0b67(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e5a8081b4b2646cf2e301e2afffc795ab7e32d6a6b52b07e5de54e172bbe245(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23fa48b9862be61ca24ddc5be9d3d852c088e91af603908b772a0f6b98d3bb60(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37bc58d63a4729db23e942a768b31134889d07403a53d90d57a88c269501d5fa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeviceProfile.LoRaWANDeviceProfileProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25caee2a3bcdb77269d5e10d73ce9e629c40f7a63107b51012a8ae652ea849bf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4afbd69995e29e676f14b8919081a76892c1a3dd232747696d84a67dd728424a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0558c6321ef1b0db79fd3fb29f490ef770458d60ef008b53201feac226735893(
    *,
    class_b_timeout: typing.Optional[jsii.Number] = None,
    class_c_timeout: typing.Optional[jsii.Number] = None,
    factory_preset_freqs_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
    mac_version: typing.Optional[builtins.str] = None,
    max_duty_cycle: typing.Optional[jsii.Number] = None,
    max_eirp: typing.Optional[jsii.Number] = None,
    ping_slot_dr: typing.Optional[jsii.Number] = None,
    ping_slot_freq: typing.Optional[jsii.Number] = None,
    ping_slot_period: typing.Optional[jsii.Number] = None,
    reg_params_revision: typing.Optional[builtins.str] = None,
    rf_region: typing.Optional[builtins.str] = None,
    rx_data_rate2: typing.Optional[jsii.Number] = None,
    rx_delay1: typing.Optional[jsii.Number] = None,
    rx_dr_offset1: typing.Optional[jsii.Number] = None,
    rx_freq2: typing.Optional[jsii.Number] = None,
    supports32_bit_f_cnt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    supports_class_b: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    supports_class_c: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    supports_join: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5943b1bf4799db06aae66d299d5e86b23f1003e16376a69594302b4e4054ee8(
    *,
    lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dc14d9e108784569e33639b9546be6bf6547039fdbf1476a6e6dc24a391c8ec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    firmware_update_image: builtins.str,
    firmware_update_role: builtins.str,
    lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFuotaTask.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
    associate_multicast_group: typing.Optional[builtins.str] = None,
    associate_wireless_device: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disassociate_multicast_group: typing.Optional[builtins.str] = None,
    disassociate_wireless_device: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b980d91ff24dc028c16177ae311632139802ed07c63559bc60b6b0a7017f8724(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e7b39665fb6873e720d392fdd079f7eb20ed523e0aa7f027788b71f4f36fa0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c1e683ef261ca9a0e323098857bde336b7b232a1debbe4ce45dedb26ca8745(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__461c299fc6e5ef170d9d68ec3a0d4fd23e292ad17e487e422fa0ced5654b660c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ced8500df8e27b1785fe0afc435e424754dde0dc634914ed9fd44ab5b30ce8(
    value: typing.Union[_IResolvable_da3f097b, CfnFuotaTask.LoRaWANProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d57cfccba3878e495806e2629c1b347cbfd7e7defe8b5465dd6bb995d141ac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__379374179bd98cbed6826061ba79e2ccdcb8f9d331dfad677cfb8ed97f739ee4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd259b9067a68c41327baaabf15d262b9fb84d09030f1cf4a7f0dd8e202ee92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01c498cd349d14eb10d07e4f5e44c09c897b78b93d259561e5a16ba5e042381(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9cb4e1ac40f6c4cb8557e33d35c0e1b17c7dca5a1e5af474d269743b81f4c32(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eacacaf44fc0b79b61f7bfe0ff15f515d32d411b03d265dc1950da37d4e1df4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af87398fea4c8098bb165637d1ed67059206096bfeaa74f0f7e4bc4f155438a5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94393e5e1d51d161120515f2e9774caa190b7efe4ebfe8fa4779de1b04a5107(
    *,
    rf_region: builtins.str,
    start_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c3e107aa1ac02161284f43f789dead141c5600532a3e5692ad63f38b6fe334(
    *,
    firmware_update_image: builtins.str,
    firmware_update_role: builtins.str,
    lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFuotaTask.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
    associate_multicast_group: typing.Optional[builtins.str] = None,
    associate_wireless_device: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disassociate_multicast_group: typing.Optional[builtins.str] = None,
    disassociate_wireless_device: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6fc3915d7fdc89e5cd965ebe2f8ae8013d87d86fae4860debc0123a0b130f24(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMulticastGroup.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
    associate_wireless_device: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disassociate_wireless_device: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea85117dcaae87f7c258e9db5b97562bfa9d3134ac4257066b0b99c150b670a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fcd2888d21219d187de015a688eab431ac6138768b481256a7336154497d286(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c294e487d95b07e085a91c7f8a13feb7802783382655634e559a8b45c99c8ed1(
    value: typing.Union[_IResolvable_da3f097b, CfnMulticastGroup.LoRaWANProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae2c095360e3b3956ec27a5a0391c8b9c6a1066c9419e78b18a128b1dce39cd3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8546711d1c48df42c3459de0d74a8bd074a39920589e487cf369cb45db970959(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c14cccbedbde81f7eab76271cf8904f266f0740eeae3b16d6d56f4c841f9bf2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9827482ae6bbc3367a4ad1ad70db1f6720ac74a9a8bff8d777c1b9974f2a0c22(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27a605465487f3c8166eed5c794a991aa0323a4e726e6135514d21538a40f38a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a226fea2e98276efaf2b644d1722fe1463b41172c734829c58e4752c3acd34f5(
    *,
    dl_class: builtins.str,
    rf_region: builtins.str,
    number_of_devices_in_group: typing.Optional[jsii.Number] = None,
    number_of_devices_requested: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c4e6fa1a2a0807dcecf7101bb34c083b7ea47e91b475851efefdc2219a41c6d(
    *,
    lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMulticastGroup.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
    associate_wireless_device: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disassociate_wireless_device: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef76e8561696d18827326b858a29c7a5bd71d6c55e2e8bf310bff5db6a892786(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trace_content: typing.Any = None,
    wireless_devices: typing.Optional[typing.Sequence[builtins.str]] = None,
    wireless_gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb735453542fc1eee5534899adaa88277e0a12f532d40466da5d9007b540f43c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d3ff277ab1c23aa596a504d2383a5cf86d5bc2401250de37145267f78d0739(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c86a3d802557338c300cca0ece6752eb71025ac87c6ef07829166d2ff477df9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93e1a9911115880ebf27f7267ad38fa5bce7c66abe33ebbe75b2bf22eabf9156(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b46f409840f000384f5933335a3a3f6ca1fc64ffa82bf977e2ecf1eab8bb21e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec63757a5145f99a0f5ef3d5b25bbe5becfee81e77d099ee2f39369f195858f6(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345530c2c6feaa99816a9ee99013b64ff606afb8afa94b821fff9b5acdaf603b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a89da82bb29c60f2cbd481009d94f8a49db119e080583ebad6fe6b40308f21(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45bcacb642e8b830d381b062a8db3fed1fc9995b8d0083e17def729766ceaa1f(
    *,
    log_level: typing.Optional[builtins.str] = None,
    wireless_device_frame_info: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de35d2504c45d0e78e2b671e6fad33a1e14e8aa548b7e508caaa7a23bf523bd5(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trace_content: typing.Any = None,
    wireless_devices: typing.Optional[typing.Sequence[builtins.str]] = None,
    wireless_gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23050117a6e6495f26306a5fff82479bd5fc0476b02f8ebd675aaba8825caf23(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_linked: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    partner_account_id: typing.Optional[builtins.str] = None,
    partner_type: typing.Optional[builtins.str] = None,
    sidewalk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkAccountInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sidewalk_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sidewalk_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkUpdateAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__614820e59436cd5cb89f1931fa964da150fbdf2e6b823323674e6cef8ab4bb79(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7087c5f1c74d1220271f38d1f9ff76843a565709c5a8c4011156d03dc8163b3a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aaf826ad1c2a370b17963e90c6207f7bb7314d3e7dc5cae931ff248746ba3fa(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e0bac11a48ea18aaab6b58e90043f92d7be541f658cdee62741f6c3c496ad6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b67a184faefbbc21a96bb714ed21601a9e1f59ee99b131697db7927e94ab59(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dfc9914aae89e0f8eb197d8ffe2bc096aa60a82245d8f1a8724edd051f7d100(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkAccountInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe1611d5cb899b19b3746136128a84710ec89f4b9d8628afa53281d1714b6abb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e0971bf93851f4e3f9a7278252a08cda6e44ea93a8e7a0b793f3aa5bc028fa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnerAccount.SidewalkUpdateAccountProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5c265354d811dc09b785b9e46927998e11bca13038834b76f0874d18d38cfa(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2026302496a7f825e68ebe0f409dc67f03e56d91b85c6e9620df1d14531c2cd8(
    *,
    app_server_private_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad67c351551efbad19725dfc18b31f0e8ac440e2de3a4b1505f542c76cb7dd5(
    *,
    amazon_id: typing.Optional[builtins.str] = None,
    arn: typing.Optional[builtins.str] = None,
    fingerprint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419d83ee7d8c9559933db42ce308a1fff6731f91c044b636c9b8c0111ed95630(
    *,
    app_server_private_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c81ac7b24f2d30b6f882858ea510845d9241758d5fd74e60160c9d089bc1de6(
    *,
    account_linked: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    partner_account_id: typing.Optional[builtins.str] = None,
    partner_type: typing.Optional[builtins.str] = None,
    sidewalk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkAccountInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sidewalk_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sidewalk_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnerAccount.SidewalkUpdateAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca074f221eda320f2c5d116c9446f9cd7110e09a78394cec71fb5ba026bbf22d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceProfile.LoRaWANServiceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__315dce048c406077b559684777c77b5922185f7618f6e7f04028b47d32b7baf3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3507ca4e4302d93d3394415217c34a0e9785c7d2280e3ed5952192a94d1fe9eb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12a1731df94a26c15c2c629e69f05069e78147796ed92c827d35da4720ce385(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceProfile.LoRaWANServiceProfileProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__495ecf85f557b8fb320530fa172728080da4333c5d1daf49554895e2ede03448(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e06c705f6bfd3ea15e35dda8a1e29b0c43e6f15d22947389e98e820e46ad578(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e153375dd84b74afa9419878247da802f9f8a8a199383f8d5fd7a83461c9d9(
    *,
    add_gw_metadata: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    channel_mask: typing.Optional[builtins.str] = None,
    dev_status_req_freq: typing.Optional[jsii.Number] = None,
    dl_bucket_size: typing.Optional[jsii.Number] = None,
    dl_rate: typing.Optional[jsii.Number] = None,
    dl_rate_policy: typing.Optional[builtins.str] = None,
    dr_max: typing.Optional[jsii.Number] = None,
    dr_min: typing.Optional[jsii.Number] = None,
    hr_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    min_gw_diversity: typing.Optional[jsii.Number] = None,
    nwk_geo_loc: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    pr_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ra_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    report_dev_status_battery: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    report_dev_status_margin: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    target_per: typing.Optional[jsii.Number] = None,
    ul_bucket_size: typing.Optional[jsii.Number] = None,
    ul_rate: typing.Optional[jsii.Number] = None,
    ul_rate_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c50b2c760a33d8243522ebcd46655f17e5c27bf15d6038dbf0c68cf36232ecb(
    *,
    lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceProfile.LoRaWANServiceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d10e64d4deea928b0f793f0894101d94fa8dbafc82f1f64d5fabc09fe26aca6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_create_tasks: typing.Union[builtins.bool, _IResolvable_da3f097b],
    lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_definition_type: typing.Optional[builtins.str] = None,
    update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9de16cdf43d0eedc9a4ca88788b721ffd3a0f35e0585fe70fc2a8d9d2f698aaa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce022de682a811bfe3b20f7d040c6f58cab74a9722d6b628e9086aee7a863dc8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2140f6dd2fd5b773e37d8f7300ca14605b82d89631076e6aa400f13c633cc9(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba999a41533710976a33b0a1023c1222f1541c811f550a29499fa6d5675bf40(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb88f2db89785cd3e23338b9b79cdcdfeb8e47dcfc703bccb73087cc7c530dac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__302c9856183cfc94540db93d88e4bc1e952c85bd9598afb0ef7bed2bc6a84411(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fd5d538e8d4ed460e65c9ddac2d1d68fd4345c4afe7e403b77fa77f80136dee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7873ddd4c5f9c059a1c30910bb0374ee468e180657a2870e1598db17895e714b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eead759e83004a38194e11d8a25d0f709bff70ca8565202c9519e20c74bbb29(
    *,
    model: typing.Optional[builtins.str] = None,
    package_version: typing.Optional[builtins.str] = None,
    station: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc21f41ee9ebd8dda0283e11946044bf70b6c27b33a3abce3ff415c7ff703f6(
    *,
    current_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.LoRaWANGatewayVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sig_key_crc: typing.Optional[jsii.Number] = None,
    update_signature: typing.Optional[builtins.str] = None,
    update_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.LoRaWANGatewayVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6341594bc267055b9e38191ae8ee71808f7e74d40bfa33ef01f6c1710119fe9(
    *,
    current_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.LoRaWANGatewayVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    update_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.LoRaWANGatewayVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2395a28ee7e4fa7cb268ed190fa8f9e55566832b4de59e0f97aadf1c082f3ac7(
    *,
    lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    update_data_role: typing.Optional[builtins.str] = None,
    update_data_source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__375ac4d1ecfc288b9e4e324b136b3fca6fc5ce7a227ca417eea320f867d83eaa(
    *,
    auto_create_tasks: typing.Union[builtins.bool, _IResolvable_da3f097b],
    lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_definition_type: typing.Optional[builtins.str] = None,
    update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a785469cac62290b28ca4347d5562cd8f4e0d3d2543a08bb415fcdfcda69c6e6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    last_uplink_received_at: typing.Optional[builtins.str] = None,
    lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.LoRaWANDeviceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    positioning: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    thing_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c3f9623871804482a281e90ea9c41a1af250f5169c286db6bc7ab0e057fb788(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac17e63441404903d9dae8730314dcfb4bdedf123d43ee74bc1d52bf06f9c24(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8061cf48768d2d28b9433ea6b1db3222bac9893ee1a0c96bcdb98226cc2f3d03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b70c988e1950493c52e44208f809dafc1d545d18b89e9e2227674650c390bc4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fc0b1687f73dd9eca4c02d192704c2293c20941495c350b0e122eea76052901(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6eb1d5a6add55c4de31d6a02d93e5a6c7b8f13ebd8c3e95893448a2464af2a4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a9387fe5c912c19442cf1a22d4b80b3bfec7bfaeaeedfde3a48464707ac5e94(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWirelessDevice.LoRaWANDeviceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79b8e8d3143dce00df934e2b0287a3a53fc9839551772e6cc273d592d0bc262f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c7b7fcf5ba7730b0ce3b8c924fe1fe208985f6c0d4fd68b55353bbe9d05b61(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de98087af9f5a2df8b9078aef4604fb7a5d9b8ce62eab7c135763cdcf4911075(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1062e2a4111f3f10850a14272256ebd97067e00cf02bb987304ac070474dc47f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3c7c33ac394ea769fdff09d74d18df5199694a0b192de0112bc6fc8bad01ac(
    *,
    dev_addr: builtins.str,
    session_keys: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.SessionKeysAbpV10xProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d86251ec9e15886b39ab32d3b20d4a624d17a6f00dd271dfc743f0d050ca1e(
    *,
    dev_addr: builtins.str,
    session_keys: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.SessionKeysAbpV11Property, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79b613fcb6e4bec4dd04e0ec3aefb63244dbaff286fed6d7327bebfa7aed6cba(
    *,
    abp_v10_x: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.AbpV10xProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    abp_v11: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.AbpV11Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    dev_eui: typing.Optional[builtins.str] = None,
    device_profile_id: typing.Optional[builtins.str] = None,
    otaa_v10_x: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.OtaaV10xProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    otaa_v11: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.OtaaV11Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_profile_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c6f728528b682776f461be6bf8de1ecea138fb90d8be311ecd7db6e21a872a5(
    *,
    app_eui: builtins.str,
    app_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6d8664fed104b7d07bc47a661096fbb46189f806c5b81cf0e8fb36eed4eb05(
    *,
    app_key: builtins.str,
    join_eui: builtins.str,
    nwk_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dedcdca7a2f761fdd916265e3946276cbb099297d1b724f7bb420d585d30380a(
    *,
    app_s_key: builtins.str,
    nwk_s_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc0e655d9778b4919d40faf860f91332e540a826df9ed46a21a69dcbb3396e1(
    *,
    app_s_key: builtins.str,
    f_nwk_s_int_key: builtins.str,
    nwk_s_enc_key: builtins.str,
    s_nwk_s_int_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b81904b6ea4a40be4179e391a0bb52c165600b850295d5a6b580ad76ede92d3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_name: builtins.str,
    sidewalk: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDeviceImportTask.SidewalkProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198856489aba15c5acfb8dfab7e2b4a71dc22d665121a8744c5ee52b5a33b0d1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31463d1c87fa93be4bb6828c4ea87fb1b208830b87cc7a58cb158e2b3a492e7e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ededfdd755af77ac21339c21b25ba1960365538a55f8efb323ccb407643c330(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b94dcee288462d05aefdffb188ba06832b12dcea7d955f135c110c087bb3874(
    value: typing.Union[_IResolvable_da3f097b, CfnWirelessDeviceImportTask.SidewalkProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f67b5df03fc789e404057fa4c7dc3cb0bf29a0dd71d20ccd91e499b959af24(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7674cfa92498ab342f9eac20d079b4999526cab4026edf48f0397de16cd53bd(
    *,
    device_creation_file: typing.Optional[builtins.str] = None,
    device_creation_file_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    role: typing.Optional[builtins.str] = None,
    sidewalk_manufacturing_sn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6e4053bc6cd657f874e13d1418635c416bc4ffa544969dd87a3e3f37282189(
    *,
    destination_name: builtins.str,
    sidewalk: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDeviceImportTask.SidewalkProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c132064eaadc8906efb4c94784760c71f0e1de304300dc1e66377c449d5892ee(
    *,
    destination_name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    last_uplink_received_at: typing.Optional[builtins.str] = None,
    lo_ra_wan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessDevice.LoRaWANDeviceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    positioning: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    thing_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83cf451292782ed7cf2ebb2ff51643f50a0853d30208d953201e94c64036e0de(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessGateway.LoRaWANGatewayProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    last_uplink_received_at: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    thing_arn: typing.Optional[builtins.str] = None,
    thing_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69dede8ca1182ed73a8de2fda4268a2b26721b01a1dca9ad4762a6b85fc46a7b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25b4ec1cc0c08824c4c5350c2f1641929aa02b1e3dc040cd37dc55da56700ac0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbc33250d661f7557837e50ada87180167d8574118707d139d2eb4fa49602882(
    value: typing.Union[_IResolvable_da3f097b, CfnWirelessGateway.LoRaWANGatewayProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eca333f4fa126f8730b33bcbb64820d18aa68f08be068891c6a435cd321aa4d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__900eeac2e5cfdb156d0e28f493a73b729234aa361c7336134d543a0a22f3b460(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc344d26426421b59939c05527ffa4450645002aaa7008eec620471cb3665ac8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__493d37495ffc45845617d2e1ba953b01719cb48c69682d0a6e27d0773456852b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff85efe4d13e96f495f18cda698b13ce262995db3a45e1f87de3a4d37d73aff8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3306c2dcc0fb9f5711e347f7795bc7c414ed553dac4e7c1a4de936a98fb073ac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc162c67799ffa5b9f0b75305d65763275f726ca096abf2be6e97d8d5507d8a(
    *,
    gateway_eui: builtins.str,
    rf_region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c638b98661b74de194655d6ea9f1ffd6ff2285ebce875290921403545f2fde80(
    *,
    lo_ra_wan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWirelessGateway.LoRaWANGatewayProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    last_uplink_received_at: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    thing_arn: typing.Optional[builtins.str] = None,
    thing_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
