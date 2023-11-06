'''
# AWS::IoTCoreDeviceAdvisor Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotcoredeviceadvisor as iotcoredeviceadvisor
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTCoreDeviceAdvisor construct libraries](https://constructs.dev/search?q=iotcoredeviceadvisor)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTCoreDeviceAdvisor resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTCoreDeviceAdvisor.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTCoreDeviceAdvisor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTCoreDeviceAdvisor.html).

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
class CfnSuiteDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotcoredeviceadvisor.CfnSuiteDefinition",
):
    '''Creates a Device Advisor test suite.

    Requires permission to access the `CreateSuiteDefinition <https://docs.aws.amazon.com//service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions>`_ action.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotcoredeviceadvisor as iotcoredeviceadvisor
        
        # suite_definition_configuration: Any
        
        cfn_suite_definition = iotcoredeviceadvisor.CfnSuiteDefinition(self, "MyCfnSuiteDefinition",
            suite_definition_configuration=suite_definition_configuration,
        
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
        suite_definition_configuration: typing.Any,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param suite_definition_configuration: The configuration of the Suite Definition. Listed below are the required elements of the ``SuiteDefinitionConfiguration`` . - ***devicePermissionRoleArn*** - The device permission arn. This is a required element. *Type:* String - ***devices*** - The list of configured devices under test. For more information on devices under test, see `DeviceUnderTest <https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_DeviceUnderTest.html>`_ Not a required element. *Type:* List of devices under test - ***intendedForQualification*** - The tests intended for qualification in a suite. Not a required element. *Type:* Boolean - ***rootGroup*** - The test suite root group. For more information on creating and using root groups see the `Device Advisor workflow <https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html>`_ . This is a required element. *Type:* String - ***suiteDefinitionName*** - The Suite Definition Configuration name. This is a required element. *Type:* String
        :param tags: Metadata that can be used to manage the the Suite Definition.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945861bb0ea34e6da34c3c8b60ba3b233f881a73cecd8fa75200bae6d1751207)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSuiteDefinitionProps(
            suite_definition_configuration=suite_definition_configuration, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93d16fdf80d2c88f3a287c1dd112d9390b367d543fcb21c7d645e5a89d9fa526)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e8121e05cd80e64c784f210231931cd13937eaec945d61023f3a7e4ab0543d6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSuiteDefinitionArn")
    def attr_suite_definition_arn(self) -> builtins.str:
        '''The Arn of the Suite Definition.

        :cloudformationAttribute: SuiteDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSuiteDefinitionId")
    def attr_suite_definition_id(self) -> builtins.str:
        '''The version of the Suite Definition.

        :cloudformationAttribute: SuiteDefinitionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionId"))

    @builtins.property
    @jsii.member(jsii_name="attrSuiteDefinitionVersion")
    def attr_suite_definition_version(self) -> builtins.str:
        '''The ID of the Suite Definition.

        :cloudformationAttribute: SuiteDefinitionVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionVersion"))

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
    @jsii.member(jsii_name="suiteDefinitionConfiguration")
    def suite_definition_configuration(self) -> typing.Any:
        '''The configuration of the Suite Definition.

        Listed below are the required elements of the ``SuiteDefinitionConfiguration`` .
        '''
        return typing.cast(typing.Any, jsii.get(self, "suiteDefinitionConfiguration"))

    @suite_definition_configuration.setter
    def suite_definition_configuration(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317c2091d233afa7482c288ee5b7936df2985381cf92c37042f75df938b06ccc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suiteDefinitionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the the Suite Definition.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cbe94c4a5fef0228a9bbec1e1b5971dc30e57c5e6ab1bc763768655a7a6620f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotcoredeviceadvisor.CfnSuiteDefinition.DeviceUnderTestProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_arn": "certificateArn", "thing_arn": "thingArn"},
    )
    class DeviceUnderTestProperty:
        def __init__(
            self,
            *,
            certificate_arn: typing.Optional[builtins.str] = None,
            thing_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param certificate_arn: 
            :param thing_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotcoredeviceadvisor as iotcoredeviceadvisor
                
                device_under_test_property = iotcoredeviceadvisor.CfnSuiteDefinition.DeviceUnderTestProperty(
                    certificate_arn="certificateArn",
                    thing_arn="thingArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__625a8e0f800bb7ba71cb50744ee106faeba855d9438d3877f0cabec98d9350d3)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_arn is not None:
                self._values["certificate_arn"] = certificate_arn
            if thing_arn is not None:
                self._values["thing_arn"] = thing_arn

        @builtins.property
        def certificate_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.html#cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-certificatearn
            '''
            result = self._values.get("certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def thing_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.html#cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-thingarn
            '''
            result = self._values.get("thing_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceUnderTestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotcoredeviceadvisor.CfnSuiteDefinition.SuiteDefinitionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_permission_role_arn": "devicePermissionRoleArn",
            "root_group": "rootGroup",
            "devices": "devices",
            "intended_for_qualification": "intendedForQualification",
            "suite_definition_name": "suiteDefinitionName",
        },
    )
    class SuiteDefinitionConfigurationProperty:
        def __init__(
            self,
            *,
            device_permission_role_arn: builtins.str,
            root_group: builtins.str,
            devices: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSuiteDefinition.DeviceUnderTestProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            intended_for_qualification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            suite_definition_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param device_permission_role_arn: The device permission role arn of the test suite.
            :param root_group: The root group of the test suite.
            :param devices: The devices being tested in the test suite.
            :param intended_for_qualification: Whether the tests are intended for qualification in a suite.
            :param suite_definition_name: The Name of the suite definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotcoredeviceadvisor as iotcoredeviceadvisor
                
                suite_definition_configuration_property = iotcoredeviceadvisor.CfnSuiteDefinition.SuiteDefinitionConfigurationProperty(
                    device_permission_role_arn="devicePermissionRoleArn",
                    root_group="rootGroup",
                
                    # the properties below are optional
                    devices=[iotcoredeviceadvisor.CfnSuiteDefinition.DeviceUnderTestProperty(
                        certificate_arn="certificateArn",
                        thing_arn="thingArn"
                    )],
                    intended_for_qualification=False,
                    suite_definition_name="suiteDefinitionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ca9dfe56a34afc7e2b0f82879e2d57319c1c636afc88023fc9e530655c375c5b)
                check_type(argname="argument device_permission_role_arn", value=device_permission_role_arn, expected_type=type_hints["device_permission_role_arn"])
                check_type(argname="argument root_group", value=root_group, expected_type=type_hints["root_group"])
                check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
                check_type(argname="argument intended_for_qualification", value=intended_for_qualification, expected_type=type_hints["intended_for_qualification"])
                check_type(argname="argument suite_definition_name", value=suite_definition_name, expected_type=type_hints["suite_definition_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "device_permission_role_arn": device_permission_role_arn,
                "root_group": root_group,
            }
            if devices is not None:
                self._values["devices"] = devices
            if intended_for_qualification is not None:
                self._values["intended_for_qualification"] = intended_for_qualification
            if suite_definition_name is not None:
                self._values["suite_definition_name"] = suite_definition_name

        @builtins.property
        def device_permission_role_arn(self) -> builtins.str:
            '''The device permission role arn of the test suite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devicepermissionrolearn
            '''
            result = self._values.get("device_permission_role_arn")
            assert result is not None, "Required property 'device_permission_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def root_group(self) -> builtins.str:
            '''The root group of the test suite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-rootgroup
            '''
            result = self._values.get("root_group")
            assert result is not None, "Required property 'root_group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def devices(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSuiteDefinition.DeviceUnderTestProperty"]]]]:
            '''The devices being tested in the test suite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devices
            '''
            result = self._values.get("devices")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSuiteDefinition.DeviceUnderTestProperty"]]]], result)

        @builtins.property
        def intended_for_qualification(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether the tests are intended for qualification in a suite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-intendedforqualification
            '''
            result = self._values.get("intended_for_qualification")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def suite_definition_name(self) -> typing.Optional[builtins.str]:
            '''The Name of the suite definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-suitedefinitionname
            '''
            result = self._values.get("suite_definition_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SuiteDefinitionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotcoredeviceadvisor.CfnSuiteDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "suite_definition_configuration": "suiteDefinitionConfiguration",
        "tags": "tags",
    },
)
class CfnSuiteDefinitionProps:
    def __init__(
        self,
        *,
        suite_definition_configuration: typing.Any,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSuiteDefinition``.

        :param suite_definition_configuration: The configuration of the Suite Definition. Listed below are the required elements of the ``SuiteDefinitionConfiguration`` . - ***devicePermissionRoleArn*** - The device permission arn. This is a required element. *Type:* String - ***devices*** - The list of configured devices under test. For more information on devices under test, see `DeviceUnderTest <https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_DeviceUnderTest.html>`_ Not a required element. *Type:* List of devices under test - ***intendedForQualification*** - The tests intended for qualification in a suite. Not a required element. *Type:* Boolean - ***rootGroup*** - The test suite root group. For more information on creating and using root groups see the `Device Advisor workflow <https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html>`_ . This is a required element. *Type:* String - ***suiteDefinitionName*** - The Suite Definition Configuration name. This is a required element. *Type:* String
        :param tags: Metadata that can be used to manage the the Suite Definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotcoredeviceadvisor as iotcoredeviceadvisor
            
            # suite_definition_configuration: Any
            
            cfn_suite_definition_props = iotcoredeviceadvisor.CfnSuiteDefinitionProps(
                suite_definition_configuration=suite_definition_configuration,
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a1bf45ec004a9aea8096b474c6edc62abc371cd3d6adc9e0f1362e1053a1891)
            check_type(argname="argument suite_definition_configuration", value=suite_definition_configuration, expected_type=type_hints["suite_definition_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "suite_definition_configuration": suite_definition_configuration,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def suite_definition_configuration(self) -> typing.Any:
        '''The configuration of the Suite Definition. Listed below are the required elements of the ``SuiteDefinitionConfiguration`` .

        - ***devicePermissionRoleArn*** - The device permission arn.

        This is a required element.

        *Type:* String

        - ***devices*** - The list of configured devices under test. For more information on devices under test, see `DeviceUnderTest <https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_DeviceUnderTest.html>`_

        Not a required element.

        *Type:* List of devices under test

        - ***intendedForQualification*** - The tests intended for qualification in a suite.

        Not a required element.

        *Type:* Boolean

        - ***rootGroup*** - The test suite root group. For more information on creating and using root groups see the `Device Advisor workflow <https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html>`_ .

        This is a required element.

        *Type:* String

        - ***suiteDefinitionName*** - The Suite Definition Configuration name.

        This is a required element.

        *Type:* String

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        '''
        result = self._values.get("suite_definition_configuration")
        assert result is not None, "Required property 'suite_definition_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the the Suite Definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSuiteDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSuiteDefinition",
    "CfnSuiteDefinitionProps",
]

publication.publish()

def _typecheckingstub__945861bb0ea34e6da34c3c8b60ba3b233f881a73cecd8fa75200bae6d1751207(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    suite_definition_configuration: typing.Any,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d16fdf80d2c88f3a287c1dd112d9390b367d543fcb21c7d645e5a89d9fa526(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8121e05cd80e64c784f210231931cd13937eaec945d61023f3a7e4ab0543d6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317c2091d233afa7482c288ee5b7936df2985381cf92c37042f75df938b06ccc(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cbe94c4a5fef0228a9bbec1e1b5971dc30e57c5e6ab1bc763768655a7a6620f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__625a8e0f800bb7ba71cb50744ee106faeba855d9438d3877f0cabec98d9350d3(
    *,
    certificate_arn: typing.Optional[builtins.str] = None,
    thing_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca9dfe56a34afc7e2b0f82879e2d57319c1c636afc88023fc9e530655c375c5b(
    *,
    device_permission_role_arn: builtins.str,
    root_group: builtins.str,
    devices: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSuiteDefinition.DeviceUnderTestProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    intended_for_qualification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    suite_definition_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1bf45ec004a9aea8096b474c6edc62abc371cd3d6adc9e0f1362e1053a1891(
    *,
    suite_definition_configuration: typing.Any,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
