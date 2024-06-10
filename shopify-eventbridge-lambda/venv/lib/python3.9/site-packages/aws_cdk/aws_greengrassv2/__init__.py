'''
# AWS::GreengrassV2 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_greengrassv2 as greengrass
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for GreengrassV2 construct libraries](https://constructs.dev/search?q=greengrassv2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::GreengrassV2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GreengrassV2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GreengrassV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GreengrassV2.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnComponentVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion",
):
    '''Creates a component.

    Components are software that run on AWS IoT Greengrass core devices. After you develop and test a component on your core device, you can use this operation to upload your component to AWS IoT Greengrass . Then, you can deploy the component to other core devices.

    You can use this operation to do the following:

    - *Create components from recipes*

    Create a component from a recipe, which is a file that defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform capability. For more information, see `AWS IoT Greengrass component recipe reference <https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

    To create a component from a recipe, specify ``inlineRecipe`` when you call this operation.

    - *Create components from Lambda functions*

    Create a component from an AWS Lambda function that runs on AWS IoT Greengrass . This creates a recipe and artifacts from the Lambda function's deployment package. You can use this operation to migrate Lambda functions from AWS IoT Greengrass V1 to AWS IoT Greengrass V2 .

    This function accepts Lambda functions in all supported versions of Python, Node.js, and Java runtimes. AWS IoT Greengrass doesn't apply any additional restrictions on deprecated Lambda runtime versions.

    To create a component from a Lambda function, specify ``lambdaFunction`` when you call this operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html
    :cloudformationResource: AWS::GreengrassV2::ComponentVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrassv2 as greengrassv2
        
        cfn_component_version = greengrassv2.CfnComponentVersion(self, "MyCfnComponentVersion",
            inline_recipe="inlineRecipe",
            lambda_function=greengrassv2.CfnComponentVersion.LambdaFunctionRecipeSourceProperty(
                component_dependencies={
                    "component_dependencies_key": greengrassv2.CfnComponentVersion.ComponentDependencyRequirementProperty(
                        dependency_type="dependencyType",
                        version_requirement="versionRequirement"
                    )
                },
                component_lambda_parameters=greengrassv2.CfnComponentVersion.LambdaExecutionParametersProperty(
                    environment_variables={
                        "environment_variables_key": "environmentVariables"
                    },
                    event_sources=[greengrassv2.CfnComponentVersion.LambdaEventSourceProperty(
                        topic="topic",
                        type="type"
                    )],
                    exec_args=["execArgs"],
                    input_payload_encoding_type="inputPayloadEncodingType",
                    linux_process_params=greengrassv2.CfnComponentVersion.LambdaLinuxProcessParamsProperty(
                        container_params=greengrassv2.CfnComponentVersion.LambdaContainerParamsProperty(
                            devices=[greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty(
                                add_group_owner=False,
                                path="path",
                                permission="permission"
                            )],
                            memory_size_in_kb=123,
                            mount_ro_sysfs=False,
                            volumes=[greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty(
                                add_group_owner=False,
                                destination_path="destinationPath",
                                permission="permission",
                                source_path="sourcePath"
                            )]
                        ),
                        isolation_mode="isolationMode"
                    ),
                    max_idle_time_in_seconds=123,
                    max_instances_count=123,
                    max_queue_size=123,
                    pinned=False,
                    status_timeout_in_seconds=123,
                    timeout_in_seconds=123
                ),
                component_name="componentName",
                component_platforms=[greengrassv2.CfnComponentVersion.ComponentPlatformProperty(
                    attributes={
                        "attributes_key": "attributes"
                    },
                    name="name"
                )],
                component_version="componentVersion",
                lambda_arn="lambdaArn"
            ),
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
        inline_recipe: typing.Optional[builtins.str] = None,
        lambda_function: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.LambdaFunctionRecipeSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param inline_recipe: The recipe to use to create the component. The recipe defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform compatibility. You must specify either ``InlineRecipe`` or ``LambdaFunction`` .
        :param lambda_function: The parameters to create a component from a Lambda function. You must specify either ``InlineRecipe`` or ``LambdaFunction`` .
        :param tags: Application-specific metadata to attach to the component version. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tag your AWS IoT Greengrass Version 2 resources <https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5d46224f527e073fe7f6fbe54ccaca3f0045fcc0ade3462681ae8b0575c59e0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComponentVersionProps(
            inline_recipe=inline_recipe, lambda_function=lambda_function, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b4437bb59606a2a9dbc98b6d542a546264b4ce6dc5594c04c8503a477b837c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddcadfc186b2781e90bf0c28ccaed5edc30f8c0c7447e9310fac34a6349fcda8)
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
        '''The ARN of the component version.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrComponentName")
    def attr_component_name(self) -> builtins.str:
        '''The name of the component.

        :cloudformationAttribute: ComponentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComponentName"))

    @builtins.property
    @jsii.member(jsii_name="attrComponentVersion")
    def attr_component_version(self) -> builtins.str:
        '''The version of the component.

        :cloudformationAttribute: ComponentVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComponentVersion"))

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
    @jsii.member(jsii_name="inlineRecipe")
    def inline_recipe(self) -> typing.Optional[builtins.str]:
        '''The recipe to use to create the component.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inlineRecipe"))

    @inline_recipe.setter
    def inline_recipe(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72eb28bfc29eebefc2ec5d2aace9f7b9a334fa75c8691abf39303421830fabd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inlineRecipe", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaFunctionRecipeSourceProperty"]]:
        '''The parameters to create a component from a Lambda function.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaFunctionRecipeSourceProperty"]], jsii.get(self, "lambdaFunction"))

    @lambda_function.setter
    def lambda_function(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaFunctionRecipeSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ccfa77f00c9c04773ae0643b7f2f0b369127a28b9747cbe78bfe426dc32f46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaFunction", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Application-specific metadata to attach to the component version.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0267e3a5b2b19b25e52f0bee8bba8f4880b864731b0138cdd45e5b72ec1bc7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.ComponentDependencyRequirementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dependency_type": "dependencyType",
            "version_requirement": "versionRequirement",
        },
    )
    class ComponentDependencyRequirementProperty:
        def __init__(
            self,
            *,
            dependency_type: typing.Optional[builtins.str] = None,
            version_requirement: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about a component dependency for a Lambda function component.

            :param dependency_type: The type of this dependency. Choose from the following options:. - ``SOFT`` – The component doesn't restart if the dependency changes state. - ``HARD`` – The component restarts if the dependency changes state. Default: ``HARD``
            :param version_requirement: The component version requirement for the component dependency. AWS IoT Greengrass uses semantic version constraints. For more information, see `Semantic Versioning <https://docs.aws.amazon.com/https://semver.org/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                component_dependency_requirement_property = greengrassv2.CfnComponentVersion.ComponentDependencyRequirementProperty(
                    dependency_type="dependencyType",
                    version_requirement="versionRequirement"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c678ca853046a4f9a77f7c2dd92c2ab09d84c106fa6e8f450dca99e2f6edbf9)
                check_type(argname="argument dependency_type", value=dependency_type, expected_type=type_hints["dependency_type"])
                check_type(argname="argument version_requirement", value=version_requirement, expected_type=type_hints["version_requirement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dependency_type is not None:
                self._values["dependency_type"] = dependency_type
            if version_requirement is not None:
                self._values["version_requirement"] = version_requirement

        @builtins.property
        def dependency_type(self) -> typing.Optional[builtins.str]:
            '''The type of this dependency. Choose from the following options:.

            - ``SOFT`` – The component doesn't restart if the dependency changes state.
            - ``HARD`` – The component restarts if the dependency changes state.

            Default: ``HARD``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html#cfn-greengrassv2-componentversion-componentdependencyrequirement-dependencytype
            '''
            result = self._values.get("dependency_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version_requirement(self) -> typing.Optional[builtins.str]:
            '''The component version requirement for the component dependency.

            AWS IoT Greengrass uses semantic version constraints. For more information, see `Semantic Versioning <https://docs.aws.amazon.com/https://semver.org/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html#cfn-greengrassv2-componentversion-componentdependencyrequirement-versionrequirement
            '''
            result = self._values.get("version_requirement")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentDependencyRequirementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.ComponentPlatformProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "name": "name"},
    )
    class ComponentPlatformProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about a platform that a component supports.

            :param attributes: A dictionary of attributes for the platform. The AWS IoT Greengrass Core software defines the ``os`` and ``platform`` by default. You can specify additional platform attributes for a core device when you deploy the AWS IoT Greengrass nucleus component. For more information, see the `AWS IoT Greengrass nucleus component <https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .
            :param name: The friendly name of the platform. This name helps you identify the platform. If you omit this parameter, AWS IoT Greengrass creates a friendly name from the ``os`` and ``architecture`` of the platform.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                component_platform_property = greengrassv2.CfnComponentVersion.ComponentPlatformProperty(
                    attributes={
                        "attributes_key": "attributes"
                    },
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__868d55cb9cd63d9081a8bb6f44c49ad0558ce766d47dc9e602b30fa6d7823104)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''A dictionary of attributes for the platform.

            The AWS IoT Greengrass Core software defines the ``os`` and ``platform`` by default. You can specify additional platform attributes for a core device when you deploy the AWS IoT Greengrass nucleus component. For more information, see the `AWS IoT Greengrass nucleus component <https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html#cfn-greengrassv2-componentversion-componentplatform-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The friendly name of the platform. This name helps you identify the platform.

            If you omit this parameter, AWS IoT Greengrass creates a friendly name from the ``os`` and ``architecture`` of the platform.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html#cfn-greengrassv2-componentversion-componentplatform-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentPlatformProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.LambdaContainerParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "devices": "devices",
            "memory_size_in_kb": "memorySizeInKb",
            "mount_ro_sysfs": "mountRoSysfs",
            "volumes": "volumes",
        },
    )
    class LambdaContainerParamsProperty:
        def __init__(
            self,
            *,
            devices: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.LambdaDeviceMountProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            memory_size_in_kb: typing.Optional[jsii.Number] = None,
            mount_ro_sysfs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            volumes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.LambdaVolumeMountProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information about a container in which AWS Lambda functions run on AWS IoT Greengrass core devices.

            :param devices: The list of system devices that the container can access.
            :param memory_size_in_kb: The memory size of the container, expressed in kilobytes. Default: ``16384`` (16 MB)
            :param mount_ro_sysfs: Whether or not the container can read information from the device's ``/sys`` folder. Default: ``false``
            :param volumes: The list of volumes that the container can access.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                lambda_container_params_property = greengrassv2.CfnComponentVersion.LambdaContainerParamsProperty(
                    devices=[greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty(
                        add_group_owner=False,
                        path="path",
                        permission="permission"
                    )],
                    memory_size_in_kb=123,
                    mount_ro_sysfs=False,
                    volumes=[greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty(
                        add_group_owner=False,
                        destination_path="destinationPath",
                        permission="permission",
                        source_path="sourcePath"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__faa404e4c8d222fafce82a4df5f456d4c0ca9f1f90cc0610f63526bc52a42562)
                check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
                check_type(argname="argument memory_size_in_kb", value=memory_size_in_kb, expected_type=type_hints["memory_size_in_kb"])
                check_type(argname="argument mount_ro_sysfs", value=mount_ro_sysfs, expected_type=type_hints["mount_ro_sysfs"])
                check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if devices is not None:
                self._values["devices"] = devices
            if memory_size_in_kb is not None:
                self._values["memory_size_in_kb"] = memory_size_in_kb
            if mount_ro_sysfs is not None:
                self._values["mount_ro_sysfs"] = mount_ro_sysfs
            if volumes is not None:
                self._values["volumes"] = volumes

        @builtins.property
        def devices(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaDeviceMountProperty"]]]]:
            '''The list of system devices that the container can access.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-devices
            '''
            result = self._values.get("devices")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaDeviceMountProperty"]]]], result)

        @builtins.property
        def memory_size_in_kb(self) -> typing.Optional[jsii.Number]:
            '''The memory size of the container, expressed in kilobytes.

            Default: ``16384`` (16 MB)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-memorysizeinkb
            '''
            result = self._values.get("memory_size_in_kb")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_ro_sysfs(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not the container can read information from the device's ``/sys`` folder.

            Default: ``false``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-mountrosysfs
            '''
            result = self._values.get("mount_ro_sysfs")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def volumes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaVolumeMountProperty"]]]]:
            '''The list of volumes that the container can access.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-volumes
            '''
            result = self._values.get("volumes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaVolumeMountProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaContainerParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_group_owner": "addGroupOwner",
            "path": "path",
            "permission": "permission",
        },
    )
    class LambdaDeviceMountProperty:
        def __init__(
            self,
            *,
            add_group_owner: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            path: typing.Optional[builtins.str] = None,
            permission: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about a device that Linux processes in a container can access.

            :param add_group_owner: Whether or not to add the component's system user as an owner of the device. Default: ``false``
            :param path: The mount path for the device in the file system.
            :param permission: The permission to access the device: read/only ( ``ro`` ) or read/write ( ``rw`` ). Default: ``ro``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                lambda_device_mount_property = greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty(
                    add_group_owner=False,
                    path="path",
                    permission="permission"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ff1c88d4c72688121e8d02d23f54e807be84dc41e8cc06f915402a59c07ab80)
                check_type(argname="argument add_group_owner", value=add_group_owner, expected_type=type_hints["add_group_owner"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_group_owner is not None:
                self._values["add_group_owner"] = add_group_owner
            if path is not None:
                self._values["path"] = path
            if permission is not None:
                self._values["permission"] = permission

        @builtins.property
        def add_group_owner(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not to add the component's system user as an owner of the device.

            Default: ``false``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-addgroupowner
            '''
            result = self._values.get("add_group_owner")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The mount path for the device in the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def permission(self) -> typing.Optional[builtins.str]:
            '''The permission to access the device: read/only ( ``ro`` ) or read/write ( ``rw`` ).

            Default: ``ro``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-permission
            '''
            result = self._values.get("permission")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaDeviceMountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.LambdaEventSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"topic": "topic", "type": "type"},
    )
    class LambdaEventSourceProperty:
        def __init__(
            self,
            *,
            topic: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about an event source for an AWS Lambda function.

            The event source defines the topics on which this Lambda function subscribes to receive messages that run the function.

            :param topic: The topic to which to subscribe to receive event messages.
            :param type: The type of event source. Choose from the following options:. - ``PUB_SUB`` – Subscribe to local publish/subscribe messages. This event source type doesn't support MQTT wildcards ( ``+`` and ``#`` ) in the event source topic. - ``IOT_CORE`` – Subscribe to AWS IoT Core MQTT messages. This event source type supports MQTT wildcards ( ``+`` and ``#`` ) in the event source topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                lambda_event_source_property = greengrassv2.CfnComponentVersion.LambdaEventSourceProperty(
                    topic="topic",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2bdb1aa21a11fead4d3211e8427d3370a925fda227540a812604c8717631e5b)
                check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if topic is not None:
                self._values["topic"] = topic
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def topic(self) -> typing.Optional[builtins.str]:
            '''The topic to which to subscribe to receive event messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html#cfn-greengrassv2-componentversion-lambdaeventsource-topic
            '''
            result = self._values.get("topic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of event source. Choose from the following options:.

            - ``PUB_SUB`` – Subscribe to local publish/subscribe messages. This event source type doesn't support MQTT wildcards ( ``+`` and ``#`` ) in the event source topic.
            - ``IOT_CORE`` – Subscribe to AWS IoT Core MQTT messages. This event source type supports MQTT wildcards ( ``+`` and ``#`` ) in the event source topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html#cfn-greengrassv2-componentversion-lambdaeventsource-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaEventSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.LambdaExecutionParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "environment_variables": "environmentVariables",
            "event_sources": "eventSources",
            "exec_args": "execArgs",
            "input_payload_encoding_type": "inputPayloadEncodingType",
            "linux_process_params": "linuxProcessParams",
            "max_idle_time_in_seconds": "maxIdleTimeInSeconds",
            "max_instances_count": "maxInstancesCount",
            "max_queue_size": "maxQueueSize",
            "pinned": "pinned",
            "status_timeout_in_seconds": "statusTimeoutInSeconds",
            "timeout_in_seconds": "timeoutInSeconds",
        },
    )
    class LambdaExecutionParametersProperty:
        def __init__(
            self,
            *,
            environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            event_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.LambdaEventSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            exec_args: typing.Optional[typing.Sequence[builtins.str]] = None,
            input_payload_encoding_type: typing.Optional[builtins.str] = None,
            linux_process_params: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.LambdaLinuxProcessParamsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            max_idle_time_in_seconds: typing.Optional[jsii.Number] = None,
            max_instances_count: typing.Optional[jsii.Number] = None,
            max_queue_size: typing.Optional[jsii.Number] = None,
            pinned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            status_timeout_in_seconds: typing.Optional[jsii.Number] = None,
            timeout_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains parameters for a Lambda function that runs on AWS IoT Greengrass .

            :param environment_variables: The map of environment variables that are available to the Lambda function when it runs.
            :param event_sources: The list of event sources to which to subscribe to receive work messages. The Lambda function runs when it receives a message from an event source. You can subscribe this function to local publish/subscribe messages and AWS IoT Core MQTT messages.
            :param exec_args: The list of arguments to pass to the Lambda function when it runs.
            :param input_payload_encoding_type: The encoding type that the Lambda function supports. Default: ``json``
            :param linux_process_params: The parameters for the Linux process that contains the Lambda function.
            :param max_idle_time_in_seconds: The maximum amount of time in seconds that a non-pinned Lambda function can idle before the AWS IoT Greengrass Core software stops its process.
            :param max_instances_count: The maximum number of instances that a non-pinned Lambda function can run at the same time.
            :param max_queue_size: The maximum size of the message queue for the Lambda function component. The AWS IoT Greengrass core device stores messages in a FIFO (first-in-first-out) queue until it can run the Lambda function to consume each message.
            :param pinned: Whether or not the Lambda function is pinned, or long-lived. - A pinned Lambda function starts when the AWS IoT Greengrass Core starts and keeps running in its own container. - A non-pinned Lambda function starts only when it receives a work item and exists after it idles for ``maxIdleTimeInSeconds`` . If the function has multiple work items, the AWS IoT Greengrass Core software creates multiple instances of the function. Default: ``true``
            :param status_timeout_in_seconds: The interval in seconds at which a pinned (also known as long-lived) Lambda function component sends status updates to the Lambda manager component.
            :param timeout_in_seconds: The maximum amount of time in seconds that the Lambda function can process a work item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                lambda_execution_parameters_property = greengrassv2.CfnComponentVersion.LambdaExecutionParametersProperty(
                    environment_variables={
                        "environment_variables_key": "environmentVariables"
                    },
                    event_sources=[greengrassv2.CfnComponentVersion.LambdaEventSourceProperty(
                        topic="topic",
                        type="type"
                    )],
                    exec_args=["execArgs"],
                    input_payload_encoding_type="inputPayloadEncodingType",
                    linux_process_params=greengrassv2.CfnComponentVersion.LambdaLinuxProcessParamsProperty(
                        container_params=greengrassv2.CfnComponentVersion.LambdaContainerParamsProperty(
                            devices=[greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty(
                                add_group_owner=False,
                                path="path",
                                permission="permission"
                            )],
                            memory_size_in_kb=123,
                            mount_ro_sysfs=False,
                            volumes=[greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty(
                                add_group_owner=False,
                                destination_path="destinationPath",
                                permission="permission",
                                source_path="sourcePath"
                            )]
                        ),
                        isolation_mode="isolationMode"
                    ),
                    max_idle_time_in_seconds=123,
                    max_instances_count=123,
                    max_queue_size=123,
                    pinned=False,
                    status_timeout_in_seconds=123,
                    timeout_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__000b16ea913d1bbaf1c4a8d0fc0503b8b2497e7799ae2cf1cbbf4d109ec5d229)
                check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
                check_type(argname="argument event_sources", value=event_sources, expected_type=type_hints["event_sources"])
                check_type(argname="argument exec_args", value=exec_args, expected_type=type_hints["exec_args"])
                check_type(argname="argument input_payload_encoding_type", value=input_payload_encoding_type, expected_type=type_hints["input_payload_encoding_type"])
                check_type(argname="argument linux_process_params", value=linux_process_params, expected_type=type_hints["linux_process_params"])
                check_type(argname="argument max_idle_time_in_seconds", value=max_idle_time_in_seconds, expected_type=type_hints["max_idle_time_in_seconds"])
                check_type(argname="argument max_instances_count", value=max_instances_count, expected_type=type_hints["max_instances_count"])
                check_type(argname="argument max_queue_size", value=max_queue_size, expected_type=type_hints["max_queue_size"])
                check_type(argname="argument pinned", value=pinned, expected_type=type_hints["pinned"])
                check_type(argname="argument status_timeout_in_seconds", value=status_timeout_in_seconds, expected_type=type_hints["status_timeout_in_seconds"])
                check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if environment_variables is not None:
                self._values["environment_variables"] = environment_variables
            if event_sources is not None:
                self._values["event_sources"] = event_sources
            if exec_args is not None:
                self._values["exec_args"] = exec_args
            if input_payload_encoding_type is not None:
                self._values["input_payload_encoding_type"] = input_payload_encoding_type
            if linux_process_params is not None:
                self._values["linux_process_params"] = linux_process_params
            if max_idle_time_in_seconds is not None:
                self._values["max_idle_time_in_seconds"] = max_idle_time_in_seconds
            if max_instances_count is not None:
                self._values["max_instances_count"] = max_instances_count
            if max_queue_size is not None:
                self._values["max_queue_size"] = max_queue_size
            if pinned is not None:
                self._values["pinned"] = pinned
            if status_timeout_in_seconds is not None:
                self._values["status_timeout_in_seconds"] = status_timeout_in_seconds
            if timeout_in_seconds is not None:
                self._values["timeout_in_seconds"] = timeout_in_seconds

        @builtins.property
        def environment_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The map of environment variables that are available to the Lambda function when it runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-environmentvariables
            '''
            result = self._values.get("environment_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def event_sources(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaEventSourceProperty"]]]]:
            '''The list of event sources to which to subscribe to receive work messages.

            The Lambda function runs when it receives a message from an event source. You can subscribe this function to local publish/subscribe messages and AWS IoT Core MQTT messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-eventsources
            '''
            result = self._values.get("event_sources")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaEventSourceProperty"]]]], result)

        @builtins.property
        def exec_args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of arguments to pass to the Lambda function when it runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-execargs
            '''
            result = self._values.get("exec_args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def input_payload_encoding_type(self) -> typing.Optional[builtins.str]:
            '''The encoding type that the Lambda function supports.

            Default: ``json``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-inputpayloadencodingtype
            '''
            result = self._values.get("input_payload_encoding_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def linux_process_params(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaLinuxProcessParamsProperty"]]:
            '''The parameters for the Linux process that contains the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-linuxprocessparams
            '''
            result = self._values.get("linux_process_params")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaLinuxProcessParamsProperty"]], result)

        @builtins.property
        def max_idle_time_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time in seconds that a non-pinned Lambda function can idle before the AWS IoT Greengrass Core software stops its process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxidletimeinseconds
            '''
            result = self._values.get("max_idle_time_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_instances_count(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of instances that a non-pinned Lambda function can run at the same time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxinstancescount
            '''
            result = self._values.get("max_instances_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_queue_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum size of the message queue for the Lambda function component.

            The AWS IoT Greengrass core device stores messages in a FIFO (first-in-first-out) queue until it can run the Lambda function to consume each message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxqueuesize
            '''
            result = self._values.get("max_queue_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pinned(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not the Lambda function is pinned, or long-lived.

            - A pinned Lambda function starts when the AWS IoT Greengrass Core starts and keeps running in its own container.
            - A non-pinned Lambda function starts only when it receives a work item and exists after it idles for ``maxIdleTimeInSeconds`` . If the function has multiple work items, the AWS IoT Greengrass Core software creates multiple instances of the function.

            Default: ``true``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-pinned
            '''
            result = self._values.get("pinned")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def status_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The interval in seconds at which a pinned (also known as long-lived) Lambda function component sends status updates to the Lambda manager component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-statustimeoutinseconds
            '''
            result = self._values.get("status_timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time in seconds that the Lambda function can process a work item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaExecutionParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.LambdaFunctionRecipeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_dependencies": "componentDependencies",
            "component_lambda_parameters": "componentLambdaParameters",
            "component_name": "componentName",
            "component_platforms": "componentPlatforms",
            "component_version": "componentVersion",
            "lambda_arn": "lambdaArn",
        },
    )
    class LambdaFunctionRecipeSourceProperty:
        def __init__(
            self,
            *,
            component_dependencies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.ComponentDependencyRequirementProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            component_lambda_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.LambdaExecutionParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            component_name: typing.Optional[builtins.str] = None,
            component_platforms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.ComponentPlatformProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            component_version: typing.Optional[builtins.str] = None,
            lambda_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about an AWS Lambda function to import to create a component.

            :param component_dependencies: The component versions on which this Lambda function component depends.
            :param component_lambda_parameters: The system and runtime parameters for the Lambda function as it runs on the AWS IoT Greengrass core device.
            :param component_name: The name of the component. Defaults to the name of the Lambda function.
            :param component_platforms: The platforms that the component version supports.
            :param component_version: The version of the component. Defaults to the version of the Lambda function as a semantic version. For example, if your function version is ``3`` , the component version becomes ``3.0.0`` .
            :param lambda_arn: The ARN of the Lambda function. The ARN must include the version of the function to import. You can't use version aliases like ``$LATEST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                lambda_function_recipe_source_property = greengrassv2.CfnComponentVersion.LambdaFunctionRecipeSourceProperty(
                    component_dependencies={
                        "component_dependencies_key": greengrassv2.CfnComponentVersion.ComponentDependencyRequirementProperty(
                            dependency_type="dependencyType",
                            version_requirement="versionRequirement"
                        )
                    },
                    component_lambda_parameters=greengrassv2.CfnComponentVersion.LambdaExecutionParametersProperty(
                        environment_variables={
                            "environment_variables_key": "environmentVariables"
                        },
                        event_sources=[greengrassv2.CfnComponentVersion.LambdaEventSourceProperty(
                            topic="topic",
                            type="type"
                        )],
                        exec_args=["execArgs"],
                        input_payload_encoding_type="inputPayloadEncodingType",
                        linux_process_params=greengrassv2.CfnComponentVersion.LambdaLinuxProcessParamsProperty(
                            container_params=greengrassv2.CfnComponentVersion.LambdaContainerParamsProperty(
                                devices=[greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty(
                                    add_group_owner=False,
                                    path="path",
                                    permission="permission"
                                )],
                                memory_size_in_kb=123,
                                mount_ro_sysfs=False,
                                volumes=[greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty(
                                    add_group_owner=False,
                                    destination_path="destinationPath",
                                    permission="permission",
                                    source_path="sourcePath"
                                )]
                            ),
                            isolation_mode="isolationMode"
                        ),
                        max_idle_time_in_seconds=123,
                        max_instances_count=123,
                        max_queue_size=123,
                        pinned=False,
                        status_timeout_in_seconds=123,
                        timeout_in_seconds=123
                    ),
                    component_name="componentName",
                    component_platforms=[greengrassv2.CfnComponentVersion.ComponentPlatformProperty(
                        attributes={
                            "attributes_key": "attributes"
                        },
                        name="name"
                    )],
                    component_version="componentVersion",
                    lambda_arn="lambdaArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c65d39b535672032cfb004ee7b6c48a4d582a473117af5905209bcaa7d8a97c)
                check_type(argname="argument component_dependencies", value=component_dependencies, expected_type=type_hints["component_dependencies"])
                check_type(argname="argument component_lambda_parameters", value=component_lambda_parameters, expected_type=type_hints["component_lambda_parameters"])
                check_type(argname="argument component_name", value=component_name, expected_type=type_hints["component_name"])
                check_type(argname="argument component_platforms", value=component_platforms, expected_type=type_hints["component_platforms"])
                check_type(argname="argument component_version", value=component_version, expected_type=type_hints["component_version"])
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_dependencies is not None:
                self._values["component_dependencies"] = component_dependencies
            if component_lambda_parameters is not None:
                self._values["component_lambda_parameters"] = component_lambda_parameters
            if component_name is not None:
                self._values["component_name"] = component_name
            if component_platforms is not None:
                self._values["component_platforms"] = component_platforms
            if component_version is not None:
                self._values["component_version"] = component_version
            if lambda_arn is not None:
                self._values["lambda_arn"] = lambda_arn

        @builtins.property
        def component_dependencies(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.ComponentDependencyRequirementProperty"]]]]:
            '''The component versions on which this Lambda function component depends.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentdependencies
            '''
            result = self._values.get("component_dependencies")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.ComponentDependencyRequirementProperty"]]]], result)

        @builtins.property
        def component_lambda_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaExecutionParametersProperty"]]:
            '''The system and runtime parameters for the Lambda function as it runs on the AWS IoT Greengrass core device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentlambdaparameters
            '''
            result = self._values.get("component_lambda_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaExecutionParametersProperty"]], result)

        @builtins.property
        def component_name(self) -> typing.Optional[builtins.str]:
            '''The name of the component.

            Defaults to the name of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentname
            '''
            result = self._values.get("component_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def component_platforms(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.ComponentPlatformProperty"]]]]:
            '''The platforms that the component version supports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentplatforms
            '''
            result = self._values.get("component_platforms")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.ComponentPlatformProperty"]]]], result)

        @builtins.property
        def component_version(self) -> typing.Optional[builtins.str]:
            '''The version of the component.

            Defaults to the version of the Lambda function as a semantic version. For example, if your function version is ``3`` , the component version becomes ``3.0.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentversion
            '''
            result = self._values.get("component_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lambda_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Lambda function.

            The ARN must include the version of the function to import. You can't use version aliases like ``$LATEST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaFunctionRecipeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.LambdaLinuxProcessParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_params": "containerParams",
            "isolation_mode": "isolationMode",
        },
    )
    class LambdaLinuxProcessParamsProperty:
        def __init__(
            self,
            *,
            container_params: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComponentVersion.LambdaContainerParamsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            isolation_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains parameters for a Linux process that contains an AWS Lambda function.

            :param container_params: The parameters for the container in which the Lambda function runs.
            :param isolation_mode: The isolation mode for the process that contains the Lambda function. The process can run in an isolated runtime environment inside the AWS IoT Greengrass container, or as a regular process outside any container. Default: ``GreengrassContainer``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                lambda_linux_process_params_property = greengrassv2.CfnComponentVersion.LambdaLinuxProcessParamsProperty(
                    container_params=greengrassv2.CfnComponentVersion.LambdaContainerParamsProperty(
                        devices=[greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty(
                            add_group_owner=False,
                            path="path",
                            permission="permission"
                        )],
                        memory_size_in_kb=123,
                        mount_ro_sysfs=False,
                        volumes=[greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty(
                            add_group_owner=False,
                            destination_path="destinationPath",
                            permission="permission",
                            source_path="sourcePath"
                        )]
                    ),
                    isolation_mode="isolationMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__756fcd867eac20b9fe5f8b006e060eeede11829ac7bf7e6785ed2fe382e6e614)
                check_type(argname="argument container_params", value=container_params, expected_type=type_hints["container_params"])
                check_type(argname="argument isolation_mode", value=isolation_mode, expected_type=type_hints["isolation_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_params is not None:
                self._values["container_params"] = container_params
            if isolation_mode is not None:
                self._values["isolation_mode"] = isolation_mode

        @builtins.property
        def container_params(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaContainerParamsProperty"]]:
            '''The parameters for the container in which the Lambda function runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html#cfn-greengrassv2-componentversion-lambdalinuxprocessparams-containerparams
            '''
            result = self._values.get("container_params")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComponentVersion.LambdaContainerParamsProperty"]], result)

        @builtins.property
        def isolation_mode(self) -> typing.Optional[builtins.str]:
            '''The isolation mode for the process that contains the Lambda function.

            The process can run in an isolated runtime environment inside the AWS IoT Greengrass container, or as a regular process outside any container.

            Default: ``GreengrassContainer``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html#cfn-greengrassv2-componentversion-lambdalinuxprocessparams-isolationmode
            '''
            result = self._values.get("isolation_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaLinuxProcessParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_group_owner": "addGroupOwner",
            "destination_path": "destinationPath",
            "permission": "permission",
            "source_path": "sourcePath",
        },
    )
    class LambdaVolumeMountProperty:
        def __init__(
            self,
            *,
            add_group_owner: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            destination_path: typing.Optional[builtins.str] = None,
            permission: typing.Optional[builtins.str] = None,
            source_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about a volume that Linux processes in a container can access.

            When you define a volume, the AWS IoT Greengrass Core software mounts the source files to the destination inside the container.

            :param add_group_owner: Whether or not to add the AWS IoT Greengrass user group as an owner of the volume. Default: ``false``
            :param destination_path: The path to the logical volume in the file system.
            :param permission: The permission to access the volume: read/only ( ``ro`` ) or read/write ( ``rw`` ). Default: ``ro``
            :param source_path: The path to the physical volume in the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                lambda_volume_mount_property = greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty(
                    add_group_owner=False,
                    destination_path="destinationPath",
                    permission="permission",
                    source_path="sourcePath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2bbd7759f413868e7d380d01e235f94a2424b3a59ed198c9bb3e2b55af65a835)
                check_type(argname="argument add_group_owner", value=add_group_owner, expected_type=type_hints["add_group_owner"])
                check_type(argname="argument destination_path", value=destination_path, expected_type=type_hints["destination_path"])
                check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_group_owner is not None:
                self._values["add_group_owner"] = add_group_owner
            if destination_path is not None:
                self._values["destination_path"] = destination_path
            if permission is not None:
                self._values["permission"] = permission
            if source_path is not None:
                self._values["source_path"] = source_path

        @builtins.property
        def add_group_owner(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not to add the AWS IoT Greengrass user group as an owner of the volume.

            Default: ``false``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-addgroupowner
            '''
            result = self._values.get("add_group_owner")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def destination_path(self) -> typing.Optional[builtins.str]:
            '''The path to the logical volume in the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-destinationpath
            '''
            result = self._values.get("destination_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def permission(self) -> typing.Optional[builtins.str]:
            '''The permission to access the volume: read/only ( ``ro`` ) or read/write ( ``rw`` ).

            Default: ``ro``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-permission
            '''
            result = self._values.get("permission")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_path(self) -> typing.Optional[builtins.str]:
            '''The path to the physical volume in the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-sourcepath
            '''
            result = self._values.get("source_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaVolumeMountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrassv2.CfnComponentVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "inline_recipe": "inlineRecipe",
        "lambda_function": "lambdaFunction",
        "tags": "tags",
    },
)
class CfnComponentVersionProps:
    def __init__(
        self,
        *,
        inline_recipe: typing.Optional[builtins.str] = None,
        lambda_function: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaFunctionRecipeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnComponentVersion``.

        :param inline_recipe: The recipe to use to create the component. The recipe defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform compatibility. You must specify either ``InlineRecipe`` or ``LambdaFunction`` .
        :param lambda_function: The parameters to create a component from a Lambda function. You must specify either ``InlineRecipe`` or ``LambdaFunction`` .
        :param tags: Application-specific metadata to attach to the component version. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tag your AWS IoT Greengrass Version 2 resources <https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrassv2 as greengrassv2
            
            cfn_component_version_props = greengrassv2.CfnComponentVersionProps(
                inline_recipe="inlineRecipe",
                lambda_function=greengrassv2.CfnComponentVersion.LambdaFunctionRecipeSourceProperty(
                    component_dependencies={
                        "component_dependencies_key": greengrassv2.CfnComponentVersion.ComponentDependencyRequirementProperty(
                            dependency_type="dependencyType",
                            version_requirement="versionRequirement"
                        )
                    },
                    component_lambda_parameters=greengrassv2.CfnComponentVersion.LambdaExecutionParametersProperty(
                        environment_variables={
                            "environment_variables_key": "environmentVariables"
                        },
                        event_sources=[greengrassv2.CfnComponentVersion.LambdaEventSourceProperty(
                            topic="topic",
                            type="type"
                        )],
                        exec_args=["execArgs"],
                        input_payload_encoding_type="inputPayloadEncodingType",
                        linux_process_params=greengrassv2.CfnComponentVersion.LambdaLinuxProcessParamsProperty(
                            container_params=greengrassv2.CfnComponentVersion.LambdaContainerParamsProperty(
                                devices=[greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty(
                                    add_group_owner=False,
                                    path="path",
                                    permission="permission"
                                )],
                                memory_size_in_kb=123,
                                mount_ro_sysfs=False,
                                volumes=[greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty(
                                    add_group_owner=False,
                                    destination_path="destinationPath",
                                    permission="permission",
                                    source_path="sourcePath"
                                )]
                            ),
                            isolation_mode="isolationMode"
                        ),
                        max_idle_time_in_seconds=123,
                        max_instances_count=123,
                        max_queue_size=123,
                        pinned=False,
                        status_timeout_in_seconds=123,
                        timeout_in_seconds=123
                    ),
                    component_name="componentName",
                    component_platforms=[greengrassv2.CfnComponentVersion.ComponentPlatformProperty(
                        attributes={
                            "attributes_key": "attributes"
                        },
                        name="name"
                    )],
                    component_version="componentVersion",
                    lambda_arn="lambdaArn"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26145a7c787773c5d69bceaa1a73ff40d6d4fa0dcdb0fa8cda22627f2fbac7e4)
            check_type(argname="argument inline_recipe", value=inline_recipe, expected_type=type_hints["inline_recipe"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if inline_recipe is not None:
            self._values["inline_recipe"] = inline_recipe
        if lambda_function is not None:
            self._values["lambda_function"] = lambda_function
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def inline_recipe(self) -> typing.Optional[builtins.str]:
        '''The recipe to use to create the component.

        The recipe defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform compatibility.

        You must specify either ``InlineRecipe`` or ``LambdaFunction`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-inlinerecipe
        '''
        result = self._values.get("inline_recipe")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_function(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComponentVersion.LambdaFunctionRecipeSourceProperty]]:
        '''The parameters to create a component from a Lambda function.

        You must specify either ``InlineRecipe`` or ``LambdaFunction`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-lambdafunction
        '''
        result = self._values.get("lambda_function")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComponentVersion.LambdaFunctionRecipeSourceProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Application-specific metadata to attach to the component version.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tag your AWS IoT Greengrass Version 2 resources <https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComponentVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDeployment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment",
):
    '''Creates a continuous deployment for a target, which is a AWS IoT Greengrass core device or group of core devices.

    When you add a new core device to a group of core devices that has a deployment, AWS IoT Greengrass deploys that group's deployment to the new device.

    You can define one deployment for each target. When you create a new deployment for a target that has an existing deployment, you replace the previous deployment. AWS IoT Greengrass applies the new deployment to the target devices.

    You can only add, update, or delete up to 10 deployments at a time to a single target.

    Every deployment has a revision number that indicates how many deployment revisions you define for a target. Use this operation to create a new revision of an existing deployment. This operation returns the revision number of the new deployment when you create it.

    For more information, see the `Create deployments <https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .
    .. epigraph::

       Deployment resources are deleted when you delete stacks. To keep the deployments in a stack, you must specify ``"DeletionPolicy": "Retain"`` on each deployment resource in the stack template that you want to keep. For more information, see `DeletionPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html>`_ .

       You can only delete up to 10 deployment resources at a time. If you delete more than 10 resources, you receive an error.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html
    :cloudformationResource: AWS::GreengrassV2::Deployment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrassv2 as greengrassv2
        
        # rate_increase_criteria: Any
        
        cfn_deployment = greengrassv2.CfnDeployment(self, "MyCfnDeployment",
            target_arn="targetArn",
        
            # the properties below are optional
            components={
                "components_key": greengrassv2.CfnDeployment.ComponentDeploymentSpecificationProperty(
                    component_version="componentVersion",
                    configuration_update=greengrassv2.CfnDeployment.ComponentConfigurationUpdateProperty(
                        merge="merge",
                        reset=["reset"]
                    ),
                    run_with=greengrassv2.CfnDeployment.ComponentRunWithProperty(
                        posix_user="posixUser",
                        system_resource_limits=greengrassv2.CfnDeployment.SystemResourceLimitsProperty(
                            cpus=123,
                            memory=123
                        ),
                        windows_user="windowsUser"
                    )
                )
            },
            deployment_name="deploymentName",
            deployment_policies=greengrassv2.CfnDeployment.DeploymentPoliciesProperty(
                component_update_policy=greengrassv2.CfnDeployment.DeploymentComponentUpdatePolicyProperty(
                    action="action",
                    timeout_in_seconds=123
                ),
                configuration_validation_policy=greengrassv2.CfnDeployment.DeploymentConfigurationValidationPolicyProperty(
                    timeout_in_seconds=123
                ),
                failure_handling_policy="failureHandlingPolicy"
            ),
            iot_job_configuration=greengrassv2.CfnDeployment.DeploymentIoTJobConfigurationProperty(
                abort_config=greengrassv2.CfnDeployment.IoTJobAbortConfigProperty(
                    criteria_list=[greengrassv2.CfnDeployment.IoTJobAbortCriteriaProperty(
                        action="action",
                        failure_type="failureType",
                        min_number_of_executed_things=123,
                        threshold_percentage=123
                    )]
                ),
                job_executions_rollout_config=greengrassv2.CfnDeployment.IoTJobExecutionsRolloutConfigProperty(
                    exponential_rate=greengrassv2.CfnDeployment.IoTJobExponentialRolloutRateProperty(
                        base_rate_per_minute=123,
                        increment_factor=123,
                        rate_increase_criteria=rate_increase_criteria
                    ),
                    maximum_per_minute=123
                ),
                timeout_config=greengrassv2.CfnDeployment.IoTJobTimeoutConfigProperty(
                    in_progress_timeout_in_minutes=123
                )
            ),
            parent_target_arn="parentTargetArn",
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
        target_arn: builtins.str,
        components: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.ComponentDeploymentSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        deployment_name: typing.Optional[builtins.str] = None,
        deployment_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.DeploymentPoliciesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        iot_job_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.DeploymentIoTJobConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        parent_target_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param target_arn: The ARN of the target AWS IoT thing or thing group.
        :param components: The components to deploy. This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component.
        :param deployment_name: The name of the deployment.
        :param deployment_policies: The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.
        :param iot_job_configuration: The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.
        :param parent_target_arn: The parent deployment's `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ for a subdeployment.
        :param tags: Application-specific metadata to attach to the deployment. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tag your AWS IoT Greengrass Version 2 resources <https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0099ed4b9647f1e31fee9e80f3453ed07e5b916846f269d15cb7aa59c5b0f80)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentProps(
            target_arn=target_arn,
            components=components,
            deployment_name=deployment_name,
            deployment_policies=deployment_policies,
            iot_job_configuration=iot_job_configuration,
            parent_target_arn=parent_target_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524ad5f78c9f968fbfe224a67e6b8648f6b2153ad09d18d40f9d97b0df1c6779)
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
            type_hints = typing.get_type_hints(_typecheckingstub__27081f49a96fd9b6be8c82348527e349696fb1b86cd8968bf684a0fc6ea3c51d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDeploymentId")
    def attr_deployment_id(self) -> builtins.str:
        '''The ID of the deployment.

        :cloudformationAttribute: DeploymentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeploymentId"))

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
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''The ARN of the target AWS IoT thing or thing group.'''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9aca642a78f9815025a310924e8d40466c2d36e58d9487bf411cd9087d6199)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="components")
    def components(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnDeployment.ComponentDeploymentSpecificationProperty"]]]]:
        '''The components to deploy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnDeployment.ComponentDeploymentSpecificationProperty"]]]], jsii.get(self, "components"))

    @components.setter
    def components(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnDeployment.ComponentDeploymentSpecificationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1eb46eb9aeb60a7ab5ad1127528e8840b937def6fe38be8c8a850d599c3f07d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentName")
    def deployment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the deployment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentName"))

    @deployment_name.setter
    def deployment_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8069055a5f48e98559e413f59fb8f8c7f772787bd94ff1febc911991c38db58e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentName", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentPolicies")
    def deployment_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentPoliciesProperty"]]:
        '''The deployment policies for the deployment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentPoliciesProperty"]], jsii.get(self, "deploymentPolicies"))

    @deployment_policies.setter
    def deployment_policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentPoliciesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bef596cb6c3ad06c55fcfb702aa42ec9c1d3b9107e9691ab1154ce9d7b05ae46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="iotJobConfiguration")
    def iot_job_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentIoTJobConfigurationProperty"]]:
        '''The job configuration for the deployment configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentIoTJobConfigurationProperty"]], jsii.get(self, "iotJobConfiguration"))

    @iot_job_configuration.setter
    def iot_job_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentIoTJobConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__879253a12cc1ff77fae7f0478b8930b3954ee32057720a99435120f7439281a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iotJobConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="parentTargetArn")
    def parent_target_arn(self) -> typing.Optional[builtins.str]:
        '''The parent deployment's `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ for a subdeployment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentTargetArn"))

    @parent_target_arn.setter
    def parent_target_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4d5673bcfb7eecac8ede7a8e39c18587c0eb66717f03e340c019ebd933adf91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentTargetArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Application-specific metadata to attach to the deployment.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e79f5864d30fae319b83ae457690221fe12d396b95ce2c98c3d893526c3c60d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.ComponentConfigurationUpdateProperty",
        jsii_struct_bases=[],
        name_mapping={"merge": "merge", "reset": "reset"},
    )
    class ComponentConfigurationUpdateProperty:
        def __init__(
            self,
            *,
            merge: typing.Optional[builtins.str] = None,
            reset: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Contains information about a deployment's update to a component's configuration on AWS IoT Greengrass core devices.

            For more information, see `Update component configurations <https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :param merge: A serialized JSON string that contains the configuration object to merge to target devices. The core device merges this configuration with the component's existing configuration. If this is the first time a component deploys on a device, the core device merges this configuration with the component's default configuration. This means that the core device keeps it's existing configuration for keys and values that you don't specify in this object. For more information, see `Merge configuration updates <https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#merge-configuration-update>`_ in the *AWS IoT Greengrass V2 Developer Guide* .
            :param reset: The list of configuration nodes to reset to default values on target devices. Use JSON pointers to specify each node to reset. JSON pointers start with a forward slash ( ``/`` ) and use forward slashes to separate the key for each level in the object. For more information, see the `JSON pointer specification <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc6901>`_ and `Reset configuration updates <https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#reset-configuration-update>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentconfigurationupdate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                component_configuration_update_property = greengrassv2.CfnDeployment.ComponentConfigurationUpdateProperty(
                    merge="merge",
                    reset=["reset"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__387f0b8380336ac206b9c77595b26aa518c606b2c12077c051460b728e9efb34)
                check_type(argname="argument merge", value=merge, expected_type=type_hints["merge"])
                check_type(argname="argument reset", value=reset, expected_type=type_hints["reset"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if merge is not None:
                self._values["merge"] = merge
            if reset is not None:
                self._values["reset"] = reset

        @builtins.property
        def merge(self) -> typing.Optional[builtins.str]:
            '''A serialized JSON string that contains the configuration object to merge to target devices.

            The core device merges this configuration with the component's existing configuration. If this is the first time a component deploys on a device, the core device merges this configuration with the component's default configuration. This means that the core device keeps it's existing configuration for keys and values that you don't specify in this object. For more information, see `Merge configuration updates <https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#merge-configuration-update>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentconfigurationupdate.html#cfn-greengrassv2-deployment-componentconfigurationupdate-merge
            '''
            result = self._values.get("merge")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reset(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of configuration nodes to reset to default values on target devices.

            Use JSON pointers to specify each node to reset. JSON pointers start with a forward slash ( ``/`` ) and use forward slashes to separate the key for each level in the object. For more information, see the `JSON pointer specification <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc6901>`_ and `Reset configuration updates <https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#reset-configuration-update>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentconfigurationupdate.html#cfn-greengrassv2-deployment-componentconfigurationupdate-reset
            '''
            result = self._values.get("reset")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationUpdateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.ComponentDeploymentSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_version": "componentVersion",
            "configuration_update": "configurationUpdate",
            "run_with": "runWith",
        },
    )
    class ComponentDeploymentSpecificationProperty:
        def __init__(
            self,
            *,
            component_version: typing.Optional[builtins.str] = None,
            configuration_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.ComponentConfigurationUpdateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            run_with: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.ComponentRunWithProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about a component to deploy.

            :param component_version: The version of the component.
            :param configuration_update: The configuration updates to deploy for the component. You can define reset updates and merge updates. A reset updates the keys that you specify to the default configuration for the component. A merge updates the core device's component configuration with the keys and values that you specify. The AWS IoT Greengrass Core software applies reset updates before it applies merge updates. For more information, see `Update component configuration <https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html>`_ .
            :param run_with: The system user and group that the software uses to run component processes on the core device. If you omit this parameter, the software uses the system user and group that you configure for the core device. For more information, see `Configure the user and group that run components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentdeploymentspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                component_deployment_specification_property = greengrassv2.CfnDeployment.ComponentDeploymentSpecificationProperty(
                    component_version="componentVersion",
                    configuration_update=greengrassv2.CfnDeployment.ComponentConfigurationUpdateProperty(
                        merge="merge",
                        reset=["reset"]
                    ),
                    run_with=greengrassv2.CfnDeployment.ComponentRunWithProperty(
                        posix_user="posixUser",
                        system_resource_limits=greengrassv2.CfnDeployment.SystemResourceLimitsProperty(
                            cpus=123,
                            memory=123
                        ),
                        windows_user="windowsUser"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e2fd4248871e67a3e8bbacfa9fd79ab295c1c5403da8ad0bb4d304b1e8aa29a8)
                check_type(argname="argument component_version", value=component_version, expected_type=type_hints["component_version"])
                check_type(argname="argument configuration_update", value=configuration_update, expected_type=type_hints["configuration_update"])
                check_type(argname="argument run_with", value=run_with, expected_type=type_hints["run_with"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_version is not None:
                self._values["component_version"] = component_version
            if configuration_update is not None:
                self._values["configuration_update"] = configuration_update
            if run_with is not None:
                self._values["run_with"] = run_with

        @builtins.property
        def component_version(self) -> typing.Optional[builtins.str]:
            '''The version of the component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentdeploymentspecification.html#cfn-greengrassv2-deployment-componentdeploymentspecification-componentversion
            '''
            result = self._values.get("component_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configuration_update(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.ComponentConfigurationUpdateProperty"]]:
            '''The configuration updates to deploy for the component.

            You can define reset updates and merge updates. A reset updates the keys that you specify to the default configuration for the component. A merge updates the core device's component configuration with the keys and values that you specify. The AWS IoT Greengrass Core software applies reset updates before it applies merge updates. For more information, see `Update component configuration <https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentdeploymentspecification.html#cfn-greengrassv2-deployment-componentdeploymentspecification-configurationupdate
            '''
            result = self._values.get("configuration_update")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.ComponentConfigurationUpdateProperty"]], result)

        @builtins.property
        def run_with(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.ComponentRunWithProperty"]]:
            '''The system user and group that the  software uses to run component processes on the core device.

            If you omit this parameter, the  software uses the system user and group that you configure for the core device. For more information, see `Configure the user and group that run components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentdeploymentspecification.html#cfn-greengrassv2-deployment-componentdeploymentspecification-runwith
            '''
            result = self._values.get("run_with")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.ComponentRunWithProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentDeploymentSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.ComponentRunWithProperty",
        jsii_struct_bases=[],
        name_mapping={
            "posix_user": "posixUser",
            "system_resource_limits": "systemResourceLimits",
            "windows_user": "windowsUser",
        },
    )
    class ComponentRunWithProperty:
        def __init__(
            self,
            *,
            posix_user: typing.Optional[builtins.str] = None,
            system_resource_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.SystemResourceLimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            windows_user: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information system user and group that the AWS IoT Greengrass Core software uses to run component processes on the core device.

            For more information, see `Configure the user and group that run components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :param posix_user: The POSIX system user and (optional) group to use to run this component. Specify the user and group separated by a colon ( ``:`` ) in the following format: ``user:group`` . The group is optional. If you don't specify a group, the AWS IoT Greengrass Core software uses the primary user for the group.
            :param system_resource_limits: The system resource limits to apply to this component's process on the core device. AWS IoT Greengrass supports this feature only on Linux core devices. If you omit this parameter, the AWS IoT Greengrass Core software uses the default system resource limits that you configure on the AWS IoT Greengrass nucleus component. For more information, see `Configure system resource limits for components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-system-resource-limits>`_ .
            :param windows_user: The Windows user to use to run this component on Windows core devices. The user must exist on each Windows core device, and its name and password must be in the LocalSystem account's Credentials Manager instance. If you omit this parameter, the AWS IoT Greengrass Core software uses the default Windows user that you configure on the AWS IoT Greengrass nucleus component. For more information, see `Configure the user and group that run components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentrunwith.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                component_run_with_property = greengrassv2.CfnDeployment.ComponentRunWithProperty(
                    posix_user="posixUser",
                    system_resource_limits=greengrassv2.CfnDeployment.SystemResourceLimitsProperty(
                        cpus=123,
                        memory=123
                    ),
                    windows_user="windowsUser"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b36ba95075fd81f7a1b0019f2c8e10a617095cd1d4c5cb46b3b30152cd4cc951)
                check_type(argname="argument posix_user", value=posix_user, expected_type=type_hints["posix_user"])
                check_type(argname="argument system_resource_limits", value=system_resource_limits, expected_type=type_hints["system_resource_limits"])
                check_type(argname="argument windows_user", value=windows_user, expected_type=type_hints["windows_user"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if posix_user is not None:
                self._values["posix_user"] = posix_user
            if system_resource_limits is not None:
                self._values["system_resource_limits"] = system_resource_limits
            if windows_user is not None:
                self._values["windows_user"] = windows_user

        @builtins.property
        def posix_user(self) -> typing.Optional[builtins.str]:
            '''The POSIX system user and (optional) group to use to run this component.

            Specify the user and group separated by a colon ( ``:`` ) in the following format: ``user:group`` . The group is optional. If you don't specify a group, the AWS IoT Greengrass Core software uses the primary user for the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentrunwith.html#cfn-greengrassv2-deployment-componentrunwith-posixuser
            '''
            result = self._values.get("posix_user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def system_resource_limits(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.SystemResourceLimitsProperty"]]:
            '''The system resource limits to apply to this component's process on the core device.

            AWS IoT Greengrass supports this feature only on Linux core devices.

            If you omit this parameter, the AWS IoT Greengrass Core software uses the default system resource limits that you configure on the AWS IoT Greengrass nucleus component. For more information, see `Configure system resource limits for components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-system-resource-limits>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentrunwith.html#cfn-greengrassv2-deployment-componentrunwith-systemresourcelimits
            '''
            result = self._values.get("system_resource_limits")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.SystemResourceLimitsProperty"]], result)

        @builtins.property
        def windows_user(self) -> typing.Optional[builtins.str]:
            '''The Windows user to use to run this component on Windows core devices.

            The user must exist on each Windows core device, and its name and password must be in the LocalSystem account's Credentials Manager instance.

            If you omit this parameter, the AWS IoT Greengrass Core software uses the default Windows user that you configure on the AWS IoT Greengrass nucleus component. For more information, see `Configure the user and group that run components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentrunwith.html#cfn-greengrassv2-deployment-componentrunwith-windowsuser
            '''
            result = self._values.get("windows_user")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentRunWithProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.DeploymentComponentUpdatePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "timeout_in_seconds": "timeoutInSeconds"},
    )
    class DeploymentComponentUpdatePolicyProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            timeout_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about a deployment's policy that defines when components are safe to update.

            Each component on a device can report whether or not it's ready to update. After a component and its dependencies are ready, they can apply the update in the deployment. You can configure whether or not the deployment notifies components of an update and waits for a response. You specify the amount of time each component has to respond to the update notification.

            :param action: Whether or not to notify components and wait for components to become safe to update. Choose from the following options: - ``NOTIFY_COMPONENTS`` – The deployment notifies each component before it stops and updates that component. Components can use the `SubscribeToComponentUpdates <https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetocomponentupdates>`_ IPC operation to receive these notifications. Then, components can respond with the `DeferComponentUpdate <https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-defercomponentupdate>`_ IPC operation. For more information, see the `Create deployments <https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* . - ``SKIP_NOTIFY_COMPONENTS`` – The deployment doesn't notify components or wait for them to be safe to update. Default: ``NOTIFY_COMPONENTS``
            :param timeout_in_seconds: The amount of time in seconds that each component on a device has to report that it's safe to update. If the component waits for longer than this timeout, then the deployment proceeds on the device. Default: ``60``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentcomponentupdatepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                deployment_component_update_policy_property = greengrassv2.CfnDeployment.DeploymentComponentUpdatePolicyProperty(
                    action="action",
                    timeout_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5375829a3f60c816195dbae5f8543c8cc49cbb3fcde08447d27deea63f4c6565)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if timeout_in_seconds is not None:
                self._values["timeout_in_seconds"] = timeout_in_seconds

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''Whether or not to notify components and wait for components to become safe to update.

            Choose from the following options:

            - ``NOTIFY_COMPONENTS`` – The deployment notifies each component before it stops and updates that component. Components can use the `SubscribeToComponentUpdates <https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetocomponentupdates>`_ IPC operation to receive these notifications. Then, components can respond with the `DeferComponentUpdate <https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-defercomponentupdate>`_ IPC operation. For more information, see the `Create deployments <https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .
            - ``SKIP_NOTIFY_COMPONENTS`` – The deployment doesn't notify components or wait for them to be safe to update.

            Default: ``NOTIFY_COMPONENTS``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentcomponentupdatepolicy.html#cfn-greengrassv2-deployment-deploymentcomponentupdatepolicy-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time in seconds that each component on a device has to report that it's safe to update.

            If the component waits for longer than this timeout, then the deployment proceeds on the device.

            Default: ``60``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentcomponentupdatepolicy.html#cfn-greengrassv2-deployment-deploymentcomponentupdatepolicy-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentComponentUpdatePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.DeploymentConfigurationValidationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"timeout_in_seconds": "timeoutInSeconds"},
    )
    class DeploymentConfigurationValidationPolicyProperty:
        def __init__(
            self,
            *,
            timeout_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about how long a component on a core device can validate its configuration updates before it times out.

            Components can use the `SubscribeToValidateConfigurationUpdates <https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetovalidateconfigurationupdates>`_ IPC operation to receive notifications when a deployment specifies a configuration update. Then, components can respond with the `SendConfigurationValidityReport <https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-sendconfigurationvalidityreport>`_ IPC operation. For more information, see the `Create deployments <https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

            :param timeout_in_seconds: The amount of time in seconds that a component can validate its configuration updates. If the validation time exceeds this timeout, then the deployment proceeds for the device. Default: ``30``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                deployment_configuration_validation_policy_property = greengrassv2.CfnDeployment.DeploymentConfigurationValidationPolicyProperty(
                    timeout_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55dea1728923b695ec20c5dee3a959b4cd22fc22ddd90735e6442720f87e24fd)
                check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if timeout_in_seconds is not None:
                self._values["timeout_in_seconds"] = timeout_in_seconds

        @builtins.property
        def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time in seconds that a component can validate its configuration updates.

            If the validation time exceeds this timeout, then the deployment proceeds for the device.

            Default: ``30``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy.html#cfn-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentConfigurationValidationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.DeploymentIoTJobConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "abort_config": "abortConfig",
            "job_executions_rollout_config": "jobExecutionsRolloutConfig",
            "timeout_config": "timeoutConfig",
        },
    )
    class DeploymentIoTJobConfigurationProperty:
        def __init__(
            self,
            *,
            abort_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.IoTJobAbortConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            job_executions_rollout_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.IoTJobExecutionsRolloutConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.IoTJobTimeoutConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about an AWS IoT job configuration.

            :param abort_config: The stop configuration for the job. This configuration defines when and how to stop a job rollout.
            :param job_executions_rollout_config: The rollout configuration for the job. This configuration defines the rate at which the job rolls out to the fleet of target devices.
            :param timeout_config: The timeout configuration for the job. This configuration defines the amount of time each device has to complete the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                # rate_increase_criteria: Any
                
                deployment_io_tJob_configuration_property = greengrassv2.CfnDeployment.DeploymentIoTJobConfigurationProperty(
                    abort_config=greengrassv2.CfnDeployment.IoTJobAbortConfigProperty(
                        criteria_list=[greengrassv2.CfnDeployment.IoTJobAbortCriteriaProperty(
                            action="action",
                            failure_type="failureType",
                            min_number_of_executed_things=123,
                            threshold_percentage=123
                        )]
                    ),
                    job_executions_rollout_config=greengrassv2.CfnDeployment.IoTJobExecutionsRolloutConfigProperty(
                        exponential_rate=greengrassv2.CfnDeployment.IoTJobExponentialRolloutRateProperty(
                            base_rate_per_minute=123,
                            increment_factor=123,
                            rate_increase_criteria=rate_increase_criteria
                        ),
                        maximum_per_minute=123
                    ),
                    timeout_config=greengrassv2.CfnDeployment.IoTJobTimeoutConfigProperty(
                        in_progress_timeout_in_minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__539a1a07fe3406166e26105a9b53bdea60ff75a1286fede7d70c48a6d080c3fd)
                check_type(argname="argument abort_config", value=abort_config, expected_type=type_hints["abort_config"])
                check_type(argname="argument job_executions_rollout_config", value=job_executions_rollout_config, expected_type=type_hints["job_executions_rollout_config"])
                check_type(argname="argument timeout_config", value=timeout_config, expected_type=type_hints["timeout_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if abort_config is not None:
                self._values["abort_config"] = abort_config
            if job_executions_rollout_config is not None:
                self._values["job_executions_rollout_config"] = job_executions_rollout_config
            if timeout_config is not None:
                self._values["timeout_config"] = timeout_config

        @builtins.property
        def abort_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobAbortConfigProperty"]]:
            '''The stop configuration for the job.

            This configuration defines when and how to stop a job rollout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-abortconfig
            '''
            result = self._values.get("abort_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobAbortConfigProperty"]], result)

        @builtins.property
        def job_executions_rollout_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobExecutionsRolloutConfigProperty"]]:
            '''The rollout configuration for the job.

            This configuration defines the rate at which the job rolls out to the fleet of target devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-jobexecutionsrolloutconfig
            '''
            result = self._values.get("job_executions_rollout_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobExecutionsRolloutConfigProperty"]], result)

        @builtins.property
        def timeout_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobTimeoutConfigProperty"]]:
            '''The timeout configuration for the job.

            This configuration defines the amount of time each device has to complete the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-timeoutconfig
            '''
            result = self._values.get("timeout_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobTimeoutConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentIoTJobConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.DeploymentPoliciesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_update_policy": "componentUpdatePolicy",
            "configuration_validation_policy": "configurationValidationPolicy",
            "failure_handling_policy": "failureHandlingPolicy",
        },
    )
    class DeploymentPoliciesProperty:
        def __init__(
            self,
            *,
            component_update_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.DeploymentComponentUpdatePolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            configuration_validation_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.DeploymentConfigurationValidationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_handling_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about policies that define how a deployment updates components and handles failure.

            :param component_update_policy: The component update policy for the configuration deployment. This policy defines when it's safe to deploy the configuration to devices.
            :param configuration_validation_policy: The configuration validation policy for the configuration deployment. This policy defines how long each component has to validate its configure updates.
            :param failure_handling_policy: The failure handling policy for the configuration deployment. This policy defines what to do if the deployment fails. Default: ``ROLLBACK``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentpolicies.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                deployment_policies_property = greengrassv2.CfnDeployment.DeploymentPoliciesProperty(
                    component_update_policy=greengrassv2.CfnDeployment.DeploymentComponentUpdatePolicyProperty(
                        action="action",
                        timeout_in_seconds=123
                    ),
                    configuration_validation_policy=greengrassv2.CfnDeployment.DeploymentConfigurationValidationPolicyProperty(
                        timeout_in_seconds=123
                    ),
                    failure_handling_policy="failureHandlingPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__afb1f8fb8f75b567210990321e7ca700727bdbe3dc3e20ea8d4230f9ea80bd9a)
                check_type(argname="argument component_update_policy", value=component_update_policy, expected_type=type_hints["component_update_policy"])
                check_type(argname="argument configuration_validation_policy", value=configuration_validation_policy, expected_type=type_hints["configuration_validation_policy"])
                check_type(argname="argument failure_handling_policy", value=failure_handling_policy, expected_type=type_hints["failure_handling_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_update_policy is not None:
                self._values["component_update_policy"] = component_update_policy
            if configuration_validation_policy is not None:
                self._values["configuration_validation_policy"] = configuration_validation_policy
            if failure_handling_policy is not None:
                self._values["failure_handling_policy"] = failure_handling_policy

        @builtins.property
        def component_update_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentComponentUpdatePolicyProperty"]]:
            '''The component update policy for the configuration deployment.

            This policy defines when it's safe to deploy the configuration to devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentpolicies.html#cfn-greengrassv2-deployment-deploymentpolicies-componentupdatepolicy
            '''
            result = self._values.get("component_update_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentComponentUpdatePolicyProperty"]], result)

        @builtins.property
        def configuration_validation_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentConfigurationValidationPolicyProperty"]]:
            '''The configuration validation policy for the configuration deployment.

            This policy defines how long each component has to validate its configure updates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentpolicies.html#cfn-greengrassv2-deployment-deploymentpolicies-configurationvalidationpolicy
            '''
            result = self._values.get("configuration_validation_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DeploymentConfigurationValidationPolicyProperty"]], result)

        @builtins.property
        def failure_handling_policy(self) -> typing.Optional[builtins.str]:
            '''The failure handling policy for the configuration deployment. This policy defines what to do if the deployment fails.

            Default: ``ROLLBACK``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentpolicies.html#cfn-greengrassv2-deployment-deploymentpolicies-failurehandlingpolicy
            '''
            result = self._values.get("failure_handling_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentPoliciesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.IoTJobAbortConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"criteria_list": "criteriaList"},
    )
    class IoTJobAbortConfigProperty:
        def __init__(
            self,
            *,
            criteria_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.IoTJobAbortCriteriaProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Contains a list of criteria that define when and how to cancel a configuration deployment.

            :param criteria_list: The list of criteria that define when and how to cancel the configuration deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                io_tJob_abort_config_property = greengrassv2.CfnDeployment.IoTJobAbortConfigProperty(
                    criteria_list=[greengrassv2.CfnDeployment.IoTJobAbortCriteriaProperty(
                        action="action",
                        failure_type="failureType",
                        min_number_of_executed_things=123,
                        threshold_percentage=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7041ab4c8598b2ddbad72ff782d211d69555393198787d4084f2f81e445ada8c)
                check_type(argname="argument criteria_list", value=criteria_list, expected_type=type_hints["criteria_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "criteria_list": criteria_list,
            }

        @builtins.property
        def criteria_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobAbortCriteriaProperty"]]]:
            '''The list of criteria that define when and how to cancel the configuration deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortconfig.html#cfn-greengrassv2-deployment-iotjobabortconfig-criterialist
            '''
            result = self._values.get("criteria_list")
            assert result is not None, "Required property 'criteria_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobAbortCriteriaProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IoTJobAbortConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.IoTJobAbortCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "failure_type": "failureType",
            "min_number_of_executed_things": "minNumberOfExecutedThings",
            "threshold_percentage": "thresholdPercentage",
        },
    )
    class IoTJobAbortCriteriaProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            failure_type: builtins.str,
            min_number_of_executed_things: jsii.Number,
            threshold_percentage: jsii.Number,
        ) -> None:
            '''Contains criteria that define when and how to cancel a job.

            The deployment stops if the following conditions are true:

            - The number of things that receive the deployment exceeds the ``minNumberOfExecutedThings`` .
            - The percentage of failures with type ``failureType`` exceeds the ``thresholdPercentage`` .

            :param action: The action to perform when the criteria are met.
            :param failure_type: The type of job deployment failure that can cancel a job.
            :param min_number_of_executed_things: The minimum number of things that receive the configuration before the job can cancel.
            :param threshold_percentage: The minimum percentage of ``failureType`` failures that occur before the job can cancel. This parameter supports up to two digits after the decimal (for example, you can specify ``10.9`` or ``10.99`` , but not ``10.999`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                io_tJob_abort_criteria_property = greengrassv2.CfnDeployment.IoTJobAbortCriteriaProperty(
                    action="action",
                    failure_type="failureType",
                    min_number_of_executed_things=123,
                    threshold_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b94ef678c8e5360c99d3f5b82cfa25d5d4194ac6954cbc99f51bad9dcf4105d)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument failure_type", value=failure_type, expected_type=type_hints["failure_type"])
                check_type(argname="argument min_number_of_executed_things", value=min_number_of_executed_things, expected_type=type_hints["min_number_of_executed_things"])
                check_type(argname="argument threshold_percentage", value=threshold_percentage, expected_type=type_hints["threshold_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "failure_type": failure_type,
                "min_number_of_executed_things": min_number_of_executed_things,
                "threshold_percentage": threshold_percentage,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The action to perform when the criteria are met.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html#cfn-greengrassv2-deployment-iotjobabortcriteria-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def failure_type(self) -> builtins.str:
            '''The type of job deployment failure that can cancel a job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html#cfn-greengrassv2-deployment-iotjobabortcriteria-failuretype
            '''
            result = self._values.get("failure_type")
            assert result is not None, "Required property 'failure_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def min_number_of_executed_things(self) -> jsii.Number:
            '''The minimum number of things that receive the configuration before the job can cancel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html#cfn-greengrassv2-deployment-iotjobabortcriteria-minnumberofexecutedthings
            '''
            result = self._values.get("min_number_of_executed_things")
            assert result is not None, "Required property 'min_number_of_executed_things' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def threshold_percentage(self) -> jsii.Number:
            '''The minimum percentage of ``failureType`` failures that occur before the job can cancel.

            This parameter supports up to two digits after the decimal (for example, you can specify ``10.9`` or ``10.99`` , but not ``10.999`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html#cfn-greengrassv2-deployment-iotjobabortcriteria-thresholdpercentage
            '''
            result = self._values.get("threshold_percentage")
            assert result is not None, "Required property 'threshold_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IoTJobAbortCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.IoTJobExecutionsRolloutConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exponential_rate": "exponentialRate",
            "maximum_per_minute": "maximumPerMinute",
        },
    )
    class IoTJobExecutionsRolloutConfigProperty:
        def __init__(
            self,
            *,
            exponential_rate: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.IoTJobExponentialRolloutRateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maximum_per_minute: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about the rollout configuration for a job.

            This configuration defines the rate at which the job deploys a configuration to a fleet of target devices.

            :param exponential_rate: The exponential rate to increase the job rollout rate.
            :param maximum_per_minute: The maximum number of devices that receive a pending job notification, per minute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                # rate_increase_criteria: Any
                
                io_tJob_executions_rollout_config_property = greengrassv2.CfnDeployment.IoTJobExecutionsRolloutConfigProperty(
                    exponential_rate=greengrassv2.CfnDeployment.IoTJobExponentialRolloutRateProperty(
                        base_rate_per_minute=123,
                        increment_factor=123,
                        rate_increase_criteria=rate_increase_criteria
                    ),
                    maximum_per_minute=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e504bac58eb94dea0e5725c8d1878ceefbb281e8d790e9a2fd4d04ad2f1f4333)
                check_type(argname="argument exponential_rate", value=exponential_rate, expected_type=type_hints["exponential_rate"])
                check_type(argname="argument maximum_per_minute", value=maximum_per_minute, expected_type=type_hints["maximum_per_minute"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exponential_rate is not None:
                self._values["exponential_rate"] = exponential_rate
            if maximum_per_minute is not None:
                self._values["maximum_per_minute"] = maximum_per_minute

        @builtins.property
        def exponential_rate(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobExponentialRolloutRateProperty"]]:
            '''The exponential rate to increase the job rollout rate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig.html#cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-exponentialrate
            '''
            result = self._values.get("exponential_rate")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeployment.IoTJobExponentialRolloutRateProperty"]], result)

        @builtins.property
        def maximum_per_minute(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of devices that receive a pending job notification, per minute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig.html#cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-maximumperminute
            '''
            result = self._values.get("maximum_per_minute")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IoTJobExecutionsRolloutConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.IoTJobExponentialRolloutRateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_rate_per_minute": "baseRatePerMinute",
            "increment_factor": "incrementFactor",
            "rate_increase_criteria": "rateIncreaseCriteria",
        },
    )
    class IoTJobExponentialRolloutRateProperty:
        def __init__(
            self,
            *,
            base_rate_per_minute: jsii.Number,
            increment_factor: jsii.Number,
            rate_increase_criteria: typing.Any,
        ) -> None:
            '''Contains information about an exponential rollout rate for a configuration deployment job.

            :param base_rate_per_minute: The minimum number of devices that receive a pending job notification, per minute, when the job starts. This parameter defines the initial rollout rate of the job.
            :param increment_factor: The exponential factor to increase the rollout rate for the job. This parameter supports up to one digit after the decimal (for example, you can specify ``1.5`` , but not ``1.55`` ).
            :param rate_increase_criteria: The criteria to increase the rollout rate for the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                # rate_increase_criteria: Any
                
                io_tJob_exponential_rollout_rate_property = greengrassv2.CfnDeployment.IoTJobExponentialRolloutRateProperty(
                    base_rate_per_minute=123,
                    increment_factor=123,
                    rate_increase_criteria=rate_increase_criteria
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__17de80de656c7b766d33e5ad4e918625197a24e1d115aeec47f1e575e37aebb5)
                check_type(argname="argument base_rate_per_minute", value=base_rate_per_minute, expected_type=type_hints["base_rate_per_minute"])
                check_type(argname="argument increment_factor", value=increment_factor, expected_type=type_hints["increment_factor"])
                check_type(argname="argument rate_increase_criteria", value=rate_increase_criteria, expected_type=type_hints["rate_increase_criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "base_rate_per_minute": base_rate_per_minute,
                "increment_factor": increment_factor,
                "rate_increase_criteria": rate_increase_criteria,
            }

        @builtins.property
        def base_rate_per_minute(self) -> jsii.Number:
            '''The minimum number of devices that receive a pending job notification, per minute, when the job starts.

            This parameter defines the initial rollout rate of the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-baserateperminute
            '''
            result = self._values.get("base_rate_per_minute")
            assert result is not None, "Required property 'base_rate_per_minute' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def increment_factor(self) -> jsii.Number:
            '''The exponential factor to increase the rollout rate for the job.

            This parameter supports up to one digit after the decimal (for example, you can specify ``1.5`` , but not ``1.55`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-incrementfactor
            '''
            result = self._values.get("increment_factor")
            assert result is not None, "Required property 'increment_factor' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rate_increase_criteria(self) -> typing.Any:
            '''The criteria to increase the rollout rate for the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-rateincreasecriteria
            '''
            result = self._values.get("rate_increase_criteria")
            assert result is not None, "Required property 'rate_increase_criteria' is missing"
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IoTJobExponentialRolloutRateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.IoTJobTimeoutConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"in_progress_timeout_in_minutes": "inProgressTimeoutInMinutes"},
    )
    class IoTJobTimeoutConfigProperty:
        def __init__(
            self,
            *,
            in_progress_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about the timeout configuration for a job.

            :param in_progress_timeout_in_minutes: The amount of time, in minutes, that devices have to complete the job. The timer starts when the job status is set to ``IN_PROGRESS`` . If the job status doesn't change to a terminal state before the time expires, then the job status is set to ``TIMED_OUT`` . The timeout interval must be between 1 minute and 7 days (10080 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobtimeoutconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                io_tJob_timeout_config_property = greengrassv2.CfnDeployment.IoTJobTimeoutConfigProperty(
                    in_progress_timeout_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__442f9e24b6b2778d2170d5dc2118941eb426c32282df0fc4bfe4b47b81c56940)
                check_type(argname="argument in_progress_timeout_in_minutes", value=in_progress_timeout_in_minutes, expected_type=type_hints["in_progress_timeout_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if in_progress_timeout_in_minutes is not None:
                self._values["in_progress_timeout_in_minutes"] = in_progress_timeout_in_minutes

        @builtins.property
        def in_progress_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in minutes, that devices have to complete the job.

            The timer starts when the job status is set to ``IN_PROGRESS`` . If the job status doesn't change to a terminal state before the time expires, then the job status is set to ``TIMED_OUT`` .

            The timeout interval must be between 1 minute and 7 days (10080 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobtimeoutconfig.html#cfn-greengrassv2-deployment-iotjobtimeoutconfig-inprogresstimeoutinminutes
            '''
            result = self._values.get("in_progress_timeout_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IoTJobTimeoutConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeployment.SystemResourceLimitsProperty",
        jsii_struct_bases=[],
        name_mapping={"cpus": "cpus", "memory": "memory"},
    )
    class SystemResourceLimitsProperty:
        def __init__(
            self,
            *,
            cpus: typing.Optional[jsii.Number] = None,
            memory: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about system resource limits that the  software applies to a component's processes.

            :param cpus: The maximum amount of CPU time that a component's processes can use on the core device. A core device's total CPU time is equivalent to the device's number of CPU cores. For example, on a core device with 4 CPU cores, you can set this value to 2 to limit the component's processes to 50 percent usage of each CPU core. On a device with 1 CPU core, you can set this value to 0.25 to limit the component's processes to 25 percent usage of the CPU. If you set this value to a number greater than the number of CPU cores, the AWS IoT Greengrass Core software doesn't limit the component's CPU usage.
            :param memory: The maximum amount of RAM, expressed in kilobytes, that a component's processes can use on the core device. For more information, see `Configure system resource limits for components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-system-resource-limits>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-systemresourcelimits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrassv2 as greengrassv2
                
                system_resource_limits_property = greengrassv2.CfnDeployment.SystemResourceLimitsProperty(
                    cpus=123,
                    memory=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__beb6642ef9cd43c09502aafc4577b01875cde60d31da577d2abd28f4feba810e)
                check_type(argname="argument cpus", value=cpus, expected_type=type_hints["cpus"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cpus is not None:
                self._values["cpus"] = cpus
            if memory is not None:
                self._values["memory"] = memory

        @builtins.property
        def cpus(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of CPU time that a component's processes can use on the core device.

            A core device's total CPU time is equivalent to the device's number of CPU cores. For example, on a core device with 4 CPU cores, you can set this value to 2 to limit the component's processes to 50 percent usage of each CPU core. On a device with 1 CPU core, you can set this value to 0.25 to limit the component's processes to 25 percent usage of the CPU. If you set this value to a number greater than the number of CPU cores, the AWS IoT Greengrass Core software doesn't limit the component's CPU usage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-systemresourcelimits.html#cfn-greengrassv2-deployment-systemresourcelimits-cpus
            '''
            result = self._values.get("cpus")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def memory(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of RAM, expressed in kilobytes, that a component's processes can use on the core device.

            For more information, see `Configure system resource limits for components <https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-system-resource-limits>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-systemresourcelimits.html#cfn-greengrassv2-deployment-systemresourcelimits-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SystemResourceLimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrassv2.CfnDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "target_arn": "targetArn",
        "components": "components",
        "deployment_name": "deploymentName",
        "deployment_policies": "deploymentPolicies",
        "iot_job_configuration": "iotJobConfiguration",
        "parent_target_arn": "parentTargetArn",
        "tags": "tags",
    },
)
class CfnDeploymentProps:
    def __init__(
        self,
        *,
        target_arn: builtins.str,
        components: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.ComponentDeploymentSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        deployment_name: typing.Optional[builtins.str] = None,
        deployment_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DeploymentPoliciesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        iot_job_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DeploymentIoTJobConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        parent_target_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeployment``.

        :param target_arn: The ARN of the target AWS IoT thing or thing group.
        :param components: The components to deploy. This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component.
        :param deployment_name: The name of the deployment.
        :param deployment_policies: The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.
        :param iot_job_configuration: The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.
        :param parent_target_arn: The parent deployment's `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ for a subdeployment.
        :param tags: Application-specific metadata to attach to the deployment. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tag your AWS IoT Greengrass Version 2 resources <https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrassv2 as greengrassv2
            
            # rate_increase_criteria: Any
            
            cfn_deployment_props = greengrassv2.CfnDeploymentProps(
                target_arn="targetArn",
            
                # the properties below are optional
                components={
                    "components_key": greengrassv2.CfnDeployment.ComponentDeploymentSpecificationProperty(
                        component_version="componentVersion",
                        configuration_update=greengrassv2.CfnDeployment.ComponentConfigurationUpdateProperty(
                            merge="merge",
                            reset=["reset"]
                        ),
                        run_with=greengrassv2.CfnDeployment.ComponentRunWithProperty(
                            posix_user="posixUser",
                            system_resource_limits=greengrassv2.CfnDeployment.SystemResourceLimitsProperty(
                                cpus=123,
                                memory=123
                            ),
                            windows_user="windowsUser"
                        )
                    )
                },
                deployment_name="deploymentName",
                deployment_policies=greengrassv2.CfnDeployment.DeploymentPoliciesProperty(
                    component_update_policy=greengrassv2.CfnDeployment.DeploymentComponentUpdatePolicyProperty(
                        action="action",
                        timeout_in_seconds=123
                    ),
                    configuration_validation_policy=greengrassv2.CfnDeployment.DeploymentConfigurationValidationPolicyProperty(
                        timeout_in_seconds=123
                    ),
                    failure_handling_policy="failureHandlingPolicy"
                ),
                iot_job_configuration=greengrassv2.CfnDeployment.DeploymentIoTJobConfigurationProperty(
                    abort_config=greengrassv2.CfnDeployment.IoTJobAbortConfigProperty(
                        criteria_list=[greengrassv2.CfnDeployment.IoTJobAbortCriteriaProperty(
                            action="action",
                            failure_type="failureType",
                            min_number_of_executed_things=123,
                            threshold_percentage=123
                        )]
                    ),
                    job_executions_rollout_config=greengrassv2.CfnDeployment.IoTJobExecutionsRolloutConfigProperty(
                        exponential_rate=greengrassv2.CfnDeployment.IoTJobExponentialRolloutRateProperty(
                            base_rate_per_minute=123,
                            increment_factor=123,
                            rate_increase_criteria=rate_increase_criteria
                        ),
                        maximum_per_minute=123
                    ),
                    timeout_config=greengrassv2.CfnDeployment.IoTJobTimeoutConfigProperty(
                        in_progress_timeout_in_minutes=123
                    )
                ),
                parent_target_arn="parentTargetArn",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc578e58fd2afb40d1b3a59c721c6a2a4fc1bd28a9afedcea97a964957c5c5ae)
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument components", value=components, expected_type=type_hints["components"])
            check_type(argname="argument deployment_name", value=deployment_name, expected_type=type_hints["deployment_name"])
            check_type(argname="argument deployment_policies", value=deployment_policies, expected_type=type_hints["deployment_policies"])
            check_type(argname="argument iot_job_configuration", value=iot_job_configuration, expected_type=type_hints["iot_job_configuration"])
            check_type(argname="argument parent_target_arn", value=parent_target_arn, expected_type=type_hints["parent_target_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_arn": target_arn,
        }
        if components is not None:
            self._values["components"] = components
        if deployment_name is not None:
            self._values["deployment_name"] = deployment_name
        if deployment_policies is not None:
            self._values["deployment_policies"] = deployment_policies
        if iot_job_configuration is not None:
            self._values["iot_job_configuration"] = iot_job_configuration
        if parent_target_arn is not None:
            self._values["parent_target_arn"] = parent_target_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The ARN of the target AWS IoT thing or thing group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def components(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDeployment.ComponentDeploymentSpecificationProperty]]]]:
        '''The components to deploy.

        This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-components
        '''
        result = self._values.get("components")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDeployment.ComponentDeploymentSpecificationProperty]]]], result)

    @builtins.property
    def deployment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-deploymentname
        '''
        result = self._values.get("deployment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeployment.DeploymentPoliciesProperty]]:
        '''The deployment policies for the deployment.

        These policies define how the deployment updates components and handles failure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-deploymentpolicies
        '''
        result = self._values.get("deployment_policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeployment.DeploymentPoliciesProperty]], result)

    @builtins.property
    def iot_job_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeployment.DeploymentIoTJobConfigurationProperty]]:
        '''The job configuration for the deployment configuration.

        The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-iotjobconfiguration
        '''
        result = self._values.get("iot_job_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeployment.DeploymentIoTJobConfigurationProperty]], result)

    @builtins.property
    def parent_target_arn(self) -> typing.Optional[builtins.str]:
        '''The parent deployment's `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ for a subdeployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-parenttargetarn
        '''
        result = self._values.get("parent_target_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Application-specific metadata to attach to the deployment.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tag your AWS IoT Greengrass Version 2 resources <https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html>`_ in the *AWS IoT Greengrass V2 Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComponentVersion",
    "CfnComponentVersionProps",
    "CfnDeployment",
    "CfnDeploymentProps",
]

publication.publish()

def _typecheckingstub__f5d46224f527e073fe7f6fbe54ccaca3f0045fcc0ade3462681ae8b0575c59e0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    inline_recipe: typing.Optional[builtins.str] = None,
    lambda_function: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaFunctionRecipeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b4437bb59606a2a9dbc98b6d542a546264b4ce6dc5594c04c8503a477b837c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddcadfc186b2781e90bf0c28ccaed5edc30f8c0c7447e9310fac34a6349fcda8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72eb28bfc29eebefc2ec5d2aace9f7b9a334fa75c8691abf39303421830fabd7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ccfa77f00c9c04773ae0643b7f2f0b369127a28b9747cbe78bfe426dc32f46(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComponentVersion.LambdaFunctionRecipeSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0267e3a5b2b19b25e52f0bee8bba8f4880b864731b0138cdd45e5b72ec1bc7a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c678ca853046a4f9a77f7c2dd92c2ab09d84c106fa6e8f450dca99e2f6edbf9(
    *,
    dependency_type: typing.Optional[builtins.str] = None,
    version_requirement: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868d55cb9cd63d9081a8bb6f44c49ad0558ce766d47dc9e602b30fa6d7823104(
    *,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa404e4c8d222fafce82a4df5f456d4c0ca9f1f90cc0610f63526bc52a42562(
    *,
    devices: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaDeviceMountProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    memory_size_in_kb: typing.Optional[jsii.Number] = None,
    mount_ro_sysfs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    volumes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaVolumeMountProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff1c88d4c72688121e8d02d23f54e807be84dc41e8cc06f915402a59c07ab80(
    *,
    add_group_owner: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    path: typing.Optional[builtins.str] = None,
    permission: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2bdb1aa21a11fead4d3211e8427d3370a925fda227540a812604c8717631e5b(
    *,
    topic: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000b16ea913d1bbaf1c4a8d0fc0503b8b2497e7799ae2cf1cbbf4d109ec5d229(
    *,
    environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    event_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaEventSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    exec_args: typing.Optional[typing.Sequence[builtins.str]] = None,
    input_payload_encoding_type: typing.Optional[builtins.str] = None,
    linux_process_params: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaLinuxProcessParamsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_idle_time_in_seconds: typing.Optional[jsii.Number] = None,
    max_instances_count: typing.Optional[jsii.Number] = None,
    max_queue_size: typing.Optional[jsii.Number] = None,
    pinned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    status_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c65d39b535672032cfb004ee7b6c48a4d582a473117af5905209bcaa7d8a97c(
    *,
    component_dependencies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.ComponentDependencyRequirementProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    component_lambda_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaExecutionParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    component_name: typing.Optional[builtins.str] = None,
    component_platforms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.ComponentPlatformProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    component_version: typing.Optional[builtins.str] = None,
    lambda_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__756fcd867eac20b9fe5f8b006e060eeede11829ac7bf7e6785ed2fe382e6e614(
    *,
    container_params: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaContainerParamsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    isolation_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bbd7759f413868e7d380d01e235f94a2424b3a59ed198c9bb3e2b55af65a835(
    *,
    add_group_owner: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    destination_path: typing.Optional[builtins.str] = None,
    permission: typing.Optional[builtins.str] = None,
    source_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26145a7c787773c5d69bceaa1a73ff40d6d4fa0dcdb0fa8cda22627f2fbac7e4(
    *,
    inline_recipe: typing.Optional[builtins.str] = None,
    lambda_function: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComponentVersion.LambdaFunctionRecipeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0099ed4b9647f1e31fee9e80f3453ed07e5b916846f269d15cb7aa59c5b0f80(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    target_arn: builtins.str,
    components: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.ComponentDeploymentSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    deployment_name: typing.Optional[builtins.str] = None,
    deployment_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DeploymentPoliciesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_job_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DeploymentIoTJobConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parent_target_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__524ad5f78c9f968fbfe224a67e6b8648f6b2153ad09d18d40f9d97b0df1c6779(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27081f49a96fd9b6be8c82348527e349696fb1b86cd8968bf684a0fc6ea3c51d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9aca642a78f9815025a310924e8d40466c2d36e58d9487bf411cd9087d6199(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1eb46eb9aeb60a7ab5ad1127528e8840b937def6fe38be8c8a850d599c3f07d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDeployment.ComponentDeploymentSpecificationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8069055a5f48e98559e413f59fb8f8c7f772787bd94ff1febc911991c38db58e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bef596cb6c3ad06c55fcfb702aa42ec9c1d3b9107e9691ab1154ce9d7b05ae46(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeployment.DeploymentPoliciesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879253a12cc1ff77fae7f0478b8930b3954ee32057720a99435120f7439281a2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeployment.DeploymentIoTJobConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4d5673bcfb7eecac8ede7a8e39c18587c0eb66717f03e340c019ebd933adf91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79f5864d30fae319b83ae457690221fe12d396b95ce2c98c3d893526c3c60d8(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__387f0b8380336ac206b9c77595b26aa518c606b2c12077c051460b728e9efb34(
    *,
    merge: typing.Optional[builtins.str] = None,
    reset: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2fd4248871e67a3e8bbacfa9fd79ab295c1c5403da8ad0bb4d304b1e8aa29a8(
    *,
    component_version: typing.Optional[builtins.str] = None,
    configuration_update: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.ComponentConfigurationUpdateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    run_with: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.ComponentRunWithProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b36ba95075fd81f7a1b0019f2c8e10a617095cd1d4c5cb46b3b30152cd4cc951(
    *,
    posix_user: typing.Optional[builtins.str] = None,
    system_resource_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.SystemResourceLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    windows_user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5375829a3f60c816195dbae5f8543c8cc49cbb3fcde08447d27deea63f4c6565(
    *,
    action: typing.Optional[builtins.str] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55dea1728923b695ec20c5dee3a959b4cd22fc22ddd90735e6442720f87e24fd(
    *,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__539a1a07fe3406166e26105a9b53bdea60ff75a1286fede7d70c48a6d080c3fd(
    *,
    abort_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.IoTJobAbortConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_executions_rollout_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.IoTJobExecutionsRolloutConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.IoTJobTimeoutConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb1f8fb8f75b567210990321e7ca700727bdbe3dc3e20ea8d4230f9ea80bd9a(
    *,
    component_update_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DeploymentComponentUpdatePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    configuration_validation_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DeploymentConfigurationValidationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_handling_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7041ab4c8598b2ddbad72ff782d211d69555393198787d4084f2f81e445ada8c(
    *,
    criteria_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.IoTJobAbortCriteriaProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b94ef678c8e5360c99d3f5b82cfa25d5d4194ac6954cbc99f51bad9dcf4105d(
    *,
    action: builtins.str,
    failure_type: builtins.str,
    min_number_of_executed_things: jsii.Number,
    threshold_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e504bac58eb94dea0e5725c8d1878ceefbb281e8d790e9a2fd4d04ad2f1f4333(
    *,
    exponential_rate: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.IoTJobExponentialRolloutRateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_per_minute: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17de80de656c7b766d33e5ad4e918625197a24e1d115aeec47f1e575e37aebb5(
    *,
    base_rate_per_minute: jsii.Number,
    increment_factor: jsii.Number,
    rate_increase_criteria: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442f9e24b6b2778d2170d5dc2118941eb426c32282df0fc4bfe4b47b81c56940(
    *,
    in_progress_timeout_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb6642ef9cd43c09502aafc4577b01875cde60d31da577d2abd28f4feba810e(
    *,
    cpus: typing.Optional[jsii.Number] = None,
    memory: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc578e58fd2afb40d1b3a59c721c6a2a4fc1bd28a9afedcea97a964957c5c5ae(
    *,
    target_arn: builtins.str,
    components: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.ComponentDeploymentSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    deployment_name: typing.Optional[builtins.str] = None,
    deployment_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DeploymentPoliciesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_job_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DeploymentIoTJobConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parent_target_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
