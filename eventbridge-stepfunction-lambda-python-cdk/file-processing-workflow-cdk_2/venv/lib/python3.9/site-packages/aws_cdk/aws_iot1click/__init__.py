'''
# AWS IoT 1-Click Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iot1click as iot1click
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoT1Click construct libraries](https://constructs.dev/search?q=iot1click)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoT1Click resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoT1Click.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoT1Click](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoT1Click.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDevice(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot1click.CfnDevice",
):
    '''The ``AWS::IoT1Click::Device`` resource controls the enabled state of an AWS IoT 1-Click compatible device.

    For more information, see `Device <https://docs.aws.amazon.com/iot-1-click/1.0/devices-apireference/devices-deviceid.html>`_ in the *AWS IoT 1-Click Devices API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot1click as iot1click
        
        cfn_device = iot1click.CfnDevice(self, "MyCfnDevice",
            device_id="deviceId",
            enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        device_id: builtins.str,
        enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param device_id: The ID of the device, such as ``G030PX0312744DWM`` .
        :param enabled: A Boolean value indicating whether the device is enabled ( ``true`` ) or not ( ``false`` ).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a339667885af529b8cd8c8d1e0a01ab39b4df8c37caaa4e780eaac7c2f9666f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeviceProps(device_id=device_id, enabled=enabled)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c208db47e9fcc79bcc2e61f32b9c12a92a8fd2fbe37297fb8a7f35416fff32e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0937e66cec46366bbf925d7a3705e020a00ac7868787dc36d1cfa4978d429e56)
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
        '''The ARN of the device, such as ``arn:aws:iot1click:us-west-2:123456789012:devices/G030PX0312744DWM`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDeviceId")
    def attr_device_id(self) -> builtins.str:
        '''The unique identifier of the device.

        :cloudformationAttribute: DeviceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeviceId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnabled")
    def attr_enabled(self) -> _IResolvable_da3f097b:
        '''A Boolean value indicating whether the device is enabled ( ``true`` ) or not ( ``false`` ).

        :cloudformationAttribute: Enabled
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEnabled"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="deviceId")
    def device_id(self) -> builtins.str:
        '''The ID of the device, such as ``G030PX0312744DWM`` .'''
        return typing.cast(builtins.str, jsii.get(self, "deviceId"))

    @device_id.setter
    def device_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1af5e1ede2c9cfe87913d3b2fe43a47c008e26ef1d491043fc5231d4a6fc4c0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A Boolean value indicating whether the device is enabled ( ``true`` ) or not ( ``false`` ).'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b986cfe7b04041b5edc4a04f13db84e74e99be88c5d7752df22893d05d9f79f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot1click.CfnDeviceProps",
    jsii_struct_bases=[],
    name_mapping={"device_id": "deviceId", "enabled": "enabled"},
)
class CfnDeviceProps:
    def __init__(
        self,
        *,
        device_id: builtins.str,
        enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        '''Properties for defining a ``CfnDevice``.

        :param device_id: The ID of the device, such as ``G030PX0312744DWM`` .
        :param enabled: A Boolean value indicating whether the device is enabled ( ``true`` ) or not ( ``false`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot1click as iot1click
            
            cfn_device_props = iot1click.CfnDeviceProps(
                device_id="deviceId",
                enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed52f8e78c1c813a8f26b92a1f5cb2a3266d3b98a462677f54a8e4c568b1c7b9)
            check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_id": device_id,
            "enabled": enabled,
        }

    @builtins.property
    def device_id(self) -> builtins.str:
        '''The ID of the device, such as ``G030PX0312744DWM`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html#cfn-iot1click-device-deviceid
        '''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A Boolean value indicating whether the device is enabled ( ``true`` ) or not ( ``false`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html#cfn-iot1click-device-enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPlacement(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot1click.CfnPlacement",
):
    '''The ``AWS::IoT1Click::Placement`` resource creates a placement to be associated with an AWS IoT 1-Click project.

    A placement is an instance of a device in a location. For more information, see `Projects, Templates, and Placements <https://docs.aws.amazon.com/iot-1-click/latest/developerguide/1click-PTP.html>`_ in the *AWS IoT 1-Click Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot1click as iot1click
        
        # associated_devices: Any
        # attributes: Any
        
        cfn_placement = iot1click.CfnPlacement(self, "MyCfnPlacement",
            project_name="projectName",
        
            # the properties below are optional
            associated_devices=associated_devices,
            attributes=attributes,
            placement_name="placementName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_name: builtins.str,
        associated_devices: typing.Any = None,
        attributes: typing.Any = None,
        placement_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param project_name: The name of the project containing the placement.
        :param associated_devices: The devices to associate with the placement, as defined by a mapping of zero or more key-value pairs wherein the key is a template name and the value is a device ID.
        :param attributes: The user-defined attributes associated with the placement.
        :param placement_name: The name of the placement.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1832ff90d2995fc576cdd9b6a1b5fa00191a74d323a5bc23e80b816f8ac9854d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlacementProps(
            project_name=project_name,
            associated_devices=associated_devices,
            attributes=attributes,
            placement_name=placement_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed4609cb5007624d058eaa3272257198873e4f46babc9f039aca356a1b992955)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af49c721837c421886783abf1ffc1647011473f5b646bd22401113aaae686e8e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrPlacementName")
    def attr_placement_name(self) -> builtins.str:
        '''The name of the placement, such as ``floor17`` .

        :cloudformationAttribute: PlacementName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlacementName"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectName")
    def attr_project_name(self) -> builtins.str:
        '''The name of the project containing the placement, such as ``conference-rooms`` .

        :cloudformationAttribute: ProjectName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        '''The name of the project containing the placement.'''
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f68bef049df594e77c7012b197213cb53a06ead39f89cf4e53e662971c19c947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectName", value)

    @builtins.property
    @jsii.member(jsii_name="associatedDevices")
    def associated_devices(self) -> typing.Any:
        '''The devices to associate with the placement, as defined by a mapping of zero or more key-value pairs wherein the key is a template name and the value is a device ID.'''
        return typing.cast(typing.Any, jsii.get(self, "associatedDevices"))

    @associated_devices.setter
    def associated_devices(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41ed621a48ebcff7516df830ca4354bd481f7fe3c2a7b02f987d9817f06437aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedDevices", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Any:
        '''The user-defined attributes associated with the placement.'''
        return typing.cast(typing.Any, jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__279a36e68d02da72c788a0ae0680ed6215b286e6067d4217301b95e1759e8945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="placementName")
    def placement_name(self) -> typing.Optional[builtins.str]:
        '''The name of the placement.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementName"))

    @placement_name.setter
    def placement_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9997ef913ccc729d6160ae2ad2530921224a6b3d37a9783881301d6e83aa1a7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot1click.CfnPlacementProps",
    jsii_struct_bases=[],
    name_mapping={
        "project_name": "projectName",
        "associated_devices": "associatedDevices",
        "attributes": "attributes",
        "placement_name": "placementName",
    },
)
class CfnPlacementProps:
    def __init__(
        self,
        *,
        project_name: builtins.str,
        associated_devices: typing.Any = None,
        attributes: typing.Any = None,
        placement_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlacement``.

        :param project_name: The name of the project containing the placement.
        :param associated_devices: The devices to associate with the placement, as defined by a mapping of zero or more key-value pairs wherein the key is a template name and the value is a device ID.
        :param attributes: The user-defined attributes associated with the placement.
        :param placement_name: The name of the placement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot1click as iot1click
            
            # associated_devices: Any
            # attributes: Any
            
            cfn_placement_props = iot1click.CfnPlacementProps(
                project_name="projectName",
            
                # the properties below are optional
                associated_devices=associated_devices,
                attributes=attributes,
                placement_name="placementName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b1bbe2d11ebbdd26b5e90bd4b93cff97bf9de6a4af0c3d4f57d17ce47727447)
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
            check_type(argname="argument associated_devices", value=associated_devices, expected_type=type_hints["associated_devices"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument placement_name", value=placement_name, expected_type=type_hints["placement_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_name": project_name,
        }
        if associated_devices is not None:
            self._values["associated_devices"] = associated_devices
        if attributes is not None:
            self._values["attributes"] = attributes
        if placement_name is not None:
            self._values["placement_name"] = placement_name

    @builtins.property
    def project_name(self) -> builtins.str:
        '''The name of the project containing the placement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-projectname
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associated_devices(self) -> typing.Any:
        '''The devices to associate with the placement, as defined by a mapping of zero or more key-value pairs wherein the key is a template name and the value is a device ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-associateddevices
        '''
        result = self._values.get("associated_devices")
        return typing.cast(typing.Any, result)

    @builtins.property
    def attributes(self) -> typing.Any:
        '''The user-defined attributes associated with the placement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Any, result)

    @builtins.property
    def placement_name(self) -> typing.Optional[builtins.str]:
        '''The name of the placement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-placementname
        '''
        result = self._values.get("placement_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlacementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot1click.CfnProject",
):
    '''The ``AWS::IoT1Click::Project`` resource creates an empty project with a placement template.

    A project contains zero or more placements that adhere to the placement template defined in the project. For more information, see `CreateProject <https://docs.aws.amazon.com/iot-1-click/latest/projects-apireference/API_CreateProject.html>`_ in the *AWS IoT 1-Click Projects API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot1click as iot1click
        
        # callback_overrides: Any
        # default_attributes: Any
        
        cfn_project = iot1click.CfnProject(self, "MyCfnProject",
            placement_template=iot1click.CfnProject.PlacementTemplateProperty(
                default_attributes=default_attributes,
                device_templates={
                    "device_templates_key": iot1click.CfnProject.DeviceTemplateProperty(
                        callback_overrides=callback_overrides,
                        device_type="deviceType"
                    )
                }
            ),
        
            # the properties below are optional
            description="description",
            project_name="projectName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        placement_template: typing.Union[_IResolvable_da3f097b, typing.Union["CfnProject.PlacementTemplateProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        project_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param placement_template: An object describing the project's placement specifications.
        :param description: The description of the project.
        :param project_name: The name of the project from which to obtain information.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2c29252c15ba10b77b5985156042673510f8f87b02c8fa43d385a6ff3839856)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(
            placement_template=placement_template,
            description=description,
            project_name=project_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70aee69d79cd59a1403adc51005f6f5e7f053b1b1860ee137f3ed174df3ed786)
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
            type_hints = typing.get_type_hints(_typecheckingstub__867b815a22af6da5102aa2a4ee22b7bd47dd9e8a4df8627649ebf70096b28fc9)
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
        '''The Amazon Resource Name (ARN) of the project, such as ``arn:aws:iot1click:us-east-1:123456789012:projects/project-a1bzhi`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectName")
    def attr_project_name(self) -> builtins.str:
        '''The name of the project, such as ``project-a1bzhi`` .

        :cloudformationAttribute: ProjectName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="placementTemplate")
    def placement_template(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnProject.PlacementTemplateProperty"]:
        '''An object describing the project's placement specifications.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnProject.PlacementTemplateProperty"], jsii.get(self, "placementTemplate"))

    @placement_template.setter
    def placement_template(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnProject.PlacementTemplateProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10329a883f29ed9a6dd8489a9b81a75968998073c701add9d1761585b9e40cd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9afaa0e2c9e7b64d739597df0dff663b59f88cd587e919e616f1d8e09db62698)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> typing.Optional[builtins.str]:
        '''The name of the project from which to obtain information.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cc0f114afe3a05f16542f8d1804e57b5ea886248e56cef59f9de5e8cf1bbca6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot1click.CfnProject.DeviceTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "callback_overrides": "callbackOverrides",
            "device_type": "deviceType",
        },
    )
    class DeviceTemplateProperty:
        def __init__(
            self,
            *,
            callback_overrides: typing.Any = None,
            device_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''In AWS CloudFormation , use the ``DeviceTemplate`` property type to define the template for an AWS IoT 1-Click project.

            ``DeviceTemplate`` is a property of the ``AWS::IoT1Click::Project`` resource.

            :param callback_overrides: An optional AWS Lambda function to invoke instead of the default AWS Lambda function provided by the placement template.
            :param device_type: The device type, which currently must be ``"button"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot1click as iot1click
                
                # callback_overrides: Any
                
                device_template_property = iot1click.CfnProject.DeviceTemplateProperty(
                    callback_overrides=callback_overrides,
                    device_type="deviceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a364cc50019121c27a835abe7b914c8315b0e2c88002dcbc6901ada8ae32bb6b)
                check_type(argname="argument callback_overrides", value=callback_overrides, expected_type=type_hints["callback_overrides"])
                check_type(argname="argument device_type", value=device_type, expected_type=type_hints["device_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if callback_overrides is not None:
                self._values["callback_overrides"] = callback_overrides
            if device_type is not None:
                self._values["device_type"] = device_type

        @builtins.property
        def callback_overrides(self) -> typing.Any:
            '''An optional AWS Lambda function to invoke instead of the default AWS Lambda function provided by the placement template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html#cfn-iot1click-project-devicetemplate-callbackoverrides
            '''
            result = self._values.get("callback_overrides")
            return typing.cast(typing.Any, result)

        @builtins.property
        def device_type(self) -> typing.Optional[builtins.str]:
            '''The device type, which currently must be ``"button"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html#cfn-iot1click-project-devicetemplate-devicetype
            '''
            result = self._values.get("device_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot1click.CfnProject.PlacementTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_attributes": "defaultAttributes",
            "device_templates": "deviceTemplates",
        },
    )
    class PlacementTemplateProperty:
        def __init__(
            self,
            *,
            default_attributes: typing.Any = None,
            device_templates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnProject.DeviceTemplateProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''In AWS CloudFormation , use the ``PlacementTemplate`` property type to define the template for an AWS IoT 1-Click project.

            ``PlacementTemplate`` is a property of the ``AWS::IoT1Click::Project`` resource.

            :param default_attributes: The default attributes (key-value pairs) to be applied to all placements using this template.
            :param device_templates: An object specifying the `DeviceTemplate <https://docs.aws.amazon.com/iot-1-click/latest/projects-apireference/API_DeviceTemplate.html>`_ for all placements using this ( `PlacementTemplate <https://docs.aws.amazon.com/iot-1-click/latest/projects-apireference/API_PlacementTemplate.html>`_ ) template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot1click as iot1click
                
                # callback_overrides: Any
                # default_attributes: Any
                
                placement_template_property = iot1click.CfnProject.PlacementTemplateProperty(
                    default_attributes=default_attributes,
                    device_templates={
                        "device_templates_key": iot1click.CfnProject.DeviceTemplateProperty(
                            callback_overrides=callback_overrides,
                            device_type="deviceType"
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dc41c90630ddc14dd8b14abf74ffbb2fc8fa550552a4b6a37ee7b0c3f65c25ba)
                check_type(argname="argument default_attributes", value=default_attributes, expected_type=type_hints["default_attributes"])
                check_type(argname="argument device_templates", value=device_templates, expected_type=type_hints["device_templates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default_attributes is not None:
                self._values["default_attributes"] = default_attributes
            if device_templates is not None:
                self._values["device_templates"] = device_templates

        @builtins.property
        def default_attributes(self) -> typing.Any:
            '''The default attributes (key-value pairs) to be applied to all placements using this template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html#cfn-iot1click-project-placementtemplate-defaultattributes
            '''
            result = self._values.get("default_attributes")
            return typing.cast(typing.Any, result)

        @builtins.property
        def device_templates(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnProject.DeviceTemplateProperty"]]]]:
            '''An object specifying the `DeviceTemplate <https://docs.aws.amazon.com/iot-1-click/latest/projects-apireference/API_DeviceTemplate.html>`_ for all placements using this ( `PlacementTemplate <https://docs.aws.amazon.com/iot-1-click/latest/projects-apireference/API_PlacementTemplate.html>`_ ) template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html#cfn-iot1click-project-placementtemplate-devicetemplates
            '''
            result = self._values.get("device_templates")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnProject.DeviceTemplateProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot1click.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "placement_template": "placementTemplate",
        "description": "description",
        "project_name": "projectName",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        placement_template: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.PlacementTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        project_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnProject``.

        :param placement_template: An object describing the project's placement specifications.
        :param description: The description of the project.
        :param project_name: The name of the project from which to obtain information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot1click as iot1click
            
            # callback_overrides: Any
            # default_attributes: Any
            
            cfn_project_props = iot1click.CfnProjectProps(
                placement_template=iot1click.CfnProject.PlacementTemplateProperty(
                    default_attributes=default_attributes,
                    device_templates={
                        "device_templates_key": iot1click.CfnProject.DeviceTemplateProperty(
                            callback_overrides=callback_overrides,
                            device_type="deviceType"
                        )
                    }
                ),
            
                # the properties below are optional
                description="description",
                project_name="projectName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1077ac21e114e5467c3dc453c6e32e23dfee1deab570e2fce54ad955b96fb2d0)
            check_type(argname="argument placement_template", value=placement_template, expected_type=type_hints["placement_template"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "placement_template": placement_template,
        }
        if description is not None:
            self._values["description"] = description
        if project_name is not None:
            self._values["project_name"] = project_name

    @builtins.property
    def placement_template(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnProject.PlacementTemplateProperty]:
        '''An object describing the project's placement specifications.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-placementtemplate
        '''
        result = self._values.get("placement_template")
        assert result is not None, "Required property 'placement_template' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnProject.PlacementTemplateProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_name(self) -> typing.Optional[builtins.str]:
        '''The name of the project from which to obtain information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-projectname
        '''
        result = self._values.get("project_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDevice",
    "CfnDeviceProps",
    "CfnPlacement",
    "CfnPlacementProps",
    "CfnProject",
    "CfnProjectProps",
]

publication.publish()

def _typecheckingstub__4a339667885af529b8cd8c8d1e0a01ab39b4df8c37caaa4e780eaac7c2f9666f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    device_id: builtins.str,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c208db47e9fcc79bcc2e61f32b9c12a92a8fd2fbe37297fb8a7f35416fff32e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0937e66cec46366bbf925d7a3705e020a00ac7868787dc36d1cfa4978d429e56(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af5e1ede2c9cfe87913d3b2fe43a47c008e26ef1d491043fc5231d4a6fc4c0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b986cfe7b04041b5edc4a04f13db84e74e99be88c5d7752df22893d05d9f79f(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed52f8e78c1c813a8f26b92a1f5cb2a3266d3b98a462677f54a8e4c568b1c7b9(
    *,
    device_id: builtins.str,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1832ff90d2995fc576cdd9b6a1b5fa00191a74d323a5bc23e80b816f8ac9854d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_name: builtins.str,
    associated_devices: typing.Any = None,
    attributes: typing.Any = None,
    placement_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4609cb5007624d058eaa3272257198873e4f46babc9f039aca356a1b992955(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af49c721837c421886783abf1ffc1647011473f5b646bd22401113aaae686e8e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f68bef049df594e77c7012b197213cb53a06ead39f89cf4e53e662971c19c947(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41ed621a48ebcff7516df830ca4354bd481f7fe3c2a7b02f987d9817f06437aa(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__279a36e68d02da72c788a0ae0680ed6215b286e6067d4217301b95e1759e8945(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9997ef913ccc729d6160ae2ad2530921224a6b3d37a9783881301d6e83aa1a7d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b1bbe2d11ebbdd26b5e90bd4b93cff97bf9de6a4af0c3d4f57d17ce47727447(
    *,
    project_name: builtins.str,
    associated_devices: typing.Any = None,
    attributes: typing.Any = None,
    placement_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2c29252c15ba10b77b5985156042673510f8f87b02c8fa43d385a6ff3839856(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    placement_template: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.PlacementTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    project_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70aee69d79cd59a1403adc51005f6f5e7f053b1b1860ee137f3ed174df3ed786(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867b815a22af6da5102aa2a4ee22b7bd47dd9e8a4df8627649ebf70096b28fc9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10329a883f29ed9a6dd8489a9b81a75968998073c701add9d1761585b9e40cd7(
    value: typing.Union[_IResolvable_da3f097b, CfnProject.PlacementTemplateProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9afaa0e2c9e7b64d739597df0dff663b59f88cd587e919e616f1d8e09db62698(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc0f114afe3a05f16542f8d1804e57b5ea886248e56cef59f9de5e8cf1bbca6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a364cc50019121c27a835abe7b914c8315b0e2c88002dcbc6901ada8ae32bb6b(
    *,
    callback_overrides: typing.Any = None,
    device_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc41c90630ddc14dd8b14abf74ffbb2fc8fa550552a4b6a37ee7b0c3f65c25ba(
    *,
    default_attributes: typing.Any = None,
    device_templates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.DeviceTemplateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1077ac21e114e5467c3dc453c6e32e23dfee1deab570e2fce54ad955b96fb2d0(
    *,
    placement_template: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.PlacementTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    project_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
