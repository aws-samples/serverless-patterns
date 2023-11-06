'''
# AWS::DeviceFarm Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_devicefarm as devicefarm
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DeviceFarm construct libraries](https://constructs.dev/search?q=devicefarm)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DeviceFarm resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DeviceFarm.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DeviceFarm](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DeviceFarm.html).

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
class CfnDevicePool(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnDevicePool",
):
    '''Represents a request to the create device pool operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devicefarm as devicefarm
        
        cfn_device_pool = devicefarm.CfnDevicePool(self, "MyCfnDevicePool",
            name="name",
            project_arn="projectArn",
            rules=[devicefarm.CfnDevicePool.RuleProperty(
                attribute="attribute",
                operator="operator",
                value="value"
            )],
        
            # the properties below are optional
            description="description",
            max_devices=123,
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
        project_arn: builtins.str,
        rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDevicePool.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        max_devices: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The device pool's name.
        :param project_arn: The ARN of the project for the device pool.
        :param rules: The device pool's rules.
        :param description: The device pool's description.
        :param max_devices: The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter. By specifying the maximum number of devices, you can control the costs that you incur by running tests.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c6314bfee539a8146973e0d5495e39f622c4c3953e795d05460e2bb76cc8db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDevicePoolProps(
            name=name,
            project_arn=project_arn,
            rules=rules,
            description=description,
            max_devices=max_devices,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06066b24c235ef43fb2b2aa45da0a1ad576ff065b3b44d12f93725c3a454a27e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88f86a0ff3bc397ecbead77b1e7a92e74d7aa974b4e493527a64fb12b9571595)
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
        '''The Amazon Resource Name (ARN) of the device pool.

        See `Amazon resource names <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *General Reference guide* .

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
        '''The device pool's name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__274a6264ef4f53855c7fb29b5e3d4eaea2f1ecaa2b107832b5c87514be43bd21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectArn")
    def project_arn(self) -> builtins.str:
        '''The ARN of the project for the device pool.'''
        return typing.cast(builtins.str, jsii.get(self, "projectArn"))

    @project_arn.setter
    def project_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90da46d699d68d2324638e678e647ad8536c9865f9885776a4593a4c7bbd5a81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectArn", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDevicePool.RuleProperty"]]]:
        '''The device pool's rules.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDevicePool.RuleProperty"]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDevicePool.RuleProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__878e6373669e306e9365c0b15e6adde48fdf3dfe289f45637e1a549ae9da641b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The device pool's description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2af8686131384f19961bfed2d06ace261ff278057a6b7b8a2ce5fb08a50041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="maxDevices")
    def max_devices(self) -> typing.Optional[jsii.Number]:
        '''The number of devices that Device Farm can add to your device pool.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDevices"))

    @max_devices.setter
    def max_devices(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678df3a1e7f007b97b7ca6f058747cd03c5fd1d9c97dce118f6007e5ff5cb8b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDevices", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2cf7f4efbed5d263cca53206f67753b2376cc6beb829af18416bb2774b62a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devicefarm.CfnDevicePool.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute": "attribute",
            "operator": "operator",
            "value": "value",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            attribute: typing.Optional[builtins.str] = None,
            operator: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a condition for a device pool.

            :param attribute: The rule's stringified attribute. For example, specify the value as ``"\\"abc\\""`` . The supported operators for each attribute are provided in the following list. - **APPIUM_VERSION** - The Appium version for the test. Supported operators: ``CONTAINS`` - **ARN** - The Amazon Resource Name (ARN) of the device (for example, ``arn:aws:devicefarm:us-west-2::device:12345Example`` . Supported operators: ``EQUALS`` , ``IN`` , ``NOT_IN`` - **AVAILABILITY** - The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE. Supported operators: ``EQUALS`` - **FLEET_TYPE** - The fleet type. Valid values are PUBLIC or PRIVATE. Supported operators: ``EQUALS`` - **FORM_FACTOR** - The device form factor. Valid values are PHONE or TABLET. Supported operators: ``EQUALS`` , ``IN`` , ``NOT_IN`` - **INSTANCE_ARN** - The Amazon Resource Name (ARN) of the device instance. Supported operators: ``IN`` , ``NOT_IN`` - **INSTANCE_LABELS** - The label of the device instance. Supported operators: ``CONTAINS`` - **MANUFACTURER** - The device manufacturer (for example, Apple). Supported operators: ``EQUALS`` , ``IN`` , ``NOT_IN`` - **MODEL** - The device model, such as Apple iPad Air 2 or Google Pixel. Supported operators: ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN`` - **OS_VERSION** - The operating system version (for example, 10.3.2). Supported operators: ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN`` - **PLATFORM** - The device platform. Valid values are ANDROID or IOS. Supported operators: ``EQUALS`` , ``IN`` , ``NOT_IN`` - **REMOTE_ACCESS_ENABLED** - Whether the device is enabled for remote access. Valid values are TRUE or FALSE. Supported operators: ``EQUALS`` - **REMOTE_DEBUG_ENABLED** - Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Supported operators: ``EQUALS`` Because remote debugging is `no longer supported <https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html>`_ , this filter is ignored.
            :param operator: Specifies how Device Farm compares the rule's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
            :param value: The rule's value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devicefarm as devicefarm
                
                rule_property = devicefarm.CfnDevicePool.RuleProperty(
                    attribute="attribute",
                    operator="operator",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0620996469fe8ee5556b96e0e9cda4bff8b92c7e9aa8aa5903cb6dd043c2aafa)
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attribute is not None:
                self._values["attribute"] = attribute
            if operator is not None:
                self._values["operator"] = operator
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def attribute(self) -> typing.Optional[builtins.str]:
            '''The rule's stringified attribute. For example, specify the value as ``"\\"abc\\""`` .

            The supported operators for each attribute are provided in the following list.

            - **APPIUM_VERSION** - The Appium version for the test.

            Supported operators: ``CONTAINS``

            - **ARN** - The Amazon Resource Name (ARN) of the device (for example, ``arn:aws:devicefarm:us-west-2::device:12345Example`` .

            Supported operators: ``EQUALS`` , ``IN`` , ``NOT_IN``

            - **AVAILABILITY** - The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.

            Supported operators: ``EQUALS``

            - **FLEET_TYPE** - The fleet type. Valid values are PUBLIC or PRIVATE.

            Supported operators: ``EQUALS``

            - **FORM_FACTOR** - The device form factor. Valid values are PHONE or TABLET.

            Supported operators: ``EQUALS`` , ``IN`` , ``NOT_IN``

            - **INSTANCE_ARN** - The Amazon Resource Name (ARN) of the device instance.

            Supported operators: ``IN`` , ``NOT_IN``

            - **INSTANCE_LABELS** - The label of the device instance.

            Supported operators: ``CONTAINS``

            - **MANUFACTURER** - The device manufacturer (for example, Apple).

            Supported operators: ``EQUALS`` , ``IN`` , ``NOT_IN``

            - **MODEL** - The device model, such as Apple iPad Air 2 or Google Pixel.

            Supported operators: ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``

            - **OS_VERSION** - The operating system version (for example, 10.3.2).

            Supported operators: ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``

            - **PLATFORM** - The device platform. Valid values are ANDROID or IOS.

            Supported operators: ``EQUALS`` , ``IN`` , ``NOT_IN``

            - **REMOTE_ACCESS_ENABLED** - Whether the device is enabled for remote access. Valid values are TRUE or FALSE.

            Supported operators: ``EQUALS``

            - **REMOTE_DEBUG_ENABLED** - Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.

            Supported operators: ``EQUALS``

            Because remote debugging is `no longer supported <https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html>`_ , this filter is ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html#cfn-devicefarm-devicepool-rule-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operator(self) -> typing.Optional[builtins.str]:
            '''Specifies how Device Farm compares the rule's attribute to the value.

            For the operators that are supported by each attribute, see the attribute descriptions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html#cfn-devicefarm-devicepool-rule-operator
            '''
            result = self._values.get("operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The rule's value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html#cfn-devicefarm-devicepool-rule-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnDevicePoolProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "project_arn": "projectArn",
        "rules": "rules",
        "description": "description",
        "max_devices": "maxDevices",
        "tags": "tags",
    },
)
class CfnDevicePoolProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        project_arn: builtins.str,
        rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevicePool.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        max_devices: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDevicePool``.

        :param name: The device pool's name.
        :param project_arn: The ARN of the project for the device pool.
        :param rules: The device pool's rules.
        :param description: The device pool's description.
        :param max_devices: The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter. By specifying the maximum number of devices, you can control the costs that you incur by running tests.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devicefarm as devicefarm
            
            cfn_device_pool_props = devicefarm.CfnDevicePoolProps(
                name="name",
                project_arn="projectArn",
                rules=[devicefarm.CfnDevicePool.RuleProperty(
                    attribute="attribute",
                    operator="operator",
                    value="value"
                )],
            
                # the properties below are optional
                description="description",
                max_devices=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdbd0dbaf5eeb8e0d1a370581a06a71801ff0d57bd9fd8d87abcb95e23dea50c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument max_devices", value=max_devices, expected_type=type_hints["max_devices"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "project_arn": project_arn,
            "rules": rules,
        }
        if description is not None:
            self._values["description"] = description
        if max_devices is not None:
            self._values["max_devices"] = max_devices
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The device pool's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html#cfn-devicefarm-devicepool-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''The ARN of the project for the device pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html#cfn-devicefarm-devicepool-projectarn
        '''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDevicePool.RuleProperty]]]:
        '''The device pool's rules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html#cfn-devicefarm-devicepool-rules
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDevicePool.RuleProperty]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The device pool's description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html#cfn-devicefarm-devicepool-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_devices(self) -> typing.Optional[jsii.Number]:
        '''The number of devices that Device Farm can add to your device pool.

        Device Farm adds devices that are available and meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.

        By specifying the maximum number of devices, you can control the costs that you incur by running tests.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html#cfn-devicefarm-devicepool-maxdevices
        '''
        result = self._values.get("max_devices")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html#cfn-devicefarm-devicepool-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDevicePoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnInstanceProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnInstanceProfile",
):
    '''Creates a profile that can be applied to one or more private fleet device instances.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devicefarm as devicefarm
        
        cfn_instance_profile = devicefarm.CfnInstanceProfile(self, "MyCfnInstanceProfile",
            name="name",
        
            # the properties below are optional
            description="description",
            exclude_app_packages_from_cleanup=["excludeAppPackagesFromCleanup"],
            package_cleanup=False,
            reboot_after_use=False,
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
        description: typing.Optional[builtins.str] = None,
        exclude_app_packages_from_cleanup: typing.Optional[typing.Sequence[builtins.str]] = None,
        package_cleanup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        reboot_after_use: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the instance profile.
        :param description: The description of the instance profile.
        :param exclude_app_packages_from_cleanup: An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes. The list of packages is considered only if you set ``packageCleanup`` to ``true`` .
        :param package_cleanup: When set to ``true`` , Device Farm removes app packages after a test run. The default value is ``false`` for private devices.
        :param reboot_after_use: When set to ``true`` , Device Farm reboots the instance after a test run. The default value is ``true`` .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9dd1552bba1f4a322e22652920f9f1fa8079a149ae08cb1e20455b8f7a548b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceProfileProps(
            name=name,
            description=description,
            exclude_app_packages_from_cleanup=exclude_app_packages_from_cleanup,
            package_cleanup=package_cleanup,
            reboot_after_use=reboot_after_use,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c146e7e4ae72d3aab6ff3154ac09aa531bf8c9be0d22f33d454b43266ed916b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c6fa7b46bf9514b077b27808bc205832a47a5c1dc9141e47081ba716d2c99f1)
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
        '''The Amazon Resource Name (ARN) of the instance profile.

        See `Amazon resource names <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *General Reference guide* .

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
        '''The name of the instance profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17aaeb013eadb1aa2000886131450d5986814e62564399d33943dc37661073b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c39d2e3a3b084568408244f32d6a7e381af3a3ad557c2426a2adb5528556edd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="excludeAppPackagesFromCleanup")
    def exclude_app_packages_from_cleanup(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeAppPackagesFromCleanup"))

    @exclude_app_packages_from_cleanup.setter
    def exclude_app_packages_from_cleanup(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57be4bbd251344311f39ec38b200083c315e5a9d8dbbf607068d9cd09772107c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeAppPackagesFromCleanup", value)

    @builtins.property
    @jsii.member(jsii_name="packageCleanup")
    def package_cleanup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When set to ``true`` , Device Farm removes app packages after a test run.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "packageCleanup"))

    @package_cleanup.setter
    def package_cleanup(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94278fbf52719304b1eeb162c050b5e9626d58ff0e40eb901b64a01f27e63972)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packageCleanup", value)

    @builtins.property
    @jsii.member(jsii_name="rebootAfterUse")
    def reboot_after_use(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When set to ``true`` , Device Farm reboots the instance after a test run.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "rebootAfterUse"))

    @reboot_after_use.setter
    def reboot_after_use(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59e2f9337c3eb103f9e3a27518e293407dc94e98fee92f2b33af3b1d9dd60698)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rebootAfterUse", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5194955750aa2f8304da100d5f6b3035ceebeb29d5b599f07f657cc4f7516714)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnInstanceProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "exclude_app_packages_from_cleanup": "excludeAppPackagesFromCleanup",
        "package_cleanup": "packageCleanup",
        "reboot_after_use": "rebootAfterUse",
        "tags": "tags",
    },
)
class CfnInstanceProfileProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        exclude_app_packages_from_cleanup: typing.Optional[typing.Sequence[builtins.str]] = None,
        package_cleanup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        reboot_after_use: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceProfile``.

        :param name: The name of the instance profile.
        :param description: The description of the instance profile.
        :param exclude_app_packages_from_cleanup: An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes. The list of packages is considered only if you set ``packageCleanup`` to ``true`` .
        :param package_cleanup: When set to ``true`` , Device Farm removes app packages after a test run. The default value is ``false`` for private devices.
        :param reboot_after_use: When set to ``true`` , Device Farm reboots the instance after a test run. The default value is ``true`` .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devicefarm as devicefarm
            
            cfn_instance_profile_props = devicefarm.CfnInstanceProfileProps(
                name="name",
            
                # the properties below are optional
                description="description",
                exclude_app_packages_from_cleanup=["excludeAppPackagesFromCleanup"],
                package_cleanup=False,
                reboot_after_use=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7392c4b7cccfb4ed48f655dd9ef8cfdda0d147224dceaf92b58913cc7bdedf0a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument exclude_app_packages_from_cleanup", value=exclude_app_packages_from_cleanup, expected_type=type_hints["exclude_app_packages_from_cleanup"])
            check_type(argname="argument package_cleanup", value=package_cleanup, expected_type=type_hints["package_cleanup"])
            check_type(argname="argument reboot_after_use", value=reboot_after_use, expected_type=type_hints["reboot_after_use"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if exclude_app_packages_from_cleanup is not None:
            self._values["exclude_app_packages_from_cleanup"] = exclude_app_packages_from_cleanup
        if package_cleanup is not None:
            self._values["package_cleanup"] = package_cleanup
        if reboot_after_use is not None:
            self._values["reboot_after_use"] = reboot_after_use
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the instance profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html#cfn-devicefarm-instanceprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the instance profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html#cfn-devicefarm-instanceprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude_app_packages_from_cleanup(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.

        The list of packages is considered only if you set ``packageCleanup`` to ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html#cfn-devicefarm-instanceprofile-excludeapppackagesfromcleanup
        '''
        result = self._values.get("exclude_app_packages_from_cleanup")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def package_cleanup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When set to ``true`` , Device Farm removes app packages after a test run.

        The default value is ``false`` for private devices.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html#cfn-devicefarm-instanceprofile-packagecleanup
        '''
        result = self._values.get("package_cleanup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def reboot_after_use(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When set to ``true`` , Device Farm reboots the instance after a test run.

        The default value is ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html#cfn-devicefarm-instanceprofile-rebootafteruse
        '''
        result = self._values.get("reboot_after_use")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html#cfn-devicefarm-instanceprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnNetworkProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnNetworkProfile",
):
    '''Creates a network profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devicefarm as devicefarm
        
        cfn_network_profile = devicefarm.CfnNetworkProfile(self, "MyCfnNetworkProfile",
            name="name",
            project_arn="projectArn",
        
            # the properties below are optional
            description="description",
            downlink_bandwidth_bits=123,
            downlink_delay_ms=123,
            downlink_jitter_ms=123,
            downlink_loss_percent=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            uplink_bandwidth_bits=123,
            uplink_delay_ms=123,
            uplink_jitter_ms=123,
            uplink_loss_percent=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        project_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        downlink_bandwidth_bits: typing.Optional[jsii.Number] = None,
        downlink_delay_ms: typing.Optional[jsii.Number] = None,
        downlink_jitter_ms: typing.Optional[jsii.Number] = None,
        downlink_loss_percent: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        uplink_bandwidth_bits: typing.Optional[jsii.Number] = None,
        uplink_delay_ms: typing.Optional[jsii.Number] = None,
        uplink_jitter_ms: typing.Optional[jsii.Number] = None,
        uplink_loss_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the network profile.
        :param project_arn: The Amazon Resource Name (ARN) of the specified project.
        :param description: The description of the network profile.
        :param downlink_bandwidth_bits: The data throughput rate in bits per second, as an integer from 0 to 104857600.
        :param downlink_delay_ms: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        :param downlink_jitter_ms: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        :param downlink_loss_percent: Proportion of received packets that fail to arrive from 0 to 100 percent.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .
        :param uplink_bandwidth_bits: The data throughput rate in bits per second, as an integer from 0 to 104857600.
        :param uplink_delay_ms: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        :param uplink_jitter_ms: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        :param uplink_loss_percent: Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600f319c8811bcdb37dc45d939671c38345fae417a48df83d7c3947fbe55cf29)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNetworkProfileProps(
            name=name,
            project_arn=project_arn,
            description=description,
            downlink_bandwidth_bits=downlink_bandwidth_bits,
            downlink_delay_ms=downlink_delay_ms,
            downlink_jitter_ms=downlink_jitter_ms,
            downlink_loss_percent=downlink_loss_percent,
            tags=tags,
            uplink_bandwidth_bits=uplink_bandwidth_bits,
            uplink_delay_ms=uplink_delay_ms,
            uplink_jitter_ms=uplink_jitter_ms,
            uplink_loss_percent=uplink_loss_percent,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__802be6b3874919bcab4f00f242ef5917d7ef30a2d95bf1f24d93fb8bd6b68061)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4605f7133abcc717586ae72fbe7d0ba058bf6bba8231c05d91a00c8425f69441)
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
        '''The Amazon Resource Name (ARN) of the network profile.

        See `Amazon resource names <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *General Reference guide* .

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
        '''The name of the network profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__294fb5334d61ef0ae6269e6e607f8c61028dacb1a4add762eec71b2612e6636b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectArn")
    def project_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified project.'''
        return typing.cast(builtins.str, jsii.get(self, "projectArn"))

    @project_arn.setter
    def project_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8541a8aba350561662e9c4d9ecd7dc3c858e32f43e2a6fe4f1881247500cc635)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the network profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__313840f222b69f6c215057569c0535e7837093d8a0e7cdf0884c32077a8a185d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="downlinkBandwidthBits")
    def downlink_bandwidth_bits(self) -> typing.Optional[jsii.Number]:
        '''The data throughput rate in bits per second, as an integer from 0 to 104857600.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "downlinkBandwidthBits"))

    @downlink_bandwidth_bits.setter
    def downlink_bandwidth_bits(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c52a6ab2b4d0eff01793635e9b13503e20d77676ea2af5a9532742ae76daa9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downlinkBandwidthBits", value)

    @builtins.property
    @jsii.member(jsii_name="downlinkDelayMs")
    def downlink_delay_ms(self) -> typing.Optional[jsii.Number]:
        '''Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "downlinkDelayMs"))

    @downlink_delay_ms.setter
    def downlink_delay_ms(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__781a2c75da42bd3d4cbc7e741db98d2bd12afe98b409d2b695ffe930455c16a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downlinkDelayMs", value)

    @builtins.property
    @jsii.member(jsii_name="downlinkJitterMs")
    def downlink_jitter_ms(self) -> typing.Optional[jsii.Number]:
        '''Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "downlinkJitterMs"))

    @downlink_jitter_ms.setter
    def downlink_jitter_ms(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d556a294ba93bfc2f2891e5fad916e5c4dbb6c8139939917faf51a5b43cf1c1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downlinkJitterMs", value)

    @builtins.property
    @jsii.member(jsii_name="downlinkLossPercent")
    def downlink_loss_percent(self) -> typing.Optional[jsii.Number]:
        '''Proportion of received packets that fail to arrive from 0 to 100 percent.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "downlinkLossPercent"))

    @downlink_loss_percent.setter
    def downlink_loss_percent(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29bab9b49350109aa13762d05ee89e4a0164006247dcfcb9c1ba4a5a796ab8d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downlinkLossPercent", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77650cacecfe99d7da6cd303af7b455933a1f46c7deac85cc197d3802ce9dbff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkBandwidthBits")
    def uplink_bandwidth_bits(self) -> typing.Optional[jsii.Number]:
        '''The data throughput rate in bits per second, as an integer from 0 to 104857600.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uplinkBandwidthBits"))

    @uplink_bandwidth_bits.setter
    def uplink_bandwidth_bits(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c1e25acdc2a7a9c94eddec633a3bc73b43204c3f335d0d5fba44e365ee2c942)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkBandwidthBits", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkDelayMs")
    def uplink_delay_ms(self) -> typing.Optional[jsii.Number]:
        '''Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uplinkDelayMs"))

    @uplink_delay_ms.setter
    def uplink_delay_ms(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e1ad1e5df83993d7d970aec5ba6a43acc420e87f67358c48cc12a958cd04ff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkDelayMs", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkJitterMs")
    def uplink_jitter_ms(self) -> typing.Optional[jsii.Number]:
        '''Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uplinkJitterMs"))

    @uplink_jitter_ms.setter
    def uplink_jitter_ms(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c26698da5c33e2193aefb85ace5f3b2907c0d48412dcb4b7992ac539b16e2ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkJitterMs", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkLossPercent")
    def uplink_loss_percent(self) -> typing.Optional[jsii.Number]:
        '''Proportion of transmitted packets that fail to arrive from 0 to 100 percent.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uplinkLossPercent"))

    @uplink_loss_percent.setter
    def uplink_loss_percent(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c91f7aaeb08d797687bac8c6cbf867868774ba52b3d695b1a462f31536446cd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkLossPercent", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnNetworkProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "project_arn": "projectArn",
        "description": "description",
        "downlink_bandwidth_bits": "downlinkBandwidthBits",
        "downlink_delay_ms": "downlinkDelayMs",
        "downlink_jitter_ms": "downlinkJitterMs",
        "downlink_loss_percent": "downlinkLossPercent",
        "tags": "tags",
        "uplink_bandwidth_bits": "uplinkBandwidthBits",
        "uplink_delay_ms": "uplinkDelayMs",
        "uplink_jitter_ms": "uplinkJitterMs",
        "uplink_loss_percent": "uplinkLossPercent",
    },
)
class CfnNetworkProfileProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        project_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        downlink_bandwidth_bits: typing.Optional[jsii.Number] = None,
        downlink_delay_ms: typing.Optional[jsii.Number] = None,
        downlink_jitter_ms: typing.Optional[jsii.Number] = None,
        downlink_loss_percent: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        uplink_bandwidth_bits: typing.Optional[jsii.Number] = None,
        uplink_delay_ms: typing.Optional[jsii.Number] = None,
        uplink_jitter_ms: typing.Optional[jsii.Number] = None,
        uplink_loss_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnNetworkProfile``.

        :param name: The name of the network profile.
        :param project_arn: The Amazon Resource Name (ARN) of the specified project.
        :param description: The description of the network profile.
        :param downlink_bandwidth_bits: The data throughput rate in bits per second, as an integer from 0 to 104857600.
        :param downlink_delay_ms: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        :param downlink_jitter_ms: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        :param downlink_loss_percent: Proportion of received packets that fail to arrive from 0 to 100 percent.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .
        :param uplink_bandwidth_bits: The data throughput rate in bits per second, as an integer from 0 to 104857600.
        :param uplink_delay_ms: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        :param uplink_jitter_ms: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        :param uplink_loss_percent: Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devicefarm as devicefarm
            
            cfn_network_profile_props = devicefarm.CfnNetworkProfileProps(
                name="name",
                project_arn="projectArn",
            
                # the properties below are optional
                description="description",
                downlink_bandwidth_bits=123,
                downlink_delay_ms=123,
                downlink_jitter_ms=123,
                downlink_loss_percent=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                uplink_bandwidth_bits=123,
                uplink_delay_ms=123,
                uplink_jitter_ms=123,
                uplink_loss_percent=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd5cc9e50d96fdbb41dccca0bc93936eeaacdb252c6703a366abcfc675c8b32)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument downlink_bandwidth_bits", value=downlink_bandwidth_bits, expected_type=type_hints["downlink_bandwidth_bits"])
            check_type(argname="argument downlink_delay_ms", value=downlink_delay_ms, expected_type=type_hints["downlink_delay_ms"])
            check_type(argname="argument downlink_jitter_ms", value=downlink_jitter_ms, expected_type=type_hints["downlink_jitter_ms"])
            check_type(argname="argument downlink_loss_percent", value=downlink_loss_percent, expected_type=type_hints["downlink_loss_percent"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument uplink_bandwidth_bits", value=uplink_bandwidth_bits, expected_type=type_hints["uplink_bandwidth_bits"])
            check_type(argname="argument uplink_delay_ms", value=uplink_delay_ms, expected_type=type_hints["uplink_delay_ms"])
            check_type(argname="argument uplink_jitter_ms", value=uplink_jitter_ms, expected_type=type_hints["uplink_jitter_ms"])
            check_type(argname="argument uplink_loss_percent", value=uplink_loss_percent, expected_type=type_hints["uplink_loss_percent"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "project_arn": project_arn,
        }
        if description is not None:
            self._values["description"] = description
        if downlink_bandwidth_bits is not None:
            self._values["downlink_bandwidth_bits"] = downlink_bandwidth_bits
        if downlink_delay_ms is not None:
            self._values["downlink_delay_ms"] = downlink_delay_ms
        if downlink_jitter_ms is not None:
            self._values["downlink_jitter_ms"] = downlink_jitter_ms
        if downlink_loss_percent is not None:
            self._values["downlink_loss_percent"] = downlink_loss_percent
        if tags is not None:
            self._values["tags"] = tags
        if uplink_bandwidth_bits is not None:
            self._values["uplink_bandwidth_bits"] = uplink_bandwidth_bits
        if uplink_delay_ms is not None:
            self._values["uplink_delay_ms"] = uplink_delay_ms
        if uplink_jitter_ms is not None:
            self._values["uplink_jitter_ms"] = uplink_jitter_ms
        if uplink_loss_percent is not None:
            self._values["uplink_loss_percent"] = uplink_loss_percent

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the network profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-projectarn
        '''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the network profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def downlink_bandwidth_bits(self) -> typing.Optional[jsii.Number]:
        '''The data throughput rate in bits per second, as an integer from 0 to 104857600.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-downlinkbandwidthbits
        '''
        result = self._values.get("downlink_bandwidth_bits")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def downlink_delay_ms(self) -> typing.Optional[jsii.Number]:
        '''Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-downlinkdelayms
        '''
        result = self._values.get("downlink_delay_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def downlink_jitter_ms(self) -> typing.Optional[jsii.Number]:
        '''Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-downlinkjitterms
        '''
        result = self._values.get("downlink_jitter_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def downlink_loss_percent(self) -> typing.Optional[jsii.Number]:
        '''Proportion of received packets that fail to arrive from 0 to 100 percent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-downlinklosspercent
        '''
        result = self._values.get("downlink_loss_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def uplink_bandwidth_bits(self) -> typing.Optional[jsii.Number]:
        '''The data throughput rate in bits per second, as an integer from 0 to 104857600.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-uplinkbandwidthbits
        '''
        result = self._values.get("uplink_bandwidth_bits")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def uplink_delay_ms(self) -> typing.Optional[jsii.Number]:
        '''Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-uplinkdelayms
        '''
        result = self._values.get("uplink_delay_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def uplink_jitter_ms(self) -> typing.Optional[jsii.Number]:
        '''Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-uplinkjitterms
        '''
        result = self._values.get("uplink_jitter_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def uplink_loss_percent(self) -> typing.Optional[jsii.Number]:
        '''Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html#cfn-devicefarm-networkprofile-uplinklosspercent
        '''
        result = self._values.get("uplink_loss_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnProject",
):
    '''Creates a project.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devicefarm as devicefarm
        
        cfn_project = devicefarm.CfnProject(self, "MyCfnProject",
            name="name",
        
            # the properties below are optional
            default_job_timeout_minutes=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_config=devicefarm.CfnProject.VpcConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        default_job_timeout_minutes: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProject.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The project's name.
        :param default_job_timeout_minutes: Sets the execution timeout value (in minutes) for a project. All test runs in this project use the specified execution timeout value unless overridden when scheduling a run.
        :param tags: The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.
        :param vpc_config: The VPC security groups and subnets that are attached to a project.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__235d8b8da76a28a97a451896d3b8c3cb58dfdd957be4b441ac00cfaaf1bccf64)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(
            name=name,
            default_job_timeout_minutes=default_job_timeout_minutes,
            tags=tags,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44321592fb37277f56b4c3ebb2731b7b3e6e2595385a1ef9fa999ecf399f65bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5290ce56dd54bd51b367f594f3fafb90e996c563b1803ea30c6c3105ca0d394)
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
        '''The Amazon Resource Name (ARN) of the project.

        See `Amazon resource names <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *General Reference guide* .

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
        '''The project's name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47a1a02042e033124a090a0b4c1edbb2a836b55be9cfe5cc7fd2d8f822070b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="defaultJobTimeoutMinutes")
    def default_job_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''Sets the execution timeout value (in minutes) for a project.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultJobTimeoutMinutes"))

    @default_job_timeout_minutes.setter
    def default_job_timeout_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acb87f983595b1a8464d152e1854f60b6c281bc9bee144f8c5527ab925d8e7ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultJobTimeoutMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41fbb1c60eec673fc1dd40b21d96b07f793303fbfbd3ec34d3536f2ad3b05f66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.VpcConfigProperty"]]:
        '''The VPC security groups and subnets that are attached to a project.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.VpcConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3fa42db493c8ae53f5c45defd768baab8f31711f46fd941b6fdd015f0417e30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devicefarm.CfnProject.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
            "vpc_id": "vpcId",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''The VPC security groups and subnets that are attached to a project.

            :param security_group_ids: A list of VPC security group IDs. A security group allows inbound traffic from network interfaces (and their associated instances) that are assigned to the same security group. See `Security groups <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon Virtual Private Cloud user guide* .
            :param subnet_ids: A subnet is a range of IP addresses in your VPC. You can launch Amazon resources, such as EC2 instances, into a specific subnet. When you create a subnet, you specify the IPv4 CIDR block for the subnet, which is a subset of the VPC CIDR block. See `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon Virtual Private Cloud user guide* .
            :param vpc_id: A list of VPC IDs. Each VPC is given a unique ID upon creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-project-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devicefarm as devicefarm
                
                vpc_config_property = devicefarm.CfnProject.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f11fa5faf31c5c93a8a6aafcc76bd21d7e1ba9accf46411ea1e06bd003aeba4)
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
            '''A list of VPC security group IDs.

            A security group allows inbound traffic from network interfaces (and their associated instances) that are assigned to the same security group. See `Security groups <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon Virtual Private Cloud user guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-project-vpcconfig.html#cfn-devicefarm-project-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''A subnet is a range of IP addresses in your VPC.

            You can launch Amazon resources, such as EC2 instances, into a specific subnet. When you create a subnet, you specify the IPv4 CIDR block for the subnet, which is a subset of the VPC CIDR block. See `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon Virtual Private Cloud user guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-project-vpcconfig.html#cfn-devicefarm-project-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''A list of VPC IDs.

            Each VPC is given a unique ID upon creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-project-vpcconfig.html#cfn-devicefarm-project-vpcconfig-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "default_job_timeout_minutes": "defaultJobTimeoutMinutes",
        "tags": "tags",
        "vpc_config": "vpcConfig",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        default_job_timeout_minutes: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProject``.

        :param name: The project's name.
        :param default_job_timeout_minutes: Sets the execution timeout value (in minutes) for a project. All test runs in this project use the specified execution timeout value unless overridden when scheduling a run.
        :param tags: The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.
        :param vpc_config: The VPC security groups and subnets that are attached to a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devicefarm as devicefarm
            
            cfn_project_props = devicefarm.CfnProjectProps(
                name="name",
            
                # the properties below are optional
                default_job_timeout_minutes=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_config=devicefarm.CfnProject.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6559d9d182fd1fc519eba56cb6cb8709e18e4013a0f927415f794e48faa0066c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_job_timeout_minutes", value=default_job_timeout_minutes, expected_type=type_hints["default_job_timeout_minutes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if default_job_timeout_minutes is not None:
            self._values["default_job_timeout_minutes"] = default_job_timeout_minutes
        if tags is not None:
            self._values["tags"] = tags
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def name(self) -> builtins.str:
        '''The project's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html#cfn-devicefarm-project-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_job_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''Sets the execution timeout value (in minutes) for a project.

        All test runs in this project use the specified execution timeout value unless overridden when scheduling a run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html#cfn-devicefarm-project-defaultjobtimeoutminutes
        '''
        result = self._values.get("default_job_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the resource.

        A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html#cfn-devicefarm-project-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.VpcConfigProperty]]:
        '''The VPC security groups and subnets that are attached to a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html#cfn-devicefarm-project-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTestGridProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnTestGridProject",
):
    '''A Selenium testing project.

    Projects are used to collect and collate sessions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devicefarm as devicefarm
        
        cfn_test_grid_project = devicefarm.CfnTestGridProject(self, "MyCfnTestGridProject",
            name="name",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_config=devicefarm.CfnTestGridProject.VpcConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
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
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestGridProject.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A human-readable name for the project.
        :param description: A human-readable description for the project.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .
        :param vpc_config: The VPC security groups and subnets that are attached to a project.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e22928736806899d37c63a4cf4f8d19875d02a5e91a831c1382fb292ebfa44)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTestGridProjectProps(
            name=name, description=description, tags=tags, vpc_config=vpc_config
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c7f8238381f2095506cd495955eb3cf26b1d8507e93baf9d05724e4a71b212f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__41d7d70a17d98dbbea986661dbd49bb3561b02c06d93b9e95cb506e4e9d84350)
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
        '''The Amazon Resource Name (ARN) of the ``TestGrid`` project.

        See `Amazon resource names <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *General Reference guide* .

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
        '''A human-readable name for the project.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e69a72fe7981b7f3cf862d501f307307a600980de1708e5a501d64dc0e8bb975)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description for the project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb4b8d6c81f5dd3da8217e1467fb328f1359edfa9f92773ad9f1d59a64cc3c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__839e0e2af77c8f8632b9f83508bf02b7b33847eec29181251d8a3f13e6bb93bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestGridProject.VpcConfigProperty"]]:
        '''The VPC security groups and subnets that are attached to a project.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestGridProject.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestGridProject.VpcConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ba7775df3aab5a721601164793bf3cc9a7f50b0967434f40a6a0e1f4e24d34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devicefarm.CfnTestGridProject.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
            "vpc_id": "vpcId",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''The VPC security groups and subnets attached to the ``TestGrid`` project.

            :param security_group_ids: A list of VPC security group IDs. A security group allows inbound traffic from network interfaces (and their associated instances) that are assigned to the same security group. See `Security groups <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon Virtual Private Cloud user guide* .
            :param subnet_ids: A list of VPC subnet IDs. A subnet is a range of IP addresses in your VPC. You can launch Amazon resources, such as EC2 instances, into a specific subnet. When you create a subnet, you specify the IPv4 CIDR block for the subnet, which is a subset of the VPC CIDR block. See `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon Virtual Private Cloud user guide* .
            :param vpc_id: A list of VPC IDs. Each VPC is given a unique ID upon creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devicefarm as devicefarm
                
                vpc_config_property = devicefarm.CfnTestGridProject.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__461a87a81b78a91ff3aa979869cf6e45bb379336dce9c9deba22bfe05b4f2630)
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
            '''A list of VPC security group IDs.

            A security group allows inbound traffic from network interfaces (and their associated instances) that are assigned to the same security group. See `Security groups <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon Virtual Private Cloud user guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html#cfn-devicefarm-testgridproject-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''A list of VPC subnet IDs.

            A subnet is a range of IP addresses in your VPC. You can launch Amazon resources, such as EC2 instances, into a specific subnet. When you create a subnet, you specify the IPv4 CIDR block for the subnet, which is a subset of the VPC CIDR block. See `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon Virtual Private Cloud user guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html#cfn-devicefarm-testgridproject-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''A list of VPC IDs.

            Each VPC is given a unique ID upon creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html#cfn-devicefarm-testgridproject-vpcconfig-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnTestGridProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "tags": "tags",
        "vpc_config": "vpcConfig",
    },
)
class CfnTestGridProjectProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestGridProject.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTestGridProject``.

        :param name: A human-readable name for the project.
        :param description: A human-readable description for the project.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .
        :param vpc_config: The VPC security groups and subnets that are attached to a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devicefarm as devicefarm
            
            cfn_test_grid_project_props = devicefarm.CfnTestGridProjectProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_config=devicefarm.CfnTestGridProject.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e145dbb564c006058fffdd2f8e7b8379a9b6dbbd495c537021b0c7c8704a07f7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def name(self) -> builtins.str:
        '''A human-readable name for the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html#cfn-devicefarm-testgridproject-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description for the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html#cfn-devicefarm-testgridproject-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html#cfn-devicefarm-testgridproject-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTestGridProject.VpcConfigProperty]]:
        '''The VPC security groups and subnets that are attached to a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html#cfn-devicefarm-testgridproject-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTestGridProject.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTestGridProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVPCEConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnVPCEConfiguration",
):
    '''Creates a configuration record in Device Farm for your Amazon Virtual Private Cloud (VPC) endpoint service.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devicefarm as devicefarm
        
        cfn_vPCEConfiguration = devicefarm.CfnVPCEConfiguration(self, "MyCfnVPCEConfiguration",
            service_dns_name="serviceDnsName",
            vpce_configuration_name="vpceConfigurationName",
            vpce_service_name="vpceServiceName",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpce_configuration_description="vpceConfigurationDescription"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        service_dns_name: builtins.str,
        vpce_configuration_name: builtins.str,
        vpce_service_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpce_configuration_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param service_dns_name: The DNS name that Device Farm will use to map to the private service you want to access.
        :param vpce_configuration_name: The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.
        :param vpce_service_name: The name of the VPC endpoint service that you want to access from Device Farm. The name follows the format ``com.amazonaws.vpce.us-west-2.vpce-svc-id`` .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .
        :param vpce_configuration_description: An optional description that provides details about your VPC endpoint configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ef2954941f94384014186cbe5af3721ce845014f6d2b72d0ecf56ea0e3af74c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVPCEConfigurationProps(
            service_dns_name=service_dns_name,
            vpce_configuration_name=vpce_configuration_name,
            vpce_service_name=vpce_service_name,
            tags=tags,
            vpce_configuration_description=vpce_configuration_description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1100b54b5235c753735625a2a7d07a06487c35fe52ade7370085c0cb1c31474b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b691f440079c02358295caacf09742ca98ffe00aa27da31efc40a2026b36b767)
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
        '''The Amazon Resource Name (ARN) of the VPC endpoint.

        See `Amazon resource names <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *General Reference guide* .

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
    @jsii.member(jsii_name="serviceDnsName")
    def service_dns_name(self) -> builtins.str:
        '''The DNS name that Device Farm will use to map to the private service you want to access.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceDnsName"))

    @service_dns_name.setter
    def service_dns_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__303fa798fb179bced207d19511c9b9acf5c07b6fec70c5048124af36a17ac05b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceDnsName", value)

    @builtins.property
    @jsii.member(jsii_name="vpceConfigurationName")
    def vpce_configuration_name(self) -> builtins.str:
        '''The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.'''
        return typing.cast(builtins.str, jsii.get(self, "vpceConfigurationName"))

    @vpce_configuration_name.setter
    def vpce_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429ed254d7f9645dfbe4b648765fd8937703a3527539e86e90498b7579782c3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpceConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="vpceServiceName")
    def vpce_service_name(self) -> builtins.str:
        '''The name of the VPC endpoint service that you want to access from Device Farm.'''
        return typing.cast(builtins.str, jsii.get(self, "vpceServiceName"))

    @vpce_service_name.setter
    def vpce_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab2e068f76446cab8036e2887d473c46e5f0dff77387f3a30458de56875ed3d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpceServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb179a9789e5e93c2563eb8ce552738b43c5fae6e5fd73954a892f883d762ca4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpceConfigurationDescription")
    def vpce_configuration_description(self) -> typing.Optional[builtins.str]:
        '''An optional description that provides details about your VPC endpoint configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpceConfigurationDescription"))

    @vpce_configuration_description.setter
    def vpce_configuration_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad8666cad9848e46a023b0491b1f108be17c542f79bd3b15e1249ec20acba18e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpceConfigurationDescription", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devicefarm.CfnVPCEConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "service_dns_name": "serviceDnsName",
        "vpce_configuration_name": "vpceConfigurationName",
        "vpce_service_name": "vpceServiceName",
        "tags": "tags",
        "vpce_configuration_description": "vpceConfigurationDescription",
    },
)
class CfnVPCEConfigurationProps:
    def __init__(
        self,
        *,
        service_dns_name: builtins.str,
        vpce_configuration_name: builtins.str,
        vpce_service_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpce_configuration_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVPCEConfiguration``.

        :param service_dns_name: The DNS name that Device Farm will use to map to the private service you want to access.
        :param vpce_configuration_name: The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.
        :param vpce_service_name: The name of the VPC endpoint service that you want to access from Device Farm. The name follows the format ``com.amazonaws.vpce.us-west-2.vpce-svc-id`` .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .
        :param vpce_configuration_description: An optional description that provides details about your VPC endpoint configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devicefarm as devicefarm
            
            cfn_vPCEConfiguration_props = devicefarm.CfnVPCEConfigurationProps(
                service_dns_name="serviceDnsName",
                vpce_configuration_name="vpceConfigurationName",
                vpce_service_name="vpceServiceName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpce_configuration_description="vpceConfigurationDescription"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2fb366fc648b755fe6a00060b1f28d06967c5eb962b685679e28dc9b18a9069)
            check_type(argname="argument service_dns_name", value=service_dns_name, expected_type=type_hints["service_dns_name"])
            check_type(argname="argument vpce_configuration_name", value=vpce_configuration_name, expected_type=type_hints["vpce_configuration_name"])
            check_type(argname="argument vpce_service_name", value=vpce_service_name, expected_type=type_hints["vpce_service_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpce_configuration_description", value=vpce_configuration_description, expected_type=type_hints["vpce_configuration_description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_dns_name": service_dns_name,
            "vpce_configuration_name": vpce_configuration_name,
            "vpce_service_name": vpce_service_name,
        }
        if tags is not None:
            self._values["tags"] = tags
        if vpce_configuration_description is not None:
            self._values["vpce_configuration_description"] = vpce_configuration_description

    @builtins.property
    def service_dns_name(self) -> builtins.str:
        '''The DNS name that Device Farm will use to map to the private service you want to access.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html#cfn-devicefarm-vpceconfiguration-servicednsname
        '''
        result = self._values.get("service_dns_name")
        assert result is not None, "Required property 'service_dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpce_configuration_name(self) -> builtins.str:
        '''The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html#cfn-devicefarm-vpceconfiguration-vpceconfigurationname
        '''
        result = self._values.get("vpce_configuration_name")
        assert result is not None, "Required property 'vpce_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpce_service_name(self) -> builtins.str:
        '''The name of the VPC endpoint service that you want to access from Device Farm.

        The name follows the format ``com.amazonaws.vpce.us-west-2.vpce-svc-id`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html#cfn-devicefarm-vpceconfiguration-vpceservicename
        '''
        result = self._values.get("vpce_service_name")
        assert result is not None, "Required property 'vpce_service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html#cfn-devicefarm-vpceconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpce_configuration_description(self) -> typing.Optional[builtins.str]:
        '''An optional description that provides details about your VPC endpoint configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html#cfn-devicefarm-vpceconfiguration-vpceconfigurationdescription
        '''
        result = self._values.get("vpce_configuration_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVPCEConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDevicePool",
    "CfnDevicePoolProps",
    "CfnInstanceProfile",
    "CfnInstanceProfileProps",
    "CfnNetworkProfile",
    "CfnNetworkProfileProps",
    "CfnProject",
    "CfnProjectProps",
    "CfnTestGridProject",
    "CfnTestGridProjectProps",
    "CfnVPCEConfiguration",
    "CfnVPCEConfigurationProps",
]

publication.publish()

def _typecheckingstub__96c6314bfee539a8146973e0d5495e39f622c4c3953e795d05460e2bb76cc8db(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    project_arn: builtins.str,
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevicePool.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    max_devices: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06066b24c235ef43fb2b2aa45da0a1ad576ff065b3b44d12f93725c3a454a27e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f86a0ff3bc397ecbead77b1e7a92e74d7aa974b4e493527a64fb12b9571595(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__274a6264ef4f53855c7fb29b5e3d4eaea2f1ecaa2b107832b5c87514be43bd21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90da46d699d68d2324638e678e647ad8536c9865f9885776a4593a4c7bbd5a81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__878e6373669e306e9365c0b15e6adde48fdf3dfe289f45637e1a549ae9da641b(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDevicePool.RuleProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2af8686131384f19961bfed2d06ace261ff278057a6b7b8a2ce5fb08a50041(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678df3a1e7f007b97b7ca6f058747cd03c5fd1d9c97dce118f6007e5ff5cb8b3(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2cf7f4efbed5d263cca53206f67753b2376cc6beb829af18416bb2774b62a6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0620996469fe8ee5556b96e0e9cda4bff8b92c7e9aa8aa5903cb6dd043c2aafa(
    *,
    attribute: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdbd0dbaf5eeb8e0d1a370581a06a71801ff0d57bd9fd8d87abcb95e23dea50c(
    *,
    name: builtins.str,
    project_arn: builtins.str,
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevicePool.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    max_devices: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9dd1552bba1f4a322e22652920f9f1fa8079a149ae08cb1e20455b8f7a548b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    exclude_app_packages_from_cleanup: typing.Optional[typing.Sequence[builtins.str]] = None,
    package_cleanup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    reboot_after_use: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c146e7e4ae72d3aab6ff3154ac09aa531bf8c9be0d22f33d454b43266ed916b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c6fa7b46bf9514b077b27808bc205832a47a5c1dc9141e47081ba716d2c99f1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17aaeb013eadb1aa2000886131450d5986814e62564399d33943dc37661073b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c39d2e3a3b084568408244f32d6a7e381af3a3ad557c2426a2adb5528556edd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57be4bbd251344311f39ec38b200083c315e5a9d8dbbf607068d9cd09772107c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94278fbf52719304b1eeb162c050b5e9626d58ff0e40eb901b64a01f27e63972(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e2f9337c3eb103f9e3a27518e293407dc94e98fee92f2b33af3b1d9dd60698(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5194955750aa2f8304da100d5f6b3035ceebeb29d5b599f07f657cc4f7516714(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7392c4b7cccfb4ed48f655dd9ef8cfdda0d147224dceaf92b58913cc7bdedf0a(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    exclude_app_packages_from_cleanup: typing.Optional[typing.Sequence[builtins.str]] = None,
    package_cleanup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    reboot_after_use: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600f319c8811bcdb37dc45d939671c38345fae417a48df83d7c3947fbe55cf29(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    project_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    downlink_bandwidth_bits: typing.Optional[jsii.Number] = None,
    downlink_delay_ms: typing.Optional[jsii.Number] = None,
    downlink_jitter_ms: typing.Optional[jsii.Number] = None,
    downlink_loss_percent: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    uplink_bandwidth_bits: typing.Optional[jsii.Number] = None,
    uplink_delay_ms: typing.Optional[jsii.Number] = None,
    uplink_jitter_ms: typing.Optional[jsii.Number] = None,
    uplink_loss_percent: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802be6b3874919bcab4f00f242ef5917d7ef30a2d95bf1f24d93fb8bd6b68061(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4605f7133abcc717586ae72fbe7d0ba058bf6bba8231c05d91a00c8425f69441(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__294fb5334d61ef0ae6269e6e607f8c61028dacb1a4add762eec71b2612e6636b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8541a8aba350561662e9c4d9ecd7dc3c858e32f43e2a6fe4f1881247500cc635(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313840f222b69f6c215057569c0535e7837093d8a0e7cdf0884c32077a8a185d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c52a6ab2b4d0eff01793635e9b13503e20d77676ea2af5a9532742ae76daa9f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__781a2c75da42bd3d4cbc7e741db98d2bd12afe98b409d2b695ffe930455c16a9(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d556a294ba93bfc2f2891e5fad916e5c4dbb6c8139939917faf51a5b43cf1c1a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29bab9b49350109aa13762d05ee89e4a0164006247dcfcb9c1ba4a5a796ab8d2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77650cacecfe99d7da6cd303af7b455933a1f46c7deac85cc197d3802ce9dbff(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c1e25acdc2a7a9c94eddec633a3bc73b43204c3f335d0d5fba44e365ee2c942(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1ad1e5df83993d7d970aec5ba6a43acc420e87f67358c48cc12a958cd04ff2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c26698da5c33e2193aefb85ace5f3b2907c0d48412dcb4b7992ac539b16e2ea(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c91f7aaeb08d797687bac8c6cbf867868774ba52b3d695b1a462f31536446cd8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd5cc9e50d96fdbb41dccca0bc93936eeaacdb252c6703a366abcfc675c8b32(
    *,
    name: builtins.str,
    project_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    downlink_bandwidth_bits: typing.Optional[jsii.Number] = None,
    downlink_delay_ms: typing.Optional[jsii.Number] = None,
    downlink_jitter_ms: typing.Optional[jsii.Number] = None,
    downlink_loss_percent: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    uplink_bandwidth_bits: typing.Optional[jsii.Number] = None,
    uplink_delay_ms: typing.Optional[jsii.Number] = None,
    uplink_jitter_ms: typing.Optional[jsii.Number] = None,
    uplink_loss_percent: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235d8b8da76a28a97a451896d3b8c3cb58dfdd957be4b441ac00cfaaf1bccf64(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    default_job_timeout_minutes: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44321592fb37277f56b4c3ebb2731b7b3e6e2595385a1ef9fa999ecf399f65bd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5290ce56dd54bd51b367f594f3fafb90e996c563b1803ea30c6c3105ca0d394(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47a1a02042e033124a090a0b4c1edbb2a836b55be9cfe5cc7fd2d8f822070b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acb87f983595b1a8464d152e1854f60b6c281bc9bee144f8c5527ab925d8e7ed(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41fbb1c60eec673fc1dd40b21d96b07f793303fbfbd3ec34d3536f2ad3b05f66(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3fa42db493c8ae53f5c45defd768baab8f31711f46fd941b6fdd015f0417e30(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.VpcConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f11fa5faf31c5c93a8a6aafcc76bd21d7e1ba9accf46411ea1e06bd003aeba4(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6559d9d182fd1fc519eba56cb6cb8709e18e4013a0f927415f794e48faa0066c(
    *,
    name: builtins.str,
    default_job_timeout_minutes: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e22928736806899d37c63a4cf4f8d19875d02a5e91a831c1382fb292ebfa44(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestGridProject.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c7f8238381f2095506cd495955eb3cf26b1d8507e93baf9d05724e4a71b212f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d7d70a17d98dbbea986661dbd49bb3561b02c06d93b9e95cb506e4e9d84350(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69a72fe7981b7f3cf862d501f307307a600980de1708e5a501d64dc0e8bb975(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb4b8d6c81f5dd3da8217e1467fb328f1359edfa9f92773ad9f1d59a64cc3c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__839e0e2af77c8f8632b9f83508bf02b7b33847eec29181251d8a3f13e6bb93bd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ba7775df3aab5a721601164793bf3cc9a7f50b0967434f40a6a0e1f4e24d34(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTestGridProject.VpcConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__461a87a81b78a91ff3aa979869cf6e45bb379336dce9c9deba22bfe05b4f2630(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e145dbb564c006058fffdd2f8e7b8379a9b6dbbd495c537021b0c7c8704a07f7(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestGridProject.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ef2954941f94384014186cbe5af3721ce845014f6d2b72d0ecf56ea0e3af74c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    service_dns_name: builtins.str,
    vpce_configuration_name: builtins.str,
    vpce_service_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpce_configuration_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1100b54b5235c753735625a2a7d07a06487c35fe52ade7370085c0cb1c31474b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b691f440079c02358295caacf09742ca98ffe00aa27da31efc40a2026b36b767(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__303fa798fb179bced207d19511c9b9acf5c07b6fec70c5048124af36a17ac05b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429ed254d7f9645dfbe4b648765fd8937703a3527539e86e90498b7579782c3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab2e068f76446cab8036e2887d473c46e5f0dff77387f3a30458de56875ed3d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb179a9789e5e93c2563eb8ce552738b43c5fae6e5fd73954a892f883d762ca4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad8666cad9848e46a023b0491b1f108be17c542f79bd3b15e1249ec20acba18e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2fb366fc648b755fe6a00060b1f28d06967c5eb962b685679e28dc9b18a9069(
    *,
    service_dns_name: builtins.str,
    vpce_configuration_name: builtins.str,
    vpce_service_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpce_configuration_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
